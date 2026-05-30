"""
CISA KEV Tracker Agent - Tracks new entries in the CISA Known Exploited Vulnerabilities catalog.

Fetches the KEV catalog, identifies entries added in the last 7 days,
and cross-references against a provided list of monitored CVE IDs.
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

CISA_KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
DEFAULT_LOOKBACK_DAYS = 7


def fetch_kev_catalog(url: str = CISA_KEV_URL) -> dict:
    """
    Fetch the CISA KEV catalog JSON.

    Args:
        url: URL of the KEV catalog feed

    Returns:
        Parsed JSON response from the CISA KEV feed

    Raises:
        requests.RequestException: If the request fails
    """
    logger.info(f"Fetching CISA KEV catalog from {url}")
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    data = response.json()
    total = data.get("count", len(data.get("vulnerabilities", [])))
    logger.info(f"Retrieved KEV catalog with {total} entries")
    return data


def filter_new_entries(
    vulnerabilities: list[dict],
    days: int = DEFAULT_LOOKBACK_DAYS,
    reference_date: Optional[datetime] = None,
) -> list[dict]:
    """
    Filter KEV entries added within the last N days.

    Args:
        vulnerabilities: List of KEV vulnerability entries
        days: Number of days to look back (default: 7)
        reference_date: Date to measure from (defaults to now in UTC)

    Returns:
        List of entries whose dateAdded is within the lookback window
    """
    if reference_date is None:
        reference_date = datetime.now(timezone.utc)

    cutoff_date = (reference_date - timedelta(days=days)).date()
    new_entries = []

    for vuln in vulnerabilities:
        date_added_str = vuln.get("dateAdded", "")
        if not date_added_str:
            continue
        try:
            date_added = datetime.strptime(date_added_str, "%Y-%m-%d").date()
        except ValueError:
            logger.warning(f"Could not parse dateAdded '{date_added_str}' for {vuln.get('cveID')}")
            continue

        if date_added >= cutoff_date:
            new_entries.append(vuln)

    logger.info(f"Found {len(new_entries)} new KEV entries in the last {days} days")
    return new_entries


def find_monitored_hits(
    vulnerabilities: list[dict],
    cve_ids: list[str],
) -> list[dict]:
    """
    Cross-reference KEV entries against a list of monitored CVE IDs.

    Args:
        vulnerabilities: List of KEV vulnerability entries to search
        cve_ids: List of CVE IDs to check against the catalog

    Returns:
        KEV entries whose cveID appears in cve_ids
    """
    if not cve_ids:
        return []

    monitored_set = {cve_id.upper() for cve_id in cve_ids}
    hits = [v for v in vulnerabilities if v.get("cveID", "").upper() in monitored_set]
    logger.info(f"Found {len(hits)} monitored CVE(s) in KEV catalog")
    return hits


def run_cisa_tracker(
    cve_ids: Optional[list[str]] = None,
    days: int = DEFAULT_LOOKBACK_DAYS,
) -> dict:
    """
    Fetch the KEV catalog and produce a summary report.

    Args:
        cve_ids: Optional list of CVE IDs to watch for in the catalog
        days: How many days back to consider "new" (default: 7)

    Returns:
        Dict with keys:
          - new_kev_entries: list of new KEV additions
          - monitored_hits: KEV entries matching provided cve_ids
          - total_kev_count: total vulnerabilities in the catalog

    Raises:
        requests.RequestException: If the CISA feed cannot be fetched
    """
    if cve_ids is None:
        cve_ids = []

    catalog = fetch_kev_catalog()
    vulnerabilities = catalog.get("vulnerabilities", [])
    total_kev_count = catalog.get("count", len(vulnerabilities))

    new_kev_entries = filter_new_entries(vulnerabilities, days=days)
    monitored_hits = find_monitored_hits(vulnerabilities, cve_ids)

    return {
        "new_kev_entries": new_kev_entries,
        "monitored_hits": monitored_hits,
        "total_kev_count": total_kev_count,
    }


def main() -> None:
    """Entry point - fetches KEV catalog and prints a summary to console."""
    monitored_cves_env = os.getenv("MONITORED_CVES", "")
    cve_ids = [c.strip() for c in monitored_cves_env.split(",") if c.strip()]

    try:
        results = run_cisa_tracker(cve_ids=cve_ids)

        print(f"\nCISA KEV Catalog Summary")
        print("=" * 80)
        print(f"Total entries in catalog: {results['total_kev_count']}")
        print(f"New entries (last {DEFAULT_LOOKBACK_DAYS} days): {len(results['new_kev_entries'])}")
        print(f"Monitored CVEs found in catalog: {len(results['monitored_hits'])}")

        if results["new_kev_entries"]:
            print(f"\nNew KEV Additions (last {DEFAULT_LOOKBACK_DAYS} days):")
            print("-" * 80)
            for entry in results["new_kev_entries"]:
                print(f"  CVE: {entry.get('cveID')}")
                print(f"  Added: {entry.get('dateAdded')}")
                print(f"  Vendor/Product: {entry.get('vendorProject')} / {entry.get('product')}")
                print(f"  Name: {entry.get('vulnerabilityName')}")
                print(f"  Due Date: {entry.get('dueDate')}")
                print()

        if results["monitored_hits"]:
            print("\nMonitored CVEs Found in KEV Catalog:")
            print("-" * 80)
            for entry in results["monitored_hits"]:
                print(f"  CVE: {entry.get('cveID')}")
                print(f"  Added: {entry.get('dateAdded')}")
                print(f"  Vendor/Product: {entry.get('vendorProject')} / {entry.get('product')}")
                print()
        elif cve_ids:
            print("\nNo monitored CVEs found in the KEV catalog.")

    except requests.RequestException as e:
        logger.error(f"Failed to fetch CISA KEV catalog: {e}")
        raise


if __name__ == "__main__":
    main()
