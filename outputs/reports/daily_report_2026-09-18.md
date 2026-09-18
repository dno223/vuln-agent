# Vulnerability Intelligence Report

**Date:** 2026-09-18  
**Generated:** 2026-09-18T12:43:46Z  

## Pipeline Warnings

- summarizer failed: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}, 'request_id': 'req_011CfAvf6n9m2Svh7PTNz1Hg'}

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
| CVE-2026-81481 | 7.5 | 2026-09-17 | Dell OpenManage Server Administrator, versions prior to 11.1.0.3, contains an Improper Limitation of a Pathname to a Res |
| CVE-2026-92918 | 8.8 | 2026-09-17 | admin3 through 3.0.0 persists user session tokens in the audit log event body when publishing UserLoggedIn domain events |
| CVE-2026-92919 | 8.1 | 2026-09-17 | admin3 through 3.0.0 fails to sanitize client-supplied filenames in the upload handler, allowing authenticated users to  |
| CVE-2026-62101 | 9.8 | 2026-09-17 | Unauthenticated Broken Authentication in EduAdmin Booking <= 5.4.2 versions. |
| CVE-2026-62104 | 10.0 | 2026-09-17 | Unauthenticated Remote Code Execution (RCE) in Migratico Lite <= 2.6.8 versions. |
| CVE-2026-62108 | 9.8 | 2026-09-17 | Unauthenticated Broken Authentication in Headless Single Sign On <= 1.7.0 versions. |
| CVE-2026-66571 | 7.1 | 2026-09-17 | Unauthenticated Cross Site Request Forgery (CSRF) in Asset CleanUp: Page Speed Booster <= 1.4.0.5 versions. |
| CVE-2026-66580 | 8.5 | 2026-09-17 | Contributor SQL Injection in Product Feed Manager <= 7.12.0 versions. |
| CVE-2026-66618 | 7.6 | 2026-09-17 | Administrator SQL Injection in WP Maps <= 4.9.9 versions. |
| CVE-2026-66619 | 7.6 | 2026-09-17 | Administrator SQL Injection in Newsletters <= 4.18 versions. |
| CVE-2026-66624 | 7.6 | 2026-09-17 | Administrator SQL Injection in WPMasterToolKit <= 2.22.0 versions. |
| CVE-2026-66625 | 7.6 | 2026-09-17 | Administrator SQL Injection in WC Vendors Marketplace <= 2.7.2.1 versions. |
| CVE-2026-66626 | 7.6 | 2026-09-17 | Editor SQL Injection in SKT Addons for Elementor <= 4.0 versions. |
| CVE-2026-66628 | 7.6 | 2026-09-17 | Shop manager SQL Injection in WP-Lister Lite for eBay <= 3.8.11 versions. |
| CVE-2026-66630 | 7.6 | 2026-09-17 | Administrator SQL Injection in PublishPress Series <= 3.1.3 versions. |
| CVE-2026-66631 | 7.6 | 2026-09-17 | Administrator SQL Injection in MC Woocommerce Wishlist <= 1.9.21 versions. |
| CVE-2026-78295 | 8.8 | 2026-09-17 | Unauthenticated Cross Site Request Forgery (CSRF) in Xagio SEO <= 7.1.0.43 versions. |
| CVE-2026-81442 | 8.1 | 2026-09-17 | Dell OpenManage Server Administrator, versions prior to 11.1.0.3, contains an Improper Privilege Management vulnerabilit |
| CVE-2026-90887 | 7.1 | 2026-09-17 | Unauthenticated Cross Site Scripting (XSS) in WP Inventory Manager <= 2.5.4 versions. |
| CVE-2026-90986 | 7.1 | 2026-09-17 | Unauthenticated Cross Site Scripting (XSS) in Visitor Traffic Real Time Statistics Pro <= 11.21 versions. |
| CVE-2026-92934 | 9.0 | 2026-09-17 | vm2 before 3.11.8 contains an incomplete fix for Error.cause sanitization that allows sandbox escape when revisited host |
| CVE-2026-92935 | 9.0 | 2026-09-17 | vm2 is a sandbox for running untrusted Node.js code. In versions >= 3.11.4 and <= 3.11.6, the NodeVM constructor compute |
| CVE-2026-92937 | 10.0 | 2026-09-17 | vm2 3.11.6 is vulnerable to a sandbox escape leading to remote code execution in the host Node.js process. The fix for G |
| CVE-2026-92938 | 9.9 | 2026-09-17 | vm2 versions 3.11.3 through 3.11.6 expose Node.js's host node:sqlite module to code running in NodeVM when that builtin  |
| CVE-2026-92939 | 9.9 | 2026-09-17 | vm2 3.11.3 through 3.11.6 exposes the host Node.js crypto module to a NodeVM sandbox when the crypto builtin is allowed. |
| CVE-2026-92940 | 10.0 | 2026-09-17 | vm2 versions 3.11.3 through 3.11.6 expose the host process's real https.globalAgent to sandboxed code when a NodeVM is e |
| CVE-2026-92941 | 10.0 | 2026-09-17 | vm2 versions from 3.11.3 before 3.11.7 expose the host tls module to NodeVM sandbox code, allowing attackers to call tls |
| CVE-2026-92942 | 7.5 | 2026-09-17 | vm2 before 3.11.7 (affected versions <= 3.11.6) does not enforce the VM({ timeout }) option on code executed outside the |
| CVE-2026-92944 | 9.8 | 2026-09-17 | vm2 versions 3.10.2 through 3.11.6 contain a sandbox escape vulnerability on Node.js 26 where Promise.prototype.finally( |
| CVE-2026-92946 | 10.0 | 2026-09-17 | vm2 before 3.11.7 contains a remote code execution vulnerability when require.external is enabled without an explicit re |
| CVE-2026-92947 | 10.0 | 2026-09-17 | vm2 before 3.11.7 exposes Node's shared Buffer pool to sandboxed code, allowing disclosure of host memory used by Buffer |
| CVE-2026-92948 | 9.9 | 2026-09-17 | vm2 versions >= 3.9.6 and <= 3.11.6 are affected by a NodeVM builtin allowlist bypass that permits a sandbox escape on N |
| CVE-2026-92950 | 8.6 | 2026-09-17 | vm2 before 3.11.7 contains a sandbox escape vulnerability in the CLI tool that allows attackers to execute arbitrary cod |
| CVE-2026-92951 | 9.9 | 2026-09-17 | vm2 before 3.11.7 contains an incorrect authorization vulnerability in the external package allowlist check that uses no |
| CVE-2026-92953 | 10.0 | 2026-09-17 | vm2 versions from 3.11.0 before 3.11.8 fail to protect host TypedArray and ArrayBuffer prototypes from sandbox mutation. |
| CVE-2026-92954 | 8.6 | 2026-09-17 | vm2 is a sandbox library for running untrusted JavaScript in Node.js. In versions >= 3.10.0 and <= 3.11.7, Promises retu |
| CVE-2026-92955 | 10.0 | 2026-09-17 | vm2 before 3.11.8 contains a sandbox escape vulnerability in NodeVM that allows attackers to access the host __proto__ g |
| CVE-2026-92956 | 10.0 | 2026-09-17 | vm2 versions 3.10.1 through 3.11.6 contain a sandbox escape reachable from a default `new VM()` sandbox when running on  |
| CVE-2026-92957 | 9.9 | 2026-09-17 | vm2 through 3.11.6 does not normalize `node:`-prefixed builtin specifiers when evaluating user-supplied negative (deny)  |
| CVE-2026-92958 | 8.5 | 2026-09-17 | vm2 through 3.11.6 contains a builtin-module denylist bypass in NodeVM. When the embedder uses the builtin wildcard toge |
| CVE-2026-92959 | 7.1 | 2026-09-17 | vm2 before 3.11.8 does not fully enforce the allowAsync: false option in VM and NodeVM. While localPromise.prototype.the |
| CVE-2026-92960 | 10.0 | 2026-09-17 | vm2 before 3.11.6 fails to restrict access to os and dns builtins under the builtin: ['*'] configuration, allowing sandb |
| CVE-2026-92961 | 7.5 | 2026-09-17 | vm2 before 3.11.6 fails to enforce bufferAllocLimit on ArrayBuffer, SharedArrayBuffer, and TypedArray constructors, allo |
| CVE-2026-92970 | 8.8 | 2026-09-17 | HUBzero CMS through 2.2.32 contains a path traversal vulnerability in project file upload handlers that allows authentic |
| CVE-2026-92971 | 7.5 | 2026-09-17 | InternLM LMDeploy through 0.17.0 contains a reachable assertion vulnerability in the DistServe decode migration loop tha |
| CVE-2026-92972 | 8.6 | 2026-09-17 | SGLang through 0.5.19 in prefill/decode disaggregation mode contains an unauthenticated PUT /route endpoint on the prefi |
| CVE-2026-26950 | 8.1 | 2026-09-17 | Dell SmartFabric Manager, versions prior to 2.2.1, contains an Insufficient Verification of Data Authenticity vulnerabil |
| CVE-2026-63459 | 8.7 | 2026-09-17 | Vendure is an open-source headless commerce platform. Prior to 3.6.5, RichTextDescriptionCell in packages/dashboard/src/ |
| CVE-2026-63460 | 7.5 | 2026-09-17 | Vendure is an open-source headless commerce platform. Prior to 3.6.5, the public Shop GraphQL API allows an unauthentica |
| CVE-2026-63472 | 9.1 | 2026-09-17 | Vendure is an open-source headless commerce platform. Prior to 3.7.0, ExternalAuthenticationService.createCustomerAndUse |
| CVE-2026-77614 | 8.8 | 2026-09-17 | Opencast is a free, open-source platform to support the management of educational audio and video content. Prior to vers |
| CVE-2026-80356 | 7.3 | 2026-09-17 | Dell OpenManage Server Administrator, versions prior to 11.1.0.3, contains an Exposure of Sensitive Information to an Un |
| CVE-2026-81445 | 7.2 | 2026-09-17 | Dell OpenManage Server Administrator, versions prior to 11.1.0.3, contains an Improper Privilege Management vulnerabilit |
| CVE-2026-81446 | 7.4 | 2026-09-17 | Dell OpenManage Server Administrator, versions prior to 11.1.0.3, contains a Server-Side Request Forgery (SSRF) vulnerab |
| CVE-2026-85077 | 8.2 | 2026-09-17 | Sanic is an opensource python web server/framework. Prior to version 24.12.1, and in version 25.12.0, the HTTP/1.1 respo |
| CVE-2026-87742 | 7.5 | 2026-09-17 | A flaw was found in quarkus-websockets-next. This vulnerability allows a remote attacker to cause a Denial of Service (D |
| CVE-2026-92983 | 7.5 | 2026-09-17 | InternLM LMDeploy through 0.17.0 in DistServe prefill/decode disaggregation mode fails to release scheduler sessions bec |
| CVE-2026-92984 | 8.1 | 2026-09-17 | HUBzero CMS through 2.2.32 accepts session identifiers from query strings and request variables instead of cookies alone |
| CVE-2026-92985 | 8.8 | 2026-09-17 | SiYuan versions before 3.8.4 fail to escape bookmark labels imported from notebook files when rendering them in the dock |
| CVE-2026-92986 | 8.8 | 2026-09-17 | SiYuan before 3.8.4 renders document titles as HTML in the backlink dock tree without escaping markup characters. Attack |
| CVE-2026-92987 | 7.5 | 2026-09-17 | roxmltree through 0.21.1 performs quadratic-time attribute and namespace validation during XML parsing without limits on |
| CVE-2026-56795 | 8.2 | 2026-09-17 | Dell Server Update Utility, versions prior to 26.07.01, contains an Uncontrolled Search Path Element vulnerability. A lo |
| CVE-2026-76834 | 8.1 | 2026-09-17 | b2evolution CMS versions 6.7.8 through 7.2.5 contain an incomplete fix for CVE-2016-8901 where the serialized-array obje |
| CVE-2026-81515 | 7.5 | 2026-09-17 | Steeltoe is an open source project that provides a collection of libraries that helps users build cloud-native applicati |
| CVE-2026-81516 | 7.5 | 2026-09-17 | Steeltoe is an open source project that provides a collection of libraries that helps users build cloud-native applicati |
| CVE-2026-85715 | 7.5 | 2026-09-17 | ExifReader is a JavaScript Exif information parser. Prior to 4.41.1, ExifReader parses attacker-controlled HEIC or AVIF  |
| CVE-2026-85719 | 7.5 | 2026-09-17 | The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process HT |
| CVE-2026-85721 | 7.5 | 2026-09-17 | The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process HT |
| CVE-2026-86038 | 7.5 | 2026-09-17 | libp2p is a JavaScript implementation of the libp2p networking stack. From 15.0.0 until 16.0.5, @libp2p/gossipsub uses t |
| CVE-2026-86039 | 8.2 | 2026-09-17 | libp2p is a JavaScript implementation of the libp2p networking stack. From 8.0.0 until 12.0.24, @libp2p/peer-store in pa |
| CVE-2026-86040 | 7.5 | 2026-09-17 | libp2p is a JavaScript implementation of the libp2p networking stack. Prior to 11.0.26, @libp2p/floodsub accepts unauthe |
| CVE-2026-86863 | 9.8 | 2026-09-17 | pgAdmin 4's Webserver authentication source is intended to accept an identity asserted by the web server or reverse prox |
| CVE-2026-86864 | 8.8 | 2026-09-17 | pgAdmin 4's Backup tool appended the client-supplied 'database' field from the /backup/job/<sid>/object request to the p |
| CVE-2026-89036 | 8.8 | 2026-09-17 | Appwrite before 2.0.0 contains an argument injection vulnerability that allows authenticated users with functions.write  |
| CVE-2026-93014 | 7.1 | 2026-09-17 | RosarioSIS versions before 12.9 fail to validate the filename request parameter in Users and Students modules, allowing  |
| CVE-2026-28326 | 8.8 | 2026-09-17 | SolarWinds Access Rights Manager was reported to be affected by an unauthenticated remote code execution vulnerability.  |
| CVE-2026-92980 | 7.2 | 2026-09-17 | HortusFox-Web prior to version 6.1 contains a remote code execution vulnerability that allows authenticated administrato |
| CVE-2026-93292 | 8.5 | 2026-09-17 | SigNoz versions from 0.88.0 before 0.142.1 contain a SQL injection vulnerability in trace-funnel analytics endpoints tha |
| CVE-2026-44236 | 7.1 | 2026-09-17 | rabbitmq-c is a C-language AMQP client library for RabbitMQ. Prior to 0.16.0, a malicious AMQP server can send an unders |
| CVE-2026-54053 | 9.6 | 2026-09-17 | Many Notes is a Markdown note-taking web application designed for simplicity. Prior to 0.16.0, the ZIP vault import impl |
| CVE-2026-54446 | 8.1 | 2026-09-17 | NetLicensing MCP Server is a natural-language interface that enables agentic applications to manage the software-licensi |
| CVE-2026-92926 | 7.3 | 2026-09-17 | A vulnerability has been found in code-projects Matrimonial System 1.0. This vulnerability affects the function writepar |
| CVE-2026-19477 | 7.8 | 2026-09-17 | There
is stack-based buffer overflow vulnerability recently discovered in MCC Universal Library for Linux (uldaq).  This |
| CVE-2026-47252 | 9.0 | 2026-09-17 | Anyquery is an SQL query engine built on top of SQLite. Prior to 0.4.5, authenticated users with INSERT or UPDATE access |
| CVE-2026-52727 | 7.2 | 2026-09-17 | lxc-ci contains continuous integration and image-build scripts for LXC. Prior to the 2026-05-28 Arch Linux image publica |
| CVE-2026-52851 | 7.1 | 2026-09-17 | Traccar is an open source GPS tracking system. Prior to 6.14.0, an authenticated, non-readonly user with access to an ob |
| CVE-2026-54239 | 8.8 | 2026-09-17 | Faust.js is a headless WordPress toolkit. Prior to 1.8.11, the FaustWP WordPress plugin authenticates only the ciphertex |
| CVE-2026-54253 | 8.2 | 2026-09-17 | TS3 Manager is modern web interface for maintaining Teamspeak3 servers. Prior to 2.2.6, the /api/download handler in pac |
| CVE-2026-54504 | 8.8 | 2026-09-17 | MCP Documentation Server is a local-first document management and semantic search server for AI coding agents. From 1.13 |
| CVE-2026-54617 | 9.8 | 2026-09-17 | GravitLauncher is an open-source Minecraft launcher based on sashok724's v3. Prior to 5.7.12, an unauthenticated remote  |
| CVE-2026-90997 | 7.4 | 2026-09-17 | A flaw was found in Keycloak. When deployed in stateless mode with MySQL or MariaDB, a mismatch in row-count semantics b |
| CVE-2026-45720 | 7.0 | 2026-09-17 | Omni manages Kubernetes on bare metal, virtual machines, or in a cloud. Prior to 1.6.6 and from 1.7.0 until 1.7.3, SAML. |
| CVE-2026-45726 | 7.6 | 2026-09-17 | Omni manages Kubernetes on bare metal, virtual machines, or in a cloud. From 1.3.0 until 1.6.6 and 1.7.3, importing a st |
| CVE-2026-50125 | 7.5 | 2026-09-17 | MKP is a Model Context Protocol server for Kubernetes. Prior to 0.4.1, cmd/server/main.go exposes the default HTTP endpo |
| CVE-2026-50285 | 7.5 | 2026-09-17 | Pomerium is an identity and context-aware access proxy. Prior to 0.32.8, decodeQueryStringV2 in pkg/hpke/url.go performs |
| CVE-2026-54618 | 9.4 | 2026-09-17 | Obsidian Web MCP is a secure remote MCP server for Obsidian vaults. Prior to 0.2.0, /oauth/authorize issues an authoriza |
| CVE-2026-54626 | 9.8 | 2026-09-17 | SAIL is a cross-platform library for loading and saving images with support for animation, metadata, and ICC profiles. I |
| CVE-2026-54627 | 9.8 | 2026-09-17 | SAIL is a cross-platform library for loading and saving images with support for animation, metadata, and ICC profiles. I |
| CVE-2026-54692 | 7.8 | 2026-09-17 | SAIL is a cross-platform library for loading and saving images with support for animation, metadata, and ICC profiles. P |
| CVE-2026-54716 | 7.5 | 2026-09-17 | Valhalla is an open source routing engine and accompanying libraries for use with OpenStreetMap data. In 3.7.0 and earli |
| CVE-2026-54752 | 9.6 | 2026-09-17 | NetBox Device Type Library is a collection of community-sourced device type definitions for import into NetBox. The vali |
| CVE-2026-92943 | 8.1 | 2026-09-17 | Improper validation of certificate with host mismatch in the MQTT client TLS connection layer in AWS IoT Device SDK for  |
| CVE-2026-93337 | 7.8 | 2026-09-17 | NetworkManager-l2tp contains an improper input validation vulnerability that allows local users with VPN connection crea |
| CVE-2026-15815 | 8.8 | 2026-09-17 | Grafana OSS and Grafana Enterprise did not safely resolve symbolic links when
extracting plugin archives. A crafted plug |
| CVE-2026-45140 | 9.8 | 2026-09-17 | Chamilo LMS is an open-source learning management system. Prior to 2.0.1, Chamilo LMS allows an unauthenticated remote a |
| CVE-2026-45143 | 9.0 | 2026-09-17 | Chamilo LMS is an open-source learning management system. From 2.0.0 through at least 2.1.0, Chamilo LMS stores private  |
| CVE-2026-50275 | 7.5 | 2026-09-17 | The Datadog PHP Tracer provides application performance monitoring and distributed tracing for PHP. Prior to 1.19.2, ddt |
| CVE-2026-50277 | 7.5 | 2026-09-17 | dd-trace-cpp is the Datadog distributed tracing library for C++. Prior to 2.1.0, dd-trace-cpp parses incoming W3C baggag |
| CVE-2026-54339 | 7.7 | 2026-09-17 | Glean is a self-hosted RSS reader and personal knowledge management tool. Prior to 0.2.6, POST /api/feeds/discover passe |
| CVE-2026-54354 | 8.2 | 2026-09-17 | MapServer is a system for developing web-based GIS applications. Prior to 8.6.4, MapServer's PostGIS runtime filter tran |
| CVE-2026-54460 | 9.8 | 2026-09-17 | OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. Prior to 1.1 |
| CVE-2026-54510 | 7.1 | 2026-09-17 | Speakr is a personal, self-hosted web application designed for transcribing audio recordings. Prior to 0.8.21-alpha, the |
| CVE-2026-54596 | 8.1 | 2026-09-17 | ITFlow provides an IT documentation, ticketing and accounting system for small managed service providers. Prior to versi |
| CVE-2026-54597 | 8.3 | 2026-09-17 | ITFlow provides an IT documentation, ticketing and accounting system for small managed service providers. Prior to versi |
| CVE-2026-54916 | 8.8 | 2026-09-17 | NetBox Device Type Library is a collection of community-sourced device type definitions for import into NetBox. The abse |
| CVE-2026-68523 | 7.5 | 2026-09-17 | `fulgur` converts untrusted HTML/CSS into PDF, commonly on a server that processes input supplied by many tenants. In ve |
| CVE-2026-68537 | 7.5 | 2026-09-17 | `fulgur` converts untrusted HTML/CSS into PDF, commonly on a server that processes input supplied by many tenants. In ve |
| CVE-2026-76154 | 7.3 | 2026-09-17 | A stored cross-site scripting vulnerability in the Geomap panel's MapLibre base layer allows a user with the Editor role |
| CVE-2026-77615 | 8.7 | 2026-09-17 | Paella Player is a set of libraries to create a multi stream video player. Prior to Paulla Player 2.12.11 (as used in Op |
| CVE-2026-86049 | 7.1 | 2026-09-17 | Jupyter Server is the backend for Jupyter web applications. Prior to version 2.21.0, the 5xx request logging path in jup |
| CVE-2026-93393 | 8.1 | 2026-09-17 | A heap-based buffer overflow exists in the TLS transport layer of the MongoDB C Driver when built with the Windows platf |
| CVE-2026-50158 | 7.7 | 2026-09-17 | yutu is an AI-powered toolkit for managing and growing YouTube channels. Prior to 0.10.9, the caption-download MCP tool  |
| CVE-2026-54506 | 7.6 | 2026-09-17 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to 1.0.8.5 |
| CVE-2026-54519 | 8.8 | 2026-09-17 | AI Agent Automation is a modular AI agent workflow automation platform with schedulers, tools, and observability. Prior  |
| CVE-2026-54520 | 8.1 | 2026-09-17 | AI Agent Automation is a modular AI agent workflow automation platform with schedulers, tools, and observability. Prior  |
| CVE-2026-54612 | 8.8 | 2026-09-17 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. From 1.0.0 until |
| CVE-2026-54634 | 7.3 | 2026-09-17 | Hamlib is a ham radio control library for radios, rotators, and amplifiers. Prior to 4.7.2, the unauthenticated rigctld  |
| CVE-2026-54646 | 7.2 | 2026-09-17 | CubeCart is an ecommerce software solution. Prior to 6.7.5, admin/sources/maintenance.index.inc.php places administrator |
| CVE-2026-54647 | 7.2 | 2026-09-17 | CubeCart is an ecommerce software solution. Prior to 6.7.5, admin/sources/settings.index.inc.php directly concatenates t |
| CVE-2026-54670 | 9.1 | 2026-09-17 | WeGIA is a web manager for charitable institutions. Prior to 3.8.5, the contribution request dispatcher in web/html/cont |
| CVE-2026-54671 | 8.8 | 2026-09-17 | WeGIA is a web manager for charitable institutions. Prior to 3.8.5, WeGIA maps InternoControle to an empty resource arra |
| CVE-2026-54734 | 10.0 | 2026-09-17 | Prebid Server Java is the Java version of Prebid Server. Prior to 3.43.0, certain bidder adapters interpolate user-suppl |
| CVE-2026-54767 | 9.1 | 2026-09-17 | WeGIA is a web manager for charitable institutions. Prior to 3.8.5, web/html/socio/sistema/controller/deletar_socios.php |
| CVE-2026-93426 | 8.5 | 2026-09-17 | SigNoz versions 0.87.0 before 0.142.0 fail to escape user-supplied telemetry field-key names in the v5 query_range API,  |
| CVE-2026-68791 | 8.6 | 2026-09-17 | Incorrect authorization in Azure Machine Learning allows an unauthorized attacker to disclose information over a network |
| CVE-2026-69399 | 10.0 | 2026-09-17 | Azure Arc Elevation of Privilege Vulnerability |
| CVE-2026-69865 | 10.0 | 2026-09-17 | Authorization bypass through user-controlled key in Microsoft Container Registry allows an unauthorized attacker to elev |
| CVE-2026-70009 | 9.3 | 2026-09-17 | Improper limitation of a pathname to a restricted directory ('path traversal') in Azure Arc allows an unauthorized attac |
| CVE-2026-70200 | 10.0 | 2026-09-17 | Improper limitation of a pathname to a restricted directory ('path traversal') in Azure Logic Apps allows an unauthorize |
| CVE-2026-77903 | 9.0 | 2026-09-17 | Authentication bypass by spoofing in Microsoft Dataverse allows an unauthorized attacker to elevate privileges over a ne |
| CVE-2026-78501 | 7.4 | 2026-09-17 | Improper neutralization of special elements used in a command ('command injection') in Microsoft 365 Copilot's Business  |
| CVE-2026-83944 | 10.0 | 2026-09-17 | Improper access control in Azure Logic Apps allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-85885 | 9.9 | 2026-09-17 | Improper neutralization of special elements used in a command ('command injection') in M365 Copilot allows an authorized |
| CVE-2026-85889 | 10.0 | 2026-09-17 | Missing authentication for critical function in Azure AI Foundry allows an unauthorized attacker to elevate privileges o |
| CVE-2026-85917 | 7.5 | 2026-09-17 | Server-side request forgery (ssrf) in Azure AI Foundry allows an unauthorized attacker to elevate privileges over a netw |
| CVE-2026-87701 | 9.6 | 2026-09-17 | Improper neutralization of special elements in output used by a downstream component ('injection') in Azure Cosmos DB al |
| CVE-2026-87886 | 7.8 | 2026-09-17 | Local privilege escalation due to insecure file permissions. The following products are affected: Acronis Backup plugin  |
| CVE-2026-93435 | 7.5 | 2026-09-17 | redis-parser through 3.0.0 contains a denial of service vulnerability in the RESP protocol parser that allows malicious  |
| CVE-2026-93436 | 7.5 | 2026-09-17 | vLLM through 0.29.0 fails to properly clean up decode-side metadata for rejected inference requests in prefill/decode di |
| CVE-2026-62874 | 10.0 | 2026-09-18 | Insufficient verification of data authenticity in Azure Billing allows an unauthorized attacker to elevate privileges ov |
| CVE-2026-69843 | 10.0 | 2026-09-18 | Authentication bypass by spoofing in Microsoft Fabric allows an unauthorized attacker to elevate privileges over a netwo |
| CVE-2026-83946 | 8.2 | 2026-09-18 | Improper neutralization of input during web page generation ('cross-site scripting') in Azure Portal allows an unauthori |
| CVE-2026-85878 | 9.9 | 2026-09-18 | Improper authorization in Azure Database for PostgreSQL allows an authorized attacker to elevate privileges over a netwo |
| CVE-2026-85887 | 7.7 | 2026-09-18 | Incorrect permission assignment for critical resource in M365 Copilot allows an authorized attacker to disclose informat |
| CVE-2026-93450 | 7.5 | 2026-09-18 | go-openapi/swag jsonutils before 0.27.1 contains a stack overflow vulnerability in ordered JSON parsing and serializatio |
| CVE-2026-93452 | 7.5 | 2026-09-18 | snappy-java through 1.1.10.8 contains a buffer overflow vulnerability in Snappy.compress(ByteBuffer, ByteBuffer) that wr |
| CVE-2026-93453 | 8.3 | 2026-09-18 | SOGo before 5.12.11 constructs password-reset links using the client-supplied Origin header as the authority, allowing u |
| CVE-2026-93331 | 7.3 | 2026-09-18 | A vulnerability was identified in GPAC 26.08-DEV. This vulnerability affects the function gf_rtp_parse_ttxt of the file  |
| CVE-2026-93456 | 8.2 | 2026-09-18 | django-page-cms through 2.0.13 exempts five admin mutation views from CSRF protection in pages/admin/views.py, allowing  |
| CVE-2026-93371 | 8.3 | 2026-09-18 | A security vulnerability has been detected in marcopiovanello yt-dlp-web-ui up to v4. This issue affects the function Ne |
| CVE-2026-93467 | 9.8 | 2026-09-18 | The OAKlouds developed by HGiga has a Insecure Deserialization vulnerability. Unauthenticated remote attackers can execu |
| CVE-2026-93468 | 7.5 | 2026-09-18 | The OAKlouds developed by HGiga has an Arbitrary File Read vulnerability. Unauthenticated remote attackers can exploit R |
| CVE-2026-17086 | 8.8 | 2026-09-18 | The ShortPixel Image Optimizer – Optimize Images, Convert WebP & AVIF plugin for WordPress is vulnerable to PHP Object I |
| CVE-2026-18911 | 7.5 | 2026-09-18 | ManageEngine DataSecurity Plus versions before 6310 are vulnerable to an agent authentication bypass, allowing unenrolle |
| CVE-2026-18912 | 7.7 | 2026-09-18 | ManageEngine DataSecurity Plus versions before 6310 are vulnerable to an authenticated SQL injection vulnerability, allo |
| CVE-2026-81810 | 7.2 | 2026-09-18 | The All-in-One WP Migration and Backup WordPress plugin before 7.111 does not perform any capability check on several of |
| CVE-2026-84738 | 9.1 | 2026-09-18 | The AF Companion  WordPress plugin before 2.2.0 does not validate the type of files uploaded through one of its import f |
| CVE-2026-85122 | 8.8 | 2026-09-18 | The Easy Form Builder by WhiteStudio  WordPress plugin before 4.2.0 does not validate a submitted value against the stor |
| CVE-2026-85127 | 8.8 | 2026-09-18 | The VikBooking Hotel Booking Engine & PMS WordPress plugin before 1.8.15 does not restrict the type of files unauthentic |
| CVE-2026-87767 | 8.6 | 2026-09-18 | The wp shortcut link and advertisement baner WordPress plugin through 1.2.0 does not sanitize and escape a parameter bef |
| CVE-2026-87770 | 8.6 | 2026-09-18 | The Price Drop Alert for Woo Commerce WordPress plugin through 1.1 does not sanitize and escape parameters before using  |
| CVE-2026-87771 | 8.6 | 2026-09-18 | The Product Question and Answer WordPress plugin through 1.1.0 does not sanitize and escape parameters before using them |
| CVE-2026-87774 | 8.6 | 2026-09-18 | The Tz Weekly Radio Schedule WordPress plugin through 1.8.1 does not sanitize and escape a parameter before using it to  |
| CVE-2026-87775 | 8.6 | 2026-09-18 | The Tz Weekly Radio Schedule WordPress plugin through 1.8.1 does not sanitize and escape a parameter before using it to  |
| CVE-2026-88825 | 8.8 | 2026-09-18 | The iGMS Direct Booking WordPress plugin before 2.0 does not authorise or escape its widget appearance settings, allowin |
| CVE-2026-90978 | 7.1 | 2026-09-18 | The Filter Gallery WordPress plugin before 1.1.5 does not verify the nonce on several of its AJAX handlers when the nonc |
| CVE-2026-93485 | 7.1 | 2026-09-18 | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in Automattic WordPre |
| CVE-2026-89413 | 8.1 | 2026-09-18 | The Filter Gallery plugin for WordPress is vulnerable to authorization bypass in all versions up to, and including, 1.1. |
| CVE-2026-92619 | 7.2 | 2026-09-18 | The Booking Calendar plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 11 |
| CVE-2026-12384 | 8.8 | 2026-09-18 | Authorization bypass through User-Controlled key vulnerability in TECHIN2B TECHIN2B Application allows Privilege Abuse.
 |
| CVE-2026-12954 | 8.8 | 2026-09-18 | The Mapster WP Maps plugin for WordPress is vulnerable to Arbitrary User Meta Write in all versions up to, and including |
| CVE-2026-14323 | 7.5 | 2026-09-18 | The Printcart Web to Print Product Designer for WooCommerce plugin for WordPress is vulnerable to Directory Traversal in |
| CVE-2026-15275 | 7.5 | 2026-09-18 | The WP Multi Store Locator Pro plugin for WordPress is vulnerable to generic SQL Injection via the 'store_locatore_searc |
| CVE-2026-18442 | 7.5 | 2026-09-18 | The WCFM Marketplace – Multivendor Marketplace for WooCommerce plugin for WordPress is vulnerable to generic SQL Injecti |
| CVE-2026-67100 | 9.8 | 2026-09-18 | HCL BigFix Service Management is affected by SQL Injection flaw and a Cross-Tenant Data Exposure flaw vulnerabilities. w |
| CVE-2026-67101 | 9.3 | 2026-09-18 | HCL BigFix Service Management is affected by a Server-Side Request Forgery (SSRF) vulnerability in its search functional |
| CVE-2026-67102 | 8.1 | 2026-09-18 | HCL BigFix Service Management is affected by a high-severity Broken Access Control vulnerability, which could allow a lo |
| CVE-2026-67103 | 7.6 | 2026-09-18 | HCL BigFix Service Management is affected by Cross-Site Scripting (XSS) vulnerability, which could allow an attacker to  |
| CVE-2026-85705 | 7.5 | 2026-09-18 | The Location Manager plugin for WordPress is vulnerable to generic SQL Injection via 'latitude' and 'longitude' REST API |
| CVE-2026-89058 | 7.4 | 2026-09-18 | A flaw was found in RESTEasy's CorsFilter, which, when configured to allow all origins ("*"), reflects the request's Ori |
| CVE-2026-89059 | 7.5 | 2026-09-18 | A flaw was found in RESTEasy's IIOImageProvider, which decodes attacker-supplied image request bodies without enforcing  |
| CVE-2026-93494 | 7.5 | 2026-09-18 | A flaw was found in Netty's StompSubframeDecoder component. A remote attacker can exploit this vulnerability by sending  |
| CVE-2026-13639 | 9.8 | 2026-09-18 | An insufficient entropy vulnerability in login logic in Synology DiskStation Manager (DSM) before 7.2.1-69057-12, 7.2.2- |
| CVE-2026-13673 | 8.8 | 2026-09-18 | An incorrect permission assignment for critical resource vulnerability in LDAP API in Synology DiskStation Manager (DSM) |
| CVE-2026-13684 | 9.8 | 2026-09-18 | An improper encoding or escaping of output vulnerability in SCGI in Synology DiskStation Manager (DSM) before 7.2.1-6905 |
| CVE-2026-40530 | 8.0 | 2026-09-18 | An improper neutralization of CRLF sequences ('CRLF injection') vulnerability in User API in Synology DiskStation Manage |
| CVE-2026-40539 | 7.1 | 2026-09-18 | An improper certificate validation vulnerability in Email API in Synology DiskStation Manager (DSM) before 7.2.1-69057-1 |
| CVE-2026-6205 | 8.1 | 2026-09-18 | An external control of file name or path vulnerability in Upload API in Synology DiskStation Manager (DSM) before 7.2.1- |
| CVE-2026-83561 | 7.2 | 2026-09-18 | The Complianz GDPR/CCPA Cookie Consent Banner plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Comm |
| CVE-2026-85410 | 8.1 | 2026-09-18 | The Master Addons for Elementor – Elementor Addons, Widgets, Mega Menu Builder, Popup Builder, Widget Builder & Template |
| CVE-2026-18405 | 7.2 | 2026-09-18 | The Jeg Kit for Elementor – Powerful Addons for Elementor, Widgets & Templates for WordPress plugin for WordPress is vul |
| CVE-2026-87743 | 7.5 | 2026-09-18 | A flaw was found in Quarkus HTTP security. An unauthenticated attacker can exploit a discrepancy in how paths are normal |
| CVE-2026-87915 | 7.2 | 2026-09-18 | The Popup Maker – Boost Sales, Conversions, Optins, Subscribers with the Ultimate WP Popup Builder plugin for WordPress  |
| CVE-2026-28197 | 8.8 | 2026-09-18 | An authenticated, low-privileged user with access to the NetBackup Flex 
OS management shell could supply a specially cr |
| CVE-2026-28198 | 8.8 | 2026-09-18 | An authenticated, low-privileged user with access to the NetBackup Flex 
OS management shell could bypass the cryptograp |
| CVE-2026-93488 | 7.5 | 2026-09-18 | A flaw was found in Netty. SpdySessionHandler accepts an unlimited number of concurrent remote-initiated streams because |

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

---

*Total entries in CISA KEV catalog: 1713*