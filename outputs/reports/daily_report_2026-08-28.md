# Vulnerability Intelligence Report

**Date:** 2026-08-28  
**Generated:** 2026-08-28T19:54:07Z  

## Pipeline Warnings

- summarizer failed: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}, 'request_id': 'req_011CeVjSXHW7u3NkUoQwHFM3'}

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
| CVE-2026-10036 | 8.8 | 2026-08-27 | SpeechBrain before 1.1.1 contains an arbitrary code execution vulnerability that allows attackers to execute arbitrary c |
| CVE-2026-19092 | 9.8 | 2026-08-27 | The Tutor LMS WordPress plugin before 4.0.6 does not prevent request data from overwriting internal variables while rend |
| CVE-2026-53580 | 8.1 | 2026-08-27 | Trilium is an open-source hierarchical note-taking application. In versions prior to 0.104.0, the automatic image-downlo |
| CVE-2026-54718 | 7.2 | 2026-08-27 | Silverstripe Advanced Workflow is a highly configurable step-based workflow module. Prior to 6.4.5, 7.1.3, and 7.2.1, an |
| CVE-2026-54721 | 8.8 | 2026-08-27 | Silverstripe UserForms provides a visual form builder for the Silverstripe CMS. From 6.0.0 until 6.4.9, 7.0.7, and 7.1.1 |
| CVE-2026-59284 | 7.6 | 2026-08-27 | There is no allow list for property keys when Spring Cloud Commons writable /actuator/env is enabled.
Spring Cloud Commo |
| CVE-2026-59307 | 8.0 | 2026-08-27 | An operator who calls JdbcMessageStore.addAllowedPatterns(...) to restrict deserialization receives no protection at all |
| CVE-2026-59316 | 8.2 | 2026-08-27 | Spring Authorization Server's default consent page renders user-controlled values without HTML entity encoding. When usi |
| CVE-2026-59324 | 8.2 | 2026-08-27 | When an IntegrationFlow uses .fluxTransform() with an asynchronous/reordering fluxFunction that emits raw payloads, conc |
| CVE-2026-75889 | 7.7 | 2026-08-27 | Grafana Alloy’s prometheus.operator.servicemonitors component allows a user who can create or modify ServiceMonitor reso |
| CVE-2026-76639 | 8.8 | 2026-08-27 | Unitree G1 EDU firmware through 1.5.2 contains an unauthenticated remote code execution vulnerability that allows networ |
| CVE-2026-76640 | 7.5 | 2026-08-27 | Unitree G1 EDU firmware through 1.5.2 contains multiple chained vulnerabilities in the BLE GATT server and WiFi provisio |
| CVE-2026-77438 | 7.5 | 2026-08-27 | Trilium is an open-source hierarchical note-taking application. In versions up to and including 0.103.0, the public shar |
| CVE-2026-81522 | 8.1 | 2026-08-27 | A weakness in the MongoDB C++ Driver's handling of caller-supplied namespace identifiers allows special characters embed |
| CVE-2026-81525 | 8.1 | 2026-08-27 | The MongoDB client library for PHP does not sufficiently sanitize special elements in application-supplied namespace ide |
| CVE-2026-81529 | 7.1 | 2026-08-27 | Improper neutralization of delimiters in connection-URL construction allows connection-option injection in the MongoDB C |
| CVE-2026-81728 | 8.1 | 2026-08-27 | Dolibarr before 24.0.0 contains a SQL injection in its CSV and XLSX import wizard. The wizard reads its update keys with |
| CVE-2026-81730 | 8.2 | 2026-08-27 | Dolibarr 9.0.0 through 23.0.4 saves inbound email attachments under the name supplied in the message's MIME headers with |
| CVE-2026-81838 | 7.1 | 2026-08-27 | A relative path traversal issue in the zip extraction functionality in AWS diagram-as-code (awsdac) in versions 0.10 thr |
| CVE-2026-81934 | 9.8 | 2026-08-27 | Redis contains a use-after-free vulnerability in the 'tlsProcessPendingData()' function, which handles the TLS pending-d |
| CVE-2025-30156 | 8.9 | 2026-08-28 | Ceph is an open-source distributed storage platform providing object, block, and file storage. In versions prior to 20.2 |
| CVE-2026-18717 | 7.4 | 2026-08-28 | ASE2000 2.35 through 2.37 is vulnerable to an improper certificate validation vulnerability, which may allow an attacker |
| CVE-2026-18965 | 8.8 | 2026-08-28 | PayRange API is missing proper authorization on management endpoints, which allows verbose details of every device on th |
| CVE-2026-39944 | 8.8 | 2026-08-28 | Ceph is an open-source distributed storage platform providing object, block, and file storage. In versions prior to 20.2 |
| CVE-2026-44629 | 7.9 | 2026-08-28 | Improper access control to the Synergis Softwire installation folder. This vulnerability affects Streamvault all-in-one  |
| CVE-2026-50152 | 9.1 | 2026-08-28 | Ceph is an open-source distributed storage platform providing object, block, and file storage. In versions prior to 20.2 |
| CVE-2026-54083 | 8.1 | 2026-08-28 | Wazuh is an open-source security platform providing unified XDR and SIEM protection for endpoints and cloud workloads. T |
| CVE-2026-54085 | 7.1 | 2026-08-28 | Wazuh is an open-source security platform providing unified XDR and SIEM protection for endpoints and cloud workloads. I |
| CVE-2026-54330 | 8.1 | 2026-08-28 | Ceph is an open-source distributed storage platform providing object, block, and file storage. In versions prior to 20.2 |
| CVE-2026-67560 | 7.5 | 2026-08-28 | Bendix EC80 Brake ECU
 is vulnerable to a stack-based buffer overflow, which may allow an 
