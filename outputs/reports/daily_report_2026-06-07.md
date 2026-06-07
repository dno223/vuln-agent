# Vulnerability Intelligence Report

**Date:** 2026-06-07  
**Generated:** 2026-06-07T10:29:14Z  

---

## Executive Summary

Our security assessment reveals 9 high-severity vulnerabilities (CVSS 7.3-8.8) affecting critical infrastructure including network routers, cloud services, and enterprise applications. Most concerning is CVE-2026-26422 with local privilege escalation potential. Additionally, 5 new vulnerabilities were added to CISA's Known Exploited Vulnerabilities catalog this week, indicating active exploitation in the wild. These include SolarWinds Serv-U and Oracle WebLogic Server flaws. While our monitored CVEs don't currently appear in the KEV catalog, the diverse range of affected systems suggests widespread exposure across our technology stack.

---

## Risk Narrative

The threat landscape shows active exploitation of enterprise software with 5 new CISA KEV entries this week. Our environment faces elevated risk from privilege escalation vulnerabilities and network infrastructure flaws. The concentration of GL.iNet router vulnerabilities suggests potential for lateral movement if exploited. Enterprise applications including CRM and OA systems present data exposure risks. The mix of cloud services, network devices, and web applications creates multiple attack vectors that threat actors could chain together for comprehensive system compromise.

---

## Prioritized Action Items

1. Immediately patch or isolate clash-verge-service-ipc systems to address CVE-2026-26422 privilege escalation vulnerability.
2. Update JingDong JD Cloud Box AX6600 firmware to address the critical CVSS 8.8 vulnerability in set_macfilter function.
3. Patch SolarWinds Serv-U and Oracle WebLogic Server instances to remediate newly exploited vulnerabilities per CISA KEV.
4. Conduct security assessment of GL.iNet router infrastructure and apply available patches for multiple identified vulnerabilities.
5. Review and update Jinher OA and perfree go-fastdfs-web installations to address file manipulation vulnerabilities.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-11413 | 8.8 | 2026-06-06 | A security vulnerability has been detected in JingDong JD Cloud Box AX6600 4.5.3.r4546. The impacted element is the func |
| CVE-2026-11435 | 7.3 | 2026-06-06 | A security vulnerability has been detected in Jinher OA 1.0. This affects an unknown function of the file nextselectplan |
| CVE-2026-11437 | 7.3 | 2026-06-06 | A flaw has been found in perfree go-fastdfs-web up to 1.3.7. Affected is the function checkServer of the file /install/c |
| CVE-2026-26422 | 8.4 | 2026-06-06 | clash-verge-service-ipc before 2.3.0 has a world-reachable IPC endpoint, leading to local privilege escalation. |
| CVE-2026-11450 | 7.3 | 2026-06-07 | A vulnerability was detected in GL.iNet GL-MT3000 4.4.5. This affects the function dlopen in the library /usr/lib/oui-ht |
| CVE-2026-11451 | 7.3 | 2026-06-07 | A flaw has been found in GL.iNet GL-MT3000 4.4.5. This impacts the function snprintf of the file /cgi-bin/glc of the com |
| CVE-2026-11452 | 7.3 | 2026-06-07 | A vulnerability has been found in GL.iNet GL-MT3000 up to 4.4.5. Affected is the function FUN_0042e200 of the file /cgi- |
| CVE-2026-11456 | 7.3 | 2026-06-07 | A vulnerability was identified in Chanjet CRM 1.0. This affects an unknown part of the file /tools/jxf_dump_systable.php |
| CVE-2026-11457 | 7.3 | 2026-06-07 | A security flaw has been discovered in erzhongxmu JeeWMS up to 141740afb2ba14d441c82a833d0a418d07ca2d69. This vulnerabil |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-28318 | SolarWinds / Serv-U | 2026-06-05 | 2026-06-19 | Unknown |
| CVE-2026-45247 | Mirasvit / Mirasvit Full Page Cache Warmer | 2026-06-03 | 2026-06-06 | Unknown |
| CVE-2022-0492 | Linux / Kernel | 2026-06-02 | 2026-06-05 | Unknown |
| CVE-2025-48595 | Android / Framework | 2026-06-02 | 2026-06-05 | Unknown |
| CVE-2024-21182 | Oracle / WebLogic Server | 2026-06-01 | 2026-06-04 | Unknown |

---

*Total entries in CISA KEV catalog: 1612*