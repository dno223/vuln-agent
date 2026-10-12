# Vulnerability Intelligence Report

**Date:** 2026-10-12  
**Generated:** 2026-10-12T17:23:54Z  

---

## Executive Summary

Our environment faces significant exposure across 129 high-severity CVEs, including a critical CVSS 9.8 modem stack buffer overflow and multiple remote code execution vulnerabilities. Five newly added CISA Known Exploited Vulnerabilities (KEV) — including long-standing flaws in BIND, Apache Struts, and ProFTPD — confirm active threat actor exploitation of legacy weaknesses. While no monitored assets currently match KEV entries, the breadth of high-severity findings and the KEV additions demand immediate remediation action. Key risks span network routing, Bluetooth stacks, entropy drivers, and third-party components, any of which could enable unauthorized access, data exfiltration, or full system compromise.

---

## Risk Narrative

Threat actors are actively exploiting known vulnerabilities — as evidenced by five KEV additions in a single week spanning software from 2015 onward — demonstrating that unpatched legacy systems remain high-value targets. The CVSS 9.8 modem buffer overflow represents a critical, potentially wormable attack surface requiring no authentication. Remote code execution flaws in database tooling and plugin systems expand the blast radius for supply chain and web-facing attacks. Embedded system vulnerabilities in Zephyr RTOS components introduce risk in IoT and industrial environments where patching cadence is slow. Collectively, these findings suggest elevated risk of initial access, privilege escalation, and lateral movement across both enterprise and embedded infrastructure if remediation is not prioritized immediately.

---

## Prioritized Action Items