attacker to crash the ECU. A  |
| CVE-2026-69658 | 9.8 | 2026-08-28 | MQTT credentials and control traffic are transmitted in cleartext, 
exposing sensitive information to network-level atta |
| CVE-2026-71187 | 9.8 | 2026-08-28 | The Ebyte device relies on client side authentication logic that can be 
reproduced by unauthenticated users. An attacke |
| CVE-2026-73125 | 9.8 | 2026-08-28 | Ebyte device web management interface does not consistently enforce 
authentication before granting access to administra |
| CVE-2026-73809 | 7.5 | 2026-08-28 | A cleartext transmission of sensitive information vulnerability exists 
in certain Ebyte gateway products. The web manag |
| CVE-2026-75418 | 7.5 | 2026-08-28 | A path traversal vulnerability exists in the built-in preview/development web server of Lektor <3.3.14 on Windows. An at |
| CVE-2026-75419 | 8.8 | 2026-08-28 | go-wind-cms (GoWind) before 1.0.0 has a missing authorization vulnerability. The NewAuthorizer() function in app/admin/s |
| CVE-2026-75813 | 7.5 | 2026-08-28 | Certain configuration endpoints may lack proper server-side 
authorization checks, allowing unauthorized users to access |
| CVE-2026-75814 | 8.8 | 2026-08-28 | The Ebyte device does not adequately verify the origin or authenticity of 
requests submitted to the web management inte |
| CVE-2026-76060 | 8.8 | 2026-08-28 | An authenticated OS command injection vulnerability exists in ZoneMinder's event export functionality. The exportFile HT |
| CVE-2026-76179 | 9.8 | 2026-08-28 | An improper protection of authentication tokens vulnerability exists in 
certain Ebyte gateway products. Authentication  |
| CVE-2026-76940 | 7.5 | 2026-08-28 | The affected Ebyte device does not restrict repeated authentication 
attempts through rate limiting or account lockout m |
| CVE-2026-76943 | 9.8 | 2026-08-28 | Xiiaozet LK100Wt contains an authentication weakness within an 
administrative service that may allow an attacker to byp |
| CVE-2026-76945 | 7.5 | 2026-08-28 | The affected Ebyte device relies on client-managed authentication tokens
 without sufficient server-side validation. An  |
