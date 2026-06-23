# Vulnerability Intelligence Report

**Date:** 2026-06-23  
**Generated:** 2026-06-23T11:15:53Z  

## Pipeline Warnings

- summarizer failed: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}, 'request_id': 'req_011CcL6aNkyp44UTo4b6hMsZ'}

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
| CVE-2026-11373 | 9.1 | 2026-06-22 | Net::Statsite::Client versions through 1.1.0 for Perl allow metric injections.

Net::Statsite::Client is a client for th |
| CVE-2025-66389 | 7.5 | 2026-06-22 | GitHub Copilot 1.372.0 allows filesystem access outside of a workspace folder (without user approval) via a file-handler |
| CVE-2026-10561 | 10.0 | 2026-06-22 | IBM Langflow OSS 1.0.0 through 1.9.3 has an vulnerability due to an improper isolation of Python execution combined with |
| CVE-2026-28381 | 9.6 | 2026-06-22 | The Snowflake datasource allows for GET/PUT commands, which can allow any user with access to run queries against the da |
| CVE-2026-42129 | 7.7 | 2026-06-22 | The Loki datasource plugin's callResource handler contains a path traversal vulnerability. An authenticated Viewer-role  |
| CVE-2026-54099 | 8.8 | 2026-06-22 | A flaw was found in the Windows Machine Config Operator (WMCO) for Red Hat OpenShift Container Platform. The WICD CSR au |
| CVE-2026-54100 | 8.3 | 2026-06-22 | A flaw was found in the Windows Machine Config Operator (WMCO) for Red Hat OpenShift Container Platform. WMCO establishe |
| CVE-2026-9029 | 7.3 | 2026-06-22 | The geomap panel's XYZ tile layer has a sanitize-then-interpolate ordering bug. sanitizeTextPanelContent() runs on the r |
| CVE-2026-10845 | 7.3 | 2026-06-22 | IBM WebSphere Application Server 8.5 and 9.0 could allow a remote attacker to bypass authentication and gain unauthorize |
| CVE-2026-12628 | 8.1 | 2026-06-22 | IBM Storage Protect Client 8.1.0.0 through 8.2.1.0 and IBM Storage Protect Snapshot For Windows 8.1.0.0 through 8.2.1.0  |
| CVE-2026-41045 | 8.1 | 2026-06-22 | A time-to-check-time-of-use in polkit authentication of qSnapper before version 1.3.3 allowed a local attacker to bypass |
| CVE-2026-41046 | 7.3 | 2026-06-22 | A path traversal attack when using a "configName" parameter in qSnapper before version 1.3.3 allowed a local attacker to |
| CVE-2026-56104 | 7.4 | 2026-06-22 | Chainlit before 2.10.1 contains a session hijacking vulnerability that allows unauthenticated attackers to restore and i |
| CVE-2026-7664 | 9.8 | 2026-06-22 | IBM Langflow OSS 1.0.0 through 1.8.4 could allow unauthenticated attackers to access protected MCP project resources and |
| CVE-2026-8646 | 7.4 | 2026-06-22 | IBM WebSphere Application Server 9.0 and 8.5 and IBM WebSphere Application Server - Liberty 17.0.0.3 through 26.0.0.6 ar |
| CVE-2026-8858 | 7.5 | 2026-06-22 | IBM i 7.6, 7.5, 7.4, and 7.3, IBM WebSphere Application Server and IBM WebSphere Application Server Liberty are vulnerab |
| CVE-2026-9006 | 7.4 | 2026-06-22 | IBM WebSphere Application Server 9.0, and 8.5 is vulnerable to server-side request forgery (SSRF) with the Ajax Proxy co |
| CVE-2026-9071 | 7.5 | 2026-06-22 | IBM WebSphere Application Server 9.0, and 8.5 and IBM WebSphere Application Server - Liberty 17.0.0.3 through 26.0.0.6 a |
| CVE-2026-9072 | 8.1 | 2026-06-22 | IBM i 7.6, 7.5, 7.4, and 7.3, IBM WebSphere Application Server, and IBM WebSphere Application Server Liberty - when usin |
| CVE-2026-10789 | 9.6 | 2026-06-22 | A maliciously crafted webpage, when visited by a user with Autodesk Fusion Desktop running and the MCP extension enabled |
| CVE-2026-12249 | 9.0 | 2026-06-22 | An issue was discovered in Canonical ADSys upstream versions through v0.16.2. During Active Directory Certificate Servic |
| CVE-2026-42127 | 7.5 | 2026-06-22 | The public dashboard query endpoint does not limit request body size before processing, allowing unauthenticated attacke |
| CVE-2026-48712 | 7.5 | 2026-06-22 | protobufjs compiles protobuf definitions into JavaScript (JS) functions. Prior to 7.6.1 and 8.4.1, protobufjs could recu |
| CVE-2026-53539 | 7.5 | 2026-06-22 | Python-Multipart is a streaming multipart parser for Python. Prior to 0.0.30, when parsing application/x-www-form-urlenc |
| CVE-2026-54271 | 8.2 | 2026-06-22 | protobufjs-cli is the command line add-on for protobuf.js. Prior to 1.3.2 and 2.5.0, a previous fix for unsafe name hand |
| CVE-2026-54283 | 7.5 | 2026-06-22 | Starlette is a lightweight ASGI framework/toolkit. From 0.4.1 until 1.3.1, request.form() accepts max_fields and max_par |
| CVE-2026-54290 | 7.1 | 2026-06-22 | Hono is a Web application framework that provides support for any JavaScript runtime. Prior to 4.12.25, with credentials |
| CVE-2026-55388 | 8.1 | 2026-06-22 | piscina is a node.js worker pool implementation. Prior to 6.0.0-rc.2, 5.2.0, and 4.9.3, piscina's constructor and run()  |
| CVE-2026-50146 | 7.1 | 2026-06-22 | Astro is a web framework. Prior to 6.3.3, when a component uses a client:* directive, Astro inserts named slot content i |
| CVE-2026-53779 | 7.5 | 2026-06-22 | WebP Server Go through 0.14.4 contains a path traversal vulnerability on Windows that allows unauthenticated attackers t |
| CVE-2026-54293 | 7.5 | 2026-06-22 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research a |
| CVE-2026-54299 | 7.5 | 2026-06-22 | Astro is a web framework. Prior to 6.4.6, Astro SSR apps with prerendered error pages (/404 or /500 using export const p |
| CVE-2026-44271 | 8.1 | 2026-06-22 | Dell Wyse Management Suite (WMS), versions prior to WMS 2605, contain an Improper Neutralization of Special Elements use |
| CVE-2026-44272 | 8.8 | 2026-06-22 | Dell Wyse Management Suite (WMS), versions prior to WMS 2605, contain an Improper Neutralization of Special Elements use |
| CVE-2026-44274 | 7.8 | 2026-06-22 | Dell Wyse Management Suite (WMS), versions prior to WMS 2605, contain an Improper Link Resolution Before File Access vul |
| CVE-2026-55603 | 7.5 | 2026-06-22 | http-proxy-middleware is node.js http-proxy middleware. From 3.0.4 until 3.0.7 and 4.1.1, fixRequestBody() is the librar |
| CVE-2025-71339 | 8.1 | 2026-06-22 | Picklescan before 0.0.33 fails to detect the numpy.f2py.crackfortran._eval_length gadget in pickle __reduce__ methods, a |
| CVE-2025-71344 | 8.1 | 2026-06-22 | picklescan before 0.0.30 (affected versions 0.0.26 and earlier) fails to detect the ensurepip._run_pip built-in function |
| CVE-2025-71358 | 8.1 | 2026-06-22 | picklescan before 0.0.29 fails to detect malicious pickle files that exploit idlelib.autocomplete.AutoComplete.get_entit |
| CVE-2026-48109 | 8.2 | 2026-06-22 | MessagePack for C# is a MessagePack serializer for C#. Prior to 2.5.301 and 3.1.7, A vulnerability exists in the optiona |
| CVE-2026-48505 | 7.4 | 2026-06-22 | Filament is a collection of full-stack components for accelerated Laravel development. From 4.0.0 until 4.11.5 and 5.6.5 |
| CVE-2026-48506 | 7.5 | 2026-06-22 | MessagePack for C# is a MessagePack serializer for C#. Prior to 2.5.301 and 3.1.7, MessagePackReader.TrySkip() recursive |
| CVE-2026-55409 | 7.6 | 2026-06-22 | Filament is a collection of full-stack components for accelerated Laravel development. From 3.0.0 until 3.3.53, a disabl |
| CVE-2026-56266 | 8.6 | 2026-06-22 | Crawl4AI before 0.8.7 contains a server-side request forgery vulnerability in the /crawl, /crawl/stream, /md, and /llm e |
| CVE-2026-56268 | 7.7 | 2026-06-22 | Flowise before 3.1.2 contains an information disclosure vulnerability in the /api/v1/chatflows/apikey/:apikey endpoint.  |
| CVE-2026-56280 | 7.1 | 2026-06-22 | Cap-go before 12.128.2 contains a privilege inversion vulnerability in GET /build/logs/:jobId that allows read-only API  |
| CVE-2026-56314 | 7.1 | 2026-06-22 | Capgo before 12.128.12 fails to filter deleted app versions when joining channels during /updates resolution, allowing d |
| CVE-2026-56323 | 7.5 | 2026-06-22 | Capgo before 12.128.2 contains an information disclosure vulnerability in the /functions/v1/channel_self endpoint that a |
| CVE-2026-56324 | 8.2 | 2026-06-22 | Capgo before 12.128.2 contains a rate limit bypass vulnerability in the channel_self endpoint that allows attackers to c |
| CVE-2026-56348 | 9.1 | 2026-06-22 | n8n before 2.20.0 contains a credential exfiltration vulnerability in the POST /rest/dynamic-node-parameters/options end |
| CVE-2026-41523 | 7.5 | 2026-06-22 | vLLM is an inference and serving engine for large language models (LLMs). Prior to 0.22.0, an assert-based security chec |
| CVE-2026-48746 | 9.1 | 2026-06-22 | vLLM is an inference and serving engine for large language models (LLMs). From 0.3.0 until 0.22.0, a vulnerability in AS |
| CVE-2026-54232 | 8.8 | 2026-06-22 | vLLM is an inference and serving engine for large language models (LLMs). Prior to 0.22.1, the vLLM Dockerfile is vulner |
| CVE-2026-10651 | 7.1 | 2026-06-23 | A malformed Bluetooth Classic SDP attribute can trigger a reachable assertion in Zephyr's SDP parser. In subsys/bluetoot |
| CVE-2026-10658 | 7.1 | 2026-06-23 | A missing length validation in the Zephyr Bluetooth Host ISO receive path can be triggered by malformed HCI ISO data. In |
| CVE-2026-12866 | 9.8 | 2026-06-23 | All versions of the package expr-eval are vulnerable to Code Execution via the toJSFunction() API. An attacker can execu |
| CVE-2026-10521 | 7.2 | 2026-06-23 | An high privileged remote attacker can access a hidden configuration method, that should not be accessible by any user,  |
| CVE-2026-11374 | 9.0 | 2026-06-23 | In ManageEngine ADSelfService Plus, RecoveryManager Plus, M365 Manager Plus, and ADAudit Plus, the SSO tickets generated |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-20253 | Splunk / Enterprise | 2026-06-18 | 2026-06-21 | Unknown |
| CVE-2026-48907 | Widget Factory / Joomla Content Editor  | 2026-06-16 | 2026-06-19 | Unknown |

---

*Total entries in CISA KEV catalog: 1623*