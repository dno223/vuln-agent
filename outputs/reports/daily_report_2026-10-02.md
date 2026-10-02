# Vulnerability Intelligence Report

**Date:** 2026-10-02  
**Generated:** 2026-10-02T14:27:48Z  

---

## Executive Summary

Our environment faces significant exposure across 153 high-severity vulnerabilities, including critical unauthenticated privilege escalation and SQL injection flaws scoring up to 9.8. One actively exploited vulnerability, CVE-2026-104286 affecting Fortinet FortiMail, is confirmed in CISA's Known Exploited Vulnerabilities catalog with a remediation deadline of October 4, 2026. Eight new KEV entries were added this week spanning Fortinet, Cisco, Apple, and Citrix platforms, signaling a surge in active threat actor exploitation. WordPress ecosystem vulnerabilities represent a broad attack surface requiring immediate attention. Immediate remediation action is required to prevent unauthorized access, data exfiltration, and system compromise.

---

## Risk Narrative

Threat actors are actively exploiting vulnerabilities across widely deployed enterprise and web platforms, as evidenced by eight new CISA KEV additions in seven days targeting Fortinet, Cisco, Citrix, and Apple products. The presence of unauthenticated remote exploitation vectors, including SQL injection scoring 9.8 and privilege escalation scoring 9.8, dramatically lowers the barrier for attackers. WordPress ecosystem vulnerabilities expand the attack surface across potentially numerous customer-facing properties. Business risks include unauthorized data access, ransomware deployment, lateral movement, and regulatory non-compliance. The combination of active exploitation and critical CVSS scores creates an environment where unpatched systems could be compromised within hours of exposure.

---

## Prioritized Action Items

1. Patch CVE-2026-104286 Fortinet FortiMail immediately as it is actively exploited and has a CISA-mandated remediation deadline of October 4, 2026.
2. Audit and remediate CVE-2026-103752 and CVE-2026-62071, both unauthenticated privilege escalation and SQL injection flaws scoring 9.8 and 9.3 respectively, within 24 hours.
3. Assess and patch all Cisco Catalyst SD-WAN Manager, Citrix NetScaler, and Apple product instances affected by newly added KEV entries from the past seven days.
4. Inventory all WordPress plugins and update or disable vulnerable versions affected by unauthenticated IDOR, XSS, access control, and privilege escalation vulnerabilities.
5. Establish a recurring vulnerability prioritization process using CVSS scores and KEV catalog alignment to systematically reduce the 153 high-severity CVE backlog within 30 days.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2024-58388 | 7.5 | 2026-10-01 | Sharp (and Toshiba Tec rebranded) multifunction printers contain an unauthenticated local file inclusion vulnerability t |
| CVE-2026-100514 | 7.5 | 2026-10-01 | Unauthenticated Insecure Direct Object References (IDOR) in REST API Log <= 1.7.2 versions. |
| CVE-2026-100517 | 7.5 | 2026-10-01 | Unauthenticated Insecure Direct Object References (IDOR) in Photo Reviews for WooCommerce <= 1.2.30 versions. |
| CVE-2026-102378 | 7.1 | 2026-10-01 | Unauthenticated Cross Site Scripting (XSS) in Parallax Section block <= 2.0.4 versions. |
| CVE-2026-103068 | 8.8 | 2026-10-01 | Subscriber Privilege Escalation in ByteCoreStack &#8211; MCP Connector for AI Tools <= 1.2.2 versions. |
| CVE-2026-103687 | 7.3 | 2026-10-01 | A vulnerability has been found in rhukster dom-sanitizer up to 1.0.15. The affected element is the function url of the f |
| CVE-2026-103752 | 9.8 | 2026-10-01 | Unauthenticated Privilege Escalation in Authorizer <= 3.15.3 versions. |
| CVE-2026-56589 | 7.2 | 2026-10-01 | HCL BigFix Service Management is affected by a Stored Cross-Site Scripting (XSS) vulnerability, which could allow an att |
| CVE-2026-62071 | 9.3 | 2026-10-01 | Unauthenticated SQL Injection in WordPress File Upload <= 5.1.10 versions. |
| CVE-2026-62073 | 7.5 | 2026-10-01 | Unauthenticated Broken Access Control in WP Full Stripe Free <= 8.5.6 versions. |
| CVE-2026-67105 | 7.4 | 2026-10-01 | HCL BigFix Service Management is affected by an Insecure Communication vulnerability, which could allow an attacker with |
| CVE-2026-79898 | 9.1 | 2026-10-01 | Fortra BoKS Manager contains a command injection vulnerability in crlserver. An authenticated user authorized to add CRL |
| CVE-2026-79899 | 7.9 | 2026-10-01 | Fortra BoKS Manager contains an insecure temporary file vulnerability in bccgethostcert. The utility creates predictable |
| CVE-2026-94390 | 7.2 | 2026-10-01 | Editor PHP Object Injection in Hide Shipping Method For WooCommerce <= 1.5.4 versions. |
| CVE-2026-95588 | 8.6 | 2026-10-01 | Unauthenticated Arbitrary File Deletion in AcyMailing SMTP Newsletter <= 11.0.5 versions. |
| CVE-2026-97260 | 7.1 | 2026-10-01 | Unauthenticated Cross Site Scripting (XSS) in MaxGalleria <= 6.5.3 versions. |
| CVE-2026-97268 | 7.1 | 2026-10-01 | Unauthenticated Cross Site Scripting (XSS) in Premmerce Wishlist for WooCommerce <= 1.1.13 versions. |
| CVE-2026-97273 | 7.1 | 2026-10-01 | Unauthenticated Cross Site Scripting (XSS) in Premmerce Wishlist for WooCommerce <= 1.1.13 versions. |
| CVE-2026-97277 | 7.6 | 2026-10-01 | Subscriber Broken Access Control in Social Boost <= 3.6.2 versions. |
| CVE-2026-97284 | 8.8 | 2026-10-01 | Contributor PHP Object Injection in Icegram <= 3.1.31 versions. |
| CVE-2026-97297 | 7.6 | 2026-10-01 | Subscriber Broken Access Control in Gratisfaction <= 4.6.3 versions. |
| CVE-2026-12627 | 9.8 | 2026-10-01 | Fortra's Core Privileged Access Manager (BoKS) contains a stack-based buffer overflow vulnerability in boks_autoregister |
| CVE-2026-46729 | 7.5 | 2026-10-01 | NULL Pointer Dereference vulnerability in Apache HTTP Servers mod_heartmonitor over unicast listener.



