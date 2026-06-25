# Vulnerability Intelligence Report

**Date:** 2026-06-25  
**Generated:** 2026-06-25T10:40:59Z  

## Pipeline Warnings

- summarizer failed: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}, 'request_id': 'req_011CcPqd49twxNYc7AwDqkDr'}

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
| CVE-2025-71354 | 8.1 | 2026-06-24 | picklescan before 0.0.29 fails to detect malicious pickle files that exploit idlelib.debugobj.ObjectTreeItem.SetText fun |
| CVE-2025-71361 | 8.1 | 2026-06-24 | picklescan before 0.0.29 fails to detect malicious idlelib.calltip.Calltip.fetch_tip calls in pickle files, allowing rem |
| CVE-2026-12242 | 8.8 | 2026-06-24 | The AdRotate Banner Manager plugin for WordPress is vulnerable to PHP Code Injection in all versions up to, and includin |
| CVE-2026-56223 | 8.7 | 2026-06-24 | Capgo before 12.128.2 contains a cross-domain SSO account takeover vulnerability in the provision-user endpoint that all |
| CVE-2026-56231 | 7.6 | 2026-06-24 | Capgo before 12.128.2 contains a broken object level authorization (BOLA) vulnerability in the POST /build/start/:jobId  |
| CVE-2026-56232 | 8.8 | 2026-06-24 | Capgo before 12.128.2 fails to enforce limited_to_orgs and limited_to_apps constraints on subkeys provided via x-limited |
| CVE-2026-56237 | 9.1 | 2026-06-24 | Capgo before 12.128.2 contains a broken authentication vulnerability in its API key generation mechanism. API keys are e |
| CVE-2026-56244 | 7.1 | 2026-06-24 | Capgo before 12.128.2 allows non-admin API keys to read webhook signing secrets via Supabase REST due to insufficient ro |
| CVE-2026-56245 | 8.2 | 2026-06-24 | Supabase Capgo before 12.128.2 contains an authorization bypass vulnerability in the SECURITY DEFINER record_build_time  |
| CVE-2026-56256 | 7.1 | 2026-06-24 | Capgo before 12.128.2 enforces mandatory two-factor authentication only at the UI level. Sensitive Organization (ORG) ma |
| CVE-2026-56257 | 7.1 | 2026-06-24 | Capgo before 12.128.2 allows direct patching of public.apps.owner_org through PostgREST, bypassing the transfer_app() wo |
| CVE-2026-56270 | 7.5 | 2026-06-24 | Flowise before 3.1.0 (versions 3.0.13 and earlier) contains a missing authentication vulnerability in the /api/v1/loginm |
| CVE-2026-56351 | 8.2 | 2026-06-24 | n8n before version 2.4.0 contains a sql injection vulnerability in MySQL, PostgreSQL, and Microsoft SQL nodes that allow |
| CVE-2026-35025 | 8.1 | 2026-06-24 | ProFTPD through 1.3.9b and 1.3.10rc2 contains an access control bypass vulnerability that allows authenticated FTP users |
| CVE-2026-57280 | 8.8 | 2026-06-24 | Jenkins Script Security Plugin 1402.v94c9ce464861 and earlier does not intercept the implicit type casts applied to the  |
| CVE-2026-57281 | 7.5 | 2026-06-24 | Jenkins Script Security Plugin 1402.v94c9ce464861 and earlier does not reject Groovy AST transformation annotations carr |
| CVE-2026-57296 | 8.8 | 2026-06-24 | Jenkins External Workspace Manager Plugin 1.3.2 and earlier does not reject path traversal sequences in the custom works |
| CVE-2026-57301 | 8.8 | 2026-06-24 | Jenkins OWASP ZAP Plugin 1.0.7 and earlier performs build operations on the Jenkins controller rather than the assigned  |
| CVE-2026-57303 | 7.1 | 2026-06-24 | Jenkins Assembla Plugin 1.4 and earlier does not configure its XML parser to prevent XML external entity (XXE) attacks,  |
| CVE-2026-49269 | 8.6 | 2026-06-24 | Apple M1 GPUs retain register file data between compute shader dispatches from different processes. A sandboxed Metal at |
| CVE-2026-56111 | 9.1 | 2026-06-24 | Marlin Firmware through 2.1.2.7, fixed in commit 1f255d1, when built with MESH_BED_LEVELING enabled, contains an out-of- |
| CVE-2026-56121 | 9.8 | 2026-06-24 | Feast before 0.63.0 contains an unsafe deserialization vulnerability that allows unauthenticated or unauthorized attacke |
| CVE-2026-54297 | 7.5 | 2026-06-24 | Faraday is an HTTP client library abstraction layer that provides a common interface over many adapters. From 1.0.0 unti |
| CVE-2026-44016 | 8.2 | 2026-06-24 | Docling simplifies document processing by parsing diverse formats and providing integrations with the generative AI ecos |
| CVE-2026-44017 | 7.5 | 2026-06-24 | Docling simplifies document processing by parsing diverse formats and providing integrations with the generative AI ecos |
| CVE-2026-44020 | 7.5 | 2026-06-24 | Docling simplifies document processing by parsing diverse formats and providing integrations with the generative AI ecos |
| CVE-2026-48703 | 7.8 | 2026-06-24 | Warp is an agentic development environment. From 0.2025.04.09.08.11.stable_00 until 0.2026.05.06.15.42.stable_01, Warp c |
| CVE-2026-48704 | 8.8 | 2026-06-24 | Warp is an agentic development environment. From 0.2023.10.24.08.03.stable_00 until 0.2026.05.06.15.42.stable_01, Warp m |
| CVE-2026-48719 | 8.0 | 2026-06-24 | Warp is an agentic development environment. From 0.2025.08.06.08.12.stable_00 until 0.2026.05.06.15.42.stable_01, Warp c |
| CVE-2026-48720 | 8.8 | 2026-06-24 | Warp is an agentic development environment. From 0.2025.03.05.08.02.stable_00 until 0.2026.05.06.15.42.stable_01, Warp a |
| CVE-2026-48721 | 8.6 | 2026-06-24 | Warp is an agentic development environment. From 0.2025.10.08.08.12.stable_00 until 0.2026.05.06.15.42.stable_01, Warp c |
| CVE-2026-48725 | 8.1 | 2026-06-24 | Warp is an agentic development environment. From 0.2021.04.25.23.05.stable_00 until 0.2026.05.06.15.42.stable_01, Warp a |
| CVE-2026-48731 | 7.8 | 2026-06-24 | Warp is an agentic development environment. From 0.2024.02.20.08.01.stable_01 until 0.2026.05.06.15.42.stable_01, Warp c |
| CVE-2026-48732 | 8.8 | 2026-06-24 | Warp is an agentic development environment. From 0.2023.03.21.08.02.stable_00 until 0.2026.05.06.15.42.stable_01, Warp c |
| CVE-2026-54699 | 7.7 | 2026-06-24 | Warp is an agentic development environment. From 0.2024.03.12.08.02.stable_01 until 0.2026.05.06.15.42.stable_01, Warp c |
| CVE-2026-13025 | 8.3 | 2026-06-24 | Race in DevTools in Google Chrome prior to 149.0.7827.197 allowed a remote attacker who had compromised the renderer pro |
| CVE-2026-13026 | 8.8 | 2026-06-24 | Use after free in Digital Credentials in Google Chrome on Mac prior to 149.0.7827.197 allowed a remote attacker to poten |
| CVE-2026-13027 | 8.8 | 2026-06-24 | Use after free in FileSystem in Google Chrome prior to 149.0.7827.197 allowed a remote attacker to potentially exploit h |
| CVE-2026-13028 | 9.6 | 2026-06-24 | Use after free in WebGL in Google Chrome on Android prior to 149.0.7827.197 allowed a remote attacker to potentially per |
| CVE-2026-13029 | 7.5 | 2026-06-24 | Use after free in Web Authentication in Google Chrome prior to 149.0.7827.197 allowed an attacker who convinced a user t |
| CVE-2026-13031 | 8.8 | 2026-06-24 | Use after free in Blink in Google Chrome prior to 149.0.7827.197 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-13032 | 9.6 | 2026-06-24 | Use after free in WebGL in Google Chrome on Android prior to 149.0.7827.197 allowed a remote attacker to potentially per |
| CVE-2026-13033 | 8.8 | 2026-06-24 | Out of bounds read and write in Blink>InterestGroups in Google Chrome prior to 149.0.7827.197 allowed a remote attacker  |
| CVE-2026-13035 | 8.8 | 2026-06-24 | Use after free in Bluetooth in Google Chrome on Mac prior to 149.0.7827.197 allowed a remote attacker to execute arbitra |
| CVE-2026-13036 | 8.8 | 2026-06-24 | Use after free in Blink in Google Chrome prior to 149.0.7827.197 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-13037 | 7.8 | 2026-06-24 | Use after free in WebView in Google Chrome on Android prior to 149.0.7827.197 allowed a local attacker to execute arbitr |
| CVE-2026-13038 | 8.8 | 2026-06-24 | Use after free in Autofill in Google Chrome on Windows prior to 149.0.7827.197 allowed a remote attacker to execute arbi |
| CVE-2026-48793 | 8.8 | 2026-06-24 | Jellyfin is an open source self hosted media server. Prior to 10.11.10, a potential FFmpeg argument injection vulnerabil |
| CVE-2026-49247 | 8.8 | 2026-06-24 | Jellyfin is an open source self hosted media server. From 10.9.0 until 10.11.10, the POST /ClientLog/Document endpoint a |
| CVE-2026-49980 | 9.8 | 2026-06-24 | Rclone is a command-line program to sync files and directories to and from different cloud storage providers. From 1.46. |
| CVE-2026-53943 | 9.6 | 2026-06-24 | Ghost is a Node.js content management system. From  until 6.37.0, when Ghost is behind a shared caching layer that resul |
| CVE-2026-53950 | 7.5 | 2026-06-24 | @tryghost/activitypub is Ghost’s social/federation client app. Prior to 3.1.0, the ActivityPub client in Ghost was vulne |
| CVE-2026-23879 | 8.0 | 2026-06-24 | py7zr is a Python-based library and utility to support 7zip archive compression, decompression, encryption and decryptio |
| CVE-2026-47389 | 8.6 | 2026-06-24 | Mastodon is a free, open-source social network server based on ActivityPub. Prior to 4.5.10, 4.4.17, and 4.3.23, when us |
| CVE-2026-55583 | 7.6 | 2026-06-24 | Twenty is an open-source CRM (customer relationship management) platform. Prior to 2.9.0, Twenty was vulnerable to a cro |
| CVE-2026-11998 | 7.6 | 2026-06-24 | A flaw in AngularJS' Strict Contextual Escaping (SCE) logic allows bypassing certain SCE policies for resource URLs and  |
| CVE-2026-1840 | 7.5 | 2026-06-24 | The Aclara Metrum Cellular Web Interface is vulnerable to unauthorized access due to the absence of authentication contr |
| CVE-2026-33235 | 7.7 | 2026-06-24 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agent |
| CVE-2026-45687 | 8.5 | 2026-06-24 | Rocket.Chat is an open-source, secure, fully customizable communications platform. Prior to 8.5.0, 8.4.1, 8.3.3, 8.2.3,  |
| CVE-2026-45688 | 9.1 | 2026-06-24 | Rocket.Chat is an open-source, secure, fully customizable communications platform. Prior to 8.5.0, 8.4.1, 8.3.3, 8.2.3,  |
| CVE-2026-45689 | 9.1 | 2026-06-24 | Rocket.Chat is an open-source, secure, fully customizable communications platform. Prior to 8.5.0, 8.4.1, 8.3.3, 8.2.3,  |
| CVE-2026-47267 | 8.3 | 2026-06-24 | Gogs is an open source self-hosted Git service. Prior to 0.14.3, the fix for CVE-2022-1285 prevents adding webooks or ru |
| CVE-2026-50129 | 7.5 | 2026-06-24 | Mastodon is a free, open-source social network server based on ActivityPub. Prior to 4.5.11, 4.4.18, and 4.3.24, a DoS c |
| CVE-2026-52797 | 8.5 | 2026-06-24 | Gogs is an open source self-hosted Git service. Prior to 0.14.0, as an authorized user, an intruder can dictate the valu |
| CVE-2026-52798 | 8.9 | 2026-06-24 | Gogs is an open source self-hosted Git service. Prior to 0.14.3, although .ipynb previews are sanitized on the server si |
| CVE-2026-52799 | 7.5 | 2026-06-24 | Gogs is an open source self-hosted Git service. Prior to 0.14.3, GET /attachments/:uuid returns the raw attachment file  |
| CVE-2026-52800 | 8.8 | 2026-06-24 | Gogs is an open source self-hosted Git service. Prior to 0.14.3, organization team member management can be performed vi |
| CVE-2026-52801 | 8.1 | 2026-06-24 | Gogs is an open source self-hosted Git service. Prior to 0.14.3, the Gogs Mirror Settings functionality provide an alter |
| CVE-2026-52805 | 8.7 | 2026-06-24 | Gogs is an open source self-hosted Git service. Prior to 0.14.3, a Server-Side Request Forgery (SSRF) vulnerability exis |
| CVE-2026-52806 | 9.9 | 2026-06-24 | Gogs is an open source self-hosted Git service. Prior to 0.14.3, Gogs allows authenticated users to achieve Remote Code  |
| CVE-2026-52808 | 7.1 | 2026-06-24 | Gogs is an open source self-hosted Git service. Prior to 0.14.3, three API endpoints — PATCH /api/v1/repos/:owner/:repo/ |
| CVE-2026-52813 | 10.0 | 2026-06-24 | Gogs is an open source self-hosted Git service. Prior to 0.14.3, organization names containing path traversal sequences  |
| CVE-2026-10043 | 7.8 | 2026-06-24 | MosaicML Composer Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vulnerability allows remot |
| CVE-2026-2050 | 7.8 | 2026-06-24 | GIMP HDR File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote a |
| CVE-2026-39893 | 9.8 | 2026-06-24 | Cacti is an open source performance and fault management framework. In versions 1.2.30 and prior, the rfilter request va |
| CVE-2026-50551 | 9.9 | 2026-06-24 | SiYuan is an open-source personal knowledge management system. Prior to 3.7.0, SiYuan contains a stored cross-site scrip |
| CVE-2026-52794 | 7.5 | 2026-06-24 | Sentry is an error tracking and performance monitoring tool. From 24.4.0 until 26.5.2, a Regular Expression Denial of Se |
| CVE-2026-54066 | 7.5 | 2026-06-24 | SiYuan is an open-source personal knowledge management system. Prior to 3.7.0, the patch for CVE-2026-41894 ("Path Trave |
| CVE-2026-54067 | 9.9 | 2026-06-24 | SiYuan is an open-source personal knowledge management system. Prior to 3.7.0, CSS snippet body containing </style> brea |
| CVE-2026-54070 | 7.1 | 2026-06-24 | SiYuan is an open-source personal knowledge management system. Prior to 3.7.0, renderPackageREADME in kernel/bazaar/read |
| CVE-2026-54158 | 9.9 | 2026-06-24 | SiYuan is an open-source personal knowledge management system. Prior to 3.7.0, the attribute-view (database) cell render |
| CVE-2026-55454 | 9.9 | 2026-06-24 | Appsmith is a platform to build admin panels, internal tools, and dashboards. Prior to 2.1, the bundled Caddy reverse-pr |
| CVE-2026-55570 | 9.0 | 2026-06-24 | SiYuan is an open-source personal knowledge management system. Prior to 3.7.0, it does not escape the untrusted fields ( |
| CVE-2026-55759 | 7.4 | 2026-06-24 | Rocket.Chat is an open-source, secure, fully customizable communications platform. Prior to 8.5.1, 8.4.4, 8.3.6, 8.2.6,  |
| CVE-2026-55762 | 8.1 | 2026-06-24 | Rocket.Chat is an open-source, secure, fully customizable communications platform. Prior to 8.5.1, 8.4.4, 8.3.6, 8.2.6,  |
| CVE-2026-9772 | 8.8 | 2026-06-24 | Unraid Web Server FileUpload Command Injection Remote Code Execution Vulnerability. This vulnerability allows remote att |
| CVE-2026-9773 | 8.8 | 2026-06-24 | Unraid Web Server ToggleState Command Injection Remote Code Execution Vulnerability. This vulnerability allows remote at |
| CVE-2026-9776 | 7.5 | 2026-06-24 | ATEN Unizon writeFileToHttpServletResponse Directory Traversal Information Disclosure Vulnerability. This vulnerability  |
| CVE-2026-9777 | 7.2 | 2026-06-24 | ATEN Unizon restoreDB Directory Traversal Remote Code Execution Vulnerability. This vulnerability allows remote attacker |
| CVE-2026-9778 | 7.2 | 2026-06-24 | ATEN Unizon ImportDeviceList Directory Traversal Remote Code Execution Vulnerability. This vulnerability allows remote a |
| CVE-2026-9779 | 7.2 | 2026-06-24 | ATEN Unizon doCryptoHugeFileToFile Improper Verification of Cryptographic Signature Remote Code Execution Vulnerability. |
| CVE-2026-39938 | 9.8 | 2026-06-24 | Cacti is an open source performance and fault management framework. Versions 1.2.30 and prior have unauthenticated LFI t |
| CVE-2026-39955 | 9.8 | 2026-06-24 | Cacti is an open source performance and fault management framework. Versions 1.2.30 and prior have pre-authentication SQ |
| CVE-2026-39951 | 7.6 | 2026-06-25 | Cacti is an open source performance and fault management framework. Versions 1.2.30 and prior have a Stored SQL Injectio |
| CVE-2026-7569 | 8.8 | 2026-06-25 | Quest NetVault Backup viewclient Cross-Site Scripting Authentication Bypass Vulnerability. This vulnerability allows rem |
| CVE-2026-7570 | 8.8 | 2026-06-25 | Quest NetVault Backup NVBUDashboard SQL Injection Remote Code Execution Vulnerability. This vulnerability allows remote  |
| CVE-2026-9780 | 8.8 | 2026-06-25 | Quest NetVault Backup addclient3 Cross-Site Scripting Authentication Bypass Vulnerability. This vulnerability allows rem |
| CVE-2026-9781 | 8.8 | 2026-06-25 | Quest NetVault Backup NVBURASDevice SQL Injection Remote Code Execution Vulnerability. This vulnerability allows remote  |
| CVE-2026-9782 | 8.8 | 2026-06-25 | Quest NetVault Backup NVBUDeviceDrive SQL Injection Remote Code Execution Vulnerability. This vulnerability allows remot |
| CVE-2026-9783 | 8.8 | 2026-06-25 | Quest NetVault Backup NVBURemovableMedia SQL Injection Remote Code Execution Vulnerability. This vulnerability allows re |
| CVE-2026-9784 | 8.8 | 2026-06-25 | Quest NetVault Backup NVBULibraryPort SQL Injection Remote Code Execution Vulnerability. This vulnerability allows remot |
| CVE-2026-9785 | 8.8 | 2026-06-25 | Quest NetVault Backup NVBULibrarySlot SQL Injection Remote Code Execution Vulnerability. This vulnerability allows remot |
| CVE-2026-9786 | 8.8 | 2026-06-25 | Quest NetVault Backup NVBUDashboard SQL Injection Remote Code Execution Vulnerability. This vulnerability allows remote  |
| CVE-2026-9787 | 8.8 | 2026-06-25 | Quest NetVault Backup NVBULogDaemon Command Injection Remote Code Execution Vulnerability. This vulnerability allows rem |
| CVE-2026-57589 | 7.4 | 2026-06-25 | sys/kern/sysv_sem.c in OpenBSD through 7.9 has a use-after-free allowing local privilege escalation to root. This is a c |
| CVE-2026-9154 | 7.1 | 2026-06-25 | Arbitrary File Write vulnerability in Rapid7 InsightConnect Sed Plugin on Linux allows authenticated attackers to write  |
| CVE-2026-9155 | 8.8 | 2026-06-25 | OS Command Injection vulnerability in Rapid7 InsightConnect Sed Plugin on Linux allows authenticated attackers to execut |
| CVE-2026-8592 | 7.7 | 2026-06-25 | OS Command Injection vulnerability in the process_string action of Rapid7 InsightConnect AWK Plugin on Linux allows remo |
| CVE-2026-8660 | 7.7 | 2026-06-25 | OS Command Injection vulnerability in the ping action of Rapid7 InsightConnect Ping Plugin on Linux allows remote attack |
| CVE-2026-8665 | 7.7 | 2026-06-25 | OS Command Injection vulnerability in the TR action of Rapid7 InsightConnect Translate Plugin on Linux allows remote att |
| CVE-2026-8666 | 7.7 | 2026-06-25 | OS Command Injection vulnerability in the traceroute action of Rapid7 InsightConnect Traceroute Plugin on Linux allows r |
| CVE-2026-12077 | 7.5 | 2026-06-25 | The Dokan Pro plugin for WordPress is vulnerable to time-based SQL Injection via the via 'latitude' and 'longitude' para |
| CVE-2026-10086 | 8.7 | 2026-06-25 | GitLab has remediated an issue in GitLab EE affecting all versions from 16.4 before 18.11.6, 19.0 before 19.0.3, and 19. |
| CVE-2026-10712 | 8.0 | 2026-06-25 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 18.10 before 18.11.6, 19.0 before 19.0.3, and |
| CVE-2026-12053 | 8.6 | 2026-06-25 | GitLab has remediated an issue in GitLab EE affecting all versions from 19.1 before 19.1.1 that under certain conditions |
| CVE-2026-13311 | 7.5 | 2026-06-25 | shell-quote prior to 1.8.5 finalizes parsed tokens in parse() using Array.prototype.concat as a reduce accumulator, whic |
| CVE-2026-12937 | 7.5 | 2026-06-25 | The Tourfic – AI Powered Travel Booking, Hotel Booking & Car Rental WordPress Plugin plugin for WordPress is vulnerable  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2025-67038 | Lantronix / EDS5000 | 2026-06-23 | 2026-06-26 | Unknown |
| CVE-2026-34910 | Ubiquiti / UniFi OS | 2026-06-23 | 2026-06-26 | Unknown |
| CVE-2026-34909 | Ubiquiti / UniFi OS | 2026-06-23 | 2026-06-26 | Unknown |
| CVE-2026-34908 | Ubiquiti / UniFi OS | 2026-06-23 | 2026-06-26 | Unknown |
| CVE-2026-20253 | Splunk / Enterprise | 2026-06-18 | 2026-06-21 | Unknown |

---

*Total entries in CISA KEV catalog: 1627*