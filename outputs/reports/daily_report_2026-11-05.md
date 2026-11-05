# Vulnerability Intelligence Report

**Date:** 2026-11-05  
**Generated:** 2026-11-05T16:09:52Z  

---

## Executive Summary

Our environment faces significant risk from 126 high-severity vulnerabilities, primarily affecting FreeRDP versions prior to 3.32.2. Critical flaws include remote code execution via out-of-bounds writes, use-after-free conditions, and heap buffer overflows exploitable by malicious RDP servers. Additionally, six new entries were added to the CISA Known Exploited Vulnerabilities catalog this week, targeting Apple, WordPress, Ivanti Connect Secure, and GitLab products. While none of our monitored CVEs currently appear in the KEV catalog, the volume and severity of open vulnerabilities represent substantial operational and reputational risk requiring immediate attention.

---

## Risk Narrative

The threat landscape is dominated by multiple critical FreeRDP vulnerabilities enabling remote code execution, memory corruption, and denial of service against both client and server endpoints. Attackers controlling malicious RDP servers can exploit these flaws to compromise client systems at scale. Concurrently, the addition of six CVEs to CISA's KEV catalog confirms active exploitation of vulnerabilities in widely deployed platforms including Ivanti, Apple, WordPress, and GitLab. These products represent common enterprise attack surfaces, and their presence in the KEV catalog indicates real-world threat actor activity. Combined, these factors elevate organizational risk of data breach, ransomware deployment, and service disruption. Prioritizing rapid patching and compensating controls is essential to reducing exposure.

---

## Prioritized Action Items

