# Vulnerability Intelligence Report

**Date:** 2026-10-29  
**Generated:** 2026-10-29T14:57:06Z  

---

## Executive Summary

Our environment faces significant vulnerability exposure with 141 high-severity CVEs identified, including critical flaws in X.org X Server, XWiki, FOG imaging systems, and commercial software. Eight vulnerabilities were added to CISA's Known Exploited Vulnerabilities catalog in the past seven days, covering Broadcom VMware ESX, Linux Kernel, Adobe Commerce, Google Brotli, and PHP — all confirmed to be actively exploited in the wild. The highest-severity finding (CVE-2026-44179, CVSS 9.9) involves remote code execution in XWiki. Immediate patching and mitigation action is required to reduce exposure and meet federal remediation timelines.

---

## Risk Narrative

The current threat landscape reflects active exploitation of enterprise infrastructure components, with CISA KEV additions confirming adversarial interest in hypervisors, operating system kernels, e-commerce platforms, and widely deployed language runtimes. Heap and buffer overflow vulnerabilities in X.org X Server create local privilege escalation paths, while web application flaws in XWiki and FOG expose organizations to remote code execution and data compromise. The combination of 141 high-severity unpatched CVEs and eight actively exploited vulnerabilities significantly elevates the likelihood of a successful breach, potential ransomware deployment, and regulatory non-compliance, translating directly into financial, reputational, and operational business risk.

---

## Prioritized Action Items

