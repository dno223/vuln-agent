# Vulnerability Intelligence Report

**Date:** 2026-08-02  
**Generated:** 2026-08-02T09:55:05Z  

## Pipeline Warnings

- summarizer failed: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}, 'request_id': 'req_011CddijFacEGGkWgRWSMQDa'}

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
| CVE-2025-71403 | 7.1 | 2026-08-01 | better-auth versions before 1.1.20 contain a bypass vulnerability in trustedOrigins validation logic affecting absolute  |
| CVE-2026-66402 | 9.8 | 2026-08-01 | FreeRDP before 3.29.0 (affected versions <= 3.28.0) contains multiple TLS certificate identity validation weaknesses in  |
| CVE-2026-67288 | 7.5 | 2026-08-01 | FreeRDP before 3.29.0 contains a null pointer dereference vulnerability in smartcard cache request decoders that accept  |
| CVE-2026-67289 | 9.8 | 2026-08-01 | FreeRDP before 3.29.0 (affected versions <= 3.28.0) does not validate CRLF and control characters in the server-controll |
| CVE-2026-67290 | 7.5 | 2026-08-01 | FreeRDP before 3.29.0 contains a heap out-of-bounds read vulnerability in the TSMF FFmpeg decoder when parsing AVC1 MPEG |
| CVE-2026-67291 | 7.5 | 2026-08-01 | FreeRDP before 3.29.0 (affected versions <= 3.28.0) contains a heap out-of-bounds read in update_process_glyph_fragments |
| CVE-2026-67296 | 7.5 | 2026-08-01 | FreeRDP before 3.29.0 contains a denial of service vulnerability in the RDPEI server channel handler that fails to valid |
| CVE-2026-67297 | 7.5 | 2026-08-01 | FreeRDP before 3.29.0 fails to enforce the RESPONSE_SIZE_LIMIT when processing Transfer-Encoding: chunked HTTP responses |
| CVE-2026-67298 | 7.5 | 2026-08-01 | FreeRDP versions 3.28.0 and earlier contain a heap buffer overflow in the server-side RAIL channel handler (rail_server_ |
| CVE-2026-67299 | 7.5 | 2026-08-01 | FreeRDP before 3.29.0 contains a client-side heap use-after-free in the async update message proxy for WINDOW_ICON_ORDER |
| CVE-2026-67300 | 7.5 | 2026-08-01 | FreeRDP before 3.29.0 contains client-side heap use-after-free vulnerabilities in the async update message proxy for RAI |
| CVE-2026-67301 | 7.5 | 2026-08-01 | FreeRDP before 3.29.0 contains out-of-bounds read vulnerabilities in the async update message proxy for the PolygonSC an |
| CVE-2026-67304 | 7.5 | 2026-08-01 | FreeRDP before 3.29.0 contains a null pointer dereference vulnerability in smartcard device control request cleanup when |
| CVE-2026-67308 | 10.0 | 2026-08-01 | Wazuh workflows before 44bf114 contain a shell injection vulnerability in GitHub Actions that allows attackers to execut |
| CVE-2026-67322 | 7.5 | 2026-08-01 | GitPython before 3.1.52 is vulnerable to environment-variable exfiltration in Repo.clone_from(). The caller-supplied rem |
| CVE-2026-67323 | 8.4 | 2026-08-01 | GitPython before 3.1.51 fails to guard against dangerous Git options passed as keyword arguments in Repo.archive() and g |
| CVE-2026-67324 | 9.8 | 2026-08-01 | GitPython 3.1.50 fails to recognize joined short-option forms such as -u<value> (the short form of --upload-pack=<value> |
| CVE-2026-67325 | 8.8 | 2026-08-01 | GitPython before 3.1.51 contains an incomplete command injection blocklist that fails to account for git's long-option p |
| CVE-2026-67326 | 7.0 | 2026-08-01 | GitPython before 3.1.50 fails to validate newline characters in the section parameter of config_writer(), allowing attac |
| CVE-2026-67327 | 8.3 | 2026-08-01 | better-auth versions >= 1.1.3 and < 1.6.22 (and pre-release versions >= 1.7.0-beta.0 and < 1.7.0-beta.10) are vulnerable |
| CVE-2026-67328 | 8.1 | 2026-08-01 | @better-auth/sso versions before 1.6.21 contain multiple authentication bypass vulnerabilities in SSO provider handling  |
| CVE-2026-67329 | 7.1 | 2026-08-01 | @better-auth/stripe versions >= 1.4.11 and < 1.6.21, and >= 1.7.0-beta.0 and < 1.7.0-beta.10, contain an authorization b |
| CVE-2026-67330 | 9.9 | 2026-08-01 | @better-auth/scim (a better-auth plugin) versions >= 1.4.0-beta.27 through <= 1.6.21 and >= 1.7.0-beta.0 through <= 1.7. |
| CVE-2026-67331 | 8.3 | 2026-08-01 | better-auth SCIM versions from 1.5.0 before 1.7.0-beta.4 fail to bind non-organization SCIM providers to their creator b |
| CVE-2026-67333 | 7.2 | 2026-08-01 | better-auth before 1.6.13 (and pre-release builds 1.7.0-beta.0 through 1.7.0-beta.3) fail to validate the scheme of redi |
| CVE-2026-67336 | 8.7 | 2026-08-01 | better-auth versions before 1.6.11 contain insecure cryptographic defaults in the oidcProvider and mcp plugins that adve |
| CVE-2026-67340 | 9.8 | 2026-08-01 | ArcadeDB before 26.7.2 (arcadedb-engine) allows trigger scripts to look up host classes in java.lang.* (via Java.type) b |
| CVE-2026-67341 | 9.8 | 2026-08-01 | ArcadeDB versions before 26.7.2 fail to enforce scripting authorization checks on the SQL DEFINE FUNCTION statement with |
| CVE-2026-67342 | 9.8 | 2026-08-01 | ArcadeDB versions before 26.7.2 contain an authorization bypass vulnerability in HTTP handlers for time series, batch, P |
| CVE-2026-67343 | 8.8 | 2026-08-01 | ArcadeDB versions before 26.7.2 fail to properly redact the cluster token in the GET /api/v1/server endpoint, allowing a |
| CVE-2026-67352 | 7.6 | 2026-08-01 | luci-app-https-dns-proxy contains a stored cross-site scripting vulnerability in the resolver_url parameter that allows  |
| CVE-2026-13339 | 7.5 | 2026-08-02 | The CubeWP Framework plugin for WordPress is vulnerable to Directory Traversal in all versions up to, and including, 1.1 |
| CVE-2026-18352 | 7.5 | 2026-08-02 | The User Access Manager plugin for WordPress is vulnerable to Directory Traversal in all versions up to, and including,  |
| CVE-2026-8457 | 9.8 | 2026-08-02 | The WooCommerce - Social Login plugin for WordPress is vulnerable to Authentication Bypass in all versions up to and inc |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-20316 | Cisco / Secure Firewall Management Center (FMC) | 2026-07-29 | 2026-08-01 | Unknown |
| CVE-2025-68686 | Fortinet / FortiOS | 2026-07-27 | 2026-08-10 | Unknown |
| CVE-2026-16812 | Arista / VeloCloud Orchestrator | 2026-07-27 | 2026-07-30 | Unknown |

---

*Total entries in CISA KEV catalog: 1656*