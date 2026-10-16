# Vulnerability Intelligence Report

**Date:** 2026-10-16  
**Generated:** 2026-10-16T13:01:11Z  

---

## Executive Summary

Our environment faces significant exposure from 211 high-severity vulnerabilities, including multiple critical-rated flaws (CVSS 9.8) enabling privilege escalation and remote code execution via object injection in widely used WordPress plugins. Seven new actively exploited vulnerabilities were added to CISA's Known Exploited Vulnerabilities catalog this week, affecting Atlassian, Cisco, Palo Alto Networks, and Ahsay products. SQL injection vulnerabilities scoring 9.3 in plugins like Link Whisper and Mang Board WP pose immediate data breach risks. While no monitored CVEs currently match the KEV catalog, the volume and severity of exposures demand immediate prioritization and remediation efforts across web infrastructure and network security appliances.

---

## Risk Narrative

The current threat landscape reflects a concentrated attack surface across web application plugins and enterprise network appliances. Threat actors are actively exploiting vulnerabilities in Atlassian, Cisco, and Palo Alto platforms, as confirmed by recent CISA KEV additions. WordPress ecosystem vulnerabilities, particularly privilege escalation and SQL injection flaws, present high-likelihood pathways for unauthorized data access, lateral movement, and full system compromise. Business risks include regulatory penalties from potential data breaches, operational disruption from ransomware leveraging privilege escalation chains, and reputational damage. The high volume of unpatched critical CVEs suggests patch management processes require immediate reinforcement to reduce mean time to remediation across the organization.

---

## Prioritized Action Items

1. Immediately patch or disable affected WordPress plugins with CVSS 9.8 ratings, specifically Link Whisper Free and Frontend Admin by DynamiApps, to prevent privilege escalation and object injection attacks.
2. Apply vendor patches for all CISA KEV-listed products including Palo Alto PAN-OS, Cisco Secure Email Gateway, and Atlassian products within 24-48 hours per federal mandate guidance.
3. Conduct emergency SQL injection mitigation for Link Whisper Free and Mang Board WP plugins, including input validation controls and WAF rule deployment, to protect sensitive databases.
4. Audit and restrict API gateway deployments running api-gateway versions 1.7.3 or earlier to prevent rate-limit bypass and potential denial-of-service abuse.
5. Establish a continuous vulnerability monitoring program to detect KEV catalog matches against the full asset inventory, reducing response time when actively exploited CVEs emerge.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-107416 | 7.5 | 2026-10-15 | Authorization Bypass Through User-Controlled Key vulnerability in Webba Plugins Webba Booking webba-booking-lite allows  |
| CVE-2026-109685 | 7.1 | 2026-10-15 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Link Whisper INC L |
| CVE-2026-109686 | 9.8 | 2026-10-15 | Deserialization of Untrusted Data vulnerability in Link Whisper INC Link Whisper Free link-whisper allows Object Injecti |
| CVE-2026-109688 | 9.3 | 2026-10-15 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Link Whisper INC L |
| CVE-2026-109692 | 7.1 | 2026-10-15 | Missing Authorization vulnerability in ThemeGrill User Registration user-registration allows Exploiting Incorrectly Conf |
| CVE-2026-109693 | 8.8 | 2026-10-15 | Incorrect Privilege Assignment vulnerability in WP ManageNinja LLC Fluent CRM fluent-crm allows Privilege Escalation.Thi |
| CVE-2026-109698 | 9.3 | 2026-10-15 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Kitae Park Mang Bo |
| CVE-2026-109702 | 7.1 | 2026-10-15 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in maxfoundry Social  |
| CVE-2026-109892 | 9.8 | 2026-10-15 | Incorrect Privilege Assignment vulnerability in Shabti Kaplan Frontend Admin by DynamiApps acf-frontend-form-element all |
| CVE-2026-110723 | 7.5 | 2026-10-15 | In `api-gateway` versions till `1.7.3`, The default rate-limit key resolver, `ClientIpKeyResolver`, derives the per-clie |
| CVE-2026-79837 | 7.3 | 2026-10-15 | A vulnerability in HPE NonStop SQL/MX UDR SERVER may allow a crafted message to cause process termination, service disru |
| CVE-2026-99999 | 9.3 | 2026-10-15 | In the Linux kernel, the following vulnerability has been resolved:

