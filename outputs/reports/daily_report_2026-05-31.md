# Vulnerability Intelligence Report

**Date:** 2026-05-31  
**Generated:** 2026-05-31T10:15:31Z  

---

## Executive Summary

Our organization faces significant cybersecurity risks with 41 high-severity vulnerabilities identified, including critical WordPress plugin flaws and network device compromises. Multiple CVEs score 8.8 on the CVSS scale, indicating severe threats including remote code execution, SQL injection, and account takeover vulnerabilities. Additionally, 5 new entries were added to CISA's Known Exploited Vulnerabilities catalog in the past week, signaling active threat actor exploitation in the wild. Immediate remediation is required to prevent potential data breaches, system compromises, and business disruption.

---

## Risk Narrative

The current threat landscape presents elevated risks with attackers actively exploiting vulnerabilities across web applications, network infrastructure, and enterprise systems. WordPress environments face particular danger from authenticated privilege escalation and remote code execution flaws. Network perimeter devices show critical weaknesses that could enable lateral movement and data exfiltration. The addition of 5 new CISA KEV entries indicates sophisticated threat actors are rapidly weaponizing vulnerabilities. Without immediate action, the organization remains vulnerable to data breaches, service disruptions, and potential regulatory compliance violations.

---

## Prioritized Action Items

