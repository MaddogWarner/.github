# Contributing

Thanks for your interest in contributing. These guidelines apply across all MaddogWarner repositories.

## Getting started

1. **Fork** the repository and create your branch from `main` (or `master` where applicable)
2. Branch naming: `feat/short-description`, `fix/short-description`, `chore/short-description`
3. Make your changes — keep commits focused and atomic
4. Ensure CI passes locally before pushing
5. Open a **pull request** against the default branch

## Commit style

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add support for custom DNS upstream
fix: resolve crash on empty config file
chore: bump dependencies
docs: update installation instructions
```

## Pull requests

- Fill in the PR template — don't delete sections
- Link related issues with `Closes #123`
- Keep PRs small and focused — one concern per PR
- All CI checks must pass before merge

## Security issues

**Do not open public issues for security vulnerabilities.** See [SECURITY.md](SECURITY.md) for the responsible disclosure process.

## Code style

Match the existing style of the file you're editing. Each repo has its own linting config — run the linter before submitting.

## Licence

By contributing, you agree your contributions are licensed under the same licence as the project (see `LICENSE` in each repo).
