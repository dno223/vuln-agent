# Vulnerability Intelligence Report

**Date:** 2026-11-15  
**Generated:** 2026-11-15T15:22:13Z  

## Pipeline Warnings

- cve_monitor failed: 503 Server Error: Service Unavailable for url: https://services.nvd.nist.gov/rest/json/cves/2.0?pubStartDate=2026-11-14T15%3A22%3A13.000&pubEndDate=2026-11-15T15%3A22%3A13.000

---

## Executive Summary

In the past seven days, CISA added 12 vulnerabilities to its Known Exploited Vulnerabilities catalog, signaling active exploitation in the wild. Affected products include UnrealIRCd, Check Point security appliances, Microsoft Office, Openwave Messaging Webtop Media Transcoder, and Cisco BroadWorks. While no currently monitored CVEs appear in the KEV catalog and no high-severity CVEs were flagged internally this cycle, the CISA additions represent confirmed, real-world threats requiring prompt attention. Organizations using any of the listed products must act immediately to assess exposure and apply available mitigations.

---

## Risk Narrative

CISA's Known Exploited Vulnerabilities catalog reflects confirmed, in-the-wild exploitation, making these additions high-priority threats regardless of internal severity ratings. The affected products span network infrastructure (Cisco BroadWorks, Check Point), productivity software (Microsoft Office), IRC services (UnrealIRCd), and messaging platforms (Openwave), indicating a broad attack surface. Threat actors exploiting these vulnerabilities may gain unauthorized access, escalate privileges, or disrupt critical services. The concentration of 12 additions in a single week suggests an elevated threat tempo. Organizations that delay remediation risk regulatory non-compliance, operational disruption, and potential data breaches with significant financial and reputational consequences.

---

## Prioritized Action Items

1. Audit your environment immediately for any instances of Check Point products, Cisco BroadWorks, Microsoft Office, UnrealIRCd, and Openwave Webtop Media Transcoder affected by the newly listed KEV entries.
2. Apply vendor-issued patches or mitigations for all 12 newly added CISA KEV vulnerabilities within the mandatory remediation window, prioritizing internet-facing systems.
3. Isolate or restrict access to any unpatched systems running affected software until patches can be applied to prevent lateral movement or data exfiltration.
4. Update threat detection rules and SIEM signatures to alert on exploitation indicators associated with the 12 newly catalogued CVEs.
5. Expand the monitored CVE list to include all 12 new KEV entries and schedule a follow-up review within 72 hours to confirm remediation progress.

---

## High Severity CVEs (CVSS ≥ 7.0)

_No high-severity CVEs found in the last 24 hours._

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-114713 | UnrealIRCd / UnrealIRCd | 2026-11-13 | 2026-11-16 | Unknown |
| CVE-2026-123039 | Check Point / Multiple Products | 2026-11-13 | 2026-11-16 | Unknown |
| CVE-2026-124194 | Microsoft / Office | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-111793 | Openwave Messaging Limited / Webtop Media Transcoder | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-20320 | Cisco / BroadWorks | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-111560 | Barracuda Networks / Multiple Products | 2026-11-10 | 2026-11-13 | Unknown |
| CVE-2026-116606 | Barracuda Networks / Barracuda Email Security Gateway (ESG) | 2026-11-10 | 2026-11-13 | Unknown |
| CVE-2026-125350 | Google / Chromium | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-102895 | GPUStack / GPUStack | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-123158 | OpenBSD / OpenSSH | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-116779 | SignalWire / FreeSwitch | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-123218 | IBM / Aspera Faspex | 2026-11-09 | 2026-11-12 | Unknown |

---

*Total entries in CISA KEV catalog: 1781*