ipv4: validate checksum_start before completing che |
| CVE-2026-108116 | 7.5 | 2026-10-15 | In Progress Kendo UI for jQuery prior to v2026.3.1015, specially crafted filter values in the PivotGrid XMLA transport c |
| CVE-2026-110746 | 7.8 | 2026-10-15 | A local privilege escalation vulnerability in TotalAV allows an unprivileged local user to forge the gRPC IPC authentica |
| CVE-2026-110957 | 10.0 | 2026-10-15 | A vulnerability has been found in Wavlink WL-WN530BE2-A up to M30BE2_V250604. The affected element is the function sub_1 |
| CVE-2026-47168 | 9.1 | 2026-10-15 | EspoCRM is an open source customer relationship management application. Prior to 9.3.7, an authenticated administrator c |
| CVE-2026-53574 | 7.6 | 2026-10-15 | EspoCRM is an open source customer relationship management application. From 8.1.0 until 9.3.8, an authenticated non-adm |
| CVE-2026-79838 | 7.3 | 2026-10-15 | A buffer overflow vulnerability in HPE NonStop ODBC/MX Services may cause memory corruption, resulting in application cr |
| CVE-2026-79839 | 7.3 | 2026-10-15 | A buffer overflow vulnerability in HPE NonStop ODBC/MX Server may cause memory corruption, resulting in application cras |
| CVE-2026-79840 | 7.3 | 2026-10-15 | A buffer overflow vulnerability in HPE NonStop XABroker may cause memory corruption, resulting in application crash. |
| CVE-2026-95179 | 7.5 | 2026-10-15 | An issue in lottie-android 6.7.1 and earlier (and master) allows a remote attacker to cause a denial of service via a cr |
| CVE-2026-9703 | 7.1 | 2026-10-15 | Grafana's data source proxy did not apply role-based access control to write requests forwarded to Loki data sources. A  |
| CVE-2026-100351 | 7.4 | 2026-10-15 | kin-openapi is a Go project for handling OpenAPI files. From 0.144.0 until 0.147.0, openapi3filter.ValidationHandler val |
| CVE-2026-100352 | 7.5 | 2026-10-15 | kin-openapi is a Go project for handling OpenAPI files. Prior to 0.148.0, the OpenAPI 3.1 validation path passes YAML Na |
| CVE-2026-110958 | 10.0 | 2026-10-15 | A vulnerability was found in Wavlink WN530HG4B M30HG4B_V260724. The impacted element is an unknown function of the file  |
| CVE-2026-111091 | 7.8 | 2026-10-15 | In JetBrains Junie CLI before 26.8.3 code execution was possible via an untrusted project's MCP server configuration |
| CVE-2026-111093 | 7.5 | 2026-10-15 | In JetBrains Datalore before 2026.2.1 unauthenticated path traversal via the report blob endpoint allowed reading arbitr |
| CVE-2026-111094 | 8.1 | 2026-10-15 | In JetBrains TeamCity before 2026.2, 
2026.1.4, 
2025.11.8 remote code execution via a whitelist bypass in the build mes |
| CVE-2026-111095 | 8.0 | 2026-10-15 | In JetBrains TeamCity before 2026.2, 
2026.1.4, 
2025.11.8 stored XSS in the classic project overview was possible |
| CVE-2026-45449 | 8.3 | 2026-10-15 | : Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in Unitronics |
| CVE-2026-45450 | 8.3 | 2026-10-15 | : Improper Restriction of Operations within the Bounds of a Memory Buffer vulnerability in Unitronics Unitronics UniStre |
| CVE-2026-45451 | 8.3 | 2026-10-15 | : Improper Authentication vulnerability in Unitronics Unitronics UniStream Pro/UniLogic.

This issue affects Unitronics  |
| CVE-2026-45452 | 8.3 | 2026-10-15 | Use of Externally-Controlled format string vulnerability in Unitronics Unitronics UniStream Pro/UniLogic.

