# Vulnerability Intelligence Report

**Date:** 2026-08-12  
**Generated:** 2026-08-12T09:09:45Z  

## Pipeline Warnings

- summarizer failed: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}, 'request_id': 'req_011CdxbQtmxnS1rdGiNxGrbH'}

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
| CVE-2026-10579 | 9.8 | 2026-08-11 | A flaw was found in Picketlink Federation SAML; the unsolcited response handler would accept forged assertions with no v |
| CVE-2026-15554 | 7.4 | 2026-08-11 | the Undertow AJP listener honours forged ssl_cert and is_ssl AJP attributes without requiring any shared-secret authenti |
| CVE-2026-15555 | 8.8 | 2026-08-11 | A flaw was found in JBoss marshalling. The Infinispan session replication path deserializes replicated session data via  |
| CVE-2026-15556 | 8.1 | 2026-08-11 | A flaw was found in Picketlink's SP signature validation; a SAML response containing zero assertion elements matching th |
| CVE-2026-15560 | 8.1 | 2026-08-11 | when EAP runs with -secmgr, the openjdk-orb's JDKBridge honours attacker-supplied CDR codebase URLs during object unmars |
| CVE-2026-15561 | 7.5 | 2026-08-11 | A flaw was found in EAP's undertow http/1.1 chunked-transfer decoder. missing limits on size and count would allow an at |
| CVE-2026-15562 | 7.5 | 2026-08-11 | A flaw was found in EAP's jboss-remoting. A remote unauthenticated attacker who can reach :8080 (or :9990, or :4447) and |
| CVE-2026-15563 | 7.4 | 2026-08-11 | A flaw was found in EAP's IIOP. The listener's NameService would accept bind operations without authentication, allowing |
| CVE-2026-15565 | 7.5 | 2026-08-11 | A flaw was found in Undertow. A remote attacker can cause Out of Memory on websockets endpoint without authentication on |
| CVE-2026-15567 | 7.5 | 2026-08-11 | A flaw was found in Wildfly. A remote unauthenticated attacker can trigger OutOfMemoryError as CSIv2Util's GSS token dec |
| CVE-2026-71217 | 7.5 | 2026-08-11 | A flaw was found in iperf3. A remote attacker can exploit this vulnerability by sending crafted control-channel JSON wit |
| CVE-2026-72693 | 7.8 | 2026-08-11 | `openvt -u` is intended to identify the owner of the current VT and then execute `login` as that user from a privileged  |
| CVE-2026-72694 | 7.1 | 2026-08-11 | A flaw was found in MRTG. When the MRTG daemon is started as a root user and subsequently drops privileges, a local, low |
| CVE-2026-58231 | 10.0 | 2026-08-11 | SAP Commerce Cloud allows an unauthenticated
attacker to abuse a default authentication client and submit specially craf |
| CVE-2026-50236 | 7.4 | 2026-08-11 | An authenticated SSRF flaw was found in the OpenShift Console Dev Console webhook helpers. User-supplied target URLs are |
| CVE-2026-50237 | 7.4 | 2026-08-11 | A Server-Side Request Forgery and supply chain flaw was found in the OpenShift Console Helm catalog proxy. A namespace t |
| CVE-2026-72533 | 8.8 | 2026-08-11 | An authentication bypass vulnerability in Portainer CE through 2.44.0 allows authenticated low-privileged users to bypas |
| CVE-2026-72534 | 8.8 | 2026-08-11 | A privilege escalation vulnerability in Authentik Security authentik through 2026.5.6 allows an attacker with a source-s |
| CVE-2026-72535 | 8.6 | 2026-08-11 | A missing authentication vulnerability in Chaskiq through commit 46dfdd1 allows unauthenticated remote attackers to mint |
| CVE-2026-72536 | 8.6 | 2026-08-11 | A missing authentication vulnerability in Chaskiq through commit 46dfdd1 allows unauthenticated remote attackers to mani |
| CVE-2026-72537 | 8.8 | 2026-08-11 | A privilege escalation vulnerability in Authentik Security authentik through 2026.5.6 allows an attacker with a source-s |
| CVE-2026-72538 | 8.8 | 2026-08-11 | An argument injection vulnerability in PrefectHQ Prefect through 3.8.2 allows authenticated users to achieve remote code |
| CVE-2026-72543 | 7.5 | 2026-08-11 | An insecure direct object reference vulnerability in OpenSignLabs OpenSign through 2.37.0 allows unauthenticated remote  |
| CVE-2026-72544 | 7.5 | 2026-08-11 | An integrity verification vulnerability in OpenSignLabs OpenSign through 2.37.0 allows unauthenticated remote attackers  |
| CVE-2026-72545 | 7.5 | 2026-08-11 | An insecure direct object reference vulnerability in OpenSignLabs OpenSign through 2.37.0 allows unauthenticated remote  |
| CVE-2026-72546 | 7.1 | 2026-08-11 | An insecure direct object reference vulnerability in Attendize through commit 9289acb allows any authenticated event org |
| CVE-2026-72547 | 7.1 | 2026-08-11 | An insecure direct object reference vulnerability in Attendize through commit 9289acb allows any authenticated event org |
| CVE-2026-72548 | 7.5 | 2026-08-11 | An information disclosure vulnerability in OpenSignLabs OpenSign through 2.37.0 allows unauthenticated remote attackers  |
| CVE-2026-72550 | 9.8 | 2026-08-11 | An SQL injection vulnerability in Friendica through the 2026.08-dev branch allows unauthenticated remote attackers to ex |
| CVE-2026-72551 | 8.8 | 2026-08-11 | A remote code execution vulnerability in Apioo Fusio 8.8.3 allows authenticated users with the Developer role to execute |
| CVE-2026-72552 | 7.5 | 2026-08-11 | A server-side request forgery vulnerability in Dub as of 2026-07-10 allows unauthenticated remote attackers to make the  |
| CVE-2026-72555 | 8.1 | 2026-08-11 | A broken access control vulnerability in Peppermint Lab Peppermint through commit ba6e217 exists because the Config.role |
| CVE-2026-72556 | 8.8 | 2026-08-11 | A remote code execution vulnerability in ZoneMinder 1.39.17 allows any authenticated user to execute OS commands by expl |
| CVE-2026-72557 | 8.8 | 2026-08-11 | An unrestricted file upload vulnerability in Cockpit CMS 2.6.0 allows authenticated users to upload files of any extensi |
| CVE-2026-72558 | 8.8 | 2026-08-11 | An SQL injection vulnerability in CiviCRM through 6.18.alpha1 allows authenticated staff to read the entire database via |
| CVE-2026-72561 | 8.8 | 2026-08-11 | A broken access control vulnerability in Peppermint Lab Peppermint through commit ba6e217 allows any authenticated non-a |
| CVE-2026-72562 | 8.8 | 2026-08-11 | An SQL injection vulnerability in Pimcore admin-ui-classic-bundle through version 2.3 allows authenticated backend users |
| CVE-2026-72563 | 8.1 | 2026-08-11 | A broken access control vulnerability in BadChoice Handesk as of 2026-07-10 allows any authenticated agent to overwrite  |
| CVE-2026-72595 | 8.1 | 2026-08-11 | A broken access control vulnerability in BadChoice Handesk as of 2026-07-10 allows any authenticated agent to update tic |
| CVE-2026-72596 | 8.1 | 2026-08-11 | A broken access control vulnerability in Ghost Foundation Ghost 5.x allows authenticated Author-role users to delete pos |
| CVE-2026-72599 | 9.8 | 2026-08-11 | An SQL injection vulnerability in e107 2.4.0 allows unauthenticated remote attackers to execute arbitrary SQL via the ne |
| CVE-2026-72600 | 7.5 | 2026-08-11 | A broken access control vulnerability in Idurar IDURAR ERP CRM 4.1.0 allows unauthenticated remote attackers to download |
| CVE-2026-72601 | 7.5 | 2026-08-11 | A broken access control vulnerability in CSZ CMS 1.3.2 allows unauthenticated remote attackers to read all form submissi |
| CVE-2026-72602 | 7.5 | 2026-08-11 | A path traversal vulnerability in AsyncFuncAI deepwiki-open through commit 16f35a0 allows unauthenticated remote attacke |
| CVE-2026-72603 | 9.9 | 2026-08-11 | An OS command injection vulnerability in wg-easy 15.3.0 allows users with the clients.create permission to execute arbit |
| CVE-2026-72605 | 7.5 | 2026-08-11 | A missing authentication vulnerability in Swing Music 3.0.0 allows unauthenticated remote attackers to create arbitrary  |
| CVE-2026-72606 | 7.5 | 2026-08-11 | A server-side request forgery vulnerability in Pinry through 2.1.13 allows unauthenticated remote attackers to make the  |
| CVE-2026-72607 | 7.1 | 2026-08-11 | A stored SQL injection vulnerability in Koha through 24.11.17, 25.05.12, 25.11.06, and 26.05.01 allows authenticated sta |
| CVE-2026-72609 | 7.1 | 2026-08-11 | An SQL injection vulnerability in Koha through 24.11.17, 25.05.12, 25.11.06, and 26.05.01 allows authenticated staff wit |
| CVE-2026-18972 | 9.6 | 2026-08-11 | An authenticated attacker can spoof another GUI user's identity by sending their request with the custom header \"Grpc-M |
| CVE-2026-50058 | 7.8 | 2026-08-11 | A vulnerability has been identified in Solid Edge SE2025 (All versions < V225.0 Update 15), Solid Edge SE2026 (All versi |
| CVE-2026-50059 | 7.8 | 2026-08-11 | A vulnerability has been identified in Solid Edge SE2025 (All versions < V225.0 Update 15), Solid Edge SE2026 (All versi |
| CVE-2026-50060 | 7.8 | 2026-08-11 | A vulnerability has been identified in Solid Edge SE2025 (All versions < V225.0 Update 15), Solid Edge SE2026 (All versi |
| CVE-2026-50061 | 7.8 | 2026-08-11 | A vulnerability has been identified in Solid Edge SE2025 (All versions < V225.0 Update 15), Solid Edge SE2026 (All versi |
| CVE-2026-50062 | 7.8 | 2026-08-11 | A vulnerability has been identified in Solid Edge SE2025 (All versions < V225.0 Update 15), Solid Edge SE2026 (All versi |
| CVE-2026-50063 | 7.8 | 2026-08-11 | A vulnerability has been identified in Solid Edge SE2025 (All versions < V225.0 Update 15), Solid Edge SE2026 (All versi |
| CVE-2026-50064 | 7.8 | 2026-08-11 | A vulnerability has been identified in Solid Edge SE2025 (All versions < V225.0 Update 15), Solid Edge SE2026 (All versi |
| CVE-2026-58115 | 10.0 | 2026-08-11 | A vulnerability has been identified in SIMATIC IoT2050 Advanced (6ES7647-0BA00-1YA2) (All versions < V4.3.4.1 running In |
| CVE-2026-59086 | 7.8 | 2026-08-11 | A vulnerability has been identified in Simcenter Nastran (All versions < V2606). The affected applications contain a sta |
| CVE-2026-59700 | 7.8 | 2026-08-11 | A vulnerability has been identified in Simcenter Femap (All versions < V2606.0001). The affected applications contains a |
| CVE-2026-59701 | 7.8 | 2026-08-11 | A vulnerability has been identified in Simcenter Femap (All versions < V2606.0001). The affected applications contains a |
| CVE-2026-64629 | 7.8 | 2026-08-11 | A vulnerability has been identified in Parasolid V38.0 (All versions < V38.0.235), Parasolid V38.1 (All versions < V38.1 |
| CVE-2026-69109 | 7.5 | 2026-08-11 | A vulnerability has been identified in Siemens License Server (SLS) (All versions < V5.3). The affected application is v |
| CVE-2026-72745 | 7.5 | 2026-08-11 | FreeRDP before 3.30.0 contains an out-of-bounds vulnerability in kerberos_DecryptMessage() (winpr/libwinpr/sspi/Kerberos |
| CVE-2026-72746 | 7.5 | 2026-08-11 | FreeRDP before 3.30.0 contains a server-side authentication bypass in the RDSTLS handshake. When a server is configured  |
| CVE-2026-72747 | 7.2 | 2026-08-11 | AVideo fails to sanitize the phone field during user registration, allowing unauthenticated attackers to inject maliciou |
| CVE-2026-72748 | 9.1 | 2026-08-11 | AVideo contains an unauthenticated arbitrary file write vulnerability in the aVideoEncoderChunk.json.php endpoint that a |
| CVE-2026-72778 | 8.8 | 2026-08-11 | Craft CMS versions from 4.0.0-RC1 before 4.18.2 and from 5.0.0-RC1 before 5.10.6 contain an authenticated remote code ex |
| CVE-2026-72781 | 8.8 | 2026-08-11 | Craft CMS versions >= 5.0.0-RC1 before 5.10.7 and >= 4.0.0-RC1 before 4.18.3 contain a remote code execution vulnerabili |
| CVE-2026-46670 | 9.8 | 2026-08-11 | YesWiki is a wiki system written in PHP. Prior to version 4.6.4,  an unauthenticated SQL injection in the Bazar form-imp |
| CVE-2026-48056 | 10.0 | 2026-08-11 | Streambert is a cross-platform Electron Desktop App to stream and download video content. Versions prior to 2.5.0  impro |
| CVE-2026-17061 | 10.0 | 2026-08-11 | A Deserialization of Untrusted Data vulnerability affecting SIMULIA Execution Engine from Release 2023 through Release 2 |
| CVE-2026-18125 | 7.5 | 2026-08-11 | An out-of-bounds read in the Agent of Ivanti Endpoint Manager before version 2024 SU7 allows a remote unauthenticated at |
| CVE-2026-18127 | 7.7 | 2026-08-11 | External control of a filename in the Core of Ivanti Endpoint Manager before version 2024 SU7 allows a remote authentica |
| CVE-2026-18129 | 8.1 | 2026-08-11 | Cleartext transmission of sensitive information in the Core of Ivanti Endpoint Manager before version 2024 SU7 allows a  |
| CVE-2026-18635 | 7.2 | 2026-08-11 | Velociraptor's VQL has a query() plugin which allows running a VQL query in a different org or user context. To be able  |
| CVE-2026-18860 | 8.7 | 2026-08-11 | Velociraptor allows multi-tenant deployments named "Orgs".

By default Velociraptor, uses the ROOT org, but users can cr |
| CVE-2026-72920 | 9.8 | 2026-08-11 | SeaweedFS is a distributed storage system. Prior to 4.24, the filer registers the SeaweedIdentityAccessManagement gRPC s |
| CVE-2026-72921 | 8.1 | 2026-08-11 | SeaweedFS is a distributed storage system. Prior to 4.24, the weed/server/filer_server_handlers.go allowed_prefixes auth |
| CVE-2026-72922 | 8.2 | 2026-08-11 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agent |
| CVE-2026-18639 | 7.3 | 2026-08-11 | When Velociraptor is configured to use an OIDC IdP for authentication, it uses the email claim as a username. However, s |
| CVE-2026-18640 | 7.1 | 2026-08-11 | The NewNotebook API does not sufficiently sanitize its parameters allowing an authenticated user with NOTEBOOK_EDIT perm |
| CVE-2026-19546 | 8.8 | 2026-08-11 | A flaw was found in DBI. This is a fix for a partial fix for CVE-2026-14380 for RHEL 9.8.z and 10.2.z.

For a detailed S |
| CVE-2026-42142 | 7.1 | 2026-08-11 | TypeBot is a chatbot builder tool. Prior to version 3.17.0, the `handleGetSheets` API handler (`POST /api/sheets/getShee |
| CVE-2026-48495 | 7.1 | 2026-08-11 | TypeBot is a chatbot builder tool. Prior to version 3.17.0, the Google Sheets OAuth callback decodes a base64-encoded JS |
| CVE-2026-48766 | 7.6 | 2026-08-11 | TypeBot is a chatbot builder tool. Versions prior to 3.17.0 allow a low-privilege guest member of a workspace to exfiltr |
| CVE-2026-53413 | 8.3 | 2026-08-11 | Missing bounds check in the annotator function of Zoom Clients allows buffer over-write, which may allow a meeting parti |
| CVE-2026-53415 | 8.3 | 2026-08-11 | Use after Free in the annotator function of Zoom Clients may allow a meeting participant to achieve remote code executio |
| CVE-2026-53416 | 7.1 | 2026-08-11 | Path traversal in Zoom VDI Client and Plugins may allow an authenticated user to conduct information disclosure via loca |
| CVE-2026-56721 | 8.8 | 2026-08-11 | CamaleonCMS version 2.9.2 and earlier contains a privilege escalation vulnerability via insecure direct object reference |
| CVE-2026-67179 | 7.8 | 2026-08-11 | Genkit does not properly validate host request headers. Any host on the developer's network, and any website the develop |
| CVE-2026-67180 | 8.4 | 2026-08-11 | Google Turbinia allows arbitrary command execution via worker tasks. An attacker with privileges to submit a processing  |
| CVE-2026-73069 | 9.1 | 2026-08-11 | Twenty is an open-source CRM (customer relationship management) platform. Prior to 2.15.0, Twenty allowed a workspace ad |
| CVE-2026-73079 | 8.5 | 2026-08-11 | Sub2API is an AI API gateway platform designed to distribute and manage API quotas from AI product subscriptions. From 0 |
| CVE-2026-73080 | 9.3 | 2026-08-11 | SeaweedFS is a distributed storage system. Prior to 4.24, VolumeServer.FetchAndWriteNeedle in weed/server/volume_grpc_re |
| CVE-2026-12571 | 9.8 | 2026-08-11 | An authentication bypass in ManageEngine DDI Central's password-reset workflow allows account takeover. |
| CVE-2026-20349 | 8.6 | 2026-08-11 | A vulnerability in the Remote Access SSL VPN service for Cisco Secure Firewall Adaptive Security Appliance (ASA) Softwar |
| CVE-2026-21273 | 8.7 | 2026-08-11 | is affected by an Improper Input Validation vulnerability that could result in privilege escalation. A low-privileged at |
| CVE-2026-21279 | 8.2 | 2026-08-11 | is affected by an Improper Input Validation vulnerability that could result in a Security feature bypass. An attacker co |
| CVE-2026-25652 | 7.8 | 2026-08-11 | is affected by an Incorrect Authorization vulnerability that could result in privilege escalation. A low-privileged atta |
| CVE-2026-34635 | 8.4 | 2026-08-11 | is affected by a Use of Hard-coded Cryptographic Key vulnerability that could result in a Security feature bypass. A low |
| CVE-2026-42976 | 7.8 | 2026-08-11 | Missing authentication for critical function in Windows RPC API allows an authorized attacker to elevate privileges loca |
| CVE-2026-47299 | 7.2 | 2026-08-11 | Improper neutralization of special elements used in a command ('command injection') in Azure Monitor Agent allows an aut |
| CVE-2026-48362 | 10.0 | 2026-08-11 | ColdFusion is affected by an Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')  |
| CVE-2026-48385 | 7.7 | 2026-08-11 | ColdFusion is affected by an Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')  |
| CVE-2026-48386 | 7.5 | 2026-08-11 | ColdFusion is affected by a Use of a Broken or Risky Cryptographic Algorithm vulnerability that could lead to disclosure |
| CVE-2026-48438 | 7.5 | 2026-08-11 | CAI Content Credentials is affected by a NULL Pointer Dereference vulnerability that could result in an application deni |
| CVE-2026-48439 | 7.5 | 2026-08-11 | CAI Content Credentials is affected by an Uncontrolled Resource Consumption vulnerability that could lead to application |
| CVE-2026-48440 | 8.1 | 2026-08-11 | ColdFusion is affected by a Heap-based Buffer Overflow vulnerability that could result in arbitrary code execution in th |
| CVE-2026-48442 | 7.1 | 2026-08-11 | CAI Content Credentials is affected by an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') |
| CVE-2026-49179 | 8.8 | 2026-08-11 | Improper neutralization of special elements used in a command ('command injection') in Windows Active Directory allows a |
| CVE-2026-50472 | 7.0 | 2026-08-11 | Heap-based buffer overflow in Windows LUAFV allows an authorized attacker to elevate privileges locally. |
| CVE-2026-50516 | 9.4 | 2026-08-11 | Missing authentication for critical function in Microsoft Azure Kubernetes Service allows an unauthorized attacker to el |
| CVE-2026-54113 | 7.5 | 2026-08-11 | Allocation of resources without limits or throttling in Windows Kernel allows an unauthorized attacker to deny service o |
| CVE-2026-54981 | 7.8 | 2026-08-11 | Inclusion of functionality from untrusted control sphere in Visual Studio Code - Python extension allows an unauthorized |
| CVE-2026-54984 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Imaging Component allows an unauthorized attacker to execute code locally. |
| CVE-2026-56174 | 7.8 | 2026-08-11 | Untrusted search path in Windows Narrator Braille allows an authorized attacker to elevate privileges locally. |
| CVE-2026-56179 | 8.3 | 2026-08-11 | Origin validation error in Windows Network Address Translation (NAT) allows an unauthorized attacker to perform spoofing |
| CVE-2026-57104 | 8.8 | 2026-08-11 | Improper neutralization of input during web page generation ('cross-site scripting') in Azure Storage Explorer allows an |
| CVE-2026-57105 | 8.0 | 2026-08-11 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allo |
| CVE-2026-58612 | 7.4 | 2026-08-11 | Server-side request forgery (ssrf) in Microsoft PowerShell Core allows an unauthorized attacker to disclose information  |
| CVE-2026-58641 | 7.8 | 2026-08-11 | Integer overflow or wraparound in .NET allows an unauthorized attacker to elevate privileges locally. |
| CVE-2026-58650 | 7.8 | 2026-08-11 | Authorization bypass through user-controlled key in Visual Studio Code allows an unauthorized attacker to bypass a secur |
| CVE-2026-58651 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-59113 | 8.8 | 2026-08-11 | Missing authorization in Visual Studio Code allows an unauthorized attacker to execute code over a network. |
| CVE-2026-59119 | 7.3 | 2026-08-11 | Incorrect default permissions in Microsoft PowerShell allows an authorized attacker to elevate privileges locally. |
| CVE-2026-59122 | 7.0 | 2026-08-11 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Telephony Service |
| CVE-2026-59124 | 9.8 | 2026-08-11 | Deserialization of untrusted data in Microsoft High Performance Computing (HPC) Pack allows an unauthorized attacker to  |
| CVE-2026-59125 | 7.0 | 2026-08-11 | Use after free in Virtual Hard Disk (VHD) Miniport Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-59126 | 7.0 | 2026-08-11 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Event Logging Ser |
| CVE-2026-59127 | 7.8 | 2026-08-11 | Integer overflow or wraparound in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-59132 | 7.5 | 2026-08-11 | Null pointer dereference in Windows TCP/IP allows an unauthorized attacker to deny service over a network. |
| CVE-2026-59133 | 8.8 | 2026-08-11 | Execution with unnecessary privileges in Microsoft High Performance Computing (HPC) Pack allows an authorized attacker t |
| CVE-2026-59134 | 7.5 | 2026-08-11 | Heap-based buffer overflow in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-61346 | 7.0 | 2026-08-11 | Use after free in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-61348 | 7.0 | 2026-08-11 | Use after free in Windows Ancillary Function Driver for WinSock allows an authorized attacker to elevate privileges loca |
| CVE-2026-61349 | 7.8 | 2026-08-11 | Use after free in Windows Work Folder Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-61352 | 7.5 | 2026-08-11 | Concurrent execution using shared resource with improper synchronization ('race condition') in Remote Desktop Client all |
| CVE-2026-61353 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Telephony Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-61355 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Sensor Data Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-61356 | 7.8 | 2026-08-11 | Missing authentication for critical function in Windows Remote Desktop Services allows an authorized attacker to elevate |
| CVE-2026-61357 | 7.8 | 2026-08-11 | Use after free in Application Information Services allows an authorized attacker to elevate privileges locally. |
| CVE-2026-61358 | 7.8 | 2026-08-11 | Improper link resolution before file access ('link following') in Windows Accessibility Infrastructure (ATBroker.exe) al |
| CVE-2026-61359 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Storage allows an authorized attacker to elevate privileges locally. |
| CVE-2026-61361 | 7.0 | 2026-08-11 | Use after free in Windows DHCP Client allows an authorized attacker to execute code locally. |
| CVE-2026-61363 | 7.5 | 2026-08-11 | Heap-based buffer overflow in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-61364 | 7.8 | 2026-08-11 | Missing authentication for critical function in Windows Remote Desktop Services allows an authorized attacker to elevate |
| CVE-2026-61365 | 7.8 | 2026-08-11 | Missing authentication for critical function in Windows Remote Desktop Services allows an authorized attacker to elevate |
| CVE-2026-61366 | 7.0 | 2026-08-11 | Double free in Windows Network Connection Broker allows an authorized attacker to elevate privileges locally. |
| CVE-2026-61367 | 7.8 | 2026-08-11 | Missing authentication for critical function in Windows Remote Desktop Services allows an authorized attacker to elevate |
| CVE-2026-61923 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Display Enhancement Service allows an authorized attacker to elevate privileges lo |
| CVE-2026-61925 | 7.8 | 2026-08-11 | Incorrect authorization in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-61926 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows USB Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-61927 | 7.0 | 2026-08-11 | Use after free in Windows Bind Filter Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-61929 | 7.0 | 2026-08-11 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-61930 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-61932 | 7.8 | 2026-08-11 | Access of resource using incompatible type ('type confusion') in Windows DWM Core Library allows an authorized attacker  |
| CVE-2026-61934 | 7.8 | 2026-08-11 | Use after free in Windows Bind Filter Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-61937 | 7.8 | 2026-08-11 | Integer overflow or wraparound in Windows HTTP.sys allows an authorized attacker to elevate privileges locally. |
| CVE-2026-61938 | 7.0 | 2026-08-11 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-61939 | 7.0 | 2026-08-11 | Use after free in Winlogon allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62688 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows MIDI Service Module allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62690 | 7.0 | 2026-08-11 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Push Notification |
| CVE-2026-62692 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Remote Desktop Services allows an authorized attacker to elevate privileges locall |
| CVE-2026-62693 | 7.0 | 2026-08-11 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows MIDI Service Modu |
| CVE-2026-62695 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Storage allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62696 | 7.8 | 2026-08-11 | Integer underflow (wrap or wraparound) in Windows Program Compatibility Assistant Service allows an authorized attacker  |
| CVE-2026-62698 | 7.8 | 2026-08-11 | Numeric truncation error in Microsoft Digest Authentication allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62700 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62701 | 7.8 | 2026-08-11 | Use after free in Windows Telephony Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62705 | 7.0 | 2026-08-11 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Bind Filter Drive |
| CVE-2026-62707 | 7.8 | 2026-08-11 | Use after free in Windows Modern Device Management (MDM) allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62710 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Device Association Service allows an authorized attacker to elevate privileges loc |
| CVE-2026-62711 | 7.8 | 2026-08-11 | Use after free in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62712 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62713 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Cloud Files Mini Filter Driver allows an authorized attacker to elevate privileges |
| CVE-2026-62717 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Message Queuing allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62719 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Message Queuing allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62721 | 7.8 | 2026-08-11 | Insufficient granularity of access control in User-Mode Power Service (UMPS) allows an authorized attacker to elevate pr |
| CVE-2026-62722 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Bind Filter Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62723 | 7.0 | 2026-08-11 | Use after free in Windows Telephony Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62724 | 7.0 | 2026-08-11 | Use after free in Windows Telephony Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62725 | 7.0 | 2026-08-11 | Use after free in Windows Telephony Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62726 | 7.0 | 2026-08-11 | Use after free in Windows Telephony Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62728 | 7.0 | 2026-08-11 | Time-of-check time-of-use (toctou) race condition in Windows Common Log File System Driver allows an authorized attacker |
| CVE-2026-62729 | 7.0 | 2026-08-11 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Telephony Service |
| CVE-2026-62732 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Telephony Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62733 | 7.8 | 2026-08-11 | Out-of-bounds read in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62734 | 7.0 | 2026-08-11 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Telephony Service |
| CVE-2026-62735 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows HTTP.sys allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62736 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows DHCP Client allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62737 | 7.8 | 2026-08-11 | Untrusted pointer dereference in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62739 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows HTTP.sys allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62741 | 7.8 | 2026-08-11 | Integer underflow (wrap or wraparound) in Windows HTTP.sys allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62747 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Device Association Service allows an authorized attacker to elevate privileges loc |
| CVE-2026-62748 | 7.0 | 2026-08-11 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Telephony Service |
| CVE-2026-62749 | 7.0 | 2026-08-11 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62751 | 7.8 | 2026-08-11 | Integer overflow or wraparound in Windows Projected File System allows an authorized attacker to elevate privileges loca |
| CVE-2026-62752 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Kerberos allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62753 | 7.0 | 2026-08-11 | Heap-based buffer overflow in Windows HTTP.sys allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62754 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Kerberos allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62755 | 7.8 | 2026-08-11 | Stack-based buffer overflow in Windows DHCP Client allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62758 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Remote Access Connection Manager allows an authorized attacker to elevate privileg |
| CVE-2026-62761 | 7.8 | 2026-08-11 | Improper link resolution before file access ('link following') in Windows DHCP Server allows an authorized attacker to e |
| CVE-2026-62766 | 7.0 | 2026-08-11 | Double free in Windows Kerberos allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62768 | 7.8 | 2026-08-11 | Stack-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62770 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Shell allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62771 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Cloud Files Mini Filter Driver allows an authorized attacker to elevate privileges |
| CVE-2026-62772 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Container Isolation FS Filter Driver (unionfs.sys) allows an authorized attacker t |
| CVE-2026-62773 | 7.0 | 2026-08-11 | Use after free in Windows Kerberos allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62774 | 7.0 | 2026-08-11 | Use after free in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62776 | 7.8 | 2026-08-11 | Improper link resolution before file access ('link following') in Windows DHCP Server allows an authorized attacker to e |
| CVE-2026-62777 | 7.8 | 2026-08-11 | Missing authentication for critical function in Windows License Manager allows an authorized attacker to elevate privile |
| CVE-2026-62778 | 8.1 | 2026-08-11 | Use after free in Windows DNS allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-62779 | 7.8 | 2026-08-11 | Use after free in Windows Schannel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62780 | 7.0 | 2026-08-11 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62781 | 8.1 | 2026-08-11 | Heap-based buffer overflow in RPC Runtime allows an unauthorized attacker to execute code over a network. |
| CVE-2026-62783 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Remote Access Connection Manager allows an authorized attacker to elevate privileg |
| CVE-2026-62784 | 8.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Local Security Authority Server (lsasrv) allows an authorized attacker to execut |
| CVE-2026-62785 | 8.8 | 2026-08-11 | Heap-based buffer overflow in Windows LDAP - Lightweight Directory Access Protocol allows an unauthorized attacker to ex |
| CVE-2026-62787 | 7.5 | 2026-08-11 | Use after free in Windows DNS allows an authorized attacker to execute code over a network. |
| CVE-2026-62788 | 7.0 | 2026-08-11 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62790 | 8.8 | 2026-08-11 | Heap-based buffer overflow in Windows SMB Server allows an authorized attacker to execute code over a network. |
| CVE-2026-62792 | 8.1 | 2026-08-11 | Stack-based buffer overflow in Windows TCP/IP allows an unauthorized attacker to execute code over a network. |
| CVE-2026-62795 | 8.8 | 2026-08-11 | Use after free in Windows LDAP - Lightweight Directory Access Protocol allows an unauthorized attacker to execute code o |
| CVE-2026-62797 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62799 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows SMB Client allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62800 | 8.8 | 2026-08-11 | Heap-based buffer overflow in Windows SMB Server allows an authorized attacker to execute code over a network. |
| CVE-2026-62803 | 7.8 | 2026-08-11 | Improper link resolution before file access ('link following') in Windows DHCP Server allows an authorized attacker to e |
| CVE-2026-62807 | 7.8 | 2026-08-11 | Improper link resolution before file access ('link following') in Windows DHCP Server allows an authorized attacker to e |
| CVE-2026-62811 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows HTTP.sys allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62812 | 7.8 | 2026-08-11 | Improper link resolution before file access ('link following') in Windows DHCP Server allows an authorized attacker to e |
| CVE-2026-62815 | 9.8 | 2026-08-11 | Use after free in Microsoft QUIC allows an unauthorized attacker to execute code over a network. |
| CVE-2026-62816 | 8.8 | 2026-08-11 | Heap-based buffer overflow in Reliable Multicast Transport Driver (RMCAST) allows an unauthorized attacker to execute co |
| CVE-2026-62817 | 8.8 | 2026-08-11 | Out-of-bounds write in Windows DNS allows an unauthorized attacker to execute code over an adjacent network. |
| CVE-2026-62818 | 8.8 | 2026-08-11 | Use after free in Active Directory Certificate Services (AD CS) allows an authorized attacker to execute code over a net |
| CVE-2026-62819 | 8.1 | 2026-08-11 | Remote Code Execution in Windows Routing and Remote Access Service (RRAS) allows attacker to gain an unauthorized access |
| CVE-2026-62820 | 8.1 | 2026-08-11 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows DNS allows an una |
| CVE-2026-62822 | 8.8 | 2026-08-11 | Integer overflow or wraparound in Windows GDI+ allows an unauthorized attacker to execute code over a network. |
| CVE-2026-62823 | 8.8 | 2026-08-11 | Heap-based buffer overflow in Windows DHCP Server allows an unauthorized attacker to execute code over an adjacent netwo |
| CVE-2026-62824 | 8.8 | 2026-08-11 | Stack-based buffer overflow in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-62827 | 8.8 | 2026-08-11 | Improper authentication in Microsoft Office SharePoint allows an authorized attacker to elevate privileges over a networ |
| CVE-2026-62832 | 7.8 | 2026-08-11 | Improper link resolution before file access ('link following') in Windows User Profile Service allows an authorized atta |
| CVE-2026-62869 | 8.8 | 2026-08-11 | Insufficient verification of data authenticity in Azure Entra ID allows an authorized attacker to perform spoofing over  |
| CVE-2026-62871 | 7.8 | 2026-08-11 | Out-of-bounds write in .NET allows an unauthorized attacker to execute code locally. |
| CVE-2026-62872 | 8.8 | 2026-08-11 | Incorrect authorization in .NET Framework allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-62876 | 7.8 | 2026-08-11 | Out-of-bounds read in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62877 | 7.8 | 2026-08-11 | Stack-based buffer overflow in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62878 | 9.8 | 2026-08-11 | Stack-based buffer overflow in Windows DNS allows an unauthorized attacker to execute code over a network. |
| CVE-2026-62880 | 7.8 | 2026-08-11 | Out-of-bounds read in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62885 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62886 | 7.8 | 2026-08-11 | Integer overflow or wraparound in .NET allows an unauthorized attacker to elevate privileges locally. |
| CVE-2026-62888 | 7.8 | 2026-08-11 | Use after free in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62889 | 8.1 | 2026-08-11 | Double free in Windows Secure Socket Tunneling Protocol (SSTP) allows an unauthorized attacker to execute code over a ne |
| CVE-2026-62890 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows GDI+ allows an authorized attacker to execute code locally. |
| CVE-2026-62892 | 7.0 | 2026-08-11 | Use after free in Capability Access Management Service (camsvc) allows an authorized attacker to elevate privileges loca |
| CVE-2026-62893 | 9.8 | 2026-08-11 | Use after free in Windows Deployment Services allows an unauthorized attacker to execute code over a network. |
| CVE-2026-62894 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62897 | 7.0 | 2026-08-11 | Integer overflow or wraparound in .NET Framework allows an unauthorized attacker to execute code locally. |
| CVE-2026-62898 | 7.5 | 2026-08-11 | Use after free in Microsoft QUIC allows an unauthorized attacker to disclose information over a network. |
| CVE-2026-62901 | 7.5 | 2026-08-11 | Unchecked input for loop condition in .NET allows an unauthorized attacker to deny service over a network. |
| CVE-2026-62908 | 7.0 | 2026-08-11 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Backup Engine all |
| CVE-2026-62909 | 7.8 | 2026-08-11 | Uncaught exception in .NET allows an authorized attacker to elevate privileges locally. |
| CVE-2026-62910 | 7.2 | 2026-08-11 | Improper control of resource identifiers ('resource injection') in Microsoft Exchange Server allows an authorized attack |
| CVE-2026-62911 | 8.0 | 2026-08-11 | Authentication bypass by capture-replay in Microsoft Exchange Server allows an authorized attacker to elevate privileges |
| CVE-2026-62913 | 8.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Exchange Server allows an authorized attacker to execute code over a network. |
| CVE-2026-62914 | 7.3 | 2026-08-11 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Exchange Server allows |
| CVE-2026-63513 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-63514 | 8.8 | 2026-08-11 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a ne |
| CVE-2026-63515 | 7.8 | 2026-08-11 | Out-of-bounds read in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-63518 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-63519 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-63520 | 8.1 | 2026-08-11 | Improper input validation in Microsoft Office SharePoint allows an unauthorized attacker to execute code over a network. |
| CVE-2026-63522 | 7.8 | 2026-08-11 | Incorrect permission assignment for critical resource in Azure SQL Database allows an authorized attacker to elevate pri |
| CVE-2026-63525 | 7.8 | 2026-08-11 | Numeric truncation error in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-63526 | 7.8 | 2026-08-11 | Stack-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-63527 | 7.8 | 2026-08-11 | Stack-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-63532 | 7.8 | 2026-08-11 | Integer overflow or wraparound in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-63533 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-64898 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-64900 | 7.3 | 2026-08-11 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allo |
| CVE-2026-64901 | 8.8 | 2026-08-11 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a ne |
| CVE-2026-64903 | 7.8 | 2026-08-11 | Integer overflow or wraparound in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-64904 | 7.8 | 2026-08-11 | Access of resource using incompatible type ('type confusion') in Microsoft Office allows an unauthorized attacker to exe |
| CVE-2026-64905 | 7.8 | 2026-08-11 | Buffer over-read in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-64906 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code locally. |
| CVE-2026-64907 | 7.8 | 2026-08-11 | Stack-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-64908 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code locally. |
| CVE-2026-64909 | 7.8 | 2026-08-11 | Integer underflow (wrap or wraparound) in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-64910 | 7.8 | 2026-08-11 | Untrusted pointer dereference in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-64911 | 7.8 | 2026-08-11 | Integer overflow or wraparound in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-64912 | 7.8 | 2026-08-11 | Stack-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code locally. |
| CVE-2026-64914 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code locally. |
| CVE-2026-64915 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-64919 | 7.8 | 2026-08-11 | Stack-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code locally. |
| CVE-2026-64920 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code locally. |
| CVE-2026-64921 | 8.8 | 2026-08-11 | Missing authentication for critical function in Microsoft Office SharePoint allows an authorized attacker to elevate pri |
| CVE-2026-65656 | 7.8 | 2026-08-11 | Improper neutralization of special elements used in a command ('command injection') in Microsoft Office allows an unauth |
| CVE-2026-65657 | 7.8 | 2026-08-11 | Use after free in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-65658 | 8.8 | 2026-08-11 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a ne |
| CVE-2026-65661 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-65663 | 8.8 | 2026-08-11 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a ne |
| CVE-2026-65664 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-65665 | 8.8 | 2026-08-11 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a ne |
| CVE-2026-65671 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Remote Access API allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65672 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Remote Access API allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65673 | 7.8 | 2026-08-11 | Entra Connect Elevation of Privilege Vulnerability |
| CVE-2026-65675 | 7.1 | 2026-08-11 | No cwe for this issue in Visual Studio Code CoPilot Chat Extension allows an unauthorized attacker to bypass a security  |
| CVE-2026-65678 | 7.0 | 2026-08-11 | Use after free in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65679 | 8.1 | 2026-08-11 | Heap-based buffer overflow in Windows iSCSI Target Service allows an unauthorized attacker to execute code over a networ |
| CVE-2026-65681 | 7.5 | 2026-08-11 | Null pointer dereference in Windows iSCSI Target Service allows an unauthorized attacker to deny service over a network. |
| CVE-2026-65767 | 8.8 | 2026-08-11 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Teams for Android allo |
| CVE-2026-65768 | 8.8 | 2026-08-11 | Improper limitation of a pathname to a restricted directory ('path traversal') in Microsoft Teams for Android allows an  |
| CVE-2026-65773 | 7.8 | 2026-08-11 | Improper access control in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65774 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65775 | 7.8 | 2026-08-11 | Use after free in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65776 | 7.0 | 2026-08-11 | Use after free in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65778 | 7.0 | 2026-08-11 | Use after free in Windows Autopilot allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65779 | 7.0 | 2026-08-11 | Use after free in Windows Autopilot allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65780 | 7.0 | 2026-08-11 | Double free in Windows Autopilot allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65781 | 7.0 | 2026-08-11 | Use after free in Windows Autopilot allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65782 | 7.0 | 2026-08-11 | Use after free in Windows Autopilot allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65783 | 7.0 | 2026-08-11 | Use after free in Windows Autopilot allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65786 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Desktop Window Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65787 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Desktop Window Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65788 | 7.0 | 2026-08-11 | Use after free in Desktop Window Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65789 | 8.1 | 2026-08-11 | Use after free in Windows DNS allows an unauthorized attacker to execute code over a network. |
| CVE-2026-65790 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Message Queuing allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65791 | 9.8 | 2026-08-11 | Heap-based buffer overflow in Windows iSCSI Target Service allows an unauthorized attacker to execute code over a networ |
| CVE-2026-65807 | 8.8 | 2026-08-11 | Access of resource using incompatible type ('type confusion') in Microsoft Office Excel allows an unauthorized attacker  |
| CVE-2026-65810 | 7.8 | 2026-08-11 | Relative path traversal in .NET Framework allows an unauthorized attacker to elevate privileges locally. |
| CVE-2026-65811 | 8.8 | 2026-08-11 | Improper input validation in Power BI allows an authorized attacker to execute code over a network. |
| CVE-2026-65814 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Storage Port Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-65815 | 8.8 | 2026-08-11 | Deserialization of untrusted data in Microsoft Dynamics 365 (on-premises) allows an authorized attacker to execute code  |
| CVE-2026-66799 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Key Guard allows an authorized attacker to elevate privileges locally. |
| CVE-2026-66802 | 8.1 | 2026-08-11 | Concurrent execution using shared resource with improper synchronization ('race condition') in Microsoft Azure Attestati |
| CVE-2026-66804 | 7.8 | 2026-08-11 | Improper access control in Windows Cross Device Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-66805 | 8.8 | 2026-08-11 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a ne |
| CVE-2026-66807 | 7.8 | 2026-08-11 | Stack-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-66808 | 8.8 | 2026-08-11 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a ne |
| CVE-2026-68792 | 7.8 | 2026-08-11 | Improper neutralization of special elements used in a command ('command injection') in Microsoft Office allows an author |
| CVE-2026-68793 | 7.8 | 2026-08-11 | Out-of-bounds read in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-68794 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-68795 | 7.8 | 2026-08-11 | Stack-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-68796 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-68798 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-68800 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-68801 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-68803 | 7.8 | 2026-08-11 | Access of resource using incompatible type ('type confusion') in Microsoft Office Excel allows an unauthorized attacker  |
| CVE-2026-68804 | 7.8 | 2026-08-11 | Numeric truncation error in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-68805 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-68806 | 7.8 | 2026-08-11 | Out-of-bounds write in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-68807 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-68810 | 7.8 | 2026-08-11 | Untrusted pointer dereference in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-68811 | 7.8 | 2026-08-11 | Access of resource using incompatible type ('type confusion') in Microsoft Office Excel allows an unauthorized attacker  |
| CVE-2026-68812 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-68814 | 7.8 | 2026-08-11 | Out-of-bounds read in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-68815 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-68816 | 7.8 | 2026-08-11 | Stack-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-68817 | 7.8 | 2026-08-11 | Stack-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-68820 | 7.0 | 2026-08-11 | Use after free in Windows Ancillary Function Driver for WinSock allows an authorized attacker to elevate privileges loca |
| CVE-2026-68821 | 7.3 | 2026-08-11 | Improper privilege management in Windows Package Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-69278 | 7.8 | 2026-08-11 | Incorrect authorization in Visual Studio Code allows an unauthorized attacker to bypass a security feature locally. |
| CVE-2026-69306 | 8.2 | 2026-08-11 | Not failing securely ('failing open') in Visual Studio Code allows an unauthorized attacker to bypass a security feature |
| CVE-2026-69320 | 8.8 | 2026-08-11 | Improper neutralization of special elements used in an os command ('os command injection') in Visual Studio Code allows  |
| CVE-2026-70130 | 8.4 | 2026-08-11 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-70306 | 9.3 | 2026-08-11 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allo |
| CVE-2026-70307 | 7.0 | 2026-08-11 | Use after free in Windows Ancillary Function Driver for WinSock allows an authorized attacker to elevate privileges loca |
| CVE-2026-70311 | 7.8 | 2026-08-11 | Use after free in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-70313 | 7.8 | 2026-08-11 | Improper input validation in Microsoft Office PowerPoint allows an unauthorized attacker to disclose information locally |
| CVE-2026-70321 | 8.8 | 2026-08-11 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a ne |
| CVE-2026-70324 | 8.8 | 2026-08-11 | Server-side request forgery (ssrf) in Microsoft Office SharePoint allows an authorized attacker to elevate privileges ov |
| CVE-2026-70326 | 8.8 | 2026-08-11 | Server-side request forgery (ssrf) in Microsoft Office SharePoint allows an authorized attacker to elevate privileges ov |
| CVE-2026-70329 | 8.8 | 2026-08-11 | Integer overflow or wraparound in Microsoft Office Outlook allows an unauthorized attacker to execute code over a networ |
| CVE-2026-70335 | 7.8 | 2026-08-11 | Improper neutralization of special elements used in an os command ('os command injection') in GitHub Copilot and Visual  |
| CVE-2026-70336 | 8.8 | 2026-08-11 | Improper control of generation of code ('code injection') in Visual Studio Code allows an unauthorized attacker to execu |
| CVE-2026-70337 | 8.8 | 2026-08-11 | Relative path traversal in Microsoft PowerShell Core allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70338 | 7.8 | 2026-08-11 | Improper control of generation of code ('code injection') in Microsoft PowerShell allows an unauthorized attacker to byp |
| CVE-2026-70340 | 8.1 | 2026-08-11 | Missing authorization in Azure CycleCloud allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-70344 | 7.8 | 2026-08-11 | Stack-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70345 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70346 | 7.8 | 2026-08-11 | Stack-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70347 | 7.8 | 2026-08-11 | Heap-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70354 | 7.8 | 2026-08-11 | Out-of-bounds write in .NET allows an unauthorized attacker to execute code locally. |
| CVE-2026-70355 | 7.3 | 2026-08-11 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allo |
| CVE-2026-71331 | 8.1 | 2026-08-11 | Integer overflow or wraparound in Microsoft Azure Attestation service and Device Health Attestation Service allows an un |
| CVE-2026-71383 | 7.3 | 2026-08-11 | is affected by an Incorrect Authorization vulnerability that could result in a Security feature bypass. An attacker coul |
| CVE-2026-71384 | 9.6 | 2026-08-11 | is affected by an Incorrect Authorization vulnerability that could result in a Security feature bypass. An attacker coul |
| CVE-2026-71386 | 8.8 | 2026-08-11 | is affected by a Cross-site Scripting (XSS) vulnerability that could result in arbitrary code execution in the context o |
| CVE-2026-71387 | 8.8 | 2026-08-11 | ColdFusion is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the  |
| CVE-2026-73086 | 7.4 | 2026-08-11 | nanoid is a secure, URL-friendly, unique string ID generator for JavaScript. Prior to versions 3.3.12 and 5.1.11, the na |
| CVE-2026-73088 | 7.5 | 2026-08-11 | Browserslist is a configuration tool for sharing target browsers and Node.js versions between front-end tools. Prior to  |
| CVE-2026-73089 | 7.5 | 2026-08-11 | Browserslist is a configuration tool for sharing target browsers and Node.js versions between front-end tools. Prior to  |
| CVE-2016-20097 | 7.5 | 2026-08-11 | Weaver (Fanwei) E-cology 8.0 contains a SQL injection vulnerability in the SignatureDownLoad servlet that allows unauthe |
| CVE-2022-50997 | 7.5 | 2026-08-11 | Weaver (Fanwei) E-cology 8.0 and 9.0 contains a SQL injection vulnerability in the HrmCareerApplyPerView.jsp endpoint th |
| CVE-2026-27302 | 10.0 | 2026-08-11 | Adobe Campaign Classic (ACC) is affected by an Incorrect Authorization vulnerability that could result in arbitrary code |
| CVE-2026-47705 | 9.6 | 2026-08-11 | TypeBot is a chatbot builder tool. Version 3.16.1 has a CSV injection vulnerability in the result export functionality.  |
| CVE-2026-47940 | 7.8 | 2026-08-11 | Lightroom Classic is affected by an Integer Overflow or Wraparound vulnerability that could result in arbitrary code exe |
| CVE-2026-48381 | 9.0 | 2026-08-11 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL  |
| CVE-2026-48397 | 8.6 | 2026-08-11 | Lightroom Classic is affected by a Deserialization of Untrusted Data vulnerability that could result in arbitrary code e |
| CVE-2026-48404 | 7.8 | 2026-08-11 | Lightroom Classic is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-48405 | 7.8 | 2026-08-11 | Lightroom Classic is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-48406 | 7.8 | 2026-08-11 | Lightroom Classic is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-48407 | 7.8 | 2026-08-11 | Lightroom Classic is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-48408 | 7.8 | 2026-08-11 | Lightroom Classic is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-48409 | 7.8 | 2026-08-11 | Lightroom Classic is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-48410 | 7.8 | 2026-08-11 | Lightroom Classic is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-48413 | 8.7 | 2026-08-11 | Adobe Commerce is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by a low-privileged |
| CVE-2026-48414 | 7.7 | 2026-08-11 | Adobe Commerce is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by a low-privileged |
| CVE-2026-48415 | 7.6 | 2026-08-11 | Adobe Commerce is affected by an Incorrect Authorization vulnerability that could result in a Security feature bypass. A |
| CVE-2026-48416 | 7.5 | 2026-08-11 | Adobe Commerce is affected by an Incorrect Authorization vulnerability that could result in a Security feature bypass. A |
| CVE-2026-48441 | 8.6 | 2026-08-11 | Lightroom Classic is affected by an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulne |
| CVE-2026-48447 | 7.7 | 2026-08-11 | Lightroom Classic is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution  |
| CVE-2026-48767 | 7.6 | 2026-08-11 | TypeBot is a chatbot builder tool. Versions prior to 3.17.0 allow a low-privilege guest member of a workspace to obtain  |
| CVE-2026-48771 | 8.2 | 2026-08-11 | ishankportfolio is a portfolio website. Prior to version 1.0.1, contact form submissions could potentially be exposed du |
| CVE-2026-69102 | 9.8 | 2026-08-11 | MaxKey contains an unauthorized access vulnerability due to a hard-coded JWT signing secret in application-maxkey.proper |
| CVE-2026-71362 | 9.1 | 2026-08-11 | Adobe Commerce is affected by an Incorrect Authorization vulnerability that could result in privilege escalation. An att |
| CVE-2026-71398 | 10.0 | 2026-08-11 | Adobe Campaign Classic (ACC) is affected by an Incorrect Authorization vulnerability that could result in arbitrary code |
| CVE-2026-72713 | 7.5 | 2026-08-11 | XAgent contains a path traversal vulnerability in the workspace file endpoint that allows self-registered or default-cre |
| CVE-2026-73090 | 9.3 | 2026-08-11 | PeerTube is an ActivityPub-federated video streaming platform. Prior to 8.2.2, processUpdateActivity and processUpdateVi |
| CVE-2026-73211 | 9.8 | 2026-08-11 | PeerTube is an ActivityPub-federated video streaming platform. Prior to 8.1.6, ActorFollowModel.updateScore() interpolat |
| CVE-2026-15426 | 8.8 | 2026-08-11 | The AcyMailing – An Ultimate Newsletter Plugin and Marketing Automation Solution for WordPress plugin for WordPress is v |
| CVE-2026-18687 | 7.1 | 2026-08-11 | MongoDB Server's handling of a Queryable Encryption maintenance operation did not properly validate certain request para |
| CVE-2026-18688 | 7.1 | 2026-08-11 | An issue in MongoDB Server's aggregation framework could allow an authenticated user to trigger an out-of-bounds memory  |
| CVE-2026-18690 | 8.1 | 2026-08-11 | An issue in MongoDB Server could allow an authenticated user with a limited database-scoped role to perform an action ag |
| CVE-2026-18691 | 8.8 | 2026-08-11 | An issue in MongoDB Server's intra-cluster connection setup could allow a party with suitable network access to influenc |
| CVE-2026-18692 | 8.8 | 2026-08-11 | An issue in MongoDB Server's handling of timeseries bucket lifecycle could allow an authenticated user with write privil |
| CVE-2026-18693 | 7.6 | 2026-08-11 | An issue in MongoDB Server's handling of timeseries collections could allow an authenticated user with write privileges  |
| CVE-2026-18694 | 7.1 | 2026-08-11 | An issue in MongoDB Server's geospatial query processing could allow an authenticated user with write privileges to caus |
| CVE-2026-18697 | 7.5 | 2026-08-11 | An issue in MongoDB Server's aggregation framework could allow an unauthenticated party to cause a mongos (router) proce |
| CVE-2026-18711 | 7.1 | 2026-08-11 | An issue in MongoDB Server's query execution engine could allow an authenticated user with read and write privileges to  |
| CVE-2026-18712 | 8.1 | 2026-08-11 | An issue in MongoDB Server's Queryable Encryption maintenance operations could allow an authenticated user with privileg |
| CVE-2026-48802 | 7.5 | 2026-08-11 | python-engineio is a Python implementation of the Engine.IO realtime client and server. Prior to version 4.13.2, an atta |
| CVE-2026-48809 | 7.5 | 2026-08-11 | python-engineio is a Python implementation of the Engine.IO realtime client and server. Versions prior to 4.13.2 have tw |
| CVE-2026-69119 | 8.3 | 2026-08-11 | Taubyte Tau v1.1.10 contains a missing authorization vulnerability in the services/auth HTTP service that allows any aut |
| CVE-2026-72742 | 8.6 | 2026-08-11 | DSPy 3.3.0b1 contains a file exfiltration vulnerability in the Image and Audio output field adapters that allows attacke |
| CVE-2026-73222 | 8.8 | 2026-08-11 | Claude Code Templates is a CLI tool for configuring and monitoring Claude Code. Prior to 1.29.4, the Claude Code Studio  |
| CVE-2026-73223 | 8.1 | 2026-08-11 | electerm is an open-sourced terminal/ssh/sftp/telnet/serialport/RDP/VNC/Spice/ftp client. Prior to 3.15.120, electerm al |
| CVE-2026-73224 | 8.8 | 2026-08-11 | electerm is an open-sourced terminal/ssh/sftp/telnet/serialport/RDP/VNC/Spice/ftp client. Prior to 3.15.120, electerm al |
| CVE-2026-73225 | 8.1 | 2026-08-11 | electerm is an open-sourced terminal/ssh/sftp/telnet/serialport/RDP/VNC/Spice/ftp client. Prior to 3.15.120, electerm al |
| CVE-2026-73226 | 8.8 | 2026-08-11 | electerm is an open-sourced terminal/ssh/sftp/telnet/serialport/RDP/VNC/Spice/ftp client. Prior to 3.15.186, electerm al |
| CVE-2026-73227 | 8.1 | 2026-08-11 | electerm is an open-sourced terminal/ssh/sftp/telnet/serialport/RDP/VNC/Spice/ftp client. Prior to 3.15.120, electerm al |
| CVE-2026-13457 | 7.5 | 2026-08-11 | The InstaWP Connect – 1-click WP Staging & Migration plugin for WordPress is vulnerable to Remote Code Execution in all  |
| CVE-2026-16230 | 9.8 | 2026-08-11 | The Formidable Digital Signatures plugin for WordPress is vulnerable to file deletion due to insufficient file path vali |
| CVE-2026-18844 | 8.1 | 2026-08-11 | The firmware of the Pulsetto Vagus Nerve Stimulator accepts several undisclosed commands over its Bluetooth Low Energy ( |
| CVE-2026-19091 | 8.1 | 2026-08-11 | The GeoDirectory – WP Business Directory Plugin and Classified Listings Directory plugin for WordPress is vulnerable to  |
| CVE-2026-45618 | 10.0 | 2026-08-11 | LiquidJS is a Shopify/GitHub Pages compatible template engine. Prior to version 10.26.0, it is possible to execute arbit |
| CVE-2026-48804 | 7.5 | 2026-08-11 | python-socketio is a Python implementation of the Socket.IO realtime client and server. The python-socketio server store |
| CVE-2026-66145 | 9.1 | 2026-08-11 | An unauthenticated remote code execution vulnerability was identified in GMS 9.5.1 (Build 9510.1044) and earlier version |
| CVE-2026-71467 | 7.5 | 2026-08-11 | A flaw was found in search-v2-api. The authentication middleware in the affected component unconditionally skips authent |
| CVE-2026-73031 | 8.7 | 2026-08-11 | telegram-search contains a stored cross-site scripting vulnerability that allows remote attackers to execute arbitrary J |
| CVE-2026-73032 | 9.6 | 2026-08-11 | PapersGPT for Zotero 0.6.1 contains a remote code execution vulnerability that allows attackers to execute arbitrary Jav |
| CVE-2026-73034 | 9.8 | 2026-08-11 | DB-GPT v0.8.1 contains an unauthenticated path traversal vulnerability that allows remote attackers to write arbitrary f |
| CVE-2026-73231 | 7.8 | 2026-08-11 | Faker generates massive amounts of fake data in the browser and Node.js. Prior to 10.5.0, the faker.helpers.fake method  |
| CVE-2026-73232 | 7.5 | 2026-08-11 | ffuf is a fast web fuzzer written in Go. Prior to 2.2.0, ffuf allows a malicious target server to cause an out-of-memory |
| CVE-2026-73234 | 7.8 | 2026-08-11 | FreeCAD is a free and open-source multiplatform 3D parametric modeler. Prior to 1.1.2, PropertyFileIncluded::Restore() i |
| CVE-2026-14863 | 8.8 | 2026-08-11 | FileRun up to and including version 2026.2.0 contains an OS command injection vulnerability that allows authenticated at |
| CVE-2026-15606 | 8.8 | 2026-08-11 | The Frontend Admin by DynamiApps plugin for WordPress is vulnerable to authorization bypass in all versions up to, and i |
| CVE-2026-48763 | 8.2 | 2026-08-11 | TypeBot is a chatbot builder tool. Versions prior to 3.17.0 expose a deprecated public upload endpoint at `GET /api/v1/t |
| CVE-2026-48765 | 9.9 | 2026-08-11 | TypeBot is a chatbot builder tool. Versions prior to 3.17.0 allow a low-privilege read collaborator to extract a workspa |
| CVE-2026-55676 | 8.8 | 2026-08-11 | Malcolm is a network traffic analysis tool suite. The file-upload component (FilePond PHP backend) accepts uploads at `P |
| CVE-2026-63177 | 7.1 | 2026-08-11 | Malcolm is a network traffic analysis tool suite. Prior to version 26.07.0, role-based access control enforced in the Ng |
| CVE-2026-66147 | 9.4 | 2026-08-11 | An unauthenticated command injection vulnerability was identified in the GMS Dispatcher Service in GMS 9.5.1 and earlier |
| CVE-2026-66149 | 7.8 | 2026-08-11 | Improper Control of Generation of Code ('Code Injection') Vulnerability in the SonicWall Email Security appliance allows |
| CVE-2026-66150 | 7.8 | 2026-08-11 | Improper Control of Generation of Code ('Code Injection') Vulnerability in the SonicWall Email Security appliance allows |
| CVE-2026-66154 | 8.3 | 2026-08-11 | An insufficient certificate validation in a privileged communication workflow, was identified in a GMS application 9.5.1 |
| CVE-2026-29036 | 7.5 | 2026-08-11 | cJSON versions 1.5.0 through 1.7.19 contain an incorrectly-resolved name or reference vulnerability in the decode_pointe |
| CVE-2026-5917 | 9.6 | 2026-08-11 | libgit2 versions v0.27.0 through v1.9.0 built with the libssh2 SSH backend (USE_SSH=libssh2) contain a shell command inj |
| CVE-2026-66875 | 8.8 | 2026-08-11 | In the Mira hormone monitor device firmware v1.7.1.47 build 01070147, a remote unauthenticated attacker within BLE range |
| CVE-2026-67558 | 7.4 | 2026-08-11 | The Mira Android companion app v4.5.15.4 identifies the paired Mira hormone analyzer by performing a substring match aga |
| CVE-2026-67568 | 9.1 | 2026-08-11 | The distributed Mira Android APK v4.5.15.4 allows an attacker read/write access to reproductive health profiles from int |
| CVE-2026-68067 | 9.8 | 2026-08-11 | The login endpoint on the Mira cloud API accepts any format-valid string in the password field and returns a live active |
| CVE-2026-73246 | 7.5 | 2026-08-11 | Kestra is an open-source, event-driven orchestration platform. Prior to 2.0.0-rc6, Kestra's worker/src/main/java/io/kest |
| CVE-2026-73247 | 8.6 | 2026-08-11 | Kestra is an open-source, event-driven orchestration platform. Prior to 2.0.0, Kestra's core/src/main/java/io/kestra/cor |
| CVE-2026-73249 | 7.5 | 2026-08-11 | calibre is an e-book manager. Prior to 9.12.0, the calibre Content Server endpoint POST /book-update-annotations/{librar |
| CVE-2026-6484 | 8.2 | 2026-08-12 | In an UEFI, Lack of verified boot to certain FV may cause arbitrary code execution. |
| CVE-2026-66878 | 7.7 | 2026-08-12 | A flaw was found in multicloud-operators-subscription. A privileged user, specifically a namespace administrator capable |
| CVE-2026-70398 | 9.6 | 2026-08-12 | A flaw was found in multicloud-integrations, a component of Red Hat Advanced Cluster Management (RHACM). This vulnerabil |
| CVE-2026-72526 | 9.9 | 2026-08-12 | A flaw was found in the multicloud-integrations component. The Application propagation controller processes the `ocm-man |
| CVE-2026-73122 | 7.7 | 2026-08-12 | A flaw was found in the multicloud-operators-channel component of Red Hat Advanced Cluster Management (RHACM). This vuln |
| CVE-2026-18961 | 8.1 | 2026-08-12 | The Social Login, Passkeys, Magic Link & Email OTP – Passwordless Login by VentraConnect plugin for WordPress is vulnera |
| CVE-2026-12234 | 7.8 | 2026-08-12 | The userspace syscall verifiers z_vrfy_zsock_sendmsg() and z_vrfy_zsock_recvmsg() in subsys/net/lib/sockets/sockets.c sn |
| CVE-2026-64954 | 8.2 | 2026-08-12 | Velociraptor allows scheduling new collections via VQL queries in notebooks. For a user to schedule a new collection, th |
| CVE-2026-19594 | 8.1 | 2026-08-12 | Insufficient input sanitization in Snowflake Python API (`snowflake.core`) versions prior to 1.13.0 allowed confused-dep |
| CVE-2026-66659 | 9.3 | 2026-08-12 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Essekia Tablesome  |
| CVE-2025-41769 | 9.8 | 2026-08-12 | The device's PROFINET service is affected by a buffer overflow vulnerability that exists in the default configuration. A |
| CVE-2025-41770 | 7.5 | 2026-08-12 | An unauthenticated denial-of-service vulnerability in the device's PLCnext Engineer communication interface allow an rem |
| CVE-2026-19426 | 8.2 | 2026-08-12 | POS System developed by FitSoft has a Missing Authentication vulnerability. Unauthenticated remote attackers can directl |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-20349 | Cisco / Secure Firewall Adaptive Security Appliance (ASA) and Secure Firewall Threat Defense (FTD)  | 2026-08-11 | 2026-08-14 | Unknown |
| CVE-2026-68820 | Microsoft / Windows Ancillary Function Driver for WinSock  | 2026-08-11 | 2026-08-25 | Unknown |
| CVE-2026-72898 | Metabase / Metabase | 2026-08-11 | 2026-08-14 | Unknown |
| CVE-2026-8037 | Progress / LoadMaster | 2026-08-07 | 2026-08-10 | Unknown |
| CVE-2026-63077 | JetBrains / TeamCity | 2026-08-05 | 2026-08-08 | Unknown |

---

*Total entries in CISA KEV catalog: 1665*