# DevOps Assignment 9: DevSecOps Fundamentals

Student: 劉芳瑜 (B11309036)

This repo adds lightweight security checks to the A8 OpenTelemetry code.

| Grade | Check | Where |
|---|---|---|
| A | Linting: flake8 + flake8-bandit, run on every push | `.github/workflows/lint.yml` |
| E | SCA: Dependabot alerts, security updates, version updates | `.github/dependabot.yml` |
| O | SAST: CodeQL code scanning (`security-extended`) + hardened workflows (actions pinned to commit SHAs, least-privilege `permissions`) | `.github/workflows/codeql.yml` |

| Path | What it is |
|---|---|
| `src/` | A8 Python code (`task1`–`task3`) plus `demo_security.py` |
| `requirements.txt` | Real dependencies (OpenTelemetry 1.45.2) |
| `demo-vulnerable/` | **Demo only.** Old packages with known CVEs and a vulnerable Flask app, so Dependabot and CodeQL have findings to show. Never install, run or deploy it. |

## Run the linter locally (PowerShell)

```powershell
py -m pip install flake8 flake8-bandit
py -m flake8 src/ --count --statistics
```

No real secrets are committed; `DB_PASSWORD` comes from an environment variable.
