# Vulnerability Intelligence Report

**Date:** 2026-09-23  
**Generated:** 2026-09-23T13:22:06Z  

---

## Executive Summary

Our environment faces critical exposure across 248 high-severity vulnerabilities, including multiple CVSS 9.8 flaws enabling SQL injection and remote code execution in network devices and infrastructure controllers. Most urgently, CVE-2026-94127 affecting F5 BIG-IP APM is actively exploited in the wild and listed in the CISA Known Exploited Vulnerabilities catalog with a federal remediation deadline of September 25, 2026. NVIDIA Infrastructure Controller vulnerabilities with hard-coded credentials and missing authentication compound risk significantly. Eleven new KEV entries in seven days signal an accelerating threat environment requiring immediate prioritization.

---

## Risk Narrative

The current threat landscape reflects a sharp rise in actively exploited vulnerabilities targeting network infrastructure, AI platforms, and edge devices. Eleven KEV additions in a single week indicate adversaries are rapidly weaponizing newly disclosed flaws. Critical vulnerabilities in NVIDIA Infrastructure Controller—including hard-coded credentials and authentication bypass—expose core compute infrastructure to full compromise. Remote code execution flaws in D-Link and F5 BIG-IP represent direct entry points for ransomware and lateral movement. Business risks include operational disruption, data exfiltration, regulatory penalties, and reputational damage. The concentration of CVSS 9.8 vulnerabilities demands board-level attention and accelerated patch cadence.

---

## Prioritized Action Items

