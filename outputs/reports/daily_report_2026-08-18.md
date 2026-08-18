# Vulnerability Intelligence Report

**Date:** 2026-08-18  
**Generated:** 2026-08-18T08:34:51Z  

## Pipeline Warnings

- summarizer failed: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}, 'request_id': 'req_011Ce9uZBSggLkvdZMF3escU'}

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
| CVE-2026-74845 | 8.8 | 2026-08-17 | Official Document Management System developed by 2100 Technology has an Arbitrary File Upload vulnerability, allowing au |
| CVE-2026-74798 | 8.7 | 2026-08-17 | SiYuan kernel before v3.7.4 contains a path traversal vulnerability in the database_clean MCP tool. The tool performs on |
| CVE-2026-74799 | 9.3 | 2026-08-17 | SiYuan before 3.7.4 registers Go net/http/pprof debug endpoints including heap and goroutine dumps without authenticatio |
| CVE-2026-74800 | 9.0 | 2026-08-17 | SiYuan before v3.7.4 fails to set Content-Disposition and X-Content-Type-Options headers when serving arbitrary file ass |
| CVE-2026-74801 | 8.2 | 2026-08-17 | SiYuan before 3.7.4 fails to properly escape workspace directory paths when constructing command-line arguments for the  |
| CVE-2026-74802 | 8.2 | 2026-08-17 | SiYuan versions before 3.7.4 contain a cross-site WebSocket hijacking vulnerability in the admin-only /ws/network/proxy  |
| CVE-2026-74868 | 7.5 | 2026-08-17 | SiYuan versions before 3.7.4 contain an unthrottled brute-force vulnerability in the Publish Service Basic Auth implemen |
| CVE-2026-74869 | 7.7 | 2026-08-17 | stoatchat before 0.15.0 contains a missing authorization vulnerability in the Subscribe message handler that allows auth |
| CVE-2026-74872 | 9.8 | 2026-08-17 | openssl_encrypt versions before 1.4.0 contain an arbitrary code execution vulnerability in the Whirlpool hash implementa |
| CVE-2026-74874 | 7.5 | 2026-08-17 | openssl_encrypt versions before 1.4.0 use Python's non-cryptographic random module for steganographic pixel selection in |
| CVE-2026-74875 | 9.8 | 2026-08-17 | openssl_encrypt versions before 1.4.0 silently skip JSON schema validation when the jsonschema library is not installed, |
| CVE-2026-74876 | 9.8 | 2026-08-17 | openssl_encrypt versions before 1.4.0 contain a vulnerability in PublicKeyBundle.from_dict() that creates key bundles fr |
| CVE-2026-74877 | 8.8 | 2026-08-17 | openssl_encrypt versions before 1.4.0 contain a missing ownership verification vulnerability in the revoke_key method th |
| CVE-2026-74878 | 9.8 | 2026-08-17 | openssl_encrypt versions before 1.4.0 use an in-memory rate limiter for TOTP brute-force protection that is not shared a |
| CVE-2026-74879 | 7.5 | 2026-08-17 | openssl_encrypt versions before 1.4.0 contain an information disclosure vulnerability in the /ready endpoint that return |
| CVE-2026-74880 | 9.8 | 2026-08-17 | openssl_encrypt versions before 1.4.0 accept refresh tokens as URL query parameters in keyserver and telemetry server ro |
| CVE-2026-74882 | 7.5 | 2026-08-17 | openssl_encrypt versions before 1.4.0 contain an insecure default configuration that trusts the entire RFC 1918 private  |
| CVE-2026-74883 | 8.8 | 2026-08-17 | openssl_encrypt versions before 1.4.0 contain a sandbox bypass vulnerability where the plugin sandbox fails to restrict  |
| CVE-2026-74884 | 7.5 | 2026-08-17 | openssl_encrypt versions before 1.4.0 contain a path traversal vulnerability in the _is_safe_path method where the plugi |
| CVE-2026-74886 | 9.8 | 2026-08-17 | openssl_encrypt versions before 1.4.0 contain a plugin sandbox bypass vulnerability where the PluginImportGuard blocks a |
| CVE-2026-74888 | 7.5 | 2026-08-17 | openssl_encrypt versions before 1.4.0 use a non-standard PBKDF2 key derivation construction with iterations=1 per call i |
| CVE-2026-74889 | 9.8 | 2026-08-17 | openssl_encrypt versions before 1.4.0 use HKDF with no salt and static info parameter in key normalization functions, re |
| CVE-2026-74891 | 9.8 | 2026-08-17 | openssl_encrypt versions before 1.4.0 contain hardcoded database credentials in standalone server configuration files. A |
| CVE-2026-74892 | 7.5 | 2026-08-17 | openssl_encrypt versions before 1.4.0 contain a hardcoded default secret key in the standalone telemetry server configur |
| CVE-2026-74893 | 8.8 | 2026-08-17 | openssl_encrypt versions before 1.4.0 contain hardcoded default JWT signing secrets in config.py that pass validation ch |
| CVE-2026-74894 | 9.8 | 2026-08-17 | openssl_encrypt before 1.4.0 contains an authentication bypass vulnerability in the verify_api_token function that accep |
| CVE-2026-74895 | 9.8 | 2026-08-17 | openssl_encrypt versions before 1.4.0 fail to apply sandbox restrictions in the default process isolation mode for plugi |
| CVE-2026-74896 | 9.8 | 2026-08-17 | openssl_encrypt versions before 1.4.0 contain a sandbox escape vulnerability in the DangerousPatternVisitor AST analyzer |
| CVE-2026-74899 | 9.8 | 2026-08-17 | openssl_encrypt versions before 1.4.0 contain a sandbox escape vulnerability in IsolatedPluginExecutor that exposes Pyth |
| CVE-2026-74900 | 9.8 | 2026-08-17 | openssl_encrypt versions before 1.4.0 contain a critical vulnerability in pqc.py where KEM decapsulation failures silent |
| CVE-2026-74901 | 9.8 | 2026-08-17 | openssl_encrypt versions before 1.4.0 contain an authentication bypass vulnerability in pqc.py where AES-GCM decryption  |
| CVE-2026-74843 | 10.0 | 2026-08-17 | A vulnerability was determined in Wavlink WN531P3 and WN535M1 V250922. Affected by this vulnerability is the function st |
| CVE-2026-14564 | 9.0 | 2026-08-17 | Insufficiently Protected Credentials vulnerability in Innotim Software Telecommunications and Consulting Trade Ltd. Co.  |
| CVE-2026-16467 | 7.5 | 2026-08-17 | Missing Authorization vulnerability in Dolusoft Software Technologies Fortilogger allows Accessing Functionality Not Pro |
| CVE-2026-74997 | 8.8 | 2026-08-17 | In Roundcube Webmail before 1.6.18 and 1.7.x before 1.7.3, the cmd_learn driver of the markasjunk plugin is subject to r |
| CVE-2026-74998 | 7.2 | 2026-08-17 | In Roundcube Webmail before 1.6.18 and 1.7.x before 1.7.3, responses from the CSS (Cascading Style Sheets) proxy were no |
| CVE-2026-75002 | 7.1 | 2026-08-17 | In Roundcube Webmail before 1.6.18 and 1.7.x before 1.7.3, mail search and LITERAL+ byte-count desynchronization could l |
| CVE-2026-15218 | 7.9 | 2026-08-17 | A flaw was found in the maas-api and maas-controller ServiceAccounts within Red Hat OpenShift AI. These ServiceAccounts  |
| CVE-2026-16137 | 7.2 | 2026-08-17 | In Progress ShareFile Storage Zones Controller v5.12.5 and below, a party with valid zone credentials can perform path t |
| CVE-2026-16138 | 8.0 | 2026-08-17 | In Progress ShareFile Storage Zones Controller v5.12.5 and below versions, unsafe deserialization of untrusted file meta |
| CVE-2026-16139 | 7.2 | 2026-08-17 | In Progress ShareFile Storage Zones Controller versions <= 5.12.5 and <= 6.0.2, an authenticated zone administrator can  |
| CVE-2026-16471 | 7.5 | 2026-08-17 | Missing Authorization vulnerability in Dolusoft Software Technologies Sonlogger allows Accessing Functionality Not Prope |
| CVE-2026-19693 | 8.1 | 2026-08-17 | extract-zip through 2.0.1 containment-checks only the parent directory of each archive entry and never the entry's own f |
| CVE-2026-56090 | 7.3 | 2026-08-17 | Dell ObjectScale, versions prior to 4.3.0.1, contain(s) an Uncontrolled Search Path Element vulnerability. A low privile |
| CVE-2026-56685 | 7.3 | 2026-08-17 | Dell ObjectScale, versions prior to 4.3.0.1, contain(s) an Improper Neutralization of Special Elements used in an OS Com |
| CVE-2026-56686 | 7.8 | 2026-08-17 | Dell ObjectScale, versions prior to 4.3.0.1, contain(s) an Improper Neutralization of Special Elements used in an OS Com |
| CVE-2026-59909 | 7.1 | 2026-08-17 | Dell ObjectScale, versions prior to 4.3.0.1, contain(s) a Path Traversal vulnerability. A low privileged attacker with l |
| CVE-2026-59910 | 7.8 | 2026-08-17 | Dell ObjectScale, versions prior to 4.3.0.1, contain(s) an Improper Neutralization of Special Elements used in an OS Com |
| CVE-2026-71566 | 9.3 | 2026-08-17 | FakeFish handles incoming credentials by passing them down
 to scripts. This works for real hardware because in the end  |
