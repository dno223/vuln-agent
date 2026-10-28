# Vulnerability Intelligence Report

**Date:** 2026-10-28  
**Generated:** 2026-10-28T14:51:45Z  

---

## Executive Summary

Our environment faces significant exposure from 204 high-severity CVEs, including critical vulnerabilities in TeamViewer, Autodesk Fusion, Grav CMS, and Nextcloud. The most urgent concern is a CVSS 9.6 CSRF vulnerability in Newsletters Lite and a CVSS 8.8 integer overflow in TeamViewer remote-control components. Additionally, six new CISA Known Exploited Vulnerabilities were added this week affecting Adobe Commerce, Google Brotli, PHP, and Arista VeloCloud — all requiring immediate remediation under federal guidance. No monitored CVEs currently overlap with the KEV catalog, which is a positive indicator, but the volume and severity of open findings demand prompt action.

---

## Risk Narrative

The current threat landscape reflects a dangerous combination of remotely exploitable application vulnerabilities and actively weaponized exploits confirmed by CISA. TeamViewer's widespread enterprise deployment amplifies the risk of the integer overflow and out-of-bounds write vulnerabilities, which could enable remote code execution at scale. The Grav CMS authorization bypass exposes web-facing infrastructure to unauthenticated attackers. The six new KEV additions signal active threat actor exploitation of commerce platforms, web runtimes, and network orchestration tools — directly threatening revenue operations and network integrity. Collectively, these vulnerabilities could result in data breaches, ransomware deployment, regulatory penalties, and operational disruption if not addressed within defined remediation windows.

---

## Prioritized Action Items