1. Patch or mitigate CVE-2026-94127 (F5 BIG-IP APM heap buffer overflow) immediately to meet the CISA KEV deadline of September 25, 2026.
2. Remediate CVE-2026-65113 and CVE-2026-65114 in NVIDIA Infrastructure Controller to eliminate hard-coded credentials and missing authentication exposures.
3. Apply vendor patches or isolate D-Link DAP-1360 devices affected by CVE-2026-95675 to prevent unauthenticated remote code execution.
4. Address CVE-2026-12718 SQL injection vulnerability in KarelIP systems to protect against unauthorized data access or database compromise.
5. Audit and patch all newly added CISA KEV entries, including Arista VeloCloud, Check Point, and Zyxel vulnerabilities, within 30 days.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
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
| CVE-2026-94127 | 9.8 | 2026-09-22 | When a BIG-IP APM access policy and an OAuth profile are configured on a virtual server, specific malicious traffic can  |
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
| CVE-2026-88344 | 7.5 | 2026-09-22 | An out-of-bounds read vulnerability exists in the schema lexer of flatcc 4c3b999e. When an exact-length FlatBuffers sche |
| CVE-2026-88419 | 8.8 | 2026-09-22 | An unrestricted upload of files with a dangerous type in the thumbnail-upload endpoint (/index.php?m=member&f=article&v= |
| CVE-2026-89281 | 8.4 | 2026-09-22 | The Apache Lounge Windows distribution of Apache HTTP Server build contains a hardcoded configuration path vulnerability |
| CVE-2026-89282 | 9.1 | 2026-09-22 | The Apache Lounge Windows distribution of Apache HTTP Server build contains an insecure installation directory permissio |
| CVE-2026-94574 | 7.8 | 2026-09-22 | A local cross-user code execution vulnerability exists in GNU wget (Windows builds from eternallybored.org) due to a har |
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
| CVE-2026-94367 | 7.2 | 2026-09-23 | OpenEye Apex Network Video Recorder (NVR) firmware 3.2.9.376 contains an OS command injection vulnerability in recbackup |
| CVE-2026-95924 | 7.3 | 2026-09-23 | A vulnerability has been found in SourceCodester Online Reviewer Management System 1.0. Impacted is an unknown function  |
| CVE-2026-95925 | 7.3 | 2026-09-23 | A vulnerability was found in SourceCodester Online Reviewer Management System 1.0. The affected element is an unknown fu |
| CVE-2026-96271 | 7.1 | 2026-09-23 | Photoview through 2.4.0 contains an authorization bypass vulnerability in the shareAlbum GraphQL mutation that allows au |
| CVE-2026-96272 | 7.5 | 2026-09-23 | ClipBucket v5 before 5.5.3-#182 contains a blind SQL injection vulnerability in the photo search endpoint where the quer |
| CVE-2026-95926 | 7.3 | 2026-09-23 | A vulnerability was determined in SourceCodester Online Reviewer Management System 1.0. The impacted element is an unkno |
| CVE-2026-95927 | 7.3 | 2026-09-23 | A vulnerability was identified in SourceCodester Online Reviewer Management System 1.0. This affects an unknown function |
| CVE-2026-89425 | 7.5 | 2026-09-23 | UTF8DataInputJsonParser._reportInvalidToken() in FasterXML jackson-core builds the offending-token text for its error me |
| CVE-2026-91776 | 7.5 | 2026-09-23 | TypeDeserializerBase._findDeserializer() in FasterXML jackson-databind caches the resolved deserializer under the raw, a |
| CVE-2026-91777 | 7.5 | 2026-09-23 | Forward-reference completion for @JsonIdentityInfo object IDs in FasterXML jackson-databind performs a linear scan of th |
| CVE-2026-96257 | 10.0 | 2026-09-23 | A flaw has been found in Fast FAC1203R Gigabit Edition 2.0.4. Affected by this issue is the function copy_msg_element of |
| CVE-2022-4997 | 8.6 | 2026-09-23 | The jet-form-builder-stripe-gateway WordPress plugin before 1.1.0 does not sanitise and escape a payment token before us |
| CVE-2026-14321 | 8.2 | 2026-09-23 | The divi-dash WordPress plugin before 1.0.7 does not validate the source of the client IP address it uses for rate limit |
| CVE-2026-19438 | 7.5 | 2026-09-23 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in ABB Mint Workbench I.

T |
| CVE-2026-75799 | 9.0 | 2026-09-23 | The YAHMAN Add-ons WordPress plugin before 0.9.31 does not validate the type of the remote files it caches in a publicly |
| CVE-2026-82843 | 9.0 | 2026-09-23 | The WP OAuth Server ( Login with WordPress ) WordPress plugin before 6.4.0 does not bind the OpenID Connect identity ass |
| CVE-2026-86608 | 8.2 | 2026-09-23 | The WP Recipe Maker WordPress plugin before 10.8.2 does not have any authorisation check in one of its REST routes, nor  |
| CVE-2026-93508 | 8.1 | 2026-09-23 | The WC Fields Factory WordPress plugin before 4.1.11 does not properly restrict access to its field-management AJAX acti |
| CVE-2026-91789 | 7.8 | 2026-09-23 | Foxit PDF Editor/Reader’s U3D/GIF texture decoding path contained insufficient validation of image dimensions and relate |
| CVE-2026-91790 | 7.8 | 2026-09-23 | When rendering the page image, Foxit PDF Editor/Reader fails to perform validation on image objects whose optional conte |
| CVE-2026-91791 | 7.8 | 2026-09-23 | When processing a specially crafted PDF file, Foxit PDF Editor/Reader may encounter a reentrant execution condition invo |
| CVE-2026-91792 | 7.8 | 2026-09-23 | When processing a specially crafted PDF, Foxit PDF Editor/Reader may perform reentrant zoom and layout operations throug |
| CVE-2026-91793 | 7.8 | 2026-09-23 | When opening a specially crafted PDF, Foxit PDF Editor/Reader executes scripts that modify annotation rich-text attribut |
| CVE-2026-91794 | 7.8 | 2026-09-23 | An out-of-bounds write vulnerability exists in the PDF rendering process of Foxit PDF Editor/Reader due to insufficient  |
| CVE-2026-91795 | 7.8 | 2026-09-23 | Foxit PDF Editor/Reader's FileOpen plugin did not adequately validate certain encryption metadata in specially crafted P |
| CVE-2026-91797 | 7.8 | 2026-09-23 | Foxit PDF Editor/Reader failed to validate the directory traversal path in the attachment file name, resulting in malici |
| CVE-2026-91798 | 8.8 | 2026-09-23 | A local privilege escalation vulnerability exists in the update daemon of Foxit PDF Editor/Reader due to an insecure per |
| CVE-2026-91799 | 7.8 | 2026-09-23 | A use-after-free vulnerability exists in Foxit PDF Editor/Reader’s handling of JavaScript array objects. A specially cra |
| CVE-2026-91800 | 8.8 | 2026-09-23 | A local privilege escalation vulnerability exists in the installer of Foxit PDF Editor for macOS due to insufficient val |
| CVE-2026-91801 | 7.8 | 2026-09-23 | A path traversal vulnerability exists in Foxit PDF Editor/Reader's handling of embedded PDF resources. Insufficient vali |
| CVE-2026-91802 | 7.8 | 2026-09-23 | A heap-based out-of-bounds write vulnerability exists in Foxit PDF Editor/Reader’s WebP image decoding due to improper h |
| CVE-2026-91803 | 8.8 | 2026-09-23 | A local privilege escalation vulnerability exists in the updater of Foxit PDF Editor/Reader due to unsafe loading of dyn |
| CVE-2026-91804 | 7.8 | 2026-09-23 | A heap-based out-of-bounds write vulnerability exists in Foxit PDF Editor/Reader’s rendering of Circle annotations with  |
| CVE-2026-91805 | 7.8 | 2026-09-23 | A use-after-free vulnerability exists in Foxit PDF Editor/Reader’s PDF page-tree handling. A specially crafted PDF can t |
| CVE-2026-91806 | 7.8 | 2026-09-23 | A use-after-free vulnerability exists in Foxit PDF Editor/Reader’s handling of PDF form fields. Embedded JavaScript may  |
| CVE-2026-91809 | 7.8 | 2026-09-23 | A use-after-free vulnerability exists in Foxit PDF Editor/Reader’s handling of malformed PDF form fields. Improper valid |
| CVE-2026-91811 | 7.8 | 2026-09-23 | A heap-based out-of-bounds write vulnerability exists in Foxit PDF Editor/Reader’s PRC parser due to insufficient valida |
| CVE-2026-91812 | 7.9 | 2026-09-23 | A vulnerability in Foxit PDF Editor/Reader’s update mechanism allows man-in-the-middle attackers to bypass certificate v |
| CVE-2026-91813 | 8.8 | 2026-09-23 | A vulnerability in Foxit PDF Editor/Reader’s update mechanism allows an update package to be replaced between download a |
| CVE-2026-91815 | 7.8 | 2026-09-23 | Foxit PDF Editor/Reader does not perform sufficient verification of the JPEG2000 image metadata in the PDF file, which l |
| CVE-2026-91816 | 7.8 | 2026-09-23 | A use-after-free vulnerability exists in Foxit PDF Editor/Reader’s handling of PDF annotations. Reentrant annotation del |
| CVE-2026-91818 | 7.8 | 2026-09-23 | A use-after-free vulnerability exists in Foxit PDF Editor/Reader’s JavaScript handling of PDF annotations. Reentrant pag |
| CVE-2026-15027 | 8.8 | 2026-09-23 | CGServiSign developed by Changing has a OS Command Injection vulnerability. Unauthenticated remote attackers can induce  |
| CVE-2026-31377 | 7.5 | 2026-09-23 | An Improper Authentication vulnerability in the Apache Doris Frontend (FE) meta service allows an unauthenticated remote |
| CVE-2026-42801 | 7.4 | 2026-09-23 | NULL pointer dereference vulnerability in ASR Crane，Falcon on Linux (as_rrc module) allows Pointer Manipulation.

This v |
| CVE-2026-93368 | 7.5 | 2026-09-23 | The Rename wp-login.php to anything you want plugin for WordPress is vulnerable to time-based SQL Injection via 'log' (U |
| CVE-2026-95626 | 8.3 | 2026-09-23 | Tauri's Content Security Policy hardening, which injects a random nonce to restrict script execution, provides zero prot |
| CVE-2026-95627 | 7.7 | 2026-09-23 | When a Tauri application uses the dialog plugin's file or folder picker, an attacker with JavaScript execution (XSS) can |
| CVE-2026-96454 | 8.2 | 2026-09-23 | Pake turns a website into a desktop application built on Tauri. Every application it generates inherits two settings fro |
| CVE-2026-96442 | 7.8 | 2026-09-23 | A code execution flaw was found in Emacs, affecting versions prior to 31.2. The Flymake mode using language backends oth |
| CVE-2026-96455 | 8.8 | 2026-09-23 | The Reachy Mini daemon exposes an HTTP API for managing the robot. Its app installation endpoint, POST /apps/install in  |
| CVE-2026-12370 | 7.6 | 2026-09-23 | ZohoCorp ManageEngine OpManager, NetFlow Analyzer, and Network Configuration Manager versions 12.8.667 and below were vu |
| CVE-2026-14913 | 8.8 | 2026-09-23 | ZohoCorp ManageEngine OpManager and Firewall Analyzer versions 12.8.669 and below were vulnerable to an SQL Injection vu |
| CVE-2026-15358 | 7.5 | 2026-09-23 | ZohoCorp ManageEngine OpManager and Network Configuration Manager versions before 12.8.671 were vulnerable to an unautho |
| CVE-2026-77791 | 7.5 | 2026-09-23 | Uncontrolled Resource Consumption vulnerability in Apache Tomcat during sending of WebSocket close message enabled a DoS |
| CVE-2026-84787 | 8.1 | 2026-09-23 | ZohoCorp ManageEngine OpManager and Firewall Analyzer versions 12.8.710 and below were vulnerable to a Privilege Escalat |
| CVE-2026-84789 | 7.1 | 2026-09-23 | ZohoCorp ManageEngine OpManager and Firewall Analyzer versions 12.8.710 and below were vulnerable to a Broken Access Con |
| CVE-2026-84791 | 7.1 | 2026-09-23 | ZohoCorp ManageEngine OpManager and Firewall Analyzer versions 12.8.710 and below were vulnerable to a Broken Access Con |
| CVE-2026-19599 | 9.9 | 2026-09-23 | ZohoCorp ManageEngine OpManager MSP versions 12.8.709 and below were vulnerable to a Remote Code Execution vulnerability |
| CVE-2026-75825 | 8.8 | 2026-09-23 | ZohoCorp ManageEngine OpManager versions 12.8.710 and below with the Application Manager Plugin enabled were vulnerable  |
| CVE-2026-76978 | 8.8 | 2026-09-23 | ZohoCorp ManageEngine OpManager and Firewall Analyzer versions 12.8.709 and below were vulnerable to a Command Injection |
| CVE-2026-76979 | 7.7 | 2026-09-23 | ZohoCorp ManageEngine OpManager and Firewall Analyzer versions 12.8.709 and below were vulnerable to an XML Injection vu |
| CVE-2026-76980 | 7.4 | 2026-09-23 | ZohoCorp ManageEngine OpManager and Firewall Analyzer versions 12.8.709 and below were vulnerable to a Data Exposure vul |

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