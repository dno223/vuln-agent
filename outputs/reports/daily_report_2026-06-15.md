# Vulnerability Intelligence Report

**Date:** 2026-06-15  
**Generated:** 2026-06-15T13:55:06Z  

## Pipeline Warnings

- cve_monitor failed: HTTPSConnectionPool(host='services.nvd.nist.gov', port=443): Read timed out. (read timeout=30)

---

## Executive Summary

Seven new vulnerabilities were added to CISA's Known Exploited Vulnerabilities catalog this week, indicating active exploitation in the wild. These affect critical enterprise systems including Oracle PeopleSoft, Ivanti Sentry, Google Chrome, Arista network equipment, and Cisco SD-WAN infrastructure. While no high-severity CVEs were reported separately, the KEV additions represent immediate threats requiring urgent remediation as attackers are already leveraging these vulnerabilities against organizations.

---

## Risk Narrative

The addition of seven vulnerabilities to CISA's KEV catalog signals an elevated threat landscape with active exploitation campaigns targeting diverse enterprise infrastructure. These vulnerabilities span critical business applications, network management systems, and web browsers, providing attackers multiple attack vectors into organizational networks. The rapid succession of KEV additions suggests coordinated threat actor activity or widespread vulnerability scanning campaigns. Organizations face immediate risk of data breaches, network compromise, and operational disruption if these vulnerabilities remain unpatched.

---

## Prioritized Action Items

1. Immediately patch Oracle PeopleSoft Enterprise PeopleTools systems to address CVE-2026-35273.
2. Update all Ivanti Sentry installations to remediate CVE-2026-10520 exploitation risk.
3. Deploy Chrome browser updates across the organization to fix CVE-2026-11645 in V8 engine.
4. Patch Arista network devices running Extensible Operating System for CVE-2026-7473.
5. Update Cisco Catalyst SD-WAN Manager systems to address CVE-2026-20245 vulnerability.

---

## High Severity CVEs (CVSS ≥ 7.0)

_No high-severity CVEs found in the last 24 hours._

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-35273 | Oracle /  PeopleSoft Enterprise PeopleTools | 2026-06-12 | 2026-06-15 | Known |
| CVE-2026-10520 | Ivanti / Sentry | 2026-06-11 | 2026-06-14 | Unknown |
| CVE-2026-11645 | Google / Chromium V8 | 2026-06-09 | 2026-06-23 | Unknown |
| CVE-2026-7473 | Arista / Extensible Operating System | 2026-06-09 | 2026-06-23 | Unknown |
| CVE-2026-20245 | Cisco / Catalyst SD-WAN Manager | 2026-06-09 | 2026-06-23 | Unknown |
| CVE-2026-42271 | BerriAI / LiteLLM | 2026-06-08 | 2026-06-22 | Unknown |
| CVE-2026-50751 | Check Point / Security Gateway | 2026-06-08 | 2026-06-11 | Known |

---

*Total entries in CISA KEV catalog: 1619*