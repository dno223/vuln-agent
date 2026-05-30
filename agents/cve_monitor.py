"""
CVE Monitor Agent - Fetches daily CVEs from NVD API.

This agent queries the NVD (National Vulnerability Database) API
to retrieve CVEs published in the last 24 hours and filters them
by CVSS score.
"""

import logging
import os
from datetime import datetime, timedelta, timezone
from typing import Optional

import requests
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
DEFAULT_CVSS_THRESHOLD = 7.0


def get_nvd_api_key() -> Optional[str]:
    """Retrieve NVD API key from environment variables."""
    return os.getenv("NVD_API_KEY")


def fetch_cves(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    api_key: Optional[str] = None,
) -> list[dict]:
    """
    Fetch CVEs from NVD API within the specified date range.

    Args:
        start_date: Start of the date range (defaults to 24 hours ago)
        end_date: End of the date range (defaults to now)
        api_key: NVD API key for authentication (optional but recommended)

    Returns:
        Raw list of CVE items from the NVD API response

    Raises:
        requests.RequestException: If the API request fails
    """
    if end_date is None:
        end_date = datetime.now(timezone.utc)
    if start_date is None:
        start_date = end_date - timedelta(hours=24)

    params = {
        "pubStartDate": start_date.strftime("%Y-%m-%dT%H:%M:%S.000"),
        "pubEndDate": end_date.strftime("%Y-%m-%dT%H:%M:%S.000"),
    }

    headers = {}
    if api_key:
        headers["apiKey"] = api_key

    logger.info(f"Fetching CVEs from {start_date} to {end_date}")

    response = requests.get(NVD_API_URL, params=params, headers=headers, timeout=30)
    response.raise_for_status()

    data = response.json()
    vulnerabilities = data.get("vulnerabilities", [])
    logger.info(f"Retrieved {len(vulnerabilities)} CVEs from NVD API")

    return vulnerabilities


def extract_cvss_score(cve_item: dict) -> Optional[float]:
    """
    Extract the highest CVSS score from a CVE item.

    Checks CVSS v3.1, v3.0, and v2.0 metrics in order of preference.

    Args:
        cve_item: A single CVE item from the NVD API response

    Returns:
        The highest CVSS base score found, or None if no score available
    """
    cve = cve_item.get("cve", {})
    metrics = cve.get("metrics", {})

    # Check CVSS v3.1 first
    cvss_v31 = metrics.get("cvssMetricV31", [])
    if cvss_v31:
        return cvss_v31[0].get("cvssData", {}).get("baseScore")

    # Check CVSS v3.0
    cvss_v30 = metrics.get("cvssMetricV30", [])
    if cvss_v30:
        return cvss_v30[0].get("cvssData", {}).get("baseScore")

    # Check CVSS v2.0
    cvss_v2 = metrics.get("cvssMetricV2", [])
    if cvss_v2:
        return cvss_v2[0].get("cvssData", {}).get("baseScore")

    return None


def extract_description(cve_item: dict) -> str:
    """
    Extract the English description from a CVE item.

    Args:
        cve_item: A single CVE item from the NVD API response

    Returns:
        The English description or a placeholder if not found
    """
    cve = cve_item.get("cve", {})
    descriptions = cve.get("descriptions", [])

    for desc in descriptions:
        if desc.get("lang") == "en":
            return desc.get("value", "No description available")

    return "No description available"


def filter_and_format_cves(
    vulnerabilities: list[dict],
    cvss_threshold: float = DEFAULT_CVSS_THRESHOLD,
) -> list[dict]:
    """
    Filter CVEs by CVSS score and format them into a clean structure.

    Args:
        vulnerabilities: Raw list of CVE items from NVD API
        cvss_threshold: Minimum CVSS score to include (default: 7.0)

    Returns:
        List of dicts with: cve_id, description, cvss_score, published_date
    """
    results = []

    for vuln in vulnerabilities:
        cvss_score = extract_cvss_score(vuln)

        if cvss_score is None or cvss_score < cvss_threshold:
            continue

        cve = vuln.get("cve", {})
        cve_id = cve.get("id", "Unknown")
        published_date = cve.get("published", "Unknown")
        description = extract_description(vuln)

        results.append(
            {
                "cve_id": cve_id,
                "description": description,
                "cvss_score": cvss_score,
                "published_date": published_date,
            }
        )

    logger.info(
        f"Filtered to {len(results)} CVEs with CVSS >= {cvss_threshold}"
    )

    return results


def get_high_severity_cves(
    cvss_threshold: float = DEFAULT_CVSS_THRESHOLD,
) -> list[dict]:
    """
    Main function to fetch and filter high-severity CVEs from the last 24 hours.

    Args:
        cvss_threshold: Minimum CVSS score to include (default: 7.0)

    Returns:
        List of dicts with: cve_id, description, cvss_score, published_date

    Raises:
        requests.RequestException: If the API request fails
    """
    api_key = get_nvd_api_key()

    if api_key:
        logger.info("Using NVD API key for authentication")
    else:
        logger.warning(
            "No NVD_API_KEY found. Rate limits may apply. "
            "Set NVD_API_KEY in .env for higher rate limits."
        )

    vulnerabilities = fetch_cves(api_key=api_key)
    return filter_and_format_cves(vulnerabilities, cvss_threshold)


def main() -> None:
    """Entry point - fetches and prints high-severity CVEs."""
    try:
        cves = get_high_severity_cves()

        if not cves:
            print("No high-severity CVEs found in the last 24 hours.")
            return

        print(f"\nFound {len(cves)} high-severity CVEs (CVSS >= 7.0):\n")
        print("-" * 80)

        for cve in cves:
            print(f"CVE ID: {cve['cve_id']}")
            print(f"CVSS Score: {cve['cvss_score']}")
            print(f"Published: {cve['published_date']}")
            print(f"Description: {cve['description'][:200]}...")
            print("-" * 80)

    except requests.RequestException as e:
        logger.error(f"Failed to fetch CVEs from NVD API: {e}")
        raise


if __name__ == "__main__":
    main()
