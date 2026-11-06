# Vulnerability Intelligence Report

**Date:** 2026-11-06  
**Generated:** 2026-11-06T15:40:08Z  

---

## Executive Summary

Our environment faces significant exposure across 203 high-severity CVEs, with four newly added CISA Known Exploited Vulnerabilities (KEVs) demanding immediate attention. Critical findings include an OpenSSH authentication bypass, a ModSecurity WAF engine flaw, and unauthenticated API access in Metasploit. Two Ivanti Connect Secure vulnerabilities and a WordPress Core flaw are actively exploited in the wild. While no monitored CVEs currently appear in the KEV catalog, the breadth of high-severity findings across foundational infrastructure components—databases, web servers, authentication libraries, and VPN gateways—represents substantial organizational risk requiring urgent prioritization and coordinated remediation.

---

## Risk Narrative

The current threat landscape reflects adversaries actively exploiting foundational infrastructure vulnerabilities, particularly in VPN gateways, CMS platforms, and authentication systems. The four new KEV entries signal real-world weaponization, with Ivanti Connect Secure remaining a persistent high-value target for nation-state and ransomware actors. The OpenSSH and ModSecurity vulnerabilities threaten perimeter security controls, while the MariaDB and musl libc flaws expose core backend systems. An unauthenticated Metasploit API creates significant lateral movement risk if exploited internally. Collectively, these vulnerabilities increase the probability of data breach, service disruption, and ransomware deployment, with potential regulatory, reputational, and financial consequences for the organization.

---

## Prioritized Action Items