1. Patch or mitigate CVE-2026-44179 (CVSS 9.9 XWiki RCE) immediately as the critical severity poses direct business-disruption risk.
2. Apply vendor patches for all eight newly added CISA KEV entries — VMware ESX, Linux Kernel, Adobe Commerce, Google Brotli, and PHP — within mandated remediation windows.
3. Audit and patch all X.org X Server and XWayland deployments affected by the five identified heap/buffer overflow vulnerabilities (CVE-2026-93518 through CVE-2026-93521).
4. Remediate authentication and authorization vulnerabilities in FOG, Shopper, Ninja Forms, and YosemiteCrew to prevent privilege escalation and unauthorized access.
5. Establish a continuous vulnerability prioritization workflow integrating CISA KEV feed monitoring to ensure future exploited CVEs are flagged and remediated within 48 hours.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-93518 | 7.8 | 2026-10-28 | An integer truncation issue in XkbResizeKeyType() that could lead to a heap buffer overflow by authenticated X clients i |
| CVE-2026-93519 | 7.8 | 2026-10-28 | A buffer overflow when handling pointer barriers in the XFIXES extension in X.Org X server before 21.1.25 and XWayland b |
| CVE-2026-93520 | 7.8 | 2026-10-28 | A heap buffer overflow caused by mismatching size calculations between XkbAllocNames and  ChangeKeycodeRange in X.org X  |
| CVE-2026-112357 | 7.8 | 2026-10-28 | GFI KerioConnect (Kerio Connect) Outlook Connector (Offline Edition), 'KOFF', before 10.0.9 Patch 2 contains a local pri |
| CVE-2026-116778 | 8.8 | 2026-10-28 | FOG is a free open-source cloning/imaging/rescue suite/inventory management system. Prior to 1.5.10.2253 and 1.6.0-RC-1, |
| CVE-2026-44179 | 9.9 | 2026-10-28 | XWiki Remote Macros provides XWiki rendering macros that are useful when migrating content from Confluence. From 1.13 un |
| CVE-2026-56828 | 8.8 | 2026-10-28 | Shopper is a Headless e-commerce Admin Panel. From 2.8.0 until 2.8.1, three Shopper Livewire admin components retain aut |
| CVE-2026-59979 | 8.3 | 2026-10-28 | YosemiteCrew provides organization-based service and task management. In the source-reported affected main and dev snaps |
| CVE-2026-67187 | 7.1 | 2026-10-28 | Ninja Forms plugin for WordPress before 3.15.4 contains an incomplete server-side validation vulnerability that allows u |
| CVE-2026-93521 | 7.8 | 2026-10-28 | A buffer overflow in RandR
ChangeProviderProperty requests in X.Org X Server before 2.1.25 and XWayland before 24.4.14 c |
| CVE-2026-93522 | 7.8 | 2026-10-28 | A heap buffer overflow caused by mismatched size usage in CopyArea CPU-to-FBO path in X.Org X Server before 21.1.15 and  |
| CVE-2026-100105 | 7.7 | 2026-10-28 | A user with permission to edit contact points but not their protected fields can change protected settings, such as a co |
| CVE-2026-103401 | 8.8 | 2026-10-28 | An Improper Link Resolution Before File Access ('Link Following') vulnerability in the unauthenticated web server handle |
| CVE-2026-103402 | 8.8 | 2026-10-28 | An Insufficient Verification of Data Authenticity vulnerability in PCLI in Juniper Networks Session Smart Router and Ses |
| CVE-2026-103403 | 8.8 | 2026-10-28 | An Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in AccessMan |
| CVE-2026-103406 | 9.8 | 2026-10-28 | An Improper Neutralization of Special Elements used in an OS Command vulnerability in the AutomatedProvisioner in Junipe |
| CVE-2026-103407 | 8.8 | 2026-10-28 | An Improper Limitation of a Pathname to a Restricted Directory vulnerability in ConfigDirector in Juniper Networks Sessi |
| CVE-2026-103408 | 8.8 | 2026-10-28 | A Stack Buffer Overflow vulnerability in the DHCP client in Juniper Networks Session Smart Router allows an unauthentica |
| CVE-2026-103409 | 9.8 | 2026-10-28 | A Missing authentication for critical function vulnerability in Juniper Networks Session Smart Router allows an unauthen |
| CVE-2026-103410 | 7.5 | 2026-10-28 | An Integer Overflow vulnerability in the DPI certificate scanner in Juniper Networks Session Smart Router allows an unau |
| CVE-2026-103411 | 7.1 | 2026-10-28 | An Integer Underflow vulnerability in DhcpMessageDecoder in Juniper Networks Session Smart Router allows an attacker wit |
| CVE-2026-106079 | 8.8 | 2026-10-28 | An Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in AccessMan |
| CVE-2026-118510 | 8.8 | 2026-10-28 | A type-handling flaw in the relationship query building of this MongoDB integration library can cause a check for the ab |
| CVE-2026-118602 | 7.8 | 2026-10-28 | Alpine iLX-F511 Fiv.System Exposed Dangerous Method Local Privilege Escalation Vulnerability. This vulnerability allows  |
| CVE-2026-118603 | 8.0 | 2026-10-28 | Alpine iLX-F511 vCard Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows |
| CVE-2026-118605 | 8.0 | 2026-10-28 | Alpine iLX-F511 prh_sdp_service_search_decode Stack-based Buffer Overflow Remote Code Execution Vulnerability. This vuln |
| CVE-2026-118606 | 8.8 | 2026-10-28 | Alpine iLX-F511 Framework Service Exposed Dangerous Function Remote Code Execution Vulnerability. This vulnerability all |
| CVE-2026-118610 | 8.8 | 2026-10-28 | Alpine iLX-F511 Android Auto Service Stack-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability |
| CVE-2026-118613 | 7.8 | 2026-10-28 | Ultralytics torch_load Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vulnerability allows  |
| CVE-2026-118614 | 7.8 | 2026-10-28 | Ultralytics check_det_dataset Code Injection Remote Code Execution Vulnerability. This vulnerability allows remote attac |
| CVE-2026-118615 | 7.8 | 2026-10-28 | Ultralytics torch_safe_load Command Injection Remote Code Execution Vulnerability. This vulnerability allows remote atta |
| CVE-2026-118616 | 7.8 | 2026-10-28 | Ultralytics parse_model Code Injection Remote Code Execution Vulnerability. This vulnerability allows remote attackers t |
| CVE-2026-118617 | 7.8 | 2026-10-28 | Ultralytics load_dataset_cache_file Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vulnerab |
| CVE-2026-118618 | 7.8 | 2026-10-28 | Ultralytics parse_model Code Injection Remote Code Execution Vulnerability. This vulnerability allows remote attackers t |
| CVE-2026-118619 | 8.8 | 2026-10-28 | Ultralytics Google Drive Download Path Traversal Remote Code Execution Vulnerability. This vulnerability allows remote a |
| CVE-2026-82961 | 7.8 | 2026-10-28 | The GPIO syscall handlers in drivers/gpio/gpio_handlers.c did not validate the pin argument supplied by a user-mode call |
| CVE-2026-88967 | 7.7 | 2026-10-28 | A user with query access to an Azure Monitor data source in Grafana can cause server-side requests to an attacker-contro |
| CVE-2026-93523 | 7.8 | 2026-10-28 | A heap buffer overflow caused by a XIPassiveUngrabDevice request with an out-of-range modifier value in X.Org X Server b |
| CVE-2026-116795 | 7.5 | 2026-10-28 | RE2JS is the JavaScript port of RE2, a regular expression engine that provides linear time matching. From 2.2.0 until 2. |
| CVE-2026-84725 | 8.1 | 2026-10-28 | when EAP runs with -secmgr, the openjdk-orb's JDKBridge honours attacker-supplied CDR codebase URLs during object unmars |
| CVE-2026-118257 | 7.2 | 2026-10-28 | Vue I18n is the internationalization plugin for Vue.js. From 11.1.10 until 11.4.14 and from 12.0.0-alpha.4 until 12.0.0- |
| CVE-2026-118633 | 8.1 | 2026-10-28 | A path traversal vulnerability allows a remote unauthenticated attacker to execute arbitrary code as root in Sophos UTM  |
| CVE-2026-118641 | 7.5 | 2026-10-28 | n8n before 1.123.85, 2.x before 2.43.5, and 2.44.x before 2.44.1 contains an OData $filter injection vulnerability in th |
| CVE-2026-118642 | 7.1 | 2026-10-28 | n8n before 1.123.85, 2.43.5, and 2.44.1 contains an authorization bypass vulnerability that allows authenticated members |
| CVE-2026-118643 | 8.2 | 2026-10-28 | n8n before 1.123.85, 2.x before 2.43.5, and 2.44.x before 2.44.1 stores credential secrets in execution error data when  |
| CVE-2026-118644 | 7.7 | 2026-10-28 | n8n before 2.41.5 and 2.42.x before 2.42.2 passes a failed workflow's full execution context, including the identity of  |
| CVE-2026-118645 | 8.7 | 2026-10-28 | n8n before 1.123.85, 2.x before 2.43.5, and 2.44.x before 2.44.1 contains a filter injection vulnerability in the Quick  |
| CVE-2026-118647 | 8.2 | 2026-10-28 | n8n before 1.123.85, 2.x before 2.43.5, and 2.44.x before 2.44.1 saves the SeaTable Trigger node's API token in error ex |
| CVE-2026-118648 | 7.3 | 2026-10-28 | n8n before 1.123.85, 2.x before 2.43.5, and 2.44.x before 2.44.1 contains a stored cross-site scripting vulnerability be |
| CVE-2026-118649 | 8.3 | 2026-10-28 | n8n before 2.43.5 and 2.44.x before 2.44.1 accepts a client-supplied workflow ID and caches each workflow's owner projec |
| CVE-2026-118675 | 7.1 | 2026-10-28 | n8n before 1.123.85, 2.43.5, and 2.44.1 contains a credential guard bypass vulnerability that allows editors of shared w |
| CVE-2026-118676 | 7.1 | 2026-10-28 | n8n before 1.123.85, 2.43.5, and 2.44.1 contains an authorization bypass vulnerability that allows member users to use c |
| CVE-2026-118678 | 7.1 | 2026-10-28 | n8n before 2.41.4 and 2.42.x before 2.42.1 contains a prototype pollution vulnerability that allows low-privileged users |
| CVE-2026-118679 | 7.5 | 2026-10-28 | n8n before 1.123.83, 2.41.4, and 2.42.1 contains a server-side request forgery vulnerability in the Slack Trigger webhoo |
| CVE-2026-118683 | 8.8 | 2026-10-28 | MONAI from 1.2.0 before 1.6.1 contains a remote code execution vulnerability in ConfigWorkflow.__init__, which passes a  |
| CVE-2026-118686 | 7.5 | 2026-10-28 | EspoCRM before 9.3.11 and 10.x before 10.0.8 contains a denial of service vulnerability in which the password-redaction  |
| CVE-2026-118688 | 7.9 | 2026-10-28 | wasmtime-wasi in Wasmtime before 36.0.18, 37.0.0 before 48.0.6, and 49.0.0 before 49.0.3 re-appends a trailing slash to  |
| CVE-2025-14260 | 8.3 | 2026-10-28 | Due to the improper implementation of access control rules, the WSO2 product accepts user-supplied input related to reso |
| CVE-2026-109411 | 8.1 | 2026-10-28 | An access control bypass flaw was found in Samba's vfs_ceph_rgw module in it's openat() function. An authenticated user  |
| CVE-2026-117574 | 9.1 | 2026-10-28 | A flaw was found in ai-gateway-payload-processing. An authenticated remote attacker can exploit this vulnerability by su |
| CVE-2026-118650 | 7.5 | 2026-10-28 | Echo is a Go web framework. Prior to 4.16.0 and 5.4.0, a globally mounted middleware.Static instance can interpret an en |
| CVE-2026-13451 | 7.7 | 2026-10-28 | A flaw was found in KServe. A namespace-scoped user with create/update permissions on InferenceService custom resources  |
| CVE-2026-61542 | 8.6 | 2026-10-28 | Gearboy is a Game Boy, Game Boy Color, and Super Game Boy emulator and debugger with an embedded MCP server. Gearsystem, |
| CVE-2026-63190 | 9.4 | 2026-10-28 | FearlessCMS is a flat-file `content` management system centered on simplicity and open source. Prior to version 0.1.4, f |
| CVE-2026-6647 | 7.4 | 2026-10-28 | In deployments of WSO2 Identity Server configured with a case-insensitive user store and a case-sensitive database for i |
| CVE-2026-76418 | 8.6 | 2026-10-28 | A vulnerability in the Remote Access SSL VPN service of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software |
| CVE-2026-78674 | 8.8 | 2026-10-28 | The BPMN System REST APIs do not sufficiently validate input parameters, allowing authenticated users to submit crafted  |
| CVE-2026-118659 | 7.5 | 2026-10-28 | Happy DOM is a JavaScript implementation of a web browser without its graphical user interface. Prior to 21.0.2, the Hap |
| CVE-2026-118660 | 8.6 | 2026-10-28 | Happy DOM is a JavaScript implementation of a web browser without its graphical user interface. Prior to 21.0.0, Happy D |
| CVE-2026-118682 | 7.5 | 2026-10-28 | KaringX ClashMi through 1.0.32.1801 disables TLS certificate validation by default in the HttpUtils helper, allowing att |
| CVE-2026-118689 | 7.5 | 2026-10-28 | OvenMediaEngine through 0.21.0 contains a denial of service vulnerability in OvtPacket::LoadHeader() that allows unauthe |
| CVE-2026-118690 | 9.8 | 2026-10-28 | Signal K Server before 2.33.0 contains a missing authentication vulnerability that allows unauthenticated remote attacke |
| CVE-2026-118692 | 7.0 | 2026-10-28 | CherryTree through 1.7.2 contains an OS command injection vulnerability in CtActions::link_clicked that allows attackers |
| CVE-2026-118694 | 7.5 | 2026-10-28 | python-markdown2 through 2.5.5 contains a denial of service vulnerability that allows remote users to exhaust CPU by sub |
| CVE-2026-118752 | 7.8 | 2026-10-28 | FreeImage (danoli3 fork) before 3.19.22 contains a heap buffer overflow vulnerability in the PBM RLE decoder of PluginIF |
| CVE-2026-118753 | 7.8 | 2026-10-28 | FreeImage (danoli3 fork) before 3.19.25 contains a heap buffer overflow vulnerability in PluginGIF.cpp that allows attac |
| CVE-2026-118755 | 7.2 | 2026-10-28 | Volmarg Personal Management System through 2.1.0 contains an OS command injection vulnerability that allows authenticate |
| CVE-2026-118803 | 7.5 | 2026-10-28 | Bricks Theme 2.4.3 and before contains an unauthenticated dynamic-data tag injection vulnerability that allows anonymous |
| CVE-2026-118804 | 7.5 | 2026-10-28 | Bricks Builder 2.4.3 and before contains a broken access control vulnerability that allows unauthenticated attackers to  |
| CVE-2026-54453 | 7.2 | 2026-10-28 | OpenCATS is an open-source applicant tracking system and recruitment CRM for staffing agencies and hiring teams. Prior t |
| CVE-2026-54455 | 7.6 | 2026-10-28 | OpenCATS is an open-source applicant tracking system and recruitment CRM for staffing agencies and hiring teams. Prior t |
| CVE-2026-61564 | 10.0 | 2026-10-28 | AVideo is a video-sharing Platform. Prior to 8.1.0, the unauthenticated installer endpoint `install/checkConfiguration.p |
| CVE-2026-61567 | 10.0 | 2026-10-28 | AVideo is a video-sharing Platform. Prior to 8.1.0, the live-streaming endpoint `view/videosListToLive.php` accepts an a |
| CVE-2026-61569 | 7.5 | 2026-10-28 | AVideo is a video-sharing Platform. Prior to 8.1.0, the unauthenticated streamer login at `objects/login.json.php` passe |
| CVE-2026-61571 | 7.3 | 2026-10-28 | AVideo is a video-sharing Platform. Prior to 8.1.0, the encoder lacks a global authentication layer and exposes control  |
| CVE-2026-61572 | 8.6 | 2026-10-28 | AVideo is a video-sharing Platform. Before the initial remediation attempt in 8.1.0, `url_get_contents` in `objects/func |
| CVE-2026-93851 | 8.0 | 2026-10-28 | Mattermost versions 11.9.x <= 11.9.1, 11.8.x <= 11.8.5, 11.7.x <= 11.7.10 fail to validate the target post ID in the Age |
| CVE-2026-118579 | 9.8 | 2026-10-28 | A weakness has been identified in D-Link DIR-505 1.10B02. The impacted element is the function main of the file /secmark |
| CVE-2026-85749 | 8.1 | 2026-10-28 | MailWatch for MailScanner is a web-based front-end to MailScanner. Prior to 1.2.27, any authenticated MailWatch user, in |
| CVE-2026-113387 | 8.6 | 2026-10-29 | The Ortto plugin for WordPress before 1.0.25 did not authenticate configuration update requests, relying only on a secre |
| CVE-2026-109516 | 9.8 | 2026-10-29 | The Bot for Telegram on WooCommerce plugin for WordPress is vulnerable to Authentication Bypass leading to Account Takeo |
| CVE-2026-42922 | 9.8 | 2026-10-29 | A authorization bypass vulnerability exists in the /nodered functionality of FUXA (version(s): 1.3.2-2809). A specially  |
| CVE-2026-93757 | 7.5 | 2026-10-29 | The Wild Apricot Login plugin for WordPress is vulnerable to Authentication Bypass via SSO Email-Collision Account Bindi |
| CVE-2026-93855 | 7.5 | 2026-10-29 | The SendPress Newsletters plugin for WordPress is vulnerable to time-based SQL Injection via the 'subscriberid' paramete |
| CVE-2026-93904 | 7.5 | 2026-10-29 | The Social Web Suite – Social Media Auto Post, Social Media Auto Publish plugin for WordPress is vulnerable to generic S |
| CVE-2026-96228 | 8.1 | 2026-10-29 | SSL Wireless SMS Notification for WordPress is vulnerable to Authentication Bypass in all versions up to, and including, |
| CVE-2026-96666 | 7.2 | 2026-10-29 | The Schema App Structured Data plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Comment Content via |
| CVE-2026-96669 | 7.2 | 2026-10-29 | The Food Store – Online Food Delivery & Pickup plugin for WordPress is vulnerable to Stored Cross-Site Scripting via 'se |
| CVE-2026-96741 | 7.2 | 2026-10-29 | The DSGVO All in one for WP plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Comment Content via Ou |
| CVE-2026-103693 | 9.0 | 2026-10-29 | The Frontend Dashboard WordPress plugin before 3.0.5, ProfileGrid  WordPress plugin before 6.0.0.5 do not prevent an una |
| CVE-2026-111739 | 7.5 | 2026-10-29 | The Two Factor Authentication WordPress plugin before 1.17.0, All-In-One Security (AIOS)  WordPress plugin before 5.5.0  |
| CVE-2026-113616 | 9.8 | 2026-10-29 | The LogixFast Auth WordPress plugin before 1.0.4 does not deliver its password-reset one-time code to the resolved accou |
| CVE-2026-113617 | 9.9 | 2026-10-29 | The Automated Import Products to Cart WordPress plugin before 1.0.4 does not sanitize a user-supplied file path before u |
| CVE-2026-114488 | 7.4 | 2026-10-29 | A flaw was found in Wildfly. A remote attacker can bypass authentication on IIOP EJB invocations as the CSIv2 security i |
| CVE-2026-115245 | 9.8 | 2026-10-29 | The Chat AI with Dispatcher WordPress plugin before 2.4 does not properly validate uploaded files, relying only on a spo |
| CVE-2026-115301 | 7.2 | 2026-10-29 | The Contact Form by Supsystic  WordPress plugin before 1.11.1 does not sandbox the template engine used to render its fo |
| CVE-2026-118905 | 7.0 | 2026-10-29 | Node Version Manager (nvm) is a POSIX-compliant shell function for managing multiple node.js versions. In versions 0.31. |
| CVE-2026-15564 | 7.4 | 2026-10-29 | Wildfly's IIOP listener may permit deserialization of input streams before authentication is performed. An attacker who  |
| CVE-2026-86794 | 8.8 | 2026-10-29 | The Community Events WordPress plugin before 1.6.0 does not have authorisation or nonce checks when processing public ev |
| CVE-2026-89216 | 8.6 | 2026-10-29 | The vTables  WordPress plugin before 0.3 does not properly sanitise and escape a parameter before using it in a SQL stat |
| CVE-2026-107743 | 7.2 | 2026-10-29 | The Mapster WP Maps plugin for WordPress is vulnerable to Stored Cross-Site Scripting in versions up to, and including,  |
| CVE-2026-111417 | 7.5 | 2026-10-29 | A broken access control vulnerability exists in the Foxit official website’s HTML-to-PDF conversion service due to the u |
| CVE-2026-111418 | 7.5 | 2026-10-29 | A server-side request forgery (SSRF) vulnerability exists in the Foxit official website’s HTML-to-PDF conversion service |
| CVE-2026-111419 | 8.6 | 2026-10-29 | A sensitive information exposure vulnerability exists on the Foxit official website because JavaScript code contains thi |
| CVE-2026-112827 | 7.1 | 2026-10-29 | Missing Authorization vulnerability in VillaTheme HANDMADE – Dropshipping for Etsy and WooCommerce handmade-dropshipping |
| CVE-2026-114193 | 7.5 | 2026-10-29 | Missing Authorization vulnerability in Eyal Fitoussi GEO my WordPress geo-my-wp allows Exploiting Incorrectly Configured |
| CVE-2026-115592 | 7.1 | 2026-10-29 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in OceanWP OceanWP oc |
| CVE-2026-115599 | 7.5 | 2026-10-29 | Missing Authorization vulnerability in ThimPress LearnPress learnpress allows Exploiting Incorrectly Configured Access C |
| CVE-2026-115611 | 7.1 | 2026-10-29 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in PluginUs.Net Table |
| CVE-2026-115963 | 7.1 | 2026-10-29 | Missing Authorization vulnerability in VideoWhisper.com Broadcast Live Video videowhisper-live-streaming-integration all |
| CVE-2026-115964 | 9.3 | 2026-10-29 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in StylemixThemes Mot |
| CVE-2026-115965 | 8.5 | 2026-10-29 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in BuddyPress BuddyPr |
| CVE-2026-115967 | 8.8 | 2026-10-29 | Weak Authentication vulnerability in Hamid Alinia Login with phone number login-with-phone-number allows Authentication  |
| CVE-2026-116409 | 7.1 | 2026-10-29 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WP Swings Upsell O |
| CVE-2026-33923 | 7.2 | 2026-10-29 | A signature verification vulnerability was discovered in the update installation functionality due to inconsistent valid |
| CVE-2026-33924 | 7.2 | 2026-10-29 | Two OS command injection vulnerabilities were discovered in the update installation functionality due to insufficient va |
| CVE-2026-103665 | 7.8 | 2026-10-29 | The installer for Yamaha LAN Monitor for Windows provided by Yamaha Corporation may insecurely load Dynamic Link Librari |
| CVE-2026-110184 | 7.5 | 2026-10-29 | The Newsmatic theme for WordPress is vulnerable to blind SQL Injection via the 'slug' parameter in all versions up to, a |
| CVE-2026-115821 | 7.2 | 2026-10-29 | The NewsmanApp plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'billing_first_name, billing_la |
| CVE-2026-119025 | 7.5 | 2026-10-29 | open 7.2.0 before 11.0.0 contains an OS command injection vulnerability that allows attackers to execute PowerShell code |
| CVE-2026-119027 | 7.5 | 2026-10-29 | oapi-codegen 2.5.0 before 2.8.1 contains a code injection vulnerability that allows attackers to inject Go code by suppl |
| CVE-2026-119028 | 8.8 | 2026-10-29 | oapi-codegen 2.0.0 before 2.8.1 contains a code injection vulnerability that allows attackers to inject Go code by suppl |
| CVE-2026-96767 | 7.2 | 2026-10-29 | The NEX-Forms – Ultimate Forms Plugin for WordPress plugin for WordPress is vulnerable to Stored Cross-Site Scripting vi |
| CVE-2026-97854 | 9.8 | 2026-10-29 | Yamaha wireless LAN router NWR100 provided by Yamaha Corporation contains an OS command injection vulnerability. Arbitra |
| CVE-2026-49142 | 8.8 | 2026-10-29 | OpenEMR before 8.5.0 contains an authenticated SQL injection vulnerability in the Syndromic Surveillance module that all |
| CVE-2019-25781 | 7.5 | 2026-10-29 | Python-Markdown 3.0 through 3.11.2 contains an algorithmic complexity vulnerability in inline link parsing that allows r |
| CVE-2026-116399 | 8.8 | 2026-10-29 | Cross-Site Request Forgery (CSRF) vulnerability in InstaWP InstaWP Connect instawp-connect allows Cross Site Request For |
| CVE-2026-119049 | 7.6 | 2026-10-29 | FreeMail before 5.3.2 contains an authorization bypass vulnerability that allows authenticated users to claim another us |
| CVE-2026-119050 | 8.1 | 2026-10-29 | Agno through 3.1.11 contains an unsafe reflection vulnerability in PandasTools that allows attackers to invoke arbitrary |
| CVE-2026-119052 | 7.5 | 2026-10-29 | llama.cpp b2877 before b11935 contains an uncaught exception vulnerability in the ggml-rpc server that allows unauthenti |
| CVE-2026-39736 | 8.5 | 2026-10-29 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Crocoblock JetEngi |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-41709 | Broadcom / VMware ESX | 2026-10-28 | 2026-11-11 | Unknown |
| CVE-2026-46300 | Linux / Kernel | 2026-10-28 | 2026-10-31 | Unknown |
| CVE-2026-48356 | Adobe / Commerce and Magento | 2026-10-27 | 2026-11-10 | Unknown |
| CVE-2026-111497 | Google / Brotli | 2026-10-27 | 2026-11-10 | Unknown |
| CVE-2026-109618 | PHP Group / PHP | 2026-10-26 | 2026-10-29 | Unknown |
| CVE-2026-109619 | PHP Group / PHP | 2026-10-26 | 2026-10-29 | Unknown |
| CVE-2026-114625 | Arista / VeloCloud Orchestrator | 2026-10-23 | 2026-10-26 | Unknown |
| CVE-2026-110447 | Collabora / Collabora Online – Built-in CODE Server | 2026-10-23 | 2026-10-26 | Unknown |

---

*Total entries in CISA KEV catalog: 1762*