This issue affe |
| CVE-2026-47360 | 7.5 | 2026-10-01 | Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache HTTP Server's mod_session_cookie modu |
| CVE-2026-79896 | 7.5 | 2026-10-01 | Fortra BoKS Manager contains an out-of-bounds read vulnerability in the custom TLS ClientHello parser used by boks_portm |
| CVE-2026-101888 | 7.2 | 2026-10-01 | The Prime Mover plugin for WordPress before 2.2.1 contains a Zip Slip path traversal vulnerability that allows authentic |
| CVE-2026-103921 | 7.4 | 2026-10-01 | GraphQL Tools provides utilities for building, stitching, and mocking GraphQL schemas. Prior to 1.1.35, the executor-leg |
| CVE-2026-12405 | 8.8 | 2026-10-01 | A flaw was found in rubygem-foreman_remote_execution. A command injection vulnerability exists in the Red Hat Satellite  |
| CVE-2026-12423 | 7.5 | 2026-10-01 | A flaw was found in Foreman. The Red Hat Satellite /unattended/provision API endpoint is vulnerable to an authentication |
| CVE-2026-12540 | 8.2 | 2026-10-01 | A flaw was found in Foreman. A command injection vulnerability exists in the foreman-rake errors:fetch_log task. The req |
| CVE-2026-12541 | 8.2 | 2026-10-01 | A flaw was found in Foreman. OS command injection vulnerabilities exist in the foreman-rake db:dump and db:import_dump t |
| CVE-2026-12544 | 7.7 | 2026-10-01 | A flaw was found in Foreman. The foreman-rake initialization logic in /usr/share/foreman/config/settings.rb contains a v |
| CVE-2026-14316 | 8.1 | 2026-10-01 | The revoked-key error path builds a human-readable failure reason using sprintf() into a heap buffer. The allocated buff |
| CVE-2026-48005 | 7.5 | 2026-10-01 | Missing authentication checks in mod_auth_digest in Apache Software Foundation Apache HTTP Server before 2.4.69 on all p |
| CVE-2026-56153 | 7.5 | 2026-10-01 | Out-of-bounds Write vulnerability in Apache HTTP Server's mod_charset_lite.



