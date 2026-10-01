# Vulnerability Intelligence Report

**Date:** 2026-10-01  
**Generated:** 2026-10-01T15:06:36Z  

---

## Executive Summary

Our environment faces significant exposure across 253 high-severity vulnerabilities, including two critical CVSS 9.8 flaws in LightLLM and Trex MES that enable unauthenticated remote code execution and SQL injection. A JetBrains TeamCity sandbox escape and an OpenSave path traversal further heighten risk. Nine new CISA Known Exploited Vulnerabilities were added this week across Cisco, Apple, Citrix, and MikroTik products, signaling active threat actor interest in infrastructure targets. While none of our monitored CVEs currently appear in the KEV catalog, the breadth and severity of open vulnerabilities demand immediate prioritization and remediation action.

---

## Risk Narrative

Threat actors are actively exploiting enterprise infrastructure, as evidenced by nine CISA KEV additions in seven days targeting Cisco, Citrix, Apple, and MikroTik platforms commonly found in corporate environments. Simultaneously, critical unpatched flaws in manufacturing systems, AI serving infrastructure, and CI/CD pipelines create multiple high-value attack paths. Unauthenticated remote code execution and SQL injection vulnerabilities represent the highest business risk, potentially enabling data exfiltration, operational disruption, and ransomware deployment. The combination of active exploitation in the wild and a large unresolved vulnerability backlog significantly elevates the organization's overall threat exposure and potential for a material security incident.

---

## Prioritized Action Items

