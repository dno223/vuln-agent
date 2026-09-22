# Vulnerability Intelligence Report

**Date:** 2026-09-22  
**Generated:** 2026-09-22T23:42:42Z  

---

## Executive Summary

Our environment faces critical exposure across 219 high-severity CVEs, including two with maximum CVSS scores of 10.0 and 9.8. Three monitored vulnerabilities now appear in CISA's Known Exploited Vulnerabilities catalog—affecting Arista VeloCloud Orchestrator, F5 BIG-IP APM, and Check Point products—with mandatory remediation deadlines of September 25, 2026. WordPress plugin vulnerabilities enabling privilege escalation, PHP object injection, and stored XSS represent broad attack surface risk. Immediate patching of actively exploited infrastructure components is required to maintain regulatory compliance and prevent network compromise.

---

## Risk Narrative

Threat actors are actively exploiting vulnerabilities in widely deployed network infrastructure—including VPN, load balancing, and firewall platforms—creating immediate risk of lateral movement and data exfiltration. The presence of three monitored CVEs in the CISA KEV catalog signals confirmed in-the-wild exploitation, elevating organizational risk beyond theoretical exposure. WordPress-based vulnerabilities affecting multiple plugins introduce privilege escalation and remote code execution paths across web properties. A CVSS 10.0 vulnerability in Gigatech PDV5701 represents a complete compromise scenario. Combined, these findings indicate a threat landscape targeting both perimeter infrastructure and application-layer assets, with potential for ransomware deployment, data breach, and regulatory penalty.

---

## Prioritized Action Items

