"""Exercise the workflow's actual shell policy without enabling any merges."""

import itertools
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

WORKFLOW = (
    Path(__file__).resolve().parents[1]
    / ".github/workflows/reusable-dependabot-automerge.yml"
)
DENYLIST = [
    "bcrypt",
    "bcryptjs",
    "cryptography",
    "pyopenssl",
    "jwcrypto",
    "argon2",
    "argon2-cffi",
    "scrypt",
    "tweetnacl",
    "libsodium-wrappers",
    "node-forge",
    "jsonwebtoken",
    "jose",
    "node-jose",
    "python-jose",
    "pyjwt",
    "passlib",
    "authlib",
    "oauthlib",
    "requests-oauthlib",
    "certifi",
    "fast-uri",
    "ip",
    "ip-address",
]


def policy_script() -> str:
    text = WORKFLOW.read_text()
    body = text.split("        run: |\n", 1)[1].split(
        "\n      - name: Enable auto-merge", 1
    )[0]
    return "\n".join(line.removeprefix("          ") for line in body.splitlines())


class PolicyTests(unittest.TestCase):
    def decision(
        self,
        update: str = "minor",
        scope: str = "direct:production",
        names: str = "axios",
        advisory: str = "",
    ) -> str:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "output"
            env = dict(
                os.environ,
                UPDATE_TYPE=f"version-update:semver-{update}",
                DEP_TYPE=scope,
                DEP_NAMES=names,
                GHSA_ID=advisory,
                GITHUB_OUTPUT=str(output),
                GITHUB_STEP_SUMMARY=str(Path(directory) / "summary"),
            )
            subprocess.run(
                ["bash", "-c", policy_script()],
                env=env,
                check=True,
                capture_output=True,
            )
            return output.read_text().strip()

    def test_allow_tiers(self) -> None:
        for args in [
            {"update": "patch"},
            {"scope": "direct:development"},
            {"advisory": "GHSA-gcfj-64vw-6mp9"},
        ]:
            with self.subTest(args=args):
                self.assertEqual(self.decision(**args), "decision=yes")
        self.assertEqual(self.decision(), "decision=no")

    def test_missing_names_cannot_allow_advisory_minor(self) -> None:
        self.assertEqual(
            self.decision(names="", advisory="GHSA-example"), "decision=no"
        )

    def test_major_always_denied(self) -> None:
        for scope, names, advisory in itertools.product(
            ["direct:production", "direct:development", "indirect"],
            ["", "axios", "bcrypt", "axios,bcrypt"],
            ["", "GHSA-example"],
        ):
            with self.subTest(scope=scope, names=names, advisory=advisory):
                self.assertEqual(
                    self.decision("major", scope, names, advisory), "decision=no"
                )

    def test_every_runtime_denylist_entry(self) -> None:
        for name, update, scope in itertools.product(
            DENYLIST, ["patch", "minor"], ["direct:production", "indirect"]
        ):
            with self.subTest(name=name, update=update, scope=scope):
                self.assertEqual(
                    self.decision(
                        update, scope, f"axios, {name.upper()} ", "GHSA-example"
                    ),
                    "decision=no",
                )

    def test_groups_and_exact_names(self) -> None:
        for names in ["bcrypt,axios", "axios,bcrypt", "axios,bcrypt,lodash"]:
            self.assertEqual(
                self.decision(names=names, advisory="GHSA-example"), "decision=no"
            )
        self.assertEqual(
            self.decision(names="bcrypt-wrapper", advisory="GHSA-example"),
            "decision=yes",
        )
        self.assertEqual(
            self.decision(scope="direct:development", names="bcrypt"), "decision=yes"
        )

    def test_defined_empty_metadata(self) -> None:
        self.assertEqual(
            self.decision(update="", scope="", names="", advisory=""), "decision=no"
        )
        self.assertEqual(self.decision(update="patch", names=""), "decision=yes")

    def test_unset_metadata_fails_closed(self) -> None:
        env = {
            key: value
            for key, value in os.environ.items()
            if key not in {"UPDATE_TYPE", "DEP_TYPE", "DEP_NAMES", "GHSA_ID"}
        }
        result = subprocess.run(
            ["bash", "-c", policy_script()], env=env, capture_output=True, check=False
        )
        self.assertNotEqual(result.returncode, 0)

    def test_permissions_and_pin_unchanged(self) -> None:
        text = WORKFLOW.read_text()
        self.assertIn("  workflow_call: {}", text)
        self.assertIn("permissions:\n  contents: read", text)
        self.assertIn("    if: github.actor == 'dependabot[bot]'", text)
        self.assertIn("      contents: write\n      pull-requests: write", text)
        self.assertIn(
            "dependabot/fetch-metadata@25dd0e34f4fe68f24cc83900b1fe3fe149efef98", text
        )


if __name__ == "__main__":
    unittest.main()
