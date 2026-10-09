# Vulnerability Intelligence Report

**Date:** 2026-10-09  
**Generated:** 2026-10-09T14:58:53Z  

---

## Executive Summary

Our environment faces significant exposure from 195 high-severity vulnerabilities, including multiple critical IBM DataPower Gateway flaws rated up to CVSS 9.8 that allow remote code execution and authentication bypass. Eight vulnerabilities were newly added to CISA's Known Exploited Vulnerabilities catalog this week, signaling active exploitation in the wild. While no monitored CVEs currently overlap with the KEV catalog, the volume and severity of new disclosures demands immediate prioritization. Unpatched systems running IBM DataPower, ILIAS, EspoCRM, and Integrics Enswitch represent the highest near-term risk to business operations, data confidentiality, and service availability.

---

## Risk Narrative

The threat landscape is characterized by a high volume of critical vulnerabilities targeting enterprise middleware, learning management, and CI/CD platforms. Active exploitation of legacy flaws in Apache Struts and ISC BIND—now confirmed in CISA's KEV catalog—demonstrates that attackers continue leveraging known weaknesses against unpatched systems. Critical authentication bypass and remote code execution vulnerabilities in IBM DataPower Gateway and Integrics Enswitch could enable attackers to gain full system control without credentials, threatening data integrity, regulatory compliance, and operational continuity. The combination of newly disclosed critical CVEs and actively exploited legacy vulnerabilities substantially elevates organizational risk, requiring accelerated patch cycles and proactive threat monitoring.

---

## Prioritized Action Items