1. Immediately patch or disable vulnerable WordPress plugins including Simple History, Spectra Gutenberg Blocks, and GEO my WP to prevent remote code execution and account takeover attacks.
2. Update TRENDnet TEW-432BRP routers to latest firmware or replace devices to address critical firewall and MAC filter vulnerabilities.
3. Apply emergency patches for Palo Alto Networks PAN-OS systems following CISA KEV addition within 24 hours.
4. Conduct security audit of eNdonesia Portal and SIM-PKH installations to remediate SQL injection and file upload vulnerabilities.
5. Review and update incident response procedures to address the increased threat landscape from newly cataloged exploits.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-7459 | 7.5 | 2026-05-30 | The Simple History – Track, Log, and Audit WordPress Changes plugin for WordPress is vulnerable to authenticated (Subscr |
| CVE-2026-7465 | 8.8 | 2026-05-30 | The Spectra Gutenberg Blocks – Website Builder for the Block Editor plugin for WordPress is vulnerable to Remote Code Ex |
| CVE-2026-9757 | 7.5 | 2026-05-30 | The GEO my WP plugin for WordPress is vulnerable to SQL Injection via the 'swlatlng' and 'nelatlng' parameters in all ve |
| CVE-2026-10119 | 8.8 | 2026-05-30 | A security vulnerability has been detected in TRENDnet TEW-432BRP 3.10B20. Impacted is the function formSetMACFilter of  |
| CVE-2026-10120 | 8.8 | 2026-05-30 | A vulnerability was detected in TRENDnet TEW-432BRP 3.10B20. The affected element is the function formSetFirewallRule of |
| CVE-2018-25405 | 8.2 | 2026-05-30 | eNdonesia Portal 8.7 contains multiple SQL injection vulnerabilities that allow unauthenticated attackers to execute arb |
| CVE-2018-25406 | 8.2 | 2026-05-30 | eNdonesia Portal 8.7 contains multiple SQL injection vulnerabilities that allow unauthenticated attackers to execute arb |
| CVE-2018-25407 | 8.2 | 2026-05-30 | eNdonesia Portal 8.7 contains multiple SQL injection vulnerabilities that allow unauthenticated attackers to execute arb |
| CVE-2018-25408 | 7.5 | 2026-05-30 | The Open ISES Project 3.30A contains a path traversal vulnerability in the ajax/download.php endpoint that allows unauth |
| CVE-2018-25409 | 8.8 | 2026-05-30 | SIM-PKH 2.4.1 contains an arbitrary file upload vulnerability that allows authenticated attackers to upload malicious fi |
| CVE-2018-25410 | 7.1 | 2026-05-30 | SIM-PKH 2.4.1 contains an SQL injection vulnerability that allows authenticated attackers to execute arbitrary SQL queri |
| CVE-2018-25411 | 8.2 | 2026-05-30 | MGB OpenSource Guestbook 0.7.0.2 contains an SQL injection vulnerability that allows unauthenticated attackers to execut |
| CVE-2018-25412 | 9.8 | 2026-05-30 | Delta Sql 1.8.2 contains an arbitrary file upload vulnerability that allows unauthenticated attackers to upload maliciou |
| CVE-2018-25413 | 8.2 | 2026-05-30 | AiOPMSD Final 1.0.0 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2018-25414 | 8.2 | 2026-05-30 | AiOPMSD Final 1.0.0 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2018-25415 | 8.2 | 2026-05-30 | AiOPMSD Final 1.0.0 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2018-25416 | 8.2 | 2026-05-30 | AiOPMSD Final 1.0.0 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2018-25417 | 8.2 | 2026-05-30 | AiOPMSD Final 1.0.0 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2018-25418 | 8.2 | 2026-05-30 | AiOPMSD Final 1.0.0 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2018-25419 | 8.2 | 2026-05-30 | AiOPMSD Final 1.0.0 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2018-25420 | 8.2 | 2026-05-30 | AiOPMSD Final 1.0.0 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2018-25422 | 8.2 | 2026-05-30 | MOGG web simulator Script contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbit |
| CVE-2018-25424 | 8.2 | 2026-05-30 | Gate Pass Management System 2.1 contains an SQL injection vulnerability that allows unauthenticated attackers to bypass  |
| CVE-2018-25425 | 8.2 | 2026-05-30 | Yot CMS 3.3.1 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary SQL que |
| CVE-2018-25426 | 7.5 | 2026-05-30 | WinMTR 0.91 contains a denial of service vulnerability that allows attackers to crash the application by sending a malfo |
| CVE-2026-10121 | 8.8 | 2026-05-30 | A flaw has been found in TRENDnet TEW-432BRP 3.10B20. The impacted element is the function formSetUrlFilter of the file  |
| CVE-2026-10122 | 8.8 | 2026-05-30 | A vulnerability has been found in TRENDnet TEW-432BRP 3.10B20. This affects the function formSetProtocolFilter of the fi |
| CVE-2026-10123 | 8.8 | 2026-05-30 | A vulnerability was found in TRENDnet TEW-432BRP 3.10B20. This impacts the function formSetDomainFilter of the file /gof |
| CVE-2026-10124 | 8.8 | 2026-05-30 | A vulnerability was determined in Shibby Tomato up to 1.28. Affected is the function rip_zebra_read_ipv4 of the file /us |
| CVE-2026-10125 | 8.8 | 2026-05-30 | A vulnerability was identified in Edimax BR-6478AC 1.23. Affected by this vulnerability is the function formPPPoESetup o |
| CVE-2026-10126 | 8.8 | 2026-05-30 | A security flaw has been discovered in Edimax BR-6478AC 1.23. Affected by this issue is the function formQoS of the file |
| CVE-2026-10157 | 7.3 | 2026-05-31 | A vulnerability was identified in Open5GS up to 2.7.6. This impacts an unknown function of the file src/amf/ngap-handler |
| CVE-2026-10158 | 8.8 | 2026-05-31 | A security flaw has been discovered in TRENDnet TEW-432BRP 3.10B20. Affected is the function formPortFw of the file /gof |
| CVE-2026-10159 | 8.8 | 2026-05-31 | A weakness has been identified in TRENDnet TEW-432BRP 3.10B20. Affected by this vulnerability is the function formSysLog |
| CVE-2026-10160 | 8.8 | 2026-05-31 | A security vulnerability has been detected in TRENDnet TEW-432BRP 3.10B20. Affected by this issue is the function formSe |
| CVE-2026-10161 | 8.8 | 2026-05-31 | A vulnerability was detected in TRENDnet TEW-432BRP 3.10B20. This affects the function formResetStatistic of the file /g |
| CVE-2026-10162 | 8.8 | 2026-05-31 | A flaw has been found in TRENDnet TEW-432BRP 3.10B20. This vulnerability affects the function formSetPassword of the fil |
| CVE-2026-10163 | 8.8 | 2026-05-31 | A vulnerability has been found in Edimax BR-6478AC 1.23. This issue affects the function formUSBAccount of the file /gof |
| CVE-2026-10164 | 8.8 | 2026-05-31 | A vulnerability was found in Edimax BR-6478AC 1.23. Impacted is the function formUSBFolder of the file /goform/formUSBFo |
| CVE-2026-10165 | 8.8 | 2026-05-31 | A vulnerability was identified in Edimax BR-6478AC 1.23. The impacted element is the function formWanTcpipSetup of the f |
| CVE-2026-10167 | 7.3 | 2026-05-31 | A weakness has been identified in OUSL-GROUP-BrinaryBrains School Student Management System up to 1e70e5ad1125b86dca4ee0 |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-0257 | Palo Alto Networks / PAN-OS | 2026-05-29 | 2026-06-01 | Unknown |
| CVE-2026-48027 | Nx / Nx Console | 2026-05-27 | 2026-06-10 | Known |
| CVE-2026-45321 | TanStack / TanStack | 2026-05-27 | 2026-06-10 | Known |
| CVE-2026-8398 | Daemon / Daemon Tools Lite | 2026-05-27 | 2026-05-30 | Unknown |
| CVE-2026-48172 | LiteSpeed / cPanel Plugin | 2026-05-26 | 2026-05-29 | Unknown |

---

*Total entries in CISA KEV catalog: 1607*