1. Patch CVE-2026-93952, CVE-2026-94127, and CVE-2026-93616 immediately, as all three are confirmed actively exploited and carry a federal remediation deadline of September 25, 2026.
2. Isolate and remediate CVE-2026-94493 (CVSS 10.0) in Gigatech PDV5701 and CVE-2026-13355 (CVSS 9.8) in Meta Box AIO WordPress plugin to block privilege escalation and full system compromise vectors.
3. Audit all WordPress plugin instances for CVE-2026-19658 PHP Object Injection and CVE-2026-91827 deserialization vulnerabilities, disabling affected plugins until patches are applied.
4. Upgrade Dancer2 to version 2.2.0 or later to remediate CVE-2026-93710 and CVE-2026-93712, which expose applications to route bypass and arbitrary file disclosure.
5. Establish an emergency patch cycle for all 11 newly added CISA KEV entries, prioritizing network infrastructure products from Check Point, F5, Arista, and Zyxel.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-93710 | 7.5 | 2026-09-22 | Dancer2 versions from 2.0.0 before 2.2.0 for Perl dispatch a route that a dying hook refused when the exception handler  |
| CVE-2026-93712 | 7.5 | 2026-09-22 | Dancer2 versions from 2.1.0 before 2.2.0 for Perl serve files from outside public_dir via relative path segments in the  |
| CVE-2026-94491 | 7.3 | 2026-09-22 | A weakness has been identified in Yonyou KSOA 9.0. This affects an unknown part of the file /cardcase/search_list.jsp. E |
| CVE-2026-94493 | 10.0 | 2026-09-22 | A vulnerability was detected in Gigatech PDV5701 1.0.31_240305_112640. This issue affects some unknown processing of the |
| CVE-2026-13355 | 9.8 | 2026-09-22 | The Meta Box AIO plugin for WordPress is vulnerable to Privilege Escalation to Administrator in versions up to, and incl |
| CVE-2026-19658 | 9.8 | 2026-09-22 | The Give Tributes plugin for WordPress is vulnerable to PHP Object Injection in all versions up to, and including, 2.3.1 |
| CVE-2026-12470 | 7.2 | 2026-09-22 | The CMP – Coming Soon & Maintenance Plugin by NiteoThemes plugin for WordPress is vulnerable to unauthorized modificatio |
| CVE-2026-89412 | 7.2 | 2026-09-22 | The TranslatePress – Translate Multilingual sites with AI Translation plugin for WordPress is vulnerable to Stored Cross |
| CVE-2026-91827 | 7.5 | 2026-09-22 | The Ninja Forms WordPress plugin 3.15.3 does not prevent user-submitted form field values from being deserialised when a |
| CVE-2026-92438 | 8.8 | 2026-09-22 | The Ninja Forms WordPress plugin 3.15.3 does not escape submitted form field values before outputting them on the submis |
| CVE-2026-94504 | 7.2 | 2026-09-22 | Ninja Forms 3.15.3 stores an anonymous non-RTE textarea value and renders it without safe HTML encoding in the legacy su |
| CVE-2016-15059 | 9.8 | 2026-09-22 | Net::IDN::Punycode versions before 2.301 for Perl allow a heap buffer overflow via unchecked writes past the output buff |
| CVE-2025-1281 | 8.8 | 2026-09-22 | The BM Content Builder plugin for WordPress is vulnerable to arbitrary file deletion due to insufficient file path valid |
| CVE-2026-6922 | 7.1 | 2026-09-22 | The WP Table Builder – Drag & Drop Table Builder plugin for WordPress is vulnerable to Incorrect Authorization in all ve |
| CVE-2026-74766 | 8.4 | 2026-09-22 | Net::IDN::Punycode versions from 2.301 before 2.590 for Perl allow a heap use-after-free via a decoded code point that r |
| CVE-2026-87078 | 9.1 | 2026-09-22 | Net::IDN::Punycode versions from 2.302 before 2.590 for Perl leak the output buffer on every rejected label in decode_pu |
| CVE-2026-87079 | 7.5 | 2026-09-22 | Net::IDN::Punycode versions before 2.590 for Perl allow CPU exhaustion via quadratic insertion cost when decoding a long |
| CVE-2026-87080 | 9.1 | 2026-09-22 | Net::IDN::Punycode::PP versions before 2.590 for Perl decode a truncated label to a name containing a character it never |
| CVE-2026-87081 | 7.5 | 2026-09-22 | Net::IDN::UTS46 versions before 2.590 for Perl allow CPU exhaustion via quadratic punycode encoding of an overlong label |
| CVE-2026-87082 | 7.5 | 2026-09-22 | Net::IDN::Punycode versions before 2.590 for Perl hang, crash or return a wrong label via unvalidated malformed UTF-8 in |
| CVE-2026-92235 | 8.1 | 2026-09-22 | The The WP Ultimate Review plugin for WordPress is vulnerable to arbitrary shortcode execution in all versions up to, an |
| CVE-2026-92969 | 8.1 | 2026-09-22 | The HUSKY – Products Filter for WooCommerce Professional plugin for WordPress is vulnerable to Local File Inclusion in a |
| CVE-2026-93778 | 7.2 | 2026-09-22 | The WP Yelp Review Slider plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Yelp Review Text (import |
| CVE-2026-93836 | 7.2 | 2026-09-22 | The WPC Product Bundles for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'qty'  |
| CVE-2026-93952 | 10.0 | 2026-09-22 | VeloCloud Orchestrator (VCO) on-prem has a security issue where this issue may allow a remote attacker to access privile |
| CVE-2026-93928 | 7.3 | 2026-09-22 | Authentication Bypass Using an Alternate Path or Channel vulnerability in Magepeople inc. Taxi Booking Manager for WooCo |
| CVE-2026-95508 | 7.4 | 2026-09-22 | A heap-based buffer overflow was found in the DHCPv6 and TFTP response builders of libslirp. When the host is configured |
| CVE-2026-9231 | 7.5 | 2026-09-22 | The WP Travel Engine – Tour Booking Plugin – Tour Operator Software plugin for WordPress is vulnerable to Local File Inc |
| CVE-2026-25254 | 9.8 | 2026-09-22 | Improper authorization leads to Remote Code Execution via SocketIO interface. |
| CVE-2026-25255 | 8.8 | 2026-09-22 | Exposed dangerous function lead to privilege escalation via gRPC server. |
| CVE-2026-25264 | 8.8 | 2026-09-22 | Privilege escalation due to weak configuration during package extraction process. |
| CVE-2026-25265 | 8.8 | 2026-09-22 | Privilege escalation due to weak configuration while temporary file handling. |
| CVE-2026-94117 | 7.6 | 2026-09-22 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in DevItems HashBar – |
| CVE-2026-74849 | 9.8 | 2026-09-22 | Zohocorp ManageEngine ADSelfService Plus versions before build 7001 are vulnerable to a remote code execution vulnerabil |
| CVE-2026-75791 | 8.6 | 2026-09-22 | Zohocorp ManageEngine ADSelfService Plus versions before build 7001 are vulnerable to an authentication bypass vulnerabi |
| CVE-2026-93616 | 9.8 | 2026-09-22 | A directory traversal and file upload vulnerability allows an unauthenticated attacker to upload and execute arbitrary s |
| CVE-2026-95271 | 7.3 | 2026-09-22 | A vulnerability has been found in dgtlmoon changedetection.io up to 0.60.7. The impacted element is the function check_a |
| CVE-2026-95619 | 7.7 | 2026-09-22 | A flaw was found in libstdc++. An integer overflow can occur when processing large inputs to the aligned operator new in |
| CVE-2026-12718 | 9.8 | 2026-09-22 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Karel Electronic I |
| CVE-2026-95499 | 7.3 | 2026-09-22 | A flaw has been found in JosephChuks php-file-manager-with-code-editor up to 3.0. This issue affects the function move_u |
| CVE-2026-95675 | 9.8 | 2026-09-22 | D-Link DAP-1360 firmware version 6.14 and earlier contains an unauthenticated remote code execution vulnerability that a |
| CVE-2026-24239 | 7.8 | 2026-09-22 | NVIDIA NeMo Speech for all platforms contains a vulnerability where malicious data created by an attacker could cause re |
| CVE-2026-24267 | 7.8 | 2026-09-22 | NVIDIA NeMo Speech for all platforms contains a vulnerability in the speech data explorer component, where malicious dat |
| CVE-2026-65111 | 7.8 | 2026-09-22 | NVIDIA NeMo Speech for all platforms contains a vulnerability where malicious input created by an attacker could cause a |
| CVE-2026-65113 | 9.8 | 2026-09-22 | NVIDIA Infrastructure Controller for Linux contains a vulnerability where an attacker could cause use of hard-coded cred |
| CVE-2026-65114 | 8.3 | 2026-09-22 | NVIDIA Infrastructure Controller for Linux contains a vulnerability where an attacker could cause missing authentication |
| CVE-2026-65118 | 7.5 | 2026-09-22 | NVIDIA Infrastructure Controller for Linux contains a vulnerability where an attacker could cause improper certificate v |
| CVE-2026-65121 | 8.2 | 2026-09-22 | NVIDIA Infrastructure Controller for Linux contains a vulnerability where an  attacker could cause an improper authentic |
| CVE-2026-65128 | 8.8 | 2026-09-22 | NVIDIA Infrastructure Controller for Linux contains a vulnerability where an attacker could cause SQL injection. A succe |
| CVE-2026-65130 | 8.0 | 2026-09-22 | NVIDIA Infrastructure Controller for Linux contains a vulnerability where an attacker could cause OS command injection.  |
| CVE-2026-65178 | 7.8 | 2026-09-22 | NVIDIA NeMo contains a vulnerability in its dataset-loading workflow where a maliciously crafted model_config.yaml can i |
| CVE-2026-65179 | 8.8 | 2026-09-22 | NVIDIA NeMo contains a vulnerability in the TabularTokenizer class where it deserializes an untrusted, attacker-controll |
| CVE-2026-79313 | 9.8 | 2026-09-22 | webpy web.py 0.76 is vulnerable to Insufficient Session Expiration. The application's session management relies on perio |
| CVE-2026-84388 | 9.6 | 2026-09-22 | A improper restriction of rendered ui layers or frames vulnerability in Fortinet FortiPAM Chrome Extension 8.0 all versi |
| CVE-2026-89407 | 7.5 | 2026-09-22 | NumberInput.looksLikeValidNumber() in FasterXML jackson-core pre-validates "stringified numbers" with two regular expres |
| CVE-2026-93088 | 9.8 | 2026-09-22 | SGLang's multimodal generation runtime is vulnerable to unauthenticated arbitrary code execution because the disaggregat |
| CVE-2026-94127 | 9.8 | 2026-09-22 | When a BIG-IP APM access policy and an OAuth profile is configured on a virtual server, specific malicious traffic can l |
| CVE-2026-95500 | 7.3 | 2026-09-22 | A vulnerability has been found in JosephChuks php-file-manager-with-code-editor up to 3.0. Impacted is the function file |
| CVE-2026-56681 | 7.3 | 2026-09-22 | 9Router is an AI router & token saver. Prior to 0.5.6, 9Router deployments that allow requests to reach Next.js without  |
| CVE-2026-70410 | 8.8 | 2026-09-22 | Use of Externally-Controlled Input to Select Classes or Code ('Unsafe Reflection') vulnerability in Apache Calcite Avati |
| CVE-2026-75607 | 8.1 | 2026-09-22 | Frigate is an open source network video recorder. Prior to 0.17.2, the WebSocket handler in frigate/comms/ws.py forwards |
| CVE-2026-75608 | 7.7 | 2026-09-22 | Frigate is an open source network video recorder. Prior to 0.18.0, the prefix-matched location /api/go2rtc/api in docker |
| CVE-2026-77633 | 7.1 | 2026-09-22 | Cloudreve is a self-hosted file management and sharing system. Prior to 4.18.0, PrepareUpload in pkg/filemanager/fs/dbfs |
| CVE-2026-80143 | 9.9 | 2026-09-22 | Lantronix SLC8000 before firmware v9.7.0.2, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB88 |
| CVE-2026-80144 | 9.9 | 2026-09-22 | Lantronix SLC8000 before firmware v9.7.0.2, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB88 |
| CVE-2026-80145 | 9.1 | 2026-09-22 | Lantronix SLC8000 before firmware v9.7.0.2, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB88 |
| CVE-2026-80146 | 9.9 | 2026-09-22 | Lantronix SLC8000 before firmware v9.7.0.2, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB88 |
| CVE-2026-80147 | 9.9 | 2026-09-22 | Lantronix SLC8000 before firmware v9.7.0.2, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB88 |
| CVE-2026-80148 | 8.6 | 2026-09-22 | Lantronix SLC8000 before firmware v9.7.0.3, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB88 |
| CVE-2026-80149 | 8.6 | 2026-09-22 | Lantronix SLC8000 before firmware v9.7.0.3, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB88 |
| CVE-2026-80150 | 7.5 | 2026-09-22 | Lantronix SLC8000 before firmware v9.7.0.3, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB88 |
| CVE-2026-80151 | 9.1 | 2026-09-22 | Lantronix SLC8000 before firmware v9.7.0.3, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB88 |
| CVE-2026-80152 | 9.1 | 2026-09-22 | Lantronix SLC8000 before firmware v9.7.0.3, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB88 |
| CVE-2026-80154 | 9.6 | 2026-09-22 | All firmware versions of Lantronix SLC8000, EMG8500, EMG7500, SLB882, SLCx-03, and SLCx-02 contain an authentication byp |
| CVE-2026-80155 | 10.0 | 2026-09-22 | Lantronix SLC8000 before firmware v9.7.0.5, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB88 |
| CVE-2026-80156 | 9.1 | 2026-09-22 | Lantronix SLC8000 before firmware v9.7.0.5, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB88 |
| CVE-2026-94640 | 7.5 | 2026-09-22 | A flaw was found in rpcbind. This vulnerability allows a remote, unauthenticated attacker to cause a Denial of Service ( |
| CVE-2026-95653 | 7.5 | 2026-09-22 | Concrete CMS Community Store before 2.7.8 derives digital product download tokens from order creation timestamps instead |
| CVE-2026-95654 | 7.4 | 2026-09-22 | Databasement before 1.7.14 validates invitation tokens only when the acceptance page loads, caching the authorization de |
| CVE-2026-95655 | 8.1 | 2026-09-22 | Aureus ERP before 1.5.0 fails to scope message lookups to the current record in ChatterPanel, allowing authenticated use |
| CVE-2026-13087 | 8.8 | 2026-09-22 | A heap out-of-bounds write vulnerability was found in the Linux kernel's RPC-over-RDMA server reply path in net/sunrpc/x |
| CVE-2026-83598 | 7.8 | 2026-09-22 | Netdata is an open source observability tool. From rom 2.0.0 until 2.10.4, during Netdata Windows Agent MSI repair, powe |
| CVE-2026-83599 | 7.5 | 2026-09-22 | Netdata is an open source observability tool. Prior to 2.11.0, Netdata's unauthenticated WebSocket server negotiates per |
| CVE-2026-83603 | 8.4 | 2026-09-22 | Netdata is an open source observability tool. Prior to 2.10.4, the setuid-root ndsudo helper command fail2ban-client-sta |
| CVE-2026-85734 | 9.1 | 2026-09-22 | LightRAG provides simple and fast retrieval-augmented generation. Prior to 1.5.5, the POST /login endpoint in lightrag/a |
| CVE-2026-85740 | 7.1 | 2026-09-22 | LightRAG provides simple and fast retrieval-augmented generation. Prior to 1.5.5, _validated_addresses in lightrag/parse |
| CVE-2026-86059 | 9.6 | 2026-09-22 | Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, Dokploy organization members without Gi |
| CVE-2026-87902 | 8.1 | 2026-09-22 | An unauthenticated attacker can make `get_page_template()` page-template resolution include a chosen readable local `.ph |
| CVE-2026-94455 | 7.1 | 2026-09-22 | An HTTP endpoint intended for provisioning enterprise and reseller organisations is reachable without any session. The a |
| CVE-2026-94456 | 9.1 | 2026-09-22 | Postiz generates security-sensitive credentials using `Math.random()` instead of a cryptographically secure source. The  |
| CVE-2026-43641 | 9.8 | 2026-09-22 | Softaculous Virtualizor before 3.2.9 (Patch 9) and 3.0.0 contains an OS command injection vulnerability in the billing m |
| CVE-2026-43642 | 8.1 | 2026-09-22 | Softaculous Virtualizor before 3.2.9 (Patch 9) and 3.0.0 contains a PHP object injection vulnerability in the billing mo |
| CVE-2026-43643 | 7.5 | 2026-09-22 | Softaculous Virtualizor before 3.2.9 (Patch 9) and 3.0.0 contains an authorization bypass vulnerability in the billing m |
| CVE-2026-73369 | 10.0 | 2026-09-22 | Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability t |
| CVE-2026-75699 | 10.0 | 2026-09-22 | Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability t |
| CVE-2026-75703 | 10.0 | 2026-09-22 | Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability t |
| CVE-2026-75721 | 10.0 | 2026-09-22 | Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability t |
| CVE-2026-75723 | 10.0 | 2026-09-22 | Adobe Campaign Classic (ACC) is affected by an Incorrect Authorization vulnerability that could result in arbitrary code |
| CVE-2026-75728 | 9.1 | 2026-09-22 | Adobe Campaign Classic (ACC) is affected by an Incorrect Authorization vulnerability that could result in arbitrary code |
| CVE-2026-77242 | 7.5 | 2026-09-22 | MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, va |
| CVE-2026-77243 | 8.8 | 2026-09-22 | MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, EN |
| CVE-2026-77244 | 10.0 | 2026-09-22 | MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, th |
| CVE-2026-77258 | 7.7 | 2026-09-22 | MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, up |
| CVE-2026-77261 | 7.1 | 2026-09-22 | MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, _m |
| CVE-2026-77605 | 7.8 | 2026-09-22 | Notepad++ is a free and open-source source code editor. Prior to 8.9.8, the Folder as Workspace Run by system action in  |
| CVE-2026-82003 | 8.5 | 2026-09-22 | Adobe Campaign Classic (ACC) is affected by an Improper Input Validation vulnerability that could result in arbitrary co |
| CVE-2026-82008 | 9.9 | 2026-09-22 | Adobe Campaign Classic (ACC) is affected by an Improper Input Validation vulnerability that could result in arbitrary co |
| CVE-2026-82009 | 9.1 | 2026-09-22 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL  |
| CVE-2026-82010 | 9.9 | 2026-09-22 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL  |
| CVE-2026-82011 | 9.1 | 2026-09-22 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL  |
| CVE-2026-82013 | 9.9 | 2026-09-22 | Adobe Campaign Classic (ACC) is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in priv |
| CVE-2026-82443 | 9.6 | 2026-09-22 | Adobe Campaign Classic (ACC) is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in priv |
| CVE-2026-83597 | 7.0 | 2026-09-22 | Netdata is an open source observability tool. From version 2.0.0 until 2.10.4, Netdata Windows Agent MSI repair launches |
| CVE-2026-83660 | 9.9 | 2026-09-22 | Adobe Campaign Classic (ACC) is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in priv |
| CVE-2026-84412 | 10.0 | 2026-09-22 | Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability t |
| CVE-2026-85279 | 8.6 | 2026-09-22 | Notepad++ is a free and open-source source code editor. Prior to 8.9.8, Notepad++ contains a stack buffer overflow in Pl |
| CVE-2026-85995 | 7.3 | 2026-09-22 | Notepad++ is a free and open-source source code editor. From 8.9.7 until 8.9.8, the Notepad++ updater and signature veri |
| CVE-2026-86054 | 7.8 | 2026-09-22 | Notepad++ is a free and open-source source code editor. Prior to 8.9.8, Notepad++ contains a stack buffer overflow in Np |
| CVE-2026-89275 | 10.0 | 2026-09-22 | Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability t |
| CVE-2026-89276 | 9.9 | 2026-09-22 | Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability t |
| CVE-2026-93345 | 7.5 | 2026-09-22 | MikroTik RouterOS before 7.25beta4 contains an improper input validation vulnerability in the labelled-VPN NLRI iterator |
| CVE-2026-94384 | 8.1 | 2026-09-22 | Missing authorization in Amazon amazon-connect-salesforce-lambda before 5.26 allows any IAM principal with lambda:Invoke |
| CVE-2026-95656 | 7.3 | 2026-09-22 | A vulnerability was found in dgtlmoon changedetection.io up to 50389b07. This vulnerability affects the function add_wat |
| CVE-2026-19480 | 7.5 | 2026-09-22 | CAI Content Credentials is affected by an Improper Input Validation vulnerability that could result in a Security featur |
| CVE-2026-34689 | 8.6 | 2026-09-22 | Adobe Connect is affected by an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerabi |
| CVE-2026-57149 | 9.9 | 2026-09-22 | plone.app.portlets.portlets provides a Plone-specific user interface for plone.portlets, as well as a standard set of po |
| CVE-2026-75632 | 7.5 | 2026-09-22 | CAI Content Credentials is affected by an Uncontrolled Resource Consumption vulnerability that could lead to application |
| CVE-2026-75649 | 7.8 | 2026-09-22 | Bridge is affected by a Heap-based Buffer Overflow vulnerability that could result in arbitrary code execution in the co |
| CVE-2026-75655 | 7.8 | 2026-09-22 | Bridge is affected by an Uncontrolled Recursion vulnerability that could result in arbitrary code execution in the conte |
| CVE-2026-75658 | 7.8 | 2026-09-22 | Bridge is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the context  |
| CVE-2026-75663 | 7.8 | 2026-09-22 | Bridge is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the context  |
| CVE-2026-75665 | 7.8 | 2026-09-22 | Bridge is affected by a Heap-based Buffer Overflow vulnerability that could result in arbitrary code execution in the co |
| CVE-2026-75676 | 7.8 | 2026-09-22 | Bridge is affected by a Stack-based Buffer Overflow vulnerability that could result in arbitrary code execution in the c |
| CVE-2026-75682 | 9.9 | 2026-09-22 | Adobe Connect is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vul |
| CVE-2026-75684 | 9.3 | 2026-09-22 | Adobe Connect is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by an attacker to in |
| CVE-2026-75686 | 9.3 | 2026-09-22 | Adobe Connect is affected by an Improper Input Validation vulnerability that could result in arbitrary code execution in |
| CVE-2026-75689 | 9.3 | 2026-09-22 | Adobe Connect is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by an attacker to in |
| CVE-2026-75697 | 9.3 | 2026-09-22 | Adobe Connect is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by an attacker to in |
| CVE-2026-75698 | 9.3 | 2026-09-22 | Adobe Connect is affected by a reflected Cross-Site Scripting (XSS) vulnerability. An attacker could exploit this vulner |
| CVE-2026-75743 | 7.1 | 2026-09-22 | Adobe Experience Manager Forms JEE is affected by a Cross-Site Request Forgery (CSRF) vulnerability that could result in |
| CVE-2026-75744 | 8.1 | 2026-09-22 | Adobe Experience Manager Forms JEE is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused |
| CVE-2026-75745 | 10.0 | 2026-09-22 | Adobe Experience Manager Forms JEE is affected by an Incorrect Authorization vulnerability that could result in arbitrar |
| CVE-2026-77246 | 7.4 | 2026-09-22 | MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, an |
| CVE-2026-77248 | 8.6 | 2026-09-22 | MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, th |
| CVE-2026-77253 | 7.1 | 2026-09-22 | MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, Ji |
| CVE-2026-77254 | 9.1 | 2026-09-22 | MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, re |
| CVE-2026-77255 | 8.6 | 2026-09-22 | MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, th |
| CVE-2026-77259 | 7.7 | 2026-09-22 | MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, co |
| CVE-2026-77262 | 8.6 | 2026-09-22 | MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, co |
| CVE-2026-77544 | 7.5 | 2026-09-22 | A malicious actor with access to the network could exploit an Out-of-bounds Write vulnerability found in certain UniFi g |
| CVE-2026-77555 | 7.5 | 2026-09-22 | A malicious actor with access to the network could exploit an Out-of-bounds Write vulnerability found in certain UniFi g |
| CVE-2026-77556 | 7.5 | 2026-09-22 | A malicious actor with access to the network could exploit an Out-of-bounds Read vulnerability found in certain UniFi ga |
| CVE-2026-77558 | 7.5 | 2026-09-22 | A malicious actor with access to the network could exploit an Out-of-bounds Read vulnerability found in certain UniFi ga |
| CVE-2026-79906 | 7.8 | 2026-09-22 | Substance3D - Modeler is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution  |
| CVE-2026-81995 | 9.1 | 2026-09-22 | Adobe Experience Manager Forms JEE is affected by an Improper Input Validation vulnerability that could result in arbitr |
| CVE-2026-81998 | 7.8 | 2026-09-22 | Substance3D - Modeler is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution  |
| CVE-2026-81999 | 8.7 | 2026-09-22 | Adobe Experience Manager Forms JEE is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result i |
| CVE-2026-82000 | 9.6 | 2026-09-22 | Adobe Experience Manager Forms JEE is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result i |
| CVE-2026-83962 | 7.8 | 2026-09-22 | Substance3D - Modeler is affected by a Stack-based Buffer Overflow vulnerability that could result in arbitrary code exe |
| CVE-2026-83963 | 7.8 | 2026-09-22 | Substance3D - Modeler is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution  |
| CVE-2026-84395 | 7.1 | 2026-09-22 | Premiere Pro is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in privilege escalation |
| CVE-2026-94462 | 7.1 | 2026-09-22 | Spree is an open source e-commerce solution built with Ruby on Rails. From 5.4.0 until 5.4.4 and 5.5.4, PATCH /api/v3/st |
| CVE-2026-95831 | 7.8 | 2026-09-22 | Crypt::SelfCertificate versions from 1.01 through 1.05 for Perl contains malware which executes Python code from an obfu |
| CVE-2026-95861 | 7.5 | 2026-09-22 | A malicious actor with access to the network could exploit an Uncontrolled Recursion vulnerability found in certain UniF |
| CVE-2026-95862 | 7.5 | 2026-09-22 | A malicious actor with access to the network could exploit an Out-of-bounds Write vulnerability found in certain UniFi g |
| CVE-2026-28324 | 9.8 | 2026-09-22 | SolarWinds Observability Self-Hosted was found to be affected by an unauthenticated remote code execution vulnerability  |
| CVE-2026-28325 | 8.8 | 2026-09-22 | SolarWinds Observability Self-Hosted was found to be affected by an unauthenticated remote code execution vulnerability  |
| CVE-2026-47116 | 9.8 | 2026-09-22 | LTSecurity LTK3500SF contains a hard-coded credentials vulnerability where root and guest account passwords are stored a |
| CVE-2026-58268 | 7.5 | 2026-09-22 | SIPGO is a library for writing SIP services in the GO language. Prior to 1.4.1, ParserStream.parseSingle in sip/parser_s |
| CVE-2026-59991 | 7.5 | 2026-09-22 | psd-tools is a Python package for working with Adobe Photoshop PSD files. Prior to 1.17.4, PSDImage.composite() and PSDI |
| CVE-2026-61570 | 7.5 | 2026-09-22 | MPXJ is an open source library to read and write project plans from a variety of file formats and databases. From 5.5.5  |
| CVE-2026-62985 | 7.5 | 2026-09-22 | request-filtering-agent is an http(s).Agent implementation that blocks requests to Private/Reserved IP addresses. Prior  |
| CVE-2026-63104 | 8.1 | 2026-09-22 | Kaneo versions 2.3.12 before 2.12.2 contain a missing authorization vulnerability that allows authenticated workspace me |
| CVE-2026-76708 | 9.8 | 2026-09-22 | A vulnerability exists in the Analytics and Location Engine (ALE) where the application and underlying operating system  |
| CVE-2026-76709 | 9.8 | 2026-09-22 | A vulnerability exists in the internal administrative component of Analytics and Location Engine (ALE). Successful explo |
| CVE-2026-76710 | 7.5 | 2026-09-22 | A vulnerability exists in the Analytics and Location Engine (ALE) management interface that may allow for the disclosure |
| CVE-2026-76711 | 7.5 | 2026-09-22 | A vulnerability exists in an Analytics and Location Engine (ALE) component where the impacted process improperly process |
| CVE-2026-76712 | 7.3 | 2026-09-22 | A vulnerability exists in the Analytics and Location Engine (ALE) that may allow for unauthorized access, information di |
| CVE-2026-76713 | 7.2 | 2026-09-22 | A vulnerability exists in the maintenance restore functionality of Analytics and Location Engine (ALE). Successful explo |
| CVE-2026-76714 | 7.2 | 2026-09-22 | Vulnerabilities in the Analytics and Location Engine web interface allows remote authenticated users to run arbitrary co |
| CVE-2026-76715 | 7.1 | 2026-09-22 | A vulnerability in an administrative component of Analytics and Location Engine (ALE) is vulnerable to a man-in-the-midd |
| CVE-2026-77322 | 7.5 | 2026-09-22 | SIPGO is a library for writing SIP services in the GO language. Prior to 1.4.3, WSConnection.Read in sip/transport_ws.go |
| CVE-2026-87121 | 9.8 | 2026-09-22 | lwIP TCP/IP Stack MQTT is vulnerable to an out-of-bounds write, which may allow an attacker to gain full code execution  |
| CVE-2026-88419 | 8.8 | 2026-09-22 | An unrestricted upload of files with a dangerous type in the thumbnail-upload endpoint (/index.php?m=member&f=article&v= |
| CVE-2026-67615 | 8.8 | 2026-09-22 | openEQUELLA before 2026.1.0 contains an authenticated remote code execution vulnerability that allows any authenticated  |
| CVE-2026-91018 | 8.8 | 2026-09-22 | lwIP (Lightweight IP) has a double free vulnerability, which could crash the system, cause a DoS, memory corruption, or  |
| CVE-2026-94450 | 7.5 | 2026-09-22 | Improper validation of the Destination Connection ID length in s2n-quic 1.88.0 and earlier may allow an unauthenticated  |
| CVE-2026-95814 | 8.1 | 2026-09-22 | Vaultwarden through 1.37.3 omits organization membership status validation from three cipher access-restriction queries, |
| CVE-2026-16346 | 9.9 | 2026-09-22 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary commands du |
| CVE-2026-16468 | 8.8 | 2026-09-22 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary commands du |
| CVE-2026-16469 | 8.8 | 2026-09-22 | IBM DataStage on Cloud Pak for Data 5.4.0.0 px-runtime could allow a remote authenticated attacker to execute arbitrary  |
| CVE-2026-16672 | 8.8 | 2026-09-22 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary code due to |
| CVE-2026-17102 | 8.8 | 2026-09-22 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary commands du |
| CVE-2026-17472 | 9.6 | 2026-09-22 | IBM Concert 1.0.0 through 3.0.0 could allow a remote authenticated attacker to access or modify unauthorized resources d |
| CVE-2026-17618 | 7.3 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote unauthenticated attacker to view and m |
| CVE-2026-17635 | 9.1 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to perform unauthorized actio |
| CVE-2026-17636 | 8.8 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote authenticated attacker to execute arbi |
| CVE-2026-17637 | 8.8 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow an adjacent-network attacker to execute arbitra |
| CVE-2026-17643 | 8.8 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a local attacker to obtain sensitive informatio |
| CVE-2026-17644 | 8.8 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a local attacker to gain unauthorized access to |
| CVE-2026-17645 | 9.1 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote authenticated attacker to gain elevate |
| CVE-2026-17646 | 8.5 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote authenticated attacker to obtain sensi |
| CVE-2026-17647 | 8.8 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a local attacker to execute arbitrary commands  |
| CVE-2026-18066 | 7.9 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a local attacker to obtain sensitive informatio |
| CVE-2026-18074 | 8.2 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to perform unauthorized actio |
| CVE-2026-18095 | 8.5 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote authenticated attacker to execute arbi |
| CVE-2026-18123 | 7.6 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to cause a denial of service  |
| CVE-2026-18131 | 8.2 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to execute arbitrary JavaScri |
| CVE-2026-18134 | 7.5 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to obtain sensitive informati |
| CVE-2026-18137 | 8.1 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to execute arbitrary ESQL com |
| CVE-2026-18152 | 7.4 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to forge validly-signed messa |
| CVE-2026-18154 | 8.0 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to obtain sensitive informati |
| CVE-2026-95819 | 7.3 | 2026-09-22 | A vulnerability has been found in anirbandutta9 College-Notes-Gallery up to 8c1cf3d98f30982d069c88ca172612c001eb39f6. Af |
| CVE-2026-18162 | 9.8 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to execute arbitrary code due |
| CVE-2026-18163 | 9.8 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to execute arbitrary code due |
| CVE-2026-18169 | 9.9 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote authenticated attacker to obtain sensi |
| CVE-2026-18172 | 7.4 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to obtain sensitive informati |
| CVE-2026-18176 | 7.4 | 2026-09-22 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to obtain sensitive informati |
| CVE-2026-61685 | 7.5 | 2026-09-22 | ReactPress is a publishing system for React developers. Prior to version 3.7.0, ReactPress API list endpoints build Type |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-93952 | Arista / VeloCloud Orchestrator | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-94127 | F5 / BIG-IP APM | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-93616 | Check Point / Multiple Products | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-85102 | Check Point / Multiple Products | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-7273 | Zyxel / GS1900 Series Switches | 2026-09-21 | 2026-09-24 | Unknown |
| CVE-2025-39964 | Linux / Kernel | 2026-09-18 | 2026-09-21 | Unknown |
| CVE-2026-53266 | Linux / Kernel | 2026-09-18 | 2026-09-21 | Unknown |
| CVE-2025-39682 | Linux / Kernel | 2026-09-18 | 2026-09-21 | Unknown |
| CVE-2026-58704 | Google / Pixel | 2026-09-16 | 2026-09-19 | Unknown |
| CVE-2026-76460 | Cisco / Identity Services Engine | 2026-09-16 | 2026-09-19 | Unknown |
| CVE-2026-87886 | Acronis / Backup | 2026-09-16 | 2026-09-19 | Unknown |

---

*Total entries in CISA KEV catalog: 1721*