| CVE-2026-71567 | 7.7 | 2026-08-17 | In openshift-metal3/fakefish there is a repeated pattern in some of the scripts where shell variables
 are injected with |
| CVE-2026-55674 | 9.3 | 2026-08-17 | Discourse is an open-source discussion platform. Prior to 2026.1.6, 2026.5.2, 2026.6.1, and 2026.7.0, an unauthenticated |
| CVE-2026-64859 | 9.1 | 2026-08-17 | New API is a large language mode (LLM) gateway and artificial intelligence (AI) asset management system. Prior to 1.0.0- |
| CVE-2026-64868 | 7.5 | 2026-08-17 | New API is a large language mode (LLM) gateway and artificial intelligence (AI) asset management system. Prior to 1.0.0- |
| CVE-2026-71479 | 9.1 | 2026-08-17 | New API is a large language mode (LLM) gateway and artificial intelligence (AI) asset management system. Prior to 1.0.0- |
| CVE-2026-73646 | 7.5 | 2026-08-17 | PostCSS takes a CSS file and provides an API to analyze and modify its rules by transforming the rules into an Abstract  |
| CVE-2026-75044 | 8.1 | 2026-08-17 | In JetBrains YouTrack before 2025.3.156085, 
2026.1.13914, 
2026.2.18095 missing authorisation allowed an authenticated  |
| CVE-2026-75045 | 9.1 | 2026-08-17 | In JetBrains YouTrack before 2025.3.156085, 
2026.1.13913, 
2026.2.18112 an unauthenticated attacker could download data |
| CVE-2026-75048 | 8.2 | 2026-08-17 | In JetBrains YouTrack before 2026.2.18068 stored XSS via the fenced code-block language label was possible |
| CVE-2026-75050 | 7.1 | 2026-08-17 | In JetBrains YouTrack before 2026.1.13901, 
2026.2.17950 doS attack was possible via crafted type parameters |
| CVE-2026-75051 | 8.1 | 2026-08-17 | In JetBrains YouTrack before 2026.2.17917 unauthorised project transfer between organisations was possible |
| CVE-2026-75056 | 7.8 | 2026-08-17 | In JetBrains IntelliJ IDEA before 2026.2.1 rCE via Markdown export tool was possible |
| CVE-2026-75060 | 8.4 | 2026-08-17 | In JetBrains PyCharm before 2026.2.1 code execution was possible via unauthenticated Jupyter MCP tools |
| CVE-2026-9771 | 8.8 | 2026-08-17 | The flash_copy() system call is verified by z_vrfy_flash_copy() in drivers/flash/flash_util.c. On builds with CONFIG_USE |
| CVE-2026-33437 | 8.1 | 2026-08-17 | Stirling-PDF is a locally hosted web application that facilitates various operations on PDF files. Prior to 2.0.0, the G |
| CVE-2026-46345 | 8.4 | 2026-08-17 | compliance-trestle is a tooling platform for managing compliance as code. Prior to versions 3.12.2 and 4.0.3, the `-o/-- |
| CVE-2026-50768 | 9.8 | 2026-08-17 | File Upload vulnerability in T-Systems International GmbH ImageMaster Version: 9.14.2.8.1 allows a remote attacker to ex |
| CVE-2026-51346 | 9.1 | 2026-08-17 | SQL Injection vulnerability in StudIP 6.0.x before 6.0.3 and 5.4.x before 5.4.12 allows a remote attacker to execute arb |
| CVE-2026-59893 | 7.5 | 2026-08-17 | sqlparse is a non-validating SQL parser module for Python. Prior to 0.6.0, SQL_REGEX in sqlparse/keywords.py and the per |
| CVE-2026-59902 | 7.5 | 2026-08-17 | Netty is an asynchronous, event-driven network application framework. Prior to 4.1.137.Final and 4.2.17.Final, io.netty. |
| CVE-2026-62982 | 8.8 | 2026-08-17 | Glances is an open-source system cross-platform monitoring tool. From 4.5.2 until 4.5.6, _sanitize_mustache_dict() in gl |
| CVE-2026-71979 | 7.5 | 2026-08-17 | INDI (Instrument Neutral Distributed Interface) indiserver through 2.2.4.2, fixed in commit 96bbd7f, contains a stack bu |
| CVE-2026-71980 | 7.5 | 2026-08-17 | Belledonne Communications bcg729 through 1.1.2 contains an out-of-bounds read vulnerability in the decodeSIDframe() func |
| CVE-2026-73522 | 7.5 | 2026-08-17 | COVESA Open1722 through 0.9.2 contains a stack buffer overflow vulnerability that allows unauthenticated remote attacker |
| CVE-2026-73523 | 7.5 | 2026-08-17 | COVESA Open1722 through 0.9.2 contains an integer truncation vulnerability in acf-can-listener.c that allows unauthentic |
| CVE-2026-45698 | 7.5 | 2026-08-17 | Netatalk is a Free and Open Source file server suite for Unix-like operating systems. In versions 3.1.19 through 4.4.2,  |
| CVE-2026-66792 | 9.9 | 2026-08-17 | A flaw was found in the multicloud-operators-subscription component. This vulnerability allows a user on a managed clust |
| CVE-2026-74238 | 7.5 | 2026-08-17 | TIER IV Nebula through 1.2.0 contains an out-of-bounds read vulnerability in the Vlp32Decoder::unpack() function that al |
| CVE-2026-19478 | 9.4 | 2026-08-17 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 18.2 before 18.11.11, 19.0 before 19.0.8, 19. |
| CVE-2026-19650 | 7.1 | 2026-08-17 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 18.2 before 18.11.11, 19.0 before 19.0.8, 19. |
| CVE-2026-54758 | 7.8 | 2026-08-17 | Notepad++ is a free and open-source source code editor. Prior to 8.9.7, the expandNppEnvironmentStrs function in PowerEd |
| CVE-2026-57233 | 8.1 | 2026-08-17 | Notepad++ is a free and open-source source code editor. Prior to 8.9.7, the WinGup decompress function joins untrusted Z |
| CVE-2026-57485 | 8.5 | 2026-08-17 | Stirling-PDF is a locally hosted web application that facilitates various operations on PDF files. Prior to 2.9.0, the / |
| CVE-2026-68005 | 7.5 | 2026-08-17 | An issue in ACME mini_httpd 1.30 and prior allows a remote attacker to cause a denial of service via the HTTP request he |
| CVE-2026-70495 | 8.8 | 2026-08-17 | A flaw was found in search-v2-operator. This component's `search-serviceaccount` has overly broad permissions, allowing  |
| CVE-2026-71472 | 9.1 | 2026-08-17 | A flaw was found in acm-search-v2-rhel9. This vulnerability allows an authenticated attacker, such as a hub administrato |
| CVE-2026-74234 | 7.7 | 2026-08-17 | Legora before 2026-08-14 contains a cross-site scripting vulnerability that allows attackers to achieve arbitrary JavaSc |
| CVE-2026-75014 | 7.3 | 2026-08-17 | A flaw has been found in SourceCodester Pet Grooming Management Software 1.0. This vulnerability affects unknown code of |
| CVE-2026-19589 | 7.1 | 2026-08-17 | Packer up to 1.15.4 is vulnerable to an issue in the third-party plugin installer that may allow unintended file system  |
| CVE-2026-34398 | 7.8 | 2026-08-17 | FreeCAD is a free and open-source multiplatform 3D parametric modeler. From 0.19 until 1.1.1, src/Mod/BIM/bimcommands/Bi |
| CVE-2026-34399 | 7.8 | 2026-08-17 | FreeCAD is a free and open-source multiplatform 3D parametric modeler. From 0.19 until 1.1.1, FreeCAD's BIM Workbench co |
| CVE-2026-34789 | 7.0 | 2026-08-17 | FreeCAD is a free and open-source multiplatform 3D parametric modeler. Prior to 1.1.2, src/App/PropertyPythonObject.cpp  |
| CVE-2026-47686 | 9.9 | 2026-08-17 | vm2 is an open source vm/sandbox for Node.js. Prior to 3.11.6, handleException() in lib/setup-sandbox.js sanitizes Suppr |
| CVE-2026-47698 | 9.8 | 2026-08-17 | vm2 is an open source vm/sandbox for Node.js. Prior to 3.11.6, lib/bridge.js and lib/setup-sandbox.js fail to block stac |
| CVE-2026-54356 | 7.1 | 2026-08-17 | Budibase is an open-source low-code platform. Prior to 3.41.3, POST /api/attachments/:datasourceId/url in packages/serve |
| CVE-2026-63409 | 8.2 | 2026-08-17 | Deskflow is a keyboard and mouse sharing app. From 1.17.0 until continuous build 1.26.0.296, a malicious Deskflow server |
| CVE-2026-64657 | 8.4 | 2026-08-17 | Budibase is an open-source low-code platform. Prior to 3.39.19, the PostgreSQL datasource connector in packages/server/s |
| CVE-2026-65640 | 8.8 | 2026-08-17 | WordPress is vulnerable to a remote code execution vulnerability via malicious Postscript file upload by an Author level |
| CVE-2026-65822 | 7.6 | 2026-08-17 | ERPNext is a free and open source Enterprise Resource Planning tool. Prior to 15.116.0 and 16.23.0, erpnext/selling/repo |
| CVE-2026-65832 | 8.2 | 2026-08-17 | Deskflow is a keyboard and mouse sharing app. Prior to continuous build 1.26.0.299, a remote unauthenticated Deskflow se |
| CVE-2026-65974 | 9.9 | 2026-08-17 | ERPNext is a free and open source Enterprise Resource Planning tool. Prior to 15.111.0 and 16.22.0, limited authenticate |
| CVE-2026-66795 | 9.1 | 2026-08-17 | A flaw was found in the managedcluster-import-controller. The Certificate Signing Request (CSR) auto-approval logic impr |
| CVE-2026-71518 | 7.5 | 2026-08-17 | Typemill before 2.26.0 contains an authorization bypass vulnerability in the media file download route that allows unaut |
| CVE-2026-73410 | 8.5 | 2026-08-17 | Budibase is an open-source low-code platform. Prior to 3.40.0, packages/backend-core/src/utils/outboundFetch.ts pinned a |
| CVE-2026-75103 | 8.8 | 2026-08-17 | Crawlab fails to verify user ownership or administrative role on the password-change endpoint, allowing any authenticate |
| CVE-2026-75105 | 7.5 | 2026-08-17 | phpIPAM through 1.8.1 fails to verify that a requested IP address belongs to the subnet a temporary share token was issu |
| CVE-2026-75106 | 9.1 | 2026-08-17 | OpnForm derives editable-submission secrets from sequential row identifiers using Hashids with an empty default salt, al |
| CVE-2026-75109 | 7.1 | 2026-08-17 | Determined fails to authorize requests on the generic task kill, pause, and unpause endpoints in the API handlers. Authe |
| CVE-2026-75110 | 9.8 | 2026-08-17 | MemOS is a memory operating system for LLMs and AI agents. In deployments where authentication is enabled (AUTH_ENABLED= |
| CVE-2026-75111 | 7.5 | 2026-08-17 | Evidently UI fails to properly validate the filename parameter in the dataset materialization endpoint, allowing unauthe |
| CVE-2026-75479 | 7.5 | 2026-08-17 | JimuReport contains an authentication bypass vulnerability in the report folder template listing endpoint that allows un |
| CVE-2026-75481 | 8.8 | 2026-08-17 | SkyPilot fails to validate that authenticated users are entitled to grant administrator roles when updating service acco |
| CVE-2026-75482 | 7.5 | 2026-08-17 | SWE-agent's trajectory inspector (sweagent inspector), confirmed in v1.1.0, is an HTTP server that joins request paths t |
| CVE-2026-45790 | 8.0 | 2026-08-17 | Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.6, Dokploy's organization.inviteMember tRPC |
| CVE-2026-56677 | 8.6 | 2026-08-17 | 9Router is an AI router & token saver. In 0.5.4 and earlier, the POST /api/auth/oidc/test endpoint in src/app/api/auth/o |
| CVE-2026-64849 | 9.3 | 2026-08-17 | MLflow is an open source AI engineering platform for agents, large language models, and machine learning models. Prior t |
| CVE-2026-69148 | 7.1 | 2026-08-17 | MLflow is an open source AI engineering platform for agents, large language models, and machine learning models. Prior t |
| CVE-2026-71424 | 9.6 | 2026-08-17 | Onyx is an open-source AI platform. Prior to 3.1.10, 3.2.14, and 4.0.0, Onyx's GET /api/mcp/servers and GET /api/mcp/ser |
| CVE-2026-9816 | 8.3 | 2026-08-17 | Mattermost versions 11.7.x <= 11.7.6, 10.11.x <= 10.11.21, 11.8.x <= 11.8.3 fail to validate BoardMember.Scheme* fields  |
| CVE-2026-75079 | 7.3 | 2026-08-18 | A weakness has been identified in SourceCodester Class and Exam Timetabling System 1.0. This vulnerability affects unkno |
| CVE-2026-75080 | 7.3 | 2026-08-18 | A security vulnerability has been detected in SourceCodester Class and Exam Timetabling System 1.0. This issue affects s |
| CVE-2026-75089 | 7.3 | 2026-08-18 | A weakness has been identified in PHPGurukul Complaint Management System 1.0. Affected by this issue is some unknown fun |
| CVE-2026-75094 | 9.1 | 2026-08-18 | A flaw has been found in COMFAST CF-N1-S 2.6.0.1. This impacts the function sub_44B438 of the file /cgi-bin/mbox-config? |
| CVE-2026-11801 | 7.5 | 2026-08-18 | The WPAdverts – Classifieds Plugin plugin for WordPress is vulnerable to authorization bypass in all versions up to, and |
| CVE-2026-15748 | 9.8 | 2026-08-18 | The Forminator Forms plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 1 |
| CVE-2026-75091 | 7.2 | 2026-08-18 | The Quill Forms \| Conversational Multi Step Forms, Surveys & quizzes plugin for WordPress is vulnerable to Stored Cross- |
| CVE-2026-15371 | 8.1 | 2026-08-18 | Velociraptor's web GUI allows specifying a custom type for columns in tables. The URL type takes the cell value and form |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2025-62593 | Ray-Project / Ray | 2026-08-17 | 2026-08-20 | Unknown |
| CVE-2026-20349 | Cisco / Secure Firewall Adaptive Security Appliance (ASA) and Secure Firewall Threat Defense (FTD)  | 2026-08-11 | 2026-08-14 | Unknown |
| CVE-2026-68820 | Microsoft / Windows Ancillary Function Driver for WinSock  | 2026-08-11 | 2026-08-25 | Unknown |
| CVE-2026-72898 | Metabase / Metabase | 2026-08-11 | 2026-08-14 | Unknown |

---

*Total entries in CISA KEV catalog: 1666*