"""
Summarizer Agent - Generates executive summaries of vulnerability data using the Claude API.

Accepts output from cve_monitor and cisa_tracker and produces human-readable
summaries suitable for executive audiences.
"""

import json
import logging
import os
import re
from typing import Optional

import anthropic
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

MODEL = "claude-sonnet-4-20250514"

SYSTEM_PROMPT = (
    "You are a cybersecurity analyst writing reports for executive audiences. "
    "You will receive vulnerability data and must produce a structured JSON response "
    "with exactly these three keys:\n"
    "- executive_summary: plain-language overview in UNDER 150 WORDS\n"
    "- action_items: a list of EXACTLY 5 strings, each ONE SENTENCE, ordered by priority "
    "(most urgent first)\n"
    "- risk_narrative: threat landscape and business risk description in UNDER 150 WORDS\n\n"
    "STRICT RULES:\n"
    "1. Return ONLY valid JSON — no markdown, no code fences, no preamble, no trailing text.\n"
    "2. The entire response must be a single JSON object starting with { and ending with }.\n"
    "3. Keep all text fields short to avoid truncation.\n"
    "4. action_items must contain exactly 5 elements — no more, no fewer."
)


def format_vulnerability_data(data: dict) -> str:
    """
    Format a vulnerability data dict into a readable prompt string for Claude.

    Args:
        data: Dict with keys high_severity_cves, new_kev_entries, monitored_hits

    Returns:
        Formatted multi-line string summarising the vulnerability data
    """
    high_severity_cves = data.get("high_severity_cves", [])
    new_kev_entries = data.get("new_kev_entries", [])
    monitored_hits = data.get("monitored_hits", [])

    lines = []

    lines.append(f"HIGH SEVERITY CVEs ({len(high_severity_cves)} total):")
    for cve in high_severity_cves[:10]:
        lines.append(
            f"  - {cve.get('cve_id', 'Unknown')}: "
            f"CVSS {cve.get('cvss_score', 'N/A')} | "
            f"{cve.get('description', '')[:150]}"
        )

    lines.append(f"\nNEW CISA KEV ENTRIES ({len(new_kev_entries)} added in last 7 days):")
    for entry in new_kev_entries[:5]:
        lines.append(
            f"  - {entry.get('cveID', 'Unknown')}: "
            f"{entry.get('vendorProject', '')} {entry.get('product', '')} | "
            f"Added: {entry.get('dateAdded', 'Unknown')}"
        )

    lines.append(f"\nMONITORED CVEs FOUND IN KEV CATALOG ({len(monitored_hits)} matches):")
    if monitored_hits:
        for hit in monitored_hits:
            lines.append(
                f"  - {hit.get('cveID', 'Unknown')}: "
                f"{hit.get('vulnerabilityName', '')} | "
                f"Due: {hit.get('dueDate', 'Unknown')}"
            )
    else:
        lines.append("  (none)")

    return "\n".join(lines)


_SAFE_DEFAULT = {
    "executive_summary": "Summary unavailable due to a parsing error.",
    "action_items": [
        "Summary unavailable — review raw vulnerability data manually.",
        "Summary unavailable",
        "Summary unavailable",
        "Summary unavailable",
        "Summary unavailable",
    ],
    "risk_narrative": "Summary unavailable due to a parsing error.",
}


def _try_loads(text: str) -> Optional[dict]:
    """Return parsed dict on success, None on failure."""
    try:
        return json.loads(text)
    except (json.JSONDecodeError, ValueError):
        return None


def _repair_truncated_json(text: str) -> Optional[dict]:
    """Try to close a truncated JSON object by working back from the last quote."""
    last_quote = text.rfind('"')
    if last_quote < 0:
        return None
    fragment = text[: last_quote + 1]
    for closing in ("}", '"}', '"]}', '", "action_items": [], "risk_narrative": "Unavailable"}'):
        result = _try_loads(fragment + closing)
        if result is not None:
            return result
    return None


def parse_summary_response(response_text: str) -> dict:
    """
    Parse the JSON response from Claude into the expected dict structure.

    Attempts four strategies in order:
      1. Standard json.loads()
      2. Regex extraction of the outermost { } block
      3. Repair of a truncated JSON string
      4. Safe default dict so the pipeline never fully fails

    Args:
        response_text: Raw text returned by the Claude API

    Returns:
        Dict with keys: executive_summary, action_items, risk_narrative
    """
    text = response_text.strip()

    # Stage 1 — standard parse
    result = _try_loads(text)

    # Stage 2 — extract JSON block via regex
    if result is None:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            result = _try_loads(match.group())
            if result is not None:
                logger.warning("Used regex extraction to recover JSON from Claude response")

    # Stage 3 — repair truncated JSON
    if result is None:
        result = _repair_truncated_json(text)
        if result is not None:
            logger.warning("Used truncation repair to recover JSON from Claude response")

    # Stage 4 — safe default so the pipeline never hard-fails
    if result is None:
        logger.error(
            "All JSON parse attempts failed; returning default summary. "
            "Response excerpt: %s",
            text[:300],
        )
        return dict(_SAFE_DEFAULT)

    required_keys = {"executive_summary", "action_items", "risk_narrative"}
    missing = required_keys - set(result.keys())
    if missing:
        logger.warning("Claude response missing keys %s; filling with defaults", missing)
        for key in missing:
            result[key] = _SAFE_DEFAULT[key]

    return {
        "executive_summary": str(result["executive_summary"]),
        "action_items": list(result["action_items"]),
        "risk_narrative": str(result["risk_narrative"]),
    }