1. Immediately patch or mitigate CVE-2026-66086 (CVSS 9.8 modem stack buffer overflow) as it enables unauthenticated remote code execution with no user interaction required.
2. Audit and remediate all systems running software affected by the five newly added CISA KEV entries — BIND, Apache Struts, Strapi, ONLYOFFICE, and ProFTPD — within 24 to 48 hours.
3. Patch CVE-2026-108963 and CVE-2026-108980 (both CVSS 8.8) immediately, as they allow remote code execution and directory traversal with root-level write access respectively.
4. Conduct an inventory of all Zephyr RTOS deployments to assess exposure to CVE-2026-19669, CVE-2026-19736, and CVE-2026-19935 affecting fuel gauge syscalls, TRNG entropy, and Bluetooth L2CAP.
5. Establish a recurring KEV monitoring process to ensure any future overlap between monitored assets and CISA's catalog triggers an automated alert and escalation within one business day.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-19577 | 7.1 | 2026-10-11 | net_route_ipv6_packet() in subsys/net/ip/route_ipv6.c resolved the nexthop's link-layer address with net_nbr_get_lladdr( |
| CVE-2026-19669 | 7.8 | 2026-10-11 | The user-mode syscall verifiers z_vrfy_fuel_gauge_get_props() and z_vrfy_fuel_gauge_set_props() in drivers/fuel_gauge/fu |
| CVE-2026-19736 | 7.8 | 2026-10-11 | The NXP MCUX TRNG entropy driver in drivers/entropy/entropy_mcux_trng.c passed the caller's byte count straight to the v |
| CVE-2026-19935 | 7.5 | 2026-10-11 | The Bluetooth LE host queues received L2CAP connection-oriented channel (CoC) data for deferred processing through a str |
| CVE-2026-108963 | 8.8 | 2026-10-11 | databasement before 1.8.2 allows remote code execution because it runs certain commands (e.g., mariadb-dump) with a data |
| CVE-2026-108976 | 7.8 | 2026-10-11 | GNU Emacs before 31.2 (and TRAMP through 2.8.2) allows OS command injection via a filename because tramp-user-regexp has |
| CVE-2026-108783 | 7.3 | 2026-10-12 | A security vulnerability has been detected in PRVTPRO Amnezia-Web-Panel up to 1.6.2/1.7.2. This affects an unknown part  |
| CVE-2026-108980 | 8.8 | 2026-10-12 | Blinko through 1.8.8 allows directory traversal, overwriting startup files as root, via installPlugin. It builds the plu |
| CVE-2026-66086 | 9.8 | 2026-10-12 | In the modem OTA stack, there is a possible stack-based buffer overflow due to improper validation of scheduling informa |
| CVE-2026-108985 | 7.1 | 2026-10-12 | ZDR decoding in libnfs through 6.0.2 before 7613236 has an out-of-bounds write related to lib/libnfs-zdr.c with libnfs_z |
| CVE-2026-108798 | 7.3 | 2026-10-12 | A vulnerability was found in ZKTeco BioTime 9.5.6 Build 20260130.3206. This issue affects some unknown processing. The m |
| CVE-2026-108799 | 7.3 | 2026-10-12 | A vulnerability was determined in jackq XCMS up to 3fab5342cc509945a7ce1b8ec39d19f701b89261. Impacted is the function Pu |
| CVE-2026-87690 | 8.8 | 2026-10-12 | The Metasploit Framework post module post/apple_ios/gather/ios_image_gather is affected by a relative path traversal vul |
| CVE-2026-108804 | 10.0 | 2026-10-12 | A vulnerability was detected in TRENDnet TEW-751DR, TEW-752DRU and TEW733GR 1.03B01/1.03B03. Affected is the function fw |
| CVE-2026-108805 | 7.3 | 2026-10-12 | A flaw has been found in krupalshah EmployeeRecruitmentSystem up to 922ff6d208278282e7c8e36d70d9ae356adec9fe. Affected b |
| CVE-2026-108806 | 7.3 | 2026-10-12 | A vulnerability has been found in krupalshah EmployeeRecruitmentSystem up to 922ff6d208278282e7c8e36d70d9ae356adec9fe. A |
| CVE-2026-108807 | 7.3 | 2026-10-12 | A vulnerability was found in krupalshah EmployeeRecruitmentSystem up to 922ff6d208278282e7c8e36d70d9ae356adec9fe. This a |
| CVE-2026-78355 | 8.7 | 2026-10-12 | A path traversal vulnerability in the OTRS SendSupportBundle functionality allows an authenticated administrator to refe |
| CVE-2026-78357 | 9.1 | 2026-10-12 | Previously issued authentication tokens are not immediately invalidated when an OTRS agent or customer user account is d |
| CVE-2026-93582 | 9.4 | 2026-10-12 | The HTTP Basic Authentication modules in ((OTRS)) Community Edition 6 and prior accept the authenticated username from e |
| CVE-2026-108818 | 7.3 | 2026-10-12 | A vulnerability was identified in agno-agi agno up to 2.7.3/3.0.6. This affects the function get_authentication_dependen |
| CVE-2026-108819 | 7.3 | 2026-10-12 | A security flaw has been discovered in agno-agi agno up to 3.0.6/3.1.1. This vulnerability affects the function exec of  |
| CVE-2026-103902 | 7.5 | 2026-10-12 | Improper verification of cryptographic signature vulnerability in DigiDoc libdigidocpp, DigiDoc DigiDoc4, DigiDoc DigiDo |
| CVE-2026-103903 | 8.8 | 2026-10-12 | An incorrect authorization vulnerability in the WinBox
authentication flow of MikroTik RouterOS allows a remote authenti |
| CVE-2026-105407 | 8.8 | 2026-10-12 | An OS Command Injection vulnerability affecting Tuleap Enterprise Edition from 17.0 through 17.5 could allow an attacker |
| CVE-2026-105408 | 8.7 | 2026-10-12 | A Stored Cross-site Scripting (XSS) vulnerability affecting Tuleap Enterprise Edition from 17.0 through 17.5 could allow |
| CVE-2026-105409 | 8.7 | 2026-10-12 | A Stored Cross-site Scripting (XSS) vulnerability affecting Tuleap Enterprise Edition from 17.0 through 17.5 could allow |
| CVE-2026-105410 | 8.7 | 2026-10-12 | A Stored Cross-site Scripting (XSS) vulnerability affecting Tuleap Enterprise Edition from 17.0 through 17.5 could allow |
| CVE-2026-105411 | 8.1 | 2026-10-12 | An Authorization Bypass Through User-Controlled Key vulnerability affecting Tuleap Enterprise Edition from 17.0 through  |
| CVE-2026-105412 | 7.1 | 2026-10-12 | An SQL Injection vulnerability affecting Tuleap Enterprise Edition 17.5 could allow an attacker to have read access the  |
| CVE-2026-108826 | 7.3 | 2026-10-12 | A vulnerability was found in Zen Cart up to 2.2.2. This impacts the function zen_db_perform in the library includes/modu |
| CVE-2026-108836 | 7.3 | 2026-10-12 | A vulnerability has been found in Ollama up to 0.34.1. The affected element is the function IsValid of the file types/mo |
| CVE-2026-108953 | 7.8 | 2026-10-12 | mac-shell-mcp before 2.0.0 contains an OS command injection vulnerability that allows MCP clients to bypass the command  |
| CVE-2026-109164 | 7.1 | 2026-10-12 | TDuck survey form through 6.0 contains an insecure direct object reference vulnerability that allows authenticated users |
| CVE-2026-109185 | 8.8 | 2026-10-12 | jshERP through 3.6 contains a missing authorization vulnerability in the UserController updateUser handler that allows a |
| CVE-2026-109186 | 8.8 | 2026-10-12 | jshERP through 3.6 contains a mass assignment vulnerability in the UserController update handler that allows authenticat |
| CVE-2026-52903 | 8.8 | 2026-10-12 | A deserialization of untrusted data vulnerability was found in ManageIQ. The YamlLoadAliases module overrides YAML.safe_ |
| CVE-2026-93695 | 7.4 | 2026-10-12 | In Progress ShareFile Storage Zones Controller v5.12.6 and below, FileCopyService uses a remote file identifier when con |
| CVE-2026-108892 | 10.0 | 2026-10-12 | A vulnerability was determined in Linksys E1700 1.0.0.4.003. This vulnerability affects the function ssid1MACFilter of t |
| CVE-2026-108893 | 9.9 | 2026-10-12 | A vulnerability was identified in Linksys E1700 up to 1.0.0.4.003. This issue affects the function setVlan of the file / |
| CVE-2026-108894 | 9.9 | 2026-10-12 | A security flaw has been discovered in Linksys E1700 1.0.0.4.003. Impacted is the function addStaticRoute of the file /g |
| CVE-2026-109199 | 8.8 | 2026-10-12 | LogicalDOC Community Edition through 9.3 contains a code injection vulnerability that allows authenticated users to exec |
| CVE-2026-109201 | 8.3 | 2026-10-12 | LogicalDOC Community Edition through 9.3 contains a missing authorization vulnerability in SoapDocumentService operation |
| CVE-2026-109205 | 7.5 | 2026-10-12 | LogicalDOC Community Edition through 9.3 contains an unauthenticated file upload vulnerability in the UploadServlet that |
| CVE-2026-109225 | 7.5 | 2026-10-12 | SGLang through 0.5.21 contains an unbounded memory allocation vulnerability that allows unauthenticated remote attackers |
| CVE-2026-109226 | 7.5 | 2026-10-12 | SGLang through 0.5.21 contains a decompression amplification vulnerability in load_audio that allows remote attackers to |
| CVE-2026-109227 | 7.5 | 2026-10-12 | SGLang through 0.5.21 contains an unbounded memory allocation vulnerability in preprocess_video in qwen_vl.py that decod |
| CVE-2026-109228 | 7.5 | 2026-10-12 | SGLang through 0.5.21 contains a resource budget bypass vulnerability that allows remote attackers to override GLM-V vid |
| CVE-2026-109229 | 7.5 | 2026-10-12 | SGLang through 0.5.21 contains a denial of service vulnerability that disables Pillow decompression bomb protection proc |
| CVE-2026-12613 | 8.8 | 2026-10-12 | Deserialization of untrusted data vulnerability in Ministry of Justice General Directorate of Information Technology UYA |
| CVE-2026-18390 | 7.8 | 2026-10-12 | Improper neutralization of special elements used in an OS command ('OS command injection') vulnerability in Ministry of  |
| CVE-2026-103521 | 7.2 | 2026-10-12 | In Thelia v2.6.0, the document upload endpoint properly blocks the upload of executable file types, but the document upd |
| CVE-2026-103522 | 7.2 | 2026-10-12 | In Thelia v2.6.0, the store banner upload feature performs insufficient filetype validation that relies exclusively on c |
| CVE-2026-108094 | 7.8 | 2026-10-12 | A use-after-free flaw was found in mutter in the Wayland color-management ICC image-description path. A local attacker w |
| CVE-2026-108895 | 9.9 | 2026-10-12 | A weakness has been identified in Linksys E1700 1.0.0.4.003. The affected element is the function setDMZ of the file /go |
| CVE-2026-108896 | 9.9 | 2026-10-12 | A vulnerability was found in Linksys E1700 1.0.0.4.003. This affects the function setLinksysIpv6 of the file /goform/set |
| CVE-2026-109390 | 9.8 | 2026-10-12 | AnyDesk before 8.0.3 allows unauthenticated remote attackers to execute arbitrary code via a heap-based buffer overflow, |
| CVE-2026-108899 | 7.3 | 2026-10-12 | A flaw has been found in tobychui zoraxy up to 3.3.4. This impacts the function handleBasicAuth of the file mod/dynamicp |
| CVE-2026-108900 | 7.3 | 2026-10-12 | A vulnerability has been found in Exponent CMS up to 3.0.2patch2. Affected is the function userLogin of the file xmlrpc. |
| CVE-2026-108906 | 7.2 | 2026-10-12 | A vulnerability has been found in Netcore NR268 1.7.121109. This affects the function filter_arp_put_file_cgi of the fil |
| CVE-2026-109391 | 8.1 | 2026-10-12 | Square Squash through commit e73f280 contains an insecure deserialization vulnerability that allows unauthenticated atta |
| CVE-2026-109394 | 7.4 | 2026-10-12 | Thirty bees through 1.7.0 contains an authentication bypass vulnerability in PasswordController::resolveCustomer() that  |
| CVE-2026-109397 | 7.2 | 2026-10-12 | Thelia before 3.1.2 and 3.2.x before 3.2.1 contains an unrestricted file upload vulnerability that allows authenticated  |
| CVE-2026-109398 | 7.5 | 2026-10-12 | Gumlet php-image-resize before 3.0.1 contains a denial of service vulnerability because the ImageResize constructor in l |
| CVE-2026-109399 | 8.1 | 2026-10-12 | SWUpdate through 2026.05.1 contains an improper certificate validation vulnerability in crypto/swupdate_cms_verify_opens |
| CVE-2026-85947 | 9.9 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain an authorization flaw in c |
| CVE-2026-85948 | 9.9 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain an XQuery injection flaw i |
| CVE-2026-85949 | 8.1 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 may record security-sensitive info |
| CVE-2026-85950 | 8.4 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain an authorization flaw that |
| CVE-2026-85951 | 8.5 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 on Azure contain a server-side req |
| CVE-2026-85952 | 8.5 | 2026-10-12 | Affected Linux-based Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain a ser |
| CVE-2026-85953 | 8.5 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain privileged legacy InfoStud |
| CVE-2026-85954 | 8.6 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 can evaluate user-controlled value |
| CVE-2026-85955 | 9.9 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 allow a remote attacker with query |
| CVE-2026-85956 | 9.6 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 allow a remote attacker with deleg |
| CVE-2026-9191 | 9.6 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 do not sufficiently isolate user-s |
| CVE-2026-108907 | 10.0 | 2026-10-12 | A vulnerability was determined in Netcore NR268 1.7.121109. Affected is the function user_ok of the component CGI Execut |
| CVE-2026-108914 | 9.9 | 2026-10-12 | A flaw has been found in Edimax BR-6208AC 1.32. Affected by this issue is some unknown functionality of the file /goform |
| CVE-2026-109237 | 8.1 | 2026-10-12 | Crawl4AI from 0.9.0 before 0.9.4 contains an untrusted-config gate bypass that allows non-admin API clients to construct |
| CVE-2026-109238 | 8.6 | 2026-10-12 | Crawl4AI 0.7.0 before 0.9.4 contains a server-side request forgery vulnerability that allows API clients to reach intern |
| CVE-2026-109242 | 7.1 | 2026-10-12 | FreeRDP before 3.0.0 and 3.6.0 before 3.32.0 renders uninitialized heap memory from un-decoded progressive tiles because |
| CVE-2026-109286 | 8.1 | 2026-10-12 | Open WebUI from 0.7.0 before 0.11.4 contains a cross-origin message handling vulnerability in SyncStatsModal that allows |
| CVE-2026-109290 | 7.3 | 2026-10-12 | Open WebUI from 0.11.1 before 0.11.4 contains a stored cross-site scripting vulnerability in DocxPreview.svelte that all |
| CVE-2026-109291 | 7.3 | 2026-10-12 | Open WebUI from 0.6.33 before 0.11.4 contains a cross-site scripting vulnerability that allows authenticated users to ex |
| CVE-2026-109305 | 8.8 | 2026-10-12 | Craft CMS from 5.10.2 before 5.10.14 contains a Twig sandbox bypass that allows non-admin users to invoke PHP callables  |
| CVE-2026-109308 | 8.8 | 2026-10-12 | Craft CMS 4.0.0 before 4.18.7 and 5.0.0 before 5.10.14 passes the raw 'updates' request parameter in AppController::acti |
| CVE-2026-109312 | 8.1 | 2026-10-12 | Grav Login plugin 2.7.0 before 3.9.9 contains an authentication bypass in processUserProfile(), which checks that the se |
| CVE-2026-109313 | 8.1 | 2026-10-12 | Grav Login plugin 2.7.0 before 3.9.9 contains an authentication bypass vulnerability that allows attackers with a valid  |
| CVE-2026-109314 | 7.3 | 2026-10-12 | Grav Login plugin 1.2.0 before 3.9.9 contains an information disclosure vulnerability that allows publishers to obtain p |
| CVE-2026-109317 | 7.2 | 2026-10-12 | Grav grav-plugin-api before 1.0.36 contains a privilege escalation vulnerability that allows delegated user managers to  |
| CVE-2026-109318 | 8.8 | 2026-10-12 | Grav Git Sync 1.0.2 through 3.4.12 contains a command injection vulnerability that allows authenticated content editors  |
| CVE-2026-109321 | 9.1 | 2026-10-12 | Grav Login OAuth plugin (grav-plugin-login-oauth) before 1.4.3 provisions OAuth accounts as ordinary Grav users with a d |
| CVE-2026-109325 | 7.5 | 2026-10-12 | Grav from 2.0.22 before 2.1.7 contains an authentication bypass vulnerability in the Clockwork profiler that trusts loop |
| CVE-2026-109326 | 7.5 | 2026-10-12 | Grav before 2.1.7 contains an information disclosure vulnerability because bundled nginx, lighttpd, IIS, and Caddy 2 con |
| CVE-2026-109331 | 7.4 | 2026-10-12 | Network-AI from 5.14.0 before 5.15.2 contains a security control bypass vulnerability in the ClaudeHookBridge PreToolUse |
| CVE-2026-109334 | 8.1 | 2026-10-12 | SurrealDB before 3.3.0 does not check the caller-selected namespace or database against the level at which a namespace-  |
| CVE-2026-109341 | 7.1 | 2026-10-12 | SurrealDB before 3.3.0 contains an authorization bypass vulnerability that allows callers with table-level write permiss |
| CVE-2026-109343 | 8.1 | 2026-10-12 | SurrealDB before 3.3.0 allows cross-tenant access because the SurrealQL USE statement switches a session to any namespac |
| CVE-2026-109346 | 8.1 | 2026-10-12 | better-auth from 1.3.8-beta.3 before 1.7.0-rc.3 contains a UI misrepresentation vulnerability in the deviceAuthorization |
| CVE-2026-109347 | 7.2 | 2026-10-12 | Adminer before 6.1.1 contains a remote code execution vulnerability that allows authenticated SQLite users to bypass ATT |
| CVE-2026-109353 | 7.1 | 2026-10-12 | LibreNMS before 26.9.0 contains an SQL injection vulnerability that allows unprivileged users to inject SQL by supplying |
| CVE-2026-109357 | 8.1 | 2026-10-12 | LibreNMS before 26.9.0 contains an LDAP filter injection in ldap-authorization and ad-authorization modes because userna |
| CVE-2026-109358 | 7.8 | 2026-10-12 | Edgeless Systems Contrast 1.8.0 before 1.24.1 contains an incorrect permissions vulnerability where the node installer w |
| CVE-2026-109359 | 7.7 | 2026-10-12 | Contrast 1.8.0 before 1.24.1 contains an improper verification vulnerability in Coordinator peer recovery that fails to  |
| CVE-2026-109360 | 7.5 | 2026-10-12 | MONAI 0.4.0 before 1.6.1 contains a remote code execution vulnerability that allows on-path attackers to execute code by |
| CVE-2026-109361 | 7.3 | 2026-10-12 | MONAI 1.2.0 before 1.6.1 contains an insecure deserialization vulnerability in nnUNetV2Runner that unpickles the postpro |
| CVE-2026-109363 | 7.5 | 2026-10-12 | ZcashFoundation Zebra 6.4.0 before 6.4.2 parses version 6 transactions carrying a pre-NU6.3 consensus branch ID, but the |
| CVE-2026-109371 | 8.2 | 2026-10-12 | ZITADEL 3.0.0 before 4.18.0 contains a missing authentication vulnerability in the hosted Login V1 UI, where the change- |
| CVE-2026-109372 | 8.7 | 2026-10-12 | ZITADEL 4.x before 4.19.2 and 3.x through 3.4.15 contains an authentication bypass in the SAML identity-provider intent  |
| CVE-2026-109373 | 8.1 | 2026-10-12 | ZITADEL 3.0.0 before 4.19.2 contains an authentication bypass vulnerability in the Login V2 UI that allows unauthenticat |
| CVE-2026-75888 | 7.7 | 2026-10-12 | A flaw was found in the OpenShift console. An authenticated console user can exploit a Server-Side Request Forgery (SSRF |
| CVE-2026-85957 | 7.5 | 2026-10-12 | Affected Progress MarkLogic Server 11.x releases before 11.3.7 use a SAML parser configuration that can process external |
| CVE-2026-85958 | 7.5 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain an authentication validati |
| CVE-2026-85959 | 7.5 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 do not consistently record success |
| CVE-2026-85960 | 7.5 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 use predictable CSRF tokens in Que |
| CVE-2026-85961 | 7.5 | 2026-10-12 | On Azure deployments, Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 may record s |
| CVE-2026-85962 | 7.5 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain an improper authentication |
| CVE-2026-85963 | 7.5 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 include deprecated OpsDirector fun |
| CVE-2026-85964 | 7.7 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 allow an authenticated Query Conso |
| CVE-2026-85965 | 8.0 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain memory-safety defects in t |
| CVE-2026-85966 | 7.7 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 do not sufficiently restrict acces |
| CVE-2026-85968 | 7.1 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 contain an out-of-bounds read vulnerability in certain query-proce |
| CVE-2026-85969 | 7.1 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain an out-of-bounds write vul |
| CVE-2026-85970 | 7.1 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 enable XML external entity process |
| CVE-2026-85971 | 7.1 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 assign overly permissive operating |
| CVE-2026-85972 | 7.4 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 do not sufficiently verify the ide |
| CVE-2026-85973 | 7.4 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 may use cleartext transport for certain cluster-management communi |
| CVE-2026-85974 | 7.4 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 do not consistently validate TLS c |
| CVE-2026-85975 | 7.5 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 may use cleartext transport for Am |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2015-5477 | ISC / BIND | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2016-3081 | Apache / Struts | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2023-22894 | Strapi / Strapi | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2021-3199 | ONLYOFFICE / Docs | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2015-3306 | ProFTPD / ProFTPD | 2026-10-08 | 2026-10-11 | Unknown |

---

*Total entries in CISA KEV catalog: 1739*