This issue affects Apache HTTP Server: fr |
| CVE-2026-56154 | 9.8 | 2026-10-01 | Use After Free vulnerability in Apache HTTP Server's mod_rewrite when using lookahead (%{LA-U:HTTP:...})



This issue a |
| CVE-2026-56449 | 7.5 | 2026-10-01 | Out-of-bounds Write vulnerability in Apache HTTP Server's mod_proxy_html with crafted HTTP response bodies.



This issu |
| CVE-2026-57941 | 9.8 | 2026-10-01 | Use After Free vulnerability in Apache HTTP Server's mod_http2 via shared session->bbtmp re-entrancy



This issue affec |
| CVE-2026-59685 | 7.5 | 2026-10-01 | Out-of-bounds Write vulnerability in Apache HTTP Server on Windows while processing paths with 8.3 names that may grow w |
| CVE-2026-59797 | 9.8 | 2026-10-01 | Improper Privilege Management vulnerability in Apache HTTP Server's mod_ssl via SSLRequire and file-related expressions. |
| CVE-2026-63045 | 7.5 | 2026-10-01 | Improper validation of FTP PASV reply address in mod_proxy_ftp in Apache Software Foundation Apache HTTP Server through  |
| CVE-2026-63292 | 7.5 | 2026-10-01 | Stack-based buffer overflow in mod_vhost_alias in Apache Software Foundation Apache HTTP Server through 2.4.68 on all pl |
| CVE-2026-63686 | 7.5 | 2026-10-01 | A NULL pointer dereference in mod_xml2enc in Apache Software Foundation Apache HTTP Server before 2.4.69 on all platform |
| CVE-2026-63718 | 7.5 | 2026-10-01 | Inconsistent Interpretation of HTTP Requests ('HTTP Request/Response Smuggling') response smuggling vulnerability in Apa |
| CVE-2026-73636 | 8.1 | 2026-10-01 | Authentication bypass by capture-replay in mod_auth_digest in Apache Software Foundation Apache HTTP Server 2.4.x on all |
| CVE-2026-73637 | 7.3 | 2026-10-01 | Use after free in mod_auth_digest in Apache Software Foundation Apache HTTP Server before 2.4.69 on all platforms allows |
| CVE-2026-93546 | 8.8 | 2026-10-01 | Integer overflow in mod_dav_fs in Apache HTTP Server through 2.4.68 allows an authenticated WebDAV client with write acc |
| CVE-2026-96658 | 9.9 | 2026-10-01 | A flaw was found in Foreman. An authenticated attacker with low-level permissions can achieve remote code execution (RCE |
| CVE-2026-96659 | 9.1 | 2026-10-01 | A flaw was found in Foreman. This vulnerability allows an authenticated user with low-level Viewer permissions to cause  |
| CVE-2023-54404 | 7.5 | 2026-10-01 | Zod schema-validation library through 4.6.5 contains an uncontrolled resource consumption vulnerability that allows atta |
| CVE-2026-103922 | 9.3 | 2026-10-01 | Capacitor is a cross-platform native runtime for web applications. From 6.0.0 until 6.2.2, 7.6.9, 8.3.5, 8.4.3, and 8.5. |
| CVE-2026-104018 | 8.8 | 2026-10-01 | An improper privilege management vulnerability (CWE-269) exists in the command shell of Wind River VxWorks 7 when config |
| CVE-2026-68495 | 7.5 | 2026-10-01 | The CBOR parser in FasterXML jackson-dataformats-binary never invokes StreamReadConstraints.validateNameLength() when de |
| CVE-2026-68496 | 7.5 | 2026-10-01 | The Smile parser in FasterXML jackson-dataformats-binary never invokes StreamReadConstraints.validateNameLength() when d |
| CVE-2026-97662 | 8.2 | 2026-10-01 | An argument injection issue in the diff scan operation in AWS security-agent-mcp-server before version 0.2.0 might allow |
| CVE-2026-104057 | 7.5 | 2026-10-01 | Podgrab contains an unauthenticated denial-of-service vulnerability caused by unsynchronized concurrent access to shared |
| CVE-2026-104059 | 8.1 | 2026-10-01 | Lektor 3.3.14 and 3.4.0b15 contains a cross-site request forgery vulnerability in the admin API blueprint that allows un |
| CVE-2026-15911 | 7.4 | 2026-10-01 | Confluent Kafka Python client's HashiCorp Vault KMS integration could allow a remote attacker to obtain sensitive inform |
| CVE-2026-55083 | 9.1 | 2026-10-01 | DHIS2 is a flexible information system for data capture, management, validation, analytics and visualization. From versi |
| CVE-2026-55230 | 8.7 | 2026-10-01 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to version |
| CVE-2026-55231 | 7.2 | 2026-10-01 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to version |
| CVE-2026-55232 | 7.6 | 2026-10-01 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to version |
| CVE-2026-102628 | 9.3 | 2026-10-01 | The Cadmos LTI application hosted at cadmos.eummena.io had Laravel debug mode enabled (APP_DEBUG=true, APP_ENV=local) in |
| CVE-2026-102667 | 8.3 | 2026-10-01 | Joyland AI app allows an attacker with shared network access to inject JavaScript into content loaded in WebView. Withou |
| CVE-2026-103484 | 8.8 | 2026-10-01 | IVFFlat index build in pgvector before 0.8.7 allows a database user to write data out-of-bounds, which can lead to arbit |
| CVE-2026-104286 | 9.8 | 2026-10-01 | An improper limitation of a pathname to a restricted directory ('path traversal') vulnerability in Fortinet FortiMail 8. |
| CVE-2026-53953 | 9.1 | 2026-10-01 | GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. In versio |
| CVE-2026-53964 | 7.2 | 2026-10-01 | Document Merge Service is a document template merge service providing an API to manage templates and merge them with giv |
| CVE-2026-54049 | 8.7 | 2026-10-01 | Sakai is a Collaboration and Learning Environment (CLE). From versions 23.0 to before 23.5, and versions 25.0 to before  |
| CVE-2026-56660 | 9.1 | 2026-10-01 | GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. Prior to  |
| CVE-2026-56661 | 7.5 | 2026-10-01 | GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. Prior to  |
| CVE-2026-56662 | 9.6 | 2026-10-01 | GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. Prior to  |
| CVE-2026-104020 | 7.5 | 2026-10-01 | Uncontrolled recursion in the Ion reader in Amazon Ion Python before 0.15.0 might allow a remote unauthenticated actor t |
| CVE-2026-104051 | 8.2 | 2026-10-01 | PictShare before 3.7.1 contains an information disclosure vulnerability that allows unauthenticated attackers to obtain  |
| CVE-2026-86344 | 7.5 | 2026-10-01 | A flaw was found in 389-ds-base. An unauthenticated remote attacker can send a complete LDAP operation followed by the f |
| CVE-2026-103761 | 7.5 | 2026-10-01 | Mooncake transfer engine through 0.3.13.post1 contains a memory exhaustion vulnerability in TransferMetadata::receivePee |
| CVE-2026-103764 | 9.8 | 2026-10-02 | Mooncake transfer engine before 0.3.13 contains an untrusted pointer dereference in ServerSession::readHeader that allow |
| CVE-2026-103765 | 9.4 | 2026-10-02 | Mooncake through 0.3.13.post1 contains a missing authentication vulnerability in the HTTP metadata server /metadata hand |
| CVE-2026-103766 | 7.2 | 2026-10-02 | ClipBucket v5 through 5.5.3-#197 contains an sql injection vulnerability that allows authenticated users with ad_manager |
| CVE-2026-86345 | 9.0 | 2026-10-02 | A flaw was found in 389-ds-base. The server does not discard plaintext bytes already buffered from a client connection w |
| CVE-2026-103096 | 7.5 | 2026-10-02 | API
key is hardcoded and retrievable from the application package. Since Android
applications can be reverse engineered, |
| CVE-2026-103097 | 7.5 | 2026-10-02 | An API key is
hardcoded and retrievable from the application package. Since Android
applications can be reverse engineer |
| CVE-2026-103098 | 7.5 | 2026-10-02 | Transmission of a sensitive key in the URL
over an unencrypted HTTP connection.  The
request is sent over HTTP rather th |
| CVE-2026-104120 | 7.3 | 2026-10-02 | A security vulnerability has been detected in modelcontextprotocol mcp-server-fetch and mcp-server-everything up to 2026 |
| CVE-2026-104123 | 7.3 | 2026-10-02 | A vulnerability was detected in SourceCodester Online Reviewer Management System 1.0. Affected by this vulnerability is  |
| CVE-2026-14378 | 9.8 | 2026-10-02 | The DevKit Pro plugin for WordPress is vulnerable to Authentication Bypass Leading to Administrator Account Takeover in  |
| CVE-2026-93367 | 7.2 | 2026-10-02 | The Visitors Traffic Real Time Statistics Pro plugin for WordPress is vulnerable to unauthenticated stored Cross-Site Sc |
| CVE-2026-10026 | 7.2 | 2026-10-02 | The CTX Feed Pro plugin for WordPress is vulnerable to Code Injection in all versions up to, and including, 7.6.12. This |
| CVE-2026-19660 | 9.8 | 2026-10-02 | The Divi Membership plugin for WordPress is vulnerable to Authentication Bypass in all versions up to, and including, 2. |
| CVE-2026-15896 | 9.1 | 2026-10-02 | The Super Forms – Drag & Drop Form Builder plugin for WordPress is vulnerable to Directory Traversal in all versions up  |
| CVE-2026-15897 | 8.8 | 2026-10-02 | The Super Forms – Drag & Drop Form Builder plugin for WordPress is vulnerable to Privilege Escalation in all versions up |
| CVE-2026-90438 | 7.2 | 2026-10-02 | The Ninja Forms – The Contact Form Builder That Grows With You plugin for WordPress is vulnerable to Stored Cross-Site S |
| CVE-2026-91828 | 7.5 | 2026-10-02 | The OMGF \| GDPR/DSGVO Compliant, Faster Google Fonts. Easy. WordPress plugin before 6.3.11 does not require authenticati |
| CVE-2026-92174 | 7.5 | 2026-10-02 | The SiteOrigin Widgets Bundle plugin for WordPress is vulnerable to Local File Inclusion in all versions up to, and incl |
| CVE-2026-92820 | 8.1 | 2026-10-02 | The Ninja Forms - File Uploads plugin for WordPress is vulnerable to arbitrary file operations in all versions up to, an |
| CVE-2026-102565 | 7.2 | 2026-10-02 | The BA Book Everything plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'booking_service_qty' p |
| CVE-2026-93029 | 9.0 | 2026-10-02 | There is a stored XSS vulnerability allowing arbitrary code execution in the WHM Manage SSL Hosts interface. |
| CVE-2026-93697 | 9.0 | 2026-10-02 | There is a stored XSS vulnerability allowing arbitrary code execution in the WHM Mass Modify Accounts interface. |
| CVE-2026-93698 | 9.9 | 2026-10-02 | Insufficient validation allows arbitrary commands to be executed via the Multilang adminbin. |
| CVE-2026-100107 | 7.2 | 2026-10-02 | The Kubio AI Page Builder plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'comment' parameter  |
| CVE-2026-100182 | 7.2 | 2026-10-02 | The Download Monitor plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Cross-Origin postMessage to A |
| CVE-2026-102772 | 7.2 | 2026-10-02 | The CMB2 plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the '<textarea_code field id> (e.g. kl_co |
| CVE-2026-103426 | 7.2 | 2026-10-02 | The Relevanssi Premium plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the '_rt' parameter in all  |
| CVE-2026-93756 | 7.2 | 2026-10-02 | The Smash Balloon Social Post Feed – Simple Social Feeds for WordPress plugin for WordPress is vulnerable to Stored Cros |
| CVE-2026-95670 | 7.2 | 2026-10-02 | The No External Links plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Log URL via /goto/{base64} R |
| CVE-2026-95817 | 7.2 | 2026-10-02 | The DoFollow Case by Case plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Comment Content in all v |
| CVE-2026-96566 | 7.2 | 2026-10-02 | The Newsletter – Send awesome emails from WordPress plugin for WordPress is vulnerable to Stored Cross-Site Scripting vi |
| CVE-2026-96567 | 7.2 | 2026-10-02 | The MW WP Form plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'post_id' parameter in all vers |
| CVE-2026-96578 | 7.2 | 2026-10-02 | The GSpeech TTS – WordPress Text To Speech Plugin plugin for WordPress is vulnerable to Stored Cross-Site Scripting via  |
| CVE-2026-96871 | 7.2 | 2026-10-02 | The Mang Board plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'data_type' parameter in all ve |
| CVE-2026-97336 | 7.2 | 2026-10-02 | The CMB2 plugin for WordPress is vulnerable to Stored Cross-Site Scripting via 'file_list' Field Type in all versions up |
| CVE-2026-97342 | 7.2 | 2026-10-02 | The JetFormBuilder — Dynamic Blocks Form Builder plugin for WordPress is vulnerable to Stored Cross-Site Scripting via ' |
| CVE-2026-97637 | 9.8 | 2026-10-02 | The JSON API Auth plugin for WordPress is vulnerable to Authentication Bypass via Cached Session Cookie Disclosure in al |
| CVE-2026-97641 | 7.2 | 2026-10-02 | The Relevanssi – A Better Search plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Comment Content i |
| CVE-2026-97663 | 7.2 | 2026-10-02 | The Customer Reviews for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Comment Autho |
| CVE-2026-80443 | 7.4 | 2026-10-02 | Improper certificate validation vulnerability in HAVELSAN Inc. Sef - AI Chatbot Platform allows Adversary in the Middle  |
| CVE-2026-80298 | 8.8 | 2026-10-02 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in HAVELSAN Inc. Sef  |
| CVE-2026-87920 | 7.2 | 2026-10-02 | The W3 Total Cache plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Comment Content via Output-Buff |
| CVE-2026-94541 | 9.8 | 2026-10-02 | The WPMobile.App – Android and iOS App Builder plugin for WordPress is vulnerable to authorization bypass in all version |
| CVE-2026-104410 | 7.5 | 2026-10-02 | SiYuan before 3.8.5 contains an information disclosure vulnerability that allows publish readers to read password-protec |
| CVE-2026-104411 | 7.3 | 2026-10-02 | Ghost from 6.22.1 before 6.64.0 contains a stored cross-site scripting vulnerability that allows staff users to host scr |
| CVE-2026-104413 | 7.3 | 2026-10-02 | Ghost from 5.94.0 before 6.64.0 contains a stored cross-site scripting vulnerability that allows staff users, including  |
| CVE-2026-104414 | 8.1 | 2026-10-02 | Ghost from 2.5.0 before 6.64.0 contains a stored cross-site scripting vulnerability that allows attackers to inject untr |
| CVE-2026-104416 | 7.5 | 2026-10-02 | Ghost from 4.39.0 before 6.64.0 contains an information disclosure vulnerability in the Admin API that allows staff user |
| CVE-2026-104418 | 7.2 | 2026-10-02 | Ghost from 6.10.3 before 6.64.0 contains a remote code execution vulnerability that allows authenticated administrators  |
| CVE-2026-104422 | 7.5 | 2026-10-02 | The block sync download path in Zebra (zebrad) before 6.3.0 reads a block's height from its unvalidated coinbase scriptS |
| CVE-2026-104423 | 7.5 | 2026-10-02 | Zebra (zebrad) before 6.2.1 contains an asymmetric resource consumption vulnerability that allows unauthenticated peers  |
| CVE-2026-104430 | 7.5 | 2026-10-02 | Zebra zebrad 4.5.0 and zebra-script 7.0.0 count P2SH redeem script signature operations in legacy mode rather than zcash |
| CVE-2026-104431 | 7.5 | 2026-10-02 | Zebra before 6.0.0 contains a denial of service vulnerability that allows unauthenticated peers to stall Tokio workers b |
| CVE-2026-104435 | 7.4 | 2026-10-02 | Zebra zebrad 4.4.0 and zebra-script 6.0.0 fail to enforce a ZIP-244 consensus rule, accepting V5 transparent inputs sign |
| CVE-2026-104437 | 7.4 | 2026-10-02 | Zebra before 4.4.0 contains a consensus divergence vulnerability in V5 transparent signature verification, computing a Z |
| CVE-2026-104443 | 8.1 | 2026-10-02 | YesWiki before 4.6.7 contains an empty-filter scope bypass in the triples delete API that allows any authenticated user  |
| CVE-2026-104444 | 7.1 | 2026-10-02 | YesWiki before 4.6.7 contains an authorization bypass vulnerability in the comments API editComment route that allows au |
| CVE-2026-104445 | 8.2 | 2026-10-02 | YesWiki before 4.6.7 contains an authentication bypass vulnerability in the ActivityPub inbox that fails to bind the ver |
| CVE-2026-104447 | 7.1 | 2026-10-02 | YesWiki before 4.6.7 contains a cross-site request forgery vulnerability in the autoupdate UpdateAction that allows atta |
| CVE-2026-104448 | 8.1 | 2026-10-02 | YesWiki before 4.6.7 contains a cross-site request forgery vulnerability in the ajaxdeletepage handler, which permanentl |
| CVE-2026-104456 | 7.6 | 2026-10-02 | YesWiki before 4.6.7 contains a second-order SQL injection vulnerability in AclService::updateRequestWithACL, where a st |
| CVE-2026-104457 | 8.6 | 2026-10-02 | YesWiki before 4.6.7 contains an SQL injection vulnerability in the Bazar filtertags action, which wraps unescaped filte |
| CVE-2026-104460 | 7.5 | 2026-10-02 | YesWiki before 4.6.7 contains a blind SQL injection vulnerability in the {{newtextsearch}} action because Bazar list opt |
| CVE-2026-104462 | 7.5 | 2026-10-02 | YesWiki before 4.6.7 contains an SQL injection vulnerability in the Bazar nuagetag action, which concatenates the unesca |
| CVE-2026-104463 | 7.0 | 2026-10-02 | YesWiki before 4.6.7 contains a server-side request forgery vulnerability that allows unauthenticated attackers to trigg |
| CVE-2026-104464 | 8.6 | 2026-10-02 | YesWiki before 4.6.7 contains a server-side request forgery vulnerability that allows unauthenticated attackers to make  |
| CVE-2026-104467 | 8.1 | 2026-10-02 | YesWiki before 4.6.7 contains an authorization bypass vulnerability in ApiService::isAuthorized() that allows unauthenti |
| CVE-2026-104470 | 7.4 | 2026-10-02 | YesWiki before 4.6.7 contains a server-side request forgery vulnerability in the Bazar valeur action that allows page ed |
| CVE-2026-104471 | 7.2 | 2026-10-02 | YesWiki before 4.6.7 contains an unrestricted file upload vulnerability that allows authenticated admins to write remote |
| CVE-2026-104472 | 7.5 | 2026-10-02 | YesWiki before 4.6.7 contains a missing authorization vulnerability in the attachment download handler that allows unaut |
| CVE-2026-104609 | 7.3 | 2026-10-02 | A weakness has been identified in onetwothreeneth HospitalManagementSystem up to 9ef91ed6007314b6473110ed699dff76d158f61 |
| CVE-2026-104610 | 10.0 | 2026-10-02 | A security vulnerability has been detected in Tenda HG7, HG9 and HG10 300001138_en_xpon. This impacts the function boaGe |
| CVE-2026-104611 | 9.1 | 2026-10-02 | A vulnerability was detected in Tenda AC9 15.03.02.13. Affected is an unknown function of the file /goform/fast_setting_ |
| CVE-2026-19652 | 9.8 | 2026-10-02 | The Divi Membership plugin for WordPress is vulnerable to Privilege Escalation in versions up to, and including, 2.2.0.  |
| CVE-2026-85215 | 7.1 | 2026-10-02 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in GG Soft Software S |
| CVE-2026-93875 | 7.2 | 2026-10-02 | The JetAppointment plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'friendlyTime' parameter in |
| CVE-2026-94422 | 8.8 | 2026-10-02 | An incorrect implementation of message filtering in xdg-dbus-proxy versions before 0.1.9 allows an attacker to bypass th |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-104286 | Fortinet / FortiMail | 2026-10-01 | 2026-10-04 | Unknown |
| CVE-2026-76504 | Cisco / Catalyst SD-WAN Manager | 2026-09-30 | 2026-10-03 | Unknown |
| CVE-2026-86950 | Apple / Multiple Products | 2026-09-29 | 2026-10-02 | Unknown |
| CVE-2026-88772 | Citrix / NetScaler | 2026-09-27 | 2026-09-30 | Unknown |
| CVE-2026-88771 | Citrix / NetScaler | 2026-09-27 | 2026-09-30 | Unknown |
| CVE-2026-67279 | MikroTik / RouterOS | 2026-09-25 | 2026-09-28 | Unknown |
| CVE-2026-65660 | Microsoft / SharePoint | 2026-09-25 | 2026-09-28 | Unknown |
| CVE-2026-87902 | WordPress / Core | 2026-09-25 | 2026-09-28 | Unknown |

---

*Total entries in CISA KEV catalog: 1731*