1. Immediately patch or isolate all IBM DataPower Gateway instances affected by CVE-2026-14269 and CVE-2026-14502 (CVSS 9.8) to prevent remote code execution.
2. Remediate the Integrics Enswitch authentication bypass (CVE-2026-107640, CVSS 9.1) by applying vendor patches or restricting API access via network controls.
3. Apply available patches for the five newly KEV-listed vulnerabilities (BIND, Apache Struts, Strapi, ONLYOFFICE, ProFTPD) within 24–48 hours per CISA guidance.
4. Update ILIAS to the latest patched version to address the argument injection vulnerability (CVE-2026-107639, CVSS 8.8) that enables privilege escalation.
5. Audit and remediate remaining high-severity CVEs across EspoCRM, Pydantic AI, and Jacamar CI, prioritizing internet-facing instances and those handling sensitive data.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-105830 | 7.5 | 2026-10-08 | league/commonmark from 2.0.0 before 2.10.2 contains a quadratic-time denial of service vulnerability in the GitHub Flavo |
| CVE-2026-105833 | 7.7 | 2026-10-08 | EspoCRM before 10.0.5 contains an insecure direct object reference vulnerability in PersonalAccount\Service that allows  |
| CVE-2026-107286 | 7.5 | 2026-10-08 | Pydantic AI is a Python agent framework for building applications and workflows with Generative AI. From 2.10.0 until 2. |
| CVE-2026-107589 | 7.5 | 2026-10-08 | Insufficient job validation for service accounts in Jacamar CI prior to v0.30.0 allows authenticated CI users to generat |
| CVE-2026-107639 | 8.8 | 2026-10-08 | ILIAS before 9.24, 10.x before 10.12 and 11.x before 11.5 contains an argument injection vulnerability in assImagemapQue |
| CVE-2026-107640 | 9.1 | 2026-10-08 | Integrics Enswitch 3.13 through 4.4 contains an authentication bypass vulnerability in /api/json/user/password/update/ t |
| CVE-2026-14269 | 9.8 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-14496 | 8.2 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-14497 | 8.1 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-14502 | 9.8 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-14507 | 7.7 | 2026-10-08 | IBM DataPower Gateway 11.0.0.0 through 11.0.0.2 could allow a remote authenticated attacker to cause a denial of service |
| CVE-2026-14888 | 8.1 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-14905 | 8.2 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-14992 | 9.8 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-14999 | 7.4 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-93017 | 7.7 | 2026-10-08 | The `insights-operator-gather` ClusterRole grants the operator's service account read access to secrets in the core API  |
| CVE-2026-93034 | 9.8 | 2026-10-08 | SGLang contains an arbitrary code execution vulnerability caused by the ZMQ message decoder unconditionally deserializin |
| CVE-2026-9209 | 9.8 | 2026-10-08 | mJobTime through build 15.7.3.32 contains an unauthenticated SQL execution vulnerability in the Login.aspx admin panel h |
| CVE-2026-95208 | 7.5 | 2026-10-08 | An issue in the ConfirmNameConstraints() function (wolfcrypt/src/asn.c) of wolfSSL v5.9.1 and v5.9.2 allows attackers to |
| CVE-2026-104077 | 7.8 | 2026-10-08 | Obsidian Desktop before 1.14.0 contains a remote code execution vulnerability that allows attackers to craft malicious M |
| CVE-2026-104078 | 7.8 | 2026-10-08 | Obsidian Desktop before 1.14.0 contains a filter bypass vulnerability in the bundled MathJax 3.2.2 Safe component that a |
| CVE-2026-105436 | 8.8 | 2026-10-08 | Deserialization of Untrusted Data vulnerability in MainWP MainWP Child mainwp-child allows Object Injection.This issue a |
| CVE-2026-107295 | 7.6 | 2026-10-08 | Pydantic AI is a Python agent framework for building applications and workflows with Generative AI. From 1.34.0 until 1. |
| CVE-2026-107300 | 7.5 | 2026-10-08 | msgpack5 is a msgpack v5 implementation for node.js and the browser. Prior to 6.1.0, the streaming decoder recursively i |
| CVE-2026-107709 | 7.8 | 2026-10-08 | A path traversal vulnerability exists in Bower decompress-zip through version 0.3.3. The vulnerability located in `lib/d |
| CVE-2026-50054 | 7.1 | 2026-10-08 | An authorization flaw in Zimbra Collaboration Suite’s GrantRightsRequest allows an attacker with access to an authentica |
| CVE-2026-107302 | 7.5 | 2026-10-08 | msgpack5 is a msgpack v5 implementation for node.js and the browser. Prior to 6.1.0, the decoder reads the four-byte len |
| CVE-2026-107303 | 7.6 | 2026-10-08 | JHipster is a development platform to quickly generate, develop, and deploy modern web applications and microservice arc |
| CVE-2026-107333 | 8.1 | 2026-10-08 | Malcolm's nginx based reverse proxy contains a URL path normalization inconsistency between its Lua based role-based acc |
| CVE-2026-107337 | 7.1 | 2026-10-08 | The Malcolm kiosk Flask application exposes a POST /script_call/<script> endpoint with zero authentication and wildcard  |
| CVE-2026-107362 | 7.1 | 2026-10-08 | Malcolm file-upload component ships the upstream FilePond PHP server (pqina/filepond-server-php) largely unmodified: Doc |
| CVE-2026-107375 | 8.8 | 2026-10-08 | JHipster is a development platform to quickly generate, develop, and deploy modern web applications and microservice arc |
| CVE-2026-107376 | 8.2 | 2026-10-08 | webonyx graphql-php is a PHP implementation of the GraphQL specification. Prior to 15.32.3, GraphQL\Language\Parser perf |
| CVE-2026-107377 | 7.5 | 2026-10-08 | datamodel-code-generator generates Python data models from schema definitions. From 0.59.0 until 0.81.0, an attacker-con |
| CVE-2026-95184 | 7.5 | 2026-10-08 | Improper certificate validation in gnutls v3.8.13 causes the application to reject legitimate certificates for valid use |
| CVE-2026-95210 | 9.1 | 2026-10-08 | Improper certificate validation in gnutls v3.8.13 causes the application to accept certificates containing invalid exten |
| CVE-2026-106433 | 8.8 | 2026-10-08 | Improper state management in MongoDB libmongocrypt can cause provider-specific data to be treated as an incompatible typ |
| CVE-2026-107322 | 7.8 | 2026-10-08 | An incomplete list of disallowed inputs in Amazon Agent Plugins for AWS databases-on-aws plugin before 1.7.1 might allow |
| CVE-2026-107383 | 7.5 | 2026-10-08 | MariaDB Connector/Node.js is used to connect applications developed on Node.js to MariaDB and MySQL databases. Prior to  |
| CVE-2026-107384 | 8.1 | 2026-10-08 | MariaDB Connector/Node.js is used to connect applications developed on Node.js to MariaDB and MySQL databases. From 3.2. |
| CVE-2026-107385 | 7.4 | 2026-10-08 | MariaDB Connector/Node.js is used to connect applications developed on Node.js to MariaDB and MySQL databases. Prior to  |
| CVE-2026-107699 | 9.8 | 2026-10-08 | ppt2png through 0.0.6 contains an OS command injection vulnerability that allows attackers to execute operating system c |
| CVE-2026-107700 | 9.8 | 2026-10-08 | dot-access 0.0.3 through 1.0.0 contains a code injection vulnerability that allows remote attackers to execute JavaScrip |
| CVE-2026-107701 | 8.2 | 2026-10-08 | dot-access through 1.0.0 contains a prototype pollution vulnerability that allows attackers to modify Object.prototype b |
| CVE-2026-107703 | 9.8 | 2026-10-08 | @enmaso/node-convert through 1.0.0 contains an OS command injection vulnerability in convert.js that allows attackers to |
| CVE-2026-107704 | 9.8 | 2026-10-08 | The image_optimizer Ruby gem 1.3.0 through 1.9.0 contains an OS command injection vulnerability in ImageOptimizer#identi |
| CVE-2026-40804 | 7.1 | 2026-10-08 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Kodezen LLC aBlock |
| CVE-2026-67693 | 7.5 | 2026-10-08 | An issue in gnutls v.3.8.13 allows an attacker to obtain sensitive information via failing to reject end-entity X.509 ce |
| CVE-2026-84276 | 7.5 | 2026-10-08 | IBM Guardium Data Protection 12.2.2 is affected by a denial-of-service vulnerability in the edge-controller. An unauthen |
| CVE-2026-84278 | 7.2 | 2026-10-08 | IBM Guardium Data Protection 12.2 is affected by a command injection vulnerability in the SUID-root ssh_config_wrapper c |
| CVE-2026-95209 | 7.5 | 2026-10-08 | An issue in gnutls v3.8.13 causes legitimate CA certificates to be rejected, leading to a Denial of Service (DoS). |
| CVE-2026-104075 | 9.8 | 2026-10-08 | TVU Networks Receiver/Transceiver devices running firmware before version 7.9 contain an authentication bypass vulnerabi |
| CVE-2026-104076 | 9.1 | 2026-10-08 | TVU Networks Receiver/Transceiver devices running firmware before version 7.9 contain a missing authentication vulnerabi |
| CVE-2026-106126 | 9.9 | 2026-10-08 | A command injection vulnerability in the Active Directory Events Listener of Tenable Identity Exposure (SaaS) allows an  |
| CVE-2026-107707 | 7.8 | 2026-10-08 | Intego Antivirus for Windows through 3.0.0.1 contains a link following vulnerability in its optimization module that all |
| CVE-2026-82334 | 8.1 | 2026-10-08 | IBM Guardium Data Protection 12.0, 12.1, 12.2 is vulnerable to a heap-based out-of-bounds read in the TDS7 LOGIN7 protoc |
| CVE-2026-82335 | 8.1 | 2026-10-08 | IBM Guardium Data Protection 12.0, 12.1, 12.2 is vulnerable to a heap-based buffer overflow in the MongoDB protocol pars |
| CVE-2026-82344 | 8.1 | 2026-10-08 | IBM Guardium Data Protection 12.0, 12.1 is vulnerable to a heap-based buffer overflow in the S-TAP TrafficTap TDS login  |
| CVE-2026-84244 | 9.3 | 2026-10-08 | IBM Guardium Data Protection 12.2 IBM Security Guardium Data Protection is vulnerable to stored cross-site scripting (XS |
| CVE-2026-84245 | 7.8 | 2026-10-08 | IBM Guardium Data Protection 12.2 is vulnerable to a local privilege escalation in the cp_wrapper component. A low-privi |
| CVE-2026-84250 | 8.4 | 2026-10-08 | IBM Guardium Data Protection 12.2 is vulnerable due to weak cryptographic protection and a hard-coded recovery key in th |
| CVE-2026-84271 | 7.8 | 2026-10-08 | IBM Guardium Data Protection 12.2 is vulnerable to a signature verification bypass in the patch installer. An attacker w |
| CVE-2026-84272 | 9.8 | 2026-10-08 | IBM Guardium Data Protection 12.1 and 12.2.2 are vulnerable to missing authentication in the edge-controller component.  |
| CVE-2026-84275 | 7.5 | 2026-10-08 | IBM Guardium Data Protection 12.2 is vulnerable to path traversal in the GIM file-upload functionality. An unauthenticat |
| CVE-2026-101024 | 8.8 | 2026-10-08 | Satel Netco Design versions prior to v2.1.7 contains a relative path traversal vulnerability in its data export function |
| CVE-2026-107318 | 7.4 | 2026-10-08 | @fastify/reply-from is a Fastify plugin that forwards requests to an upstream HTTP or HTTPS server. In versions prior to |
| CVE-2026-107779 | 9.8 | 2026-10-08 | Dromara Skyeye through commit 003549ae5615bd114ba5bb8ddf6a8e8ead97c321 contains a missing authentication vulnerability i |
| CVE-2026-107780 | 9.8 | 2026-10-08 | Dromara Skyeye through commit 003549ae5615bd114ba5bb8ddf6a8e8ead97c321 contains an OS command injection vulnerability in |
| CVE-2026-107781 | 7.4 | 2026-10-08 | Dromara Skyeye through commit 003549ae5615bd114ba5bb8ddf6a8e8ead97c321 contains a server-side request forgery and missin |
| CVE-2026-107782 | 7.8 | 2026-10-08 | System Informer before 4.0.26241.138 contains an incorrect authorization vulnerability in the phsvc helper that allows l |
| CVE-2026-11318 | 7.8 | 2026-10-08 | Deskin through 3.3.4.3 contains a privilege escalation vulnerability in the com.deskin.service.installer XPC service tha |
| CVE-2026-16823 | 9.1 | 2026-10-08 | IBM Security Verify Access 10.0 through 10.0.9.2 and IBM Verify Identity Access 11.0 through 11.0.3 could allow a remote |
| CVE-2026-16916 | 9.1 | 2026-10-08 | IBM Security Verify Access 10.0 through 10.0.9.2 and IBM Verify Identity Access 11.0 through 11.0.3 could allow a remote |
| CVE-2026-17189 | 8.2 | 2026-10-08 | IBM Security Verify Access 10.0 through 10.0.9.2 and IBM Verify Identity Access 11.0 through 11.0.3 is vulnerable to cro |
| CVE-2026-18740 | 8.8 | 2026-10-08 | IBM Security Verify Access 10.0 through 10.0.9.2 and IBM Verify Identity Access 11.0 through 11.0.3 could allow a remote |
| CVE-2026-19482 | 8.8 | 2026-10-08 | IBM Security Verify Access 10.0 through 10.0.9.2 and IBM Verify Identity Access 11.0 through 11.0.3 could allow a remote |
| CVE-2026-19491 | 9.1 | 2026-10-08 | IBM Security Verify Access 10.0 through 10.0.9.2 and IBM Verify Identity Access 11.0 through 11.0.3 could allow a remote |
| CVE-2026-19493 | 7.5 | 2026-10-08 | IBM Security Verify Access 10.0 through 10.0.9.2 and IBM Verify Identity Access 11.0 through 11.0.3 could allow a remote |
| CVE-2026-19494 | 8.1 | 2026-10-08 | IBM Security Verify Access 10.0 through 10.0.9.2 and IBM Verify Identity Access 11.0 through 11.0.3 could allow a remote |
| CVE-2026-78401 | 9.8 | 2026-10-08 | IBM Security Verify Access 10.0 through 10.0.9.2 and IBM Verify Identity Access 11.0 through 11.0.3 could allow a remote |
| CVE-2026-78406 | 9.8 | 2026-10-08 | IBM Security Verify Access 10.0 through 10.0.9.2 and IBM Verify Identity Access 11.0 through 11.0.3 could allow a remote |
| CVE-2026-79842 | 9.1 | 2026-10-08 | An authentication bypass vulnerability exists in HPE Intelligent Management Center (iMC) prior to v7.3 E0713 |
| CVE-2026-107720 | 7.4 | 2026-10-08 | fast-jwt provides fast JSON Web Token (JWT) implementation. Prior to 6.3.1, fast-jwt createVerifier accepts an unsigned  |
| CVE-2026-107722 | 9.8 | 2026-10-08 | fast-jwt provides fast JSON Web Token (JWT) implementation. From 6.2.0 until 6.3.0, fast-jwt can misclassify RSA public- |
| CVE-2026-107723 | 8.1 | 2026-10-08 | fast-jwt provides fast JSON Web Token (JWT) implementation. Prior to 6.3.0, fast-jwt createVerifier accepts a validly si |
| CVE-2026-107724 | 7.4 | 2026-10-08 | fast-jwt provides fast JSON Web Token (JWT) implementation. In 6.2.4, fast-jwt can classify raw serialized public JWK or |
| CVE-2026-75875 | 9.8 | 2026-10-08 | IBM Guardium Data Protection 12.0, 12.1, and 12.2 could allow a remote attacker to execute arbitrary code due to path tr |
| CVE-2026-80381 | 9.8 | 2026-10-08 | IBM Guardium Data Protection 12.0, 12.1, and 12.2 could allow a remote attacker to execute unauthorized SQL statements d |
| CVE-2026-81932 | 8.6 | 2026-10-08 | IBM Guardium Data Protection 12.0, 12.1, and 12.2 is vulnerable to SQL injection. A remote unauthenticated attacker coul |
| CVE-2026-82895 | 8.1 | 2026-10-08 | IBM Guardium Data Protection 12.0, 12.1, and 12.2 could allow a remote attacker to execute arbitrary code due to a buffe |
| CVE-2026-82900 | 8.1 | 2026-10-08 | IBM Guardium Data Protection 12.2.2, and 12.1 could allow a remote attacker to delete arbitrary files due to improper li |
| CVE-2026-84035 | 8.1 | 2026-10-08 | IBM Guardium Data Protection 12.0, 12.1, and 12.2 could allow a remote attacker to execute arbitrary code due to a stack |
| CVE-2026-84057 | 8.1 | 2026-10-08 | IBM Guardium Data Protection 12.2.2, and 12.1 could allow a remote attacker to execute arbitrary commands due to imprope |
| CVE-2026-84058 | 8.1 | 2026-10-08 | IBM Guardium Data Protection 12.0, 12.1, and 12.2 is vulnerable to a buffer overrun in the TDS (Microsoft SQL Server) PR |
| CVE-2026-84198 | 8.1 | 2026-10-08 | IBM Guardium Data Protection 12.0, 12.1, and 12.2 could allow a remote attacker to execute arbitrary code due to a buffe |
| CVE-2026-84209 | 8.1 | 2026-10-08 | IBM Guardium Data Protection 12.2.2, and 12.1 could allow a remote attacker to execute arbitrary SQL commands due to imp |
| CVE-2026-84230 | 7.5 | 2026-10-08 | IBM Guardium Data Protection 12.2.2 could allow a remote attacker to cause a denial of service due to a race condition r |
| CVE-2026-84246 | 8.1 | 2026-10-08 | IBM Guardium Data Protection 12.0, 12.1, and 12.2 could allow a remote attacker to execute arbitrary code due to a buffe |
| CVE-2026-84247 | 8.1 | 2026-10-08 | IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to cause a denial of service due to a path |
| CVE-2026-84249 | 9.8 | 2026-10-08 | IBM Guardium Data Protection 12.2, and 12.2.2 could allow a remote attacker to execute arbitrary management operations d |
| CVE-2026-84875 | 7.5 | 2026-10-08 | IBM Guardium Data Protection 12.0, 12.1, and 12.2 could allow a remote attacker to execute arbitrary code due to a buffe |
| CVE-2026-89091 | 8.8 | 2026-10-08 | A flaw was found in ansible-core. When installing a collection with
`ansible-galaxy collection install`, the archive ext |
| CVE-2026-107728 | 7.5 | 2026-10-08 | Strawberry GraphQL is a library for creating GraphQL APIs. From 0.217.0 until 0.326.1, PermissionExtension.resolve() on  |
| CVE-2026-69435 | 9.6 | 2026-10-08 | Missing authorization in Azure SRE Agent allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-77900 | 9.8 | 2026-10-08 | Missing authentication for critical function in Azure App Service allows an unauthorized attacker to execute code over a |
| CVE-2026-83943 | 8.7 | 2026-10-08 | Exposure of sensitive information to an unauthorized actor in Azure API Center allows an unauthorized attacker to disclo |
| CVE-2026-83947 | 7.7 | 2026-10-08 | Missing authorization in Azure Event Grid allows an authorized attacker to perform spoofing over a network. |
| CVE-2026-88131 | 9.8 | 2026-10-08 | Deserialization of untrusted data in Microsoft Dataverse allows an unauthorized attacker to execute code over a network. |
| CVE-2026-94510 | 9.9 | 2026-10-08 | Authorization bypass through user-controlled key in Microsoft Bookings allows an unauthorized attacker to elevate privil |
| CVE-2026-96207 | 10.0 | 2026-10-08 | Improper certificate validation in Microsoft Partner Center allows an unauthorized attacker to elevate privileges over a |
| CVE-2026-5759 | 9.8 | 2026-10-09 | A double free and use-after-free vulnerability in the RdbLoadDeletedNodes function of the RDB graph decoders (src/serial |
| CVE-2026-7826 | 9.1 | 2026-10-09 | A heap-based out-of-bounds read in the BufferSerializerIOv2_ReadBuffer function (src/serializers/serializer_io.c) in Fal |
| CVE-2026-7827 | 8.1 | 2026-10-09 | A stack-based buffer overflow in the _RdbLoadEntity function of the RDB graph decoders (src/serializers/decoders/*/decod |
| CVE-2026-107908 | 9.8 | 2026-10-09 | A heap-based out-of-bounds write in the BoltReadHandler function (src/bolt/bolt_api.c) in FalkorDB before 4.20.0 allows  |
| CVE-2026-107909 | 9.1 | 2026-10-09 | A heap-based out-of-bounds write in the ws_read_frame function (src/bolt/ws.c) and the buffer_apply_mask function (src/b |
| CVE-2026-107910 | 8.1 | 2026-10-09 | An improper authentication vulnerability in the is_authenticated function (src/bolt/bolt_api.c) in FalkorDB before 4.20. |
| CVE-2026-107911 | 7.5 | 2026-10-09 | A type confusion vulnerability in the _read_flags function (src/commands/cmd_dispatcher.c) in FalkorDB before 4.20.0 all |
| CVE-2026-107914 | 7.8 | 2026-10-09 | Backdrop CMS 1.34 before 1.34.5 and 1.35 before 1.35.1 doesn't sufficiently protect configuration exports when deliverin |
| CVE-2026-81929 | 7.2 | 2026-10-09 | The Ocean Pro Demos and Ocean eComm Treasure Box plugins for WordPress is vulnerable to Stored Cross-Site Scripting via  |
| CVE-2026-97076 | 7.5 | 2026-10-09 | Executable Regular Expression Error vulnerability in WP Media WP Rocket wp-rocket allows Code Injection.This issue affec |
| CVE-2026-106145 | 7.1 | 2026-10-09 | In Progress® Telerik® Report Server prior to version 12.2.26.1007, incorrect privilege assignment in the service-agent S |
| CVE-2026-106155 | 8.9 | 2026-10-09 | In Progress® Telerik® Report Server prior to version 12.2.26.1007, a stored cross-site scripting vulnerability in the sh |
| CVE-2026-19569 | 8.8 | 2026-10-09 | dynamic_object_create() in kernel/userspace/userspace.c computed the backing allocation for a dynamically allocated kern |
| CVE-2026-19570 | 8.8 | 2026-10-09 | The LE Audio Broadcast Sink in subsys/bluetooth/audio/bap_broadcast_sink.c copies subgroup metadata from a received Basi |
| CVE-2026-19574 | 7.0 | 2026-10-09 | The ARM64 MMU back-end allocated address space identifiers (ASIDs) for memory domains with a bare round-robin counter in |
| CVE-2026-19575 | 7.8 | 2026-10-09 | The user-mode verification handler for the device_deinit() system call, z_vrfy_device_deinit() in kernel/device.c, valid |
| CVE-2026-76779 | 7.4 | 2026-10-09 | Dell Secure Connect Gateway (SCG) Policy Manager, versions prior to 5.34.00.16, contains an Improper Restriction of Exce |
| CVE-2026-78019 | 7.5 | 2026-10-09 | Dell Secure Connect Gateway (SCG) Policy Manager, versions prior to 5.34.00.16, contains an Inclusion of Functionality f |
| CVE-2026-78020 | 7.5 | 2026-10-09 | Dell Secure Connect Gateway (SCG) Policy Manager, versions prior to 5.34.00.16, contains an Improper Certificate Validat |
| CVE-2026-107935 | 9.3 | 2026-10-09 | A path traversal vulnerability was found in gvproxy, the network forwarder provided by the gvisor-tap-vsock package. The |
| CVE-2026-78023 | 7.1 | 2026-10-09 | Dell Secure Connect Gateway (SCG) Policy Manager, versions prior to 5.34.00.16, contains an Authorization Bypass Through |
| CVE-2026-78024 | 7.7 | 2026-10-09 | Dell Secure Connect Gateway (SCG) Policy Manager, versions prior to 5.34.00.16, contains a Server-Side Request Forgery ( |
| CVE-2026-78025 | 7.5 | 2026-10-09 | Dell Secure Connect Gateway (SCG) Policy Manager, versions prior to 5.34.00.16, contains a Missing Authentication for Cr |
| CVE-2026-93947 | 9.3 | 2026-10-09 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Shinetheme Travele |
| CVE-2026-94158 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in bkninja Gloria Adm |
| CVE-2026-94159 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in KlbTheme Total Don |
| CVE-2026-94161 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in ThemeGoods Grand R |
| CVE-2026-94166 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in UpSolution UpSolut |
| CVE-2026-94167 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Extend Themes Kubi |
| CVE-2026-94170 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Heateor Support Sa |
| CVE-2026-94415 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Muffingroup Bethem |
| CVE-2026-94503 | 10.0 | 2026-10-09 | Unrestricted Upload of File with Dangerous Type vulnerability in PX-lab Zombify zombify allows Upload a Web Shell to a W |
| CVE-2026-94568 | 7.2 | 2026-10-09 | Deserialization of Untrusted Data vulnerability in WP Hosting AS Pay with Vipps for WooCommerce woo-vipps allows Object  |
| CVE-2026-94632 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Stiofan BlockStrap |
| CVE-2026-94641 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Stiofan UsersWP us |
| CVE-2026-94661 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Crocoblock JetBlog |
| CVE-2026-94663 | 8.5 | 2026-10-09 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Metagauss ProfileG |
| CVE-2026-94664 | 7.5 | 2026-10-09 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in add-ons.org PDF for Cont |
| CVE-2026-94666 | 7.5 | 2026-10-09 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in ZealousWeb Generate PDF  |
| CVE-2026-94668 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Dimitri Grassi Sal |
| CVE-2026-95591 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in e4jvikwp VikBookin |
| CVE-2026-95596 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Mamunur Rashid Sho |
| CVE-2026-95598 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in codepeople Search  |
| CVE-2026-95599 | 8.5 | 2026-10-09 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Taskbuilder Taskbu |
| CVE-2026-95607 | 8.5 | 2026-10-09 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in VibeThemes WPLMS   |
| CVE-2026-95608 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in PluginUs.Net HUSKY |
| CVE-2026-95609 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in David Lingren Medi |
| CVE-2026-95610 | 8.5 | 2026-10-09 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in UpSolution UpSolut |
| CVE-2026-96327 | 9.3 | 2026-10-09 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in VibeThemes WPLMS w |
| CVE-2026-96328 | 9.3 | 2026-10-09 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in jegtheme JNews - P |
| CVE-2026-96329 | 8.5 | 2026-10-09 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in tagDiv tagDiv Opt- |
| CVE-2026-96330 | 9.3 | 2026-10-09 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in tagDiv tagDiv Opt- |
| CVE-2026-96331 | 9.3 | 2026-10-09 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in wpdreams Ajax Sear |
| CVE-2026-96332 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in yalla ya! Simple P |
| CVE-2026-96333 | 7.5 | 2026-10-09 | Authentication Bypass by Spoofing vulnerability in Liquid Web / StellarWP GiveWP give allows Identity Spoofing.This issu |
| CVE-2026-96336 | 7.5 | 2026-10-09 | Authentication Bypass by Spoofing vulnerability in WPMU DEV Forminator forminator allows Identity Spoofing.This issue af |
| CVE-2026-96461 | 7.5 | 2026-10-09 | Missing Authorization vulnerability in TMS Amelia ameliabooking allows Exploiting Incorrectly Configured Access Control  |
| CVE-2026-96553 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Damian Góra FiboSe |
| CVE-2026-96607 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Basix NEX-Forms ne |
| CVE-2026-96671 | 8.8 | 2026-10-09 | Cross-Site Request Forgery (CSRF) vulnerability in fifu.app Featured Image from URL featured-image-from-url allows Cross |
| CVE-2026-96761 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Welcart Welcart e- |
| CVE-2026-96809 | 9.3 | 2026-10-09 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in MultiNet Interacti |
| CVE-2026-103412 | 8.8 | 2026-10-09 | Improper limitation of a pathname to a restricted directory ('path traversal') vulnerability in Apache Camel Karavan.


 |
| CVE-2026-103413 | 8.8 | 2026-10-09 | Improper input validation vulnerability in Apache Camel Karavan.



When a deployment was started, Karavan unmarshalled  |
| CVE-2026-104392 | 8.8 | 2026-10-09 | Deserialization of Untrusted Data vulnerability in ExpressTech Quiz And Survey Master quiz-master-next allows Object Inj |
| CVE-2026-105318 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Datasolution AcyMa |
| CVE-2026-105870 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Delight Star Inc.  |
| CVE-2026-105872 | 7.2 | 2026-10-09 | Deserialization of Untrusted Data vulnerability in mklacroix Product Configurator for WooCommerce product-configurator-f |
| CVE-2026-105883 | 7.1 | 2026-10-09 | Missing Authorization vulnerability in ThemeHunk Th Shop Mania th-shop-mania allows Exploiting Incorrectly Configured Ac |
| CVE-2026-85531 | 9.8 | 2026-10-09 | Improper verification of cryptographic signature vulnerability in Sipay Electronic Money and Payment Services Inc. OpenC |
| CVE-2026-86405 | 9.8 | 2026-10-09 | Improper verification of cryptographic signature vulnerability in Sipay Electronic Money and Payment Services Inc. Prest |
| CVE-2026-94058 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Bracketweb Treck t |
| CVE-2026-94059 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Bracketweb Ogency  |
| CVE-2026-94060 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Bracketweb Voldor  |
| CVE-2026-94061 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Designthemes Whist |
| CVE-2026-94062 | 8.1 | 2026-10-09 | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability in |
| CVE-2026-100730 | 9.8 | 2026-10-09 | A service console interface on openPDC and openHistorian deserializes a client-supplied data structure. On systems using |
| CVE-2026-104629 | 8.8 | 2026-10-09 | A component loading mechanism in openPDC and openHistorian will construct and run any specified type, which may be an in |
| CVE-2026-105281 | 7.5 | 2026-10-09 | The internal data publisher on openPDC accepts network connections without authentication in its default configuration.  |
| CVE-2026-62026 | 7.1 | 2026-10-09 | Cross-Site Request Forgery (CSRF) vulnerability in MIGHTYminnow Dashboard Notes dashboard-notes allows Cross Site Reques |
| CVE-2026-94063 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in ThemeREX Education |
| CVE-2026-94064 | 8.8 | 2026-10-09 | Deserialization of Untrusted Data vulnerability in BuddhaThemes Neo \| Barber Shop WordPress Theme neocut allows Object I |
| CVE-2026-94065 | 8.8 | 2026-10-09 | Deserialization of Untrusted Data vulnerability in BuddhaThemes ColorFolio colorit allows Object Injection.This issue af |
| CVE-2026-94066 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in SpabRice Pond pond |
| CVE-2026-94067 | 8.1 | 2026-10-09 | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability in |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2015-5477 | ISC / BIND | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2016-3081 | Apache / Struts | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2023-22894 | Strapi / Strapi | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2021-3199 | ONLYOFFICE / Docs | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2015-3306 | ProFTPD / ProFTPD | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2026-88779 | Citrix / NetScaler | 2026-10-04 | 2026-10-07 | Unknown |
| CVE-2026-102490 | Zammad GmbH / Zammad | 2026-10-02 | 2026-10-05 | Unknown |
| CVE-2026-102489 | Zammad GmbH / Zammad | 2026-10-02 | 2026-10-05 | Unknown |

---

*Total entries in CISA KEV catalog: 1739*