1. Immediately patch or mitigate all four CISA KEV entries, prioritizing the two Ivanti Connect Secure vulnerabilities (CVE-2026-118527, CVE-2026-111357) due to confirmed active exploitation.
2. Apply emergency patches for the OpenSSH authentication bypass (CVE-2026-123158) and ModSecurity WAF engine flaw (CVE-2026-104269) to protect critical authentication and perimeter defense infrastructure.
3. Remediate the Metasploit unauthenticated REST API vulnerability (CVE-2026-121139) by enforcing authentication controls and isolating the service from untrusted networks.
4. Conduct a full audit and patching cycle for the remaining 200 high-severity CVEs, prioritizing internet-facing and critical infrastructure components such as MariaDB and musl libc.
5. Establish continuous KEV monitoring and a mandatory 72-hour remediation SLA for any future CVEs added to the CISA KEV catalog affecting organizational assets.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-102523 | 8.0 | 2026-11-05 | MariaDB server is a community developed fork of MySQL server. From 10.11.1 until 10.11.19, 11.4.13, 11.8.9, 12.3.3, and  |
| CVE-2026-102615 | 7.6 | 2026-11-05 | HeyForm is an open-source form builder. Prior to 3.0.1, /api/upload accepts a file according to the client-controlled mu |
| CVE-2026-104269 | 8.6 | 2026-11-05 | ModSecurity is an open source, cross platform web application firewall (WAF) engine for Apache, IIS and Nginx. From 3.0. |
| CVE-2026-107891 | 8.1 | 2026-11-05 | musl libc before 1.2.7, when an untrusted regular expression is used with regcomp, has multiple integer overflows, possi |
| CVE-2026-121139 | 7.8 | 2026-11-05 | The Rapid7 Metasploit msf-ws suffers from a missing authentication vulnerability whereby the REST API grants an unauthen |
| CVE-2026-122328 | 7.8 | 2026-11-05 | SDL_mixer 3.1.2 through 3.2.4 contains a stack-based buffer overflow vulnerability in FetchXLaw() of src/decoder_wav.c w |
| CVE-2026-122329 | 7.8 | 2026-11-05 | SDL_mixer 3.1.2 through 3.2.4 contains a stack-based buffer overflow in FetchXLaw() in src/decoder_aiff.c due to miscalc |
| CVE-2026-123095 | 7.5 | 2026-11-05 | mpv 0.29.0 before 0.42.0 contains a playlist injection vulnerability in the bundled ytdl_hook script that allows remote  |
| CVE-2026-123158 | 8.1 | 2026-11-05 | sshd in OpenSSH before 10.6p2 on Linux, when musl libc is used without PAM, lacks a workaround for a password authentica |
| CVE-2026-70659 | 7.8 | 2026-11-05 | stable-diffusion.cpp is a pure C/C++ library for running diffusion model (Stable Diffusion, Flux, Wan, Qwen Image, Z-Ima |
| CVE-2026-73856 | 8.6 | 2026-11-05 | ModSecurity is an open source, cross platform web application firewall (WAF) engine for Apache, IIS and Nginx. From 3.0. |
| CVE-2026-102739 | 7.8 | 2026-11-05 | ESPectre is a Wi-Fi motion sensing platform for ESP32. Prior to 3.0.0-rc1, Micro-ESPectre analysis tools, including tool |
| CVE-2026-103112 | 7.5 | 2026-11-05 | A flaw was found in the authentication session handling of the keycloak-services component in Keycloak. The issue occurs |
| CVE-2026-107123 | 7.5 | 2026-11-05 | A flaw was found in the SAML XML processing component of Keycloak, an open-source identity and access management solutio |
| CVE-2026-107602 | 7.5 | 2026-11-05 | A flaw was found in the SAML 1.1 XML parsing logic of Keycloak, an open-source identity and access management solution.  |
| CVE-2026-110931 | 7.5 | 2026-11-05 | A flaw was found in the SAML 1.1 assertion parser of Keycloak, a tool used for identity and access management. The issue |
| CVE-2026-110932 | 7.5 | 2026-11-05 | A flaw was found in the theme resource endpoint of Keycloak, an open-source identity and access management solution. The |
| CVE-2026-112208 | 8.1 | 2026-11-05 | A flaw was found in the Organization identity-first login flow of the Keycloak authentication server. Keycloak is an ope |
| CVE-2026-114232 | 8.1 | 2026-11-05 | A flaw was found in the UserManagedPermissionService of the Keycloak authorization server. The UMA Protection API, which |
| CVE-2026-119083 | 7.8 | 2026-11-05 | Path traversal in the archive extraction utility in GluonTS before 0.17.0 might allow an actor who supplies a crafted ta |
| CVE-2026-120499 | 7.8 | 2026-11-05 | h5io before 0.2.6 contains a code injection vulnerability in read_hdf5() that allows attackers to execute arbitrary code |
| CVE-2026-121994 | 8.8 | 2026-11-05 | A stack buffer overflow in the GDB client's remote protocol handler allows an attacker-controlled debug target to execut |
| CVE-2026-121995 | 7.5 | 2026-11-05 | A stack buffer overflow in the GDB client's tracepoint upload handler allows an attacker-controlled debug stub to corrup |
| CVE-2026-121996 | 8.2 | 2026-11-05 | A length validation flaw in gdbserver's agent-expression parser allows an unauthenticated remote attacker to read uninit |
| CVE-2026-121997 | 8.1 | 2026-11-05 | A heap buffer overflow in gdbserver's QTDPsrc packet handler allows an unauthenticated remote attacker to achieve native |
| CVE-2026-123151 | 7.5 | 2026-11-05 | A flaw was found in the GNU debugger (GDB). When GDB connects to a remote debug target, a malicious target can cause GDB |
| CVE-2026-49393 | 8.4 | 2026-11-05 | OpenHuman is an open-source agent harness available as a desktop application and Rust library. Before 0.56.0, the core s |
| CVE-2026-49407 | 7.7 | 2026-11-05 | OpenHuman is an open-source agent harness available as a desktop application and Rust library. Before version 0.57.44, i |
| CVE-2026-54140 | 8.3 | 2026-11-05 | OpenHuman is an open-source agent harness available as a desktop application and Rust library. Before 0.57.13, OpenHuman |
| CVE-2026-54141 | 9.0 | 2026-11-05 | OpenHuman is an open-source agent harness available as a desktop application and Rust library. Before 0.57.13, a remote  |
| CVE-2026-54142 | 8.7 | 2026-11-05 | OpenHuman is an open-source agent harness available as a desktop application and Rust library. Before 0.57.13, backgroun |
| CVE-2026-54143 | 9.8 | 2026-11-05 | OpenHuman is an open-source agent harness available as a desktop application and Rust library. Before version 0.57.13, a |
| CVE-2026-54145 | 8.8 | 2026-11-05 | OpenHuman is an open-source agent harness available as a desktop application and Rust library. In affected versions befo |
| CVE-2026-54146 | 8.8 | 2026-11-05 | OpenHuman is an open-source agent harness available as a desktop application and Rust library. From 0.53.15 before 0.57. |
| CVE-2026-75614 | 8.1 | 2026-11-05 | ASN1SCC is an open source ASN.1 compiler for embedded systems. Prior to 4.7.0.1, BitStream_DecodeConstraintWholeNumber i |
| CVE-2026-76077 | 8.1 | 2026-11-05 | ASN1SCC is an open source ASN.1 compiler for embedded systems. Prior to 4.7.0.1, the XER tokenizer NT() in asn1crt/asn1c |
| CVE-2026-82413 | 8.8 | 2026-11-05 | ntopng is a web-based network traffic monitoring application. Prior to 6.7.260717, scripts/lua/rest/v2/add/host/to_scan. |
| CVE-2026-82965 | 7.5 | 2026-11-05 | A flaw was found in the SAML implementation of Keycloak, an open-source identity and access management solution. The SAM |
| CVE-2026-105607 | 8.3 | 2026-11-05 | Joomla Extension - balbooa.com - Unauthenticated stored XSS in the "Recent Comments / Recent Reviews" widget in Gridbox  |
| CVE-2026-107903 | 8.3 | 2026-11-05 | Joomla Extension - balbooa.com - Stored XSS in reviews via inconsistent sanitization in Gridbox < 2.20.5.0 |
| CVE-2026-112109 | 7.0 | 2026-11-05 | A local privilege escalation vulnerability in Thales SafeNet Authentication Client (SAC) SACSrv can allow an authenticat |
| CVE-2026-120859 | 7.8 | 2026-11-05 | PyMoDAQ before 4.4.13, and pymodaq_data, pymodaq_gui, and pymodaq_utils before 5.1.15, 5.2.x before 5.2.14, and 5.3.x be |
| CVE-2026-123184 | 8.1 | 2026-11-05 | An incorrect authorization vulnerability exists in the Altium 365 Git Service. The permission check performed when a use |
| CVE-2026-77439 | 8.8 | 2026-11-05 | Immich is a self-hosted photo and video management solution. Prior to 3.0.3, an authenticated user with editor access to |
| CVE-2026-92855 | 7.4 | 2026-11-05 | A flaw was found in the SAML identity broker component of Keycloak, which is used to delegate authentication to external |
| CVE-2026-92857 | 8.1 | 2026-11-05 | Keycloak provides a Dynamic Client Registration feature that allows users with specific tokens to register their own app |
| CVE-2026-93998 | 7.4 | 2026-11-05 | A flaw was found in the SAML adapter component of Keycloak, which is used to secure applications with SAML-based authent |
| CVE-2026-96453 | 8.0 | 2026-11-05 | A flaw was found in the Keycloak Admin CLI kcadm tool, which is used by administrators to manage Keycloak servers from t |
| CVE-2026-97175 | 8.8 | 2026-11-05 | A flaw was found in the idp-auto-link authenticator of the keycloak-services component, which handles user identity fede |
| CVE-2026-97847 | 7.1 | 2026-11-05 | A flaw was found in the protocol mapper and identity resolution components of Keycloak. The issue occurs when a client m |
| CVE-2026-100361 | 7.1 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-100363 | 8.8 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-100364 | 7.1 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-100365 | 8.8 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-123196 | 8.1 | 2026-11-05 | Authorizer before 2.4.2 contains a password reset poisoning vulnerability that allows unauthenticated attackers to contr |
| CVE-2026-123198 | 9.8 | 2026-11-05 | LMFDB before commit 01829bd contains a server-side template injection vulnerability in the render_knowl function that al |
| CVE-2026-123200 | 7.5 | 2026-11-05 | VRPN through 07.36 contains an out-of-bounds stack write vulnerability in vrpn_Endpoint::handle_sender_message() and han |
| CVE-2026-123202 | 7.5 | 2026-11-05 | libnxml before 0.18.6 contains a stack-based buffer overflow vulnerability in src/nxml_parser.c that allows remote attac |
| CVE-2026-123208 | 8.8 | 2026-11-05 | noname Electron desktop build v1.11.2 through v1.11.6.1 contains an unauthenticated local file server with wildcard CORS |
| CVE-2026-123271 | 8.0 | 2026-11-05 | ChatCLI before v1.215.2 contains an improper validation vulnerability in the MCP OAuth login flow that uses server-suppl |
| CVE-2026-123272 | 8.0 | 2026-11-05 | Mark3labs mcp-go before v1.2.1 contains an improper validation vulnerability in OAuthHandler.fetchServerMetadata that al |
| CVE-2026-61648 | 8.3 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-61649 | 7.7 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-61650 | 8.1 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-61651 | 8.3 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-61653 | 8.3 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-63213 | 7.2 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-63214 | 8.8 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-63215 | 8.3 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-69134 | 8.8 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-69135 | 7.1 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-69136 | 7.1 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-69137 | 7.7 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-69140 | 8.3 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-69141 | 8.3 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-69142 | 8.8 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-71548 | 8.8 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-71550 | 9.9 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-97377 | 8.8 | 2026-11-05 | SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15. |
| CVE-2026-102940 | 9.6 | 2026-11-05 | OpenEMR is a free and open source electronic health records and medical practice management application. Prior to 8.4.0, |
| CVE-2026-103935 | 8.1 | 2026-11-05 | OpenEMR is a free and open source electronic health records and medical practice management application. Prior to 8.3.0, |
| CVE-2026-103938 | 7.1 | 2026-11-05 | OpenEMR is a free and open source electronic health records and medical practice management application. Prior to 8.3.0, |
| CVE-2026-104133 | 7.1 | 2026-11-05 | OpenEMR is a free and open source electronic health records and medical practice management application. Prior to 8.3.0, |
| CVE-2026-110930 | 8.0 | 2026-11-05 | Codex Desktop for Windows does not correctly check quotation marks in project paths from Windows Explorer. If a user sel |
| CVE-2026-115573 | 8.1 | 2026-11-05 | OpenEMR is a free and open source electronic health records and medical practice management application. Prior to 8.3.0, |
| CVE-2026-115928 | 7.5 | 2026-11-05 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-116567 | 7.5 | 2026-11-05 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-116568 | 7.5 | 2026-11-05 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-116569 | 7.5 | 2026-11-05 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-116570 | 7.5 | 2026-11-05 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-116779 | 9.8 | 2026-11-05 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-116782 | 7.5 | 2026-11-05 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-116783 | 8.2 | 2026-11-05 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-116784 | 7.5 | 2026-11-05 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-116785 | 9.1 | 2026-11-05 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-116786 | 8.8 | 2026-11-05 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-116787 | 7.5 | 2026-11-05 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-116788 | 8.2 | 2026-11-05 | FreeSWITCH is an open-source software telecommunications platform. Before version 1.11.2, an integer underflow in  switc |
| CVE-2026-116789 | 7.4 | 2026-11-05 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-116790 | 9.1 | 2026-11-05 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-44875 | 7.8 | 2026-11-05 | In HPE Cray Programming Environment versions 25.03 and 25.09, prior to 26.03, the method that CPE is deployed on HPCM po |
| CVE-2026-65983 | 7.5 | 2026-11-05 | OpenEMR is a free and open source electronic health records and medical practice management application. Prior to 8.2.0, |
| CVE-2026-77604 | 7.5 | 2026-11-05 | Code Graph RAG is an AI-powered knowledge graph and retrieval system for querying, understanding, and editing multi-lang |
| CVE-2026-46350 | 9.1 | 2026-11-05 | dcmjs is a JavaScript implementation of DICOM manipulation. Prior to 0.52.0, the DecimalString and IntegerString impleme |
| CVE-2026-48705 | 9.3 | 2026-11-05 | MONAI (Medical Open Network for AI) is an AI toolkit for health care imaging. Prior to 1.6.1, PydicomReader._get_affine( |
| CVE-2026-49272 | 8.5 | 2026-11-05 | OAuthLib is an implementation of the OAuth request-signing logic for Python 3.6+. From 3.3.0 until 4.0.1, OAuthLib's RFC |
| CVE-2026-87008 | 7.1 | 2026-11-05 | Code Graph RAG is an AI-powered knowledge graph and retrieval system for querying, understanding, and editing multi-lang |
| CVE-2026-111768 | 7.5 | 2026-11-05 | The Model Context Protocol TypeScript SDK provides TypeScript client and server implementations of the Model Context Pro |
| CVE-2026-111770 | 7.7 | 2026-11-05 | The Model Context Protocol TypeScript SDK provides TypeScript client and server implementations of the Model Context Pro |
| CVE-2026-119757 | 9.8 | 2026-11-05 | BTCPay Server before 2.4.2, including 2.4.2 release candidates, contains an information disclosure vulnerability that al |
| CVE-2026-33944 | 8.8 | 2026-11-05 | Dolibarr is an open-source enterprise resource planning and customer relationship management application. Prior to 22.0. |
| CVE-2026-58273 | 8.1 | 2026-11-05 | Rucio is a scientific data management framework. From 1.16.1 until 35.9.0, 38.6.0, and 41.0.0rc1, the /credentials/signu |
| CVE-2026-113663 | 8.8 | 2026-11-05 | AG2 is an open-source AgentOS. From 0.13.2 until ag2 1.1.1, and from autogen 0.13.2 to 0.14.1, SandboxShellTool configur |
| CVE-2026-77596 | 9.6 | 2026-11-05 | Kubeflow Pipelines enables users to build and deploy portable, scalable machine learning workflows. Prior to 2.18.0, the |
| CVE-2026-88980 | 8.6 | 2026-11-05 | Kubeflow Pipelines enables users to build and deploy portable, scalable machine learning workflows. Prior to 2.18.0, the |
| CVE-2026-88981 | 8.6 | 2026-11-05 | Kubeflow Pipelines enables users to build and deploy portable, scalable machine learning workflows. Prior to 2.18.0, the |
| CVE-2026-92693 | 8.2 | 2026-11-05 | FastNetMon is a high-performance DDoS detector and sensor. In version 1.2.9 and earlier, parse_raw_packet_to_simple_pack |
| CVE-2026-92695 | 8.2 | 2026-11-05 | FastNetMon is a high-performance DDoS detector and sensor. In version 1.2.9 and earlier, the live parse_packet() callbac |
| CVE-2026-92697 | 7.5 | 2026-11-05 | FastNetMon is a high-performance DDoS detector and sensor. In version 1.2.9 and earlier, the NetFlow v9 collector calls  |
| CVE-2026-92698 | 8.2 | 2026-11-05 | FastNetMon is a high-performance DDoS detector and sensor. In version 1.2.9 and earlier, process_sflow_flow_sample() in  |
| CVE-2026-93424 | 7.5 | 2026-11-05 | FastNetMon is a high-performance DDoS detector and sensor. In version 1.2.9 and earlier, peer_find_template() in src/net |
| CVE-2025-71458 | 7.5 | 2026-11-06 | FTS3 Web Monitoring (fts-monitoring) versions 3.12.0 through 3.13.2 and 3.14.0 contain an unauthenticated sql injection  |
| CVE-2026-63017 | 9.0 | 2026-11-06 | Incorrect authorization in PowerSYSTEM Center allows a low-privileged, authenticated user to access resources normally l |
| CVE-2026-63774 | 9.0 | 2026-11-06 | Insufficient input validation in the PowerSYSTEM Center report designer allows an authenticated user to execute unauthor |
| CVE-2026-77299 | 7.5 | 2026-11-06 | Regexp2 is a feature-rich RegExp engine for Go. Prior to version 2.3.0, when regexp2 compiles and matches a pattern cont |
| CVE-2026-119431 | 7.7 | 2026-11-06 | A server-side request forgery (SSRF) vulnerability exists in Foxit Workspace's file-upload functionality. Insufficient v |
| CVE-2026-119432 | 8.7 | 2026-11-06 | A stored cross-site scripting (XSS) vulnerability exists in the Foxit Workspace's file share preview functionality. An a |
| CVE-2026-119433 | 7.7 | 2026-11-06 | A server-side request forgery (SSRF) vulnerability exists in an undocumented API endpoint of Foxit Workspace due to insu |
| CVE-2026-110525 | 8.8 | 2026-11-06 | The MCB  WordPress plugin through 1.0.0 does not sanitise or escape request header values before storing them and later  |
| CVE-2026-110532 | 8.6 | 2026-11-06 | The Mail Mage WordPress plugin through 0.0.25 does not properly sanitise and escape a user-supplied value before using i |
| CVE-2026-110813 | 7.5 | 2026-11-06 | The Advanced Custom Fields (ACF®) WordPress plugin before 6.8.11 does not properly sanitize a stored field definition th |
| CVE-2026-110955 | 9.8 | 2026-11-06 | The Wurdey WordPress plugin through 1.0.0 does not verify a request signature before logging a user in, allowing unauthe |
| CVE-2026-113584 | 9.8 | 2026-11-06 | The placester WordPress plugin through 1.4.3 does not perform any capability, nonce or ownership check on an AJAX action |
| CVE-2026-113615 | 9.8 | 2026-11-06 | The GS JWT Authentication for WP REST API WordPress plugin through 1.0.0 does not sanitize or parameterize a request val |
| CVE-2026-115230 | 9.8 | 2026-11-06 | The WHIZZ WordPress plugin through 1.1.8 does not validate the password-reset key before updating a user's password, rel |
| CVE-2026-115673 | 7.5 | 2026-11-06 | The Anti-Spam, Spam FireWall by CleanTalk WordPress plugin before 6.91 does not escape a commenter-supplied value before |
| CVE-2026-116533 | 9.8 | 2026-11-06 | The Static Snapshot WordPress plugin through 0.2.1 does not sanitise shell metacharacters in a user-supplied value befor |
| CVE-2026-118045 | 8.7 | 2026-11-06 | The Ever Accounting  WordPress plugin before 2.3.3 does not restrict the file path supplied to its CSV import routine to |
| CVE-2026-120408 | 8.0 | 2026-11-06 | The All-in-One Video Gallery  WordPress plugin before 5.1.0 does not escape a video's stored thumbnail URL before output |
| CVE-2026-86606 | 7.5 | 2026-11-06 | The iubenda \| All-in-one Compliance for GDPR / CCPA Cookie Consent + more WordPress plugin before 3.13.7 does not proper |
| CVE-2026-87784 | 8.8 | 2026-11-06 | The Cool Media Filter WordPress plugin through 1.0.1 does not perform any capability or nonce check when updating the ca |
| CVE-2026-83493 | 9.1 | 2026-11-06 | A flaw was found in distributed-workloads. A remote attacker could exploit a vulnerability in the pull_request_target wo |
| CVE-2026-118423 | 10.0 | 2026-11-06 | The WP Libre Form WordPress plugin 1.5.0.1 does not validate the type of files uploaded through its form submissions, al |
| CVE-2026-119488 | 7.1 | 2026-11-06 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Shamim Rajani Pie  |
| CVE-2026-119499 | 7.5 | 2026-11-06 | Insertion of Sensitive Information Into Sent Data vulnerability in BAKKBONE Australia FloristPress bakkbone-florist-comp |
| CVE-2026-119516 | 9.8 | 2026-11-06 | Deserialization of Untrusted Data vulnerability in Mamunur Rashid Radius Booking — Booking Calendar for Appointments &am |
| CVE-2026-120844 | 9.8 | 2026-11-06 | Incorrect Privilege Assignment vulnerability in miniOrange OAuth Single Sign On – SSO (OAuth Client) miniorange-login-wi |
| CVE-2026-39744 | 7.1 | 2026-11-06 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WC Lovers WCFM Mem |
| CVE-2026-88799 | 8.8 | 2026-11-06 | The MDJM Event Management and Mobile Events Manager WordPress plugins through 1.7.8.7 do not check ownership or capabili |
| CVE-2026-88800 | 9.1 | 2026-11-06 | The MDJM Event Management and Mobile Events Manager WordPress plugins through 1.7.8.7 act on a role deletion request on  |
| CVE-2026-88801 | 8.0 | 2026-11-06 | The MDJM Event Management and Mobile Events Manager WordPress plugins through 1.7.8.7 do not check a capability or a non |
| CVE-2026-110291 | 7.2 | 2026-11-06 | The Graphina – Charts and Graphs For Elementor plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the |
| CVE-2026-19877 | 7.5 | 2026-11-06 | INFINITT ULite 5.0.2.1_BN48_20260528 and earlier protects image-share links with a low-entropy password and does not res |
| CVE-2026-110776 | 7.2 | 2026-11-06 | The MDTF – Meta Data and Taxonomies Filter plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'va |
| CVE-2026-116592 | 7.4 | 2026-11-06 | undici is an HTTP client for Node.js. In versions 7.30.1 and 8.12.2 through 8.12.3, when an originless Agent composes th |
| CVE-2026-33379 | 8.5 | 2026-11-06 | A user with any role, including Viewer or a service account with no permissions, can create, externally publish, and del |
| CVE-2026-87964 | 7.2 | 2026-11-06 | The Product Feed Manager for WooCommerce – CTX Feed – Support 220+ Shopping, AI & Social Channels plugin for WordPress i |
| CVE-2026-123276 | 7.8 | 2026-11-06 | In JetBrains CLion before 2026.3, 
2026.2.4.1 code execution was possible in Safe Mode via a crafted GDB server debug pr |
| CVE-2026-123279 | 9.0 | 2026-11-06 | In JetBrains Datalore before 2026.4 code execution was possible in a notebook's computation by view-only collaborators |
| CVE-2026-123280 | 8.1 | 2026-11-06 | In JetBrains Datalore before 2026.2.4 unauthenticated users could execute code via published interactive reports |
| CVE-2026-123281 | 7.5 | 2026-11-06 | In JetBrains Datalore before 2026.4 notebook code could execute commands in the sidecar container via the mount broker |
| CVE-2026-123282 | 7.4 | 2026-11-06 | In JetBrains Datalore before 2026.4 missing expiration validation of account tokens allowed a new authenticated session |
| CVE-2026-123293 | 7.8 | 2026-11-06 | In JetBrains IntelliJ IDEA before 2026.3, 
2026.2.4 code execution was possible in untrusted projects  via the Terraform |
| CVE-2026-123294 | 9.6 | 2026-11-06 | In JetBrains Hub before 2026.2.52556 privilege escalation was possible by changing email authentication details during t |
| CVE-2026-123295 | 8.1 | 2026-11-06 | In JetBrains Hub before 2026.2.52519 enforced two-factor authentication could be disabled via the profile update endpoin |
| CVE-2026-123296 | 7.5 | 2026-11-06 | In JetBrains Hub before 2026.2.52519 privilege escalation via forged email verification was possible |
| CVE-2026-123301 | 8.2 | 2026-11-06 | In JetBrains IntelliJ IDEA before 2026.3 dOM-based XSS in the OpenAPI preview error view was possible |
| CVE-2026-123302 | 7.8 | 2026-11-06 | In JetBrains IntelliJ IDEA before 2026.3, 
2026.2.4, 
2026.1.5.1, 
2025.3.6.2 code execution was possible in untrusted p |
| CVE-2026-123304 | 7.8 | 2026-11-06 | In JetBrains IntelliJ IDEA before 2026.3 code execution in untrusted projects via a configured ShellCheck path |
| CVE-2026-123305 | 7.5 | 2026-11-06 | In JetBrains IntelliJ IDEA before 2026.3 path traversal was possible via unpacking Dev Container archives from a remote  |
| CVE-2026-123306 | 7.4 | 2026-11-06 | In JetBrains IntelliJ IDEA before 2026.3 improper checks allowed server certificates to be added to the trust store duri |
| CVE-2026-123315 | 7.0 | 2026-11-06 | In JetBrains Junie CLI before 26.8.24 command execution was possible via the Allow Similar Commands option |
| CVE-2026-123317 | 8.1 | 2026-11-06 | In JetBrains Ktor before 3.6.1 session forgery was possible via tampered encrypted session cookies |
| CVE-2026-123321 | 7.8 | 2026-11-06 | In JetBrains WebStorm before 2026.3, 
2026.2.3 code execution via Grunt and Gulp task loading was possible in untrusted  |
| CVE-2026-123323 | 8.4 | 2026-11-06 | In JetBrains YouTrack before 2025.3.170763, 
2026.1.14150, 
2026.2.19656 improper URL validation in the app widget host  |
| CVE-2026-123324 | 7.7 | 2026-11-06 | In JetBrains YouTrack before 2026.2.19562 information disclosure via shared mailbox message history was possible |
| CVE-2026-123325 | 7.1 | 2026-11-06 | In JetBrains YouTrack before 2025.3.170763, 
2026.1.14150, 
2026.2.19656 inclusion of untrusted remote code was possible |
| CVE-2026-123326 | 7.1 | 2026-11-06 | In JetBrains YouTrack before 2026.2.19197 incorrect authorisation in the scripts debugger allowed workflow script disclo |
| CVE-2026-123327 | 7.5 | 2026-11-06 | In JetBrains YouTrack before 2026.2.19562 missing authorization in the saved query endpoint allowed disclosure of issue  |
| CVE-2026-103479 | 7.6 | 2026-11-06 | The Pubjet \| پاب‌جت plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 5.4 |
| CVE-2026-104010 | 7.5 | 2026-11-06 | The WPSyncSheets For Contact Form 7 – CF7 Google Sheets Connector & Save to Database plugin for WordPress is vulnerable  |
| CVE-2026-107622 | 9.8 | 2026-11-06 | The BuddyForms plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 2.10.5 v |
| CVE-2026-114630 | 9.1 | 2026-11-06 | The ELEX WordPress HelpDesk & Customer Ticketing System plugin for WordPress is vulnerable to arbitrary file deletion du |
| CVE-2026-116624 | 8.8 | 2026-11-06 | The Advanced Members for ACF plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and inclu |
| CVE-2026-123655 | 7.5 | 2026-11-06 | A flaw was found in Moodle. Insufficient access control checks on H5P content files allow unauthenticated remote attacke |
| CVE-2026-92895 | 8.1 | 2026-11-06 | The Live2DWebCanvas plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 2. |
| CVE-2026-109883 | 7.1 | 2026-11-06 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Elementor Elemento |
| CVE-2026-109884 | 7.1 | 2026-11-06 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Elementor Elemento |
| CVE-2026-115431 | 7.1 | 2026-11-06 | Missing Authorization vulnerability in WP Swings Upsell Order Bump Offer for WooCommerce upsell-order-bump-offer-for-woo |
| CVE-2026-112340 | 8.2 | 2026-11-06 | Wazuh dashboard plugins from 4.9.0 before 4.14.9 contain an authorization bypass vulnerability that allows authenticated |
| CVE-2026-123487 | 7.5 | 2026-11-06 | Parse Server before 8.6.115 and 9.0.0 before 9.10.7-alpha.1 validates user email address format with a regular expressio |
| CVE-2026-123488 | 9.8 | 2026-11-06 | Craft CMS 4.0.0 before 4.18.9 and 5.0.0 before 5.11.2 contains an unauthenticated SQL injection vulnerability in the ele |
| CVE-2026-123489 | 7.1 | 2026-11-06 | Craft CMS 4.0.0 before 4.18.9 and 5.0.0 before 5.11.2 contains a blind SQL injection vulnerability because the sandbox-e |
| CVE-2026-123490 | 8.8 | 2026-11-06 | Craft CMS from 5.8.17 before 5.11.2 contains a privilege escalation vulnerability because getOwners() applies caller cri |
| CVE-2026-123491 | 8.2 | 2026-11-06 | Craft CMS 4.0.0 before 4.18.9 and 5.0.0 before 5.11.2 contains an SQL injection vulnerability in GraphQL eager-loading:  |
| CVE-2026-123620 | 7.5 | 2026-11-06 | Usermin through 2.570 contains an OS command injection vulnerability in the Read Mail module that allows authenticated u |
| CVE-2026-123621 | 8.8 | 2026-11-06 | Usermin through 2.570 contains a path traversal vulnerability in mailbox/detachall.cgi that allows remote unauthenticate |
| CVE-2026-123783 | 8.8 | 2026-11-06 | Skyvern through 1.0.56 contains a sandbox bypass vulnerability that allows authenticated users to execute code by recons |
| CVE-2026-123784 | 7.8 | 2026-11-06 | Fluxbox through 1.3.7 contains an OS command injection vulnerability in RootTheme::reconfigTheme() that allows attackers |
| CVE-2026-123786 | 8.5 | 2026-11-06 | Agenta before 0.122.5 contains a server-side request forgery vulnerability that allows workspace members with workflow e |
| CVE-2026-53980 | 8.1 | 2026-11-06 | Charmbracelet wish before 2.0.5 contains a path traversal vulnerability in the git middleware (charm.land/wish/v2) that  |
| CVE-2026-59105 | 9.8 | 2026-11-06 | Jumis (formerly Tildes Jumis) creates and uses a Microsoft SQL Server login named ##Tilde_JumisAdmin## whose password is |
| CVE-2026-87045 | 7.5 | 2026-11-06 | The HTTP/2 server in subsys/net/lib/http/http_server_http2.c clears the connection's stream binding at the start of ever |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2024-27834 | Apple / Multiple Products | 2026-11-04 | 2026-11-18 | Unknown |
| CVE-2026-119977 | WordPress / WordPress Core | 2026-11-03 | 2026-11-06 | Unknown |
| CVE-2026-118527 | Ivanti / Connect Secure | 2026-10-30 | 2026-11-13 | Unknown |
| CVE-2026-111357 | Ivanti / Connect Secure | 2026-10-30 | 2026-11-02 | Unknown |

---

*Total entries in CISA KEV catalog: 1768*