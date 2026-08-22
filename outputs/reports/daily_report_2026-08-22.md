# Vulnerability Intelligence Report

**Date:** 2026-08-22  
**Generated:** 2026-08-22T08:27:29Z  

## Pipeline Warnings

- summarizer failed: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}, 'request_id': 'req_011CeHUE8773cBzoFU9EDf9W'}

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
| CVE-2026-50112 | 8.8 | 2026-08-21 | SSRF via Metalink Mirror URL Resolution:

An authenticated tenant can register a template pointing to an attacker-contro |
| CVE-2026-61400 | 8.8 | 2026-08-21 | Improper Neutralization of Special Elements used in a Command ('Command Injection') vulnerability in Apache CloudStack's |
| CVE-2026-63046 | 8.8 | 2026-08-21 | Improper Neutralization of Argument Delimiters in a Command ('Argument Injection') vulnerability in Apache InLong. Agent |
| CVE-2026-47827 | 7.5 | 2026-08-21 | Command Injection in BOSH CLI tool on windows in Cloud Foundry allows a remote attacker to execute arbitrary shell comma |
| CVE-2026-77086 | 9.1 | 2026-08-21 | SiYuan before v3.7.4 fails to validate the packageName parameter in Bazaar install and uninstall endpoints, allowing aut |
| CVE-2026-77683 | 9.9 | 2026-08-21 | A security flaw has been discovered in Comfast CF-N1-S 2.6.0.1. Affected by this issue is the function system of the fil |
| CVE-2026-77767 | 7.5 | 2026-08-21 | Reconmap's API applies a fallback authorization policy in apps/api/app/Program.cs that requires an authenticated user ho |
| CVE-2026-59279 | 7.5 | 2026-08-21 | The MCP Streamable HTTP server transport (WebFlux and WebMvc variants) does not place any limit on the number of session |
| CVE-2026-77775 | 8.6 | 2026-08-21 | Headroom's LLM proxy lets a client choose the upstream destination with the x-headroom-base-url request header. _resolve |
| CVE-2026-77776 | 9.1 | 2026-08-21 | Headroom's LLM proxy derives the memory owner from the x-headroom-user-id request header. The header is read directly at |
| CVE-2026-77806 | 9.8 | 2026-08-21 | SPIP before 4.4.21 allows unauthenticated remote attackers to execute arbitrary code, as exploited in the wild in August |
| CVE-2026-48749 | 9.9 | 2026-08-21 | Incus is a system container and virtual machine manager. Prior to version 7.2.0, a specially crafted image can be used t |
| CVE-2026-48750 | 9.9 | 2026-08-21 | Incus is a system container and virtual machine manager. Prior to version 7.2.0, the `record-output` parameter of the `/ |
| CVE-2026-48751 | 9.9 | 2026-08-21 | Incus is a system container and virtual machine manager. Prior to version 7.2.0, instance snapshots ignore the `restrict |
| CVE-2026-48752 | 9.9 | 2026-08-21 | Incus is a system container and virtual machine manager. Prior to version 7.2.0, a specially crafted image or instance b |
| CVE-2026-48753 | 9.9 | 2026-08-21 | Incus is a system container and virtual machine manager. Prior to version 7.1.0, the S3 protocol upload endpoint is vuln |
| CVE-2026-48755 | 9.9 | 2026-08-21 | Incus is a system container and virtual machine manager. Prior to version 7.1.0, improper validation of user-provided ba |
| CVE-2026-48769 | 9.9 | 2026-08-21 | Incus is a system container and virtual machine manager. Prior to version 7.2.0, an arbitrary file write exists in the I |
| CVE-2026-55621 | 7.7 | 2026-08-21 | Incus is a system container and virtual machine manager. Prior to version 7.2.0, missing authorization checks exist for  |
| CVE-2026-55622 | 7.7 | 2026-08-21 | Incus is a system container and virtual machine manager. Prior to version 7.2.0, missing authorization checks exist for  |
| CVE-2026-62867 | 9.9 | 2026-08-21 | Incus is a system container and virtual machine manager. Prior to version 7.3.0, improper validation of user-provided `b |
| CVE-2026-62940 | 9.9 | 2026-08-21 | Incus is a system container and virtual machine manager. Prior to version 7.3.0, when migrating an instance to another c |
| CVE-2026-62941 | 9.9 | 2026-08-21 | Incus is a system container and virtual machine manager. Prior to version 7.3.0, when copying an instance across project |
| CVE-2026-63125 | 9.9 | 2026-08-21 | Incus is a system container and virtual machine manager. Prior to version 7.3.0, an unprivileged, project-confined Incus |
| CVE-2026-63343 | 9.9 | 2026-08-21 | Incus is a system container and virtual machine manager. Prior to version 7.3.0, a malicious image containing a `metadat |
| CVE-2026-77087 | 9.6 | 2026-08-21 | Paperclip before 0.3.1 in default local_trusted mode fails to validate Host headers, allowing attackers to execute arbit |
| CVE-2026-77814 | 7.5 | 2026-08-21 | is_path_trusted in scripts/iib/api.py compares the requested path against each allowed parent directory with path.starts |
| CVE-2026-77815 | 7.5 | 2026-08-21 | to_abs_path in scripts/iib/tool.py normalised the requested path with os.path.normpath, which collapses dot segments but |
| CVE-2026-22681 | 8.5 | 2026-08-21 | OpenViking before 0.3.4 contains a server-side request forgery vulnerability that allows authenticated low-privilege att |
| CVE-2026-49114 | 7.1 | 2026-08-21 | In ONNX before 1.21.0, the 'save_external_data' function builds the external-data file path from the model's external_da |
| CVE-2026-54789 | 7.5 | 2026-08-21 | mod_auth_openidc is an OpenID Certified authentication and authorization module for the Apache 2.x HTTP server that impl |
| CVE-2026-69502 | 10.0 | 2026-08-21 | Server-side request forgery (ssrf) in Azure SQL Database allows an unauthorized attacker to elevate privileges over a ne |
| CVE-2026-75932 | 8.6 | 2026-08-21 | Jet Admin allows an attacker to create a malicious app and connect it to a target user's custom domain, edit the authent |
| CVE-2026-75933 | 7.3 | 2026-08-21 | Jet Admin allows an authenticated attacker to inject JavaScript via the sign-in page's scripts and styles option. Inject |
| CVE-2026-39909 | 8.1 | 2026-08-21 | llama.cpp before b8585 contains a use-after-free vulnerability in the RPC server's GRAPH_RECOMPUTE handler that allows u |
| CVE-2026-41449 | 7.8 | 2026-08-21 | UAC (Unix-like Artifacts Collector) versions prior to 3.3.0 contain a command injection vulnerability in the _run_comman |
| CVE-2026-41450 | 7.8 | 2026-08-21 | UAC (Unix-like Artifacts Collector) versions prior to 3.3.0 contain a command injection vulnerability in the _command_co |
| CVE-2026-41451 | 7.8 | 2026-08-21 | UAC (Unix-like Artifacts Collector) versions prior to 3.3.0 contain a command injection vulnerability in the user substi |
| CVE-2026-55241 | 7.5 | 2026-08-21 | Checkmate is an open-source, self-hosted tool designed to track and monitor server hardware, uptime, response times, and |
| CVE-2026-62674 | 9.0 | 2026-08-21 | Omnigent is an open-source AI agent framework and meta-harness for orchestrating coding agents. Prior to 0.3.0, PUT /ses |
| CVE-2026-62675 | 8.8 | 2026-08-21 | Omnigent is an open-source AI agent framework and meta-harness for orchestrating coding agents. Prior to 0.3.0, multipar |
| CVE-2026-62676 | 7.1 | 2026-08-21 | Omnigent is an open-source AI agent framework and meta-harness for orchestrating coding agents. Prior to 0.3.0, the shar |
| CVE-2026-62677 | 8.8 | 2026-08-21 | Omnigent is an open-source AI agent framework and meta-harness for orchestrating coding agents. Prior to 0.3.0, an authe |
| CVE-2026-71862 | 7.5 | 2026-08-21 | Checkmate is an open-source, self-hosted tool designed to track and monitor server hardware, uptime, response times, and |
| CVE-2026-77234 | 8.8 | 2026-08-21 | Improper input validation in FreeRTOS-Kernel before 11.3.1 might allow an unprivileged task on MPU-enabled ports to exec |
| CVE-2026-77235 | 7.3 | 2026-08-21 | Missing privilege verification in the secure context cleanup handler in FreeRTOS-Kernel before 11.3.1 might allow local  |
| CVE-2026-77236 | 7.3 | 2026-08-21 | Missing minimum size validation in secure context allocation in FreeRTOS-Kernel before 11.3.1 might allow local users to |
| CVE-2026-54071 | 7.8 | 2026-08-21 | BabelDOC is a document translation tool. Prior to 0.6.3, BabelDOC's vendored PDF parser in babeldoc/pdfminer/cmapdb.py d |
| CVE-2026-54682 | 8.2 | 2026-08-21 | DiscordChatExporter saves Discord chat logs to a file. Prior to 2.47.2, HTML exports generated with markdown formatting  |
| CVE-2026-63462 | 7.5 | 2026-08-21 | Unleash is an open-source feature management platform. Prior to 7.5.2, 7.6.5, and 8.0.2, the shared OpenAPI validation e |
| CVE-2026-27462 | 7.5 | 2026-08-21 | Combodo iTop is a web based IT service management tool. Prior to 3.2.3, iTop returns different responses for valid/inval |
| CVE-2026-27490 | 7.5 | 2026-08-21 | Combodo iTop is a web based IT service management tool. Prior to 3.2.3, inline images that are accessible without being  |
| CVE-2026-30819 | 7.3 | 2026-08-21 | Combodo iTop is a web based IT service management tool. Prior to 3.2.3, iTop has a reflected Cross-Site Scripting (XSS)  |
| CVE-2026-30866 | 7.5 | 2026-08-21 | Combodo iTop is a web based IT service management tool. Prior to 3.2.3, unauthenticated users can access uploaded sensit |
| CVE-2026-62960 | 7.4 | 2026-08-21 | Git for Windows is the Windows port of Git. Prior to 2.55.0.windows.4, a malicious remote Git server can advertise a bun |
| CVE-2026-77810 | 9.9 | 2026-08-21 | In the Neptune connector, a user with access to Neptune through Athena Federated Query could gain access to properties i |
| CVE-2026-30826 | 8.0 | 2026-08-21 | Combodo iTop is a web based IT service management tool. Prior to 3.2.3, there is a Reflected Cross-Site Scripting (XSS)  |
| CVE-2026-30865 | 7.1 | 2026-08-21 | Combodo iTop is a web based IT service management tool. Prior to 3.2.3, there is a Reflected Cross-Site Scripting (XSS)  |
| CVE-2026-30890 | 8.0 | 2026-08-21 | Combodo iTop is a web based IT service management tool. Prior to 3.2.3, there is a Reflected Cross-Site Scripting (XSS)  |
| CVE-2026-31803 | 8.0 | 2026-08-21 | Combodo iTop is a web based IT service management tool. Prior to 3.2.3, 3.2.3, there is a Reflected Cross-Site Scripting |
| CVE-2026-31880 | 8.0 | 2026-08-21 | Combodo iTop is a web based IT service management tool. Prior to 3.2.3, there is a Reflected Cross-Site Scripting (XSS)  |
| CVE-2026-50538 | 8.8 | 2026-08-21 | LibVNCClient is a library for easy implementation of a VNC client. In versions 0.9.12 through 0.9.15, a malicious (or ma |
| CVE-2026-54457 | 7.7 | 2026-08-21 | TensorZero is an open-source LLMOps platform that unifies an LLM gateway, observability, evaluation, optimization, and e |
| CVE-2026-61539 | 10.0 | 2026-08-21 | Xinference is an inference API for running open-source, speech, and multimodal models. In 2.5.0 and earlier, Xinference  |
| CVE-2026-61824 | 8.2 | 2026-08-21 | Defuddle cleans up HTML pages. Prior to 0.19.1, site extractors interpolate page-derived image alt and src values, og:im |
| CVE-2026-62283 | 9.9 | 2026-08-21 | Nezha Monitoring is a self-hostable, lightweight, servers and websites monitoring and O&M tool. Nezha versions 1.14.13 t |
| CVE-2026-62316 | 8.8 | 2026-08-21 | Microsoft UFO open-source framework for intelligent automation across devices and platforms. Prior to 3.0.8, ufo/client/ |
| CVE-2026-63135 | 8.2 | 2026-08-21 | YOURLS is a self-hosted, customizable URL shortener written in PHP. From 1.5.1 until 1.10.4, YOURLS stores the HTTP Refe |
| CVE-2026-63421 | 7.5 | 2026-08-21 | Keystone is a content management system for Node.js. Prior to 6.5.3, the findMany resolver in packages/core/src/lib/core |
| CVE-2026-64679 | 8.1 | 2026-08-21 | Atlantis is a self-hosted golang application that listens for Terraform pull request events via webhooks. From 0.19.8 un |
| CVE-2026-68508 | 7.8 | 2026-08-21 | Hydra is a framework for elegantly configuring complex applications. Prior to 1.3.4, hydra.utils.instantiate() resolves  |
| CVE-2026-76904 | 9.8 | 2026-08-21 | GeoTools is an open source Java library that provides tools for geospatial data. Starting in version 30.5 and prior to v |
| CVE-2026-76905 | 7.5 | 2026-08-21 | kin-openapi is a Go project for handling OpenAPI files. From 0.10.0 until 0.141.0, openapi3filter.convertParseError in o |
| CVE-2026-77219 | 7.1 | 2026-08-21 | GNU Emacs before 31.0.91 contains an integer overflow in the PBM/PPM/PGM image loader that allows an attacker to leak he |
| CVE-2026-77811 | 8.7 | 2026-08-21 | Improper input validation in the dashboards-observability plugin in OpenSearch Dashboards allows a remote authenticated  |
| CVE-2026-31936 | 8.8 | 2026-08-21 | Combodo iTop is a web based IT service management tool. Prior to 3.2.3, users can access to unauthorized object informat |
| CVE-2026-33240 | 8.8 | 2026-08-21 | Combodo iTop is a web based IT service management tool. Prior to 3.2.3, there was a Reflected Cross-Site Scripting (XSS) |
| CVE-2026-34741 | 8.6 | 2026-08-21 | Combodo iTop is a web based IT service management tool. Prior to 3.2.3, authentication bypass allows unauthenticated rem |
| CVE-2026-49849 | 9.1 | 2026-08-21 | xShop is an open-source shop developed in Laravel. An Unrestricted File Upload vulnerability in xShop version 3.0.3 allo |
| CVE-2026-53527 | 8.8 | 2026-08-21 | LeafWiki is a self-hosted wiki. Versions 0.1.0 through 0.10.0 have a privilege escalation vulnerability in the user upda |
| CVE-2026-53528 | 8.8 | 2026-08-21 | LeafWiki is a self-hosted wiki. Versions 0.3.0 through 0.10.0 have a path traversal vulnerability in LeafWiki’s asset re |
| CVE-2026-34948 | 7.7 | 2026-08-21 | Combodo iTop is a web based IT service management tool. Prior to 3.2.3, only classes present in the SELECT clause are pr |
| CVE-2026-53525 | 7.4 | 2026-08-21 | WeeChat (Wee Enhanced Environment for Chat) is a free chat client. In versions 0.3.1 through 4.9.0, the WeeChat relay au |
| CVE-2026-19883 | 8.8 | 2026-08-22 | The WPeMatico RSS Feed Fetcher plugin for WordPress is vulnerable to unauthorized modification of data that can lead to  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-73570 | Synacor / Zimbra Collaboration Suite (ZCS) | 2026-08-21 | 2026-08-24 | Unknown |
| CVE-2026-72530 | TrueConf / Server | 2026-08-20 | 2026-09-03 | Unknown |
| CVE-2026-72529 | TrueConf / Server | 2026-08-20 | 2026-08-23 | Unknown |
| CVE-2026-64849 | MLflow / MLflow | 2026-08-19 | 2026-09-02 | Unknown |
| CVE-2026-33824 | Microsoft / Internet Key Exchange (IKE) Service Extensions | 2026-08-18 | 2026-08-21 | Unknown |
| CVE-2026-59310 | Broadcom / VMware vCenter | 2026-08-18 | 2026-08-21 | Unknown |
| CVE-2026-55040 | Microsoft / SharePoint | 2026-08-18 | 2026-08-21 | Unknown |
| CVE-2026-65400 | Apple / macOS | 2026-08-18 | 2026-08-21 | Unknown |
| CVE-2025-62593 | Ray-Project / Ray | 2026-08-17 | 2026-08-20 | Unknown |

---

*Total entries in CISA KEV catalog: 1674*