1. Immediately patch or isolate LightLLM deployments to remediate the unauthenticated RPyC deserialization flaw (CVE-2026-103395, CVSS 9.8) enabling full remote code execution.
2. Apply vendor patches or implement network-level controls for the Trex MES SQL injection and authentication bypass vulnerabilities (CVE-2026-18782, CVE-2026-18783) within 24 hours.
3. Update all Cisco Catalyst SD-WAN Manager, Citrix NetScaler, Apple, and MikroTik RouterOS systems to address the nine newly added CISA KEV entries within 72 hours.
4. Upgrade JetBrains TeamCity to version 2026.2, 2026.1.4, or 2025.11.8 to close the Kotlin DSL sandbox escape vulnerability (CVE-2026-100253) allowing code execution.
5. Conduct an immediate audit of oc-mirror, OpenSave, and LightLLM RL API deployments to identify exploitable path traversal and unauthenticated endpoint exposures across the environment.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-101295 | 7.3 | 2026-09-30 | Path traversal / arbitrary file write in oc-mirror's operator catalog image extraction. When mirroring operator catalogs |
| CVE-2026-102717 | 7.5 | 2026-09-30 | MQTT WebSocket setter ABI mismatch may disclose memory or cause a crash |
| CVE-2026-103270 | 7.5 | 2026-09-30 | LightLLM through 1.2.0 mounts reinforcement learning control routes on the public HTTP API without authentication checks |
| CVE-2026-103395 | 9.8 | 2026-09-30 | LightLLM through 1.2.0 visual_only deployments expose an unauthenticated RPyC service with allow_pickle enabled that des |
| CVE-2026-103398 | 8.1 | 2026-09-30 | OpenSave through 2.4.0 fails to properly validate save paths supplied by paired peers in the manifest request handler. A |
| CVE-2026-18782 | 9.8 | 2026-09-30 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Trex Digital Smart |
| CVE-2026-18783 | 8.8 | 2026-09-30 | Missing authentication for critical function vulnerability in Trex Digital Smart Manufacturing Systems Inc. Trex MES all |
| CVE-2026-47097 | 7.5 | 2026-09-30 | AJA HELO Plus firmware before 2.1.7 contains an information disclosure vulnerability that allows unauthenticated attacke |
| CVE-2026-62097 | 7.6 | 2026-09-30 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in WPTasty Business D |
| CVE-2026-100253 | 8.8 | 2026-09-30 | In JetBrains TeamCity before 2026.2, 
2026.1.4, 
2025.11.8 sandbox escape leading to code execution was possible via the |
| CVE-2026-100254 | 8.8 | 2026-09-30 | In JetBrains TeamCity before 2026.2, 
2026.1.4, 
2025.11.8 authenticated users could execute commands on Windows servers |
| CVE-2026-100255 | 8.1 | 2026-09-30 | In JetBrains TeamCity before 2026.2, 
2026.1.4, 
2025.11.8 administrator account takeover was possible via password rese |
| CVE-2026-100256 | 7.8 | 2026-09-30 | In JetBrains IntelliJ IDEA before 2026.2.3 rCE via Structural Search script constraints was possible in untrusted projec |
| CVE-2026-100262 | 7.6 | 2026-09-30 | In JetBrains YouTrack before 2026.2.18991 missing authorisation allowed users with read-only project access to overwrite |
| CVE-2026-100266 | 7.7 | 2026-09-30 | In JetBrains Hub before 2026.2.52366 missing authorisation allowed authenticated users to send arbitrary emails from the |
| CVE-2026-100268 | 7.7 | 2026-09-30 | In JetBrains YouTrack before 2026.2.19197 project administrators could read comments from other projects via notificatio |
| CVE-2026-100273 | 8.2 | 2026-09-30 | In JetBrains YouTrack before 2026.2.19197 authorisation bypass in the scripts debugger allowed arbitrary code execution |
| CVE-2026-100277 | 8.9 | 2026-09-30 | In JetBrains YouTrack before 2026.2.19197 account takeover was possible by replaying a notification signature |
| CVE-2026-102427 | 10.0 | 2026-09-30 | Joomla Extension - ordasoft.com - Unauthenticated Remote Code Execution in OrdaSoft Joomla CCK < 8.3.16 - site/uploader. |
| CVE-2026-103229 | 7.3 | 2026-09-30 | A vulnerability was found in AdithyaYelloju Restaurant-Management-System up to 7f0e7e84255e8fcfd488e83f8f91451bbbff6b9c. |
| CVE-2026-103230 | 7.3 | 2026-09-30 | A vulnerability was determined in AdithyaYelloju Restaurant-Management-System up to 7f0e7e84255e8fcfd488e83f8f91451bbbff |
| CVE-2026-103231 | 7.3 | 2026-09-30 | A vulnerability was identified in AdithyaYelloju Restaurant-Management-System up to 7f0e7e84255e8fcfd488e83f8f91451bbbff |
| CVE-2026-103432 | 8.1 | 2026-09-30 | apcupsd through 3.14.14 has an sscanf stack-based buffer overflow in getupsvar() in src/cgi/upsfetch.c (used by upsstats |
| CVE-2026-47489 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the kernel mode layer where permissions on read-only mem |
| CVE-2026-47491 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the kernel mode layer where an unprivileged user can cau |
| CVE-2026-47493 | 7.8 | 2026-09-30 | NVIDIA vGPU software for Windows and Linux contains a vulnerability in the GPU kernel driver where a guest may access pr |
| CVE-2026-47494 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability where a user might be able to cause a format string issue.  |
| CVE-2026-47495 | 7.8 | 2026-09-30 | NVIDIA vGPU Virtual GPU Manager for Windows and Linux contains a vulnerability in the kernel mode layer where a user cou |
| CVE-2026-47496 | 7.3 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the Virtual GPU Manager (vGPU plugin) where a guest VM u |
| CVE-2026-47497 | 7.8 | 2026-09-30 | NVIDIA Virtual GPU Manager contains a vulnerability in the GPU System Processor (GSP) tracing component where a guest VM |
| CVE-2026-47498 | 7.8 | 2026-09-30 | NVIDIA vGPU Manager contains a vulnerability in the GPU System Processor (GSP) plugin where a guest VM user may cause an |
| CVE-2026-47499 | 7.8 | 2026-09-30 | NVIDIA vGPU Virtual GPU Manager for Windows and Linux contains a vulnerability in the kernel mode layer where a guest co |
| CVE-2026-47500 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer where improper cleanup |
| CVE-2026-47501 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the kernel mode layer where a user could cause an out-of |
| CVE-2026-47502 | 7.8 | 2026-09-30 | NVIDIA vGPU Virtual GPU Manager for Windows and Linux contains a vulnerability in the kernel mode layer, where a guest u |
| CVE-2026-47503 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the Virtual GPU Manager (vGPU plugin), where a guest VM  |
| CVE-2026-47504 | 7.8 | 2026-09-30 | NVIDIA Linux GPU Display Driver contains a vulnerability in the NGX updater where an outdated embedded cryptographic lib |
| CVE-2026-47505 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows contains a vulnerability in the kernel mode layer where an attacker could cause a  |
| CVE-2026-47507 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer, where a user could ca |
| CVE-2026-47508 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer, where a user could ca |
| CVE-2026-47510 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer, where a user could ca |
| CVE-2026-47511 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer, where a user could ca |
| CVE-2026-47512 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer, where a user could ca |
| CVE-2026-47513 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer, where a user could ca |
| CVE-2026-47514 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer, where a user could ca |
| CVE-2026-47516 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability where an unprivileged user could cause a use-af |
| CVE-2026-47519 | 7.8 | 2026-09-30 | NVIDIA vGPU Virtual GPU Manager for Linux contains a vulnerability in the kernel mode layer where an attacker could caus |
| CVE-2026-47520 | 7.8 | 2026-09-30 | NVIDIA vGPU Virtual GPU Manager for Linux contains a vulnerability in the kernel mode layer where an attacker could caus |
| CVE-2026-47521 | 7.8 | 2026-09-30 | NVIDIA vGPU Virtual GPU Manager for Linux contains a vulnerability in the kernel mode layer where an attacker could caus |
| CVE-2026-47523 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer where an attacker coul |
| CVE-2026-47528 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the firmware where an attacker could cause a |
| CVE-2026-47530 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer where an attacker coul |
| CVE-2026-47535 | 7.8 | 2026-09-30 | NVIDIA vGPU Virtual GPU Manager for Linux contains a vulnerability in the firmware where an attacker could cause an out- |
| CVE-2026-47536 | 7.8 | 2026-09-30 | NVIDIA vGPU Virtual GPU Manager for Linux contains a vulnerability in the kernel mode layer where an attacker could caus |
| CVE-2026-47540 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer where an attacker coul |
| CVE-2026-47541 | 7.8 | 2026-09-30 | NVIDIA vGPU Virtual GPU Manager for Linux contains a vulnerability in the kernel mode layer where an attacker could caus |
| CVE-2026-47545 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer where an attacker coul |
| CVE-2026-47548 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer where an attacker coul |
| CVE-2026-47550 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows contains a vulnerability in the kernel mode layer where an unprivileged local user |
| CVE-2026-47551 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer where a user could cau |
| CVE-2026-47552 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the kernel mode layer where an unprivileged user could b |
| CVE-2026-47553 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer where an unprivileged  |
| CVE-2026-47554 | 7.1 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the kernel mode layer where improper verification of cry |
| CVE-2026-47556 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer where an unprivileged  |
| CVE-2026-47558 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the kernel mode layer where an unprivileged user could c |
| CVE-2026-47559 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer, where a user could ac |
| CVE-2026-47560 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the kernel mode layer where an unprivileged user could c |
| CVE-2026-47561 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the kernel mode layer where the size of an ioctl input b |
| CVE-2026-47563 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the kernel mode layer where a user could cause a NULL po |
| CVE-2026-47569 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the kernel mode layer where a user could cause a type co |
| CVE-2026-47570 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows contains a vulnerability in the CUDA driver where an attacker could cause a librar |
| CVE-2026-47571 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows contains a vulnerability in kernel-mode escape handling where an attacker with loc |
| CVE-2026-47572 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the kernel mode layer where a user could cause type conf |
| CVE-2026-47573 | 7.8 | 2026-09-30 | NVIDIA NVAPI for Windows contains a vulnerability where an attacker could cause an out-of-bounds write. A successful exp |
| CVE-2026-47574 | 7.8 | 2026-09-30 | NVIDIA vGPU Virtual GPU Manager for Linux contains a vulnerability where an attacker could cause incorrect resource tran |
| CVE-2026-47575 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows contains a vulnerability in the display driver DIAG escape handler where a local u |
| CVE-2026-47576 | 7.7 | 2026-09-30 | NVIDIA GPU Display Driver for Windows contains a vulnerability in the kernel module through which an attacker might init |
| CVE-2026-47577 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows contains a vulnerability in the kernel module where an attacker could cause an inc |
| CVE-2026-47578 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows contains a vulnerability in the kernel mode layer where an attacker could cause an |
| CVE-2026-47579 | 7.8 | 2026-09-30 | The NVIDIA GPU Display Driver for Windows contains a vulnerability in the kernel mode driver through which a user might  |
| CVE-2026-47580 | 7.3 | 2026-09-30 | NVIDIA GPU Display Driver for Windows contains a vulnerability in the kernel module where an attacker could cause a miss |
| CVE-2026-47582 | 7.0 | 2026-09-30 | NVIDIA GPU Display Driver for Windows contains a vulnerability in the kernel module where an attacker could cause an out |
| CVE-2026-47583 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows contains a vulnerability in the kernel module where an attacker could cause type c |
| CVE-2026-47585 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows contains a vulnerability in the kernel module where an attacker could cause an int |
| CVE-2026-47587 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability where an unprivileged user could cause a use-after-free. A  |
| CVE-2026-47588 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability where an unprivileged user could cause a use-after-free con |
| CVE-2026-47589 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability where an unprivileged user may cause a use-afte |
| CVE-2026-47590 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability where an unprivileged user may cause a use-afte |
| CVE-2026-47591 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the kernel mode layer where an unprivileged user could b |
| CVE-2026-47592 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer where an unprivileged  |
| CVE-2026-47593 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows contains a vulnerability in the kernel mode layer where an unprivileged user can c |
| CVE-2026-47594 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability where an unprivileged user may cause a use-afte |
| CVE-2026-47595 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the kernel mode layer where an unprivileged user can wri |
| CVE-2026-47596 | 7.0 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the kernel mode layer where an unprivileged user can wri |
| CVE-2026-47597 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the open-source kernel module Resource Serve |
| CVE-2026-47598 | 7.0 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the open-source kernel module event delivery path where  |
| CVE-2026-47599 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Linux contains a vulnerability in the open-source kernel module where an unprivileged loca |
| CVE-2026-47600 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer where an error-handlin |
| CVE-2026-47601 | 7.8 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the open-source kernel module DMA-BUF import |
| CVE-2026-47602 | 7.1 | 2026-09-30 | NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode driver where a local user ca |
| CVE-2026-103232 | 7.3 | 2026-09-30 | A weakness has been identified in AdithyaYelloju Restaurant-Management-System up to 7f0e7e84255e8fcfd488e83f8f91451bbbff |
| CVE-2026-46711 | 8.3 | 2026-09-30 | Soft Machine is a Virtual Machine–based agentic development environment / Cloud OS. In versions 0.2.247 and prior, the w |
| CVE-2026-55176 | 9.0 | 2026-09-30 | Soft Machine is a Virtual Machine–based agentic development environment / Cloud OS. In versions 0.2.247 and prior, two a |
| CVE-2026-55181 | 9.4 | 2026-09-30 | Tugtainer is a self-hosted app for automating updates of Docker containers. Prior to version 1.30.3, Tugtainer's OIDC au |
| CVE-2026-55494 | 9.8 | 2026-09-30 | Tugtainer is a self-hosted app for automating updates of Docker containers. Prior to version 1.30.4, Tugtainer Agent all |
| CVE-2026-62308 | 9.1 | 2026-09-30 | Tugtainer is a self-hosted app for automating updates of Docker containers. Prior to version 1.30.6, Tugtainer allows an |
| CVE-2026-100510 | 7.1 | 2026-09-30 | Unauthenticated Cross Site Scripting (XSS) in Post and Page Builder by BoldGrid <= 1.27.14 versions. |
| CVE-2026-100512 | 9.8 | 2026-09-30 | Contributor PHP Object Injection in Nested Pages <= 3.3.2 versions. |
| CVE-2026-102376 | 7.1 | 2026-09-30 | Subscriber Cross Site Scripting (XSS) in Branda <= 3.4.32 versions. |
| CVE-2026-102377 | 8.8 | 2026-09-30 | Contributor PHP Object Injection in Photo Gallery by 10Web <= 1.8.46 versions. |
| CVE-2026-102391 | 7.1 | 2026-09-30 | Unauthenticated Cross Site Scripting (XSS) in JetFormBuilder <= 3.6.5.4 versions. |
| CVE-2026-102392 | 7.2 | 2026-09-30 | Shop manager PHP Object Injection in Extra Product Options For WooCommerce \| Custom Product Addons and Fields <= 3.3.8 v |
| CVE-2026-103471 | 7.5 | 2026-09-30 | restbed through 5.0.0 buffers HTTP request headers without enforcing a maximum size limit, allowing remote unauthenticat |
| CVE-2026-103472 | 7.5 | 2026-09-30 | restbed through 5.0.0 accepts WebSocket frames with declared payload lengths up to 2^63 bytes and buffers the payload wi |
| CVE-2026-103473 | 8.1 | 2026-09-30 | Deno versions 2.7.0 through 2.9.7 on Windows contain a command injection vulnerability in node:child_process where shell |
| CVE-2026-103474 | 8.8 | 2026-09-30 | yii2-starter-kit through 4.2.0 fails to validate file types in the backend storage upload actions, allowing authenticate |
| CVE-2026-103475 | 9.1 | 2026-09-30 | yii2-starter-kit through 4.2.0 exposes the Yii debug and Gii modules to all IP addresses by setting allowedIPs to ['*']  |
| CVE-2026-53605 | 7.8 | 2026-09-30 | Reachy Mini ISO for Wireless contains the necessary files to build a custom Raspberry Pi OS image for the Reachy Mini Wi |
| CVE-2026-55107 | 10.0 | 2026-09-30 | Kobako is a Ruby gem that embeds a Wasm-isolated mruby interpreter inside applications, allowing execution of untrusted  |
| CVE-2026-87004 | 8.1 | 2026-09-30 | Tugtainer is a self-hosted app for automating updates of Docker containers. Prior to version 1.31.3, when the OIDC login |
| CVE-2026-94171 | 7.1 | 2026-09-30 | Unauthenticated Cross Site Scripting (XSS) in CURCY <= 2.2.16 versions. |
| CVE-2026-97256 | 7.2 | 2026-09-30 | Editor PHP Object Injection in Page Builder by SiteOrigin <= 2.36.0 versions. |
| CVE-2026-97290 | 7.1 | 2026-09-30 | Unauthenticated Cross Site Scripting (XSS) in Photonic Gallery & Lightbox for Flickr, SmugMug & Others <= 3.36 versions. |
| CVE-2026-97291 | 8.8 | 2026-09-30 | Contributor PHP Object Injection in Schema & Structured Data for WP & AMP <= 1.66 versions. |
| CVE-2026-101880 | 8.8 | 2026-09-30 | OpenClaw Windows Node before 2026.7.1 contains an incorrect authorization vulnerability in the system.run exec-approval  |
| CVE-2026-101882 | 8.8 | 2026-09-30 | OpenClaw Windows Node before 2026.7.1 contains an incomplete validation vulnerability in system.execApprovals.set that a |
| CVE-2026-101884 | 7.5 | 2026-09-30 | OpenClaw Windows Node before 2026.7.1 contains an incomplete environment-variable sanitizer in system.run that fails to  |
| CVE-2026-101885 | 7.8 | 2026-09-30 | ZeroClaw versions before 0.8.5 built with plugins-wasm feature contain a path traversal vulnerability in plugin installa |
| CVE-2023-54402 | 7.5 | 2026-09-30 | iDocView contains a server-side request forgery vulnerability in its /doc/upload endpoint that allows remote unauthentic |
| CVE-2023-54403 | 7.5 | 2026-09-30 | Yonyou U8 CRM before V16.5 and V18 contains an arbitrary file read vulnerability in /ajax/getemaildata.php that allows u |
| CVE-2024-58387 | 7.5 | 2026-09-30 | Inspur Haiyue HCM Cloud contains an arbitrary file read vulnerability in the /api/model_report/file/download endpoint th |
| CVE-2026-102089 | 7.2 | 2026-09-30 | Kiteworks Email Protection Gateway before version 9.5.0 is vulnerable to a path traversal weakness in an administrative  |
| CVE-2026-102091 | 7.5 | 2026-09-30 | Kiteworks Secure Data Forms before version 9.5.0 is vulnerable to Server-Side Request Forgery that could allow an unauth |
| CVE-2026-102092 | 8.7 | 2026-09-30 | Kiteworks Core before version 9.5.0 is vulnerable to Stored Cross-site Scripting (XSS) that could allow an authenticated |
| CVE-2026-102093 | 7.2 | 2026-09-30 | Kiteworks Core before version 9.5.0 is vulnerable to Improper Privilege Management and does not correctly enforce restri |
| CVE-2026-102094 | 7.2 | 2026-09-30 | Kiteworks Email Protection Gateway before version 9.5.0 is vulnerable to Unsafe Reflection and does not sufficiently res |
| CVE-2026-102095 | 9.1 | 2026-09-30 | Kiteworks Email Protection Gateway before version 9.5.0 is vulnerable to Server-Side Request Forgery. Kiteworks Email Pr |
| CVE-2026-102096 | 7.2 | 2026-09-30 | Kiteworks Core before version 9.5.0 is vulnerable to OS Command Injection that allows an authenticated administrator to  |
| CVE-2026-102097 | 7.2 | 2026-09-30 | Kiteworks Email Protection Gateway before version 9.5.0 is vulnerable to Remote Code Execution. Kiteworks Email Protecti |
| CVE-2026-102098 | 7.2 | 2026-09-30 | Kiteworks Core before version 9.5.0 is vulnerable to SQL Injection. A stored SQL injection vulnerability in a Kiteworks  |
| CVE-2026-102099 | 7.2 | 2026-09-30 | Kiteworks Core before version 9.5.0 is vulnerable to Arbitrary File Write. An improper restriction of a user-supplied fi |
| CVE-2026-102100 | 8.7 | 2026-09-30 | Kiteworks Core before version 9.5.0 is vulnerable to Stored Cross-Site Scripting. A stored cross-site scripting (XSS) we |
| CVE-2026-102101 | 8.1 | 2026-09-30 | Kiteworks Core before version 9.5.0 is vulnerable to Deserialization of Untrusted Data. A deserialization weakness in Ki |
| CVE-2026-102102 | 9.1 | 2026-09-30 | Kiteworks Email Protection Gateway before version 9.5.0 is vulnerable to Server-Side Request Forgery (SSRF). A server-si |
| CVE-2026-102103 | 9.1 | 2026-09-30 | Kiteworks Email Protection Gateway before version 9.5.0 is vulnerable to Server-Side Request Forgery (SSRF). A server-si |
| CVE-2026-102104 | 9.1 | 2026-09-30 | Kiteworks Email Protection Gateway before version 9.5.0 is vulnerable to Server-Side Request Forgery (SSRF). A server-si |
| CVE-2026-102105 | 9.1 | 2026-09-30 | Kiteworks Email Protection Gateway before version 9.5.0 is vulnerable to Server-Side Request Forgery (SSRF). A server-si |
| CVE-2026-102106 | 9.1 | 2026-09-30 | Improper authentication in a Kiteworks Email Protection Gateway administrative service. An administrative service in Kit |
| CVE-2026-102108 | 7.2 | 2026-09-30 | An authenticated administrator of Kiteworks Email Protection Gateway could submit a crafted serialized object to a clust |
| CVE-2026-102109 | 7.1 | 2026-09-30 | A SQL injection vulnerability existed in Kiteworks Secure Data Forms, where a value derived from the authenticated user' |
| CVE-2026-102112 | 7.8 | 2026-09-30 | A privilege escalation vulnerability in Kiteworks could allow an attacker who has already obtained code execution as an  |
| CVE-2026-102113 | 7.8 | 2026-09-30 | A privilege escalation vulnerability in Kiteworks could allow an attacker who has already obtained code execution as an  |
| CVE-2026-102114 | 7.2 | 2026-09-30 | A command injection vulnerability in Kiteworks could allow a high-privileged authenticated administrator to execute arbi |
| CVE-2026-102115 | 9.8 | 2026-09-30 | Kiteworks Core did not correctly validate a parameter submitted to the password reset workflow. An unauthenticated attac |
| CVE-2026-102116 | 7.2 | 2026-09-30 | -A weakness could have allowed an authenticated Kiteworks Email Protection Gateway administrator to write a file outside |
| CVE-2026-102117 | 7.2 | 2026-09-30 | On deployments where the remote-support capability is licensed and enabled, an authenticated System Administrator who al |
| CVE-2026-102118 | 7.8 | 2026-09-30 | A local privilege escalation vulnerability in Kiteworks could have allowed an attacker with an existing shell under a lo |
| CVE-2026-102119 | 7.2 | 2026-09-30 | A path traversal weakness in an optional, non-default administrative feature allowed an authenticated administrator to m |
| CVE-2026-102120 | 8.8 | 2026-09-30 | A privilege escalation vulnerability in Kiteworks could have allowed an attacker who had already obtained code execution |
| CVE-2026-102121 | 8.6 | 2026-09-30 | A form-rendering interface in the Advanced Forms component is reachable without authentication so that published forms c |
| CVE-2026-102123 | 7.4 | 2026-09-30 | A Kiteworks appliance setup interface did not confine a user-supplied file path to its intended directory, which could a |
| CVE-2026-102125 | 8.8 | 2026-09-30 | The sandbox that isolates document conversion on a Kiteworks appliance did not fully confine the code running inside it. |
| CVE-2026-102126 | 8.1 | 2026-09-30 | A stored cross-site scripting (XSS) weakness in Kiteworks Core could allow an administrator holding only a single, narro |
| CVE-2026-102127 | 7.0 | 2026-09-30 | An XML parser used by Kiteworks Email Protection Gateway did not restrict external entity references. Where an optional, |
| CVE-2026-102128 | 7.5 | 2026-09-30 | An identity-verification weakness in Kiteworks Email Protection Gateway allowed the gateway to act on the Kiteworks plat |
| CVE-2026-102129 | 7.2 | 2026-09-30 | A user-provisioning interface in Kiteworks Core did not verify that the requesting administrator was entitled to grant t |
| CVE-2026-102130 | 7.2 | 2026-09-30 | Kiteworks Email Protection Gateway did not sufficiently validate the content of an uploaded backup, and allowed an admin |
| CVE-2026-102131 | 7.2 | 2026-09-30 | Kiteworks Email Protection Gateway rejected certain configuration settings, but its validation did not recognize every f |
| CVE-2026-102132 | 7.2 | 2026-09-30 | An administrative import function in Kiteworks Core did not verify that the requesting administrator was entitled to cre |
| CVE-2026-102142 | 7.2 | 2026-09-30 | A system notification template on the Kiteworks appliance was rendered by a template engine that evaluated expressions c |
| CVE-2026-102143 | 7.5 | 2026-09-30 | An unauthenticated attacker could cause a file with attacker-controlled content to be written to the appliance filesyste |
| CVE-2026-102147 | 9.3 | 2026-09-30 | A stored cross-site scripting (XSS) weakness in Kiteworks Core could allow an unauthenticated attacker to store crafted  |
| CVE-2026-102149 | 9.4 | 2026-09-30 | Kiteworks Email Protection Gateway did not sufficiently restrict which account a certificate could be assigned to. This  |
| CVE-2026-102150 | 7.2 | 2026-09-30 | A function in the Kiteworks Advanced Forms component was reachable without authentication. An unauthenticated attacker c |
| CVE-2026-51568 | 8.1 | 2026-09-30 | modelscope Agentscope v1.0.18-v1.0.0 is vulnerable to Path Traversal in write_text_file. |
| CVE-2026-51570 | 8.1 | 2026-09-30 | modelscope Agentscope v1.0.0-v1.0.8 is vulnerable to Path Traversal in insert_text_file. |
| CVE-2026-103591 | 7.5 | 2026-09-30 | DeepWiki-Open through commit d92819a contains an unauthenticated arbitrary file read vulnerability in the GET /codemap/f |
| CVE-2026-103530 | 7.3 | 2026-10-01 | A vulnerability was detected in decolua 9Router up to 0.5.55. The affected element is the function fetch of the file src |
| CVE-2026-92245 | 7.5 | 2026-10-01 | The Simply Schedule Appointments plugin for WordPress is vulnerable to Sensitive Information Exposure in all versions up |
| CVE-2026-96561 | 7.2 | 2026-10-01 | The AI Engine – The Chatbot, AI Framework & MCP for WordPress plugin for WordPress is vulnerable to Stored Cross-Site Sc |
| CVE-2026-103536 | 7.3 | 2026-10-01 | A vulnerability was identified in ZongXR Supermarket 1.0.0.0. Affected by this vulnerability is the function OrderContro |
| CVE-2026-82824 | 9.8 | 2026-10-01 | Hitachi Coding Software Suite contains a vulnerability related to Path Traversal vulnerability that allows an attacker t |
| CVE-2026-82825 | 9.8 | 2026-10-01 | Hitachi Coding Software Suite contains a vulnerability related to Missing Authentication for Critical Function. This all |
| CVE-2026-82826 | 7.5 | 2026-10-01 | Hitachi Coding Software Suite contains a vulnerability related to the Cleartext Transmission of Sensitive Information wh |
| CVE-2026-82827 | 9.8 | 2026-10-01 | Hitachi Coding Software Suite contains a vulnerability related to Use of Hard-coded Cryptographic Key. The Hardcoding of |
| CVE-2026-82828 | 8.8 | 2026-10-01 | Hitachi Coding Software Suite contains an Incorrect Authorization vulnerability that allows an unprivileged user to perf |
| CVE-2026-82829 | 9.8 | 2026-10-01 | Hitachi Coding Software Suite contains a vulnerability related to Hidden Functionality vulnerability which allows an att |
| CVE-2026-92966 | 9.1 | 2026-10-01 | The The Appointment Booking Plugin – LatePoint \| Calendar & Scheduling for WordPress plugin for WordPress is vulnerable  |
| CVE-2026-101147 | 8.8 | 2026-10-01 | The Featured Image from URL (FIFU) WordPress plugin before 6.0.8, Featured Image from URL (FIFU) Premium WordPress plugi |
| CVE-2026-101148 | 10.0 | 2026-10-01 | The BackupSheep WordPress Backup Plugin WordPress plugin through 1.8 does not properly validate its integration key, tre |
| CVE-2026-19253 | 8.7 | 2026-10-01 | The Cache Enabler WordPress plugin before 1.8.17 does not validate a URL before using it to build a filesystem path in i |
| CVE-2026-80275 | 8.8 | 2026-10-01 | Comelit Multi-User Gateway for VIP System (model 1456B) firmware versions 2.9.1 and 2.10.0 fail to enforce server-side a |
| CVE-2026-80276 | 7.5 | 2026-10-01 | Comelit Multi-User Gateway for VIP System (model 1456B) firmware versions 2.9.1 and 2.10.0 expose a network-accessible m |
| CVE-2026-81739 | 7.5 | 2026-10-01 | The Paytm Payment Gateway WordPress plugin before 2.8.9 does not sanitize and escape data it stores from payment callbac |
| CVE-2026-81809 | 7.5 | 2026-10-01 | The Paytm Payment Gateway WordPress plugin before 2.8.9 does not properly escape data taken from payment callbacks befor |
| CVE-2026-85679 | 7.2 | 2026-10-01 | The Extendify plugin for WordPress is vulnerable to Stored Cross-Site Scripting via 'styles.blocks' Block Type Key in al |
| CVE-2026-89296 | 8.6 | 2026-10-01 | The Pro Like Button WordPress plugin before 2.0 does not properly sanitize and escape a parameter before using it in a S |
| CVE-2026-92412 | 7.1 | 2026-10-01 | The Five Star Restaurant Reviews WordPress plugin before 2.3.14 does not properly escape a user-supplied value before ou |
| CVE-2026-96255 | 7.5 | 2026-10-01 | The Payments for Hubtel WordPress plugin before 1.0.2 does not prevent public access to a debug log in which it records  |
| CVE-2025-41753 | 9.8 | 2026-10-01 | The object name of a dynamically created BACnet File Object is interpreted as a file path without sufficient validation. |
| CVE-2026-15989 | 9.8 | 2026-10-01 | The Super Forms – Drag & Drop Form Builder plugin for WordPress is vulnerable to Privilege Escalation in all versions up |
| CVE-2026-19807 | 8.8 | 2026-10-01 | The ByteCoreStack – MCP Connector for AI Tools plugin for WordPress is vulnerable to Privilege Escalation in all version |
| CVE-2026-75957 | 9.8 | 2026-10-01 | The Ultimate Multisite – WordPress Multisite SaaS & WaaS Platform plugin for WordPress is vulnerable to Authentication B |
| CVE-2026-93882 | 7.5 | 2026-10-01 | The LearnPress – WordPress LMS Plugin for Create and Sell Online Courses plugin for WordPress is vulnerable to Insecure  |
| CVE-2026-103431 | 7.7 | 2026-10-01 | colmux in collectl before 4.3.20.2 does not sanitize ANSI/VT100 terminal escape sequences in data received from remote c |
| CVE-2026-14995 | 7.2 | 2026-10-01 | The Autoptimize plugin for WordPress is vulnerable to Stored Cross-Site Scripting via REQUEST_URI Path in all versions u |
| CVE-2026-15983 | 8.1 | 2026-10-01 | The Super Forms – Drag & Drop Form Builder plugin for WordPress is vulnerable to Arbitrary File/Directory Deletion in al |
| CVE-2026-85235 | 7.2 | 2026-10-01 | The Forminator Forms – Contact Form, Payment Form & Custom Form Builder plugin for WordPress is vulnerable to Stored Cro |
| CVE-2026-92244 | 7.2 | 2026-10-01 | The PDF Invoices & Packing Slips for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via B |
| CVE-2026-95687 | 8.8 | 2026-10-01 | The WPC Shop as a Customer for WooCommerce plugin for WordPress is vulnerable to privilege escalation via account takeov |
| CVE-2026-96573 | 7.2 | 2026-10-01 | The Appointment Hour Booking – Booking Calendar plugin for WordPress is vulnerable to Stored DOM-Based Cross-Site Script |
| CVE-2026-96813 | 7.2 | 2026-10-01 | The Form Maker by 10Web – Mobile-Friendly Drag & Drop Contact Form Builder plugin for WordPress is vulnerable to Stored  |
| CVE-2026-97661 | 7.2 | 2026-10-01 | The Business Essentials for Contact Form 7 plugin for WordPress is vulnerable to Stored Cross-Site Scripting via 'gatewa |
| CVE-2026-103488 | 7.1 | 2026-10-01 | In JetBrains YouTrack before 2026.2.19422 missing authorisation allowed authenticated users to add themselves to project |
| CVE-2026-103490 | 7.2 | 2026-10-01 | In JetBrains YouTrack before 2026.2.19422 privilege escalation was possible via user group links |
| CVE-2026-103493 | 8.1 | 2026-10-01 | In JetBrains YouTrack before 2026.2.19422 stored XSS via Mermaid and LaTeX content was possible |
| CVE-2026-92144 | 7.2 | 2026-10-01 | The Forminator Forms – Contact Form, Payment Form & Custom Form Builder plugin for WordPress is vulnerable to Stored Cro |
| CVE-2026-96577 | 7.1 | 2026-10-01 | A flaw was found in oc-mirror. During mirroring operations, the embedded local cache registry binds to all network inter |
| CVE-2026-103082 | 7.2 | 2026-10-01 | Server-Side Request Forgery (SSRF) vulnerability in LA-Studio LA-Studio Element Kit for Elementor lastudio-element-kit a |
| CVE-2026-103244 | 9.8 | 2026-10-01 | ground-station versions before 0.8.0 contain an authentication bypass vulnerability in the setup.restore command that al |
| CVE-2026-103246 | 7.7 | 2026-10-01 | n8n versions before 2.39.6 and 2.40.0 before 2.40.1 fail to validate credential ownership during inline agent node-tool  |
| CVE-2026-103247 | 8.5 | 2026-10-01 | n8n versions before 1.123.80 contain a credential tampering vulnerability where duplicate node IDs bypass the workflow c |
| CVE-2026-103248 | 9.0 | 2026-10-01 | n8n versions before 1.123.80, from 2.0.0 before 2.39.6, and from 2.40.0 before 2.40.1 contain a filter injection vulnera |
| CVE-2026-103249 | 7.6 | 2026-10-01 | n8n versions before 1.123.80, from 2.0.0 before 2.39.6, and from 2.40.0 before 2.40.1 contain a stored DOM cross-site sc |
| CVE-2026-103250 | 8.1 | 2026-10-01 | n8n versions before 1.123.80, from 2.0.0 before 2.39.6, and from 2.40.0 before 2.40.1 contain a NoSQL injection vulnerab |
| CVE-2026-103251 | 7.1 | 2026-10-01 | n8n versions before 1.123.80, from 2.0.0 before 2.39.6, and from 2.40.0 before 2.40.1 contain a validation bypass vulner |
| CVE-2026-103252 | 7.7 | 2026-10-01 | n8n versions before 1.123.80, from 2.0.0 before 2.39.6, and from 2.40.0 before 2.40.1 contain an authorization bypass vu |
| CVE-2026-103253 | 8.7 | 2026-10-01 | n8n versions before 1.123.80, from 2.0.0 before 2.39.6, and from 2.40.0 before 2.40.1 contain an SQL injection vulnerabi |
| CVE-2026-103255 | 9.0 | 2026-10-01 | n8n versions before 1.123.80, from 2.0.0 before 2.39.6, and from 2.40.0 before 2.40.1 contain a path traversal vulnerabi |
| CVE-2026-103256 | 7.1 | 2026-10-01 | n8n versions before 2.39.6 and 2.40.0 before 2.40.1 contain a credentials leak vulnerability in the Wekan and Baserow us |
| CVE-2026-103257 | 7.7 | 2026-10-01 | n8n versions before 1.123.80, from 2.0.0 before 2.39.6, and from 2.40.0 before 2.40.1 contain a path traversal vulnerabi |
| CVE-2026-103259 | 7.6 | 2026-10-01 | n8n versions before 2.39.6 and 2.40.0 before 2.40.1 contain a session token leakage vulnerability in the Dynamic Credent |
| CVE-2026-103262 | 7.5 | 2026-10-01 | Tornado versions before 6.5.9 contain an unbounded memory accumulation vulnerability in CurlAsyncHTTPClient that allows  |
| CVE-2026-103264 | 9.1 | 2026-10-01 | Fleet versions before 4.87.0 contain an authentication bypass vulnerability in the device API that accepts hostnames and |
| CVE-2026-103266 | 7.1 | 2026-10-01 | Ghost versions 5.2.0 through versions prior to 6.62.0 allow a remote attacker, without authentication, to abuse the Stri |
| CVE-2026-103268 | 8.8 | 2026-10-01 | Ghost versions before 6.62.0 contain an authentication bypass vulnerability that allows suspended staff users to reactiv |
| CVE-2026-103271 | 7.5 | 2026-10-01 | Ghost versions from 4.0.0 before 6.63.0 contain a content API vulnerability that allows unauthenticated visitors to acce |
| CVE-2026-103272 | 7.5 | 2026-10-01 | Ghost versions from 2.10.0 before 6.63.0 contain a staff enumeration vulnerability in the content API that allows unauth |
| CVE-2026-103277 | 8.1 | 2026-10-01 | Ghost versions from 2.5.0 before 6.34.0 contain an untrusted script execution vulnerability in the oEmbed preview featur |
| CVE-2026-103278 | 7.3 | 2026-10-01 | Ghost versions 5.8.0 before 6.34.0 contain an input validation vulnerability in the admin iframe that allows attackers t |
| CVE-2026-103283 | 8.1 | 2026-10-01 | Ghost versions 6.20.0 before 6.57.1 contain a session handling vulnerability that allows authenticated staff users to lo |
| CVE-2026-103286 | 7.3 | 2026-10-01 | Ghost versions from 2.21.0 before 6.56.0 contain a privilege escalation vulnerability in the notifications system that a |
| CVE-2026-103292 | 8.0 | 2026-10-01 | Ghost versions from 0.5.3 through versions prior to 6.50.0 fail to sanitize the data placed in the JSON-LD HTML tag emit |
| CVE-2026-103757 | 7.7 | 2026-10-01 | Budibase through 3.41.0 contains a server-side request forgery vulnerability in AI table generation because the uploadUr |
| CVE-2026-103758 | 8.1 | 2026-10-01 | Obot 0.21.1 through 0.24.1 contains an authorization bypass vulnerability that allows authenticated users to reach MCP s |
| CVE-2026-88789 | 8.6 | 2026-10-01 | Improper Restriction of XML External Entity Reference in the XSLT support extension (camel-quarkus-support-xalan) in Apa |
| CVE-2026-102379 | 8.5 | 2026-10-01 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in VillaTheme BuildKi |
| CVE-2026-103067 | 8.0 | 2026-10-01 | Cross-Site Request Forgery (CSRF) vulnerability in Memberful Memberful - Membership Plugin memberful-wp allows Cross Sit |
| CVE-2026-103338 | 8.5 | 2026-10-01 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Unlimited Elements |
| CVE-2026-62059 | 7.6 | 2026-10-01 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Ultimate Member Ul |
| CVE-2026-62060 | 7.6 | 2026-10-01 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in captivateaudio Cap |
| CVE-2026-66246 | 8.8 | 2026-10-01 | iControl is affected by a Broken Access Control vulnerability, which could allow an attacker to exploit missing authenti |
| CVE-2026-79901 | 9.9 | 2026-10-01 | In deployments using BoKS keytab management, affected versions of boks_keytabmd generate Active Directory service-accoun |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-76504 | Cisco / Catalyst SD-WAN Manager | 2026-09-30 | 2026-10-03 | Unknown |
| CVE-2026-86950 | Apple / Multiple Products | 2026-09-29 | 2026-10-02 | Unknown |
| CVE-2026-88772 | Citrix / NetScaler | 2026-09-27 | 2026-09-30 | Unknown |
| CVE-2026-88771 | Citrix / NetScaler | 2026-09-27 | 2026-09-30 | Unknown |
| CVE-2026-67279 | MikroTik / RouterOS | 2026-09-25 | 2026-09-28 | Unknown |
| CVE-2026-65660 | Microsoft / SharePoint | 2026-09-25 | 2026-09-28 | Unknown |
| CVE-2026-87902 | WordPress / Core | 2026-09-25 | 2026-09-28 | Unknown |
| CVE-2026-5430 | WSO2 / Multiple Products | 2026-09-24 | 2026-09-27 | Unknown |
| CVE-2026-71362 | Adobe / Commerce and Magento  | 2026-09-24 | 2026-09-27 | Unknown |

---

*Total entries in CISA KEV catalog: 1730*