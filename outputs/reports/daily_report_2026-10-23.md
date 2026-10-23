# Vulnerability Intelligence Report

**Date:** 2026-10-23  
**Generated:** 2026-10-23T13:04:56Z  

---

## Executive Summary

Our environment currently faces 161 high-severity vulnerabilities across critical components including authentication libraries, log processing, Node.js middleware, DNS toolkits, and XML parsers. The most critical finding is CVE-2026-114607 (CVSS 9.1), a Better Auth authentication bypass enabling unauthorized account access. Eight new entries were added to the CISA Known Exploited Vulnerabilities catalog this week, primarily targeting Plex Media Server and SiteGuard, signaling active exploitation in the wild. While no monitored CVEs currently overlap with the KEV catalog, the volume and severity of open vulnerabilities represent significant organizational risk requiring immediate prioritization and remediation.

---

## Risk Narrative

The current threat landscape reflects a broad attack surface spanning web middleware, authentication systems, DNS infrastructure, and legacy XML processing components. The CISA KEV additions indicate threat actors are actively exploiting media server and endpoint management software, heightening the urgency for rapid response. CVE-2026-114607's near-perfect CVSS score poses direct risk to customer identity and access controls, potentially enabling account takeover at scale. Unpatched Node.js middleware and log processing vulnerabilities expose backend services to denial-of-service and privilege escalation. Collectively, these vulnerabilities create pathways for data exfiltration, service disruption, and unauthorized access that could result in regulatory penalties, reputational damage, and significant operational downtime if left unaddressed.

---

## Prioritized Action Items

1. Immediately patch or disable Better Auth Magic Link functionality to remediate CVE-2026-114607 (CVSS 9.1), which allows full authentication bypass.
2. Audit all Plex Media Server and SiteGuard deployments and apply available patches or isolate systems, as four Plex CVEs and one SiteGuard CVE are now actively exploited per CISA KEV.
3. Update rsyslog to a version above 8.2610.0 to close the dynaFile privilege escalation vulnerability (CVE-2026-92709, CVSS 8.1) on all log processing infrastructure.
4. Upgrade Node.js middleware packages body-parser and multer to their patched versions to prevent denial-of-service and file upload exploitation across web applications.
5. Conduct a full inventory review of Apache Abdera and dnspython deployments and apply patches or implement compensating controls to address XML injection and DNS pointer chain vulnerabilities.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-113582 | 7.5 | 2026-10-22 | UNSUPPORTED WHEN ASSIGNED Improper restriction of XML external entity references in Apache Abdera allows an attacker to  |
| CVE-2026-92709 | 8.1 | 2026-10-22 | Rsyslog is a rocket-fast system for log processing. From versions 1.15.0 to 8.2610.0, rsyslog's omfile dynaFile facility |
| CVE-2026-111181 | 7.5 | 2026-10-22 | body-parser is body parsing middleware for Node.js and Express. In versions before 1.20.9 and in versions from 2.0.0 bef |
| CVE-2026-113872 | 7.5 | 2026-10-22 | multer is a middleware for Node.js that handles multipart/form-data file uploads. In versions from 2.0.0 before 2.5.0, w |
| CVE-2026-114510 | 7.1 | 2026-10-22 | Flexible GraphRAG is a Python framework for building graph and retrieval-augmented generation applications across multip |
| CVE-2026-61791 | 7.4 | 2026-10-22 | OCO-Server is a self-hosted endpoint management application for computer inventory, software deployment, and mobile devi |
| CVE-2026-115482 | 7.5 | 2026-10-22 | In lsquic before 4.9.0, the HTTP/3 implementation can use an excessive amount of memory because the number of buffered h |
| CVE-2026-104068 | 7.2 | 2026-10-22 | JetBackup plugin for WordPress before 3.1.24.10 contains a symlink-based arbitrary file write vulnerability that allows  |
| CVE-2026-114605 | 7.5 | 2026-10-22 | dnspython is a DNS toolkit for Python. Prior to 2.9.0, dns.name.from_wire_parser follows attacker-controlled DNS compres |
| CVE-2026-114607 | 9.1 | 2026-10-22 | Better Auth is an authentication and authorization library for TypeScript. From 1.4.0-beta.18 until 1.7.7, deployments t |
| CVE-2026-115416 | 7.7 | 2026-10-22 | Incorrect authorization checks in Amazon Athena engine version 3 query processing could have allowed an authenticated us |
| CVE-2026-115513 | 8.7 | 2026-10-22 | OpenCATS before 0.12.0 contains a stored cross-site scripting vulnerability that allows a low-privileged authenticated u |
| CVE-2026-75507 | 7.5 | 2026-10-22 | GraphQL-core is a Python port of the GraphQL.js reference implementation. From 3.0.0 until 3.2.12 and 3.3.0rc1, the Over |
| CVE-2026-75508 | 7.5 | 2026-10-22 | GraphQL-core is a Python port of the GraphQL.js reference implementation. From 3.2.3 until 3.2.12 and 3.3.0rc1, the pars |
| CVE-2026-113873 | 7.5 | 2026-10-22 | SmileCDR HAPI FHIR does not properly handle highly compressed data, allowing an unauthenticated attacker to send compres |
| CVE-2026-113874 | 8.1 | 2026-10-22 | SmileCDR HAPI FHIR allows an untrusted bundle body to replace a partition identity previously established by a trusted s |
| CVE-2026-114611 | 9.1 | 2026-10-22 | OCO-Server is a self-hosted endpoint management application for computer inventory, software deployment, and mobile devi |
| CVE-2026-13599 | 7.8 | 2026-10-22 | Missing authentication for critical function vulnerability in ABB Ability Edgenius.

