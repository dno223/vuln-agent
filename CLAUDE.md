# Vulnerability Agent Project

## Purpose
Learning AI agent development using public vulnerability data.
NO company data. NO proprietary systems.

## Stack
- Language: Python 3.11+
- LLM: Claude API (claude-sonnet-4-20250514)
- Data Sources: NVD API, CISA KEV, MITRE ATT&CK
- Output: Markdown reports, CSV, HTML
- CI/CD: GitHub Actions (daily scheduled runs)
- Dashboard: GitHub Pages (live)
- Alerts: Email delivery via HTML reports

## Project Structure
- agents/        → individual agent scripts
- data/          → synthetic or public data only
- outputs/       → generated reports
- tests/         → one test file per agent
- .github/       → GitHub Actions workflows

## Agents (all built and tested)
1. cve_monitor.py     — fetches daily CVEs from NVD API
2. cisa_tracker.py    — tracks CISA KEV catalog additions
3. summarizer.py      — Claude API summarization layer
4. orchestrator.py    — chains all agents together
5. dashboard.py       — generates GitHub Pages HTML dashboard
6. email_alert.py     — sends HTML vulnerability reports via email

## Infrastructure
- GitHub Actions: daily workflow triggers orchestrator, commits reports, deploys dashboard
- GitHub Pages: live vulnerability dashboard auto-updated on each run
- Email alerts: HTML report delivery to configured recipients

## Rules
- Public/synthetic data only
- All secrets via .env, never hardcoded
- Tests required for every agent
- Outputs go to /outputs/reports/

## Next Session Focus
1. Security by design audit — Phase 1-4
2. CVE trending analysis
3. Asset cross-reference feature