| CVE-2026-77977 | 8.1 | 2026-08-28 | Ebyte gateway product's vendor configuration utility does not require authentication before 
allowing certain disruptive |
| CVE-2026-78037 | 8.8 | 2026-08-28 | Xiiaozet LK100W is vulnerable to OS command injection through its 
web-based management interface. An authenticated atta |
| CVE-2026-78239 | 9.8 | 2026-08-28 | Xiiaozet LK100W exposes a critical management function that can be 
invoked without authentication, allowing a remote at |
| CVE-2026-82072 | 8.8 | 2026-08-28 | Out of bounds read in V8 in Google Chrome prior to 151.0.7922.72 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-38820 | 8.3 | 2026-08-28 | openNDS before 11.0.0 is susceptible to unauthenticated OS command execution via shell command injection through the fas |
| CVE-2026-38821 | 7.1 | 2026-08-28 | A heap-based buffer overflow vulnerability exists in openNDS before 11.0.0 that allows an unauthenticated attacker on th |
| CVE-2026-38822 | 7.6 | 2026-08-28 | In openNDS before 11.0.0, the client_params.sh script, invoked by the openNDS daemon to serve the authenticated client s |
| CVE-2026-61800 | 9.1 | 2026-08-28 | Wazuh is an open-source security platform providing unified XDR and SIEM protection for endpoints and cloud workloads. I |
| CVE-2026-18324 | 7.2 | 2026-08-28 | The Forminator Forms – Contact Form, Payment Form & Custom Form Builder plugin for WordPress is vulnerable to Stored Cro |
| CVE-2026-18978 | 7.2 | 2026-08-28 | The LiteSpeed Cache plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Comment Content in all version |
| CVE-2026-18983 | 7.5 | 2026-08-28 | The One User Avatar \| User Profile Picture plugin for WordPress is vulnerable to Stored Cross-Site Scripting in all vers |
| CVE-2026-76053 | 7.2 | 2026-08-28 | The TranslatePress – Translate Multilingual sites with AI Translation plugin for WordPress is vulnerable to Stored Cross |
| CVE-2026-77365 | 7.2 | 2026-08-28 | The Optimole – Optimize Images \| Convert WebP & AVIF \| CDN & Lazy Load \| Image Optimization plugin for WordPress is vuln |
| CVE-2026-82082 | 9.8 | 2026-08-28 | NUMail developed by Green-Computing has an OS Command Injection vulnerability. Unauthenticated remote attackers can inje |
| CVE-2026-14558 | 7.2 | 2026-08-28 | The User Frontend  WordPress plugin before 4.3.10 does not properly validate field type definitions and deserialises use |
| CVE-2026-19084 | 7.5 | 2026-08-28 | The shared-files-pro WordPress plugin before 1.7.70 does not validate the file path supplied when creating a featured im |
| CVE-2026-19423 | 8.1 | 2026-08-28 | The Ultimate Member  WordPress plugin before 2.13.0 does not validate a submitted role selection when it cannot resolve  |
| CVE-2026-40541 | 9.0 | 2026-08-28 | An improper neutralization of input during web page generation ('Cross-site Scripting') vulnerability in extract domain  |
| CVE-2026-5097 | 7.5 | 2026-08-28 | The wpForo Forum plugin for WordPress is vulnerable to SQL Injection via the 'referer' parameter in all versions up to,  |
| CVE-2026-6286 | 7.2 | 2026-08-28 | The Booking for Appointments and Events Calendar – Amelia plugin for WordPress is vulnerable to Stored Cross-Site Script |
| CVE-2026-76581 | 9.8 | 2026-08-28 | The WPMU DEV Dashboard plugin for WordPress is vulnerable to Authentication Bypass in all versions up to, and including, |
| CVE-2026-78032 | 9.8 | 2026-08-28 | SOY CMS  contains an issue with deserialization of untrusted data. An arbitrary code may be executed by an attacker with |
| CVE-2026-79996 | 7.2 | 2026-08-28 | The User Registration & Membership  WordPress plugin before 5.2.6 does not perform a capability check when saving its lo |
| CVE-2026-27852 | 7.5 | 2026-08-28 | An attacker that can send mail to a user can craft a message whose headers contain a very large number of email addresse |
| CVE-2026-33605 | 7.5 | 2026-08-28 | An unauthenticated attacker can crash the ManageSieve login process by sending a small malformed command before authenti |
| CVE-2026-40018 | 7.4 | 2026-08-28 | None None None No publicly available exploits are known. |
| CVE-2026-42007 | 9.1 | 2026-08-28 | An attacker that has valid credentials can use a Sieve script with the editheader extension to trigger a use-after-free  |
| CVE-2026-42391 | 7.5 | 2026-08-28 | An unauthenticated attacker can send an IMAP ID command with a very large number of parameters before logging in, which  |
| CVE-2026-73208 | 7.4 | 2026-08-28 | An attacker that holds a token intended for a different purpose can authenticate, because when an OAuth2 token response  |
| CVE-2026-82222 | 10.0 | 2026-08-28 | Deserialization of Untrusted Data vulnerability in Liquid Web / StellarWP GiveWP allows Object Injection.