1. Patch all FreeRDP installations to version 3.32.2 or later immediately to remediate CVSS 9.8 remote code execution and use-after-free vulnerabilities.
2. Audit and patch Ivanti Connect Secure deployments to address two newly KEV-listed vulnerabilities added within the last seven days.
3. Update all WordPress Core installations and Apple products to vendor-recommended versions to close actively exploited KEV-listed vulnerabilities.
4. Patch GitLab Community and Enterprise Edition instances to eliminate the actively exploited vulnerability added to the KEV catalog on October 29.
5. Implement network segmentation and enhanced monitoring around RDP infrastructure to detect exploitation attempts while patching is completed.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-121951 | 7.5 | 2026-11-04 | FreeRDP 3.0.0 before 3.32.2 server-side RDP peer input parsing skips the six-byte body of a slow-path input event with a |
| CVE-2026-121952 | 9.8 | 2026-11-04 | FreeRDP before 3.32.2 has an out-of-bounds write in the proxy because rdp_read_bitmap_cache_v2_capability_set rejects on |
| CVE-2026-121953 | 9.8 | 2026-11-04 | FreeRDP before 3.32.2 has a use-after-free in the client's rdpgfx dynamic virtual channel: a duplicate-name channel with |
| CVE-2026-121955 | 7.5 | 2026-11-04 | FreeRDP before 3.32.2 contains a use-after-free vulnerability in Emulate_SCardReleaseContext that frees the emulated SCa |
| CVE-2026-121956 | 7.5 | 2026-11-04 | FreeRDP before 3.32.2 contains a double free in the WinPR Kerberos SSPI retrieveSomeTgt function, which installs the krb |
| CVE-2026-121957 | 7.5 | 2026-11-04 | FreeRDP before 3.32.2 contains a use-after-free vulnerability that allows malicious RDP servers to corrupt client memory |
| CVE-2026-121958 | 8.8 | 2026-11-04 | FreeRDP through 3.32.1 has a heap out-of-bounds write in the RDPGFX client because the delete_surface callback truncates |
| CVE-2026-121960 | 7.5 | 2026-11-04 | FreeRDP before 3.32.2 contains a denial of service vulnerability in the NLA-enabled shadow server when a CredSSP TSReque |
| CVE-2026-121962 | 8.1 | 2026-11-04 | FreeRDP before 3.32.2 contains a heap buffer overflow in transport_default_read_pdu when handling partial Early User Aut |
| CVE-2026-121964 | 7.5 | 2026-11-04 | FreeRDP before 3.32.2 contains a heap-based buffer overflow in the RD Gateway RPC client, where rpc_client_recv_fragment |
| CVE-2026-121966 | 8.7 | 2026-11-04 | Traefik 2.x before 2.11.60 and 3.x before 3.7.16 sends ForwardAuth subrequests (and, in 3.7, Ingress NGINX auth-url requ |
| CVE-2026-92704 | 8.3 | 2026-11-04 | SharpEmu is an experimental PlayStation 5 emulator for Windows and Linux. In version 0.0.3-release.3 and earlier, the re |
| CVE-2026-119747 | 7.1 | 2026-11-04 | The GetPaid plugin for WordPress before 2.8.63 contains an incorrect authorization vulnerability where the check_post_pe |
| CVE-2026-119749 | 7.5 | 2026-11-04 | The GetPaid plugin for WordPress before 2.8.63 contains an improper input validation vulnerability that allows unauthent |
| CVE-2026-121926 | 7.3 | 2026-11-04 | A vulnerability was detected in yezhihao jt808-server up to a07f68c466b560b97ef41edb8a4966469abdf83e. Affected is the fu |
| CVE-2026-76506 | 7.6 | 2026-11-04 | A vulnerability in the web-based management interface of Cisco UCS Central Software could allow an authenticated, remote |
| CVE-2026-122118 | 7.4 | 2026-11-04 | In certain Yealink products before 2026-04-15, when the Wi-Fi AP function is enabled, a default 8-digit numeric PSK with |
| CVE-2026-57853 | 8.8 | 2026-11-04 | DataGerry before 3.3.0 contains a server-side template injection vulnerability that allows authenticated attackers with  |
| CVE-2026-113780 | 9.3 | 2026-11-04 | ESF-IDF is the Espressif Internet of Things (IOT) Development Framework. From 5.5.5 until 5.5.6, 6.0.4, and 6.1.1, the e |
| CVE-2026-113782 | 7.1 | 2026-11-04 | ESP-IDF is the Espressif Internet of Things (IOT) Development Framework. From 5.2.0 until 5.2.8, 5.3.6, 5.4.5, 5.5.5, an |
| CVE-2026-113783 | 7.4 | 2026-11-04 | ESP-IDF is the Espressif Internet of Things (IOT) Development Framework. From 5.2.3 until 5.3.7, 5.4.5, 5.5.6, and 6.0.3 |
| CVE-2026-121930 | 9.1 | 2026-11-04 | A weakness has been identified in Linksys WRT54GL 4.30.18. The affected element is the function system of the file apply |
| CVE-2026-121931 | 9.1 | 2026-11-04 | A security vulnerability has been detected in Linksys WRT54GL 4.30.18. The impacted element is the function system of th |
| CVE-2026-121932 | 10.0 | 2026-11-04 | A vulnerability was detected in Linksys E5350 1.0.00.037. This affects the function system of the file /wizard/apply.cgi |
| CVE-2026-122120 | 9.0 | 2026-11-04 | In Yealink Plug-in Softwares before 2.35.219.0, there is an unauthorized file write vulnerability under specific scenari |
| CVE-2026-82033 | 8.4 | 2026-11-04 | DeepSeek Harness prior to 0.1.2-alpha.2, and specifically commit 3e24087, contains a missing authentication vulnerabilit |
| CVE-2026-121933 | 10.0 | 2026-11-04 | A flaw has been found in Linksys E5350 1.0.00.037. This impacts the function save_settings of the file /wizard/apply.cgi |
| CVE-2026-122192 | 7.5 | 2026-11-04 | Improper handling of a failed memory remap in Firecracker versions 0.23.0 through 1.16.1 might allow a guest user with r |
| CVE-2026-122220 | 7.4 | 2026-11-04 | WPO365 \| LOGIN (wpo365-login) plugin before version 45.2 contains an authentication bypass by capture-replay vulnerabili |
| CVE-2026-97705 | 7.5 | 2026-11-04 | Moleculer is a progressive microservices framework for Node.js. Prior to 0.14.36 and 0.15.2, Parser._write in src/transp |
| CVE-2025-71456 | 8.1 | 2026-11-04 | vtenext before 25.02.2 contains an SQL injection vulnerability that allows authenticated low-privileged users to inject  |
| CVE-2025-71457 | 9.8 | 2026-11-04 | vtenext 25.02 before 25.02.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to ch |
| CVE-2026-102339 | 8.2 | 2026-11-04 | Telepresence enables local development against a remote Kubernetes or OpenShift cluster. Prior to 2.31.0, the Traffic Ma |
| CVE-2026-102340 | 8.5 | 2026-11-04 | Telepresence enables local development against a remote Kubernetes or OpenShift cluster. Prior to 2.31.0, the Traffic Ma |
| CVE-2026-102664 | 7.1 | 2026-11-04 | ProxySQL is a proxy for MySQL and its forks, as well as PostgreSQL. Prior to 3.0.10, 3.1.10, and 4.0.10, decompress_mysq |
| CVE-2026-104203 | 7.5 | 2026-11-04 | Traccar is an open source GPS tracking system. From 5.1 until 6.15.0, WebModule.java's MediaFilter Guice mapping and Web |
| CVE-2026-10859 | 7.5 | 2026-11-04 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.1 |
| CVE-2026-11376 | 8.8 | 2026-11-04 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.1 |
| CVE-2026-11724 | 8.5 | 2026-11-04 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.1 |
| CVE-2026-122009 | 7.3 | 2026-11-04 | A flaw has been found in DataLinkDC Dinky up to 1.2.5. This vulnerability affects the function FlinkWebURITemplateProxyS |
| CVE-2026-122013 | 10.0 | 2026-11-04 | A vulnerability was detected in Comfast CF-WR632AX 2.6.0.1. Affected by this vulnerability is an unknown functionality o |
| CVE-2026-122127 | 7.5 | 2026-11-04 | CESNET ipfixcol2 2.7.1 before 2.9.0 contains a heap-based buffer overflow in Lz4Decoder.cpp that allows unauthenticated  |
| CVE-2026-122130 | 8.2 | 2026-11-04 | CESNET ipfixcol2 2.3.0 before 2.9.0 contains an integer overflow vulnerability in the Forwarder output plugin that allow |
| CVE-2026-122133 | 8.8 | 2026-11-04 | Mistral Vibe before 2.25.5 on Windows contains an untrusted search path vulnerability that allows attackers to execute c |
| CVE-2026-122134 | 8.8 | 2026-11-04 | Mistral Vibe before 2.25.7 contains a remote code execution vulnerability that allows attackers to run commands by confi |
| CVE-2026-122135 | 8.8 | 2026-11-04 | Mistral Vibe before 3.0.3 contains a remote code execution vulnerability that allows attackers to run commands by abusin |
| CVE-2026-122224 | 8.1 | 2026-11-04 | WebVirtCloud through commit bb920b0 contains a missing authorization vulnerability that allows low-privileged authentica |
| CVE-2026-12356 | 7.5 | 2026-11-04 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.1 |
| CVE-2026-13271 | 8.1 | 2026-11-04 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.1 |
| CVE-2026-13284 | 7.1 | 2026-11-04 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.1 |
| CVE-2026-13289 | 7.1 | 2026-11-04 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.1 |
| CVE-2026-13292 | 8.8 | 2026-11-04 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.1 |
| CVE-2026-17493 | 7.5 | 2026-11-04 | IBM Watson Speech Services Cartridge 4.0.0 through 5.4.0 could allow a remote attacker to cause a denial of service due  |
| CVE-2026-18142 | 7.1 | 2026-11-04 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.1 |
| CVE-2026-82418 | 9.8 | 2026-11-04 | IBM Watson Speech Services Cartridge 4.0.0 through 5.4.0 could allow a remote attacker to execute arbitrary code due to  |
| CVE-2026-102894 | 9.1 | 2026-11-04 | GPUStack is an open-source GPU cluster manager for AI model serving and GPU instance provisioning. From 0.7.1 until 2.2. |
| CVE-2026-102895 | 9.8 | 2026-11-04 | GPUStack is an open-source GPU cluster manager for AI model serving and GPU instance provisioning. Prior to 2.2.0, get_c |
| CVE-2026-103002 | 8.8 | 2026-11-04 | GPUStack is an open-source GPU cluster manager for AI model serving and GPU instance provisioning. From 2.2.0 until 2.2. |
| CVE-2026-122019 | 7.3 | 2026-11-04 | A vulnerability was identified in 6amTech 6valley 16.0. Impacted is the function existingAccountCheck of the file /api/v |
| CVE-2026-122266 | 8.7 | 2026-11-04 | Improper isolation of shared resources in aws-network-policy-agent in Amazon EKS Network Policy Agent before 1.3.7 (VPC  |
| CVE-2026-54372 | 8.8 | 2026-11-04 | VitaFit Android application (com.vt.vitafit) before 2.8.1.0 contains an insecure TLS/SSL certificate validation vulnerab |
| CVE-2026-54374 | 7.5 | 2026-11-04 | VitaFit Android application (com.vt.vitafit) before 2.8.1.0 contains a hardcoded credentials vulnerability that allows a |
| CVE-2026-54375 | 8.4 | 2026-11-04 | VitaFit Android application (com.vt.vitafit) before 2.8.1.0 contains an insecure session management vulnerability that a |
| CVE-2026-54376 | 8.2 | 2026-11-04 | VitaFit Android application (com.vt.vitafit) before 2.8.1.0 contains an insecure custom URI scheme vulnerability that al |
| CVE-2026-54378 | 9.6 | 2026-11-04 | VitaFit cloud API before 2026-10-30 contained a broken access control vulnerability that allows any authenticated user t |
| CVE-2026-55367 | 7.5 | 2026-11-04 | h2o is an HTTP server with support for HTTP/1.x, HTTP/2 and HTTP/3. Prior to commit 4212ce114506a073505fd389db16ad2ba4e5 |
| CVE-2026-55368 | 8.1 | 2026-11-04 | h2o is an HTTP server with support for HTTP/1.x, HTTP/2 and HTTP/3. Prior to commit 48b7ae12107fd2b118e4641da49599e9aac8 |
| CVE-2026-57566 | 9.3 | 2026-11-04 | Readest is a modern, feature-rich ebook reader designed for seamless cross-platform access and an intuitive reading expe |
| CVE-2026-57567 | 8.6 | 2026-11-04 | Readest is a modern, feature-rich ebook reader designed for seamless cross-platform access and an intuitive reading expe |
| CVE-2026-63655 | 7.5 | 2026-11-04 | tsParticles is a TypeScript library for creating highly customizable particle animations. Prior to 4.3.1, the HTTP mode  |
| CVE-2026-97693 | 9.9 | 2026-11-04 | Yuxi is a large-model-based intelligent knowledge base and knowledge graph agent development platform.  From 0.6.0.beta1 |
| CVE-2026-115770 | 9.6 | 2026-11-04 | Pocket ID is an OIDC provider that allows users to authenticate with their passkeys to services. From 2.2.0 until 2.12.0 |
| CVE-2026-122038 | 7.3 | 2026-11-04 | A vulnerability was identified in krupalshah EmployeeRecruitmentSystem up to 922ff6d208278282e7c8e36d70d9ae356adec9fe. A |
| CVE-2026-122047 | 7.3 | 2026-11-04 | A security vulnerability has been detected in Campcodes Complete Advance Loan Management System 1.0. This affects the fu |
| CVE-2026-122048 | 7.3 | 2026-11-04 | A vulnerability was identified in Campcodes Division Regional Athletic Meet Game Result Matrix System up to 2.1. This af |
| CVE-2026-122299 | 8.8 | 2026-11-04 | Dulwich before 1.2.20 contains a commit object parsing vulnerability where the read path in _parse_commit resolves a dup |
| CVE-2026-54381 | 7.5 | 2026-11-04 | VitaFit cloud API before 2026-10-30 contained a misconfigured cloud storage bucket vulnerability that allows unauthentic |
| CVE-2026-54382 | 7.7 | 2026-11-04 | VitaFit cloud API before 2026-10-30 contained an improper access control vulnerability in its Cognito-issued AWS role th |
| CVE-2026-54384 | 9.8 | 2026-11-04 | VitaFit cloud API before 2026-10-30 contained an authentication bypass vulnerability that allows remote attackers to obt |
| CVE-2026-62662 | 7.7 | 2026-11-04 | Pocket ID is an OIDC provider that allows users to authenticate with their passkeys to services. From 1.11.0 until 2.10. |
| CVE-2026-122050 | 7.3 | 2026-11-05 | A vulnerability was found in Campcodes Complete Sales and Inventory System with Credit Management 1.0. This issue affect |
| CVE-2026-122051 | 10.0 | 2026-11-05 | A flaw has been found in Edimax BR-6208AC 1.32. Affected by this vulnerability is an unknown functionality of the file / |
| CVE-2026-122146 | 7.3 | 2026-11-05 | A weakness has been identified in 101arrowz fflate up to 0.8.3. This issue affects the function unzipSync of the file es |
| CVE-2026-122302 | 9.8 | 2026-11-05 | Kyverno before 1.19.2 contains a privilege escalation vulnerability that allows namespace admins to create resources bey |
| CVE-2026-122303 | 9.9 | 2026-11-05 | Kyverno from 1.17.0 before 1.19.2 contains an authorization bypass vulnerability that allows namespace tenants to overwr |
| CVE-2026-122304 | 9.9 | 2026-11-05 | Kyverno from 1.17.0 before 1.19.2 contains an authorization bypass vulnerability that allows namespace admins to escape  |
| CVE-2026-122305 | 7.7 | 2026-11-05 | Kyverno before 1.19.2 contains a denial of service vulnerability in substituteVariablesIfAny that allows low-privileged  |
| CVE-2026-122306 | 7.7 | 2026-11-05 | Kyverno before 1.19.2 contains a denial of service vulnerability that allows namespaced policy authors to exhaust admiss |
| CVE-2026-122307 | 7.7 | 2026-11-05 | Kyverno before 1.19.2 contains a policy bypass vulnerability in the admissionpolicygenerator controller, which folds Pol |
| CVE-2026-122308 | 8.5 | 2026-11-05 | Kyverno before 1.19.2 contains an authorization bypass vulnerability in the Generation Handler that allows users with cr |
| CVE-2026-122310 | 9.9 | 2026-11-05 | Kyverno from 1.19.1 before 1.19.2 validates a Policy's context.apiCall urlPath after cleaning it but executes the raw pa |
| CVE-2026-122311 | 9.9 | 2026-11-05 | Kyverno from 1.16.0 before 1.19.2 fails to validate path segments in the resource argument of resource.get() and resourc |
| CVE-2026-122312 | 7.7 | 2026-11-05 | Kyverno from 1.19.1 before 1.19.2 contains a namespace isolation bypass in APICall Fetch() in pkg/engine/apicall/apiCall |
| CVE-2026-122313 | 9.9 | 2026-11-05 | Kyverno from 1.17.0 before 1.19.2 contains a privilege escalation vulnerability that allows namespace-scoped tenants to  |
| CVE-2026-122314 | 7.5 | 2026-11-05 | Kyverno before 1.19.2 contains an unchecked type assertion in its variable-substitution engine that allows users who can |
| CVE-2026-122315 | 7.5 | 2026-11-05 | Kyverno before 1.19.2 contains an unchecked type assertion in buildStatementMap that allows unauthenticated attackers to |
| CVE-2026-122316 | 8.5 | 2026-11-05 | Kyverno from 1.17.0 before 1.19.2 contains a missing authorization vulnerability in the mutate-existing background proce |
| CVE-2026-122318 | 7.7 | 2026-11-05 | Kyverno before 1.19.2 contains an authentication bypass in matchCertificateData that skips verifyImages subject and subj |
| CVE-2026-122319 | 7.5 | 2026-11-05 | Kyverno before 1.19.2 contains a denial-of-service vulnerability in the In and NotIn operators that allows attackers to  |
| CVE-2026-122320 | 7.7 | 2026-11-05 | Kyverno before 1.19.2 contains a missing authorization vulnerability that allows namespaced Policy authors to read resou |
| CVE-2026-122321 | 9.1 | 2026-11-05 | Kyverno 1.18.0 before 1.19.2 contains a signature verification bypass in verifyImages because cached verification result |
| CVE-2026-122322 | 7.5 | 2026-11-05 | Kyverno from 1.11.0 before 1.19.2 contains an unbounded decompression vulnerability in extractStatement that allows remo |
| CVE-2026-122323 | 7.5 | 2026-11-05 | Kyverno from 1.11.0 before 1.19.2 contains an unbounded decompression vulnerability in FetchSignatureBlob that allows at |
| CVE-2026-116617 | 8.1 | 2026-11-05 | The Motors – Car Dealership & Classified Listings Plugin plugin for WordPress is vulnerable to File Deletion in all vers |
| CVE-2026-118193 | 8.8 | 2026-11-05 | The GiveWP – Donation Plugin and Fundraising Platform plugin for WordPress is vulnerable to Privilege Escalation in all  |
| CVE-2026-123010 | 7.2 | 2026-11-05 | @twilio-labs/netlify-okta-auth through 1.0.2 relies on an unverified iss claim. This affects an outbound HTTP request to |
| CVE-2026-93389 | 8.2 | 2026-11-05 | The LiteSpeed Cache plugin for WordPress is vulnerable to unauthenticated disclosure of sensitive WooCommerce customer d |
| CVE-2026-123029 | 7.5 | 2026-11-05 | Wowza Streaming Engine before 4.12.2 processes XML external entities, which allows remote attackers to read local files  |
| CVE-2026-123033 | 8.3 | 2026-11-05 | Authentication bypass in the HA heartbeat origin check in middlewared in TrueNAS SCALE before 25.10.8 (and in release tr |
| CVE-2026-100109 | 9.8 | 2026-11-05 | The Security For WooCommerce WordPress plugin from 1.0.10 to 1.0.16 does not perform capability checks when creating use |
| CVE-2026-109408 | 7.4 | 2026-11-05 | vault-java-driver, a Java client for HashiCorp Vault, silently disables TLS certificate and hostname verification in thr |
| CVE-2026-118869 | 8.8 | 2026-11-05 | An OS command injection vulnerability exists in SHIRASAGI, which may allow an authenticated attacker to execute arbitrar |
| CVE-2026-123018 | 8.3 | 2026-11-05 | A security flaw has been discovered in eosphoros-ai DB-GPT up to 0.8.2. This issue affects the function execute_code of  |
| CVE-2026-123019 | 7.3 | 2026-11-05 | A weakness has been identified in eosphoros-ai DB-GPT up to 0.8.2. Impacted is the function exec_module of the file hf_a |
| CVE-2026-123047 | 7.5 | 2026-11-05 | In Eclipse BaSyx Helm Charts versions 3.0.0-rc.1 to 3.12.1 of the `basyx` chart, deployments with the bundled Keycloak e |
| CVE-2026-104720 | 7.5 | 2026-11-05 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Kobikom Telecommunicatio |
| CVE-2026-105321 | 7.5 | 2026-11-05 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Kobikom Telecommun |
| CVE-2026-107912 | 7.7 | 2026-11-05 | A flaw was found in the management interface of the Quarkus framework, specifically within the quarkus-vertx-http compon |
| CVE-2026-117691 | 9.1 | 2026-11-05 | A flaw was found in the SAML HTTP-Redirect binding implementation of Keycloak. The issue occurs because the server proce |
| CVE-2026-123022 | 7.3 | 2026-11-05 | A vulnerability was detected in agentscope-ai AgentScope up to 2.0.11. The impacted element is the function subprocess.P |
| CVE-2026-123023 | 7.3 | 2026-11-05 | A flaw has been found in agentscope-ai AgentScope up to 2.0.8. This affects the function check_permissions of the file s |
| CVE-2026-123024 | 7.3 | 2026-11-05 | A vulnerability has been found in agentscope-ai AgentScope up to 2.0.11. This impacts the function get_current_user_id o |
| CVE-2026-123028 | 7.3 | 2026-11-05 | A vulnerability was identified in itsourcecode Online Book Store 1.0. Affected by this issue is some unknown functionali |
| CVE-2026-123059 | 7.5 | 2026-11-05 | In Eclipse BaSyx Helm Charts version 2.2.0 of the `aas-basyx-v2-full` chart, deployments with the bundled Keycloak enabl |
| CVE-2026-119744 | 8.8 | 2026-11-05 | Cendio ThinLinc contains an improper authentication vulnerability in its browser-based web client (tlwebaccess) that all |
| CVE-2026-123032 | 7.3 | 2026-11-05 | A security flaw has been discovered in OpenBMB Internet of Agents up to 9d78e88e47160eb42ee1ee8538c05e1c2c47877a. This a |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2024-27834 | Apple / Multiple Products | 2026-11-04 | 2026-11-18 | Unknown |
| CVE-2026-119977 | WordPress / WordPress Core | 2026-11-03 | 2026-11-06 | Unknown |
| CVE-2026-118527 | Ivanti / Connect Secure | 2026-10-30 | 2026-11-13 | Unknown |
| CVE-2026-111357 | Ivanti / Connect Secure | 2026-10-30 | 2026-11-02 | Unknown |
| CVE-2026-97229 | GitLab / Community Edition and Enterprise Edition | 2026-10-29 | 2026-11-01 | Unknown |
| CVE-2026-76418 | Cisco / Secure Firewall ASA Software and Cisco Secure FTD Software | 2026-10-29 | 2026-11-01 | Unknown |

---

*Total entries in CISA KEV catalog: 1768*