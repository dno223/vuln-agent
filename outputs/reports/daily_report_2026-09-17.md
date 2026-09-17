# Vulnerability Intelligence Report

**Date:** 2026-09-17  
**Generated:** 2026-09-17T13:03:37Z  

## Pipeline Warnings

- summarizer failed: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}, 'request_id': 'req_011Cf94MFNFTBk4ew9MRkLab'}

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
| CVE-2026-19667 | 7.5 | 2026-09-16 | If an attacker-controlled authoritative server can produce a negative answer that is exactly 65536 bytes, then a flaw in |
| CVE-2026-61590 | 7.4 | 2026-09-16 | djust provides Phoenix LiveView-style reactive server-side rendering for Django with Rust-powered performance. Prior to  |
| CVE-2026-77692 | 7.5 | 2026-09-16 | An attacker can cause `named` to abort by sending a crafted DNS-over-HTTPS request with a cryptographically invalid SIG( |
| CVE-2026-81563 | 7.5 | 2026-09-16 | A BIND resolver encountering an SVCB/HTTPS AliasMode record referencing 14 or more SVCB/HTTPS ServiceMode records may fa |
| CVE-2026-81736 | 7.5 | 2026-09-16 | If a BIND resolver has cached a tree of SVCB/HTTPS AliasMode records, and is then queried for the root of that tree, the |
| CVE-2026-89028 | 7.5 | 2026-09-16 | MikroTik RouterOS before 7.24 contains a heap memory corruption vulnerability in the userspace SMB daemon that allows re |
| CVE-2026-91843 | 9.8 | 2026-09-16 | A stack overflow during the unauthenticated login process may allow an attacker to run arbitrary code remotely with root |
| CVE-2026-92122 | 8.8 | 2026-09-16 | Jenkins Script Security Plugin 1415.v9a_f9b_3a_c253d and earlier does not check the method called through the proxy crea |
| CVE-2026-92123 | 8.8 | 2026-09-16 | Jenkins Script Security Plugin 1415.v9a_f9b_3a_c253d and earlier does not intercept operations performed on a null recei |
| CVE-2026-92124 | 8.8 | 2026-09-16 | Jenkins Script Security Plugin 1415.v9a_f9b_3a_c253d and earlier checks the operations Groovy will perform with the elem |
| CVE-2026-92125 | 8.8 | 2026-09-16 | Jenkins Script Security Plugin 1415.v9a_f9b_3a_c253d and earlier does not reject the @GroovyASTTransformationClass annot |
| CVE-2026-92127 | 8.0 | 2026-09-16 | Jenkins Script Security Plugin 1415.v9a_f9b_3a_c253d and earlier automatically approves the classpath entries in an item |
| CVE-2026-92128 | 7.5 | 2026-09-16 | Jenkins Script Security Plugin 1415.v9a_f9b_3a_c253d and earlier downloads a JAR file specified by URL twice, confirming |
| CVE-2026-92129 | 7.5 | 2026-09-16 | Jenkins Script Security Plugin 1415.v9a_f9b_3a_c253d and earlier does not check calls from sandboxed scripts to methods  |
| CVE-2026-92134 | 8.0 | 2026-09-16 | Jenkins Warnings Plugin 13.10258.va_17d49a_78c3b_ and earlier does not validate the analysis results ID when a job confi |
| CVE-2026-92135 | 8.0 | 2026-09-16 | Jenkins Coverage Plugin 3.3358.v9487dde48783 and earlier does not validate the coverage results ID when a job configurat |
| CVE-2026-92136 | 8.0 | 2026-09-16 | Jenkins OWASP Dependency-Check Plugin 5.6.4 and earlier does not escape CWE values from Dependency-Check reports on the  |
| CVE-2026-92137 | 8.8 | 2026-09-16 | Jenkins Robot Framework Plugin 6.2.2 and earlier does not check that the archive directory configured for Robot Framewor |
| CVE-2026-92362 | 7.3 | 2026-09-16 | A vulnerability was detected in ag-ui-protocol ag-ui 1.0. This impacts an unknown function of the file crates/ag-ui-clie |
| CVE-2026-92466 | 8.8 | 2026-09-16 | zlt2000 microservices-platform through 6.0.0 contains a missing authorization vulnerability where the zlt.security.auth. |
| CVE-2026-92467 | 8.3 | 2026-09-16 | zlt2000 microservices-platform through 6.0.0 contains an unverified password change vulnerability in the PUT /users/pass |
| CVE-2026-92469 | 8.1 | 2026-09-16 | zlt2000 microservices-platform through 6.0.0 contains an authorization bypass vulnerability in the file-center module DE |
| CVE-2026-18212 | 7.5 | 2026-09-16 | A flaw was found in the SAML Redirect Binding implementation of Keycloak, an open-source identity and access management  |
| CVE-2026-19666 | 7.5 | 2026-09-16 | On a resolver configured to use ``dns64``, if an applicable answer from the authoritative server is malformed in a speci |
| CVE-2026-63127 | 8.2 | 2026-09-16 | RMCP is an official Rust SDK for the Model Context Protocol. Prior to 2.0.0, the rmcp crate's OAuth implementation in cr |
| CVE-2026-63128 | 7.5 | 2026-09-16 | RMCP is an official Rust SDK for the Model Context Protocol. Prior to 2.0.0, the rmcp crate's stateful Streamable HTTP s |
| CVE-2026-63671 | 8.1 | 2026-09-16 | MDC is a tool to take regular Markdown and write documents interacting deeply with a Vue component. Prior to 0.22.1, @nu |
| CVE-2026-74909 | 8.1 | 2026-09-16 | Keycloak provides a policy enforcer to protect applications by matching incoming web requests against defined security p |
| CVE-2026-76163 | 7.5 | 2026-09-16 | If BIND is loaded with a "`named.conf`" file that contains no global "`options`" block, an attacker can send a query of  |
| CVE-2026-76825 | 8.4 | 2026-09-16 | RestrictedPython is a tool that helps define a subset of the Python language for accepting program input in a trusted en |
| CVE-2026-79651 | 7.5 | 2026-09-16 | A flaw was found in the theme localization endpoints of the keycloak-services component, which is the core service respo |
| CVE-2026-80274 | 7.5 | 2026-09-16 | If a BIND resolver sends a query for a DNSSEC-signed authoritative zone, and the authoritative server replies with a val |
| CVE-2026-82964 | 8.8 | 2026-09-16 | Improper preservation of permissions in the Avast sandbox minifilter driver (aswSnx.sys) on Windows allows a local, low- |
| CVE-2026-84858 | 8.8 | 2026-09-16 | ScadaLTS 2.8.1-release-candidate build 0 is affected by an Authenticated Remote Code Execution via Scripting Sandbox Byp |
| CVE-2026-84860 | 8.8 | 2026-09-16 | ScadaLTS 2.8.1-release-candidate build 0 is affected by an Authorization Bypass



Spring Security gates DWR endpoints b |
| CVE-2026-84997 | 7.5 | 2026-09-16 | react/http is an event-driven, streaming HTTP client and server implementation for ReactPHP. From 0.6.0 until 1.11.1, Re |
| CVE-2026-88064 | 8.8 | 2026-09-16 | Backstage is an open framework for building developer portals. Prior to 1.14.6 and from 1.15.0 until 1.15.4, the @backst |
| CVE-2026-92087 | 8.1 | 2026-09-16 | @fastify/auth is a Fastify plugin that composes multiple authentication and authorization strategies into a single route |
| CVE-2026-92366 | 7.3 | 2026-09-16 | A vulnerability was determined in code-projects Matrimonial System 1.0. This affects an unknown part of the file /search |
| CVE-2026-92380 | 7.3 | 2026-09-16 | A flaw has been found in WuzhiCMS up to 4.1.0. The impacted element is the function ckditor::saveRemote of the file core |
| CVE-2026-92395 | 9.1 | 2026-09-16 | @fastify/proxy-addr is a Fastify plugin that determines a request's client address behind trusted reverse proxies, and i |
| CVE-2026-92566 | 8.2 | 2026-09-16 | DataGear through 6.0.0 contains a server-side request forgery vulnerability in the /dataSet/preview/Http endpoint that a |
| CVE-2025-43936 | 8.1 | 2026-09-16 | Dell ObjectScale, versions prior to ObjectScale 4.4.0.0, contains an Improper Authentication vulnerability. An unauthent |
| CVE-2025-59953 | 9.8 | 2026-09-16 | LMDeploy is a toolkit for compressing, deploying, and serving large language models. Starting in version 0.9.1 and prior |
| CVE-2026-17526 | 7.2 | 2026-09-16 | Keycloak is an open-source identity and access management solution. A vulnerability was discovered where a user with the |
| CVE-2026-61593 | 8.1 | 2026-09-16 | djust provides Phoenix LiveView-style reactive server-side rendering for Django with Rust-powered performance. Prior to  |
| CVE-2026-61595 | 7.7 | 2026-09-16 | djust provides Phoenix LiveView-style reactive server-side rendering for Django with Rust-powered performance. Prior to  |
| CVE-2026-70416 | 10.0 | 2026-09-16 | Dell ObjectScale, versions prior to 4.4.0.0, contains a Deserialization of Untrusted Data vulnerability. An unauthentica |
| CVE-2026-92397 | 9.1 | 2026-09-16 | A vulnerability has been found in Ruijie RG-EW3000GX EW_3.0(1)B11P380. Affected by this vulnerability is the function cc |
| CVE-2026-92625 | 7.5 | 2026-09-16 | Control iD iDSecure versions prior to 4.8.3.0 are affected by an unauthenticated Denial of Service.


The /api/license/r |
| CVE-2026-92626 | 7.5 | 2026-09-16 | Control iD iDSecure versions prior to 4.8.3.0 are affected by an unauthenticated Denial of Service.


The /api/dguardint |
| CVE-2026-20234 | 9.9 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Identity Services Engine (ISE |
| CVE-2026-20305 | 9.1 | 2026-09-16 | A vulnerability in the diagnostic tools of Cisco ISE and ISE-PIC could allow an authenticated, remote attacker to perfor |
| CVE-2026-20306 | 9.1 | 2026-09-16 | A vulnerability in the REST API of Cisco ISE and ISE-PIC could allow an authenticated, remote attacker to perform comman |
| CVE-2026-20307 | 9.9 | 2026-09-16 | A vulnerability in the web-based management interface of Cisco ISE could allow an authenticated, remote attacker to exec |
| CVE-2026-20331 | 9.6 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Adaptive Security Appl |
| CVE-2026-42784 | 7.4 | 2026-09-16 | A flaw was found in sequoia-openpgp. The library incorrectly infers key flags for older certificates when a key flags su |
| CVE-2026-59974 | 7.8 | 2026-09-16 | Stanza is a Stanford NLP Python library for tokenization, sentence segmentation, NER, and parsing of many human language |
| CVE-2026-68904 | 7.0 | 2026-09-16 | node-opcua is an OPC UA implementation for TypeScript and Node.js. From 2.0.0 until 2.170.0, node-opcua clients using th |
| CVE-2026-71179 | 7.3 | 2026-09-16 | Dell Update Package Framework, versions prior to 26.07.03, contains an Improper Neutralization of Special Elements used  |
| CVE-2026-71180 | 8.2 | 2026-09-16 | Dell Update Package Framework, versions prior to 26.07.03, contains an Unchecked Return Value vulnerability. A low privi |
| CVE-2026-76420 | 9.0 | 2026-09-16 | A vulnerability in the internal configuration of the Apache JServ Protocol (AJP)&nbsp;connector for Cisco Secure FMC Sof |
| CVE-2026-85731 | 8.8 | 2026-09-16 | oras-go is a Go library for managing OCI artifacts. Prior to 2.6.2, content/file.Store extraction of OCI layers marked w |
| CVE-2026-85756 | 7.5 | 2026-09-16 | SSH.NET is a Secure Shell (SSH) library for .NET. Prior to 2026.0.0, ScpClient places caller-supplied remote paths into  |
| CVE-2026-86359 | 8.5 | 2026-09-16 | Dell Repository Manager, versions prior to 3.5.2, contains an Incorrect Default Permissions vulnerability. A low privile |
| CVE-2026-92398 | 9.1 | 2026-09-16 | A vulnerability was found in Ruijie RG-EW3000GX EW_3.0(1)B11P380. Affected by this issue is some unknown functionality o |
| CVE-2026-92399 | 7.3 | 2026-09-16 | A vulnerability was determined in GPAC 26.07.0. This affects the function rmt_client_handle_ws_frame of the file src/uti |
| CVE-2026-92401 | 7.3 | 2026-09-16 | A vulnerability was identified in ChangeWeDer crm up to c07bd4c97141521af6475034bc58523beed51bbd. This vulnerability aff |
| CVE-2026-92405 | 7.3 | 2026-09-16 | A security vulnerability has been detected in SourceCodester Inventory and Monitoring System 1.0. The affected element i |
| CVE-2026-92602 | 7.1 | 2026-09-16 | TDuck survey form through version 5.3 fails to validate webhook URLs or verify form ownership in the WebhookConfigContro |
| CVE-2026-47094 | 8.8 | 2026-09-16 | SIMAC MyPHR 1.1 contains an insecure direct object reference (IDOR) vulnerability that allows authenticated attackers to |
| CVE-2026-92406 | 7.3 | 2026-09-16 | A vulnerability was detected in SourceCodester Inventory and Monitoring System 1.0. The impacted element is an unknown f |
| CVE-2026-92604 | 8.1 | 2026-09-16 | Scirius through 3.8.0 contains an arbitrary file write vulnerability in the PCAP filestore upload endpoint that allows d |
| CVE-2026-92716 | 9.6 | 2026-09-16 | Shuffle through 2.2.1 contains a cross-tenant privilege escalation vulnerability in the HandleApiGeneration endpoint tha |
| CVE-2026-92717 | 9.1 | 2026-09-16 | Covenant through 0.6 registers the CovenantHub SignalR hub without an Authorize attribute, allowing unauthenticated call |
| CVE-2026-92718 | 7.3 | 2026-09-16 | Nuclei versions before 3.11.1 cache template signature verification based only on file modification time without content |
| CVE-2026-92719 | 7.5 | 2026-09-16 | Quickwit through 0.9.0 fails to validate the host and scheme of the queue_url parameter in SQS file sources, allowing at |
| CVE-2026-92720 | 9.1 | 2026-09-16 | Kubero through 3.1.1 fails to apply authentication guards to the notifications API endpoints, allowing unauthenticated a |
| CVE-2026-46352 | 7.5 | 2026-09-16 | Suricata is a network Intrusion Detection System, Intrusion Prevention System and Network Security Monitoring engine. St |
| CVE-2026-63126 | 7.5 | 2026-09-16 | Wire provides gRPC and protocol buffers for Android, Kotlin, Swift, and Java. Prior to 6.4.5 and 7.0.0-alpha04, Wire pro |
| CVE-2026-63325 | 7.8 | 2026-09-16 | Redocly CLI makes OpenAPI validation, linting, and documentation workflows easier. Prior to version 2.33.0 of @redocly/r |
| CVE-2026-73456 | 10.0 | 2026-09-16 | Under certain circumstances on affected platforms running Arista EOS with gRPC Network Packet Sampling Interface (gNPSI) |
| CVE-2026-81875 | 7.5 | 2026-09-16 | HAPI FHIR is a complete implementation of the HL7 FHIR standard for healthcare interoperability in Java. Prior to versio |
| CVE-2026-81876 | 7.5 | 2026-09-16 | HAPI FHIR is a complete implementation of the HL7 FHIR standard for healthcare interoperability in Java. Prior to versio |
| CVE-2026-82399 | 7.5 | 2026-09-16 | CoreDNS is a DNS server written in Go. Prior to 1.14.7, the DNS-over-HTTPS, DNS-over-HTTP/3, DNS-over-QUIC, and DNS-over |
| CVE-2026-86003 | 7.5 | 2026-09-16 | CoreDNS is a DNS server written in Go. Prior to 1.14.7, the DNS-over-HTTPS, DNS-over-HTTP/3, DNS-over-QUIC, and DNS-over |
| CVE-2026-86043 | 7.5 | 2026-09-16 | Skipper is an HTTP router and reverse proxy for service composition. Prior to version 0.27.37, the opaAuthorizeRequestWi |
| CVE-2026-92729 | 8.2 | 2026-09-16 | SigNoz versions 0.88.0 through 0.141.0 fail to apply authorization wrappers to trace-funnel analytics endpoints in the H |
| CVE-2026-20130 | 10.0 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Identity Services Engine (ISE |
| CVE-2026-20176 | 9.1 | 2026-09-16 | A vulnerability in Cisco ISE could allow an authenticated, remote attacker to execute arbitrary commands on the underlyi |
| CVE-2026-20192 | 10.0 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Identity Services Engine (ISE |
| CVE-2026-20194 | 9.1 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Identity Services Engine (ISE |
| CVE-2026-20211 | 9.1 | 2026-09-16 | A vulnerability in Cisco ISE could allow an authenticated, remote attacker to execute arbitrary commands on the underlyi |
| CVE-2026-20237 | 9.1 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Identity Services Engine (ISE |
| CVE-2026-20242 | 9.8 | 2026-09-16 | A vulnerability in the External Database Access feature of Cisco Secure Firewall Management Center (FMC) Software could  |
| CVE-2026-20322 | 9.9 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Nexus Dashboard&nbsp;engineer |
| CVE-2026-20324 | 9.9 | 2026-09-16 | A vulnerability in the sftunnel inter-device communication protocol of Cisco Secure Firewall Management Center (FMC) Sof |
| CVE-2026-20325 | 9.9 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Nexus Dashboard&nbsp;engineer |
| CVE-2026-20326 | 9.8 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Nexus Dashboard engineering t |
| CVE-2026-20329 | 9.9 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Adaptive Security Appl |
| CVE-2026-20330 | 9.9 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Adaptive Security Appl |
| CVE-2026-20341 | 9.1 | 2026-09-16 | A vulnerability in the sftunnel inter-device communication protocol of Cisco Secure FMC Software could allow an authenti |
| CVE-2026-20361 | 8.8 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Nexus Dashboard engineering t |
| CVE-2026-76423 | 10.0 | 2026-09-16 | A vulnerability in the REST API of Cisco ISE and Cisco ISE-PIC could allow an unauthenticated, remote attacker to gain a |
| CVE-2026-86831 | 8.7 | 2026-09-16 | Improper validation of pod identifier uniqueness in aws-network-policy-agent in Amazon EKS Network Policy Agent before v |
| CVE-2026-86865 | 8.8 | 2026-09-16 | Tanium addressed a SQL injection vulnerability in Asset. |
| CVE-2026-87024 | 7.2 | 2026-09-16 | Tanium addressed a SQL injection vulnerability in Asset. |
| CVE-2026-87105 | 8.8 | 2026-09-16 | Tanium addressed a SQL injection vulnerability in Threat Response. |
| CVE-2026-20135 | 8.6 | 2026-09-16 | A vulnerability in the TLS 1.3 implementation in Cisco Secure Firewall Threat Defense (FTD) Software could allow an unau |
| CVE-2026-20154 | 8.6 | 2026-09-16 | A vulnerability in the system rate-limiting process for syslog message 419002 of Cisco Secure Firewall Adaptive Security |
| CVE-2026-20222 | 7.4 | 2026-09-16 | A vulnerability in the EIGRP implementation in Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisc |
| CVE-2026-20247 | 7.5 | 2026-09-16 | A vulnerability in Cisco ISE could allow an unauthenticated, remote attacker to conduct SQL injection attacks on an affe |
| CVE-2026-20249 | 8.6 | 2026-09-16 | A vulnerability in the certification authentication feature of Internet Key Exchange version 2 (IKEv2)&nbsp;for Cisco Se |
| CVE-2026-20250 | 8.6 | 2026-09-16 | A vulnerability in Datagram TLS (DTLS) message handling of Cisco Secure Firewall Adaptive Security Appliance (ASA) Softw |
| CVE-2026-20284 | 9.1 | 2026-09-16 | A vulnerability in the SXP REST API of Cisco ISE could allow an authenticated, remote attacker to conduct SQL injection  |
| CVE-2026-20295 | 8.6 | 2026-09-16 | A vulnerability in the sftunnel inter-device communication protocol of Cisco Secure FMC Software and Cisco Secure FTD So |
| CVE-2026-20300 | 7.1 | 2026-09-16 | A vulnerability in Cisco ISE could allow an authenticated, remote attacker to conduct SQL injection attacks on an affect |
| CVE-2026-20323 | 8.3 | 2026-09-16 | A vulnerability in the sftunnel inter-device communication protocol of Cisco Secure FMC Software and Cisco Secure FTD So |
| CVE-2026-20332 | 9.9 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Adaptive Security Appl |
| CVE-2026-20333 | 8.8 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Adaptive Security Appl |
| CVE-2026-20334 | 8.4 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Adaptive Security Appl |
| CVE-2026-20335 | 8.1 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Adaptive Security Appl |
| CVE-2026-20336 | 8.8 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Adaptive Security Appl |
| CVE-2026-20340 | 8.8 | 2026-09-16 | A vulnerability in Cisco Secure FMC Software could allow an authenticated, remote attacker to execute arbitrary commands |
| CVE-2026-20342 | 7.7 | 2026-09-16 | A vulnerability in a specific file download API of Cisco Secure FMC Software could allow an authenticated, remote attack |
| CVE-2026-20343 | 7.5 | 2026-09-16 | A vulnerability in a critical API for Cisco Secure FMC Software could allow an unauthenticated, remote attacker to downl |
| CVE-2026-20344 | 8.8 | 2026-09-16 | A vulnerability in the web-based management interface of Cisco Secure FMC Software could allow an authenticated, remote  |
| CVE-2026-20352 | 8.6 | 2026-09-16 | A vulnerability in the RADIUS feature of Cisco Identity Services Engine (ISE) could allow an unauthenticated, remote att |
| CVE-2026-20360 | 8.8 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Nexus Dashboard engineering t |
| CVE-2026-63506 | 8.8 | 2026-09-16 | Tina is a headless content management system. Prior to @tinacms/auth 1.1.4 and next-tinacms-azure 15.0.1, isAuthorized a |
| CVE-2026-75513 | 9.1 | 2026-09-16 | Marten is a .NET Transactional Document DB and Event Store on PostgreSQL. From version 7.0.0 until 9.13.0, several Marte |
| CVE-2026-76409 | 8.8 | 2026-09-16 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Nexus Dashboard engineering t |
| CVE-2026-76412 | 8.5 | 2026-09-16 | A vulnerability in the remote diagnostics debugger of Cisco Secure FMC Software could allow an authenticated, remote att |
| CVE-2026-76413 | 8.2 | 2026-09-16 | A vulnerability in Cisco Adaptive Security Device Manager (ASDM) single sign-on (SSO) handler for Cisco Secure FMC Softw |
| CVE-2026-76424 | 7.2 | 2026-09-16 | A vulnerability in the REST API of Cisco ISE could allow an authenticated, remote attacker to upload or copy arbitrary f |
| CVE-2026-76425 | 7.6 | 2026-09-16 | A vulnerability in the APIs of Cisco ISE could allow an authenticated, remote attacker to conduct SQL injection attacks  |
| CVE-2026-76460 | 10.0 | 2026-09-16 | A vulnerability in an API of Cisco Identity Services Engine (ISE) could allow an unauthenticated, remote attacker to byp |
| CVE-2026-92748 | 8.8 | 2026-09-16 | BC Security Empire before 6.7.1 fails to validate the multipart filename parameter in upload endpoints, allowing authent |
| CVE-2026-92749 | 8.1 | 2026-09-16 | SafeLine through 9.4.1 derives the management console session-signing secret from a time-seeded math/rand generator, all |
| CVE-2026-92751 | 8.1 | 2026-09-16 | CMAK through 3.0.0.6 fails to install a cross-site request forgery filter, allowing attackers to perform state-changing  |
| CVE-2026-92752 | 8.3 | 2026-09-16 | metasfresh DocumentAttachmentsRestController and CommentsRestController endpoints check only that callers are logged in  |
| CVE-2026-92753 | 7.1 | 2026-09-16 | PatrowlManager through 1.8.4 contains an authorization bypass vulnerability in the events and alerts API endpoints that  |
| CVE-2026-92761 | 8.8 | 2026-09-16 | WebVirtCloud fails to properly validate permission flags in UserInstance grants, allowing view-only users to perform pri |
| CVE-2026-92762 | 8.8 | 2026-09-16 | Pelican Panel versions before 1.0.0-beta35 enforce startup write permissions only through disabled form controls rather  |
| CVE-2026-92763 | 8.1 | 2026-09-16 | Rundeck through 6.2.1 fails to properly authorize the importConfig and importNodesSources parameters in the project arch |
| CVE-2026-92772 | 7.1 | 2026-09-16 | Leantime before 3.9.6 contains an authorization bypass vulnerability in the HTMX plugin install endpoint that lacks perm |
| CVE-2026-92773 | 7.1 | 2026-09-16 | Trigger.dev before 4.6.0 fails to verify that an authenticated user controls a GitHub App installation before binding it |
| CVE-2026-92776 | 8.1 | 2026-09-16 | Wiki.js through 2.5.314 fails to require path separators when matching START and END page rules, allowing attackers to a |
| CVE-2026-92779 | 7.6 | 2026-09-16 | Builder.io Gen2 SDKs through versions 5.2.11 and 0.25.13 contain a prototype pollution vulnerability in the deep-set hel |
| CVE-2026-92780 | 8.8 | 2026-09-16 | KnowStreaming through 3.4.1 fails to enforce role-based access control on REST API endpoints, allowing any authenticated |
| CVE-2026-92782 | 8.1 | 2026-09-16 | Chroma through 1.5.9 fails to validate tenant and database segments when resolving collections, allowing authenticated a |
| CVE-2026-92783 | 8.1 | 2026-09-16 | Yeti through 2.11.0 fails to validate caller permissions in the DELETE /api/v2/rbac/{id} endpoint, allowing users with r |
| CVE-2026-92784 | 7.5 | 2026-09-16 | @refinedev/inferencer through 7.0.0 fails to escape API field names when interpolating them into generated JSX source co |
| CVE-2026-92785 | 8.1 | 2026-09-16 | Angel through 3.3.0 deserializes untrusted setAlgoMetrics payload using Kryo without class registration or allowlist val |
| CVE-2026-92786 | 7.8 | 2026-09-16 | LightGBM through 4.7.0 fails to validate child and split array values when parsing text models, allowing attackers to wr |
| CVE-2026-92787 | 9.8 | 2026-09-16 | Feast through 0.66.0 fails to verify JWT token signatures before establishing user identity, allowing attackers to bypas |
| CVE-2026-92788 | 8.8 | 2026-09-16 | Coze Studio through 0.5.1 fails to validate that table names in workflow SQL customization nodes belong to the caller's  |
| CVE-2026-92791 | 7.5 | 2026-09-16 | Uber Kraken through 0.1.29 fails to validate the tag parameter in the /tags/{tag} endpoint, allowing unauthenticated att |
| CVE-2026-92792 | 7.5 | 2026-09-16 | OpenNHP through 1.0.2 selects its trusted-execution attestation verifier based on attacker-supplied evidence containing  |
| CVE-2026-92793 | 8.1 | 2026-09-16 | GoAdmin through 1.2.26 fails to properly anchor the logout pattern when checking permissions, allowing authenticated use |
| CVE-2026-92794 | 7.5 | 2026-09-16 | OpenSign through 2.41.3 fails to validate caller identity in the getDocument cloud function when one-time-password verif |
| CVE-2026-92796 | 8.8 | 2026-09-16 | Manticore Search versions 27.0.0 before 28.4.4 fail to validate permissions for all statements in multi-statement SQL re |
| CVE-2026-92801 | 8.8 | 2026-09-16 | cc-connect through 1.5.0 fails to enforce per-user allowlist filtering in the onCardAction handler for Feishu interactiv |
| CVE-2026-92804 | 7.1 | 2026-09-16 | Nango through 0.70.4 fails to validate caller-supplied connection configuration values interpolated into provider token  |
| CVE-2026-92805 | 9.8 | 2026-09-16 | UVdesk Community Skeleton through 1.1.8 fails to authenticate or validate installation state on wizard endpoints in Conf |
| CVE-2026-92806 | 8.1 | 2026-09-16 | phpList versions before 3.6.17 fail to validate cross-site request forgery tokens in the mass subscriber removal form ha |
| CVE-2026-92815 | 7.5 | 2026-09-16 | changedetection.io through 0.60.6 fails to validate the Goto URL action in browser steps, allowing unauthenticated attac |
| CVE-2026-92816 | 7.8 | 2026-09-16 | ComfyUI before 0.30.0 fails to sanitize folder_name input in dataset save nodes, allowing attackers to write files to ar |
| CVE-2026-61591 | 8.1 | 2026-09-16 | djust provides Phoenix LiveView-style reactive server-side rendering for Django with Rust-powered performance. Prior to  |
| CVE-2026-61592 | 7.4 | 2026-09-16 | djust provides Phoenix LiveView-style reactive server-side rendering for Django with Rust-powered performance. Prior to  |
| CVE-2026-61594 | 9.1 | 2026-09-16 | djust provides Phoenix LiveView-style reactive server-side rendering for Django with Rust-powered performance. Prior to  |
| CVE-2026-85469 | 8.0 | 2026-09-16 | A flaw was found in quay-builder-qemu. A remote attacker could exploit this by compromising the upstream `Noelware/docke |
| CVE-2026-92576 | 8.6 | 2026-09-16 | HKUDS nanobot before 0.3.0 contains a server-side request forgery vulnerability in the WebFetchTool component where the  |
| CVE-2026-92577 | 7.5 | 2026-09-16 | In AVideo through 29.0, the API get_api_video endpoint contains a broken access control vulnerability in the clean_title |
| CVE-2026-92578 | 8.1 | 2026-09-16 | WWBN AVideo through 29.0 contains an authentication bypass vulnerability where the stored password hash is accepted as a |
| CVE-2026-92580 | 8.8 | 2026-09-16 | In AVideo through 29.0, the CloneSite plugin is vulnerable to stored OS command injection. In plugin/CloneSite/cloneClie |
| CVE-2026-92582 | 7.1 | 2026-09-16 | AVideo (WWBN/AVideo) through 29.0 (commit e01e41ecc) is vulnerable to cross-site request forgery. objects/videoAddNew.js |
| CVE-2026-92592 | 8.8 | 2026-09-16 | Craft CMS 4.8.0 through 4.18.5 and 5.0.0 through 5.10.12 sign an authenticated user's attacker-controlled license-shun c |
| CVE-2026-92593 | 8.8 | 2026-09-16 | Craft CMS versions 5.10.0 through 5.10.12 contain an incomplete fix for CVE-2026-55794: the Controller::getPostedRedirec |
| CVE-2026-92594 | 7.5 | 2026-09-16 | Craft CMS 5.0.0-RC1 through versions before 5.11.0 incorrectly authorize the GraphQL draftCreator and revisionCreator fi |
| CVE-2026-92596 | 7.5 | 2026-09-16 | Nodemailer before 9.1.0 contains a quadratic time complexity vulnerability in the addressparser component that allows re |
| CVE-2026-92599 | 7.5 | 2026-09-16 | joi (npm package `joi`, hapi.js) versions >=17.2.0 <17.13.7 and >=18.0.0 <18.2.6 are vulnerable to regular expression de |
| CVE-2026-61596 | 7.1 | 2026-09-16 | djust provides Phoenix LiveView-style reactive server-side rendering for Django with Rust-powered performance. Prior to  |
| CVE-2026-81546 | 7.7 | 2026-09-17 | The Affinity by Canva application before 3.3.0 (September 2026 release) did not perform adequate bounds checking when pa |
| CVE-2026-92838 | 7.8 | 2026-09-17 | A DLL hijacking
vulnerability exists in the GeoVision GV-Remote E-Map desktop
application. The application loads one or  |
| CVE-2025-59607 | 7.8 | 2026-09-17 | Memory Corruption when copying large input data exceeds normal allocation limits. |
| CVE-2026-24073 | 7.8 | 2026-09-17 | Memory corruption when processing decode statistics due to insufficient validation of offset against structure size. |
| CVE-2026-24074 | 7.8 | 2026-09-17 | Memory Corruption when processing data with large offset and length values exceeds buffer limits during data copy operat |
| CVE-2026-24075 | 7.8 | 2026-09-17 | Memory Corruption when multiple threads issue concurrent IOCTL requests to the device control handler due to improper sy |
| CVE-2026-24081 | 7.4 | 2026-09-17 | Transient DOS when processing a channel map with insufficient used channels and adaptive frequency hopping is fully enab |
| CVE-2026-25275 | 7.5 | 2026-09-17 | Transient DOS when processing authentication frames with invalid FILS information element header lengths. |
| CVE-2026-25278 | 7.8 | 2026-09-17 | Memory Corruption when processing I2C transfer requests due to a race condition between memory allocation and data copyi |
| CVE-2026-25280 | 7.8 | 2026-09-17 | Memory corruption when processing escape handling flow with insufficient user buffer sizes. |
| CVE-2026-25281 | 7.4 | 2026-09-17 | Transient DOS when processing large or numerous request buffers without sufficient memory allocation validation. |
| CVE-2026-25282 | 7.9 | 2026-09-17 | Transient DOS when processing unverified data from a neighboring system causes out of bound memory access. |
| CVE-2026-25283 | 8.8 | 2026-09-17 | Memory Corruption when copying unverified data from an external source exceeds the allocated buffer size. |
| CVE-2026-25284 | 7.3 | 2026-09-17 | Information Disclosure when a pointer is reused after being deallocated. |
| CVE-2026-25290 | 7.8 | 2026-09-17 | Memory Corruption when validating large data buffers from external sources using addition to check buffer length. |
| CVE-2026-25294 | 7.4 | 2026-09-17 | Transient DOS while parsing frame during channel usage. |
| CVE-2026-87796 | 9.8 | 2026-09-17 | The Multi Uploader for Gravity Forms plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to,  |
| CVE-2026-87935 | 8.1 | 2026-09-17 | The Paid Downloads plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 3.1 |
| CVE-2026-86801 | 8.8 | 2026-09-17 | The To Do List Member WordPress plugin from 1.4 through 1.6 ships a file upload endpoint that does not load WordPress an |
| CVE-2026-87963 | 8.6 | 2026-09-17 | The Yo WordPress plugin from 1.1 through 1.3.1 does not sanitize or parameterize the username request parameter before u |
| CVE-2026-86320 | 7.8 | 2026-09-17 | A flaw was found in flatpak-builder where Git hooks are not disabled when applying patch sources with use-git-am: true.  |
| CVE-2026-78428 | 8.0 | 2026-09-17 | For users authenticated through SAML or OpenID Connect (OIDC), this vulnerability can result in one user receiving anoth |
| CVE-2026-66269 | 7.3 | 2026-09-17 | Dell OpenManage Server Administrator, versions prior to 11.1.0.3, contains a Use of Externally-Controlled Input to Selec |
| CVE-2026-81474 | 7.8 | 2026-09-17 | Dell OpenManage Server Administrator, versions prior to 11.1.0.3, contains a Heap-based Buffer Overflow vulnerability. A |
| CVE-2026-92903 | 8.2 | 2026-09-17 | Improper input validation in Snowflake CLI versions prior to 3.27.0 allowed unsanitized user-controlled values to be int |
| CVE-2026-81440 | 7.3 | 2026-09-17 | Dell OpenManage Server Administrator, versions prior to 11.1.0.3, contains a Use of Hard-coded Credentials vulnerability |
| CVE-2026-81475 | 8.1 | 2026-09-17 | Dell OpenManage Server Administrator, versions prior to 11.1.0.3, contains a Missing Authentication for Critical Functio |
| CVE-2026-81476 | 8.1 | 2026-09-17 | Dell OpenManage Server Administrator, versions prior to 11.1.0.3, contains an Improper Neutralization of Special Element |
| CVE-2026-81477 | 7.2 | 2026-09-17 | Dell OpenManage Server Administrator, versions prior to 11.1.0.3, contains a Heap-based Buffer Overflow vulnerability. A |
| CVE-2026-81478 | 8.1 | 2026-09-17 | Dell OpenManage Server Administrator, versions prior to 11.1.0.3, contains a Use of Hard-coded Cryptographic Key vulnera |
| CVE-2026-81480 | 7.2 | 2026-09-17 | Dell OpenManage Server Administrator, versions prior to 11.1.0.3, contains a Stack-based Buffer Overflow vulnerability.  |
| CVE-2026-90822 | 9.8 | 2026-09-17 | FatPipe MPVPN, WARP, and IPVPN appliances running the end-of-life firmware version 10.1.2r60p100 contain an OS command i |
| CVE-2026-90823 | 9.8 | 2026-09-17 | FatPipe MPVPN, WARP, and IPVPN appliances running the end-of-life firmware version 10.1.2r60p100 contain a stack-based b |
| CVE-2026-92860 | 9.1 | 2026-09-17 | A security flaw has been discovered in rcourtman Pulse up to 6.0.4/6.1.0-rc.4. Affected by this issue is the function fm |
| CVE-2026-92913 | 7.4 | 2026-09-17 | AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 uses a cryptographically weak pseudo-random number genera |
| CVE-2026-92914 | 8.1 | 2026-09-17 | AVideo LoginControl contains an authentication bypass vulnerability in the PGP second factor verification that compares  |
| CVE-2026-92915 | 7.3 | 2026-09-17 | WWBN AVideo through commit e01e41ecc (no patched version available) contains a broken access control flaw in objects/use |
| CVE-2026-92916 | 7.5 | 2026-09-17 | Grav is a flat-file CMS. In Grav 1.7.0 through 1.7.53.2 and 2.0.0 through 2.0.21, when the debugger is enabled (system.d |
| CVE-2026-92917 | 7.5 | 2026-09-17 | Grav is a flat-file CMS. In versions 2.0.0-rc.1 through 2.0.21, the Twig content sandbox fails to restrict the dump and  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-58704 | Google / Pixel | 2026-09-16 | 2026-09-19 | Unknown |
| CVE-2026-76460 | Cisco / Identity Services Engine | 2026-09-16 | 2026-09-19 | Unknown |
| CVE-2026-87886 | Acronis / Backup | 2026-09-16 | 2026-09-19 | Unknown |
| CVE-2026-76461 | Cisco / Secure Email Gateway | 2026-09-14 | 2026-09-17 | Unknown |
| CVE-2026-84869 | ConnectWise / ScreenConnect | 2026-09-11 | 2026-09-14 | Unknown |
| CVE-2026-42016 | JFrog / Artifactory | 2026-09-11 | 2026-09-25 | Unknown |
| CVE-2026-42018 | JFrog / Artifactory | 2026-09-11 | 2026-09-25 | Unknown |
| CVE-2026-85706 | GitLab / Community Edition and Enterprise Edition | 2026-09-11 | 2026-09-14 | Unknown |
| CVE-2026-86060 | MikroTik / RouterOS | 2026-09-10 | 2026-09-13 | Unknown |
| CVE-2026-67277 | MikroTik / RouterOS | 2026-09-10 | 2026-09-13 | Unknown |

---

*Total entries in CISA KEV catalog: 1713*