This issue affects Ability Edgenius |
| CVE-2026-97635 | 8.1 | 2026-10-22 | The Agent Zero Web UI before 1.15 does not correctly sanitize user-provided input in chat messages or file uploads. When |
| CVE-2022-51026 | 9.8 | 2026-10-22 | Bytebase 0.12.0 before 1.0.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to lo |
| CVE-2026-114612 | 9.9 | 2026-10-22 | LiteLLM is a proxy server (AI Gateway) to call LLM APIs in OpenAI (or native) format. From 1.87.0 until 1.100.4, 1.101.3 |
| CVE-2026-114613 | 7.5 | 2026-10-22 | MessagePack is the serializer implementation for Python msgpack.org. Prior to 1.2.3, the msgpack-python C extension (msg |
| CVE-2026-114648 | 7.6 | 2026-10-22 | The MongoDB C# Driver does not neutralize dot and dollar characters in dictionary keys, field names and array-filter ide |
| CVE-2026-115347 | 7.5 | 2026-10-22 | Mistune before 3.3.0 contains an inefficient algorithmic complexity vulnerability in parse_link_text that allows remote  |
| CVE-2026-115348 | 7.5 | 2026-10-22 | Mistune from 3.0.0 before 3.3.0 contains an algorithmic complexity vulnerability in the inline link parser's parse_link_ |
| CVE-2026-115349 | 7.5 | 2026-10-22 | Mistune from 3.0.0 before 3.3.0 contains an algorithmic complexity denial of service vulnerability in the parse_link_tex |
| CVE-2026-115352 | 7.5 | 2026-10-22 | Mistune before 3.3.0 contains an algorithmic complexity vulnerability in the inline link parser that allows unauthentica |
| CVE-2026-115353 | 8.6 | 2026-10-22 | Mistune before 3.3.0 contains a path traversal vulnerability in the RST include directive that allows attackers to read  |
| CVE-2026-115355 | 7.5 | 2026-10-22 | Mistune before 3.3.0 contains a path traversal vulnerability in the Include directive that allows attackers to read arbi |
| CVE-2026-115371 | 7.1 | 2026-10-22 | Incus 6.0.3 before 6.0.7, 6.6.0 before 7.0.2, and 7.1.0 before 7.5.0 contains an improper authorization vulnerability th |
| CVE-2026-115372 | 8.5 | 2026-10-22 | Incus from 7.3.0 before 7.5.0 contains a project restriction bypass that allows restricted project users to set block.cr |
| CVE-2026-115374 | 7.1 | 2026-10-22 | Incus 7.0.0 before 7.0.2 and 7.1.0 before 7.5.0 contains a signature verification flaw in its built-in S3 server that al |
| CVE-2026-115375 | 9.9 | 2026-10-22 | Incus 7.0.0 before 7.0.2 and 7.1.0 before 7.5.0 contains a path traversal vulnerability that allows clients able to crea |
| CVE-2026-115376 | 7.7 | 2026-10-22 | Incus 7.0.1 before 7.0.2 and 7.2.0 before 7.5.0 contains an authorization bypass vulnerability that allows project-restr |
| CVE-2026-115377 | 9.9 | 2026-10-22 | Incus before 6.0.7, 6.1.0 before 7.0.2, and 7.1.0 before 7.5.0 contains an arbitrary file write vulnerability that allow |
| CVE-2026-115384 | 9.9 | 2026-10-22 | Wasmtime 39.0.0 before 48.0.4 and 49.0.0 before 49.0.2 contains a stack buffer overflow vulnerability that allows malici |
| CVE-2026-115392 | 7.9 | 2026-10-22 | Wasmtime before 24.0.13, 25.0.0 before 36.0.14, 37.0.0 before 46.0.3, and 47.0.0 before 47.0.4 allows a filesystem sandb |
| CVE-2026-115414 | 7.8 | 2026-10-22 | OS command injection in the Terraform hook in AWS SAM CLI before 1.166.2 might allow an actor who can influence the Terr |
| CVE-2026-79844 | 10.0 | 2026-10-22 | No description provided |
| CVE-2026-79846 | 10.0 | 2026-10-22 | No description provided |
| CVE-2026-79847 | 10.0 | 2026-10-22 | No description provided |
| CVE-2026-79848 | 10.0 | 2026-10-22 | No description provided |
| CVE-2026-79849 | 10.0 | 2026-10-22 | No description provided |
| CVE-2026-79850 | 10.0 | 2026-10-22 | No description provided |
| CVE-2026-79851 | 10.0 | 2026-10-22 | No description provided |
| CVE-2026-79852 | 9.8 | 2026-10-22 | No description provided |
| CVE-2026-79853 | 9.8 | 2026-10-22 | No description provided |
| CVE-2026-79854 | 9.8 | 2026-10-22 | No description provided |
| CVE-2026-79855 | 9.8 | 2026-10-22 | No description provided |
| CVE-2026-79856 | 9.8 | 2026-10-22 | No description provided |
| CVE-2026-79857 | 9.8 | 2026-10-22 | No description provided |
| CVE-2026-79858 | 9.8 | 2026-10-22 | No description provided |
| CVE-2026-79859 | 9.8 | 2026-10-22 | No description provided |
| CVE-2026-79860 | 9.8 | 2026-10-22 | No description provided |
| CVE-2026-79861 | 9.8 | 2026-10-22 | No description provided |
| CVE-2026-79862 | 9.6 | 2026-10-22 | No description provided |
| CVE-2026-79863 | 9.6 | 2026-10-22 | No description provided |
| CVE-2026-79864 | 9.6 | 2026-10-22 | No description provided |
| CVE-2026-79865 | 9.6 | 2026-10-22 | No description provided |
| CVE-2026-79866 | 9.6 | 2026-10-22 | No description provided |
| CVE-2026-79867 | 9.6 | 2026-10-22 | No description provided |
| CVE-2026-79868 | 9.6 | 2026-10-22 | No description provided |
| CVE-2026-79869 | 9.6 | 2026-10-22 | No description provided |
| CVE-2026-79870 | 9.6 | 2026-10-22 | No description provided |
| CVE-2026-79871 | 9.6 | 2026-10-22 | No description provided |
| CVE-2026-79872 | 9.4 | 2026-10-22 | No description provided |
| CVE-2026-79873 | 9.3 | 2026-10-22 | No description provided |
| CVE-2026-79874 | 9.3 | 2026-10-22 | No description provided |
| CVE-2026-79875 | 9.3 | 2026-10-22 | No description provided |
| CVE-2026-79876 | 9.3 | 2026-10-22 | No description provided |
| CVE-2026-79877 | 8.8 | 2026-10-22 | No description provided |
| CVE-2026-79878 | 8.8 | 2026-10-22 | No description provided |
| CVE-2026-79879 | 8.8 | 2026-10-22 | No description provided |
| CVE-2026-79880 | 8.7 | 2026-10-22 | No description provided |
| CVE-2026-79881 | 8.3 | 2026-10-22 | No description provided |
| CVE-2026-79882 | 8.3 | 2026-10-22 | No description provided |
| CVE-2026-79883 | 8.3 | 2026-10-22 | No description provided |
| CVE-2026-79884 | 8.2 | 2026-10-22 | No description provided |
| CVE-2026-79885 | 8.2 | 2026-10-22 | No description provided |
| CVE-2026-79886 | 8.2 | 2026-10-22 | No description provided |
| CVE-2026-79887 | 8.1 | 2026-10-22 | No description provided |
| CVE-2026-79888 | 8.1 | 2026-10-22 | No description provided |
| CVE-2026-79889 | 8.1 | 2026-10-22 | No description provided |
| CVE-2026-79890 | 8.1 | 2026-10-22 | No description provided |
| CVE-2026-79891 | 8.1 | 2026-10-22 | No description provided |
| CVE-2026-79892 | 7.8 | 2026-10-22 | No description provided |
| CVE-2026-79893 | 7.5 | 2026-10-22 | No description provided |
| CVE-2026-79894 | 7.5 | 2026-10-22 | No description provided |
| CVE-2026-79895 | 7.5 | 2026-10-22 | No description provided |
| CVE-2026-79955 | 7.5 | 2026-10-22 | No description provided |
| CVE-2026-79956 | 7.2 | 2026-10-22 | No description provided |
| CVE-2026-95704 | 7.2 | 2026-10-22 | No description provided |
| CVE-2026-95705 | 7.2 | 2026-10-22 | No description provided |
| CVE-2026-95706 | 7.2 | 2026-10-22 | No description provided |
| CVE-2026-95707 | 7.2 | 2026-10-22 | No description provided |
| CVE-2026-95708 | 7.2 | 2026-10-22 | No description provided |
| CVE-2026-95709 | 7.2 | 2026-10-22 | No description provided |
| CVE-2026-95710 | 7.1 | 2026-10-22 | No description provided |
| CVE-2026-95711 | 7.1 | 2026-10-22 | No description provided |
| CVE-2026-95712 | 7.1 | 2026-10-22 | No description provided |
| CVE-2026-95713 | 7.0 | 2026-10-22 | No description provided |
| CVE-2026-112330 | 7.5 | 2026-10-22 | Motor.NET before 0.19.0 contains a denial of service vulnerability that allows a remote attacker who can publish to a co |
| CVE-2026-112331 | 7.5 | 2026-10-22 | Motor.NET before 0.19.0 contains a denial-of-service vulnerability that allows a remote attacker who can produce records |
| CVE-2026-112332 | 7.5 | 2026-10-22 | Motor.NET before 0.19.0 contains an uncaught exception vulnerability in JsonNetDeserializer.Deserialize that allows a re |
| CVE-2026-115504 | 7.8 | 2026-10-22 | CFITSIO through 4.7.0 contains an out-of-bounds write vulnerability in ffgcls2() in getcols.c that trusts attacker-contr |
| CVE-2026-115505 | 7.6 | 2026-10-22 | libsmb2 before 6.3 contains integer overflow vulnerabilities in the DCE/RPC NDR decoder in lib/dcerpc.c that allow heap  |
| CVE-2026-115506 | 7.5 | 2026-10-22 | libexpat through 2.9.0 contains a denial of service vulnerability because billion laughs protection in accountingDiffTol |
| CVE-2026-114625 | 9.9 | 2026-10-22 | VeloCloud Orchestrator (VCO) on-prem has a security issue where this issue may allow a remote attacker to access privile |
| CVE-2026-115417 | 7.5 | 2026-10-22 | Memory allocation with excessive size value in the MQTT 3.1.1 compatibility adapter in AWS aws-c-mqtt before 0.16.2 migh |
| CVE-2026-115419 | 8.1 | 2026-10-22 | The A2A server component in Amazon Strands Agents SDK for Python before 1.43.0 and Amazon Strands Agents SDK for TypeScr |
| CVE-2026-105014 | 9.1 | 2026-10-22 | Improper neutralization of special elements used in a command ('command injection') in Azure Pipelines allows an unautho |
| CVE-2026-108456 | 7.7 | 2026-10-22 | Server-side request forgery (ssrf) in Azure AI Foundry allows an authorized attacker to elevate privileges over a networ |
| CVE-2026-109122 | 9.1 | 2026-10-22 | The network management service on affected Kiloview E3 NDI encoder firmware fails to sanitize one field used when config |
| CVE-2026-110063 | 10.0 | 2026-10-22 | Improper link resolution before file access ('link following') in VM Inspector for Azure Virtual Machines allows an unau |
| CVE-2026-111594 | 8.1 | 2026-10-22 | InterSystems IRIS for Health has TLS/SSL encryption turned off by default, which may enable an attacker to view transmit |
| CVE-2026-114615 | 7.4 | 2026-10-22 | Authlib is a Python library which builds OAuth and OpenID Connect servers. From 1.3.1 until 1.9.0, OctKey.import_key() c |
| CVE-2026-114616 | 7.4 | 2026-10-22 | Authlib is a Python library which builds OAuth and OpenID Connect servers. Prior to 1.9.1, Authlib's OctKey.import_key() |
| CVE-2026-83938 | 10.0 | 2026-10-22 | Missing authentication for critical function in Azure Kubernetes Configuration Service allows an unauthorized attacker t |
| CVE-2026-96185 | 7.5 | 2026-10-22 | Stack-based buffer overflow in Microsoft Exchange Online allows an authorized attacker to execute code over a network. |
| CVE-2026-97785 | 10.0 | 2026-10-22 | Improper authentication in AAD App Proxy allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-107861 | 9.9 | 2026-10-22 | The system control service on affected Kiloview E3 NDI encoder firmware fails to sanitize the hostname parameter accepte |
| CVE-2026-110243 | 9.9 | 2026-10-22 | The network management service on affected Kiloview E3 NDI encoder firmware fails to validate the network interface name |
| CVE-2026-110491 | 7.5 | 2026-10-22 | The ONVIF service on the E3 can be rendered unresponsive by sending malformed or incomplete requests to certain operatio |
| CVE-2026-110825 | 7.5 | 2026-10-22 | The ONVIF device service on affected Kiloview E3 NDI encoder firmware accepts hostname, DNS, and NTP configuration write |
| CVE-2026-92450 | 7.5 | 2026-10-22 | The authentication framework used by affected Kiloview E3 NDI encoder firmware signs session JSON Web Tokens using an HM |
| CVE-2026-115484 | 7.6 | 2026-10-23 | A flaw was found in the iscsiuio component of open-iscsi. The DHCPv4 option parser incorrectly calculates the length of  |
| CVE-2026-115486 | 7.1 | 2026-10-23 | A flaw was found in the iscsiuio component of open-iscsi. The IPv6 Neighbor Discovery handler accesses link-layer addres |
| CVE-2026-115546 | 8.1 | 2026-10-23 | Okta Access Gateway (OAG) does not validate the selected authentication source during sign-on. An authenticated user wit |
| CVE-2026-115547 | 9.1 | 2026-10-23 | An input validation issue in the Okta Access Gateway (OAG) Admin Console allows the processing of specially formatted co |
| CVE-2026-54630 | 9.6 | 2026-10-23 | Part-DB is an open source inventory management system for electronic components. Prior to version 2.12.1, the part attac |
| CVE-2026-109198 | 7.2 | 2026-10-23 | The Anti-Spam by CleanTalk – Spam Protection Without CAPTCHA plugin for WordPress is vulnerable to Stored Cross-Site Scr |
| CVE-2026-115497 | 7.5 | 2026-10-23 | The Music Store – WordPress eCommerce plugin for WordPress is vulnerable to Directory Traversal in all versions up to, a |
| CVE-2026-109936 | 7.5 | 2026-10-23 | The Otter Blocks  WordPress plugin before 3.2.8 does not correctly bound a pattern it uses to rewrite its dynamic-conten |
| CVE-2026-111982 | 7.2 | 2026-10-23 | The User Profile Builder  WordPress plugin before 4.0.5 does not verify that a user is authorized to edit the specific a |
| CVE-2026-113499 | 7.5 | 2026-10-23 | The LiteSpeed Cache WordPress plugin before 7.9.2 does not restrict one of its HTML rewriting routines to stylesheet con |
| CVE-2026-113500 | 7.5 | 2026-10-23 | The LiteSpeed Cache WordPress plugin before 7.9.2 does not limit one of its HTML optimization routines to stylesheet con |
| CVE-2026-94262 | 8.1 | 2026-10-23 | The Advanced Custom Fields: Extended WordPress plugin before 0.9.2.8, Advanced Custom Fields: Extended PRO WordPress plu |
| CVE-2026-94267 | 9.0 | 2026-10-23 | The Advanced Custom Fields: Extended WordPress plugin before 0.9.2.8, Advanced Custom Fields: Extended PRO WordPress plu |
| CVE-2026-94268 | 8.1 | 2026-10-23 | The Advanced Custom Fields: Extended WordPress plugin before 0.9.2.8, Advanced Custom Fields: Extended PRO WordPress plu |
| CVE-2026-55981 | 9.6 | 2026-10-23 | A firmware verification vulnerability in Creative Sound
Blaster Katana could allow an attacker to modify a legitimate fi |
| CVE-2026-63244 | 9.8 | 2026-10-23 | An authentication
bypass vulnerability in WizLearn Technologies' Learning Management System (LMS)
could allow an unauthe |
| CVE-2026-112359 | 7.5 | 2026-10-23 | Missing Authorization vulnerability in Amauri.IO WPMobile.App wpappninja allows Exploiting Incorrectly Configured Access |
| CVE-2026-112835 | 7.1 | 2026-10-23 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in e4jvikwp VikRentCa |
| CVE-2026-112837 | 8.5 | 2026-10-23 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Ruben Garcia GamiP |
| CVE-2026-112838 | 7.1 | 2026-10-23 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in e4jvikwp VikRentCa |
| CVE-2026-112860 | 9.3 | 2026-10-23 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in xnau webdesign Par |
| CVE-2026-112862 | 9.8 | 2026-10-23 | Deserialization of Untrusted Data vulnerability in xnau webdesign Participants Database participants-database allows Obj |
| CVE-2026-25716 | 7.1 | 2026-10-23 | Missing Authorization vulnerability in Hallo Welt! GmbH BlueSpice (Extension:BlueSpiceUserManager) allows any authentica |
| CVE-2026-25784 | 9.8 | 2026-10-23 | Initialization of a Resource with an Insecure Default vulnerability in Hallo Welt! GmbH BlueSpice (container image blues |
| CVE-2026-112904 | 8.7 | 2026-10-23 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. In versions 1.0. |
| CVE-2026-115723 | 7.4 | 2026-10-23 | Snap7 through 1.4.3 contains an out-of-bounds write vulnerability in the passive partner that allows a malicious active  |
| CVE-2026-115726 | 7.8 | 2026-10-23 | Aider through 0.86.2 contains a command execution vulnerability that allows attackers to run shell commands by committin |
| CVE-2026-115727 | 8.1 | 2026-10-23 | AgenticSeek before commit 409840c contains a remote code execution vulnerability because llm_server/app.py hardcodes Fla |
| CVE-2026-56832 | 8.8 | 2026-10-23 | PraisonAI is a multi-agent teams system. From version 4.5.2 to before version 4.6.59, praisonai.bots.DiscordApproval app |
| CVE-2026-56833 | 7.5 | 2026-10-23 | PraisonAI is a multi-agent teams system. From version 3.8.1 to before version 4.6.59, PraisonAI's Dynamic Context module |
| CVE-2026-56834 | 7.5 | 2026-10-23 | PraisonAI is a multi-agent teams system. From version 3.8.1 to before version 4.6.59, PraisonAI's Dynamic Context Discov |
| CVE-2026-56835 | 8.3 | 2026-10-23 | PraisonAI is a multi-agent teams system. From version 3.11.0 to before version 4.6.59, PraisonAI's Slack bot applies its |
| CVE-2026-56836 | 8.2 | 2026-10-23 | PraisonAI is a multi-agent teams system. From version 4.5.112 to before version 4.6.59, PraisonAI's installed console en |
| CVE-2026-56837 | 8.6 | 2026-10-23 | PraisonAI is a multi-agent teams system. From version 4.6.56 to before version 4.6.59, PraisonAI's LinearBot starts a pu |
| CVE-2026-56838 | 7.8 | 2026-10-23 | PraisonAI is a multi-agent teams system. From version 4.5.87 to before version 4.6.59, PraisonAI recipe execution blocks |
| CVE-2026-56840 | 8.8 | 2026-10-23 | PraisonAI is a multi-agent teams system. From version 4.5.2 to before version 4.6.59, praisonai.bots.HTTPApproval render |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-106931 | EG Secure Solutions / SiteGuard Server Edition | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96656 | Plex / Media Server | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96655 | Plex / Media Server | 2026-10-20 | 2026-11-03 | Unknown |
| CVE-2026-96654 | Plex / Media Server | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96652 | Plex / Media Server | 2026-10-20 | 2026-11-03 | Unknown |
| CVE-2026-110936 | Siemens / Software Center | 2026-10-20 | 2026-11-03 | Unknown |
| CVE-2026-102764 | BeyondTrust / Remote Support | 2026-10-16 | 2026-10-19 | Unknown |
| CVE-2025-61624 | Fortinet / Multiple Products | 2026-10-16 | 2026-10-19 | Unknown |

---

*Total entries in CISA KEV catalog: 1754*