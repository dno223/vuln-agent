# Vulnerability Intelligence Report

**Date:** 2026-07-23  
**Generated:** 2026-07-23T10:21:15Z  

## Pipeline Warnings

- summarizer failed: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}, 'request_id': 'req_011CdJpdxzTBrFT8Ji8moFLa'}

---

## Executive Summary

_No summary available._

---

## Risk Narrative

_No risk narrative available._

---

## Prioritized Action Items

_No action items available._

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-44189 | 7.8 | 2026-07-22 | A flaw was found in the Visual Studio Code Ansible Lightspeed extension's AnsiblePlaybookRunProvider. This command injec |
| CVE-2026-44190 | 7.8 | 2026-07-22 | A flaw was found in the Ansible Lightspeed Visual Studio Code extension. This Command Injection vulnerability (CWE-78) a |
| CVE-2026-4773 | 8.1 | 2026-07-22 | Improper validation of specified type of input vulnerability in Magarsus Consulting Ltd. Co. IDM-MFA allows Authenticati |
| CVE-2026-57600 | 7.5 | 2026-07-22 | Insufficient validation of input parameters in the firmware of some Hikvision cameras allows unauthenticated attackers t |
| CVE-2026-61390 | 7.7 | 2026-07-22 | There is a heap buffer overflow vulnerability in some Hikvision cameras, which may allow unauthenticated attackers to ca |
| CVE-2026-61391 | 7.2 | 2026-07-22 | There is a stack-based buffer overflow vulnerability in some Hikvision cameras, which may allow authenticated attackers  |
| CVE-2026-65603 | 8.8 | 2026-07-22 | The Grav Login plugin (grav-plugin-login) versions <= 3.8.11 contain a privilege escalation flaw in the authenticated pr |
| CVE-2026-44191 | 7.8 | 2026-07-22 | A flaw was found in the Visual Studio Code Ansible Lightspeed extension. This command injection vulnerability (CWE-78) a |
| CVE-2026-13181 | 8.1 | 2026-07-22 | In Progress® Telerik® UI for AJAX prior to v2026.2.708, forged upload metadata can influence AsyncUploadTypeName process |
| CVE-2026-13182 | 7.5 | 2026-07-22 | In Progress® Telerik® UI for AJAX prior to v2026.2.708, RadAsyncUpload client-state processing can distinguish decrypt f |
| CVE-2026-13183 | 7.5 | 2026-07-22 | In Progress® Telerik® UI for AJAX prior to v2026.2.708, RadAsyncUpload upload metadata processing may leak cryptographic |
| CVE-2026-13184 | 7.5 | 2026-07-22 | In Progress® Telerik® UI for AJAX prior to v2026.2.708, when Telerik.Upload.ConfigurationHashKey is absent and machineKe |
| CVE-2026-13185 | 8.1 | 2026-07-22 | In Progress® Telerik® UI for AJAX prior to v2026.2.708, applications using cookie-based storage in RadPersistenceManager |
| CVE-2026-13186 | 8.1 | 2026-07-22 | In Progress® Telerik® UI for AJAX prior to v2026.2.708, a path traversal vulnerability in the file-based persistence sto |
| CVE-2026-13187 | 8.1 | 2026-07-22 | In Progress® Telerik® UI for AJAX prior to v2026.2.708, DialogHandler provider type input may be tampered with, potentia |
| CVE-2026-13189 | 7.5 | 2026-07-22 | In Progress® Telerik® UI for AJAX prior to v2026.2.708, insufficient validation of the language parameter in the spell c |
| CVE-2026-13190 | 8.1 | 2026-07-22 | In Progress® Telerik® UI for AJAX prior to v2026.2.708, a deserialization vulnerability in the persistence utilities all |
| CVE-2026-16232 | 9.1 | 2026-07-22 | An authentication bypass vulnerability in the Check Point SmartConsole login process allows an unauthenticated remote at |
| CVE-2026-32665 | 7.5 | 2026-07-22 | In NLnet Labs Unbound 1.22.0 up to and including 1.25.1, when downstream DNS-over-QUIC (DoQ) is enabled, the first two b |
| CVE-2026-40691 | 7.5 | 2026-07-22 | In Unbound 1.9.0 up to and including 1.25.1, when a DNSCrypt query is received over TCP, the routine that encrypts the r |
| CVE-2026-44690 | 7.5 | 2026-07-22 | In NLnet Labs Unbound 1.7.0 up to and including 1.25.1, insufficient validation of the RRSIG.Labels field combined with  |
| CVE-2026-55973 | 7.5 | 2026-07-22 | In NLnet Labs Unbound 1.23.0 up to and including 1.25.1, when 'dns-error-reporting: yes' is set, the EDNS Report-Channel |
| CVE-2026-62144 | 9.1 | 2026-07-22 | An authentication bypass vulnerability in Check Point Security Management and Multi-Domain Security Management allows an |
| CVE-2026-62145 | 7.5 | 2026-07-22 | A vulnerability in Check Point Gaia Portal allows an authenticated attacker with read-only Gaia Portal privileges to exe |
| CVE-2026-11331 | 7.5 | 2026-07-22 | An attacker who knows (or guesses) that a resolver uses RPZ with wildcard CNAME policies can craft query names long enou |
| CVE-2026-11605 | 7.5 | 2026-07-22 | The issue is a resource exhaustion vulnerability associated with DNSSEC validation. BIND always validates all RRSIG reco |
| CVE-2026-11622 | 7.5 | 2026-07-22 | A DNSSEC validating resolver that is under a random subdomain attack against a DNSSEC-signed zone can suffer from runawa |
| CVE-2026-11721 | 7.5 | 2026-07-22 | It is possible for an attacker's zone to respond to a query with an RRSIG that has a smaller number of labels than the z |
| CVE-2026-12617 | 7.5 | 2026-07-22 | The issue is unexpected program termination based on ordering and/or specific content in responses to queries for CNAME  |
| CVE-2026-13204 | 7.5 | 2026-07-22 | If a provably insecure domain is covered by both an NSEC and NSEC3 record at the parent, and there exist an RRSIG for on |
| CVE-2026-13321 | 8.6 | 2026-07-22 | The BIND resolver accepts validly-signed NSEC records where the "Next Domain Name" field points outside the signer's zon |
| CVE-2026-2395 | 9.8 | 2026-07-22 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Xpoda Türkiye Info |
| CVE-2026-48029 | 7.1 | 2026-07-22 | libheif is a HEIF and AVIF file format decoder and encoder. Versions 1.19.0 through 1.21.2 have a heap OOB read in Image |
| CVE-2026-16606 | 9.8 | 2026-07-22 | A vulnerability in Fujitsu Software Linux openFT and Fujitsu Software Oracle Solaris openFT before version 12.1D00 allow |
| CVE-2026-16607 | 7.8 | 2026-07-22 | A vulnerability in Fujitsu Software Linux openFT and Fujitsu Software Oracle Solaris openFT before version 12.1D00 allow |
| CVE-2026-40712 | 9.1 | 2026-07-22 | Dell PowerProtect Data Manager, versions prior to 20.2.0.0, contain(s) an Improper Input Validation vulnerability in the |
| CVE-2026-40714 | 7.2 | 2026-07-22 | Dell PowerProtect Data Manager, versions prior to 20.2.0.0, contain(s) an Improper Input Validation vulnerability. A hig |
| CVE-2026-46738 | 9.1 | 2026-07-22 | Dell PowerProtect Data Manager, versions prior to 20.2.0.0, contain(s) an Improper Input Validation vulnerability in the |
| CVE-2026-49499 | 8.8 | 2026-07-22 | Dell PowerProtect Data Manager, versions prior to 20.2.0.0, contain(s) a Generation of Incorrect Security Tokens vulnera |
| CVE-2026-64830 | 8.8 | 2026-07-22 | FFmpeg versions 2.1 through 8.1.2 contains a heap buffer overflow vulnerability in the VobSub subtitle demuxer that allo |
| CVE-2026-64831 | 8.8 | 2026-07-22 | FFmpeg versions 8.0 through 8.1.2 contains a stack buffer overflow vulnerability in the Vulkan HEVC hardware decoder tha |
| CVE-2026-65013 | 8.8 | 2026-07-22 | Onlook through 0.2.32, fixed in commit 423e2e9, contains a broken object level authorization vulnerability that allows a |
| CVE-2026-64832 | 8.8 | 2026-07-22 | FFmpeg versions 4.4 through 8.1.2 contain a double-free vulnerability in the NVIDIA NVDEC hardware decoder within libavc |
| CVE-2026-64833 | 7.1 | 2026-07-22 | FFmpeg versions 0.7.1 through 8.1.2 contain an out-of-bounds read vulnerability in the S/PDIF muxer that allows attacker |
| CVE-2026-64834 | 7.5 | 2026-07-22 | FFmpeg versions 0.6.3 through 8.1.2 contain an infinite loop vulnerability in the RTP/ASF demuxer within libavformat/rtp |
| CVE-2026-64835 | 8.8 | 2026-07-22 | FFmpeg versions 4.4 through 8.1.2 contain an out-of-bounds memory access vulnerability in the ADX audio decoder within l |
| CVE-2026-13059 | 8.1 | 2026-07-22 | An authenticated user with low privileges may be able to perform unauthorized reads and writes on data protected by role |
| CVE-2026-13072 | 8.1 | 2026-07-22 | When compute mode is enabled on a standalone mongod instance, insufficient validation of externally sourced BSON data du |
| CVE-2026-13077 | 7.1 | 2026-07-22 | A missing bounds check in the BSON CodeWScope element accessors allows an attacker to trigger an out-of-bounds heap read |
| CVE-2026-13078 | 7.7 | 2026-07-22 | A vulnerability was discovered in MongoDB Server where the server-side MozJS scripting engine unconditionally registered |
| CVE-2026-14881 | 7.8 | 2026-07-22 | When importing connections in Compass it is possible to override some connection options that are otherwise can't be cha |
| CVE-2026-64829 | 7.4 | 2026-07-22 | Question2Answer through 1.8.8 contains a session invalidation vulnerability that allows attackers with a previously obta |
| CVE-2026-60366 | 10.0 | 2026-07-22 | Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Third |
| CVE-2026-60367 | 9.8 | 2026-07-22 | Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Third |
| CVE-2026-60368 | 8.8 | 2026-07-22 | Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Third |
| CVE-2026-60369 | 9.9 | 2026-07-22 | Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Third |
| CVE-2026-60370 | 7.5 | 2026-07-22 | Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Third |
| CVE-2026-60371 | 8.0 | 2026-07-22 | Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Third |
| CVE-2026-60372 | 9.8 | 2026-07-22 | Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Third |
| CVE-2026-60373 | 8.8 | 2026-07-22 | Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Third |
| CVE-2026-60439 | 8.8 | 2026-07-22 | Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Third |
| CVE-2026-60455 | 8.8 | 2026-07-22 | Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Third |
| CVE-2026-61246 | 8.8 | 2026-07-22 | Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Third |
| CVE-2026-16632 | 7.3 | 2026-07-23 | A flaw has been found in boazsegev facil.io up to 0.7.4. Affected is the function websocket_on_protocol_error in the lib |
| CVE-2026-15074 | 7.5 | 2026-07-23 | @fastify/static up to and including version 10.1.0 fails to reject dot-dot path segments in request pathnames before the |
| CVE-2026-7232 | 7.2 | 2026-07-23 | The FormCraft plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the '[parameter name]' parameter in  |
| CVE-2026-7534 | 7.2 | 2026-07-23 | The SUMO Reward Points plugin for WordPress is vulnerable to Unauthenticated Stored Cross-Site Scripting via the REST AP |
| CVE-2026-12421 | 7.2 | 2026-07-23 | The ARforms plugin for WordPress is vulnerable to Stored Cross-Site Scripting via 'password' Field Values in all version |
| CVE-2026-9713 | 7.5 | 2026-07-23 | The Lumise Product Designer for WooCommerce plugin for WordPress is vulnerable to SQL Injection via the 'id' and 'table' |
| CVE-2024-58023 | 8.4 | 2026-07-23 | Information disclosure in Bosch Configuration Manager in Version 7.72.0106 allows an attacker to access sensitive inform |
| CVE-2024-58330 | 7.5 | 2026-07-23 | A missing authentication check in Bosch IP cameras of families CPP13 and CPP14 allows an unauthenticated attacker to ret |
| CVE-2026-16287 | 7.8 | 2026-07-23 | Improper neutralization of special elements used in an OS command ('OS command injection') vulnerability in TUBITAK BILG |
| CVE-2026-16723 | 9.0 | 2026-07-23 | A remote code execution (RCE) vulnerability exists in fastjson 1.2.68 through 1.2.83. This vulnerability is exploitable  |
| CVE-2026-52688 | 7.5 | 2026-07-23 | RRSIGs with too few labels can lead to bypass of DNSSEC wildcard validation |
| CVE-2026-14282 | 9.8 | 2026-07-23 | The GoDAM – Organize WordPress Media Library & File Manager with Unlimited Folders for Images, Videos & more plugin for  |
| CVE-2026-15011 | 9.8 | 2026-07-23 | The Customer Support Ticket System & Helpdesk plugin for WordPress is vulnerable to Code Injection via the 'path' parame |
| CVE-2026-15015 | 9.8 | 2026-07-23 | The MountDev AI MCP Connector for WordPress plugin for WordPress is vulnerable to authorization bypass in all versions u |
| CVE-2026-15017 | 8.8 | 2026-07-23 | The MDJM Event Management plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and includin |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-16232 | Check Point / SmartConsole | 2026-07-22 | 2026-07-25 | Unknown |
| CVE-2026-50522 | Microsoft / SharePoint | 2026-07-22 | 2026-07-25 | Unknown |
| CVE-2026-60137 | WordPress / Core | 2026-07-21 | 2026-08-04 | Unknown |
| CVE-2026-63030 | WordPress / Core | 2026-07-21 | 2026-07-24 | Unknown |
| CVE-2026-0770 | Langflow / Langflow | 2026-07-21 | 2026-07-24 | Unknown |
| CVE-2021-27137 | DD-WRT / DD-WRT | 2026-07-21 | 2026-07-24 | Unknown |
| CVE-2026-58644 | Microsoft / SharePoint | 2026-07-16 | 2026-07-19 | Unknown |
| CVE-2026-25089 | Fortinet / FortiSandbox | 2026-07-16 | 2026-07-19 | Unknown |
| CVE-2026-39808 | Fortinet / FortiSandbox | 2026-07-16 | 2026-07-19 | Unknown |

---

*Total entries in CISA KEV catalog: 1653*