This issue af |
| CVE-2026-82234 | 8.2 | 2026-08-28 | SiYuan versions before v3.8.1 contain a server-side request forgery vulnerability in the http_request and web_fetch agen |
| CVE-2026-82239 | 8.1 | 2026-08-28 | Budibase before 3.41.3 fails to enforce per-table role restrictions on the POST /api/datasources/query endpoint, allowin |
| CVE-2026-82240 | 8.1 | 2026-08-28 | Budibase before 3.41.3 fails to validate app-scoped builder role assignments in the public user create and update endpoi |
| CVE-2026-82241 | 7.1 | 2026-08-28 | Budibase backend-core (@budibase/backend-core, as used by @budibase/server) omits the shared address space range 100.64. |
| CVE-2026-82242 | 7.7 | 2026-08-28 | Budibase versions before 3.41.3 contain a missing authorization vulnerability in the POST /api/resources/duplicate endpo |
| CVE-2026-82243 | 7.6 | 2026-08-28 | Budibase Server before 3.41.3 contains a server-side request forgery vulnerability in the datasource verify endpoint tha |
| CVE-2026-82244 | 9.1 | 2026-08-28 | Budibase versions before 3.41.3 contain a remote code execution vulnerability in plugin handling that allows authenticat |
| CVE-2026-82245 | 8.1 | 2026-08-28 | Budibase before 3.41.3 fails to enforce role-based authorization on license management endpoints, allowing any authentic |
| CVE-2026-82246 | 7.1 | 2026-08-28 | Budibase Server before 3.41.3 contains a server-side request forgery vulnerability in the query import endpoint that fai |
| CVE-2026-82247 | 7.5 | 2026-08-28 | gitoxide's gix-url crate (<= 0.32.0, fixed in 0.37.1) uses a hand-rolled URL parser that does not treat '?' or '#' as te |
| CVE-2026-82251 | 7.5 | 2026-08-28 | gitoxide before 0.52.1 fails to validate submodule names from .gitmodules configuration, allowing path traversal when de |
| CVE-2026-82252 | 7.5 | 2026-08-28 | gitoxide before 0.52.1 follows symlinks when reading the worktree .gitmodules file, allowing attackers to inject out-of- |
| CVE-2026-82253 | 7.5 | 2026-08-28 | gitoxide (Rust crates gix <= 0.72.0 and gix-validate <= 0.10.0) contains a path traversal vulnerability. The submodule n |
| CVE-2026-82254 | 7.5 | 2026-08-28 | gitoxide before 0.69.0 contains unchecked array indexing in delta application and uncapped allocation from attacker-cont |
| CVE-2026-82259 | 7.5 | 2026-08-28 | SvelteKit versions from 2.49.0 through 2.53.2 (fixed in 2.53.3) contain a deserialization expansion issue in the experim |
| CVE-2026-82260 | 7.5 | 2026-08-28 | SvelteKit (@sveltejs/kit) versions >=2.49.0 and <=2.52.1 with experimental remote functions (experimental.remoteFunction |
| CVE-2026-82261 | 7.5 | 2026-08-28 | SvelteKit (@sveltejs/kit) versions >=2.49.0 and <=2.52.1 with experimental remote functions and form enabled contain a C |
| CVE-2026-5934 | 7.2 | 2026-08-28 | The WP Rocket plugin for WordPress is vulnerable to Stored Cross-Site Scripting in versions up to, and including, 3.21.0 |
| CVE-2026-6176 | 7.2 | 2026-08-28 | The Customer Reviews for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the aggregate |
| CVE-2026-81019 | 7.4 | 2026-08-28 | wolfProvider before 1.2.2 generates the 8-byte explicit AES-GCM nonce once when the TLS write key is set and never incre |
| CVE-2026-81020 | 7.4 | 2026-08-28 | wolfEngine before 1.4.1 generates the 8-byte explicit AES-GCM nonce once when the TLS write key is set and never increme |
| CVE-2026-81285 | 7.5 | 2026-08-28 | Unauthenticated Denial of Service Attack in Smush Image Compression and Optimization <= 4.2.0 versions. |
| CVE-2026-81757 | 7.2 | 2026-08-28 | Author Remote Code Execution (RCE) in Rank Math SEO <= 1.0.276 versions. |
| CVE-2026-81760 | 7.1 | 2026-08-28 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Crocoblock JetEngi |
| CVE-2026-81767 | 7.5 | 2026-08-28 | Unauthenticated Broken Access Control in Simple Payment <= 2.5.2 versions. |
| CVE-2026-82227 | 8.5 | 2026-08-28 | Contributor SQL Injection in WPBulky <= 1.2.2 versions. |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2023-49105 | ownCloud / ownCloud | 2026-08-27 | 2026-08-30 | Unknown |
| CVE-2026-53362 | Linux / Kernel | 2026-08-27 | 2026-08-30 | Unknown |
| CVE-2026-66384 | JFrog / Artifactory | 2026-08-27 | 2026-09-10 | Unknown |
| CVE-2021-23758 | Ajax.NET Professional / Ajax.NET Professional | 2026-08-26 | 2026-09-09 | Unknown |
| CVE-2015-3246 | Red Hat / Libuser | 2026-08-26 | 2026-09-09 | Unknown |
| CVE-2015-5287 | Red Hat / Automatic Bug Reporting Tool | 2026-08-26 | 2026-09-09 | Unknown |
| CVE-2022-0995 | Linux / Kernel | 2026-08-26 | 2026-09-09 | Unknown |
| CVE-2026-8452 | Citrix / NetScaler ADC and NetScaler Gateway | 2026-08-26 | 2026-08-29 | Unknown |
| CVE-2019-1068 | Microsoft / SQL Server | 2026-08-26 | 2026-08-29 | Unknown |
| CVE-2026-60004 | Gitea / Gitea | 2026-08-25 | 2026-08-28 | Unknown |
| CVE-2026-21962 | Oracle / HTTP Server and Oracle Weblogic Server Proxy Plug-in | 2026-08-24 | 2026-08-27 | Unknown |
| CVE-2026-73570 | Synacor / Zimbra Collaboration Suite (ZCS) | 2026-08-21 | 2026-08-24 | Unknown |

---

*Total entries in CISA KEV catalog: 1685*