This issue af |
| CVE-2026-53582 | 7.1 | 2026-10-15 | OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.10, the Trust module stores attacker-co |
| CVE-2026-57155 | 9.9 | 2026-10-15 | OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.11, the Firewall Alias GeoIP importer's |
| CVE-2026-58390 | 8.0 | 2026-10-15 | OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.11, the OpenVPN connection-status dashb |
| CVE-2026-63442 | 8.1 | 2026-10-15 | OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.11, the unauthenticated WebGUI login us |
| CVE-2026-71490 | 7.1 | 2026-10-15 | OPNsense is a FreeBSD based firewall and routing platform. Prior to 26.1.11, OPNsense\Core\ACL::hasPrivilege() appends a |
| CVE-2026-92982 | 8.5 | 2026-10-15 | A flaw was found in Ansible Operator Plugins. A low-privileged Kubernetes user can exploit a Jinja2 template injection v |
| CVE-2026-95155 | 7.5 | 2026-10-15 | FasterXML Jackson 1.x, confirmed in jackson-mapper-asl versions 1.8.3, 1.9.2, 1.9.11, 1.9.12, and 1.9.13, allows attacke |
| CVE-2026-97394 | 7.5 | 2026-10-15 | kin-openapi is a Go project for handling OpenAPI files. From 0.136.0 until 0.143.0, openapi3filter accepts OpenAPI 3.1 a |
| CVE-2026-100353 | 7.5 | 2026-10-15 | kin-openapi is a Go project for handling OpenAPI files. From 0.136.0 until 0.149.0, three openapi3filter decoder paths t |
| CVE-2026-100354 | 7.5 | 2026-10-15 | kin-openapi is a Go project for handling OpenAPI files. Prior to 0.149.0, runtime request, response, and direct schema v |
| CVE-2026-100409 | 7.5 | 2026-10-15 | OpenNext Cloudflare is an open Next.js adapter for Cloudflare. From 0.3.0 until 1.20.2, applications that enable enableC |
| CVE-2026-105065 | 7.1 | 2026-10-15 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in 8theme.com XStore  |
| CVE-2026-110812 | 9.9 | 2026-10-15 | Deserialization of untrusted data in the Gremlin graph data import component in Amazon Neptune engine might allow an aut |
| CVE-2026-61611 | 7.5 | 2026-10-15 | Lychee is a free, open-source photo-management tool. Prior to 7.6.1, POST /api/v2/Album::unlock has no throttle, attempt |
| CVE-2026-85634 | 8.8 | 2026-10-15 | A flaw was found in the ContentRepositoryImpl.copyExplodedContent function of the wildfly-core library, which is used by |
| CVE-2026-103936 | 7.5 | 2026-10-15 | libp2p is a JavaScript implementation of the libp2p networking stack. Prior to 6.0.28, the @libp2p/webrtc webRTCDirect() |
| CVE-2026-111105 | 7.0 | 2026-10-15 | Telegram rlottie Numeric Truncation Remote Code Execution Vulnerability. This vulnerability allows remote attackers to e |
| CVE-2026-55103 | 8.6 | 2026-10-15 | Discourse ActivityPub adds ActivityPub support to Discourse. Prior to commit 1c8518b0f2abdf31cbea3e0b242f74d8994a9ba5, i |
| CVE-2026-55246 | 7.8 | 2026-10-15 | bincookie is a header-only binarycookies parser. Prior to 0.1.9, bincookie_init_file() in bincookie.h allocates a buffer |
| CVE-2026-84731 | 9.8 | 2026-10-15 | An unauthenticated remote attacker can bypass authentication and gain full access to administrative API endpoints in Nut |
| CVE-2026-102946 | 9.1 | 2026-10-15 | joserfc is a Python library that provides an implementation of several JSON Object Signing and Encryption (JOSE) standar |
| CVE-2026-104827 | 7.5 | 2026-10-15 | react/http is an event-driven, streaming HTTP client and server implementation for ReactPHP. From 1.0.0 until 1.11.1, Re |
| CVE-2026-104828 | 7.2 | 2026-10-15 | HtmlUnit Neko is an HtmlUnit adaptation of NekoHTML. Prior to 5.4.0, HTMLWriterFilter writes decoded TEXTAREA and TITLE  |
| CVE-2026-108334 | 7.4 | 2026-10-15 | A flaw was found in the internal WebAssembly (WASM) shim used by the Kuadrant operator. When generating the CEL predicat |
| CVE-2026-109383 | 7.4 | 2026-10-15 | undici is an HTTP client library for Node.js. In versions 4.0.0 through 6.29.0, 7.0.0 through 7.30.0, and 8.0.0 through  |
| CVE-2026-109829 | 7.4 | 2026-10-15 | undici is an HTTP client library for Node.js. In versions 7.0.0 through 7.30.0 and 8.0.0 through 8.12.1, when an originl |
| CVE-2026-109869 | 7.5 | 2026-10-15 | undici is an HTTP client library for Node.js. In versions 6.23.0 through 6.29.0, 7.18.0 through 7.30.0, and 8.0.0 throug |
| CVE-2026-111160 | 7.5 | 2026-10-15 | LightLLM through 1.2.0 contains a denial of service vulnerability that allows unauthenticated attackers to crash the inf |
| CVE-2026-111214 | 7.2 | 2026-10-15 | Netgate pfSense CE 2.7.0 through 2.9.0 contains an OS command injection vulnerability that allows authenticated users wi |
| CVE-2026-111215 | 7.2 | 2026-10-15 | Netgate pfSense CE through 2.9.0 contains an OS command injection vulnerability that allows authenticated users to execu |
| CVE-2026-111216 | 7.2 | 2026-10-15 | Netgate pfSense CE through 2.9.0 contains an OS command injection vulnerability that allows authenticated users with gat |
| CVE-2026-111217 | 7.2 | 2026-10-15 | Netgate pfSense CE through 2.9.0 contains an OS command injection vulnerability that allows authenticated users with Vir |
| CVE-2026-111218 | 7.2 | 2026-10-15 | Netgate pfSense CE 2.7.0 through 2.9.0 contains an OS command injection vulnerability that allows authenticated users wi |
| CVE-2026-111220 | 7.2 | 2026-10-15 | pfSense CE through 2.9.0 contains a crontab injection vulnerability in interfaces_ppps_edit.php that allows authenticate |
| CVE-2026-111223 | 7.2 | 2026-10-15 | Netgate pfSense CE 2.7.0 through 2.9.0 contains a configuration injection vulnerability that allows authenticated users  |
| CVE-2026-111224 | 7.5 | 2026-10-15 | pfSense CE through 2.9.0 contains an OS command injection vulnerability in the OpenVPN openvpn.connect_async.sh script t |
| CVE-2026-111226 | 7.2 | 2026-10-15 | pfSense CE 2.4.5 through 2.9.0 contains an OS command injection vulnerability that allows authenticated WebGUI users wit |
| CVE-2026-111229 | 7.2 | 2026-10-15 | pfSense CE 2.7.0 through 2.9.0 contains a command injection vulnerability in services_captiveportal_hasync.php that allo |
| CVE-2026-111231 | 7.2 | 2026-10-15 | Netgate pfSense CE through 2.9.0 contains an authorization bypass vulnerability that allows read-only WebGUI users to re |
| CVE-2026-111235 | 9.1 | 2026-10-15 | An authorization bypass vulnerability exists in the REST API of multiple versions of OpenNMS Meridian and Horizon. The / |
| CVE-2026-55239 | 8.8 | 2026-10-15 | Tianji is an open source analytics, uptime monitoring, and server status platform. Prior to 1.31.29, the getDateQuery()  |
| CVE-2026-55240 | 9.1 | 2026-10-15 | Tianji is an open source analytics, uptime monitoring, and server status platform. Prior to 1.31.29, formatString() in s |
| CVE-2026-55587 | 8.1 | 2026-10-15 | AliasVault is a privacy-first password manager with built-in email aliasing. Prior to 0.29.4, the AliasVault browser ext |
| CVE-2026-55872 | 8.7 | 2026-10-15 | GYM One is open-source gym management software for fitness centers, personal trainers, and sports clubs. Prior to 1.4.1, |
| CVE-2026-57496 | 9.6 | 2026-10-15 | NetLicensing MCP Server is a natural-language interface that enables agentic applications to manage the software-licensi |
| CVE-2026-87018 | 7.5 | 2026-10-15 | undici is an HTTP client library for Node.js. In versions 4.2.1 through 6.29.0, 7.0.0 through 7.30.0, and 8.0.0 through  |
| CVE-2026-97370 | 7.5 | 2026-10-15 | Junrar is an open source Java RAR archive library. Prior to 7.6.1, RarVM.ExecuteCode in src/main/java/com/github/junrar/ |
| CVE-2026-106700 | 8.8 | 2026-10-15 | ELADMIN v2.7 and earlier contains an improper access control vulnerability in the user-management endpoint PUT /api/user |
| CVE-2026-106708 | 8.8 | 2026-10-15 | XXL-JOB 3.5.0-SNAPSHOT and earlier contains a Cross-Site Request Forgery (CSRF) vulnerability in the user management con |
| CVE-2026-105032 | 9.1 | 2026-10-15 | The EnergizeLab Eilik and EilikO AI skill upload endpoint, served by the FastAPI AI inference and profiling services, do |
| CVE-2026-105033 | 8.8 | 2026-10-15 | The EnergizeLab AI Station (RK3562) firmware image ships with default root credentials and SSH enabled. An attacker with |
| CVE-2026-105034 | 8.2 | 2026-10-15 | The EnergizeLab Eilik NestJS auth service issues device tokens for arbitrary robot serial numbers without authentication |
| CVE-2026-105035 | 7.8 | 2026-10-15 | The EnergizeLab FirmwareUpdater (AArch64 ELF, distributed in the CDN bin.zip) uses a single hard-coded AES key shared by |
| CVE-2026-105036 | 7.5 | 2026-10-15 | EnergizeLab AI Station firmware, EilikO Linux robot firmware v2.1_20260617182218_release, and the EnergizeLab Windows de |
| CVE-2026-105037 | 9.9 | 2026-10-15 | EnergizeLab station-middleware (NestJS) Docker images 1.6.5 through 1.8.2 allow any registered, low-privilege account to |
| CVE-2026-105038 | 9.8 | 2026-10-15 | The EnergizeLab Eilik and EilikO FastAPI AI inference and profiling services expose AI model administration functions wi |
| CVE-2026-105039 | 9.6 | 2026-10-15 | EnergizeLab station-middleware (NestJS) Docker images 1.6.5 through 1.8.2 do not check user roles on administrative APIs |
| CVE-2026-105040 | 8.8 | 2026-10-15 | The EnergizeLab Eilik NestJS auth service accepts a user-controlled user ID in account update requests (mass assignment) |
| CVE-2026-108426 | 8.8 | 2026-10-15 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108427 | 8.8 | 2026-10-15 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108428 | 8.8 | 2026-10-15 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108429 | 8.8 | 2026-10-15 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108430 | 8.8 | 2026-10-15 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108431 | 8.8 | 2026-10-15 | Stack-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108432 | 8.8 | 2026-10-15 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108433 | 7.8 | 2026-10-15 | Reliance on untrusted inputs in a security decision in Microsoft Office Word allows an unauthorized attacker to bypass a |
| CVE-2026-108437 | 8.8 | 2026-10-15 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108439 | 8.8 | 2026-10-15 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108440 | 8.8 | 2026-10-15 | Stack-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108441 | 8.8 | 2026-10-15 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108442 | 8.8 | 2026-10-15 | Use after free in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108443 | 8.8 | 2026-10-15 | Off-by-one error in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108444 | 8.8 | 2026-10-15 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108445 | 8.8 | 2026-10-15 | Stack-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108446 | 8.8 | 2026-10-15 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108447 | 8.8 | 2026-10-15 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108448 | 7.5 | 2026-10-15 | Heap-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108449 | 8.8 | 2026-10-15 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108450 | 8.8 | 2026-10-15 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108451 | 8.8 | 2026-10-15 | Numeric truncation error in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108452 | 8.8 | 2026-10-15 | Improper limitation of a pathname to a restricted directory ('path traversal') in Microsoft Office SharePoint allows an  |
| CVE-2026-109468 | 7.5 | 2026-10-15 | Allocation of resources without limits or throttling in ASP.NET Core allows an unauthorized attacker to deny service ove |
| CVE-2026-111357 | 7.0 | 2026-10-15 | Ivanti Connect Secure 22.8R2.4 mishandles the manner in which the dsinvoked broker trusts DSCache configuration data, le |
| CVE-2026-110913 | 8.8 | 2026-10-15 | Memory corruption in DOM in Google Chrome prior to 155.0.8059.84 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-110914 | 8.8 | 2026-10-15 | Memory corruption in Workers in Google Chrome prior to 155.0.8059.84 allowed a remote attacker to potentially execute ar |
| CVE-2026-110915 | 8.8 | 2026-10-15 | Use after free in Compositing in Google Chrome prior to 155.0.8059.84 allowed a remote attacker to execute arbitrary cod |
| CVE-2026-110919 | 8.8 | 2026-10-15 | Use after free in V8 in Google Chrome prior to 155.0.8059.84 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-110920 | 8.8 | 2026-10-15 | Memory corruption in V8 in Google Chrome prior to 155.0.8059.84 allowed a remote attacker to execute arbitrary code insi |
| CVE-2026-110921 | 8.8 | 2026-10-15 | Use after free in V8 in Google Chrome prior to 155.0.8059.84 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-110922 | 8.8 | 2026-10-15 | Use after free in Prerender in Google Chrome prior to 155.0.8059.84 allowed a remote attacker to execute arbitrary code  |
| CVE-2026-111277 | 7.5 | 2026-10-15 | NivoCart through 2.5.1 contains a missing authorization vulnerability in the download() action of account/order that all |
| CVE-2026-111279 | 7.5 | 2026-10-15 | Dragonfly through 2.0.2 contains an unbounded memory allocation vulnerability that allows unauthenticated clients to exh |
| CVE-2026-111280 | 7.4 | 2026-10-15 | snap7 through 1.4.3 contains an out-of-bounds write vulnerability in TSnap7MicroClient::opReadArea() that allows malicio |
| CVE-2026-111281 | 9.8 | 2026-10-15 | Jooan JA-A12 IP cameras with firmware 009_20171107 and 05.02.31.105 contain a remote code execution vulnerability that a |
| CVE-2026-111282 | 8.2 | 2026-10-15 | Driftregion iso14229 before 0.10.1 contains an integer wraparound in Handle_0x38_RequestFileTransfer that lets unauthent |
| CVE-2026-111283 | 9.0 | 2026-10-15 | BMC Helix Network Management on-prem before 26.3.01 contains an authentication bypass vulnerability that allows unauthen |
| CVE-2026-111312 | 7.7 | 2026-10-15 | OpenHealth through 0.2.0 contains a missing authentication and authorization vulnerability in the /api/health-data/[id]  |
| CVE-2026-111322 | 9.8 | 2026-10-15 | Archon 0.2.13 through 0.11.1 contains a missing authentication vulnerability that allows unauthenticated attackers to ac |
| CVE-2026-111329 | 9.8 | 2026-10-15 | JuggleIM im-server through 1.8.16 ships default administrator credentials admin/123456 that allow unauthenticated remote |
| CVE-2026-111352 | 8.8 | 2026-10-15 | ThinkCMF through 8.0.1 contains an incorrect authorization vulnerability in RestAdminBaseController that allows restrict |
| CVE-2026-111356 | 7.4 | 2026-10-15 | MacCMS v10 through 2026.1000.4056 does not limit attempts on the six-digit password recovery code, allowing unauthentica |
| CVE-2026-111359 | 7.1 | 2026-10-15 | CRMEB 5.6.1 through 6.0.0 contains an insecure direct object reference vulnerability that allows authenticated storefron |
| CVE-2026-111366 | 7.2 | 2026-10-15 | cool-admin-midway through 8.0.0 contains an authorization bypass vulnerability that allows department-limited admins to  |
| CVE-2026-111369 | 7.1 | 2026-10-15 | ClassroomIO through 1.0.0 contains an incorrect authorization vulnerability in the PUT and DELETE /:lessonId lesson rout |
| CVE-2026-111210 | 7.3 | 2026-10-16 | A vulnerability was determined in bitcoinj up to 0.17. Affected is the function url.openConnection of the file PaymentSe |
| CVE-2026-75941 | 8.0 | 2026-10-16 | A potential vulnerability was reported in the Lenovo Legion Zone application, distributed exclusively in the Chinese mar |
| CVE-2026-84823 | 7.1 | 2026-10-16 | A flaw was found in WildFly. A user with the `Monitor` role, which is the lowest standard Role-Based Access Control (RBA |
| CVE-2026-92629 | 7.3 | 2026-10-16 | A potential improper authorization vulnerability was reported in Lenovo Baiying PC Client, distributed exclusively in th |
| CVE-2026-111378 | 7.5 | 2026-10-16 | FreeRDP from 3.0.0 before 3.32.0 contains an uncontrolled resource consumption vulnerability in parse_nla_mode_pdu that  |
| CVE-2026-111379 | 7.3 | 2026-10-16 | FreeRDP before 3.32.0 contains a heap buffer overflow vulnerability in persistent_cache_read_entry_v3 that allows local  |
| CVE-2026-111380 | 8.8 | 2026-10-16 | FreeRDP from 3.29.0 before 3.32.0 contains an integer overflow in the Apple audin backends (audin_mac.m, audin_ios.m), w |
| CVE-2026-111381 | 7.3 | 2026-10-16 | FreeRDP before 3.32.0 contains a heap buffer overflow vulnerability in persistent_cache_read_entry_v2 that allows local  |
| CVE-2026-111382 | 8.8 | 2026-10-16 | FreeRDP before 3.32.0 contains a client-side heap out-of-bounds write vulnerability in general_LumaToYUV444 and general_ |
| CVE-2026-111389 | 7.7 | 2026-10-16 | Frappe HRMS 14.x before 14.38.2, 15.x before 15.64.0, and 16.x before 16.18.0 contains a SQL injection vulnerability in  |
| CVE-2026-104745 | 8.1 | 2026-10-16 | The Customer Email Verification for WooCommerce plugin for WordPress is vulnerable to Privilege Escalation via the `alg_ |
| CVE-2026-107758 | 7.2 | 2026-10-16 | The Colibri Page Builder plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'comment' parameter i |
| CVE-2026-109207 | 7.2 | 2026-10-16 | The RSS Aggregator by Feedzy – Feed to Post, Autoblogging, News & YouTube Video Feeds Aggregator plugin for WordPress is |
| CVE-2026-109990 | 7.2 | 2026-10-16 | The Flying Scripts: Delay JavaScript to Improve Site Speed & Performance plugin for WordPress is vulnerable to Stored Cr |
| CVE-2026-111444 | 9.8 | 2026-10-16 | Wheels through 4.1.2 allows SQL injection on MySQL/MariaDB with backslash escaping enabled (NO_BACKSLASH_ESCAPES absent) |
| CVE-2026-111445 | 8.1 | 2026-10-16 | Wheels 4.0.0 through 4.1.2 before 4.2.0 replaces incoming scope conditions with a primary-key condition in findByKey() a |
| CVE-2026-111446 | 8.6 | 2026-10-16 | Wheels 4.0.0 through 4.1.2 exposes password-less development tools under /wheels/* to remote clients when enablePublicCo |
| CVE-2026-111447 | 8.1 | 2026-10-16 | Wheels 1.1 through 4.1.2 resolves nestedProperties() records by posted primary key without checking that they belong to  |
| CVE-2026-111451 | 7.8 | 2026-10-16 | Wheels CLI 4.0.0 through 4.1.1 insufficiently validates or escapes caller-supplied values and package contents. Deploy r |
| CVE-2026-93953 | 8.0 | 2026-10-16 | The Backuply – Backup, Restore, Migrate and Clone plugin for WordPress is vulnerable to SQL Injection via the Biographic |
| CVE-2026-97339 | 7.2 | 2026-10-16 | The Complianz GDPR/CCPA Cookie Consent Banner plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Comm |
| CVE-2026-103525 | 7.5 | 2026-10-16 | The FluentCart A New Era of eCommerce – Faster, Lighter, and Simpler plugin for WordPress is vulnerable to Insecure Dire |
| CVE-2026-103895 | 8.1 | 2026-10-16 | The miniOrange OTP Login, Verification and SMS Notifications plugin for WordPress is vulnerable to Authentication Bypass |
| CVE-2026-104798 | 9.8 | 2026-10-16 | The My Calendar – Accessible Event Manager plugin for WordPress is vulnerable to Privilege Escalation in all versions up |
| CVE-2026-107659 | 7.5 | 2026-10-16 | The Modula Image Gallery – Photo Grid & Video Gallery plugin for WordPress is vulnerable to Sensitive Information Exposu |
| CVE-2026-107746 | 7.5 | 2026-10-16 | The FunnelKit – Funnel Builder for WooCommerce Checkout plugin for WordPress is vulnerable to authorization bypass in al |
| CVE-2026-109219 | 9.8 | 2026-10-16 | The Mang Board plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 2.4.4 v |
| CVE-2026-109221 | 8.1 | 2026-10-16 | The Groundhogg — CRM, Newsletters, and Marketing Automation plugin for WordPress is vulnerable to arbitrary file deletio |
| CVE-2026-109400 | 7.5 | 2026-10-16 | The InstaWP Connect – 1-click WP Staging & Migration plugin for WordPress is vulnerable to Privilege Escalation in all v |
| CVE-2026-109515 | 9.8 | 2026-10-16 | The MailOptin – Popup, Optin Forms & Email Newsletters for Mailchimp, HubSpot, AWeber Etc. plugin for WordPress is vulne |
| CVE-2026-109998 | 7.2 | 2026-10-16 | The Mang Board plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'content' parameter in all vers |
| CVE-2026-110590 | 7.5 | 2026-10-16 | The Klarna for WooCommerce plugin for WordPress is vulnerable to authorization bypass in all versions up to, and includi |
| CVE-2026-111114 | 7.5 | 2026-10-16 | The Nexter Extension – Security, Performance, Code Snippets & Site Toolkit plugin for WordPress is vulnerable to Privile |
| CVE-2026-100186 | 7.2 | 2026-10-16 | The User Profile Builder – Beautiful User Registration Forms, User Profiles & User Role Editor plugin for WordPress is v |
| CVE-2026-103768 | 9.8 | 2026-10-16 | The ELEX WordPress HelpDesk & Customer Ticketing System plugin for WordPress is vulnerable to Arbitrary File Upload in a |
| CVE-2026-103896 | 7.5 | 2026-10-16 | The 10Web Booster – Website speed optimization, Cache & Page Speed optimizer plugin for WordPress is vulnerable to a lim |
| CVE-2026-103999 | 7.2 | 2026-10-16 | The Ultra Addons for Contact Form 7 plugin for WordPress is vulnerable to Stored Cross-Site Scripting via File Upload in |
| CVE-2026-104000 | 7.2 | 2026-10-16 | The Simply Schedule Appointments plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'status' para |
| CVE-2026-104932 | 8.0 | 2026-10-16 | The Search Regex plugin for WordPress is vulnerable to PHP Object Injection in version 3.5 via deserialization of untrus |
| CVE-2026-107764 | 7.2 | 2026-10-16 | The SiteOrigin CSS plugin for WordPress is vulnerable to Stored DOM-Based Cross-Site Scripting via the 'url (comment_aut |
| CVE-2026-109232 | 7.2 | 2026-10-16 | The Salon Booking System – Appointment Booking for Salons, Barbershops & Spas plugin for WordPress is vulnerable to Stor |
| CVE-2026-109447 | 8.1 | 2026-10-16 | The User Profile Builder – Beautiful User Registration Forms, User Profiles & User Role Editor plugin for WordPress is v |
| CVE-2026-109513 | 7.2 | 2026-10-16 | The NotificationX – FOMO, Live Sales Notification, WooCommerce Sales Popup, GDPR, Social Proof, Announcement Banner & Fl |
| CVE-2026-111122 | 7.2 | 2026-10-16 | The SiteOrigin CSS plugin for WordPress is vulnerable to Stored DOM-Based Cross-Site Scripting via the 'href' parameter  |
| CVE-2026-85659 | 8.8 | 2026-10-16 | The PilotPress plugin for WordPress is vulnerable to Privilege Escalation via Account Takeover in all versions up to, an |
| CVE-2026-89051 | 7.2 | 2026-10-16 | The WP Ghost (Hide My WP Ghost) – Security & Firewall plugin for WordPress is vulnerable to Stored Cross-Site Scripting  |
| CVE-2026-89079 | 9.8 | 2026-10-16 | The Theme My Login plugin for WordPress is vulnerable to privilege escalation via account takeover in versions up to, an |
| CVE-2026-95686 | 7.2 | 2026-10-16 | The Opti-Behavior – Self-Hosted Heatmaps, Session Recordings, Funnels, A/B Testing & Smart Insights plugin for WordPress |
| CVE-2026-95809 | 7.2 | 2026-10-16 | The Opti-Behavior – Self-Hosted Heatmaps, Session Recordings, Funnels, A/B Testing & Smart Insights plugin for WordPress |
| CVE-2026-96570 | 7.2 | 2026-10-16 | The Schema & Structured Data for WP & AMP plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'sas |
| CVE-2026-104715 | 7.8 | 2026-10-16 | A flaw was found in cifs-utils. This flaw allows an unprivileged local user to achieve privilege escalation. When a priv |
| CVE-2026-104730 | 9.8 | 2026-10-16 | The Sunshine Photo Cart – Client Photo Gallery & Photo Proofing for Photographers plugin for WordPress is vulnerable to  |
| CVE-2026-107768 | 7.2 | 2026-10-16 | The TranslatePress – Translate Multilingual sites with AI Translation plugin for WordPress is vulnerable to Stored Cross |
| CVE-2026-109193 | 7.2 | 2026-10-16 | The HivePress – Business Directory, Listings & Classified Ads Plugin plugin for WordPress is vulnerable to Stored Cross- |
| CVE-2026-110701 | 7.2 | 2026-10-16 | The CP Multi View Events Calendar plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'CalendarTit |
| CVE-2026-92115 | 8.8 | 2026-10-16 | The WP Photo Album Plus plugin for WordPress is vulnerable to authenticated Command Injection in all versions up to, and |
| CVE-2026-92553 | 8.8 | 2026-10-16 | The YaySMTP – WP Mail SMTP with Email Logs, Tracking & Reports plugin for WordPress is vulnerable to Arbitrary File Uplo |
| CVE-2026-94169 | 10.0 | 2026-10-16 | Improper Control of Generation of Code ('Code Injection') vulnerability in Theme-one The Grid the-grid allows Command In |
| CVE-2026-94388 | 9.3 | 2026-10-16 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in halfdata Green Pop |
| CVE-2026-96339 | 7.1 | 2026-10-16 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Houzez.co Houzez h |
| CVE-2026-97296 | 8.1 | 2026-10-16 | Deserialization of Untrusted Data vulnerability in Rocketgenius, Inc Gravity Forms gravityforms allows Object Injection. |
| CVE-2026-97640 | 7.2 | 2026-10-16 | The WPConsent – Cookie Banner & Cookie Consent for Privacy Compliance (GDPR / CCPA / EU Compliance Cookie Notice) plugin |
| CVE-2026-16453 | 7.1 | 2026-10-16 | Mattermost versions 11.10.x <= 11.10.0, 11.7.x <= 11.7.9, 11.9.x <= 11.9.1, 11.8.x <= 11.8.5 fail to verify the integrit |
| CVE-2026-75903 | 8.1 | 2026-10-16 | The Vulnity Security plugin for WordPress is vulnerable to authentication bypass in all versions up to, and including, 1 |
| CVE-2026-87111 | 7.2 | 2026-10-16 | The User Registration PRO – Custom Registration Form, Login Form, and User Profile WordPress Plugin plugin for WordPress |
| CVE-2026-109224 | 7.2 | 2026-10-16 | The SureCart – Ecommerce Made Easy For Selling Physical Products, Digital Downloads, Subscriptions, Donations, & Payment |
| CVE-2026-111311 | 8.8 | 2026-10-16 | The DoubleScale \| All-in-One CRM – Sales, Multi-Channel Marketing, Newsletter, Booking, Helpdesk, Automation, MCP & More |
| CVE-2026-14177 | 7.5 | 2026-10-16 | Observable response discrepancy vulnerability in IKAS Technology Inc. Ikas E-Commerce Infrastructure allows Account Foot |
| CVE-2026-92766 | 7.5 | 2026-10-16 | The Vitepos – Point of Sale (POS) for WooCommerce plugin for WordPress is vulnerable to generic SQL Injection via the 's |
| CVE-2026-96768 | 7.2 | 2026-10-16 | The GoSMTP Pro plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Comment Content via Email Log Body  |
| CVE-2026-109119 | 8.8 | 2026-10-16 | Improper Privilege Management in the user management API endpoint (/api/users/{username_or_id}) in Rdiffweb allows authe |
| CVE-2026-105959 | 7.5 | 2026-10-16 | A flaw was found in spice-server. The GLZ encoder dictionary restore path truncates a size_t allocation size to int when |
| CVE-2026-107648 | 7.2 | 2026-10-16 | The WP Sessions Time Monitoring Full Automatic plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the |
| CVE-2026-111391 | 8.1 | 2026-10-16 | SGLang 0.5.10 through 0.5.22 contains a code injection vulnerability in _evaluate_filter() that allows remote attackers  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-21589 | Atlassian / Multiple Products | 2026-10-15 | 2026-10-18 | Unknown |
| CVE-2026-105134 | Ahsay / AhsayCBS | 2026-10-14 | 2026-10-17 | Unknown |
| CVE-2026-76519 | Cisco / Secure Email Gateway | 2026-10-14 | 2026-10-17 | Unknown |
| CVE-2026-105133 | Ahsay / AhsayCBS | 2026-10-14 | 2026-10-17 | Unknown |
| CVE-2026-0322 | Palo Alto Networks / PAN-OS | 2026-10-14 | 2026-10-17 | Unknown |
| CVE-2026-104935 | Ivanti / Connect Secure | 2026-10-13 | 2026-10-16 | Unknown |
| CVE-2026-96951 | Microsoft / Windows | 2026-10-13 | 2026-10-16 | Unknown |

---

*Total entries in CISA KEV catalog: 1746*