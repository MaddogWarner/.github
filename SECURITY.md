# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest release | :white_check_mark: |
| Older releases | :x: |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Use GitHub's private vulnerability reporting:

1. Go to the **Security** tab of the affected repository
2. Click **Report a vulnerability**
3. Fill in the details — include reproduction steps, impact assessment, and any suggested fix

Alternatively, email **security@maddogwarner.com** for coordinated disclosure.

### What to include

- Description of the vulnerability and affected component
- Steps to reproduce (proof-of-concept if applicable)
- Potential impact
- Any suggested mitigation or fix

### Response timeline

| Stage | Target |
|-------|--------|
| Acknowledgement | Within 48 hours |
| Initial assessment | Within 5 business days |
| Resolution or workaround | Within 30 days for critical, 90 days for others |

We follow responsible disclosure principles. We will credit reporters in release notes unless you prefer to remain anonymous.

## Security Practices

These projects implement controls aligned with the [ASD Essential Eight](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight) and follow OWASP secure development guidelines. CI pipelines run automated SAST, dependency auditing, and secrets scanning on every pull request.
