# Vulnerability Intelligence Report

**Date:** 2026-06-14  
**Generated:** 2026-06-14T10:48:22Z  

---

## Executive Summary

Our environment faces elevated security risks with 5 high-severity vulnerabilities discovered, including a critical CVSS 9.8 authentication bypass in gas station systems and an 8.8-rated D-Link camera vulnerability. Additionally, 7 new CISA Known Exploited Vulnerabilities were added this week, targeting Oracle PeopleSoft, Ivanti Sentry, Google Chrome, Arista systems, and Cisco SD-WAN platforms. While none of our monitored CVEs appear in the KEV catalog, the high-severity findings require immediate attention to prevent potential exploitation.

---

## Risk Narrative

The threat landscape shows active exploitation patterns with 7 new KEV entries targeting enterprise infrastructure including Oracle, Cisco, and Ivanti platforms. Our high-severity vulnerabilities span critical authentication bypasses, SQL injection, and XSS attacks across diverse systems from industrial controls to web applications. The critical gas station vulnerability poses immediate operational risks, while the D-Link camera flaw creates network infiltration opportunities. Threat actors are increasingly targeting infrastructure components, making rapid patching essential to prevent lateral movement and data compromise.

---

## Prioritized Action Items

1. Immediately patch CVE-2026-12183 in Nefteprodukttekhnika gas station systems due to critical authentication bypass vulnerability.
2. Update D-Link DCS-935L cameras to address CVE-2026-12174 buffer overflow vulnerability affecting web interfaces.
3. Patch LiteSpeed cPanel plugin to version 2.4.8 or later to resolve CVE-2026-54420 symlink handling issue.
4. Apply SQL injection fixes for CVE-2026-6428 in Koha library management systems immediately.
5. Update WordPress Bookly plugin to resolve CVE-2026-5513 stored cross-site scripting vulnerability.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-5513 | 7.2 | 2026-06-13 | The Online Scheduling and Appointment Booking System – Bookly plugin for WordPress is vulnerable to Stored Cross-Site Sc |
| CVE-2026-6428 | 7.6 | 2026-06-13 | SQL Injection in reports/catalogue_out.pl in Koha Community Koha through 22.11.37, 23.x, 24.x before 24.11.16, 25.05.x b |
| CVE-2026-12183 | 9.8 | 2026-06-13 | Nefteprodukttekhnika BUK TS-G Gas Station Automation System 2.9.1 through 2.10.2 on Linux contains an Improper Authentic |
| CVE-2026-12174 | 8.8 | 2026-06-13 | A security vulnerability has been detected in D-Link DCS-935L 1.10.01. This issue affects the function snprintf of the f |
| CVE-2026-54420 | 8.5 | 2026-06-14 | LiteSpeed cPanel plugin before 2.4.8 (as distributed in LiteSpeed WHM PlugIn before 5.3.2.0) mishandles symlinks provide |

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