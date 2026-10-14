# Vulnerability Intelligence Report

**Date:** 2026-10-14  
**Generated:** 2026-10-14T13:18:46Z  

---

## Executive Summary

Our environment faces significant exposure across 1,312 high-severity vulnerabilities, with two monitored CVEs now confirmed in CISA's Known Exploited Vulnerabilities catalog and remediation deadlines of October 16, 2026. Critical issues span IBM WebSphere, FreeRDP, Wazuh, and Froxlor platforms, enabling remote code execution, privilege escalation, and data exfiltration. Seven new KEV entries were added this week alone, including actively exploited flaws in Ivanti Connect Secure and Microsoft Windows. Immediate action is required to contain exposure before federal remediation deadlines expire and adversaries leverage these confirmed exploit paths against our infrastructure.

---

## Risk Narrative

The current threat landscape reflects a rapidly maturing exploitation environment where attackers are actively leveraging known vulnerabilities in widely deployed enterprise software. The presence of two monitored CVEs in CISA's KEV catalog—covering Ivanti and Microsoft Windows—indicates confirmed, in-the-wild exploitation with imminent regulatory deadlines. Legacy vulnerabilities such as ISC BIND (2015) and Apache Struts (2016) appearing in fresh KEV additions signal that threat actors continue exploiting unpatched older systems. The combination of remote code execution flaws, kernel-level privilege escalation, and security tool compromise (Wazuh) creates compounded business risk including data breaches, ransomware deployment, and loss of security visibility. Without immediate prioritized remediation, the organization faces regulatory non-compliance, operational disruption, and potential reputational damage.

---

## Prioritized Action Items