def generate_summary(vulnerability_data: dict) -> dict:
    """
    Generate an executive vulnerability summary using the Claude API.

    Args:
        vulnerability_data: Dict with keys:
          - high_severity_cves: list of CVE dicts from cve_monitor
          - new_kev_entries: list of KEV entry dicts from cisa_tracker
          - monitored_hits: list of KEV entries matching watched CVEs

    Returns:
        Dict with keys:
          - executive_summary: plain-language 3-4 sentence overview
          - action_items: list of 5 prioritised remediation actions
          - risk_narrative: 2-3 paragraph threat landscape description

    Raises:
        anthropic.APIError: If the Claude API call fails
        ValueError: If the API response cannot be parsed into the expected structure
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    client = anthropic.Anthropic(api_key=api_key)

    formatted = format_vulnerability_data(vulnerability_data)
    logger.info(
        "Generating summary for %d CVEs, %d new KEV entries, %d monitored hits",
        len(vulnerability_data.get("high_severity_cves", [])),
        len(vulnerability_data.get("new_kev_entries", [])),
        len(vulnerability_data.get("monitored_hits", [])),
    )

    response = client.messages.create(
        model=MODEL,
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": (
                    "Analyze the following vulnerability data and produce the "
                    "structured JSON report:\n\n" + formatted
                ),
            }
        ],
    )

    response_text = next(
        (block.text for block in response.content if block.type == "text"), ""
    )

    logger.info("Successfully received summary from Claude API")
    return parse_summary_response(response_text)


def main() -> None:
    """Entry point — generates a summary using synthetic vulnerability data."""
    sample_data = {
        "high_severity_cves": [
            {
                "cve_id": "CVE-2021-44228",
                "description": (
                    "Apache Log4j2 remote code execution vulnerability via JNDI lookup "
                    "in log messages. Affects Log4j2 versions 2.0-beta9 through 2.14.1."
                ),
                "cvss_score": 10.0,
                "published_date": "2021-12-10T00:00:00.000",
            },
            {
                "cve_id": "CVE-2021-26855",
                "description": (
                    "Microsoft Exchange Server server-side request forgery vulnerability "
                    "allowing unauthenticated remote code execution."
                ),
                "cvss_score": 9.8,
                "published_date": "2021-03-02T00:00:00.000",
            },
            {
                "cve_id": "CVE-2023-44487",
                "description": (
                    "HTTP/2 Rapid Reset attack enabling denial-of-service against web "
                    "servers supporting HTTP/2."
                ),
                "cvss_score": 7.5,
                "published_date": "2023-10-10T00:00:00.000",
            },
        ],
        "new_kev_entries": [
            {
                "cveID": "CVE-2024-21762",
                "vendorProject": "Fortinet",
                "product": "FortiOS",
                "vulnerabilityName": "Fortinet FortiOS Out-of-Bound Write Vulnerability",
                "dateAdded": "2024-02-09",
                "dueDate": "2024-02-16",
                "knownRansomwareCampaignUse": "Known",
            },
            {
                "cveID": "CVE-2024-1709",
                "vendorProject": "ConnectWise",
                "product": "ScreenConnect",
                "vulnerabilityName": "ConnectWise ScreenConnect Authentication Bypass",
                "dateAdded": "2024-02-22",
                "dueDate": "2024-02-29",
                "knownRansomwareCampaignUse": "Known",
            },
        ],
        "monitored_hits": [
            {
                "cveID": "CVE-2021-44228",
                "vendorProject": "Apache",
                "product": "Log4j2",
                "vulnerabilityName": "Apache Log4j2 Remote Code Execution Vulnerability",
                "dateAdded": "2021-12-10",
                "dueDate": "2021-12-24",
                "knownRansomwareCampaignUse": "Known",
            },
        ],
    }

    try:
        result = generate_summary(sample_data)

        print("\nVulnerability Intelligence Summary")
        print("=" * 80)

        print("\nEXECUTIVE SUMMARY")
        print("-" * 80)
        print(result["executive_summary"])

        print("\nPRIORITIZED ACTION ITEMS")
        print("-" * 80)
        for i, item in enumerate(result["action_items"], 1):
            print(f"{i}. {item}")

        print("\nRISK NARRATIVE")
        print("-" * 80)
        print(result["risk_narrative"])

    except anthropic.APIError as e:
        logger.error("Claude API error: %s", e)
        raise
    except ValueError as e:
        logger.error("Failed to parse Claude response: %s", e)
        raise


if __name__ == "__main__":
    main()
