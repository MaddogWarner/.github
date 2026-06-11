# MaddogWarner

IT professional, homelab operator, and security practitioner based in Australia.

Projects span home automation (Homebridge/ESPHome), self-hosted infrastructure, security tooling, and ASD Essential Eight compliance.

## Security Baseline Status

| Repository | Branch Protection | Dependabot | Secret Scanning | Security Workflows | SECURITY.md |
|---|:---:|:---:|:---:|:---:|:---:|
| [adguard-sync-mdw](https://github.com/MaddogWarner/adguard-sync-mdw) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [homebridge-esphome-ts-mdw](https://github.com/MaddogWarner/homebridge-esphome-ts-mdw) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [MDW-Agents-Setup](https://github.com/MaddogWarner/MDW-Agents-Setup) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [stake-selfhost-finance-dashboard](https://github.com/MaddogWarner/stake-selfhost-finance-dashboard) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [maddogwarnercom](https://github.com/MaddogWarner/maddogwarnercom) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [E8-Knowledgebase-Web](https://github.com/MaddogWarner/E8-Knowledgebase-Web) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [unifi-dashboard](https://github.com/MaddogWarner/unifi-dashboard) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [e8-hardening-audit-policy-compliance-checker](https://github.com/MaddogWarner/e8-hardening-audit-policy-compliance-checker) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [homebridge-tp-link-powerline-mdw](https://github.com/MaddogWarner/homebridge-tp-link-powerline-mdw) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [homebridge-plugin-withings-sleep-MDW](https://github.com/MaddogWarner/homebridge-plugin-withings-sleep-MDW) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [homebridge-philips-air-purifier-complete](https://github.com/MaddogWarner/homebridge-philips-air-purifier-complete) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [essential8-kb-ios](https://github.com/MaddogWarner/essential8-kb-ios) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [homebridge-philips-air-purifier](https://github.com/MaddogWarner/homebridge-philips-air-purifier) | ✅ | ✅ | ✅ | ✅ | ✅ |

> Last updated: 11/06/2026 — Controls applied via automated security baseline.

## Security Approach

All repositories implement:
- **Branch protection** — PRs required, CI must pass, linear history enforced
- **Dependabot** — weekly dependency updates with auto-merge for patch releases
- **Secret scanning** — push protection enabled, blocks credential commits
- **SAST** — Semgrep (Python/TypeScript/JS) or CodeQL (TypeScript) on every PR
- **Dependency auditing** — pip-audit / npm audit on every PR
- **Container scanning** — Trivy on Docker-based repos

Security practices align with the [ASD Essential Eight](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight).