1. Immediately patch or isolate systems affected by CVE-2026-104935 (Ivanti Connect Secure) and CVE-2026-96951 (Microsoft Windows) before the October 16, 2026 CISA KEV deadline.
2. Apply available patches for FreeRDP CVE-2026-109676 (CVSS 8.8) and Colorful iGameCenter CVE-2026-109520 (CVSS 8.8) to eliminate critical remote code execution and kernel-level exploitation risk.
3. Audit and patch IBM WebSphere Application Server Liberty instances affected by CVE-2026-103499 to prevent unauthorized remote access across all affected versions.
4. Remediate Wazuh CVE-2026-74034 immediately to prevent enrolled agents from issuing unauthorized upgrade commands that could compromise the security monitoring infrastructure itself.
5. Conduct a full audit of Froxlor deployments to address stored XSS (CVE-2026-109960) and newline injection (CVE-2026-109961) vulnerabilities that allow authenticated users to escalate impact.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-103499 | 7.5 | 2026-10-13 | IBM WebSphere Application Server - Liberty 17.0.0.3 through 26.0.0.10 and IBM WebSphere Application Server 8.5, and 9.0  |
| CVE-2026-109519 | 8.3 | 2026-10-13 | A vulnerability was detected in YouTransfer up to 0.0.7/1.0.6/1.1.0. Affected is an unknown function of the file /settin |
| CVE-2026-109520 | 8.8 | 2026-10-13 | A flaw has been found in Colorful iGameCenter 2.0.0.82. Affected by this vulnerability is the function MmMapIoSpace in t |
| CVE-2026-109676 | 8.8 | 2026-10-13 | FreeRDP from 3.0.0-beta1 before 3.32.0 contains a use-after-free vulnerability in smartcard handling that allows attacke |
| CVE-2026-109956 | 7.0 | 2026-10-13 | NLTK through 3.10.3 contains a path traversal vulnerability in WekaClassifier that allows attackers to bypass nltk.paths |
| CVE-2026-109960 | 7.7 | 2026-10-13 | Froxlor 2.0.0 before 2.3.14 contains a stored cross-site scripting vulnerability that allows authenticated customers to  |
| CVE-2026-109961 | 8.5 | 2026-10-13 | Froxlor 0.10.0 before 2.3.14 contains a newline injection vulnerability that allows authenticated customers to inject ar |
| CVE-2026-109965 | 7.1 | 2026-10-13 | Serena before 2.0.0 contains an improper link resolution vulnerability that allows attackers to access files outside the |
| CVE-2026-109967 | 7.5 | 2026-10-13 | yt-dlp-web-ui through 4.0.0 contains a NULL pointer dereference vulnerability in the Service.Formats JSON-RPC method tha |
| CVE-2026-74034 | 7.5 | 2026-10-13 | Wazuh from 4.1.0 before 4.14.8 contains a missing origin check in wm_agent_upgrade that allows enrolled agents to issue  |
| CVE-2026-74035 | 7.2 | 2026-10-13 | Wazuh versions from 4.6.0 before 4.14.8 contain an authentication bypass vulnerability where security.update_user places |
| CVE-2026-74036 | 7.2 | 2026-10-13 | Wazuh from 4.3.0 before 4.14.8 contains a remote code execution vulnerability where SCA policy trust is determined by fi |
| CVE-2026-74037 | 7.2 | 2026-10-13 | Wazuh 4.0.0 before 4.14.8 fails to invalidate issued tokens for run_as users with zero static roles, because check_token |
| CVE-2026-74040 | 9.1 | 2026-10-13 | Wazuh versions from 3.9.0 before 4.14.8 contain an arbitrary file overwrite vulnerability in MasterHandler.process_files |
| CVE-2026-74041 | 9.1 | 2026-10-13 | Wazuh 4.14.3 before 4.14.8 contains a case-sensitivity mismatch between the ossec.conf validator and wazuh-logcollector  |
| CVE-2026-74043 | 9.0 | 2026-10-13 | Wazuh from 4.1.1 before 4.14.8 contains a path traversal vulnerability in upload_list_file, upload_rule_file, and upload |
| CVE-2026-74045 | 7.1 | 2026-10-13 | Wazuh from 3.12.0 before 4.14.8 contains a heap buffer overflow in fim_generate_alert() where full_log is sized from inp |
| CVE-2026-93907 | 8.1 | 2026-10-13 | IBM WebSphere Application Server 8.5, and 9.0 could allow a remote attacker to bypass authentication by exploiting a fla |
| CVE-2026-95680 | 8.0 | 2026-10-13 | IBM WebSphere Application Server 8.5, and 9.0 could allow an authenticated attacker to bypass authorization leading to a |
| CVE-2026-104192 | 9.6 | 2026-10-13 | Dragonfly is an in-memory data store built for modern application workloads. Prior to 1.40, OpaqueObjLoader::CreateStrea |
| CVE-2026-108184 | 7.4 | 2026-10-13 | Improper certificate validation in certain Zoom Clients for Windows may allow an unauthenticated user to conduct an info |
| CVE-2026-108185 | 7.4 | 2026-10-13 | Improper certificate validation in the My Notes feature of certain Zoom Clients may allow an unauthenticated user to con |
| CVE-2026-109521 | 7.3 | 2026-10-13 | A vulnerability was detected in girishsaraf Online-Appointment-Booking-System up to f427b4757128ca253d33d0cc4e87bbb9c999 |
| CVE-2026-109522 | 7.3 | 2026-10-13 | A vulnerability has been found in girishsaraf Online-Appointment-Booking-System up to f427b4757128ca253d33d0cc4e87bbb9c9 |
| CVE-2026-109523 | 7.3 | 2026-10-13 | A vulnerability was found in girishsaraf Online-Appointment-Booking-System up to f427b4757128ca253d33d0cc4e87bbb9c999a4d |
| CVE-2026-11731 | 8.8 | 2026-10-13 | An authentication bypass vulnerability in the listed NETGEAR RAX series models allows an unauthenticated attacker with a |
| CVE-2026-11732 | 8.8 | 2026-10-13 | An insufficient input validation vulnerability in the website blocking feature (Block Sites) of the listed NETGEAR route |
| CVE-2026-53418 | 8.1 | 2026-10-13 | Improper Authorization in Handler for Custom URL Scheme in Zoom Workplace for Android before version 7.2.1 may allow an  |
| CVE-2026-53420 | 8.0 | 2026-10-13 | Buffer overflow in a Zoom Phone feature of Zoom Workplace Clients may allow an unauthenticated user to conduct a escalat |
| CVE-2026-53709 | 9.8 | 2026-10-13 | MCP Context Forge is an MCP gateway and administrative platform. Prior to 1.0.2, mcpgateway/config.py and .env.example s |
| CVE-2026-65198 | 8.6 | 2026-10-13 | Huawei's openUBMC ships a default SNMPv3 USM key that uses one value for both authentication and privacy. An attacker wh |
| CVE-2026-95114 | 7.5 | 2026-10-13 | libwebsockets contains an out-of-bounds read vulnerability in the LEJP incremental parser in lib/misc/lejp.c. This allow |
| CVE-2026-95122 | 7.5 | 2026-10-13 | mp4v2 2.0.0 contains a NULL pointer dereference vulnerability in MP4File::GenerateTracks() in src/mp4file.cpp. This allo |
| CVE-2024-34323 | 10.0 | 2026-10-13 | ProPhoenix Law RMS v2022.2403.3.101 was discovered to contain an Insecure Direct Object Reference (IDOR) via the usrLogi |
| CVE-2026-104935 | 8.6 | 2026-10-13 | Authentication bypass by spoofing in ICS before version 25.1.3.0 allows a remote unauthenticated attacker to execute arb |
| CVE-2026-109525 | 7.3 | 2026-10-13 | A vulnerability was identified in girishsaraf Online-Appointment-Booking-System up to f427b4757128ca253d33d0cc4e87bbb9c9 |
| CVE-2026-109605 | 7.3 | 2026-10-13 | A security vulnerability has been detected in SourceCodester Simple Cafe Billing System 1.0. This affects the function A |
| CVE-2026-110025 | 7.3 | 2026-10-13 | A flaw has been found in slackero phpwcms up to 1.9.49/1.12.3. This issue affects some unknown processing of the file in |
| CVE-2026-55376 | 8.8 | 2026-10-13 | Heym builds and runs agentic systems and business-process automations on self-hosted infrastructure. Prior to 0.0.40, an |
| CVE-2026-55675 | 10.0 | 2026-10-13 | The Salty documentation repository builds and deploys the docs.saltbox.dev website. Prior to commit 649c9aea2daef1168eeb |
| CVE-2026-55695 | 9.1 | 2026-10-13 | FearlessCMS is a flat-file content management system centered on simplicity and open source. In 0.1.2b and earlier, an a |
| CVE-2026-102989 | 9.3 | 2026-10-13 | TanStack Router is a client-first, server-capable, fully type-safe router and full-stack framework for the web. From 1.1 |
| CVE-2026-103030 | 7.5 | 2026-10-13 | Dio is a powerful HTTP client for Dart and Flutter. From 1.0.0 until 2.8.0, dio_http2_adapter follows redirects in Http2 |
| CVE-2026-106042 | 9.9 | 2026-10-13 | An External Control of File Name or Path vulnerability in Ivanti Xtraction before version 2026.4 allows a remote authent |
| CVE-2026-106043 | 7.5 | 2026-10-13 | A Missing Authentication for Critical Function vulnerability in Ivanti Xtraction before version 2026.4 allows a remote u |
| CVE-2026-106047 | 7.7 | 2026-10-13 | A Path Traversal vulnerability in the template export functionality of Ivanti Xtraction before version 2026.4 allows a r |
| CVE-2026-109412 | 9.9 | 2026-10-13 | An exposed dangerous endpoint in Ivanti Neurons Patch for Intune allows a remote authenticated attacker to leak sensitiv |
| CVE-2026-109606 | 7.3 | 2026-10-13 | A vulnerability was detected in SourceCodester Art Gallery Management System 1.0. This impacts the function Action::save |
| CVE-2026-109607 | 7.3 | 2026-10-13 | A flaw has been found in SourceCodester Online Exam System 1.0. Affected is an unknown function of the file adminpanel/a |
| CVE-2026-109620 | 7.3 | 2026-10-13 | A vulnerability has been found in SourceCodester Online Reviewer System 1.0. Affected by this vulnerability is the funct |
| CVE-2026-110097 | 8.1 | 2026-10-13 | Ikaros 1.2.0 through 1.2.5 contains an authentication bypass vulnerability that allows attackers with a valid password t |
| CVE-2026-110102 | 7.5 | 2026-10-13 | Powerlevel10k through 1.20.0 contains an insecure download vulnerability in the gitstatus/install script that disables T |
| CVE-2026-110108 | 8.1 | 2026-10-13 | MateCloud through 5.0.8 contains a missing authorization vulnerability that allows any authenticated user to manage obje |
| CVE-2026-110115 | 7.5 | 2026-10-13 | Risesoft Digital-Infrastructure 9.6.5 through 9.6.11 contains a path traversal vulnerability in the fileManager Y9FileCo |
| CVE-2026-110116 | 9.1 | 2026-10-13 | Risesoft-y9 Digital-Infrastructure 9.6.5 through 9.6.11 contains a path traversal vulnerability in the fileManager store |
| CVE-2026-110119 | 7.1 | 2026-10-13 | Yshopmall through 2.0.0 contains an insecure direct object reference vulnerability in the member address API that allows |
| CVE-2026-110123 | 7.1 | 2026-10-13 | Makunet maku-boot 4.3.0 through 5.0.0 contains a missing authorization vulnerability that allows authenticated users to  |
| CVE-2026-110124 | 8.1 | 2026-10-13 | FastBee through 2.1.0 contains an insecure direct object reference vulnerability in DeviceController that allows authent |
| CVE-2026-110128 | 7.5 | 2026-10-13 | fuint through commit 4c4bc8a contains a missing authentication vulnerability that allows unauthenticated attackers to re |
| CVE-2026-54454 | 9.1 | 2026-10-13 | OpenCATS is an open-source applicant tracking system and recruitment CRM for staffing agencies and hiring teams. Prior t |
| CVE-2026-54640 | 7.6 | 2026-10-13 | OpenRemote is an open-source internet-of-things platform. Prior to 1.24.2, the KNXProtocol.startAssetImport method in ag |
| CVE-2026-54641 | 7.7 | 2026-10-13 | OpenRemote is an open-source internet-of-things platform. Prior to 1.24.2, the get, getUserClientRoles, and getUserRealm |
| CVE-2026-55183 | 9.6 | 2026-10-13 | RClone Manager is a cross-platform GUI application designed to help users manage Rclone remotes efficiently. Prior to 0. |
| CVE-2026-55562 | 9.0 | 2026-10-13 | Cronicle is a multi-server task scheduler and runner, with a web based front-end UI. Prior to 0.9.119, the administrator |
| CVE-2026-61642 | 7.7 | 2026-10-13 | Squid is a caching proxy for the Web. From 3.3.0.1 to before 7.6, due to an improper enforcement of behavioral workflow  |
| CVE-2026-69227 | 9.8 | 2026-10-13 | A flaw in Portal for ArcGIS allows unauthenticated access to certain /portaladmin/local API endpoints under specific con |
| CVE-2026-77459 | 9.9 | 2026-10-13 | Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. From 2.10.0 until 3.3.15, 3.4.10, 3.5.4, and 3 |
| CVE-2026-82416 | 7.7 | 2026-10-13 | FrankenPHP is a modern application server for PHP. Prior to 1.12.5, FrankenPHP worker mode can retain PHP session state  |
| CVE-2026-85990 | 8.8 | 2026-10-13 | Leantime is an open source project management system. Prior to 3.10.0, for the provisionally grouped account-creation an |
| CVE-2026-94603 | 10.0 | 2026-10-13 | Podman is a tool for managing OCI containers and pods. From 4.4.0 until 5.8.8 and 6.1.3, podman run treats an image carr |
| CVE-2025-46773 | 8.8 | 2026-10-13 | An Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability [CWE-89] vulnerabi |
| CVE-2025-57739 | 8.8 | 2026-10-13 | An improper neutralization of special elements used in an SQL Command ("SQL Injection") vulnerability [CWE-89] vulnerabi |
| CVE-2026-104085 | 8.8 | 2026-10-13 | odt2spip plugin for SPIP before 4.4.0 contains an OS command injection vulnerability that allows authenticated authors t |
| CVE-2026-106173 | 9.8 | 2026-10-13 | A improper limitation of a pathname to a restricted directory ('path traversal') vulnerability in Fortinet FortiSIEM 7.5 |
| CVE-2026-108375 | 8.8 | 2026-10-13 | dataclasses-avroschema generates Avro schemas from Python dataclasses, Pydantic models, and Faust Records and generates  |
| CVE-2026-108376 | 8.8 | 2026-10-13 | dataclasses-avroschema generates Avro schemas from Python dataclasses, Pydantic models, and Faust Records and generates  |
| CVE-2026-108377 | 8.8 | 2026-10-13 | dataclasses-avroschema generates Avro schemas from Python dataclasses, Pydantic models, and Faust Records and generates  |
| CVE-2026-108378 | 8.8 | 2026-10-13 | dataclasses-avroschema generates Avro schemas from Python dataclasses, Pydantic models, and Faust Records and generates  |
| CVE-2026-108379 | 8.8 | 2026-10-13 | dataclasses-avroschema generates Avro schemas from Python dataclasses, Pydantic models, and Faust Records and generates  |
| CVE-2026-108380 | 8.8 | 2026-10-13 | dataclasses-avroschema generates Avro schemas from Python dataclasses, Pydantic models, and Faust Records and generates  |
| CVE-2026-108381 | 8.8 | 2026-10-13 | dataclasses-avroschema generates Avro schemas from Python dataclasses, Pydantic models, and Faust Records and generates  |
| CVE-2026-108382 | 8.8 | 2026-10-13 | dataclasses-avroschema generates Avro schemas from Python dataclasses, Pydantic models, and Faust Records and generates  |
| CVE-2026-108383 | 8.8 | 2026-10-13 | dataclasses-avroschema generates Avro schemas from Python dataclasses, Pydantic models, and Faust Records and generates  |
| CVE-2026-108384 | 8.8 | 2026-10-13 | dataclasses-avroschema generates Avro schemas from Python dataclasses, Pydantic models, and Faust Records and generates  |
| CVE-2026-108385 | 8.8 | 2026-10-13 | dataclasses-avroschema generates Avro schemas from Python dataclasses, Pydantic models, and Faust Records and generates  |
| CVE-2026-23705 | 7.2 | 2026-10-13 | An Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability [CWE-89] vulnerabi |
| CVE-2026-23707 | 7.2 | 2026-10-13 | An Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability [CWE-89] vulnerabi |
| CVE-2026-37107 | 9.8 | 2026-10-13 | An issue in HTMLy v.3.1.1 allows a remote attacker to escalate privileges via the get_feed function in the admin.php com |
| CVE-2026-52394 | 9.1 | 2026-10-13 | DeepSeek V4 is vulnerable to Incorrect Access Control via a crafted input. |
| CVE-2026-92892 | 9.0 | 2026-10-13 | Potential arbitrary code execution, under specific configurations. |
| CVE-2026-100133 | 9.3 | 2026-10-13 | Adobe Commerce is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by an attacker to i |
| CVE-2026-100200 | 7.0 | 2026-10-13 | Use after free in Windows Update Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-100201 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Windows Client License Service allows an authorized attacker to elevate privileges locally |
| CVE-2026-100202 | 9.8 | 2026-10-13 | Use after free in Windows Message Queuing Queue Manager allows an unauthorized attacker to execute code over a network. |
| CVE-2026-100203 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Windows Update Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-100205 | 7.1 | 2026-10-13 | Untrusted pointer dereference in SysInternals allows an authorized attacker to elevate privileges locally. |
| CVE-2026-100207 | 7.3 | 2026-10-13 | Improper neutralization of special elements used in an os command ('os command injection') in Azure CycleCloud allows an |
| CVE-2026-100209 | 8.8 | 2026-10-13 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-100210 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-100211 | 8.8 | 2026-10-13 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-100212 | 8.8 | 2026-10-13 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-100214 | 8.8 | 2026-10-13 | Deserialization of untrusted data in Dynamics Business Central allows an authorized attacker to execute code over a netw |
| CVE-2026-100215 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Graphics Component allows an unauthorized attacker to execute code locally. |
| CVE-2026-100216 | 7.0 | 2026-10-13 | Stack-based buffer overflow in Windows Storage allows an authorized attacker to elevate privileges locally. |
| CVE-2026-100217 | 7.8 | 2026-10-13 | Improper privilege management in Windows Group Policy allows an authorized attacker to elevate privileges locally. |
| CVE-2026-100218 | 8.1 | 2026-10-13 | Use after free in Remote Desktop Gateway Service allows an unauthorized attacker to execute code over a network. |
| CVE-2026-100219 | 9.8 | 2026-10-13 | Use after free in Microsoft QUIC allows an unauthorized attacker to execute code over a network. |
| CVE-2026-100220 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows Media Video Decoder allows an unauthorized attacker to execute code over a network |
| CVE-2026-100222 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Network Policy Server (NPS) allows an unauthorized attacker to execute code over a network |
| CVE-2026-100225 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Windows Storage allows an authorized attacker to elevate privileges locally. |
| CVE-2026-102189 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Windows Storage allows an authorized attacker to elevate privileges locally. |
| CVE-2026-102191 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Windows Storage allows an authorized attacker to elevate privileges locally. |
| CVE-2026-102192 | 7.5 | 2026-10-13 | Integer underflow (wrap or wraparound) in Windows Failover Cluster allows an unauthorized attacker to deny service over  |
| CVE-2026-102193 | 7.0 | 2026-10-13 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-102194 | 7.0 | 2026-10-13 | Use after free in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-102195 | 7.0 | 2026-10-13 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-102196 | 7.8 | 2026-10-13 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-102197 | 7.0 | 2026-10-13 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-102201 | 7.8 | 2026-10-13 | Use after free in Microsoft Windows Media Foundation allows an authorized attacker to elevate privileges locally. |
| CVE-2026-102202 | 7.8 | 2026-10-13 | Improper access control in Windows Container Isolation FS Filter Driver (unionfs.sys) allows an authorized attacker to e |
| CVE-2026-102203 | 8.8 | 2026-10-13 | Access of resource using incompatible type ('type confusion') in RPC Runtime allows an unauthorized attacker to execute  |
| CVE-2026-102204 | 7.8 | 2026-10-13 | Improper link resolution before file access ('link following') in Microsoft Defender for Endpoint allows an authorized a |
| CVE-2026-102205 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Universal Disk Format File System Driver (UDFS) allows an authorized attacker to e |
| CVE-2026-102207 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Kernel allows an  |
| CVE-2026-102208 | 7.0 | 2026-10-13 | Use after free in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-102209 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Microsoft Graphics Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-102210 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Windows Text Shaping allows an unauthorized attacker to execute code over a network. |
| CVE-2026-102211 | 7.0 | 2026-10-13 | Use after free in Windows Virtualization-Based Security (VBS) Enclave allows an authorized attacker to elevate privilege |
| CVE-2026-102214 | 8.8 | 2026-10-13 | Use after free in Windows Hyper-V allows an authorized attacker to execute code locally. |
| CVE-2026-102215 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Universal Disk Format File System Driver (UDFS) allows an authorized attacker to e |
| CVE-2026-102216 | 7.8 | 2026-10-13 | Access of resource using incompatible type ('type confusion') in Windows StateRepository API allows an authorized attack |
| CVE-2026-102217 | 8.8 | 2026-10-13 | Improper resolution of path equivalence in WebDAV allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-102218 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Universal Disk Format File System Driver (UDFS) allows an authorized attacker to e |
| CVE-2026-102220 | 7.8 | 2026-10-13 | Use after free in Windows VHD miniport driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-102225 | 8.8 | 2026-10-13 | Out-of-bounds read in Windows Text Shaping allows an unauthorized attacker to execute code over a network. |
| CVE-2026-102226 | 8.8 | 2026-10-13 | Improper limitation of a pathname to a restricted directory ('path traversal') in Dynamics Business Central allows an au |
| CVE-2026-102227 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Resilient File System (ReFS) allows an authorized attacker to execute code locally |
| CVE-2026-102231 | 7.7 | 2026-10-13 | Improper resolution of path equivalence in Visual Studio Code allows an unauthorized attacker to bypass a security featu |
| CVE-2026-102232 | 7.0 | 2026-10-13 | Incorrect authorization in Visual Studio Code allows an unauthorized attacker to bypass a security feature locally. |
| CVE-2026-102233 | 7.8 | 2026-10-13 | Missing authorization in Visual Studio Code allows an unauthorized attacker to bypass a security feature locally. |
| CVE-2026-102599 | 7.5 | 2026-10-13 | Socket.IO enables bidirectional and low-latency communication for every platform. From Engine.IO 6.6.0 until 6.6.10, a t |
| CVE-2026-102849 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-102850 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-102856 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Visio allows an unauthorized attacker to execute code over a network. |
| CVE-2026-102857 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Visio allows an unauthorized attacker to execute code over a network. |
| CVE-2026-102858 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office OneNote allows an unauthorized attacker to execute code over a network. |
| CVE-2026-102860 | 8.8 | 2026-10-13 | Improper access control in Microsoft Office SharePoint allows an authorized attacker to elevate privileges over a networ |
| CVE-2026-102861 | 8.8 | 2026-10-13 | Missing authorization in Microsoft Office SharePoint allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-102862 | 8.8 | 2026-10-13 | Incorrect authorization in Microsoft Office SharePoint allows an authorized attacker to elevate privileges over a networ |
| CVE-2026-102863 | 8.8 | 2026-10-13 | Improper control of generation of code ('code injection') in Microsoft Office SharePoint allows an authorized attacker t |
| CVE-2026-102866 | 8.1 | 2026-10-13 | Improper verification of cryptographic signature in Microsoft Office SharePoint allows an unauthorized attacker to eleva |
| CVE-2026-102869 | 8.8 | 2026-10-13 | Access of resource using incompatible type ('type confusion') in .NET and Visual Studio allows an unauthorized attacker  |
| CVE-2026-102870 | 8.8 | 2026-10-13 | Improper control of generation of code ('code injection') in ASP.NET Core allows an unauthorized attacker to execute cod |
| CVE-2026-103553 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows Partition Management Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-103554 | 7.0 | 2026-10-13 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-103555 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Virtual Hard Disk (VHD) Miniport Driver allows an authorized attacker to elevate privilege |
| CVE-2026-103558 | 7.5 | 2026-10-13 | Deadlock in Windows Routing and Remote Access Service (RRAS) allows an unauthorized attacker to deny service over a netw |
| CVE-2026-103565 | 7.0 | 2026-10-13 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-103568 | 7.8 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Credential Provid |
| CVE-2026-103569 | 7.5 | 2026-10-13 | Out-of-bounds read in Windows IKE Extension allows an unauthorized attacker to disclose information over a network. |
| CVE-2026-103572 | 8.8 | 2026-10-13 | Improper control of generation of code ('code injection') in Visual Studio Tools for Applications and SQL Server Managem |
| CVE-2026-103575 | 8.8 | 2026-10-13 | Use after free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-103577 | 7.5 | 2026-10-13 | Insecure default variable initialization in Microsoft QUIC allows an unauthorized attacker to bypass a security feature  |
| CVE-2026-103849 | 10.0 | 2026-10-13 | Adobe Commerce is affected by an Improper Neutralization of Special Elements Used in a Template Engine vulnerability tha |
| CVE-2026-103966 | 7.8 | 2026-10-13 | Adobe Framemaker is affected by a Heap-based Buffer Overflow vulnerability that could result in arbitrary code execution |
| CVE-2026-103967 | 7.8 | 2026-10-13 | Adobe Framemaker is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in th |
| CVE-2026-104340 | 7.8 | 2026-10-13 | Adobe Framemaker is affected by a Heap-based Buffer Overflow vulnerability that could result in arbitrary code execution |
| CVE-2026-104341 | 7.8 | 2026-10-13 | Adobe Framemaker is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in th |
| CVE-2026-104342 | 7.8 | 2026-10-13 | Adobe Framemaker is affected by a Use After Free vulnerability that could result in arbitrary code execution in the cont |
| CVE-2026-104344 | 7.8 | 2026-10-13 | Adobe Framemaker is affected by a Heap-based Buffer Overflow vulnerability that could result in arbitrary code execution |
| CVE-2026-104875 | 7.1 | 2026-10-13 | Ente provides end-to-end encrypted cloud services and security tools. Prior to server image 2026.07.09, the POST /emerge |
| CVE-2026-105003 | 7.8 | 2026-10-13 | Heap-based buffer overflow in HID class driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105004 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows Overlay Filter allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105005 | 8.1 | 2026-10-13 | Out-of-bounds write in Windows Schannel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105007 | 8.8 | 2026-10-13 | An elevation of privilege vulnerability exists in the Network Driver Interface Specification (NDIS) when ndis.sys fails  |
| CVE-2026-105008 | 9.0 | 2026-10-13 | No cwe for this issue in Windows Schannel allows an unauthorized attacker to perform spoofing over a network. |
| CVE-2026-105009 | 7.5 | 2026-10-13 | Incorrect default permissions in Windows Server Update Service allows an authorized attacker to elevate privileges local |
| CVE-2026-105010 | 9.8 | 2026-10-13 | Use after free in Microsoft Windows Search Component allows an unauthorized attacker to elevate privileges over a networ |
| CVE-2026-105013 | 7.4 | 2026-10-13 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a ne |
| CVE-2026-105016 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft QUIC allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105591 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105592 | 7.5 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105593 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105595 | 8.8 | 2026-10-13 | Out-of-bounds read in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105596 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105597 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105598 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105599 | 7.5 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office PowerPoint allows an unauthorized attacker to execute code over a network |
| CVE-2026-105714 | 7.5 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105715 | 7.5 | 2026-10-13 | Integer overflow or wraparound in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105716 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105717 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105718 | 8.8 | 2026-10-13 | Out-of-bounds read in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105722 | 7.0 | 2026-10-13 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105723 | 7.5 | 2026-10-13 | Untrusted pointer dereference in Windows Distributed File System (DFS) allows an unauthorized attacker to elevate privil |
| CVE-2026-105725 | 7.0 | 2026-10-13 | Use after free in Windows Security App allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105727 | 8.8 | 2026-10-13 | Improper limitation of a pathname to a restricted directory ('path traversal') in Dynamics Business Central allows an au |
| CVE-2026-105728 | 7.5 | 2026-10-13 | Improper authentication in Dynamics Business Central allows an unauthorized attacker to disclose information over a netw |
| CVE-2026-105729 | 7.1 | 2026-10-13 | Untrusted pointer dereference in SysInternals allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105732 | 7.3 | 2026-10-13 | Stack-based buffer overflow in SysInternals allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105733 | 8.8 | 2026-10-13 | Improper access control in Windows Hyper-V allows an authorized attacker to execute code locally. |
| CVE-2026-106625 | 7.8 | 2026-10-13 | Adobe Framemaker is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in th |
| CVE-2026-108130 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Virtualization-Based Security (VBS) Enclave allows an authorized attacker to eleva |
| CVE-2026-108131 | 7.5 | 2026-10-13 | No cwe for this issue in Active Directory Federation Services (AD FS) allows an unauthorized attacker to perform spoofin |
| CVE-2026-108132 | 7.0 | 2026-10-13 | Double free in Windows Kerberos allows an authorized attacker to elevate privileges locally. |
| CVE-2026-108133 | 7.8 | 2026-10-13 | Release of invalid pointer or reference in Windows Modern Device Management (MDM) allows an authorized attacker to eleva |
| CVE-2026-108134 | 7.0 | 2026-10-13 | Use after free in Windows Autopilot allows an authorized attacker to elevate privileges locally. |
| CVE-2026-108135 | 7.0 | 2026-10-13 | Improper link resolution before file access ('link following') in Windows Backup Engine allows an authorized attacker to |
| CVE-2026-108136 | 7.8 | 2026-10-13 | Use after free in Microsoft Windows Search Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-108396 | 7.0 | 2026-10-13 | Time-of-check time-of-use (toctou) race condition in Windows Modern Device Management (MDM) allows an authorized attacke |
| CVE-2026-108398 | 8.8 | 2026-10-13 | Untrusted search path in .NET Framework allows an authorized attacker to bypass a security feature locally. |
| CVE-2026-108399 | 7.2 | 2026-10-13 | Heap-based buffer overflow in Windows Hyper-V allows an authorized attacker to elevate privileges locally. |
| CVE-2026-108400 | 8.8 | 2026-10-13 | Integer overflow or wraparound in Microsoft Windows Codecs Library allows an unauthorized attacker to execute code over  |
| CVE-2026-108457 | 8.1 | 2026-10-13 | Out-of-bounds write in Microsoft Windows PDF allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108458 | 8.8 | 2026-10-13 | Use after free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108460 | 8.1 | 2026-10-13 | Use after free in Windows Message Queuing allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108461 | 7.0 | 2026-10-13 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-108463 | 8.8 | 2026-10-13 | Improper resolution of path equivalence in Windows SmartScreen allows an unauthorized attacker to bypass a security feat |
| CVE-2026-108464 | 7.0 | 2026-10-13 | Use after free in Software Protection Platform (SPP) allows an authorized attacker to elevate privileges locally. |
| CVE-2026-108465 | 7.0 | 2026-10-13 | Use after free in Windows Update Delivery Optimization allows an authorized attacker to elevate privileges locally. |
| CVE-2026-108467 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft PostScript Printer Driver allows an authorized attacker to execute code over a n |
| CVE-2026-108468 | 7.0 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-108471 | 8.8 | 2026-10-13 | Untrusted pointer dereference in Windows Virtualization-Based Security (VBS) Enclave allows an authorized attacker to el |
| CVE-2026-109428 | 8.8 | 2026-10-13 | Mistral Vibe before 2.25.5 contains a permission validation bypass vulnerability that allows attackers to execute unauth |
| CVE-2026-109429 | 8.8 | 2026-10-13 | Mistral Vibe before 2.25.4 contains a command permission gate bypass vulnerability that allows attackers to execute arbi |
| CVE-2026-109453 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Virtual Hard Disk (VHD) Miniport Driver allows an authorized attacker to elevate privilege |
| CVE-2026-110111 | 7.5 | 2026-10-13 | Xen Orchestra before 6.9.0 contains an improper access control vulnerability that allows any authenticated user to becom |
| CVE-2026-110112 | 8.1 | 2026-10-13 | Dockhand before 1.0.50 contains a privilege escalation vulnerability that allows users from another tenant to gain admin |
| CVE-2026-110130 | 10.0 | 2026-10-13 | Dockhand before 1.0.45 contains an authentication bypass in which the global auth hook skips authentication for any path |
| CVE-2026-110202 | 8.8 | 2026-10-13 | Roo Code through 3.54.0 contains a command approval bypass vulnerability in getCommandDecision() that allows attackers t |
| CVE-2026-110203 | 8.8 | 2026-10-13 | Roo Code through 3.54.0 contains a command approval bypass vulnerability that allows attackers to auto-approve denied sh |
| CVE-2026-110204 | 8.8 | 2026-10-13 | Roo Code through 3.54.0 contains a command approval bypass vulnerability that allows attackers to run denied shell comma |
| CVE-2026-110205 | 8.8 | 2026-10-13 | Roo Code through 3.54.0 contains a command approval bypass vulnerability in parseCommandLine() that discards command sub |
| CVE-2026-110206 | 8.8 | 2026-10-13 | Roo Code through 3.54.0 contains a command approval bypass vulnerability in parseCommandLine() that allows attackers to  |
| CVE-2026-110207 | 8.8 | 2026-10-13 | Wukong AICRM through 20260610 contains a missing authorization vulnerability that allows any authenticated user to call  |
| CVE-2026-110208 | 7.1 | 2026-10-13 | Wukong AICRM through 20260610 contains a missing authorization vulnerability in the /systemConfig controller that allows |
| CVE-2026-110211 | 8.1 | 2026-10-13 | iFlytek SkillHub through 0.2.22 contains a missing authorization vulnerability that allows any authenticated user to per |
| CVE-2026-110215 | 8.8 | 2026-10-13 | youlai-boot through 2.21.1 contains a missing authorization vulnerability that allows authenticated users to assign arbi |
| CVE-2026-110216 | 7.1 | 2026-10-13 | youlai-boot through 2.21.1 contains a missing authorization vulnerability that allows any authenticated user to enable o |
| CVE-2026-110220 | 7.1 | 2026-10-13 | Kubeflow Model Registry through 0.3.17 contains a server-side request forgery vulnerability that allows namespace users  |
| CVE-2026-110233 | 7.8 | 2026-10-13 | Rovr through 0.10.3 on Windows contains an OS command injection vulnerability that allows attackers to execute commands  |
| CVE-2026-110236 | 7.0 | 2026-10-13 | KDE Dolphin 24.08.0 through 26.08.2 contains an OS command injection vulnerability that allows attackers to execute comm |
| CVE-2026-110237 | 7.3 | 2026-10-13 | Vifm 0.8.1-beta through 0.14.4 reuses a pre-existing IPC FIFO in the shared temporary directory without checking ownersh |
| CVE-2026-110238 | 8.8 | 2026-10-13 | Rapyd Admin from 9.0.0 before 9.20.0 contains an authorization bypass vulnerability that allows authenticated company me |
| CVE-2026-110255 | 8.5 | 2026-10-13 | Finsys Dockhand before 1.0.43 contains a response-disclosing server-side request forgery vulnerability that allows authe |
| CVE-2026-49785 | 7.8 | 2026-10-13 | Improper resource shutdown or release in Windows UEFI allows an authorized attacker to bypass a security feature locally |
| CVE-2026-58280 | 7.5 | 2026-10-13 | Uncontrolled recursion in .NET allows an unauthorized attacker to deny service over a network. |
| CVE-2026-61931 | 7.8 | 2026-10-13 | Use after free in Windows Perception Simulation Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-68836 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows kernel32.dll allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69326 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Graphic Fonts allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69354 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Error Reporting allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69363 | 8.0 | 2026-10-13 | Heap-based buffer overflow in Windows Error Reporting allows an authorized attacker to elevate privileges over a network |
| CVE-2026-69370 | 8.8 | 2026-10-13 | Improper neutralization of special elements used in a command ('command injection') in Visual Studio Code allows an unau |
| CVE-2026-69387 | 7.0 | 2026-10-13 | Use after free in Windows Error Reporting allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69452 | 7.1 | 2026-10-13 | Use after free in Windows Enterprise App Management allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-69454 | 7.5 | 2026-10-13 | Out-of-bounds read in Microsoft Azure Attestation service and Device Health Attestation Service allows an unauthorized a |
| CVE-2026-69471 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69521 | 8.8 | 2026-10-13 | Integer overflow or wraparound in Windows iSCSI allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69577 | 7.5 | 2026-10-13 | Out-of-bounds read in Microsoft Azure Attestation service and Device Health Attestation Service allows an unauthorized a |
| CVE-2026-69596 | 7.0 | 2026-10-13 | Use after free in Windows Program Compatibility Assistant Service allows an authorized attacker to elevate privileges lo |
| CVE-2026-69633 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Update allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69634 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Windows iSCSI allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69639 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Windows Libarchive allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69650 | 7.8 | 2026-10-13 | Improper verification of cryptographic signature in Windows Key Distribution Center allows an authorized attacker to ele |
| CVE-2026-69651 | 7.5 | 2026-10-13 | Inefficient algorithmic complexity in .NET allows an unauthorized attacker to deny service over a network. |
| CVE-2026-69673 | 7.8 | 2026-10-13 | Improper link resolution before file access ('link following') in Windows Update allows an authorized attacker to elevat |
| CVE-2026-69705 | 9.8 | 2026-10-13 | Out-of-bounds write in Windows iSCSI allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69718 | 7.8 | 2026-10-13 | Improper neutralization of special elements used in a command ('command injection') in Windows Update allows an authoriz |
| CVE-2026-69733 | 7.8 | 2026-10-13 | Untrusted search path in Windows Update allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69736 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Credential Manage |
| CVE-2026-69743 | 7.0 | 2026-10-13 | Use after free in Windows Program Compatibility Assistant Service allows an authorized attacker to elevate privileges lo |
| CVE-2026-69763 | 7.0 | 2026-10-13 | Use after free in Windows Storage allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69765 | 8.8 | 2026-10-13 | Use after free in Windows Storport Miniport Driver allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69766 | 7.0 | 2026-10-13 | Use after free in Windows Storage allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69783 | 7.8 | 2026-10-13 | External control of file name or path in Windows Update allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69789 | 7.5 | 2026-10-13 | Heap-based buffer overflow in Reliable Multicast Transport Driver (RMCAST) allows an unauthorized attacker to execute co |
| CVE-2026-69795 | 7.0 | 2026-10-13 | Null pointer dereference in Windows Clipboard Server allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69798 | 7.8 | 2026-10-13 | Use after free in Windows Wired AutoConfig Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69802 | 8.1 | 2026-10-13 | Weak authentication in Network Device Enrollment Service (NDES) allows an unauthorized attacker to execute code over a n |
| CVE-2026-69830 | 8.1 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows DHCP Server allow |
| CVE-2026-69840 | 7.0 | 2026-10-13 | Use after free in Windows Certificates allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69850 | 7.8 | 2026-10-13 | Untrusted pointer dereference in Windows Certificates allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69856 | 7.0 | 2026-10-13 | Use after free in Windows Storage allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69867 | 7.8 | 2026-10-13 | Out-of-bounds read in SQLite allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69880 | 7.8 | 2026-10-13 | Access of resource using incompatible type ('type confusion') in Desktop Window Manager allows an authorized attacker to |
| CVE-2026-69882 | 7.8 | 2026-10-13 | Untrusted search path in Windows Update allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69883 | 9.8 | 2026-10-13 | Use after free in Windows iSCSI allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69884 | 7.8 | 2026-10-13 | Buffer over-read in Windows GDI allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69886 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Windows Imaging Component allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69898 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69909 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft COM for Windows allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69913 | 8.1 | 2026-10-13 | Use after free in Windows TCP/IP allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69915 | 7.0 | 2026-10-13 | Use after free in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69916 | 7.8 | 2026-10-13 | Integer overflow or wraparound in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69918 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows Core Messaging allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69923 | 7.8 | 2026-10-13 | Uncontrolled search path element in Windows AI allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69926 | 7.8 | 2026-10-13 | Access of resource using incompatible type ('type confusion') in Desktop Window Manager allows an authorized attacker to |
| CVE-2026-69931 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Storage allows an |
| CVE-2026-69934 | 7.8 | 2026-10-13 | Integer overflow or wraparound in Windows Spaceport.sys allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69935 | 7.0 | 2026-10-13 | Use after free in Windows Storage allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69942 | 7.8 | 2026-10-13 | Buffer over-read in Windows Overlay Filter allows an authorized attacker to execute code locally. |
| CVE-2026-69943 | 8.8 | 2026-10-13 | Improper limitation of a pathname to a restricted directory ('path traversal') in Microsoft Office SharePoint allows an  |
| CVE-2026-69945 | 8.8 | 2026-10-13 | Missing authorization in Windows AppX Deployment Extensions allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69949 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Client for NFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69950 | 7.8 | 2026-10-13 | Buffer over-read in Windows Overlay Filter allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69952 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows Overlay Filter allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69953 | 7.8 | 2026-10-13 | Buffer over-read in Windows Overlay Filter allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69957 | 7.8 | 2026-10-13 | Integer overflow or wraparound in Windows Overlay Filter allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69959 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows Overlay Filter allows an authorized attacker to execute code locally. |
| CVE-2026-69963 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Streaming Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69964 | 7.0 | 2026-10-13 | Use after free in Microsoft Streaming Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69966 | 7.8 | 2026-10-13 | Integer overflow or wraparound in Microsoft Streaming Service allows an authorized attacker to elevate privileges locall |
| CVE-2026-69970 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Microsoft Streaming Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69976 | 7.5 | 2026-10-13 | Use after free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69977 | 7.0 | 2026-10-13 | Use after free in Quality Windows Audio/Video Experience (QWAVE) service allows an authorized attacker to elevate privil |
| CVE-2026-69984 | 7.5 | 2026-10-13 | Use after free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69985 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows Libarchive allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69986 | 7.5 | 2026-10-13 | Use after free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69987 | 7.5 | 2026-10-13 | Use after free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69988 | 7.5 | 2026-10-13 | Use after free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69991 | 7.5 | 2026-10-13 | Use after free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69992 | 7.5 | 2026-10-13 | Use after free in Windows Remote Desktop Services allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69994 | 7.5 | 2026-10-13 | Use after free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69995 | 7.5 | 2026-10-13 | Use after free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69996 | 7.5 | 2026-10-13 | Use after free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69997 | 7.5 | 2026-10-13 | Use after free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-69998 | 7.5 | 2026-10-13 | Use after free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70004 | 7.5 | 2026-10-13 | Use after free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70006 | 7.5 | 2026-10-13 | Use after free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70007 | 8.8 | 2026-10-13 | Out-of-bounds write in .NET Framework allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70008 | 7.8 | 2026-10-13 | Integer overflow or wraparound in Windows IP Over USB Service allows an authorized attacker to elevate privileges locall |
| CVE-2026-70010 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70012 | 7.5 | 2026-10-13 | Use after free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70013 | 8.1 | 2026-10-13 | Use after free in Windows iSCSI allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70014 | 7.5 | 2026-10-13 | Use after free in Windows Cryptographic Services allows an authorized attacker to execute code over a network. |
| CVE-2026-70015 | 7.8 | 2026-10-13 | Use after free in Windows Local Security Authority Subsystem Service (LSASS) allows an authorized attacker to elevate pr |
| CVE-2026-70021 | 7.0 | 2026-10-13 | Use after free in Windows Direct Composition allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70023 | 7.8 | 2026-10-13 | Use after free in Windows Hyper-V allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70024 | 9.8 | 2026-10-13 | Stack-based buffer overflow in Windows Internet Information Services allows an unauthorized attacker to execute code ove |
| CVE-2026-70026 | 7.0 | 2026-10-13 | Use after free in Windows Secure Kernel Mode allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70027 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Subsystem for Linux allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70031 | 7.5 | 2026-10-13 | Heap-based buffer overflow in Windows iSCSI allows an unauthorized attacker to deny service over a network. |
| CVE-2026-70033 | 7.5 | 2026-10-13 | Missing release of memory after effective lifetime in Remote Desktop Gateway Service allows an unauthorized attacker to  |
| CVE-2026-70035 | 8.8 | 2026-10-13 | Deserialization of untrusted data in .NET Framework allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70038 | 8.1 | 2026-10-13 | Use after free in Windows iSCSI allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70045 | 7.0 | 2026-10-13 | Use after free in Windows Work Folders allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70048 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Resilient File System (ReFS) allows an authorized attacker to elevate privileges l |
| CVE-2026-70049 | 8.0 | 2026-10-13 | Improper neutralization of special elements used in an sql command ('sql injection') in Microsoft Configuration Manager  |
| CVE-2026-70051 | 7.8 | 2026-10-13 | Access of resource using incompatible type ('type confusion') in Windows SmartScreen allows an authorized attacker to el |
| CVE-2026-70052 | 7.8 | 2026-10-13 | Integer overflow or wraparound in Windows PowerShell allows an authorized attacker to execute code locally. |
| CVE-2026-70054 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows NetBIOS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70056 | 7.0 | 2026-10-13 | Use after free in Windows Update Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70058 | 7.5 | 2026-10-13 | Out-of-bounds write in Windows DHCP Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70059 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows OLE allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70060 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally |
| CVE-2026-70062 | 8.1 | 2026-10-13 | Double free in Windows Libarchive allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70064 | 7.8 | 2026-10-13 | Integer underflow (wrap or wraparound) in Windows Kerberos allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70066 | 7.0 | 2026-10-13 | Use after free in Windows DHCP Server allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70067 | 7.0 | 2026-10-13 | Use after free in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70068 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows Client-Side Caching (CSC) Service allows an unauthorized attacker to elevate privi |
| CVE-2026-70069 | 8.8 | 2026-10-13 | Stack-based buffer overflow in Windows DHCP Server allows an authorized attacker to execute code over a network. |
| CVE-2026-70076 | 7.0 | 2026-10-13 | Use after free in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70079 | 7.5 | 2026-10-13 | Improper enforcement of behavioral workflow in Windows DNS allows an unauthorized attacker to deny service over a networ |
| CVE-2026-70082 | 7.5 | 2026-10-13 | Uncaught exception in Windows DNS allows an unauthorized attacker to deny service over a network. |
| CVE-2026-70086 | 7.0 | 2026-10-13 | Use after free in Microsoft Windows Search Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70089 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows GDI allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70092 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft PostScript Printer Driver allows an unauthorized attacker to elevate privileges  |
| CVE-2026-70093 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Rich Text Edit Control allows an authorized attacker to elevate privileges locally |
| CVE-2026-70095 | 7.5 | 2026-10-13 | Heap-based buffer overflow in Windows iSCSI allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70096 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Windows Rich Text Edit Control allows an unauthorized attacker to execute code over a netw |
| CVE-2026-70102 | 7.8 | 2026-10-13 | Use after free in Windows Spaceport.sys allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70103 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Error Reporting allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70104 | 7.8 | 2026-10-13 | Untrusted pointer dereference in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges loca |
| CVE-2026-70106 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70108 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally |
| CVE-2026-70109 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft PostScript Printer Driver allows an unauthorized attacker to elevate privileges  |
| CVE-2026-70110 | 7.8 | 2026-10-13 | Stack-based buffer overflow in Microsoft PostScript Printer Driver allows an unauthorized attacker to elevate privileges |
| CVE-2026-70111 | 8.1 | 2026-10-13 | Untrusted pointer dereference in Windows Kernel allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-70112 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Spaceport.sys allows an authorized attacker to execute code locally. |
| CVE-2026-70113 | 7.8 | 2026-10-13 | Integer overflow or wraparound in Windows Client for NFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70114 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70115 | 7.0 | 2026-10-13 | Use after free in Microsoft Windows Search Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70117 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally |
| CVE-2026-70118 | 7.0 | 2026-10-13 | Use after free in Windows Audio Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70121 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70123 | 7.8 | 2026-10-13 | Numeric truncation error in Microsoft Graphics Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70126 | 7.1 | 2026-10-13 | Out-of-bounds read in Windows Bluetooth Port Driver allows an unauthorized attacker to execute code over an adjacent net |
| CVE-2026-70127 | 8.1 | 2026-10-13 | Use after free in DNS Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70131 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Windows Media Foundation allows an unauthorized attacker to elevate privileges l |
| CVE-2026-70132 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Portable Device File System Driver allows an authorized attacker to elevate privil |
| CVE-2026-70133 | 7.5 | 2026-10-13 | Allocation of resources without limits or throttling in Windows SMB Server allows an unauthorized attacker to deny servi |
| CVE-2026-70134 | 7.0 | 2026-10-13 | Use after free in Windows Event Tracing allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70136 | 7.0 | 2026-10-13 | Use after free in Microsoft Windows Search Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70138 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows OLE allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70139 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Update Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70140 | 7.0 | 2026-10-13 | Use after free in Windows Audio Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70142 | 7.8 | 2026-10-13 | Untrusted search path in Windows Update Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70143 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Network File System allows an authorized attacker to execute code locally. |
| CVE-2026-70144 | 7.0 | 2026-10-13 | Use after free in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70147 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft PostScript Printer Driver allows an unauthorized attacker to execute code over a |
| CVE-2026-70149 | 8.8 | 2026-10-13 | Exposure of sensitive information to an unauthorized actor in Windows Client Side Caching driver (csc.sys) allows an aut |
| CVE-2026-70150 | 7.0 | 2026-10-13 | Use after free in Microsoft Windows Search Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70151 | 7.8 | 2026-10-13 | Use after free in Windows Direct Composition allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70153 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft PostScript Printer Driver allows an unauthorized attacker to execute code over a |
| CVE-2026-70155 | 7.5 | 2026-10-13 | Missing release of memory after effective lifetime in Windows DNS allows an unauthorized attacker to deny service over a |
| CVE-2026-70156 | 7.0 | 2026-10-13 | Use after free in Microsoft Windows Search Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70157 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Windows System Information Console allows an unauthorized attacker to execute code over a  |
| CVE-2026-70158 | 8.8 | 2026-10-13 | Remote Code Execution in Windows Routing and Remote Access Service (RRAS) allows attacker to gain an unauthorized access |
| CVE-2026-70159 | 7.5 | 2026-10-13 | Allocation of resources without limits or throttling in ASP.NET Core allows an unauthorized attacker to deny service ove |
| CVE-2026-70160 | 7.0 | 2026-10-13 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70161 | 7.3 | 2026-10-13 | Improper limitation of a pathname to a restricted directory ('path traversal') in .NET allows an authorized attacker to  |
| CVE-2026-70163 | 7.5 | 2026-10-13 | Allocation of resources without limits or throttling in OpenSSH for Windows allows an unauthorized attacker to deny serv |
| CVE-2026-70164 | 7.0 | 2026-10-13 | Use after free in Windows TCP/IP allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70167 | 8.8 | 2026-10-13 | Access of resource using incompatible type ('type confusion') in DNS Server allows an authorized attacker to execute cod |
| CVE-2026-70168 | 7.0 | 2026-10-13 | Use after free in Windows Ancillary Function Driver for WinSock allows an authorized attacker to elevate privileges loca |
| CVE-2026-70169 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Connected Devices |
| CVE-2026-70172 | 7.8 | 2026-10-13 | Untrusted pointer dereference in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70174 | 8.8 | 2026-10-13 | Improperly implemented security check for standard in .NET allows an unauthorized attacker to execute code over a networ |
| CVE-2026-70175 | 8.1 | 2026-10-13 | Improper authentication in ASP.NET Core allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-70176 | 7.0 | 2026-10-13 | Use after free in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70177 | 7.8 | 2026-10-13 | Numeric truncation error in Microsoft Windows Search Component allows an authorized attacker to elevate privileges local |
| CVE-2026-70179 | 7.5 | 2026-10-13 | Authentication bypass by spoofing in ASP.NET Core allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-70181 | 7.5 | 2026-10-13 | Allocation of resources without limits or throttling in ASP.NET Core allows an unauthorized attacker to deny service ove |
| CVE-2026-70183 | 7.5 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in ASP.NET Core allows an au |
| CVE-2026-70184 | 7.8 | 2026-10-13 | Improper resolution of path equivalence in Windows Backup Engine allows an authorized attacker to elevate privileges loc |
| CVE-2026-70185 | 8.8 | 2026-10-13 | Protection mechanism failure in Windows PowerShell allows an authorized attacker to bypass a security feature locally. |
| CVE-2026-70186 | 7.5 | 2026-10-13 | Deadlock in ASP.NET Core allows an unauthorized attacker to deny service over a network. |
| CVE-2026-70187 | 8.1 | 2026-10-13 | Use after free in Remote Desktop Gateway Service allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70188 | 9.1 | 2026-10-13 | Inconsistent interpretation of http requests ('http request/response smuggling') in ASP.NET Core allows an unauthorized  |
| CVE-2026-70190 | 7.3 | 2026-10-13 | Improper link resolution before file access ('link following') in .NET allows an authorized attacker to elevate privileg |
| CVE-2026-70197 | 8.1 | 2026-10-13 | Out-of-bounds write in .NET allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70198 | 7.0 | 2026-10-13 | Use after free in Windows Push Notifications allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70202 | 7.5 | 2026-10-13 | Server-side request forgery (ssrf) in Microsoft Office SharePoint allows an authorized attacker to elevate privileges ov |
| CVE-2026-70205 | 7.0 | 2026-10-13 | Access of resource using incompatible type ('type confusion') in Windows Ancillary Function Driver for WinSock allows an |
| CVE-2026-70207 | 7.5 | 2026-10-13 | Heap-based buffer overflow in Network Policy Server (NPS) allows an authorized attacker to execute code over a network. |
| CVE-2026-70209 | 7.0 | 2026-10-13 | Use after free in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70210 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows OLE DB allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-70212 | 7.0 | 2026-10-13 | Improper restriction of communication channel to intended endpoints in Windows Security Center allows an authorized atta |
| CVE-2026-70213 | 8.0 | 2026-10-13 | Origin validation error in Microsoft Power Apps allows an authorized attacker to execute code over a network. |
| CVE-2026-70215 | 8.8 | 2026-10-13 | Use after free in Microsoft Office PowerPoint allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70218 | 7.8 | 2026-10-13 | Insufficient granularity of access control in Windows StateRepository API allows an authorized attacker to elevate privi |
| CVE-2026-70220 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-70222 | 7.8 | 2026-10-13 | Relative path traversal in Windows Shell allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70223 | 7.0 | 2026-10-13 | Use after free in Windows Console Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70225 | 7.8 | 2026-10-13 | Access of resource using incompatible type ('type confusion') in Windows Ancillary Function Driver for WinSock allows an |
| CVE-2026-70228 | 7.8 | 2026-10-13 | Out-of-bounds read in Desktop Window Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70229 | 8.1 | 2026-10-13 | Incorrect authorization in Active Directory Domain Services allows an unauthorized attacker to execute code over a netwo |
| CVE-2026-70230 | 7.0 | 2026-10-13 | Use after free in Windows Audio Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70233 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Common Log File System Driver allows an authorized attacker to elevate privileges  |
| CVE-2026-70236 | 7.0 | 2026-10-13 | Use after free in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70237 | 7.0 | 2026-10-13 | Use after free in Windows Ancillary Function Driver for WinSock allows an authorized attacker to elevate privileges loca |
| CVE-2026-70238 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Storage Spaces Controller allows an authorized attacker to elevate privileges loca |
| CVE-2026-70241 | 7.0 | 2026-10-13 | Use after free in Windows Kerberos allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70242 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70243 | 7.0 | 2026-10-13 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70245 | 7.8 | 2026-10-13 | Access of resource using incompatible type ('type confusion') in Windows Ancillary Function Driver for WinSock allows an |
| CVE-2026-70246 | 8.8 | 2026-10-13 | Incorrect authorization in Microsoft Office SharePoint allows an authorized attacker to elevate privileges over a networ |
| CVE-2026-70247 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows HTTP.sys allows an authorized attacker to execute code locally. |
| CVE-2026-70249 | 7.0 | 2026-10-13 | Use after free in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70250 | 8.8 | 2026-10-13 | Use after free in Windows DHCP Client allows an unauthorized attacker to execute code over an adjacent network. |
| CVE-2026-70251 | 7.5 | 2026-10-13 | Server-side request forgery (ssrf) in Microsoft Office SharePoint allows an authorized attacker to elevate privileges ov |
| CVE-2026-70252 | 7.0 | 2026-10-13 | Use after free in Virtual Hard Disk (VHD) Miniport Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70253 | 7.0 | 2026-10-13 | Use after free in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70254 | 8.8 | 2026-10-13 | Out-of-bounds read in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70255 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Desktop Window Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70256 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70257 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70258 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Windows Media Foundation allows an unauthorized attacker to execute code over a  |
| CVE-2026-70262 | 8.8 | 2026-10-13 | Heap-based buffer overflow in WebDAV allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-70266 | 8.8 | 2026-10-13 | Improper neutralization of special elements used in an sql command ('sql injection') in Microsoft Office SharePoint allo |
| CVE-2026-70267 | 7.2 | 2026-10-13 | Inclusion of functionality from untrusted control sphere in Microsoft Office SharePoint allows an authorized attacker to |
| CVE-2026-70268 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70269 | 8.1 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70271 | 7.0 | 2026-10-13 | Use after free in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70272 | 7.0 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70273 | 7.0 | 2026-10-13 | Use after free in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70274 | 7.8 | 2026-10-13 | Use after free in Windows Bind Filter Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70275 | 8.8 | 2026-10-13 | Untrusted pointer dereference in Windows CD-ROM Driver allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70276 | 7.0 | 2026-10-13 | Use after free in Microsoft Office Click-To-Run allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70278 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Windows Media Foundation allows an authorized attacker to elevate privileges loc |
| CVE-2026-70279 | 9.3 | 2026-10-13 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Exchange Server allows |
| CVE-2026-70281 | 7.5 | 2026-10-13 | Out-of-bounds read in Microsoft Office Outlook allows an unauthorized attacker to disclose information over a network. |
| CVE-2026-70282 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70285 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally |
| CVE-2026-70286 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Win32K - GRFX allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70287 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70291 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70297 | 8.8 | 2026-10-13 | Absolute path traversal in Skype for Business and Microsoft Lync allows an authorized attacker to execute code over a ne |
| CVE-2026-70299 | 8.8 | 2026-10-13 | Improper access control in Windows Bind Filter Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70300 | 9.8 | 2026-10-13 | Untrusted pointer dereference in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70301 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70302 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70303 | 7.8 | 2026-10-13 | Out-of-bounds write in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70343 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft MPEG-2 Video Extension allows an unauthorized attacker to execute code over a ne |
| CVE-2026-70566 | 7.8 | 2026-10-13 | Null pointer dereference in Windows Schannel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70571 | 8.1 | 2026-10-13 | Stack-based buffer overflow in Microsoft Exchange Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70580 | 8.8 | 2026-10-13 | Missing authentication for critical function in Windows Credential Guard allows an authorized attacker to perform spoofi |
| CVE-2026-72934 | 7.0 | 2026-10-13 | Use after free in Windows Program Compatibility Assistant Service allows an authorized attacker to elevate privileges lo |
| CVE-2026-72955 | 7.0 | 2026-10-13 | Use after free in Windows Application Compatibility Cache allows an authorized attacker to elevate privileges locally. |
| CVE-2026-72968 | 7.0 | 2026-10-13 | Use after free in Windows Program Compatibility Assistant Service allows an authorized attacker to elevate privileges lo |
| CVE-2026-72969 | 7.0 | 2026-10-13 | Use after free in Windows Program Compatibility Assistant Service allows an authorized attacker to elevate privileges lo |
| CVE-2026-73027 | 7.8 | 2026-10-13 | External control of system or configuration setting in Windows Setup Files Cleanup allows an authorized attacker to elev |
| CVE-2026-77496 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows Imaging Component allows an unauthorized attacker to execute code over a network. |
| CVE-2026-77902 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-77910 | 8.8 | 2026-10-13 | Incorrect authorization in Microsoft Exchange Server allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-78459 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Internet Information Services allows an authorized attacker to elevate privileges  |
| CVE-2026-81969 | 7.8 | 2026-10-13 | Insufficient granularity of access control in Windows Server Update Service allows an authorized attacker to elevate pri |
| CVE-2026-81971 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows NTFS allows an au |
| CVE-2026-83499 | 7.8 | 2026-10-13 | Insufficient granularity of access control in Windows Server Update Service allows an authorized attacker to elevate pri |
| CVE-2026-83505 | 7.0 | 2026-10-13 | Time-of-check time-of-use (toctou) race condition in Windows Setup Files Cleanup allows an authorized attacker to elevat |
| CVE-2026-83506 | 7.8 | 2026-10-13 | Untrusted search path in Servicing Stack Updates allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83508 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83509 | 7.0 | 2026-10-13 | Untrusted search path in Windows Setup Files Cleanup allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83510 | 7.0 | 2026-10-13 | Time-of-check time-of-use (toctou) race condition in Windows Setup Files Cleanup allows an authorized attacker to elevat |
| CVE-2026-83511 | 7.4 | 2026-10-13 | Weak authentication in Active Directory Federation Services (AD FS) allows an unauthorized attacker to perform spoofing  |
| CVE-2026-83513 | 7.8 | 2026-10-13 | Use after free in Windows Universal Disk Format File System Driver (UDFS) allows an authorized attacker to elevate privi |
| CVE-2026-83514 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Partition Management Driver allows an authorized attacker to elevate privileges lo |
| CVE-2026-83516 | 7.5 | 2026-10-13 | Out-of-bounds read in Windows Local Security Authority Subsystem Service (LSASS) allows an unauthorized attacker to deny |
| CVE-2026-83517 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Windows Media Foundation allows an unauthorized attacker to execute code over a  |
| CVE-2026-83518 | 7.8 | 2026-10-13 | Heap-based buffer overflow in RPC Runtime allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83519 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Windows Error Reporting allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83520 | 8.8 | 2026-10-13 | Deserialization of untrusted data in .NET allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83522 | 8.1 | 2026-10-13 | Reliance on untrusted inputs in a security decision in Windows IKE Extension allows an unauthorized attacker to perform  |
| CVE-2026-83523 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows Image Acquisition allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83564 | 7.0 | 2026-10-13 | Use after free in Microsoft Windows Search Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83566 | 7.0 | 2026-10-13 | Use after free in Windows Win32K - ICOMP allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83567 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83568 | 7.8 | 2026-10-13 | Improper access control in Windows Kernel-Mode Drivers allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83569 | 7.8 | 2026-10-13 | Heap-based buffer overflow in HID Parser Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83570 | 7.8 | 2026-10-13 | Use after free in Microsoft Windows Search Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83574 | 7.0 | 2026-10-13 | Use after free in Microsoft Windows Search Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83575 | 7.0 | 2026-10-13 | Use after free in Microsoft Windows Search Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83578 | 9.8 | 2026-10-13 | Integer underflow (wrap or wraparound) in Windows PowerShell allows an unauthorized attacker to execute code over a netw |
| CVE-2026-83579 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Smart Card allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83580 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Windows Client-Side Caching (CSC) Service allows an authorized attacker to elevate privile |
| CVE-2026-83583 | 7.8 | 2026-10-13 | Improper access control in Windows Geotag Broker allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83584 | 7.0 | 2026-10-13 | Use after free in Windows Smart Card allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83585 | 7.8 | 2026-10-13 | Use of externally-controlled format string in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83586 | 7.8 | 2026-10-13 | Weak authentication in Windows Resilient File System (ReFS) Deduplication Service allows an authorized attacker to eleva |
| CVE-2026-83587 | 7.8 | 2026-10-13 | Untrusted pointer dereference in Windows Core Messaging allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83588 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows USB Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83634 | 7.8 | 2026-10-13 | Double free in Windows BitLocker allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83635 | 7.5 | 2026-10-13 | Out-of-bounds read in DNS Server allows an unauthorized attacker to deny service over a network. |
| CVE-2026-83637 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows Kernel-Mode Drivers allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83638 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows USB Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83639 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Sensor Data Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83640 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows NTFS allows an authorized attacker to execute code locally. |
| CVE-2026-83641 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Media allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83642 | 8.8 | 2026-10-13 | Access of resource using incompatible type ('type confusion') in DNS Server allows an unauthorized attacker to execute c |
| CVE-2026-83643 | 8.8 | 2026-10-13 | Stack-based buffer overflow in Windows Error Reporting allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83644 | 7.0 | 2026-10-13 | Use after free in Windows Audio Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83645 | 7.5 | 2026-10-13 | Allocation of resources without limits or throttling in Active Directory Federation Services (AD FS) allows an unauthori |
| CVE-2026-83647 | 7.5 | 2026-10-13 | Out-of-bounds read in Active Directory Domain Services allows an unauthorized attacker to deny service over a network. |
| CVE-2026-83650 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Media allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83652 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83654 | 7.8 | 2026-10-13 | Missing authentication for critical function in Windows Modern Device Management (MDM) allows an authorized attacker to  |
| CVE-2026-83655 | 7.5 | 2026-10-13 | Out-of-bounds read in Network Policy Server (NPS) allows an unauthorized attacker to deny service over a network. |
| CVE-2026-83659 | 7.8 | 2026-10-13 | Improper link resolution before file access ('link following') in Windows User Profile Service allows an authorized atta |
| CVE-2026-83665 | 7.5 | 2026-10-13 | Null pointer dereference in Windows DHCP Server allows an unauthorized attacker to deny service over a network. |
| CVE-2026-83666 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Active Directory Certific |
| CVE-2026-83669 | 7.8 | 2026-10-13 | Use of uninitialized resource in Windows Error Reporting allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83670 | 7.5 | 2026-10-13 | Out-of-bounds read in Function Discovery Service (fdwsd.dll) allows an unauthorized attacker to disclose information ove |
| CVE-2026-83674 | 8.1 | 2026-10-13 | Weak authentication in Active Directory Federation Services (AD FS) allows an unauthorized attacker to perform spoofing  |
| CVE-2026-83675 | 7.0 | 2026-10-13 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83676 | 7.0 | 2026-10-13 | Integer underflow (wrap or wraparound) in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83677 | 7.5 | 2026-10-13 | Missing release of memory after effective lifetime in Windows DHCP Client allows an unauthorized attacker to deny servic |
| CVE-2026-83678 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows TCP/IP allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83679 | 7.8 | 2026-10-13 | Use after free in Windows Defender Firewall Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83680 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83682 | 7.0 | 2026-10-13 | Use after free in Windows TCP/IP allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83687 | 7.0 | 2026-10-13 | Use after free in Windows Connected User Experiences and Telemetry allows an authorized attacker to elevate privileges l |
| CVE-2026-83688 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83689 | 7.0 | 2026-10-13 | Use after free in Windows Error Reporting allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83690 | 7.8 | 2026-10-13 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83691 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows DHCP Server allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83692 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Bind Filter Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83693 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Windows Error Reporting allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83694 | 7.0 | 2026-10-13 | Out-of-bounds read in Windows Volume Manager Extension Driver allows an authorized attacker to elevate privileges locall |
| CVE-2026-83696 | 7.0 | 2026-10-13 | Use after free in Windows Cloud Files Mini Filter Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83698 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Client-Side Caching (CSC) Service allows an authorized attacker to elevate privile |
| CVE-2026-83699 | 7.8 | 2026-10-13 | Stack-based buffer overflow in Windows Client-Side Caching (CSC) Service allows an authorized attacker to elevate privil |
| CVE-2026-83700 | 7.8 | 2026-10-13 | Use after free in Windows Now Playing Session Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83701 | 7.0 | 2026-10-13 | Use after free in Windows Now Playing Session Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83702 | 7.0 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83704 | 7.8 | 2026-10-13 | Improper link resolution before file access ('link following') in Microsoft Windows Search Component allows an authorize |
| CVE-2026-83707 | 7.0 | 2026-10-13 | Use after free in Windows Event Tracing allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83708 | 7.0 | 2026-10-13 | Stack-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83709 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows NTLM allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83710 | 7.0 | 2026-10-13 | Use after free in Windows Device Association Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83712 | 7.8 | 2026-10-13 | Out-of-bounds write in Windows NTFS allows an authorized attacker to execute code locally. |
| CVE-2026-83715 | 7.1 | 2026-10-13 | Missing authentication for critical function in Windows Error Reporting allows an authorized attacker to perform tamperi |
| CVE-2026-83716 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows Hyper-V allows an authorized attacker to execute code locally. |
| CVE-2026-83717 | 7.0 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83718 | 7.0 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83720 | 7.0 | 2026-10-13 | Use after free in Windows Kerberos allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83721 | 7.8 | 2026-10-13 | Use after free in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83722 | 7.0 | 2026-10-13 | Use after free in Microsoft Local Security Authority Server (lsasrv) allows an authorized attacker to elevate privileges |
| CVE-2026-83724 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Windows Management Instrumentation allows an authorized attacker to elevate privileges loc |
| CVE-2026-83725 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Windows Search Component allows an unauthorized attacker to execute code over a  |
| CVE-2026-83726 | 7.8 | 2026-10-13 | Use after free in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83727 | 7.8 | 2026-10-13 | Buffer over-read in Windows Overlay Filter allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83728 | 8.8 | 2026-10-13 | Improper validation of syntactic correctness of input in Windows Hyper-V allows an authorized attacker to perform spoofi |
| CVE-2026-83732 | 7.8 | 2026-10-13 | Use after free in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83735 | 7.8 | 2026-10-13 | Release of invalid pointer or reference in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83738 | 7.0 | 2026-10-13 | Use after free in Windows Ancillary Function Driver for WinSock allows an authorized attacker to elevate privileges loca |
| CVE-2026-83739 | 7.5 | 2026-10-13 | Use after free in Windows Bluetooth Service allows an unauthorized attacker to execute code over an adjacent network. |
| CVE-2026-83740 | 7.0 | 2026-10-13 | Use after free in Windows Hello allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83741 | 7.8 | 2026-10-13 | Use after free in Internet Explorer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83746 | 8.1 | 2026-10-13 | Absolute path traversal in Skype for Business and Microsoft Lync allows an authorized attacker to elevate privileges ove |
| CVE-2026-83748 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Windows Error Reporting allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83749 | 7.0 | 2026-10-13 | Use after free in Windows Overlay Filter allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83750 | 7.0 | 2026-10-13 | Time-of-check time-of-use (toctou) race condition in Windows Error Reporting allows an authorized attacker to elevate pr |
| CVE-2026-83751 | 7.0 | 2026-10-13 | Use after free in Windows MIDI Service Module allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83752 | 7.0 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83753 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Camera Frame Server Monitor allows an authorized attacker to elevate privileges lo |
| CVE-2026-83754 | 7.5 | 2026-10-13 | Heap-based buffer overflow in OpenSSH for Windows allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83756 | 7.8 | 2026-10-13 | Use after free in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83757 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83758 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Error Reporting allows an authorized attacker to execute code locally. |
| CVE-2026-83759 | 8.8 | 2026-10-13 | Improper control of generation of code ('code injection') in Windows Encrypting File System (EFS) allows an authorized a |
| CVE-2026-83761 | 7.8 | 2026-10-13 | Use after free in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83762 | 7.8 | 2026-10-13 | Use after free in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83763 | 7.8 | 2026-10-13 | Access of resource using incompatible type ('type confusion') in Windows Input System allows an authorized attacker to e |
| CVE-2026-83767 | 7.8 | 2026-10-13 | Stack-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83768 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83769 | 7.8 | 2026-10-13 | Use after free in OpenSSH for Windows allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83770 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Windows Text Shaping allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83771 | 8.8 | 2026-10-13 | Use after free in Windows Camera Frame Server Monitor allows an unauthorized attacker to elevate privileges over an adja |
| CVE-2026-83775 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Installer allows  |
| CVE-2026-83777 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows Bluetooth Service allows an unauthorized attacker to elevate privileges over an ad |
| CVE-2026-83778 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Internet Messaging API allows an unauthorized attacker to execute code over a ne |
| CVE-2026-83779 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83780 | 9.8 | 2026-10-13 | Use after free in Windows CCFFilter Driver allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83781 | 7.8 | 2026-10-13 | Improper null termination in Windows Program Compatibility Assistant Service allows an authorized attacker to elevate pr |
| CVE-2026-83782 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Windows Shell allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83783 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Management Instrumentation allows an authorized attacker to elevate privileges loc |
| CVE-2026-83784 | 8.8 | 2026-10-13 | Absolute path traversal in Windows Encrypting File System (EFS) allows an authorized attacker to elevate privileges over |
| CVE-2026-83785 | 7.0 | 2026-10-13 | Use after free in Windows COM+ Event System Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83789 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows SMB Client allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-83790 | 7.0 | 2026-10-13 | Use after free in Windows Hello allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83791 | 7.8 | 2026-10-13 | Improper authorization in Windows Virtual Input allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83792 | 7.8 | 2026-10-13 | Incorrect authorization in Windows Device Install Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83793 | 7.0 | 2026-10-13 | Improper link resolution before file access ('link following') in Windows Update Orchestrator Service allows an authoriz |
| CVE-2026-83795 | 7.5 | 2026-10-13 | Heap-based buffer overflow in Windows IKE Extension allows an unauthorized attacker to deny service over a network. |
| CVE-2026-83796 | 7.8 | 2026-10-13 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83797 | 8.8 | 2026-10-13 | Out-of-bounds read in Windows Partition Management Driver allows an unauthorized attacker to execute code over a network |
| CVE-2026-83826 | 7.8 | 2026-10-13 | Untrusted pointer dereference in Windows Error Reporting allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83827 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Windows Bluetooth Port Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83828 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows MIDI Service Module allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83829 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Windows Search Component allows an authorized attacker to elevate privileges loc |
| CVE-2026-83830 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows COM+ Event System Service allows an authorized attacker to elevate privileges loca |
| CVE-2026-83832 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows Spaceport.sys allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83833 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83834 | 7.0 | 2026-10-13 | Use after free in Windows Kernel-Mode Drivers allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83836 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Event Tracing allows an unauthorized attacker to execute code locally. |
| CVE-2026-83837 | 7.8 | 2026-10-13 | Improper access control in Windows Kernel-Mode Drivers allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83838 | 8.0 | 2026-10-13 | Integer underflow (wrap or wraparound) in Windows Bluetooth A2DP driver allows an authorized attacker to elevate privile |
| CVE-2026-83839 | 7.0 | 2026-10-13 | Time-of-check time-of-use (toctou) race condition in Windows Hyper-V allows an authorized attacker to elevate privileges |
| CVE-2026-83840 | 7.8 | 2026-10-13 | Weak authentication in Windows Error Reporting allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83841 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Win32K allows an  |
| CVE-2026-83842 | 7.0 | 2026-10-13 | Double free in Windows TCP/IP allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83843 | 7.5 | 2026-10-13 | Out-of-bounds read in Windows Internet Key Exchange (IKE) Protocol allows an unauthorized attacker to deny service over  |
| CVE-2026-83844 | 8.1 | 2026-10-13 | Out-of-bounds read in Windows Paint allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83845 | 8.4 | 2026-10-13 | Improper privilege management in Windows Internet (wininet.dll) allows an authorized attacker to perform spoofing locall |
| CVE-2026-83846 | 7.0 | 2026-10-13 | Use after free in Connected Devices Platform Service (Cdpsvc) allows an authorized attacker to elevate privileges locall |
| CVE-2026-83847 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Account allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83848 | 7.8 | 2026-10-13 | Untrusted pointer dereference in Windows COM+ Event System Service allows an authorized attacker to elevate privileges l |
| CVE-2026-83850 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Windows Search Component allows an authorized attacker to elevate privileges loc |
| CVE-2026-83851 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows Partition Management Driver allows an unauthorized attacker to elevate privileges  |
| CVE-2026-83852 | 7.0 | 2026-10-13 | Use after free in Windows Bind Filter Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83853 | 7.0 | 2026-10-13 | Use after free in Windows Hello allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83855 | 7.5 | 2026-10-13 | Integer underflow (wrap or wraparound) in Windows WLAN Service allows an unauthorized attacker to deny service over a ne |
| CVE-2026-83856 | 7.5 | 2026-10-13 | Out-of-bounds read in Windows Event Logging Service allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83857 | 7.8 | 2026-10-13 | Use after free in Windows Universal Disk Format File System Driver (UDFS) allows an authorized attacker to elevate privi |
| CVE-2026-83859 | 7.8 | 2026-10-13 | Use after free in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83860 | 7.5 | 2026-10-13 | Stack-based buffer overflow in Windows GDI allows an unauthorized attacker to deny service over a network. |
| CVE-2026-83861 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Remote Desktop Protocol allows an authorized attacker to elevate privileges locall |
| CVE-2026-83862 | 9.8 | 2026-10-13 | Use after free in Windows Network Load Balancing allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83863 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Servicing Stack Updates allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83866 | 7.0 | 2026-10-13 | Use after free in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83867 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Push Notifications allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83868 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Microsoft Bluetooth Drive |
| CVE-2026-83869 | 9.8 | 2026-10-13 | Integer underflow (wrap or wraparound) in DNS Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83871 | 7.0 | 2026-10-13 | Heap-based buffer overflow in OpenSSH for Windows allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83872 | 7.8 | 2026-10-13 | Incorrect conversion between numeric types in Windows TCP/IP allows an authorized attacker to elevate privileges locally |
| CVE-2026-83873 | 7.8 | 2026-10-13 | Relative path traversal in Windows Shell allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83874 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows Event Tracing allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83876 | 7.8 | 2026-10-13 | Use after free in Windows Shell allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83877 | 7.8 | 2026-10-13 | Integer overflow or wraparound in HID Parser Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83879 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Overlay Filter al |
| CVE-2026-83881 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows exFAT File System allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83882 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83883 | 7.8 | 2026-10-13 | Use after free in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83886 | 7.0 | 2026-10-13 | Use after free in Windows Update Orchestrator Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83889 | 8.8 | 2026-10-13 | Release of invalid pointer or reference in DNS Server allows an authorized attacker to execute code over a network. |
| CVE-2026-83891 | 8.8 | 2026-10-13 | Stack-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83896 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Direct Composition allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83899 | 7.0 | 2026-10-13 | Improper privilege management in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83900 | 7.0 | 2026-10-13 | Use after free in Windows Bind Filter Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83901 | 7.0 | 2026-10-13 | Use after free in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83902 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Direct Composition allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83903 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Direct Composition allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83908 | 7.0 | 2026-10-13 | Release of invalid pointer or reference in RPC Runtime allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83910 | 9.8 | 2026-10-13 | Out-of-bounds write in RPC Runtime allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83911 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Windows Storage allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83912 | 7.8 | 2026-10-13 | Use after free in Windows Direct Composition allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83913 | 7.8 | 2026-10-13 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83914 | 8.1 | 2026-10-13 | Use after free in Microsoft XML allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83915 | 7.0 | 2026-10-13 | Use after free in Windows Diagnostic Policy Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83916 | 7.0 | 2026-10-13 | Double free in Windows Error Reporting allows an authorized attacker to execute code locally. |
| CVE-2026-83917 | 7.0 | 2026-10-13 | Use after free in Windows ALPC allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83918 | 7.8 | 2026-10-13 | Integer overflow or wraparound in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83919 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Internet Messaging API allows an authorized attacker to execute code locally. |
| CVE-2026-83920 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Windows Search Component allows an authorized attacker to elevate privileges loc |
| CVE-2026-83921 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Microsoft Windows Search Component allows an authorized attacker to elevate privileges loc |
| CVE-2026-83922 | 7.8 | 2026-10-13 | Use after free in Windows Direct Composition allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83923 | 8.8 | 2026-10-13 | Relative path traversal in OpenSSH for Windows allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83924 | 7.0 | 2026-10-13 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83927 | 7.8 | 2026-10-13 | Improper link resolution before file access ('link following') in Windows Registry allows an authorized attacker to elev |
| CVE-2026-83928 | 8.8 | 2026-10-13 | Out-of-bounds write in Windows Local Security Authority Subsystem Service (LSASS) allows an unauthorized attacker to exe |
| CVE-2026-83929 | 8.8 | 2026-10-13 | Out-of-bounds write in Windows GDI allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83930 | 7.0 | 2026-10-13 | Use after free in Windows Update Orchestrator Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83931 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Hyper-V allows an authorized attacker to execute code locally. |
| CVE-2026-83932 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Group Policy allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83934 | 8.8 | 2026-10-13 | Stack-based buffer overflow in Windows GDI+ allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83935 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft XML allows an unauthorized attacker to execute code over a network. |
| CVE-2026-84008 | 7.5 | 2026-10-13 | Inefficient algorithmic complexity in .NET allows an unauthorized attacker to deny service over a network. |
| CVE-2026-84012 | 8.1 | 2026-10-13 | Double free in Remote Desktop Gateway Service allows an unauthorized attacker to execute code over a network. |
| CVE-2026-84013 | 7.8 | 2026-10-13 | Use after free in Windows Telephony Server allows an authorized attacker to elevate privileges locally. |
| CVE-2026-84014 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Windows Device Association Service allows an authorized attacker to elevate privileges loc |
| CVE-2026-84015 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Remote Access Point-to-Point Protocol (PPP) EAP-TLS allows an unauthorized attacker to exe |
| CVE-2026-84016 | 7.8 | 2026-10-13 | Out-of-bounds write in Windows EAPHost Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-84017 | 7.5 | 2026-10-13 | Null pointer dereference in Windows Routing and Remote Access Service (RRAS) allows an unauthorized attacker to deny ser |
| CVE-2026-84018 | 7.0 | 2026-10-13 | Use after free in Windows Print Spooler Components allows an authorized attacker to elevate privileges locally. |
| CVE-2026-84019 | 7.0 | 2026-10-13 | Use after free in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileges locally. |
| CVE-2026-84020 | 7.0 | 2026-10-13 | Use after free in Windows Routing and Remote Access Service (RRAS) allows an authorized attacker to elevate privileges l |
| CVE-2026-85318 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Servicing Stack Updates allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85319 | 7.5 | 2026-10-13 | Allocation of resources without limits or throttling in Active Directory Federation Services (AD FS) allows an unauthori |
| CVE-2026-85321 | 7.5 | 2026-10-13 | Allocation of resources without limits or throttling in Active Directory Federation Services (AD FS) allows an unauthori |
| CVE-2026-85322 | 7.5 | 2026-10-13 | Use of uninitialized resource in Windows Routing and Remote Access Service (RRAS) allows an unauthorized attacker to dis |
| CVE-2026-85324 | 7.5 | 2026-10-13 | Memory allocation with excessive size value in Active Directory Federation Services (AD FS) allows an unauthorized attac |
| CVE-2026-85327 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Print Spooler Components allows an authorized attacker to elevate privileges local |
| CVE-2026-85328 | 7.0 | 2026-10-13 | Weak authentication in Windows Projected File System allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85329 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Microsoft Account allows  |
| CVE-2026-85332 | 7.8 | 2026-10-13 | Use after free in Windows Device Association Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85334 | 7.5 | 2026-10-13 | Out-of-bounds read in Windows Message Queuing Queue Manager allows an unauthorized attacker to disclose information over |
| CVE-2026-85338 | 7.8 | 2026-10-13 | Out-of-bounds read in Microsoft Graphics Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85339 | 8.8 | 2026-10-13 | Remote Code Execution in Windows Routing and Remote Access Service (RRAS) allows attacker to gain an unauthorized access |
| CVE-2026-85340 | 7.8 | 2026-10-13 | Use after free in Microsoft Office Click-To-Run allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85341 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows USB Video Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85342 | 7.0 | 2026-10-13 | Use after free in Windows Device Association Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85343 | 7.8 | 2026-10-13 | Improper link resolution before file access ('link following') in Windows Hyper-V allows an authorized attacker to eleva |
| CVE-2026-85352 | 7.0 | 2026-10-13 | Use after free in Windows Device Association Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85353 | 7.5 | 2026-10-13 | Out-of-bounds read in Windows Print Spooler Components allows an unauthorized attacker to disclose information over a ne |
| CVE-2026-85354 | 7.0 | 2026-10-13 | Use after free in Windows Error Reporting allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85355 | 7.0 | 2026-10-13 | Inclusion of functionality from untrusted control sphere in Windows Common Log File System Driver allows an authorized a |
| CVE-2026-85356 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows Volume Manager Extension Driver allows an authorized attacker to elevate privileges locall |
| CVE-2026-85357 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Phone Service all |
| CVE-2026-85358 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85359 | 7.8 | 2026-10-13 | Improper control of generation of code ('code injection') in Windows Performance Monitor allows an authorized attacker t |
| CVE-2026-85361 | 7.0 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85362 | 7.0 | 2026-10-13 | Release of invalid pointer or reference in Windows Management Instrumentation allows an authorized attacker to elevate p |
| CVE-2026-85363 | 8.8 | 2026-10-13 | Integer overflow or wraparound in .NET Framework allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-85364 | 7.0 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85365 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Servicing Stack Updates allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85366 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85367 | 7.0 | 2026-10-13 | Use after free in Windows Cash Drawer Protocol Provider allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85368 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows TCP/IP allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85369 | 8.2 | 2026-10-13 | Out-of-bounds read in Windows Hyper-V allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85370 | 7.0 | 2026-10-13 | Use after free in WebDAV allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85371 | 8.1 | 2026-10-13 | Use after free in Network Policy Server (NPS) allows an unauthorized attacker to execute code over a network. |
| CVE-2026-85372 | 7.0 | 2026-10-13 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85373 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Universal Plug and Play (UPnP) Device Host allows an authorized attacker to elevat |
| CVE-2026-85375 | 7.8 | 2026-10-13 | Use after free in Windows Universal Plug and Play (UPnP) Device Host allows an authorized attacker to elevate privileges |
| CVE-2026-85376 | 7.8 | 2026-10-13 | Weak authentication in Windows Print Spooler Components allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85377 | 7.8 | 2026-10-13 | Access of resource using incompatible type ('type confusion') in Windows CD-ROM Driver allows an authorized attacker to  |
| CVE-2026-85791 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Windows Encrypting File System (EFS) allows an authorized attacker to elevate privileges l |
| CVE-2026-85792 | 9.8 | 2026-10-13 | Remote Code Execution in Windows Routing and Remote Access Service (RRAS) allows attacker to gain an unauthorized access |
| CVE-2026-85795 | 7.8 | 2026-10-13 | Use after free in Windows Text Services Framework allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85796 | 7.8 | 2026-10-13 | Numeric truncation error in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85798 | 7.2 | 2026-10-13 | Heap-based buffer overflow in Windows Distributed File System (DFS) allows an authorized attacker to execute code over a |
| CVE-2026-85799 | 8.1 | 2026-10-13 | Use after free in Network Policy Server (NPS) allows an unauthorized attacker to execute code over a network. |
| CVE-2026-85800 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Error Reporting allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85802 | 7.0 | 2026-10-13 | Use after free in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85803 | 7.0 | 2026-10-13 | Use after free in Windows Camera Frame Server Monitor allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85804 | 7.8 | 2026-10-13 | Use after free in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85806 | 9.8 | 2026-10-13 | Integer underflow (wrap or wraparound) in Network Policy Server (NPS) allows an unauthorized attacker to execute code ov |
| CVE-2026-85807 | 7.8 | 2026-10-13 | Integer overflow or wraparound in Windows USB Video Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85808 | 7.5 | 2026-10-13 | Out-of-bounds read in Windows Routing and Remote Access Service (RRAS) allows an unauthorized attacker to deny service o |
| CVE-2026-85809 | 9.8 | 2026-10-13 | Remote Code Execution in Windows Routing and Remote Access Service (RRAS) allows attacker to gain an unauthorized access |
| CVE-2026-85810 | 7.0 | 2026-10-13 | Use after free in Windows Telephony Server allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85811 | 7.5 | 2026-10-13 | Use after free in Network Policy Server (NPS) allows an unauthorized attacker to execute code over an adjacent network. |
| CVE-2026-85814 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Windows Media Foundation allows an unauthorized attacker to execute code over a  |
| CVE-2026-85817 | 8.8 | 2026-10-13 | Reliance on untrusted inputs in a security decision in Windows PowerShell allows an unauthorized attacker to execute cod |
| CVE-2026-85818 | 9.0 | 2026-10-13 | Improper verification of cryptographic signature in Windows Schannel allows an unauthorized attacker to perform spoofing |
| CVE-2026-85820 | 7.8 | 2026-10-13 | Use after free in Windows Universal Disk Format File System Driver (UDFS) allows an authorized attacker to elevate privi |
| CVE-2026-85822 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows exFAT File System allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85823 | 7.0 | 2026-10-13 | Use after free in Windows Composite Image File System allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85824 | 7.0 | 2026-10-13 | Use after free in Windows Composite Image File System allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85825 | 7.0 | 2026-10-13 | Use after free in Windows Universal Disk Format File System Driver (UDFS) allows an authorized attacker to elevate privi |
| CVE-2026-85826 | 7.0 | 2026-10-13 | Out-of-bounds write in Windows Fast FAT Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85827 | 7.0 | 2026-10-13 | Heap-based buffer overflow in WebDAV allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85828 | 7.0 | 2026-10-13 | Heap-based buffer overflow in WebDAV allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85829 | 7.8 | 2026-10-13 | Double free in Windows Wired AutoConfig Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85832 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Background Intelligent Transfer Service (BITS) allows an authorized attacker to el |
| CVE-2026-85833 | 7.8 | 2026-10-13 | Use after free in Windows Modern Device Management (MDM) allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85834 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Windows TCP/IP allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85836 | 7.8 | 2026-10-13 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85837 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85842 | 7.8 | 2026-10-13 | Use of externally-controlled format string in Windows Image Acquisition allows an authorized attacker to elevate privile |
| CVE-2026-85843 | 7.8 | 2026-10-13 | Use of uninitialized resource in Windows Background Intelligent Transfer Service (BITS) allows an authorized attacker to |
| CVE-2026-85846 | 7.0 | 2026-10-13 | Use after free in Windows Web Account Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85848 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Background Intelligent Transfer Service (BITS) allows an authorized attacker to el |
| CVE-2026-85849 | 7.8 | 2026-10-13 | Improper link resolution before file access ('link following') in Windows AppX Deployment Service allows an authorized a |
| CVE-2026-85850 | 7.8 | 2026-10-13 | Release of invalid pointer or reference in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85851 | 7.8 | 2026-10-13 | Use after free in Windows SmartScreen allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85853 | 7.0 | 2026-10-13 | Out-of-bounds read in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85854 | 7.0 | 2026-10-13 | Use after free in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85855 | 7.0 | 2026-10-13 | Use after free in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85856 | 7.1 | 2026-10-13 | Heap-based buffer overflow in Windows Internet Connection Sharing (ICS) allows an authorized attacker to execute code ov |
| CVE-2026-85858 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85860 | 7.8 | 2026-10-13 | Use after free in Windows Message Queuing Queue Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85861 | 7.8 | 2026-10-13 | Use after free in Windows Clipboard User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85863 | 7.8 | 2026-10-13 | Use after free in Windows Clipboard User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85864 | 7.8 | 2026-10-13 | Improper privilege management in Python allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85867 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Remote Access Connection Manager allows an authorized attacker to elevate privileg |
| CVE-2026-85868 | 7.0 | 2026-10-13 | Use after free in Windows Common Log File System Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85869 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Windows Search Component allows an authorized attacker to elevate privileges loc |
| CVE-2026-85870 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Windows Common Log File System Driver allows an authorized attacker to elevate privileges  |
| CVE-2026-85871 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Kernel-Mode Drivers allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85872 | 7.8 | 2026-10-13 | Use after free in Windows Storage VSP Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85874 | 7.8 | 2026-10-13 | Use after free in Windows Message Queuing Queue Manager allows an authorized attacker to execute code locally. |
| CVE-2026-85879 | 7.0 | 2026-10-13 | Time-of-check time-of-use (toctou) race condition in Windows Subsystem for Linux allows an authorized attacker to elevat |
| CVE-2026-85881 | 8.0 | 2026-10-13 | Stack-based buffer overflow in Microsoft Graphics Component allows an authorized attacker to elevate privileges over a n |
| CVE-2026-85884 | 7.8 | 2026-10-13 | Missing authentication for critical function in Windows Health and Optimized Experiences Service allows an authorized at |
| CVE-2026-85891 | 7.5 | 2026-10-13 | Exposure of sensitive information to an unauthorized actor in Azure HDInsight allows an unauthorized attacker to disclos |
| CVE-2026-85900 | 8.8 | 2026-10-13 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a ne |
| CVE-2026-85901 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Win32K - GRFX allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85902 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Direct Composition allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85903 | 8.8 | 2026-10-13 | Untrusted pointer dereference in DNS Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-85904 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Device Associatio |
| CVE-2026-85905 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows UI Immersive Server allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85906 | 7.8 | 2026-10-13 | Use after free in Windows Direct Composition allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85908 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Win32K - GRFX allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85911 | 7.8 | 2026-10-13 | Use after free in Windows StateRepository API allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85912 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Clipboard User Se |
| CVE-2026-85914 | 7.0 | 2026-10-13 | Use after free in Windows Embedded Mode Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85915 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows PCI Bus Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85918 | 7.0 | 2026-10-13 | Use after free in Windows Universal Plug and Play (UPnP) Device Host allows an authorized attacker to elevate privileges |
| CVE-2026-85920 | 7.0 | 2026-10-13 | Time-of-check time-of-use (toctou) race condition in Windows BitLocker allows an authorized attacker to elevate privileg |
| CVE-2026-85922 | 7.4 | 2026-10-13 | Weak authentication in Azure Key Vault allows an unauthorized attacker to bypass a security feature over a network. |
| CVE-2026-85925 | 8.2 | 2026-10-13 | Improper restriction of communication channel to intended endpoints in Azure Key Vault allows an authorized attacker to  |
| CVE-2026-85926 | 8.1 | 2026-10-13 | Use after free in Windows Secure Socket Tunneling Protocol (SSTP) allows an unauthorized attacker to execute code over a |
| CVE-2026-85927 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Universal Plug and Play (UPnP) Device Host allows an authorized attacker to elevat |
| CVE-2026-85928 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Windows Volume Manager Extension Driver allows an unauthorized attacker to execute code ov |
| CVE-2026-85930 | 7.0 | 2026-10-13 | Use after free in Windows Image Acquisition allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85931 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows Distributed File System (DFS) allows an authorized attacker to execute code over a |
| CVE-2026-85933 | 7.8 | 2026-10-13 | Use after free in Windows Print Spooler Components allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85934 | 7.0 | 2026-10-13 | Use after free in Windows AppX Deployment Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85936 | 8.8 | 2026-10-13 | Double free in Windows Shell allows an unauthorized attacker to execute code over a network. |
| CVE-2026-85941 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Installer allows  |
| CVE-2026-85943 | 7.0 | 2026-10-13 | Time-of-check time-of-use (toctou) race condition in Reliable Multicast Transport Driver (RMCAST) allows an authorized a |
| CVE-2026-85945 | 7.8 | 2026-10-13 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-87691 | 7.8 | 2026-10-13 | Use after free in Windows Management Services allows an authorized attacker to elevate privileges locally. |
| CVE-2026-87692 | 7.8 | 2026-10-13 | Deserialization of untrusted data in Microsoft Exchange Server allows an authorized attacker to elevate privileges local |
| CVE-2026-87693 | 7.0 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-87694 | 7.8 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-87695 | 7.8 | 2026-10-13 | Inclusion of functionality from untrusted control sphere in Microsoft Exchange Server allows an authorized attacker to e |
| CVE-2026-87696 | 7.5 | 2026-10-13 | Improper verification of cryptographic signature in Microsoft Exchange Server allows an authorized attacker to elevate p |
| CVE-2026-87697 | 8.8 | 2026-10-13 | Deserialization of untrusted data in .NET allows an unauthorized attacker to execute code over a network. |
| CVE-2026-87699 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Winlogon allows an authorized attacker to elevate privileges locally. |
| CVE-2026-87700 | 7.8 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-87702 | 7.8 | 2026-10-13 | Integer overflow or wraparound in Windows Resource Management (MRM) allows an authorized attacker to elevate privileges  |
| CVE-2026-87704 | 7.0 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-87705 | 7.4 | 2026-10-13 | Improper verification of source of a communication channel in Windows Hyper-V allows an unauthorized attacker to bypass  |
| CVE-2026-87706 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Storage Spaces Controller allows an authorized attacker to elevate privileges loca |
| CVE-2026-87707 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Fax and Scan Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-87708 | 7.0 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-87710 | 7.0 | 2026-10-13 | Improper access control in Microsoft Local Security Authority Server (lsasrv) allows an authorized attacker to elevate p |
| CVE-2026-87711 | 7.8 | 2026-10-13 | Stack-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-87712 | 7.8 | 2026-10-13 | Use after free in Windows Quality of Service (QoS) Packet Scheduler allows an authorized attacker to elevate privileges  |
| CVE-2026-87713 | 7.5 | 2026-10-13 | Use after free in Windows Bluetooth Port Driver allows an unauthorized attacker to elevate privileges over an adjacent n |
| CVE-2026-87715 | 7.0 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-87716 | 7.5 | 2026-10-13 | Heap-based buffer overflow in Windows Storage Spaces Controller allows an unauthorized attacker to deny service over a n |
| CVE-2026-88070 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows BitLocker allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88071 | 7.8 | 2026-10-13 | Double free in Windows Hyper-V allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88072 | 7.8 | 2026-10-13 | Improper access control in Windows Host Guardian Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88073 | 8.8 | 2026-10-13 | Use after free in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88074 | 7.8 | 2026-10-13 | Integer overflow or wraparound in Windows Virtualization-Based Security (VBS) Enclave allows an authorized attacker to e |
| CVE-2026-88075 | 8.8 | 2026-10-13 | Improper neutralization of special elements used in an sql command ('sql injection') in Microsoft Configuration Manager  |
| CVE-2026-88076 | 7.0 | 2026-10-13 | Null pointer dereference in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88079 | 7.0 | 2026-10-13 | Null pointer dereference in Windows MIDI Service Module allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88080 | 7.8 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88091 | 7.8 | 2026-10-13 | Deserialization of untrusted data in Windows Management Instrumentation allows an authorized attacker to elevate privile |
| CVE-2026-88092 | 9.4 | 2026-10-13 | Inconsistent interpretation of http requests ('http request/response smuggling') in ASP.NET Core allows an unauthorized  |
| CVE-2026-88093 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Desktop Window Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88094 | 8.1 | 2026-10-13 | Improper neutralization of special elements in output used by a downstream component ('injection') in Azure Storage Libr |
| CVE-2026-88096 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows DCOM Server allow |
| CVE-2026-88098 | 7.0 | 2026-10-13 | Untrusted pointer dereference in Windows Security Support Provider Interface allows an authorized attacker to elevate pr |
| CVE-2026-88100 | 7.8 | 2026-10-13 | Use after free in Windows Storage Spaces Controller allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88101 | 7.8 | 2026-10-13 | Weak authentication in Microsoft Input Method Editor (IME) allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88102 | 9.8 | 2026-10-13 | Use after free in Windows Failover Cluster allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88103 | 7.0 | 2026-10-13 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88105 | 7.8 | 2026-10-13 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88106 | 7.0 | 2026-10-13 | Use after free in Windows Cloud Files Mini Filter Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88107 | 7.0 | 2026-10-13 | Use after free in Windows Cloud Files Mini Filter Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88109 | 7.8 | 2026-10-13 | Use after free in Microsoft Office Click-To-Run allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88110 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88112 | 8.8 | 2026-10-13 | Untrusted pointer dereference in DNS Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88113 | 7.0 | 2026-10-13 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88114 | 8.8 | 2026-10-13 | Untrusted pointer dereference in DNS Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88115 | 8.8 | 2026-10-13 | Out-of-bounds read in Windows Server for NFS allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88116 | 8.8 | 2026-10-13 | Untrusted pointer dereference in DNS Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88117 | 8.1 | 2026-10-13 | Use after free in Windows DHCP Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88118 | 7.8 | 2026-10-13 | Integer overflow or wraparound in Windows Background Intelligent Transfer Service (BITS) allows an authorized attacker t |
| CVE-2026-88119 | 8.1 | 2026-10-13 | Use after free in Windows DHCP Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88120 | 8.1 | 2026-10-13 | Use after free in Windows DHCP Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88121 | 8.0 | 2026-10-13 | Use after free in Windows Background Intelligent Transfer Service (BITS) allows an unauthorized attacker to execute code |
| CVE-2026-88124 | 7.0 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88126 | 7.8 | 2026-10-13 | Untrusted pointer dereference in WebDAV allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88127 | 7.0 | 2026-10-13 | Use after free in Windows SMB Server allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88128 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88133 | 7.8 | 2026-10-13 | Improper authorization in Windows Portable Device Enumerator Service allows an authorized attacker to elevate privileges |
| CVE-2026-88134 | 7.8 | 2026-10-13 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88135 | 7.8 | 2026-10-13 | Improper access control in WebDAV allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88136 | 8.8 | 2026-10-13 | Improper resolution of path equivalence in WebDAV allows an authorized attacker to execute code over a network. |
| CVE-2026-88139 | 7.0 | 2026-10-13 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88141 | 7.0 | 2026-10-13 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88142 | 8.8 | 2026-10-13 | Use after free in Windows Background Intelligent Transfer Service (BITS) allows an unauthorized attacker to execute code |
| CVE-2026-88144 | 8.8 | 2026-10-13 | Use after free in Microsoft Office PowerPoint allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88145 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88146 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Background Intell |
| CVE-2026-88147 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Secure Socket Tunneling Protocol (SSTP) allows an authorized attacker to elevate p |
| CVE-2026-88149 | 7.0 | 2026-10-13 | Double free in Windows Ancillary Function Driver for WinSock allows an authorized attacker to elevate privileges locally |
| CVE-2026-88150 | 8.8 | 2026-10-13 | Use of uninitialized resource in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88152 | 7.8 | 2026-10-13 | Use after free in Windows Background Intelligent Transfer Service (BITS) allows an authorized attacker to elevate privil |
| CVE-2026-88155 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office SharePoint allows an authorized attacker to execute code over a network. |
| CVE-2026-88156 | 9.8 | 2026-10-13 | Stack-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88157 | 8.8 | 2026-10-13 | Heap-based buffer overflow in OpenSSH for Windows allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88159 | 8.8 | 2026-10-13 | Use after free in Windows Background Intelligent Transfer Service (BITS) allows an unauthorized attacker to execute code |
| CVE-2026-88160 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Microsoft Windows Search  |
| CVE-2026-88161 | 7.0 | 2026-10-13 | Use after free in Windows Local Security Authority (LSA) allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88163 | 8.8 | 2026-10-13 | Integer overflow or wraparound in Microsoft Office SharePoint allows an authorized attacker to execute code over a netwo |
| CVE-2026-88165 | 8.8 | 2026-10-13 | Out-of-bounds write in Active Directory Domain Services allows an authorized attacker to execute code over a network. |
| CVE-2026-88166 | 8.8 | 2026-10-13 | Integer overflow or wraparound in Microsoft Office SharePoint allows an authorized attacker to execute code over a netwo |
| CVE-2026-88168 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Bind Filter Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88171 | 8.1 | 2026-10-13 | Double free in Windows DHCP Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88173 | 8.1 | 2026-10-13 | Use after free in Windows Background Intelligent Transfer Service (BITS) allows an unauthorized attacker to execute code |
| CVE-2026-88174 | 8.1 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Deployment Servic |
| CVE-2026-88177 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88178 | 9.8 | 2026-10-13 | Use after free in Microsoft Office PowerPoint allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88179 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88180 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88181 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88182 | 7.8 | 2026-10-13 | Use after free in Microsoft Windows Search Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88185 | 8.1 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88186 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88188 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88189 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88191 | 7.8 | 2026-10-13 | Improper link resolution before file access ('link following') in Microsoft Windows Search Component allows an authorize |
| CVE-2026-88193 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Scripting Engine allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88194 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88196 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88197 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88198 | 8.8 | 2026-10-13 | Missing authorization in Microsoft Office SharePoint allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-88200 | 8.8 | 2026-10-13 | Privilege context switching error in Microsoft Office SharePoint allows an authorized attacker to elevate privileges ove |
| CVE-2026-88202 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88204 | 7.3 | 2026-10-13 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allo |
| CVE-2026-88206 | 7.5 | 2026-10-13 | Server-side request forgery (ssrf) in Microsoft Office SharePoint allows an authorized attacker to elevate privileges ov |
| CVE-2026-88207 | 7.5 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office PowerPoint allows an unauthorized attacker to execute code over a network |
| CVE-2026-88210 | 7.8 | 2026-10-13 | Reliance on untrusted inputs in a security decision in Microsoft Office Word allows an unauthorized attacker to bypass a |
| CVE-2026-88219 | 8.8 | 2026-10-13 | Untrusted pointer dereference in RPC Runtime allows an unauthorized attacker to execute code over a network. |
| CVE-2026-91013 | 9.3 | 2026-10-13 | Adobe Commerce is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by an attacker to i |
| CVE-2026-92464 | 9.1 | 2026-10-13 | Adobe Commerce is affected by an Improper Input Validation vulnerability that could result in arbitrary code execution i |
| CVE-2026-92908 | 8.3 | 2026-10-13 | Adobe Commerce is affected by an Incorrect Authorization vulnerability that could result in a Security feature bypass. A |
| CVE-2026-92909 | 9.8 | 2026-10-13 | Adobe Commerce is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in  |
| CVE-2026-92910 | 7.2 | 2026-10-13 | Adobe Commerce is affected by an Incorrect Authorization vulnerability that could result in a Security feature bypass. A |
| CVE-2026-92911 | 8.7 | 2026-10-13 | Adobe Commerce is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by a low-privileged |
| CVE-2026-92922 | 8.1 | 2026-10-13 | Adobe Commerce is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by a high-privilege |
| CVE-2026-95631 | 8.7 | 2026-10-13 | Adobe Commerce is affected by an Improper Input Validation vulnerability that could result in arbitrary code execution i |
| CVE-2026-95943 | 7.0 | 2026-10-13 | Double free in Connected Devices Platform Service (Cdpsvc) allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96044 | 8.8 | 2026-10-13 | No cwe for this issue in Microsoft Office SharePoint allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-96071 | 7.5 | 2026-10-13 | Heap-based buffer overflow in Windows Media allows an unauthorized attacker to execute code over a network. |
| CVE-2026-96096 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Windows Media Player allows an unauthorized attacker to execute code over a network. |
| CVE-2026-96108 | 7.8 | 2026-10-13 | Use after free in Desktop Window Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96113 | 9.8 | 2026-10-13 | Heap-based buffer overflow in DNS Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-96118 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96186 | 7.8 | 2026-10-13 | Deserialization of untrusted data in Microsoft Windows Media Foundation allows an authorized attacker to elevate privile |
| CVE-2026-96188 | 7.3 | 2026-10-13 | External control of system or configuration setting in Microsoft PowerToys allows an authorized attacker to elevate priv |
| CVE-2026-96202 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows Raw Image Extension allows an unauthorized attacker to execute code over a network |
| CVE-2026-96209 | 7.0 | 2026-10-13 | Out-of-bounds read in Windows Network File System allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96215 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Autopilot allows  |
| CVE-2026-96216 | 7.0 | 2026-10-13 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96217 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96219 | 9.8 | 2026-10-13 | Out-of-bounds write in Windows Local Security Authority Subsystem Service (LSASS) allows an unauthorized attacker to exe |
| CVE-2026-96220 | 7.8 | 2026-10-13 | Improper control of generation of code ('code injection') in Windows Assigned Access allows an authorized attacker to el |
| CVE-2026-96222 | 7.4 | 2026-10-13 | Improper certificate validation in Active Directory Federation Services (AD FS) allows an unauthorized attacker to perfo |
| CVE-2026-96223 | 7.8 | 2026-10-13 | Use after free in Windows Hyper-V allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96224 | 8.8 | 2026-10-13 | Out-of-bounds write in .NET allows an unauthorized attacker to execute code over a network. |
| CVE-2026-96225 | 7.8 | 2026-10-13 | Improper link resolution before file access ('link following') in .NET allows an authorized attacker to elevate privileg |
| CVE-2026-96230 | 8.8 | 2026-10-13 | Improper neutralization of input during web page generation ('cross-site scripting') in ASP.NET Core allows an unauthori |
| CVE-2026-96231 | 7.8 | 2026-10-13 | Improper link resolution before file access ('link following') in .NET allows an authorized attacker to elevate privileg |
| CVE-2026-96232 | 7.5 | 2026-10-13 | Out-of-bounds read in .NET allows an unauthorized attacker to disclose information over a network. |
| CVE-2026-96233 | 7.5 | 2026-10-13 | Out-of-bounds write in ASP.NET Core allows an unauthorized attacker to deny service over a network. |
| CVE-2026-96235 | 8.8 | 2026-10-13 | Out-of-bounds write in .NET allows an unauthorized attacker to execute code over a network. |
| CVE-2026-96236 | 7.5 | 2026-10-13 | Allocation of resources without limits or throttling in ASP.NET Core allows an unauthorized attacker to deny service ove |
| CVE-2026-96237 | 7.5 | 2026-10-13 | Inclusion of functionality from untrusted control sphere in .NET allows an unauthorized attacker to execute code over a  |
| CVE-2026-96243 | 7.8 | 2026-10-13 | Improper link resolution before file access ('link following') in Windows WalletService allows an authorized attacker to |
| CVE-2026-96244 | 7.8 | 2026-10-13 | Use after free in Windows Internal System User Profile allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96245 | 7.5 | 2026-10-13 | Out-of-bounds read in Windows Routing and Remote Access Service (RRAS) allows an unauthorized attacker to disclose infor |
| CVE-2026-96246 | 7.5 | 2026-10-13 | Out-of-bounds read in Network Policy Server (NPS) allows an unauthorized attacker to disclose information over a network |
| CVE-2026-96248 | 7.5 | 2026-10-13 | Stack-based buffer overflow in Windows Host Guardian Service allows an unauthorized attacker to deny service over a netw |
| CVE-2026-96249 | 7.8 | 2026-10-13 | Use after free in Windows Win32 Kernel Subsystem allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96250 | 7.0 | 2026-10-13 | Use after free in Windows USB Print Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96251 | 8.8 | 2026-10-13 | Reliance on untrusted inputs in a security decision in Microsoft PowerShell allows an unauthorized attacker to execute c |
| CVE-2026-96252 | 9.1 | 2026-10-13 | Improper verification of cryptographic signature in Active Directory Federation Services (AD FS) allows an unauthorized  |
| CVE-2026-96253 | 7.0 | 2026-10-13 | Use after free in Windows USB Print Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96254 | 7.0 | 2026-10-13 | Use after free in Windows USB Print Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96301 | 7.0 | 2026-10-13 | Use after free in Windows USB Print Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96302 | 7.0 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96304 | 7.0 | 2026-10-13 | Use after free in Windows USB Print Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96305 | 7.0 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96306 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows Sysmain Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96307 | 7.0 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96308 | 7.8 | 2026-10-13 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96309 | 7.8 | 2026-10-13 | Use after free in Windows Subsystem for Linux allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96310 | 7.0 | 2026-10-13 | Use after free in Windows USB Print Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96312 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96313 | 7.0 | 2026-10-13 | Missing authentication for critical function in Windows Push Notifications allows an authorized attacker to elevate priv |
| CVE-2026-96317 | 7.8 | 2026-10-13 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96318 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Resume allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96319 | 7.0 | 2026-10-13 | Use after free in Windows USB Print Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96320 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Windows DHCP Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-96322 | 7.0 | 2026-10-13 | Use after free in Windows Remote Desktop Protocol allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96323 | 7.0 | 2026-10-13 | Use after free in Windows Update allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96324 | 7.8 | 2026-10-13 | Use after free in Microsoft Windows Search Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96325 | 7.5 | 2026-10-13 | Missing reference to active allocated resource in Windows SMB Server allows an unauthorized attacker to deny service ove |
| CVE-2026-96843 | 7.8 | 2026-10-13 | Heap-based buffer overflow in WebDAV allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96844 | 8.0 | 2026-10-13 | Integer underflow (wrap or wraparound) in Microsoft Bluetooth Driver allows an authorized attacker to elevate privileges |
| CVE-2026-96847 | 7.8 | 2026-10-13 | Untrusted pointer dereference in WebDAV allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96852 | 7.0 | 2026-10-13 | Use after free in Windows TCP/IP allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96856 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Management Instrumentation allows an authorized attacker to elevate privileges loc |
| CVE-2026-96861 | 7.5 | 2026-10-13 | Out-of-bounds read in Network Device Enrollment Service (NDES) allows an unauthorized attacker to deny service over a ne |
| CVE-2026-96862 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows Spaceport.sys allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96864 | 9.8 | 2026-10-13 | Double free in Microsoft Failover Cluster Virtual Driver allows an unauthorized attacker to execute code over a network. |
| CVE-2026-96866 | 7.5 | 2026-10-13 | Out-of-bounds read in Network Device Enrollment Service (NDES) allows an unauthorized attacker to deny service over a ne |
| CVE-2026-96867 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows NTFS allows an authorized attacker to execute code locally. |
| CVE-2026-96868 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96909 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Windows BitLocker allows an unauthorized attacker to execute code over a network. |
| CVE-2026-96911 | 7.8 | 2026-10-13 | Improper link resolution before file access ('link following') in Microsoft Windows Search Component allows an authorize |
| CVE-2026-96912 | 7.8 | 2026-10-13 | Use after free in Windows Client License Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96913 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96914 | 8.8 | 2026-10-13 | Integer overflow or wraparound in Windows Virtualization-Based Security (VBS) Enclave allows an authorized attacker to e |
| CVE-2026-96915 | 7.8 | 2026-10-13 | Integer overflow or wraparound in Windows Kernel-Mode Drivers allows an authorized attacker to elevate privileges locall |
| CVE-2026-96916 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96917 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Windows PCI Bus Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96918 | 7.8 | 2026-10-13 | Improper access control in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96919 | 7.0 | 2026-10-13 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96920 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Program Compatibility Assistant Service allows an authorized attacker to elevate p |
| CVE-2026-96923 | 7.0 | 2026-10-13 | Use after free in Windows Workstation Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96924 | 9.8 | 2026-10-13 | Untrusted pointer dereference in Windows OLE allows an unauthorized attacker to execute code over a network. |
| CVE-2026-96928 | 7.8 | 2026-10-13 | Out-of-bounds read in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96929 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96931 | 7.8 | 2026-10-13 | Untrusted pointer dereference in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96932 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Embedded Mode Ser |
| CVE-2026-96933 | 7.8 | 2026-10-13 | Untrusted pointer dereference in Windows COM+ Event System Service allows an authorized attacker to elevate privileges l |
| CVE-2026-96934 | 9.8 | 2026-10-13 | Use after free in Windows DHCP Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-96937 | 7.0 | 2026-10-13 | Use after free in Microsoft Windows Search Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96939 | 7.0 | 2026-10-13 | Time-of-check time-of-use (toctou) race condition in Servicing Stack Updates allows an authorized attacker to elevate pr |
| CVE-2026-96943 | 8.8 | 2026-10-13 | Integer overflow or wraparound in Windows Raw Image Extension allows an unauthorized attacker to execute code over a net |
| CVE-2026-96945 | 7.5 | 2026-10-13 | Uncaught exception in Windows Failover Cluster allows an unauthorized attacker to deny service over a network. |
| CVE-2026-96946 | 7.8 | 2026-10-13 | Use after free in Windows Universal Disk Format File System Driver (UDFS) allows an authorized attacker to elevate privi |
| CVE-2026-96947 | 7.8 | 2026-10-13 | Use after free in Windows Universal Disk Format File System Driver (UDFS) allows an authorized attacker to elevate privi |
| CVE-2026-96949 | 7.0 | 2026-10-13 | Use after free in Windows Universal Disk Format File System Driver (UDFS) allows an authorized attacker to elevate privi |
| CVE-2026-96950 | 7.8 | 2026-10-13 | Use after free in Windows Universal Disk Format File System Driver (UDFS) allows an authorized attacker to elevate privi |
| CVE-2026-96951 | 8.8 | 2026-10-13 | Improper neutralization of special elements used in a command ('command injection') in Windows Shell allows an unauthori |
| CVE-2026-96952 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Windows Media Foundation allows an unauthorized attacker to execute code over a  |
| CVE-2026-96953 | 7.8 | 2026-10-13 | Null pointer dereference in Windows Universal Disk Format File System Driver (UDFS) allows an authorized attacker to exe |
| CVE-2026-96957 | 8.8 | 2026-10-13 | Improper verification of cryptographic signature in .NET allows an unauthorized attacker to bypass a security feature ov |
| CVE-2026-96958 | 7.5 | 2026-10-13 | Inefficient algorithmic complexity in .NET allows an unauthorized attacker to deny service over a network. |
| CVE-2026-96959 | 7.5 | 2026-10-13 | Allocation of resources without limits or throttling in .NET allows an unauthorized attacker to deny service over a netw |
| CVE-2026-96960 | 7.5 | 2026-10-13 | Asymmetric resource consumption (amplification) in .NET allows an unauthorized attacker to deny service over a network. |
| CVE-2026-96995 | 7.8 | 2026-10-13 | Stack-based buffer overflow in Microsoft Office Word allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96996 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-96997 | 7.8 | 2026-10-13 | Use after free in Microsoft Office OneNote allows an authorized attacker to elevate privileges locally. |
| CVE-2026-97001 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-97003 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97004 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97007 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97008 | 8.8 | 2026-10-13 | Buffer underwrite ('buffer underflow') in Microsoft Office Excel allows an unauthorized attacker to execute code over a  |
| CVE-2026-97009 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-97010 | 8.8 | 2026-10-13 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97011 | 8.8 | 2026-10-13 | Use of uninitialized resource in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97012 | 8.8 | 2026-10-13 | Stack-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97016 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97017 | 8.8 | 2026-10-13 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97738 | 8.8 | 2026-10-13 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97739 | 8.8 | 2026-10-13 | Integer underflow (wrap or wraparound) in Microsoft Office Excel allows an unauthorized attacker to execute code over a  |
| CVE-2026-97741 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97742 | 8.8 | 2026-10-13 | Stack-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97745 | 8.8 | 2026-10-13 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97746 | 8.8 | 2026-10-13 | Integer underflow (wrap or wraparound) in Microsoft Office Excel allows an unauthorized attacker to execute code over a  |
| CVE-2026-97747 | 8.8 | 2026-10-13 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97748 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97749 | 9.8 | 2026-10-13 | Double free in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97750 | 8.8 | 2026-10-13 | Stack-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97751 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97752 | 8.8 | 2026-10-13 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97753 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97754 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97755 | 8.8 | 2026-10-13 | Out-of-bounds read in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97756 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97757 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97758 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97759 | 8.8 | 2026-10-13 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97761 | 8.8 | 2026-10-13 | Stack-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97762 | 8.8 | 2026-10-13 | Out-of-bounds write in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97763 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97765 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97766 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97767 | 8.8 | 2026-10-13 | Double free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97768 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97769 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97770 | 8.8 | 2026-10-13 | Stack-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97771 | 8.8 | 2026-10-13 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97772 | 8.8 | 2026-10-13 | Double free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97773 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97774 | 7.0 | 2026-10-13 | Time-of-check time-of-use (toctou) race condition in Microsoft Office Click-To-Run allows an authorized attacker to elev |
| CVE-2026-97775 | 8.8 | 2026-10-13 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97776 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97777 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97778 | 8.8 | 2026-10-13 | Integer overflow or wraparound in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97780 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97781 | 8.8 | 2026-10-13 | Improper neutralization of special elements used in a command ('command injection') in Microsoft Office OneNote allows a |
| CVE-2026-97783 | 8.1 | 2026-10-13 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allo |
| CVE-2026-97787 | 7.0 | 2026-10-13 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Container Isolati |
| CVE-2026-97788 | 7.5 | 2026-10-13 | Observable discrepancy in Active Directory Federation Services (AD FS) allows an unauthorized attacker to disclose infor |
| CVE-2026-97789 | 7.5 | 2026-10-13 | Use after free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97792 | 7.8 | 2026-10-13 | Improper access control in Windows Container Isolation FS Filter Driver (unionfs.sys) allows an authorized attacker to e |
| CVE-2026-97793 | 7.0 | 2026-10-13 | Missing authentication for critical function in Windows Setup and Deployment allows an authorized attacker to elevate pr |
| CVE-2026-97794 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Container Isolation FS Filter Driver (unionfs.sys) allows an authorized attacker t |
| CVE-2026-97798 | 7.8 | 2026-10-13 | Improper neutralization of argument delimiters in a command ('argument injection') in Windows Error Reporting allows an  |
| CVE-2026-97799 | 7.8 | 2026-10-13 | Improper verification of cryptographic signature in Windows Audio Service allows an authorized attacker to elevate privi |
| CVE-2026-97800 | 7.8 | 2026-10-13 | Incorrect permission assignment for critical resource in Windows Mobile Broadband allows an authorized attacker to eleva |
| CVE-2026-97801 | 7.5 | 2026-10-13 | Improper validation of specified type of input in .NET Framework allows an unauthorized attacker to perform tampering ov |
| CVE-2026-97803 | 7.8 | 2026-10-13 | Heap-based buffer overflow in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-97804 | 7.8 | 2026-10-13 | Heap-based buffer overflow in HID class driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-97805 | 9.8 | 2026-10-13 | Out-of-bounds read in Windows Partition Management Driver allows an unauthorized attacker to execute code over a network |
| CVE-2026-97806 | 7.8 | 2026-10-13 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-97807 | 7.8 | 2026-10-13 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-97808 | 7.0 | 2026-10-13 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-97809 | 7.8 | 2026-10-13 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-97810 | 7.0 | 2026-10-13 | Heap-based buffer overflow in Windows Container Isolation FS Filter Driver (unionfs.sys) allows an authorized attacker t |
| CVE-2026-97811 | 7.8 | 2026-10-13 | Double free in OpenSSH for Windows allows an authorized attacker to elevate privileges locally. |
| CVE-2026-97812 | 7.0 | 2026-10-13 | Double free in Windows Update Orchestrator Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-97814 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Windows Text Shaping allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97815 | 9.8 | 2026-10-13 | Heap-based buffer overflow in Windows Error Reporting allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97816 | 9.8 | 2026-10-13 | Use after free in OpenSSH for Windows allows an unauthorized attacker to execute code over a network. |
| CVE-2026-97830 | 7.5 | 2026-10-13 | Double free in Windows Internet Information Services allows an unauthorized attacker to deny service over a network. |
| CVE-2026-102234 | 7.4 | 2026-10-13 | Reliance on untrusted inputs in a security decision in Visual Studio Code allows an unauthorized attacker to bypass a se |
| CVE-2026-102235 | 8.8 | 2026-10-13 | Improper encoding or escaping of output in Visual Studio Code allows an unauthorized attacker to execute code over a net |
| CVE-2026-102238 | 9.6 | 2026-10-13 | Improper limitation of a pathname to a restricted directory ('path traversal') in Visual Studio Code allows an unauthori |
| CVE-2026-102855 | 8.8 | 2026-10-13 | Heap-based buffer overflow in Microsoft Office Visio allows an unauthorized attacker to execute code over a network. |
| CVE-2026-103830 | 7.8 | 2026-10-13 | Substance3D - Stager is affected by a Stack-based Buffer Overflow vulnerability that could result in arbitrary code exec |
| CVE-2026-103832 | 7.8 | 2026-10-13 | Substance3D - Stager is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution i |
| CVE-2026-103833 | 7.8 | 2026-10-13 | Substance3D - Stager is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution i |
| CVE-2026-103834 | 7.8 | 2026-10-13 | Substance3D - Stager is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution i |
| CVE-2026-103835 | 7.8 | 2026-10-13 | Substance3D - Stager is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution i |
| CVE-2026-103836 | 7.8 | 2026-10-13 | Substance3D - Stager is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution i |
| CVE-2026-103837 | 7.8 | 2026-10-13 | Substance3D - Stager is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution i |
| CVE-2026-103838 | 7.8 | 2026-10-13 | Substance3D - Stager is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution i |
| CVE-2026-103839 | 7.8 | 2026-10-13 | Substance3D - Stager is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution i |
| CVE-2026-103840 | 7.8 | 2026-10-13 | Substance3D - Stager is affected by an out-of-bounds read vulnerability when parsing a crafted file, which could result  |
| CVE-2026-103841 | 7.8 | 2026-10-13 | Substance3D - Stager is affected by an out-of-bounds read vulnerability when parsing a crafted file, which could result  |
| CVE-2026-103842 | 7.8 | 2026-10-13 | Substance3D - Stager is affected by an out-of-bounds read vulnerability when parsing a crafted file, which could result  |
| CVE-2026-103843 | 7.8 | 2026-10-13 | Substance3D - Stager is affected by a Use After Free vulnerability that could result in arbitrary code execution in the  |
| CVE-2026-103844 | 7.8 | 2026-10-13 | Dimension is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the conte |
| CVE-2026-103845 | 8.6 | 2026-10-13 | Dimension is affected by an Uncontrolled Search Path Element vulnerability that could result in arbitrary code execution |
| CVE-2026-103846 | 8.6 | 2026-10-13 | Dimension is affected by an Improper Neutralization of Input During Web Page Generation vulnerability that could result  |
| CVE-2026-103847 | 8.6 | 2026-10-13 | Dimension is affected by an Untrusted Search Path vulnerability that could result in arbitrary code execution in the con |
| CVE-2026-103848 | 9.9 | 2026-10-13 | Adobe Experience Manager is affected by an Improper Neutralization of Special Elements used in an OS Command ('OS Comman |
| CVE-2026-103851 | 7.8 | 2026-10-13 | Substance3D - Stager is affected by a Stack-based Buffer Overflow vulnerability that could result in arbitrary code exec |
| CVE-2026-103854 | 7.8 | 2026-10-13 | Dimension is affected by a Stack-based Buffer Overflow vulnerability that could result in arbitrary code execution in th |
| CVE-2026-104252 | 9.8 | 2026-10-13 | Vitess is a database clustering system for horizontal scaling of MySQL. Prior to 23.0.5 and 24.0.2, twopczHandler in go/ |
| CVE-2026-105895 | 9.9 | 2026-10-13 | Adobe Experience Manager is affected by an Improper Input Validation vulnerability that could result in arbitrary code e |
| CVE-2026-106626 | 9.1 | 2026-10-13 | Adobe Experience Manager is affected by an Improper Input Validation vulnerability that could result in arbitrary code e |
| CVE-2026-106629 | 9.3 | 2026-10-13 | Adobe Experience Manager is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by an att |
| CVE-2026-106630 | 9.3 | 2026-10-13 | Adobe Experience Manager is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by an att |
| CVE-2026-106634 | 7.7 | 2026-10-13 | Adobe Experience Manager is affected by an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal' |
| CVE-2026-110083 | 7.1 | 2026-10-13 | Adobe Experience Manager is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Inje |
| CVE-2026-110084 | 7.1 | 2026-10-13 | Adobe Experience Manager is affected by an XML Injection (aka Blind XPath Injection) vulnerability that could result in  |
| CVE-2026-48382 | 10.0 | 2026-10-13 | Adobe Experience Manager is affected by an Incorrect Authorization vulnerability that could result in arbitrary code exe |
| CVE-2026-48383 | 10.0 | 2026-10-13 | Adobe Experience Manager is affected by an Incorrect Authorization vulnerability that could result in arbitrary code exe |
| CVE-2026-55601 | 7.3 | 2026-10-13 | MultiTail is a utility for monitoring multiple log files in one terminal. In version 7.1.5 and earlier, the -ex and -eX  |
| CVE-2026-63146 | 9.8 | 2026-10-13 | Omnispace Agora Project before 26.10.0 contains a code injection vulnerability where unescaped, attacker-controlled valu |
| CVE-2026-63149 | 7.4 | 2026-10-13 | Omnispace Agora Project before 26.10.0 contains an insecure randomness vulnerability that allows attackers to predict te |
| CVE-2026-63152 | 8.1 | 2026-10-13 | Omnispace Agora Project before 26.10.0 contains a second-order SQL injection vulnerability that allows authenticated att |
| CVE-2026-63153 | 8.1 | 2026-10-13 | Omnispace Agora Project before 26.10.0 contains a broken access control vulnerability in setAffectations() that allows a |
| CVE-2026-63154 | 8.8 | 2026-10-13 | Omnispace Agora Project before 26.10.0 contains a SQL identifier injection vulnerability that allows a space administrat |
| CVE-2026-63158 | 7.4 | 2026-10-13 | Omnispace Agora Project before 26.10.0 contains an authentication bypass vulnerability that allows attackers possessing  |
| CVE-2026-63159 | 7.4 | 2026-10-13 | Omnispace Agora Project before 26.10.0 contains a predictable password-reset token vulnerability that allows unauthentic |
| CVE-2026-63160 | 7.4 | 2026-10-13 | Omnispace Agora Project before 26.10.0 contains a vulnerability where the persistent remember-me token is stored verbati |
| CVE-2026-63161 | 8.8 | 2026-10-13 | Omnispace Agora Project before 26.10.0 contains a session fixation vulnerability that allows remote attackers to hijack  |
| CVE-2026-63162 | 8.8 | 2026-10-13 | Omnispace Agora Project before 26.10.0 contains a path traversal vulnerability that allows attackers to write arbitrary  |
| CVE-2026-63163 | 7.5 | 2026-10-13 | Omnispace Agora Project before 26.10.0 contains a broken access control vulnerability in the MobileFileDownload route th |
| CVE-2026-63165 | 8.1 | 2026-10-13 | Omnispace Agora Project before 26.10.0 contains a SQL injection vulnerability in the calendar functionality that allows  |
| CVE-2026-63172 | 7.1 | 2026-10-13 | Omnispace Agora Project before 26.10.0 contains a broken access control vulnerability that allows a regular, non-adminis |
| CVE-2026-63174 | 8.1 | 2026-10-13 | Omnispace Agora Project before 26.10.0 contains a broken access control vulnerability that allows a space administrator  |
| CVE-2026-70098 | 8.8 | 2026-10-13 | Missing authorization in Visual Studio Code allows an unauthorized attacker to execute code over a network. |
| CVE-2026-75732 | 9.9 | 2026-10-13 | Adobe Experience Manager is affected by an Incorrect Authorization vulnerability that could result in arbitrary code exe |
| CVE-2026-83662 | 9.3 | 2026-10-13 | Adobe Experience Manager is affected by a reflected Cross-Site Scripting (XSS) vulnerability. An attacker could exploit  |
| CVE-2026-86016 | 8.2 | 2026-10-13 | VNote is a note-taking platform. Prior to 4.3.0, VNote uses the assignment `preNode.innerHTML = p_metaData` in src/data/ |
| CVE-2026-86022 | 7.0 | 2026-10-13 | VNote is a note-taking platform. Prior to 4.3.0, SessionConfig::ExternalProgram::fetchCommand wraps a note path in doubl |
| CVE-2026-90531 | 9.6 | 2026-10-13 | Adobe Experience Manager is affected by an Improper Restriction of XML External Entity Reference ('XXE') vulnerability t |
| CVE-2026-90532 | 10.0 | 2026-10-13 | Adobe Experience Manager is affected by an Incorrect Authorization vulnerability that could result in arbitrary code exe |
| CVE-2026-100111 | 7.8 | 2026-10-13 | Photoshop Desktop is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-100112 | 7.8 | 2026-10-13 | Photoshop Desktop is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-100127 | 7.8 | 2026-10-13 | Bridge is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the context  |
| CVE-2026-100128 | 7.8 | 2026-10-13 | Bridge is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the context  |
| CVE-2026-100129 | 7.8 | 2026-10-13 | Bridge is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the context  |
| CVE-2026-101294 | 8.7 | 2026-10-13 | IBM WebSphere Application Server - Liberty 17.0.0.3 through 26.0.0.10 and IBM WebSphere Application Server 8.5, and 9.0  |
| CVE-2026-103821 | 7.8 | 2026-10-13 | Substance3D - Designer is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution |
| CVE-2026-104346 | 7.8 | 2026-10-13 | Photoshop Desktop is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-104347 | 7.8 | 2026-10-13 | Photoshop Desktop is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-104348 | 7.8 | 2026-10-13 | Photoshop Desktop is affected by a Heap-based Buffer Overflow vulnerability that could result in arbitrary code executio |
| CVE-2026-105442 | 7.5 | 2026-10-13 | IBM WebSphere Application Server 8.5, and 9.0 and IBM WebSphere Application Server - Liberty 17.0.0.3 through 26.0.0.10  |
| CVE-2026-105443 | 8.2 | 2026-10-13 | IBM WebSphere Application Server - Liberty 17.0.0.3 through 26.0.0.10 has insufficient isolation between servers sharing |
| CVE-2026-105897 | 8.6 | 2026-10-13 | ColdFusion is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in privilege escalation.  |
| CVE-2026-105898 | 8.2 | 2026-10-13 | ColdFusion is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the  |
| CVE-2026-105899 | 10.0 | 2026-10-13 | ColdFusion is affected by an Unrestricted Upload of File with Dangerous Type vulnerability that could result in arbitrar |
| CVE-2026-105900 | 7.5 | 2026-10-13 | ColdFusion is affected by an Improper Input Validation vulnerability that could result in an application denial-of-servi |
| CVE-2026-105901 | 8.8 | 2026-10-13 | ColdFusion is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the  |
| CVE-2026-105903 | 9.9 | 2026-10-13 | ColdFusion is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could result i |
| CVE-2026-105994 | 7.7 | 2026-10-13 | ColdFusion is affected by an Incorrect Authorization vulnerability that could result in a Security feature bypass. A low |
| CVE-2026-106089 | 8.8 | 2026-10-13 | ColdFusion is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the  |
| CVE-2026-106090 | 8.8 | 2026-10-13 | ColdFusion is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the  |
| CVE-2026-106612 | 9.9 | 2026-10-13 | ColdFusion is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the  |
| CVE-2026-106613 | 8.8 | 2026-10-13 | ColdFusion is affected by an Improper Input Validation vulnerability that could result in arbitrary code execution in th |
| CVE-2026-106614 | 7.8 | 2026-10-13 | ColdFusion is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the  |
| CVE-2026-106615 | 8.8 | 2026-10-13 | ColdFusion is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the  |
| CVE-2026-106616 | 8.6 | 2026-10-13 | ColdFusion is affected by an Improper Restriction of XML External Entity Reference ('XXE') vulnerability that could lead |
| CVE-2026-106617 | 8.8 | 2026-10-13 | ColdFusion is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the  |
| CVE-2026-106618 | 8.8 | 2026-10-13 | ColdFusion is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the  |
| CVE-2026-106619 | 9.0 | 2026-10-13 | ColdFusion is affected by an Improper Input Validation vulnerability that could result in arbitrary code execution in th |
| CVE-2026-106620 | 9.6 | 2026-10-13 | ColdFusion is affected by an Incorrect Authorization vulnerability that could result in a Security feature bypass. A low |
| CVE-2026-106621 | 9.1 | 2026-10-13 | ColdFusion is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could result i |
| CVE-2026-106622 | 10.0 | 2026-10-13 | ColdFusion is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in privilege escalation.  |
| CVE-2026-106623 | 7.5 | 2026-10-13 | ColdFusion is affected by an Incorrect Authorization vulnerability that could lead to disclosure of sensitive memory. An |
| CVE-2026-106624 | 10.0 | 2026-10-13 | ColdFusion is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could result i |
| CVE-2026-34633 | 7.7 | 2026-10-13 | ColdFusion is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in privilege escalation.  |
| CVE-2026-34634 | 8.6 | 2026-10-13 | ColdFusion is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in privilege escalation.  |
| CVE-2026-49950 | 9.8 | 2026-10-13 | Xorbits Xoscar through 0.11.2 contains an unauthenticated deserialization vulnerability that allows remote attackers to  |
| CVE-2026-62840 | 7.0 | 2026-10-13 | Time-of-check time-of-use (toctou) race condition in Linux Kernel allows an authorized attacker to elevate privileges lo |
| CVE-2026-65674 | 8.8 | 2026-10-13 | Deserialization of untrusted data in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-67625 | 8.5 | 2026-10-13 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-68883 | 8.5 | 2026-10-13 | Heap-based buffer overflow in SQL Server allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-71385 | 8.4 | 2026-10-13 | ColdFusion is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the  |
| CVE-2026-75748 | 7.6 | 2026-10-13 | ColdFusion is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in privilege escalation.  |
| CVE-2026-75994 | 9.6 | 2026-10-13 | ColdFusion is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the  |
| CVE-2026-75995 | 8.4 | 2026-10-13 | ColdFusion is affected by an Improper Input Validation vulnerability that could result in arbitrary code execution in th |
| CVE-2026-75996 | 7.5 | 2026-10-13 | ColdFusion is affected by an Uncontrolled Resource Consumption vulnerability that could lead to application denial-of-se |
| CVE-2026-76001 | 7.1 | 2026-10-13 | ColdFusion is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in privilege escalation.  |
| CVE-2026-83661 | 7.8 | 2026-10-13 | Photoshop Desktop is affected by an Integer Overflow or Wraparound vulnerability that could result in arbitrary code exe |
| CVE-2026-83965 | 7.8 | 2026-10-13 | Substance3D - Sampler is affected by a Stack-based Buffer Overflow vulnerability that could result in arbitrary code exe |
| CVE-2026-83966 | 7.8 | 2026-10-13 | Substance3D - Sampler is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution  |
| CVE-2026-85876 | 7.0 | 2026-10-13 | Use after free in SQL Server allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85886 | 8.5 | 2026-10-13 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-85888 | 7.7 | 2026-10-13 | Out-of-bounds read in SQL Server allows an authorized attacker to disclose information over a network. |
| CVE-2026-85919 | 7.0 | 2026-10-13 | Heap-based buffer overflow in SQL Server allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88081 | 7.7 | 2026-10-13 | Out-of-bounds read in SQL Server allows an authorized attacker to disclose information over a network. |
| CVE-2026-88082 | 7.0 | 2026-10-13 | Heap-based buffer overflow in SQL Server allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88083 | 7.5 | 2026-10-13 | Stack-based buffer overflow in SQL Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88088 | 7.0 | 2026-10-13 | Integer overflow or wraparound in SQL Server allows an authorized attacker to elevate privileges locally. |
| CVE-2026-90530 | 9.3 | 2026-10-13 | ColdFusion RDS is affected by an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerab |
| CVE-2026-93895 | 9.1 | 2026-10-13 | IBM WebSphere Application Server - Liberty 20.0.0.12 through 26.0.0.10 could allow an unauthenticated remote attacker to |
| CVE-2026-93905 | 8.2 | 2026-10-13 | IBM WebSphere Application Server - Liberty 17.0.0.3 through 26.0.0.10 could allow an unauthenticated remote attacker to  |
| CVE-2026-93909 | 9.1 | 2026-10-13 | IBM WebSphere Application Server - Liberty 17.0.0.3 through 26.0.0.10 is vulnerable by an authentication bypass vulnerab |
| CVE-2026-94512 | 8.8 | 2026-10-13 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-95635 | 7.8 | 2026-10-13 | Photoshop Desktop is affected by a Double Free vulnerability that could result in arbitrary code execution in the contex |
| CVE-2026-95636 | 7.8 | 2026-10-13 | Photoshop Desktop is affected by an Integer Overflow or Wraparound vulnerability that could result in arbitrary code exe |
| CVE-2026-95637 | 7.8 | 2026-10-13 | Photoshop Desktop is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-95638 | 7.8 | 2026-10-13 | Photoshop Desktop is affected by a Heap-based Buffer Overflow vulnerability that could result in arbitrary code executio |
| CVE-2026-95639 | 8.6 | 2026-10-13 | Photoshop Desktop is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution  |
| CVE-2026-95641 | 7.8 | 2026-10-13 | Photoshop Desktop is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-95695 | 7.4 | 2026-10-13 | IBM WebSphere Application Server - Liberty 20.0.0.12 through 26.0.0.10 could allow a remote attacker to bypass security  |
| CVE-2026-96521 | 7.8 | 2026-10-13 | Photoshop Desktop is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-96522 | 7.8 | 2026-10-13 | Photoshop Desktop is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-96523 | 7.8 | 2026-10-13 | Photoshop Desktop is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-96956 | 8.0 | 2026-10-13 | Stack-based buffer overflow in SQL Server allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-97312 | 7.8 | 2026-10-13 | Photoshop Desktop is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-100113 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Improper Input Validation vulnerability that could result in a Security featur |
| CVE-2026-100114 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Improper Access Control vulnerability that could result in a Security feature  |
| CVE-2026-100115 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Improper Access Control vulnerability that could result in a Security feature  |
| CVE-2026-100117 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Improper Input Validation vulnerability that could result in a Security featur |
| CVE-2026-100118 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Improper Certificate Validation vulnerability that could result in a Security  |
| CVE-2026-100119 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Improper Input Validation vulnerability that could result in a Security featur |
| CVE-2026-100120 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Improper Input Validation vulnerability that could result in a Security featur |
| CVE-2026-100121 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Improper Certificate Validation vulnerability that could result in a Security  |
| CVE-2026-100122 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Improper Certificate Validation vulnerability that could result in a Security  |
| CVE-2026-100123 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Improper Certificate Validation vulnerability that could result in a Security  |
| CVE-2026-100124 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Improper Input Validation vulnerability that could result in a Security featur |
| CVE-2026-100135 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Improper Input Validation vulnerability that could result in a Security featur |
| CVE-2026-100136 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Integer Overflow or Wraparound vulnerability that could result in an applicati |
| CVE-2026-100137 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Uncontrolled Resource Consumption vulnerability that could lead to application |
| CVE-2026-100138 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Uncontrolled Resource Consumption vulnerability that could lead to application |
| CVE-2026-100139 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Uncontrolled Resource Consumption vulnerability that could lead to application |
| CVE-2026-103296 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Improper Verification of Cryptographic Signature vulnerability that could resu |
| CVE-2026-103297 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Improper Verification of Cryptographic Signature vulnerability that could resu |
| CVE-2026-104345 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Improper Input Validation vulnerability that could result in a Security featur |
| CVE-2026-105902 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Uncontrolled Resource Consumption vulnerability that could lead to application |
| CVE-2026-106627 | 7.5 | 2026-10-13 | CAI Content Credentials is affected by an Uncontrolled Resource Consumption vulnerability that could lead to application |
| CVE-2026-77206 | 7.5 | 2026-10-13 | Libreswan's IKEv2 state machine has a null pointer dereference bug in the EAP handling code for authentication. As a res |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-104935 | Ivanti / Connect Secure | 2026-10-13 | 2026-10-16 | Unknown |
| CVE-2026-96951 | Microsoft / Windows | 2026-10-13 | 2026-10-16 | Unknown |
| CVE-2015-5477 | ISC / BIND | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2016-3081 | Apache / Struts | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2023-22894 | Strapi / Strapi | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2021-3199 | ONLYOFFICE / Docs | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2015-3306 | ProFTPD / ProFTPD | 2026-10-08 | 2026-10-11 | Unknown |

---

*Total entries in CISA KEV catalog: 1741*