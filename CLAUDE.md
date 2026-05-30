# Vulnerability Agent Project

## Purpose
Learning AI agent development using public vulnerability data.
NO company data. NO proprietary systems.

## Stack
- Language: Python 3.11+
- LLM: Claude API (claude-sonnet-4-20250514)
- Data Sources: NVD API, CISA KEV, MITRE ATT&CK
- Output: Markdown reports, CSV, HTML

## Project Structure
- agents/        → individual agent scripts
- data/          → synthetic or public data only
- outputs/       → generated reports
- tests/         → one test file per agent

## Agents Being Built
1. cve_monitor.py     — fetches daily CVEs from NVD API
2. cisa_tracker.py    — tracks CISA KEV catalog additions
3. summarizer.py      — Claude API summarization layer
4. orchestrator.py    — chains all agents together

## Rules
- Public/synthetic data only
- All secrets via .env, never hardcoded
- Tests required for every agent
- Outputs go to /outputs/reports/