1. Immediately patch or disable TeamViewer Full Client, Portable, and Remote Control App to address the CVSS 8.8 integer overflow and CVSS 8.8 out-of-bounds write vulnerabilities before remote exploitation occurs.
2. Apply emergency patches for all six newly added CISA KEV entries — Adobe Commerce, Google Brotli, PHP, and Arista VeloCloud — as these represent actively exploited vulnerabilities requiring compliance-driven remediation.
3. Remediate the CVSS 9.6 CSRF vulnerability in Newsletters Lite (CVE-2026-116863) immediately by updating to a patched version or removing the plugin from all WordPress installations.
4. Upgrade Grav CMS to version 1.7.53.6 or later to eliminate the unauthenticated authorization bypass in the Debugger component that exposes web infrastructure to unauthorized access.
5. Audit and restrict installation privileges for TeamViewer Remote Management products to mitigate the three DLL hijacking and race condition vulnerabilities affecting Windows installer processes.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-117604 | 7.5 | 2026-10-27 | Grav from 1.7.53.3 before 1.7.53.6 contains an authorization bypass in Debugger::isDebuggerRequestAuthorized() that allo |
| CVE-2026-104189 | 7.5 | 2026-10-27 | The 3D Viewer for Nextcloud is a comprehensive 3D model viewer application for Nextcloud that supports multiple 3D file  |
| CVE-2026-107672 | 8.8 | 2026-10-27 | A maliciously crafted .stack.json file can trigger a trusted Markdown injection vulnerability in Autodesk Fusion Post Pr |
| CVE-2026-111582 | 7.3 | 2026-10-27 | A DLL loading vulnerability in the
TeamViewer Remote Management Monitoring installer for Windows prior to version 26.10. |
| CVE-2026-111583 | 7.3 | 2026-10-27 | Improper access control in the installer
staging directory used by TeamViewer Full Client and Host prior to version
15.8 |
| CVE-2026-111584 | 7.3 | 2026-10-27 | A race condition in the installation
process of TeamViewer Remote Management - Patch Management for Windows prior to
ver |
| CVE-2026-111585 | 8.8 | 2026-10-27 | An integer overflow in the remote-control
screen processing component of TeamViewer clients (Full Client, Portable and R |
| CVE-2026-116863 | 9.6 | 2026-10-27 | Cross-Site Request Forgery (CSRF) vulnerability in Tribulant Software Newsletters newsletters-lite allows Cross Site Req |
| CVE-2026-117511 | 7.3 | 2026-10-27 | A vulnerability has been found in desmondmorris node-tesseract up to 0.2.7. Affected by this issue is the function proce |
| CVE-2026-92372 | 8.8 | 2026-10-27 | An out-of-bounds write vulnerability in the
screen-image decoder of TeamViewer Full Client for Linux and macOS prior to
 |
| CVE-2026-92374 | 7.8 | 2026-10-27 | A time-of-check time-of-use (TOCTOU) race condition combined with improper symbolic link handling in the privileged help |
| CVE-2026-92375 | 7.8 | 2026-10-27 | An improper access control vulnerability in
the IPC communication between TeamViewer Full Client or Host prior to versio |
| CVE-2026-92376 | 7.8 | 2026-10-27 | Improper authentication in the
inter-process communication (IPC) mechanism of TeamViewer Remote Management
Monitoring fo |
| CVE-2026-92377 | 7.8 | 2026-10-27 | Improper access control in the Patch
Management update mechanism of TeamViewer Full Client and Host for Windows
prior to |
| CVE-2026-102636 | 7.1 | 2026-10-27 | A maliciously crafted HTML payload in a design name, when displayed after another user opens the manipulated design, can |
| CVE-2026-102637 | 7.1 | 2026-10-27 | A maliciously crafted HTML payload in the documentName parameter of a Fusion protocol URL, when the protocol URL is invo |
| CVE-2026-102638 | 7.1 | 2026-10-27 | A maliciously crafted HTML payload in the description of an electronic library (.lbr) file, when displayed in the Librar |
| CVE-2026-104349 | 7.3 | 2026-10-27 | Creative Cloud Desktop is affected by an Uncontrolled Search Path Element vulnerability that could result in arbitrary c |
| CVE-2026-104350 | 9.3 | 2026-10-27 | Adobe Campaign Classic (ACC) is affected by a reflected Cross-Site Scripting (XSS) vulnerability. An attacker could expl |
| CVE-2026-104351 | 9.9 | 2026-10-27 | Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability t |
| CVE-2026-104353 | 9.9 | 2026-10-27 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an OS Command ('OS Co |
| CVE-2026-104354 | 9.1 | 2026-10-27 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL  |
| CVE-2026-105489 | 9.9 | 2026-10-27 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL  |
| CVE-2026-105779 | 9.1 | 2026-10-27 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL  |
| CVE-2026-105780 | 9.9 | 2026-10-27 | Adobe Campaign Classic (ACC) is affected by an Incorrect Authorization vulnerability that could result in arbitrary code |
| CVE-2026-105781 | 10.0 | 2026-10-27 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL  |
| CVE-2026-109089 | 7.5 | 2026-10-27 | A buffer overflow when handling DEVICE_RESOLUTION in libXi before 1.8.4 could overflow a heap, triggered by a malicious  |
| CVE-2026-109090 | 7.5 | 2026-10-27 | A malicious X server could cause a heap overflow by injecting a large DEVICE_ENABLE reply when processed by libXi before |
| CVE-2026-112353 | 8.2 | 2026-10-27 | GFI KerioConnect (Kerio Connect) before 10.0.8 Patch 2 contains a stored cross-site scripting vulnerability in the Webma |
| CVE-2026-113775 | 7.8 | 2026-10-27 | A maliciously crafted dynamic library, when loaded from an arbitrary path through the TextCommands.LoadDll command expos |
| CVE-2026-114595 | 9.8 | 2026-10-27 | In EPICS Base release 7.0.10 and prior, an integer overflow in network request processing can cause memory to be allocat |
| CVE-2026-114596 | 8.2 | 2026-10-27 | In EPICS Base release 7.0.10 and prior, an improper validation of message length values during protocol parsing can trig |
| CVE-2026-114597 | 7.5 | 2026-10-27 | In EPICS Base release 7.0.10 and prior, an insufficient validation of element or length values in a network message can  |
| CVE-2026-114598 | 7.5 | 2026-10-27 | In EPICS Base release 7.0.10 and prior, an insufficient validation of element or length values in a network message can  |
| CVE-2026-116672 | 8.8 | 2026-10-27 | Authlib is a Python library which builds OAuth and OpenID Connect servers. From 0.15 until 1.9.1, the documented ClientC |
| CVE-2026-117512 | 7.3 | 2026-10-27 | A vulnerability was found in oretnom23 php-travel-agency-system. This affects an unknown part of the file admin/employee |
| CVE-2026-117513 | 7.3 | 2026-10-27 | A vulnerability was determined in oretnom23 php-travel-agency-system. This vulnerability affects unknown code of the fil |
| CVE-2026-117514 | 7.3 | 2026-10-27 | A vulnerability was identified in oretnom23 php-travel-agency-system. This issue affects some unknown processing of the  |
| CVE-2026-48360 | 9.6 | 2026-10-27 | Adobe Connect is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could resul |
| CVE-2026-48379 | 7.8 | 2026-10-27 | Substance3D - Painter is affected by a Stack-based Buffer Overflow vulnerability that could result in arbitrary code exe |
| CVE-2026-57201 | 7.5 | 2026-10-27 | Asterisk is an open source private branch exchange and telephony toolkit. Prior to Asterisk 20.20.1, 21.12.3, 22.10.1, 2 |
| CVE-2026-77167 | 7.5 | 2026-10-27 | Abusing the federated share endpoint, an attacker can write arbitrary rows into the oc_share_external database table. Th |
| CVE-2026-108303 | 8.8 | 2026-10-27 | Tanium addressed an unauthorized code execution vulnerability in Certificate Manager. |
| CVE-2026-108304 | 7.8 | 2026-10-27 | Tanium addressed a local privilege escalation vulnerability in End-User Notifications. |
| CVE-2026-108305 | 7.8 | 2026-10-27 | Tanium addressed a local privilege escalation vulnerability in End-User Notifications. |
| CVE-2026-108306 | 7.8 | 2026-10-27 | Tanium addressed a local privilege escalation vulnerability in End-User Notifications. |
| CVE-2026-108307 | 7.8 | 2026-10-27 | Tanium addressed a heap-based buffer overflow vulnerability in Index. |
| CVE-2026-108329 | 8.8 | 2026-10-27 | Tanium addressed an unauthorized code execution vulnerability in Threat Response. |
| CVE-2026-116647 | 7.1 | 2026-10-27 | Tanium addressed an improper output sanitization vulnerability in Comply. |
| CVE-2026-116649 | 7.1 | 2026-10-27 | Tanium addressed an improper output sanitization vulnerability in Enforce. |
| CVE-2026-116656 | 7.5 | 2026-10-27 | Tanium addressed an uncontrolled resource consumption vulnerability in Enforce. |
| CVE-2026-116662 | 7.5 | 2026-10-27 | Tanium addressed a compression bomb vulnerability in Enforce. |
| CVE-2026-116676 | 8.8 | 2026-10-27 | Atlantis is a self-hosted golang application that listens for Terraform pull request events via webhooks. From version 0 |
| CVE-2026-116682 | 8.6 | 2026-10-27 | FileBrowser Quantum is a free, self-hosted, web-based file manager. Prior to 1.5.2-stable and 2.0.1-beta, file read hand |
| CVE-2026-117515 | 7.3 | 2026-10-27 | A security flaw has been discovered in oretnom23 php-travel-agency-system 4e28b8f84d72420373dd15c3ae32900beb7e0635. Impa |
| CVE-2026-117516 | 7.3 | 2026-10-27 | A weakness has been identified in oretnom23 php-travel-agency-system. The affected element is an unknown function of the |
| CVE-2026-57202 | 8.1 | 2026-10-27 | Asterisk is an open source private branch exchange and telephony toolkit. Prior to Asterisk 20.20.1, 21.12.3, 22.10.1, 2 |
| CVE-2026-87086 | 7.5 | 2026-10-27 | Tanium addressed a denial of service vulnerability in Provision. |
| CVE-2026-88812 | 7.8 | 2026-10-27 | A double free in XKB SetGeometryin X.Org X Server before 21.1.25 and X Wayland before 24.1.14 could be used by attached  |
| CVE-2026-115413 | 7.8 | 2026-10-27 | Missing token audience validation in the OAuth authentication mode of AWS API MCP Server before version 1.6.0 might allo |
| CVE-2026-112350 | 7.5 | 2026-10-27 | Sunhillo SureLine before 9.1.5 contains a path traversal vulnerability in the radarUpdater.cgi endpoint that allows unau |
| CVE-2026-112351 | 8.8 | 2026-10-27 | Sunhillo SureLine before 9.1.5 contains an OS command injection vulnerability in the networkDiag.cgi endpoint that allow |
| CVE-2026-112352 | 9.1 | 2026-10-27 | Sunhillo SureLine before 9.1.5 contains an authentication bypass vulnerability that allows an unauthenticated remote att |
| CVE-2026-112355 | 7.5 | 2026-10-27 | The MembershipWorks plugin for WordPress before 6.17 contains an information disclosure vulnerability that allows unauth |
| CVE-2026-116688 | 8.1 | 2026-10-27 | CKEditor 5 is a modern JavaScript rich-text editor with an MVC architecture. From 45.0.0 until 47.7.4 and 48.5.1, the en |
| CVE-2026-116690 | 7.5 | 2026-10-27 | MLflow is an open source AI engineering platform for agents, large language models, and machine learning models. From 3. |
| CVE-2026-116692 | 9.8 | 2026-10-27 | MLflow is an open source AI engineering platform for agents, large language models, and machine learning models. From 3. |
| CVE-2026-57195 | 7.5 | 2026-10-27 | Asterisk is an open source private branch exchange and telephony toolkit. Prior to Asterisk 20.20.1, 21.12.3, 22.10.1, 2 |
| CVE-2026-57200 | 7.5 | 2026-10-27 | Asterisk is an open source private branch exchange and telephony toolkit. Prior to Asterisk 20.20.1, 21.12.3, 22.10.1, 2 |
| CVE-2026-83831 | 8.8 | 2026-10-27 | Double free in Microsoft Edge (Chromium-based) allows an unauthorized attacker to execute code over a network. |
| CVE-2026-85898 | 8.8 | 2026-10-27 | Access of resource using incompatible type ('type confusion') in Microsoft Edge (Chromium-based) allows an unauthorized  |
| CVE-2026-57186 | 7.5 | 2026-10-27 | Asterisk is an open source private branch exchange and telephony toolkit. From 21.0.0-pre1 until Asterisk 21.12.3, 22.10 |
| CVE-2026-62765 | 7.5 | 2026-10-27 | Access of resource using incompatible type ('type confusion') in Microsoft Edge (Chromium-based) allows an unauthorized  |
| CVE-2026-118304 | 8.8 | 2026-10-27 | Improper input validation in SVG in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially execut |
| CVE-2026-118307 | 8.8 | 2026-10-27 | Use after free in Paint in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially execute arbitra |
| CVE-2026-118311 | 8.8 | 2026-10-27 | Memory corruption in Media in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially execute arbi |
| CVE-2026-118313 | 8.8 | 2026-10-27 | Use after free in Video in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to execute arbitrary code insi |
| CVE-2026-118314 | 8.8 | 2026-10-27 | Improper input validation in UI in Google Chrome on on Android prior to 156.0.8078.73 allowed a remote attacker to poten |
| CVE-2026-118315 | 8.8 | 2026-10-27 | Improper input validation in SVG in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially execut |
| CVE-2026-118317 | 8.8 | 2026-10-27 | Memory corruption in HTML in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially execute arbit |
| CVE-2026-118320 | 8.8 | 2026-10-27 | Memory corruption in V8 in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially execute arbitra |
| CVE-2026-118327 | 8.8 | 2026-10-27 | Memory corruption in Media in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially execute arbi |
| CVE-2026-118328 | 8.8 | 2026-10-27 | Improper input validation in WebRTC in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially exe |
| CVE-2026-118329 | 8.8 | 2026-10-27 | Improper input validation in ANGLE in Google Chrome on on Mac prior to 156.0.8078.73 allowed a remote attacker to potent |
| CVE-2026-118330 | 8.8 | 2026-10-27 | Use after free in Browser in Google Chrome on on Windows prior to 156.0.8078.73 allowed a remote attacker to execute arb |
| CVE-2026-118331 | 8.8 | 2026-10-27 | Improper input validation in FileAPI in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially ex |
| CVE-2026-118334 | 8.8 | 2026-10-27 | Use after free in ImageCapture in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to execute arbitrary co |
| CVE-2026-118335 | 8.8 | 2026-10-27 | Improper input validation in Metrics in Google Chrome on on Mac prior to 156.0.8078.73 allowed a remote attacker to pote |
| CVE-2026-118336 | 8.8 | 2026-10-27 | Improper input validation in Headless in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially e |
| CVE-2026-118338 | 8.8 | 2026-10-27 | Use after free in Animation in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially execute arb |
| CVE-2026-118339 | 8.8 | 2026-10-27 | Use after free in Animation in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to execute arbitrary code  |
| CVE-2026-118341 | 8.8 | 2026-10-27 | Use after free in Modularization in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to execute arbitrary  |
| CVE-2026-118343 | 8.8 | 2026-10-27 | Improper input validation in ReadingList in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentiall |
| CVE-2026-118344 | 8.8 | 2026-10-27 | Use after free in Layout in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-118345 | 8.8 | 2026-10-27 | Use after free in PDFium in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially execute arbitr |
| CVE-2026-118346 | 8.8 | 2026-10-27 | Use after free in Compositing in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially execute a |
| CVE-2026-118347 | 8.8 | 2026-10-27 | Use after free in FileSystem in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to execute arbitrary code |
| CVE-2026-118348 | 8.8 | 2026-10-27 | Improper input validation in Skia in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially execu |
| CVE-2026-118349 | 8.8 | 2026-10-27 | Memory corruption in Payments in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to execute arbitrary cod |
| CVE-2026-118350 | 8.8 | 2026-10-27 | Use after free in Turbolev in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to execute arbitrary code i |
| CVE-2026-118351 | 8.8 | 2026-10-27 | Memory corruption in Skia in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to execute arbitrary code in |
| CVE-2026-118352 | 8.8 | 2026-10-27 | Memory corruption in Cache in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially execute arbi |
| CVE-2026-118353 | 8.8 | 2026-10-27 | Use after free in Paint in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to execute arbitrary code insi |
| CVE-2026-118354 | 8.8 | 2026-10-27 | Improper input validation in Skia in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially execu |
| CVE-2026-118356 | 8.8 | 2026-10-27 | Use after free in WTF in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-118357 | 8.8 | 2026-10-27 | Use after free in FileSystem in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially execute ar |
| CVE-2026-118358 | 8.8 | 2026-10-27 | Memory corruption in WebAudio in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially execute a |
| CVE-2026-118359 | 8.8 | 2026-10-27 | Memory corruption in V8 in Google Chrome prior to 156.0.8078.73 allowed a remote attacker to potentially execute arbitra |
| CVE-2026-58205 | 8.1 | 2026-10-27 | GRR is a resource management and reservation application. Prior to version 4.5.0, `maj.php` reflects the `forcemaj` para |
| CVE-2026-58255 | 8.8 | 2026-10-27 | Cronicle is a multi-server task scheduler and runner, with a web based front-end UI. Prior to 0.9.121, a non-administrat |
| CVE-2026-58256 | 9.1 | 2026-10-27 | GRR is a resource management and reservation application. Prior to the advisory-reported fixed version 4.5.0, an adminis |
| CVE-2026-58257 | 7.2 | 2026-10-27 | GRR is a resource management and reservation application. Prior to the advisory-reported fixed version 4.5.0, the databa |
| CVE-2026-59158 | 7.5 | 2026-10-27 | Nuxt Ollama integrates the official Ollama JavaScript library into Nuxt applications. Prior to 1.3.1, `src/module.ts` un |
| CVE-2026-104016 | 7.5 | 2026-10-28 | ProtobufParser parses length-prefixed protobuf string and bytes fields by checking (_inputPtr + len) <= _inputEnd and th |
| CVE-2026-104895 | 7.5 | 2026-10-28 | The asynchronous Smile parser (NonBlockingByteArrayParser) uses a raw-binary length prefix taken from untrusted input to |
| CVE-2026-110747 | 7.5 | 2026-10-28 | ProtobufParser._readStringKey() reads the length prefix of a protobuf map entry's string key into an attacker-controlled |
| CVE-2026-110879 | 9.8 | 2026-10-28 | jackson-databind validates the outer class of a class-name type ID but accepts attacker-selected classes inside its gene |
| CVE-2026-106013 | 9.8 | 2026-10-28 | The Jupiter X Core plugin for WordPress is vulnerable to Authentication Bypass via the Twitter/X Social Login handler in |
| CVE-2013-20007 | 7.2 | 2026-10-28 | Linksys WAG200G through 1.01.06 contains an OS command injection vulnerability that allows authenticated attackers to ex |
| CVE-2014-125138 | 8.8 | 2026-10-28 | C97net qEngine CMS through 6.0.0, Kemana Directory through 1.5.6, and Cart Engine through 3.0.0 contain an unrestricted  |
| CVE-2015-20129 | 8.8 | 2026-10-28 | CrushFTP before 7.3.0 contains a cross-site request forgery vulnerability that allows attackers to perform administrativ |
| CVE-2026-109999 | 7.2 | 2026-10-28 | The AI Marketing Expert — AI Email Marketing, AI Content Generator, SEO Analyzer, AI Workflow Automation, Social Media & |
| CVE-2026-111314 | 7.2 | 2026-10-28 | The affiliate-toolkit – Multi-Network Affiliate & Amazon Product Display plugin for WordPress is vulnerable to Stored Cr |
| CVE-2026-117607 | 7.2 | 2026-10-28 | Xerte Online Toolkits through 3.15.5 contains a remote code execution vulnerability that allows authenticated users with |
| CVE-2026-117609 | 7.1 | 2026-10-28 | rtl_433 through 25.12 contains a stack-based buffer overflow vulnerability in proflame2_mc() that allows nearby attacker |
| CVE-2026-118375 | 8.1 | 2026-10-28 | llama.cpp b8841 before b11865 contains an out-of-bounds write vulnerability in the ggml-rpc RDMA transport rdma_recv() f |
| CVE-2026-118377 | 7.5 | 2026-10-28 | mews/pos through 2.0.0 contains an insufficient verification of data authenticity vulnerability that allows unauthentica |
| CVE-2026-118378 | 7.8 | 2026-10-28 | Tabularis before 0.28.0 contains an SQL injection vulnerability in its SQLite driver that allows MCP clients to execute  |
| CVE-2026-84999 | 9.8 | 2026-10-28 | The Pie Register Premium plugin for WordPress is vulnerable to Unrestricted File Type Upload in all versions up to, and  |
| CVE-2026-97019 | 7.2 | 2026-10-28 | The AMP for WP – Accelerated Mobile Pages plugin for WordPress is vulnerable to Stored Cross-Site Scripting via 'headlin |
| CVE-2026-111255 | 7.5 | 2026-10-28 | The affiliate-toolkit – Multi-Network Affiliate & Amazon Product Display plugin for WordPress is vulnerable to Arbitrary |
| CVE-2026-116613 | 7.5 | 2026-10-28 | The Animated Text Block plugin for WordPress is vulnerable to Sensitive Information Exposure in versions up to, and incl |
| CVE-2026-1928 | 8.8 | 2026-10-28 | The Rank Math SEO – AI SEO Tools to Dominate SEO Rankings plugin for WordPress is vulnerable to PHP Object Injection in  |
| CVE-2026-15323 | 7.5 | 2026-10-28 | The Product Designer for WooCommerce WordPress \| Lumise plugin for WordPress is vulnerable to Directory Traversal in all |
| CVE-2026-109218 | 9.8 | 2026-10-28 | The Contact Manager plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 9. |
| CVE-2026-109381 | 7.2 | 2026-10-28 | The Mage Eventpress plugin for WordPress is vulnerable to privilege escalation in versions up to, and including, 5.7.8 T |
| CVE-2026-109384 | 8.8 | 2026-10-28 | The The Innovative Form Builder – IvyForms plugin for WordPress is vulnerable to Arbitrary File Upload in all versions u |
| CVE-2026-110662 | 7.2 | 2026-10-28 | The MxChat – AI Chatbot & Content Generation for WordPress plugin for WordPress is vulnerable to Stored DOM-Based Cross- |
| CVE-2026-111111 | 7.2 | 2026-10-28 | The Prime Slider – Hero Slider, Carousel, WooCommerce & Post Slider Elementor Addons plugin for WordPress is vulnerable  |
| CVE-2026-111120 | 8.8 | 2026-10-28 | The VikRentCar Car Rental Management System plugin for WordPress is vulnerable to Cross-Site Request Forgery in all vers |
| CVE-2026-63286 | 7.1 | 2026-10-28 | Database backups are vulnerable to offline attacks. Backups created using a version prior to the patched version are sti |
| CVE-2026-92797 | 8.8 | 2026-10-28 | The MemberPress plugin for WordPress is vulnerable to Cross-Site Request Forgery in versions up to, and including, 1.14. |
| CVE-2026-86395 | 7.2 | 2026-10-28 | Dell PowerProtect Data Domain Virtual Edition, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7. |
| CVE-2026-86396 | 8.8 | 2026-10-28 | Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7 |
| CVE-2026-86397 | 9.8 | 2026-10-28 | Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7 |
| CVE-2026-86398 | 8.8 | 2026-10-28 | Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7 |
| CVE-2026-86399 | 7.2 | 2026-10-28 | Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7 |
| CVE-2026-86400 | 9.8 | 2026-10-28 | Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7 |
| CVE-2026-90717 | 9.1 | 2026-10-28 | Dell PowerProtect Data Domain Management Center, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions  |
| CVE-2026-86379 | 7.2 | 2026-10-28 | Dell PowerProtect Data Domain Management Center, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions  |
| CVE-2026-86380 | 7.2 | 2026-10-28 | Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7 |
| CVE-2026-86384 | 9.8 | 2026-10-28 | Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7 |
| CVE-2026-86385 | 8.8 | 2026-10-28 | Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, contain an Improper Check for Dropped Privi |
| CVE-2026-86389 | 7.2 | 2026-10-28 | Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7 |
| CVE-2026-86393 | 7.2 | 2026-10-28 | Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7 |
| CVE-2026-86394 | 7.2 | 2026-10-28 | Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7 |
| CVE-2025-30414 | 7.1 | 2026-10-28 | Local privilege escalation due to improper authentication. The following products are affected: Acronis Cyber Protect Cl |
| CVE-2026-103779 | 8.3 | 2026-10-28 | Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7 |
| CVE-2026-103780 | 9.8 | 2026-10-28 | Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7 |
| CVE-2026-103792 | 9.6 | 2026-10-28 | Dell PowerProtect Data Domain Management Center, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions  |
| CVE-2026-103799 | 9.6 | 2026-10-28 | Dell PowerProtect Data Domain Management Center, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions  |
| CVE-2026-110540 | 7.1 | 2026-10-28 | Dell PowerProtect Data Domain Management Center, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions  |
| CVE-2026-110541 | 7.2 | 2026-10-28 | Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7 |
| CVE-2026-6064 | 7.3 | 2026-10-28 | Link following vulnerability in Data Shredder components in Norton Antivirus, Avast Antivirus, and AVG Internet Security |
| CVE-2026-86377 | 7.6 | 2026-10-28 | Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7 |
| CVE-2026-86378 | 8.8 | 2026-10-28 | Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7 |
| CVE-2026-87102 | 7.4 | 2026-10-28 | Sensitive information disclosure and manipulation due to improper token validation. The following products are affected: |
| CVE-2026-87103 | 7.4 | 2026-10-28 | Sensitive information disclosure and manipulation due to improper token validation. The following products are affected: |
| CVE-2026-114278 | 9.8 | 2026-10-28 | The che-machine-exec service constructs a shell command by concatenating user-controlled input (the username and namespa |
| CVE-2026-118477 | 9.8 | 2026-10-28 | The ei_git_repo_url parameter in the Git remote configuration endpoint of KaliFast is vulnerable to OS Command Injection |
| CVE-2026-118485 | 8.1 | 2026-10-28 | Axel Download Accelerator 2.17.14 and earlier performs URL percent-decoding (http_decode()) on the output filename after |
| CVE-2026-111411 | 9.3 | 2026-10-28 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Aman FunnelKit Aut |
| CVE-2026-111850 | 8.5 | 2026-10-28 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in BuddyPress BuddyPr |
| CVE-2026-115591 | 7.5 | 2026-10-28 | Insertion of Sensitive Information Into Sent Data vulnerability in Supsystic Contact Form by Supsystic contact-form-by-s |
| CVE-2026-115593 | 7.1 | 2026-10-28 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Unlimited Elements |
| CVE-2026-115596 | 7.1 | 2026-10-28 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in impleCode eCommerc |
| CVE-2026-115606 | 7.1 | 2026-10-28 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Crowd Favorite DXP |
| CVE-2026-115607 | 9.3 | 2026-10-28 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Crowd Favorite DXP |
| CVE-2026-115609 | 7.1 | 2026-10-28 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Stiofan GetPaid in |
| CVE-2026-115612 | 7.1 | 2026-10-28 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in iova.mihai SliceWP |
| CVE-2026-115904 | 9.6 | 2026-10-28 | Topluyo is a social networking platform. A vulnerability exists in Topluyo Desktop for Linux prior to version 2026.9.241 |
| CVE-2026-116391 | 8.8 | 2026-10-28 | Deserialization of Untrusted Data vulnerability in GS Plugins GS Logo Slider gs-logo-slider allows Object Injection.This |
| CVE-2026-116392 | 7.2 | 2026-10-28 | Deserialization of Untrusted Data vulnerability in PickPlugins Accordion accordions allows Object Injection.This issue a |
| CVE-2026-116393 | 7.5 | 2026-10-28 | Missing Authorization vulnerability in iHomefinder, Inc. Optima Express optima-express allows Exploiting Incorrectly Con |
| CVE-2026-118035 | 7.5 | 2026-10-28 | In Progress® Telerik® Document Processing Libraries prior to version 2026.3.1027, uncontrolled recursion, inefficient al |
| CVE-2026-118036 | 7.5 | 2026-10-28 | In Progress® Telerik® Document Processing Libraries prior to version 2026.3.1027, uncontrolled recursion, infinite loop, |
| CVE-2026-118037 | 7.5 | 2026-10-28 | In Progress® Telerik® Document Processing Libraries prior to version 2026.3.1027, uncontrolled recursion, infinite loop, |
| CVE-2026-118038 | 7.1 | 2026-10-28 | In Progress® Telerik® Document Processing Libraries prior to version 2026.3.1027, a path traversal vulnerability in the  |
| CVE-2026-118039 | 7.5 | 2026-10-28 | In Progress® Telerik® Document Processing Libraries prior to version 2026.3.1027, an XML external entity reference vulne |
| CVE-2026-118040 | 7.5 | 2026-10-28 | In Progress® Telerik® Document Processing Libraries prior to version 2026.3.1027, improper verification of cryptographic |
| CVE-2026-67073 | 8.6 | 2026-10-28 | HCL BigFix AEX is affected by an Unrestricted File Upload and Improper Access Control vulnerability. This could allow an |
| CVE-2026-67074 | 9.1 | 2026-10-28 | HCL BigFix AEX is affected by a Remote Code Execution Vulnerability . It may allow attackers to execute code with the pr |
| CVE-2026-115590 | 7.2 | 2026-10-28 | Deserialization of Untrusted Data vulnerability in weDevs Dokan dokan-lite allows Object Injection.This issue affects Do |
| CVE-2026-115603 | 8.5 | 2026-10-28 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Advanced Ads GmbH  |
| CVE-2026-115968 | 9.8 | 2026-10-28 | Deserialization of Untrusted Data vulnerability in Ultimate Member Ultimate Member ultimate-member allows Object Injecti |
| CVE-2026-116389 | 8.8 | 2026-10-28 | Deserialization of Untrusted Data vulnerability in crossi72 Phoenix Media Rename phoenix-media-rename allows Object Inje |
| CVE-2026-116390 | 7.2 | 2026-10-28 | Deserialization of Untrusted Data vulnerability in stepasyuk Filter Everything&nbsp;— WordPress &amp; WooCommerce Filter |
| CVE-2026-52729 | 7.1 | 2026-10-28 | Xibo is an open source digital signage platform with a web content management system and Windows display player software |
| CVE-2026-59164 | 7.1 | 2026-10-28 | NORA is a self-hosted artifact registry and pull-through cache. Prior to 0.9.5, `nora-registry` authenticates the token- |
| CVE-2026-59172 | 7.8 | 2026-10-28 | Joker is a small Clojure interpreter, linter and formatter written in Go. Prior to 1.8.2, `joker --lint <file>` walks up |
| CVE-2026-59176 | 7.8 | 2026-10-28 | Functype is a family of TypeScript functional programming libraries. Prior to 1.4.4, the `set_functype_version` MCP tool |
| CVE-2026-59177 | 8.8 | 2026-10-28 | ESPHome Device Builder Dashboard is a dashboard for the ESPHome home management software. Prior to 1.0.10, the `Home Ass |
| CVE-2026-59179 | 8.3 | 2026-10-28 | OpenHop is a tool for creating interactive data-flow diagrams. Prior to 0.3.7, `@openhop/server` passes unauthenticated  |
| CVE-2026-59185 | 8.5 | 2026-10-28 | identrail is a machine identity security platform for AWS, GitHub/OIDC, and Kubernetes. Prior to 1.0.2, the default-on ` |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-48356 | Adobe / Commerce and Magento | 2026-10-27 | 2026-11-10 | Unknown |
| CVE-2026-111497 | Google / Brotli | 2026-10-27 | 2026-11-10 | Unknown |
| CVE-2026-109618 | PHP Group / PHP | 2026-10-26 | 2026-10-29 | Unknown |
| CVE-2026-109619 | PHP Group / PHP | 2026-10-26 | 2026-10-29 | Unknown |
| CVE-2026-114625 | Arista / VeloCloud Orchestrator | 2026-10-23 | 2026-10-26 | Unknown |
| CVE-2026-110447 | Collabora / Collabora Online – Built-in CODE Server | 2026-10-23 | 2026-10-26 | Unknown |

---

*Total entries in CISA KEV catalog: 1760*