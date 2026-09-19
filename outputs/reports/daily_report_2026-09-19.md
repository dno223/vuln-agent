# Vulnerability Intelligence Report

**Date:** 2026-09-19  
**Generated:** 2026-09-19T12:17:24Z  

## Pipeline Warnings

- summarizer failed: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}, 'request_id': 'req_011CfCnQeHdjfuvg9fqkz2Vu'}

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
| CVE-2026-28197 | 8.8 | 2026-09-18 | An authenticated, low-privileged user with access to the NetBackup Flex 
OS management shell could supply a specially cr |
| CVE-2026-28198 | 8.8 | 2026-09-18 | An authenticated, low-privileged user with access to the NetBackup Flex 
OS management shell could bypass the cryptograp |
| CVE-2026-93488 | 7.5 | 2026-09-18 | A flaw was found in Netty. SpdySessionHandler accepts an unlimited number of concurrent remote-initiated streams because |
| CVE-2026-93491 | 7.5 | 2026-09-18 | A flaw was found in Netty's HttpServerCodec. A remote, unauthenticated attacker can exploit this vulnerability by pipeli |
| CVE-2023-5778 | 7.5 | 2026-09-18 | Improper handling of length parameter inconsistency vulnerability in ABB Freelance Controller DCP, ABB Freelance Control |
| CVE-2026-88622 | 8.8 | 2026-09-18 | NUUO Network Video Recorder 2.0.0 is vulnerable to Command Injection in handle_import_privilege.php. |
| CVE-2026-93019 | 9.1 | 2026-09-18 | Imager versions before 1.036 for Perl exit the process reading a TGA with a colour map length of 32768 or more in tga_pa |
| CVE-2026-93560 | 7.5 | 2026-09-18 | A flaw was found in the Netty STOMP codec. A remote attacker could send a specially crafted STOMP frame with a content-l |
| CVE-2026-93591 | 7.6 | 2026-09-18 | SiYuan versions before 3.8.3 contain an SQL injection vulnerability in the graph.go query2Stmt function where tag values |
| CVE-2026-93592 | 7.5 | 2026-09-18 | vLLM versions before 0.28.0 fail to validate the lower bound of token IDs in the /v1/embeddings and /pooling endpoints,  |
| CVE-2026-93593 | 8.1 | 2026-09-18 | ArcadeDB before 26.9.1 fails to enforce security-group types ACL entries for TimeSeries types because the ACL resolver b |
| CVE-2026-93594 | 8.1 | 2026-09-18 | ArcadeDB (Maven artifact com.arcadedb:arcadedb-engine) through 26.8.1 enforces its per-type/per-record access-control ru |
| CVE-2026-93597 | 7.7 | 2026-09-18 | ArcadeDB versions before 26.9.1 fail to validate IPv6 transition addresses in the SSRF guard used by IMPORT DATABASE and |
| CVE-2026-93599 | 7.5 | 2026-09-18 | rustls-webpki through 0.103.12 (and 0.104.0-alpha releases before 0.104.0-alpha.7) contains a reachable panic in bit_str |
| CVE-2026-93603 | 10.0 | 2026-09-18 | vm2 through 3.12.0 (fixed in 3.12.1) does not correctly handle a nullish `this` receiver in the apply trap of its bridge |
| CVE-2026-93604 | 7.2 | 2026-09-18 | vm2 through 3.12.0 exposes Node.js's crypto.setFips() function to untrusted guest code when an embedder explicitly allow |
| CVE-2026-93605 | 10.0 | 2026-09-18 | vm2 NodeVM versions before 3.12.1 contain a sandbox escape vulnerability where the DANGEROUS_BUILTINS denylist omits chi |
| CVE-2026-93606 | 10.0 | 2026-09-18 | vm2 (npm) versions 3.12.0 and earlier contain a sandbox escape in `VM` and `NodeVM`. When an embedder exposes a host API |
| CVE-2026-77929 | 8.8 | 2026-09-18 | ClipBucket v5 before 5.5.3-#182 contains a file upload vulnerability that allows authenticated users to achieve remote c |
| CVE-2026-93558 | 7.5 | 2026-09-18 | A flaw was found in Netty's WebSocketServerExtensionHandler. A remote, unauthenticated attacker can exploit this vulnera |
| CVE-2026-93564 | 7.5 | 2026-09-18 | A flaw was found in Netty. A reference-count leak in the HAProxy PROXY-v2 message decoder allows a remote, unauthenticat |
| CVE-2026-93565 | 7.5 | 2026-09-18 | A flaw was found in Netty RtspDecoder. The `RtspMethods.valueOf()` function incorrectly strips trailing control bytes fr |
| CVE-2026-93567 | 7.5 | 2026-09-18 | A flaw was found in Netty's HTTP/2 codec. When converting HTTP/1 CONNECT requests to HTTP/2, the component incorrectly u |
| CVE-2026-93568 | 7.5 | 2026-09-18 | A flaw was found in Netty. A remote attacker could exploit this vulnerability by sending specially crafted HTTP/2 or HTT |
| CVE-2026-93569 | 8.2 | 2026-09-18 | A flaw was found in Netty. A remote unauthenticated attacker can exploit a vulnerability in Netty's HTTP/1 to HTTP/2 con |
| CVE-2026-93576 | 7.5 | 2026-09-18 | A flaw was found in Netty netty-codec-smtp. The component does not properly validate Carriage Return (CR) and Line Feed  |
| CVE-2026-93652 | 7.5 | 2026-09-18 | Integer overflow in µD3TN v0.15.0 TCPCLv3 handshake causes heap overflow, allowing remote attackers to reliably cause Do |
| CVE-2026-93657 | 7.5 | 2026-09-18 | hickory-resolver versions before 0.26.2 fail to propagate bogus DNSSEC proof states through the Resolver::lookup() and R |
| CVE-2026-93658 | 7.0 | 2026-09-18 | uutils coreutils versions before 0.10.0 apply setuid or setgid mode to install destinations before finalizing ownership  |
| CVE-2026-93659 | 8.7 | 2026-09-18 | Concrete CMS Community Store before 2.7.8 renders customer-supplied order fields without HTML escaping in checkout and a |
| CVE-2025-14753 | 7.5 | 2026-09-18 | IBM Cloud Pak for Data 5.1.2 could allow a remote attacker to traverse directories on the system. An attacker could send |
| CVE-2025-14754 | 8.8 | 2026-09-18 | IBM Cloud Pak for Data 5.1.2 could allow an authenticated user to execute arbitrary commands with elevated privileges on |
| CVE-2025-15399 | 10.0 | 2026-09-18 | IBM Common Licensing Agent 9.0, Agent 9.0.0.1, Agent 9.0.0.2, ART 9.0, ART 9.0.0.1, and ART 9.0.0.2 is vulnerable to cro |
| CVE-2025-53837 | 9.9 | 2026-09-18 | XWiki Rendering is a generic rendering system that converts textual input in a given syntax (wiki syntax, HTML, etc) int |
| CVE-2025-61682 | 8.6 | 2026-09-18 | Semantic MediaWiki is a free, open-source extension to MediaWiki that lets users store and query data within the wiki's  |
| CVE-2026-10027 | 8.1 | 2026-09-18 | IBM MQ could allow a remote attacker to cause a denial of service or execute arbitrary code due to a buffer overflow whe |
| CVE-2026-10030 | 7.1 | 2026-09-18 | IBM MQ Console allows authenticated non-administrative users to create and start queue managers due to improper authoriz |
| CVE-2026-10575 | 8.8 | 2026-09-18 | IBM MQ could allow an authenticated attacker to cause a denial of service or potentially escalate privileges due to a he |
| CVE-2026-10744 | 7.5 | 2026-09-18 | IBM MQ for HPE NonStop 8.1.0 through 8.1.0.40 could allow an authenticated attacker to cause a denial of service or pote |
| CVE-2026-10747 | 10.0 | 2026-09-18 | IBM MQ Appliance could allow a remote attacker to cause a denial of service or potentially execute arbitrary code due to |
| CVE-2026-10751 | 7.5 | 2026-09-18 | IBM MQ Java and JMS client libraries could allow an authenticated attacker to execute arbitrary code on client applicati |
| CVE-2026-10853 | 7.5 | 2026-09-18 | IBM MQ could allow an authenticated attacker with cluster access to cause a denial of service or potentially execute arb |
| CVE-2026-10858 | 9.9 | 2026-09-18 | IBM MQ for HPE NonStop 8.1.0 through 8.1.0.40 could allow an authenticated attacker to cause a denial of service or pote |
| CVE-2026-11375 | 8.8 | 2026-09-18 | IBM MQ could allow an authenticated attacker to cause a denial of service or potentially execute arbitrary code due to a |
| CVE-2026-11378 | 8.8 | 2026-09-18 | IBM MQ could allow an authenticated attacker to cause a denial of service or potentially execute arbitrary code due to a |
| CVE-2026-11381 | 8.8 | 2026-09-18 | IBM MQ could allow an authenticated attacker to cause a denial of service or potentially execute arbitrary code due to i |
| CVE-2026-54148 | 8.1 | 2026-09-18 | http4k is a functional toolkit for Kotlin HTTP applications. Prior to 4.51.0.0, 5.42.0.0, and 6.50.0.0, DigestAuthProvid |
| CVE-2026-61682 | 9.9 | 2026-09-18 | kcp is a Kubernetes-like control plane for form-factors and use-cases beyond Kubernetes and container workloads. Prior t |
| CVE-2026-63419 | 7.8 | 2026-09-18 | OpenImageIO is a toolset for reading, writing, and manipulating image files of any image file format relevant to VFX / a |
| CVE-2026-63422 | 7.8 | 2026-09-18 | OpenImageIO is a toolset for reading, writing, and manipulating image files of any image file format relevant to VFX / a |
| CVE-2026-63638 | 8.3 | 2026-09-18 | OpenImageIO is a toolset for reading, writing, and manipulating image files of any image file format relevant to VFX / a |
| CVE-2026-67549 | 7.6 | 2026-09-18 | OpenImageIO is a toolset for reading, writing, and manipulating image files of any image file format relevant to VFX / a |
| CVE-2026-75031 | 9.8 | 2026-09-18 | In the interchange/interchange project, a critical remote code execution (RCE) vulnerability was found in the 
“quick qu |
| CVE-2026-7006 | 7.3 | 2026-09-18 | Sublime Text for Windows through Build 4192 (Sublime Text 4) and Build 3207 (Sublime Text 3) contains a local privilege  |
| CVE-2026-81942 | 8.8 | 2026-09-18 | PLANET IGS-5225-8P2T4S industrial managed switch V1 and V2 firmware versions before 1.2412b260707 and 2.2412b260519 cont |
| CVE-2026-81944 | 7.5 | 2026-09-18 | PLANET IGS-5225-8P2T4S industrial managed switch V1 and V2 firmware versions before 1.2412b260707 and 2.2412b260519 cont |
| CVE-2026-84383 | 9.8 | 2026-09-18 | libheif is a HEIF and AVIF file format decoder and encoder. From 1.22.0 until 1.23.2, a crafted HEIF, HEIC, or AVIF item |
| CVE-2026-84384 | 7.5 | 2026-09-18 | libheif is a HEIF and AVIF file format decoder and encoder. From 1.19.0 until 1.23.2, crafted HEIF or AVIF mime metadata |
| CVE-2026-84398 | 7.5 | 2026-09-18 | CM2507 IP cameras accept an empty password for a privileged account exposed through its ONVIF management service. An att |
| CVE-2026-84444 | 7.4 | 2026-09-18 | libheif is a HEIF and AVIF file format decoder and encoder. Prior to 1.23.2, when WITH_UNCOMPRESSED_CODEC is enabled, he |
| CVE-2026-84446 | 7.5 | 2026-09-18 | libheif is a HEIF and AVIF file format decoder and encoder. Prior to 1.23.2, crafted HEIF sequence timing and edit-list  |
| CVE-2026-84447 | 7.5 | 2026-09-18 | libheif is a HEIF and AVIF file format decoder and encoder. In 1.23.1 and earlier, crafted grid, iovl, and iden referenc |
| CVE-2026-86520 | 7.5 | 2026-09-18 | Bransys ELD is shipped with hardcoded MQTT credentials, which will grant read access to real-time data for every active  |
| CVE-2026-88259 | 7.5 | 2026-09-18 | CareCam CM2507 IP cameras do not require authentication for access to its network video streaming service. An unauthenti |
| CVE-2026-93687 | 7.5 | 2026-09-18 | braces through 3.0.3 contains a stack overflow vulnerability in the recursive AST walkers that lack depth guards. Attack |
| CVE-2026-93688 | 7.5 | 2026-09-18 | SGLang through 0.5.19 in prefill/decode disaggregation mode with Mooncake KV transfer backend fails to validate bootstra |
| CVE-2026-93690 | 7.5 | 2026-09-18 | uri-js through 4.4.1 contains a denial of service vulnerability in the removeDotSegments function that loops infinitely  |
| CVE-2026-46655 | 7.8 | 2026-09-18 | virtio-win provides Windows paravirtualized drivers for QEMU and KVM. From mm210 until mm320, the Viosock driver permits |
| CVE-2026-58197 | 8.8 | 2026-09-18 | ToolHive is a utility designed to simplify the deployment and management of Model Context Protocol servers. Prior to Too |
| CVE-2026-61548 | 8.1 | 2026-09-18 | Rsyslog is a rocket-fast system for log processing. From 7.5.4 until 8.2606.0, the optional mmpstrucdata plugin's parseS |
| CVE-2026-61672 | 7.1 | 2026-09-18 | Capsule is a multi-tenancy and policy-based framework for Kubernetes. Prior to 0.13.7, ForbiddenListSpec.ExactMatch in p |
| CVE-2026-61833 | 8.1 | 2026-09-18 | zot is a container image and artifact registry based on the Open Container Initiative Distribution Specification. Prior  |
| CVE-2026-77239 | 8.1 | 2026-09-18 | WACRM is a self-hostable CRM template for WhatsApp. In version 0.7.0 and earlier, WACRM flow and automation write routes |
| CVE-2026-77240 | 9.9 | 2026-09-18 | WACRM is a self-hostable CRM template for WhatsApp. In version 0.7.0 and earlier, the profiles_update row-level security |
| CVE-2026-77301 | 7.5 | 2026-09-18 | adm-zip is a JavaScript library for creating and extracting ZIP archives in Node.js. Prior to 0.6.1, getData() in zipEnt |
| CVE-2026-81321 | 9.8 | 2026-09-18 | CM2507 IP cameras store configured wireless network credentials in cleartext within the device filesystem. An attacker w |
| CVE-2026-85497 | 9.8 | 2026-09-18 | CareCam CM2507 IP cameras store the device's root-account password using a fixed legacy password hash that provides insu |
| CVE-2026-91149 | 7.5 | 2026-09-18 | A flaw was found in Cockpit. An unauthenticated remote attacker can exploit this vulnerability by initiating and sustain |
| CVE-2026-93559 | 7.3 | 2026-09-18 | A vulnerability was identified in Forget-C Jellyfish AI Short Drama Studio 0.1.0-alpha/0.2.0/0.3.0/0.3.1/0.3.2. This aff |
| CVE-2026-93758 | 8.1 | 2026-09-18 | An insecure direct object reference in the nested attributes handling of the Mongoid object-document mapper may allow a  |
| CVE-2026-93765 | 9.1 | 2026-09-18 | Mongoid contains an unsafe reflection weakness in the document persistence layer of its object-document mapping code. In |
| CVE-2025-66455 | 9.8 | 2026-09-18 | LMDeploy is a toolkit for compressing, deploying, and serving large language models. Starting in version 0.9.2 and prior |
| CVE-2026-32641 | 7.5 | 2026-09-18 | Parseable is a log analytics platform built for high-volume data ingestion and analysis. Prior to 3.0.0, src/handlers/ht |
| CVE-2026-33625 | 8.8 | 2026-09-18 | LMDeploy is a toolkit for compressing, deploying, and serving large language models. Versions 012.1 through 0.12.2 conta |
| CVE-2026-59163 | 9.1 | 2026-09-18 | Mnemosyne is a memory layer for artificial intelligence agents. Prior to v3.10.1, the auth check in mnemosyne/core/sync_ |
| CVE-2026-61550 | 9.8 | 2026-09-18 | Icinga 2 is an open source monitoring system. From 2.8 until 2.14.9, 2.15.4, and 2.16.2, certificate update JSON-RPC mes |
| CVE-2026-61551 | 8.6 | 2026-09-18 | Icinga 2 is an open source monitoring system. Prior to 2.14.9, 2.15.4, and 2.16.2, parsing deeply nested JSON can exhaus |
| CVE-2026-61552 | 7.2 | 2026-09-18 | Icinga 2 is an open source monitoring system. From 2.4 until 2.14.9, 2.15.4, and 2.16.2, the /v1/objects API writes atta |
| CVE-2026-62278 | 8.1 | 2026-09-18 | LubeLogger is a self-hosted, open-source, web-based vehicle maintenance and fuel mileage tracker. Prior to 1.6.8, authen |
| CVE-2026-62279 | 7.1 | 2026-09-18 | LubeLogger is a self-hosted, open-source, web-based vehicle maintenance and fuel mileage tracker. Prior to 1.6.8, an aut |
| CVE-2026-69184 | 7.5 | 2026-09-18 | c-ares is an asynchronous resolver library. Prior to 1.34.7, ares_dns_name_parse() enforces backward DNS compression poi |
| CVE-2026-81179 | 8.1 | 2026-09-18 | SysReptor is a fully customizable pentest reporting platform. Prior to 2026.58, installations that enable password reset |
| CVE-2026-81180 | 8.8 | 2026-09-18 | SysReptor is a fully customizable pentest reporting platform. Prior to 2026.61, authenticated users of SysReptor Profess |
| CVE-2026-84975 | 7.4 | 2026-09-18 | PJSIP is a free and open source multimedia communication library written in C. In 2.17 and earlier, the OpenSSL and GnuT |
| CVE-2026-85058 | 7.5 | 2026-09-18 | Moquette is a lightweight Java MQTT broker. Prior to 0.18.1, PostOffice.publishWill publishes a client-controlled Last W |
| CVE-2026-91127 | 8.2 | 2026-09-18 | File Viewer is a browser-native viewer for Office, PDF, CAD, archive, and other files in private and internal web applic |
| CVE-2026-92701 | 9.1 | 2026-09-18 | trusted execution environments. In versions up to and including 0.8.2, the intra-handshake attested TLS (aTLS) Intel TDX |
| CVE-2026-92702 | 9.1 | 2026-09-18 | Cocos AI is a confidential computing system for running AI workloads inside trusted execution environments. In versions  |
| CVE-2026-93748 | 7.5 | 2026-09-18 | http-cache-semantics through 4.2.0 fails to properly validate security-zeroed cache entries when processing client max-s |
| CVE-2026-93749 | 7.5 | 2026-09-18 | source-map-js through 1.2.1 fails to validate the per-section offset line value in indexed source maps, allowing attacke |
| CVE-2026-93752 | 7.5 | 2026-09-18 | CSSOM through 0.5.0 contains a denial of service vulnerability in CSSStyleDeclaration.setProperty() that fails to valida |
| CVE-2026-93753 | 7.5 | 2026-09-18 | deepmerge through 4.3.1 contains a prototype poisoning vulnerability in the mergeObject() function that fails to properl |
| CVE-2026-93759 | 8.6 | 2026-09-18 | Mongoid does not neutralize a string-typed query criterion supplied to its query builder, and instead passes it to the d |
| CVE-2026-93760 | 8.2 | 2026-09-18 | Mongoid does not restrict which query operators may come from caller-supplied filter data when an application hands that |
| CVE-2026-93761 | 7.5 | 2026-09-18 | An inefficient regular expression complexity issue in the in-memory query evaluation component of the Mongoid library ma |
| CVE-2026-93762 | 9.8 | 2026-09-18 | Mongoid contains an unsafe reflection weakness in the query path used for embedded documents. An application that passes |
| CVE-2019-25776 | 7.5 | 2026-09-18 | Weaver E-cology contains an unauthenticated SQL injection vulnerability that allows remote attackers to execute arbitrar |
| CVE-2021-48008 | 7.5 | 2026-09-18 | Chanjet CRM contains an unauthenticated SQL injection vulnerability that allows remote attackers to execute arbitrary SQ |
| CVE-2023-54399 | 9.8 | 2026-09-18 | Hongjing e-HR before 8.2 contains a SQL injection vulnerability in the /servlet/codesettree endpoint where the categorie |
| CVE-2017-20284 | 7.5 | 2026-09-18 | Caucho Resin contains a path traversal vulnerability in the documentation webapp (resin-doc) that allows remote unauthen |
| CVE-2026-11716 | 7.5 | 2026-09-18 | IBM MQ for HPE NonStop 8.1.0 through 8.1.0.40 could allow an authenticated attacker to cause a denial of service or pote |
| CVE-2026-11725 | 8.8 | 2026-09-18 | IBM MQ could allow an authenticated attacker to cause a denial of service or potentially execute arbitrary code due to a |
| CVE-2026-11726 | 8.1 | 2026-09-18 | IBM MQ for HPE NonStop 8.1.0 through 8.1.0.40 could allow an authenticated attacker to obtain sensitive information or c |
| CVE-2026-11727 | 8.1 | 2026-09-18 | IBM MQ for HPE NonStop 8.1.0 through 8.1.0.40 IBM MQ C client could allow a remote attacker to cause a denial of service |
| CVE-2026-17619 | 8.6 | 2026-09-18 | IBM Platform RTM is vulnerable to SQL injection. A remote attacker could send specially crafted SQL statements, which co |
| CVE-2026-58264 | 9.8 | 2026-09-18 | FluidSynth is a software synthesizer based on the SoundFont 2 specifications. From 1.1.2 until 2.5.6, the FluidSynth com |
| CVE-2026-61714 | 7.8 | 2026-09-18 | FluidSynth is a software synthesizer based on the SoundFont 2 specifications. From 2.2.4 until 2.5.6, configuring synth. |
| CVE-2026-61721 | 8.0 | 2026-09-18 | FluidSynth is a software synthesizer based on the SoundFont 2 specifications. From 2.5.0 until 2.5.6, the native DLS loa |
| CVE-2026-61781 | 9.9 | 2026-09-18 | pg_partman is a PostgreSQL extension that manages partitioned tables by time or ID. Prior to 5.5.0, create_partition_tim |
| CVE-2026-61817 | 8.5 | 2026-09-18 | pg_partman is a PostgreSQL extension that manages partitioned tables by time or ID. Prior to 5.5.0, run_maintenance(), s |
| CVE-2026-61818 | 8.5 | 2026-09-18 | pg_partman is a PostgreSQL extension that manages partitioned tables by time or ID. Prior to 5.5.0, undo_partition() rea |
| CVE-2026-61819 | 8.5 | 2026-09-18 | pg_partman is a PostgreSQL extension that manages partitioned tables by time or ID. Prior to 5.5.0, when pg_jobmon is in |
| CVE-2026-61820 | 8.5 | 2026-09-18 | pg_partman is a PostgreSQL extension that manages partitioned tables by time or ID. Prior to 5.5.0, inherit_template_pro |
| CVE-2026-61821 | 8.5 | 2026-09-18 | pg_partman is a PostgreSQL extension that manages partitioned tables by time or ID. Prior to 5.5.0, drop_partition_id()  |
| CVE-2026-75878 | 9.1 | 2026-09-18 | IBM Sterling File Gateway could allow a remote attacker to bypass authentication and obtain a fully authenticated sessio |
| CVE-2026-80441 | 9.8 | 2026-09-18 | IBM Guardium Data Protection 12.2 is vulnerable to an unauthenticated second-order SQL injection vulnerability in the ge |
| CVE-2026-80442 | 9.9 | 2026-09-18 | IBM Guardium Data Protection 12.2 is vulnerable to an authenticated OS command injection vulnerability in the exportCert |
| CVE-2026-81626 | 8.6 | 2026-09-18 | IBM Guardium Data Protection 12.2 is vulnerable to a SQL injection vulnerability in the Load Balancer Groups component.  |
| CVE-2026-81656 | 8.8 | 2026-09-18 | IBM Guardium Data Protection 12.2 is vulnerable to a SQL injection vulnerability in the New Query Builder REST Processor |
| CVE-2026-81657 | 9.8 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote unauthenticated attacker to execute arbitrary code on the system  |
| CVE-2026-81669 | 7.2 | 2026-09-18 | IBM Guardium Data Protection 12.2 is vulnerable to a command injection vulnerability in the create csr wildcard CLI comm |
| CVE-2026-81933 | 8.8 | 2026-09-18 | IBM Guardium Data Protection 12.2 is vulnerable to a SQL injection vulnerability in the Analytic Grid Service Handler. A |
| CVE-2026-81937 | 7.2 | 2026-09-18 | IBM Guardium Data Protection 12.2 is vulnerable to a command injection vulnerability in the import remotelog_config file |
| CVE-2026-82340 | 9.8 | 2026-09-18 | IBM Guardium Data Protection 12.2 is vulnerable to unauthenticated insecure deserialization and attacker-controlled refl |
| CVE-2026-82832 | 9.6 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to execute arbitrary code due to improper  |
| CVE-2026-82885 | 8.8 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to gain elevated privileges due to missing |
| CVE-2026-82887 | 8.8 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to execute arbitrary commands due to impro |
| CVE-2026-82892 | 8.1 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote attacker to execute arbitrary commands due to improper neutraliza |
| CVE-2026-82893 | 7.8 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a local attacker to gain elevated privileges due to improper privilege man |
| CVE-2026-82896 | 7.6 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to traverse directories on the system due  |
| CVE-2026-82967 | 9.8 | 2026-09-18 | IBM Guardium Data Protection 12.2 is vulnerable to an authentication bypass that allows an unauthenticated remote attack |
| CVE-2026-84031 | 9.0 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to execute arbitrary code due to improper  |
| CVE-2026-84034 | 8.8 | 2026-09-18 | IBM Guardium Data Protection 12.2 is vulnerable to a hardcoded credentials vulnerability in the hardware_assess/obstore  |
| CVE-2026-84036 | 7.4 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to bypass security restrictions due to imp |
| CVE-2026-84064 | 9.9 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to execute arbitrary SQL commands due to i |
| CVE-2026-84070 | 8.9 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to execute arbitrary code due to improper  |
| CVE-2026-84071 | 7.2 | 2026-09-18 | IBM Guardium Data Protection 12.2 is vulnerable to OS command injection in the Universal Connector plugin upload functio |
| CVE-2026-84073 | 9.1 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to execute arbitrary SQL commands due to i |
| CVE-2026-84074 | 8.9 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to execute arbitrary code due to improper  |
| CVE-2026-84075 | 9.9 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote attacker to bypass security restrictions due to missing authentic |
| CVE-2026-84076 | 7.6 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to bypass security restrictions due to imp |
| CVE-2026-84077 | 8.1 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote attacker to bypass security restrictions due to a cross-site requ |
| CVE-2026-84078 | 9.9 | 2026-09-18 | IBM Guardium Data Protection 12.2 is vulnerable to a missing authentication vulnerability in the LoadBalancerServlet. An |
| CVE-2026-84081 | 8.1 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote attacker to bypass security restrictions due to improper certific |
| CVE-2026-84082 | 9.8 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote attacker to execute arbitrary SQL commands due to improper neutra |
| CVE-2026-84083 | 7.8 | 2026-09-18 | IBM Guardium Data Protection 12.2 is vulnerable to local privilege escalation via the SUID-root nmap_wrapper binary on t |
| CVE-2026-84084 | 8.8 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote attacker to bypass security restrictions due to a cross-site requ |
| CVE-2026-84085 | 8.1 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote attacker to execute arbitrary OS commands due to improper neutral |
| CVE-2026-84086 | 7.2 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to execute arbitrary code due to improper  |
| CVE-2026-84089 | 7.8 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a local attacker to gain elevated privileges due to improper privilege man |
| CVE-2026-84105 | 7.7 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to obtain sensitive information due to imp |
| CVE-2026-84106 | 8.9 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to execute arbitrary code due to improper  |
| CVE-2026-84108 | 8.1 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote attacker to execute arbitrary code due to improper neutralization |
| CVE-2026-84239 | 7.6 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to obtain sensitive information due to imp |
| CVE-2026-84241 | 8.1 | 2026-09-18 | IBM Guardium Data Protection 12.2 could allow a remote attacker to bypass security restrictions due to improper authoriz |
| CVE-2026-92708 | 7.5 | 2026-09-18 | Svelte devalue is a JavaScript library that serializes values into strings when JSON.stringify isn't sufficient for the  |
| CVE-2026-93031 | 8.8 | 2026-09-18 | The WP Cloud Plugins Use-your-Drive, Out-of-the-Box, Share-one-Drive, and Lets-Box plugins for WordPress are vulnerable  |
| CVE-2026-93839 | 9.8 | 2026-09-18 | LightLLM through 1.2.0 contains an authentication bypass vulnerability in the /pd_register WebSocket endpoint that allow |
| CVE-2026-93868 | 8.1 | 2026-09-18 | Cotonti through 1.0.0 derives password recovery validation tokens from md5(microtime()) in users.passrecover.php, creati |
| CVE-2026-93872 | 7.5 | 2026-09-18 | Cotonti 1.0.0 passes the base64-decoded cb parameter to unserialize() without allowed_classes restriction in the comment |
| CVE-2026-57223 | 7.0 | 2026-09-18 | Suricata is a network Intrusion Detection System, Intrusion Prevention System and Network Security Monitoring engine. Pr |
| CVE-2026-57227 | 7.5 | 2026-09-18 | Suricata is a network Intrusion Detection System, Intrusion Prevention System and Network Security Monitoring engine. Fr |
| CVE-2026-57228 | 8.2 | 2026-09-18 | Suricata is a network Intrusion Detection System, Intrusion Prevention System and Network Security Monitoring engine. Fr |
| CVE-2026-63446 | 7.5 | 2026-09-18 | Suricata is a network Intrusion Detection System, Intrusion Prevention System and Network Security Monitoring engine. Fr |
| CVE-2026-63447 | 7.5 | 2026-09-18 | Suricata is a network Intrusion Detection System, Intrusion Prevention System and Network Security Monitoring engine. Fr |
| CVE-2026-63452 | 7.5 | 2026-09-18 | Suricata is a network Intrusion Detection System, Intrusion Prevention System and Network Security Monitoring engine. Fr |
| CVE-2026-68928 | 8.6 | 2026-09-18 | Acode is a powerful text and code editor for Android. From 1.11.6 until 1.12.7, com.foxdebug.acode.rk.exec.terminal.Term |
| CVE-2026-71418 | 7.5 | 2026-09-18 | Suricata is a network Intrusion Detection System, Intrusion Prevention System and Network Security Monitoring engine. Fr |
| CVE-2026-88097 | 8.1 | 2026-09-18 | Use after free in Microsoft Edge (Chromium-based) allows an unauthorized attacker to elevate privileges locally. |
| CVE-2026-93738 | 9.9 | 2026-09-18 | A vulnerability was found in Totolink A3002MU Hh-B20211125.1046. This affects the function formSchedule of the file /boa |
| CVE-2026-75885 | 9.3 | 2026-09-18 | A flaw was found in the OpenShift console. Unauthenticated access to the `/api/devfile/` and `/api/devfile/samples/` end |
| CVE-2026-93739 | 9.9 | 2026-09-18 | A vulnerability was determined in Totolink A3002MU Hh-B20211125.1046. This impacts the function formWlAc of the file /bo |
| CVE-2026-93740 | 10.0 | 2026-09-18 | A vulnerability was identified in Totolink A3002MU Hh-B20211125.1046. Affected is the function formWlEncrypt of the file |
| CVE-2026-93922 | 8.8 | 2026-09-19 | SiYuan through 3.8.4 renders notebook names as raw HTML in the Daily Note picker dialog without escaping, allowing store |
| CVE-2026-93923 | 8.8 | 2026-09-19 | SiYuan through 3.8.4 fails to escape heading style attributes when rendering outline and bookmark dock HTML, allowing st |
| CVE-2026-13354 | 7.2 | 2026-09-19 | The Asset CleanUp: Page Speed Booster plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Comment Cont |
| CVE-2026-84434 | 9.8 | 2026-09-19 | The Gravity Forms plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 3.1. |
| CVE-2026-87909 | 7.5 | 2026-09-19 | The WP Photo Album Plus plugin for WordPress is vulnerable to Remote Code Execution in all versions via the wppa_image_m |
| CVE-2026-89274 | 9.1 | 2026-09-19 | The WP Recipe Maker plugin for WordPress is vulnerable to Arbitrary Shortcode Execution in all versions up to, and inclu |
| CVE-2026-92229 | 9.1 | 2026-09-19 | The The Forminator Forms – Contact Form, Payment Form & Custom Form Builder plugin for WordPress is vulnerable to arbitr |
| CVE-2026-92807 | 8.8 | 2026-09-19 | The Save as PDF Plugin by PDFCrowd plugin for WordPress is vulnerable to Arbitrary Function Invocation in all versions u |
| CVE-2026-93741 | 10.0 | 2026-09-19 | A security flaw has been discovered in Totolink A3002MU Hh-B20211125.1046. Affected by this vulnerability is the functio |
| CVE-2026-15664 | 7.2 | 2026-09-19 | The Quill Forms \| Conversational Multi Step Forms, Surveys & quizzes plugin for WordPress is vulnerable to Stored Cross- |
| CVE-2026-4327 | 8.8 | 2026-09-19 | The The Welcomizer plugin for WordPress is vulnerable to Remote Code Execution in all versions up to and including 2.8.1 |
| CVE-2026-85658 | 8.1 | 2026-09-19 | The Paid Membership Plugin, Ecommerce, User Registration Form, Login Form, User Profile & Restrict Content – ProfilePres |
| CVE-2026-1255 | 7.5 | 2026-09-19 | The YS LeadGen plugin for WordPress is vulnerable to Sensitive Information Exposure in all versions up to, and including |
| CVE-2026-93742 | 9.9 | 2026-09-19 | A weakness has been identified in Totolink A3002MU Hh-B20211125.1046. Affected by this issue is the function formWsc of  |
| CVE-2026-93985 | 9.9 | 2026-09-19 | OpenPanel js-runtime through commit bad75bdd contains a sandbox escape vulnerability in the JavaScript webhook template  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2025-39964 | Linux / Kernel | 2026-09-18 | 2026-09-21 | Unknown |
| CVE-2026-53266 | Linux / Kernel | 2026-09-18 | 2026-09-21 | Unknown |
| CVE-2025-39682 | Linux / Kernel | 2026-09-18 | 2026-09-21 | Unknown |
| CVE-2026-58704 | Google / Pixel | 2026-09-16 | 2026-09-19 | Unknown |
| CVE-2026-76460 | Cisco / Identity Services Engine | 2026-09-16 | 2026-09-19 | Unknown |
| CVE-2026-87886 | Acronis / Backup | 2026-09-16 | 2026-09-19 | Unknown |
| CVE-2026-76461 | Cisco / Secure Email Gateway | 2026-09-14 | 2026-09-17 | Unknown |

---

*Total entries in CISA KEV catalog: 1716*