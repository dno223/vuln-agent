# Vulnerability Intelligence Report

**Date:** 2026-11-25  
**Generated:** 2026-11-25T18:26:05Z  

---

## Executive Summary

Our environment faces significant exposure across 169 high-severity vulnerabilities, with critical concerns centered on Adobe Experience Manager (AEM) and Apache Karaf. Two AEM code injection flaws score 9.9 CVSS, enabling arbitrary code execution by low-privileged attackers. Additionally, 14 new CISA Known Exploited Vulnerabilities (KEV) were added in the past seven days, signaling active threat actor exploitation across the broader ecosystem. Immediate remediation prioritization is essential to protect business continuity, sensitive data, and regulatory standing.

---

## Risk Narrative

The current threat landscape presents compounding risk from exploitable vulnerabilities across widely deployed enterprise platforms. AEM code injection flaws offer attackers a low-barrier path to full system compromise. The 14 new KEV additions confirm that threat actors are actively weaponizing similar vulnerabilities in production environments. Exploitation of these flaws could result in data exfiltration, ransomware deployment, regulatory penalties, and reputational damage. Organizations using Drupal, HPE Juniper, and Optimizely products face imminent risk given confirmed active exploitation. Without rapid remediation, the attack surface remains critically exposed.

---

## Prioritized Action Items

1. Immediately patch or mitigate the two CVSS 9.9 AEM code injection vulnerabilities (CVE-2026-123266 and CVE-2026-132877) to eliminate arbitrary code execution risk.
2. Disable or restrict SFTP access on Apache Karaf (CVE-2026-129959) by setting sftpEnabled=false unless explicitly required for business operations.
3. Assess all 14 newly added CISA KEV entries, particularly HPE Juniper and Drupal Core, and apply available patches within 24-48 hours per federal guidance.
4. Remediate remaining high-severity AEM vulnerabilities including stored XSS and template injection flaws to prevent privilege escalation and session hijacking.
5. Implement compensating controls such as web application firewall rules and enhanced privilege monitoring while long-term patching cycles are completed.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-119579 | 8.7 | 2026-11-24 | Adobe Experience Manager is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by a low- |
| CVE-2026-121357 | 8.7 | 2026-11-24 | Adobe Experience Manager is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by a low- |
| CVE-2026-123253 | 8.7 | 2026-11-24 | Adobe Experience Manager is affected by an Improper Neutralization of Special Elements Used in a Template Engine vulnera |
| CVE-2026-123256 | 7.1 | 2026-11-24 | Adobe Experience Manager is affected by an Incorrect Authorization vulnerability that could result in a Security feature |
| CVE-2026-123266 | 9.9 | 2026-11-24 | Adobe Experience Manager is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that  |
| CVE-2026-129959 | 8.8 | 2026-11-24 | When sftpEnabled=true (the default configuration in etc/org.apache.karaf.shell.cfg), the SSH server exposes the karaf.ba |
| CVE-2026-132877 | 9.9 | 2026-11-24 | Adobe Experience Manager is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that  |
| CVE-2026-134066 | 7.3 | 2026-11-24 | Improper neutralization of special elements in data query logic in the query construction of AWS Graph Explorer before 3 |
| CVE-2026-134068 | 7.5 | 2026-11-24 | A stack-based buffer overflow in the replication origin name parsing component in AWS pgactive before 2.1.10 might allow |
| CVE-2026-134716 | 8.8 | 2026-11-24 | Cross-Site Request Forgery (CSRF) vulnerability in Mahmudul Hasan Arif Ninja Charts ninja-charts allows Cross Site Reque |
| CVE-2026-134986 | 8.8 | 2026-11-24 | Cross-Site Request Forgery (CSRF) vulnerability in Brainstorm Force SureCart surecart allows Cross Site Request Forgery. |
| CVE-2026-135794 | 9.9 | 2026-11-24 | A vulnerability was determined in Panabit Smart Application Gateway TANGr7p10. The affected element is the function add_ |
| CVE-2026-135796 | 9.9 | 2026-11-24 | A vulnerability was determined in Volans NGFW Next-Generation Firewall r5.1. This issue affects the function exec/system |
| CVE-2026-135797 | 10.0 | 2026-11-24 | A vulnerability was identified in Volans NGFW Next-Generation Firewall r5.1. Impacted is the function exec of the file s |
| CVE-2026-135798 | 7.3 | 2026-11-24 | A security flaw has been discovered in Volans NGFW Next-Generation Firewall r5.1. The affected element is an unknown fun |
| CVE-2026-136404 | 9.8 | 2026-11-24 | ntop n2n supernode 3.0 through 3.1.1 contains a stack-based buffer overflow vulnerability that allows remote unauthentic |
| CVE-2026-136410 | 9.0 | 2026-11-24 | Thymeleaf before 3.1.6.RELEASE contains a restricted expression mode bypass vulnerability that allows unauthenticated re |
| CVE-2026-136411 | 9.8 | 2026-11-24 | BusyBox through 1.38.0 contains an absolute path traversal vulnerability in tftpd that allows unauthenticated remote att |
| CVE-2026-136412 | 8.1 | 2026-11-24 | OpenResty stream-lua-nginx-module before 0.0.20rc4 contains a use-after-free vulnerability that allows remote peers to t |
| CVE-2026-136422 | 7.8 | 2026-11-24 | Soda PDF Desktop PDF File Parsing Memory Corruption Remote Code Execution Vulnerability. This vulnerability allows remot |
| CVE-2026-136423 | 7.8 | 2026-11-24 | Soda PDF Desktop PDF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability. This vulnerability allows rem |
| CVE-2026-136424 | 7.8 | 2026-11-24 | Soda PDF Desktop PDF File Parsing Memory Corruption Remote Code Execution Vulnerability. This vulnerability allows remot |
| CVE-2026-136425 | 7.8 | 2026-11-24 | Soda PDF Desktop App Object Use-After-Free Remote Code Execution Vulnerability. This vulnerability allows remote attacke |
| CVE-2026-136426 | 7.8 | 2026-11-24 | PyTorch Foundation PyTorch PT2 File Parsing Code Injection Remote Code Execution Vulnerability. This vulnerability allow |
| CVE-2026-136427 | 7.8 | 2026-11-24 | PyTorch Foundation PyTorch AOTIModelPackageLoader Command Injection Remote Code Execution Vulnerability. This vulnerabil |
| CVE-2026-136428 | 7.8 | 2026-11-24 | PyTorch Foundation PyTorch load_compiled_function Deserialization of Untrusted Data Remote Code Execution Vulnerability. |
| CVE-2026-136429 | 7.0 | 2026-11-24 | PyTorch Foundation PyTorch PT2 File Parsing Exposed Dangerous Method Remote Code Execution Vulnerability. This vulnerabi |
| CVE-2026-136430 | 7.8 | 2026-11-24 | PyTorch Foundation PyTorch AOTIModelPackageLoader  Directory Traversal Remote Code Execution Vulnerability. This vulnera |
| CVE-2026-136431 | 7.8 | 2026-11-24 | PyTorch Foundation PyTorch load_state_dict_from_url Deserialization of Untrusted Data Remote Code Execution Vulnerabilit |
| CVE-2026-136432 | 7.8 | 2026-11-24 | PyTorch Foundation PyTorch FileSystemReader Deserialization of Untrusted Data Remote Code Execution Vulnerability. This  |
| CVE-2026-136433 | 7.8 | 2026-11-24 | PyTorch Foundation PyTorch torch_save_to_dcp Deserialization of Untrusted Data Remote Code Execution Vulnerability. This |
| CVE-2026-136434 | 9.8 | 2026-11-24 | Super Magic PHPSandbox Command Injection Sandbox Escape Vulnerability. This vulnerability allows remote attackers to byp |
| CVE-2026-136435 | 7.8 | 2026-11-24 | DeepSpeed InferenceEngine Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vulnerability allo |
| CVE-2026-136436 | 7.8 | 2026-11-24 | DeepSpeed torch_checkpoint_engine Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vulnerabil |
| CVE-2026-136437 | 7.8 | 2026-11-24 | DeepSpeed parse_optim_states Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vulnerability a |
| CVE-2026-136438 | 7.8 | 2026-11-24 | DeepSpeed build_engine_from_ds_checkpoint Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vu |
| CVE-2026-136439 | 7.8 | 2026-11-24 | DeepSpeed _get_zero_stage Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vulnerability allo |
| CVE-2026-136440 | 7.3 | 2026-11-24 | Python Packaging Authority pip Configuration File Incorrect Permission Assignment Local Privilege Escalation Vulnerabili |
| CVE-2026-136441 | 9.8 | 2026-11-24 | Bytebase DBHub MCP Incorrect Authorization Authentication Bypass Vulnerability. This vulnerability allows remote attacke |
| CVE-2026-112732 | 9.8 | 2026-11-24 | Double free in Microsoft Office Visio allows an unauthorized attacker to execute code over a network. |
| CVE-2026-123215 | 9.8 | 2026-11-24 | Copeland XWEB Pro contains a missing authentication vulnerability. Fixed in 1.16.1. |
| CVE-2026-123216 | 9.6 | 2026-11-24 | Copeland XWEB Pro contains an OS command injection vulnerability that allows a remote, authenticated attacker to execute |
| CVE-2026-123340 | 9.6 | 2026-11-24 | Copeland XWEB Pro contains an OS command injection vulnerability that allows a remote, authenticated attacker to execute |
| CVE-2026-135046 | 8.8 | 2026-11-24 | Cross-Site Request Forgery (CSRF) vulnerability in Rymera Web Co Store Exporter woocommerce-exporter allows Cross Site R |
| CVE-2026-135800 | 7.3 | 2026-11-24 | A flaw has been found in hiyouga LLaMA-Factory up to 0.9.5. Affected is the function save_args/load_args of the file src |
| CVE-2026-136328 | 7.8 | 2026-11-24 | A flaw was found in the file-psd plugin in GIMP. When processing a specially crafted PSD (Photoshop Document) image file |
| CVE-2026-136455 | 8.8 | 2026-11-24 | borg-ui before 2.4.1 contains a privilege escalation vulnerability that allows a repository-scoped operator to escalate  |
| CVE-2026-132264 | 8.1 | 2026-11-24 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agent |
| CVE-2026-133453 | 9.1 | 2026-11-24 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agent |
| CVE-2026-135810 | 7.3 | 2026-11-24 | A vulnerability was identified in GongShengyue OnlineBooks up to dfc5eacc08d3b0396c266049548618f6fb9587ea. This vulnerab |
| CVE-2026-136522 | 9.6 | 2026-11-24 | CubeWP Forms before 1.1.13 contains an unauthenticated stored cross-site scripting vulnerability that allows attackers t |
| CVE-2026-136534 | 7.3 | 2026-11-24 | Devin Desktop Uncontrolled Search Path Element Local Privilege Escalation Vulnerability. This vulnerability allows local |
| CVE-2026-136535 | 7.2 | 2026-11-24 | LiteLLM MCP Command Injection Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute |
| CVE-2026-136539 | 7.2 | 2026-11-24 | LiteLLM Pass-Through Endpoint Code Injection Remote Code Execution Vulnerability. This vulnerability allows remote attac |
| CVE-2026-61512 | 7.0 | 2026-11-24 | VeraCrypt before 1.26.30 on Linux contains a command injection vulnerability in CoreUnix::CheckFilesystem that allows a  |
| CVE-2026-61513 | 7.0 | 2026-11-24 | VeraCrypt through 1.26.31 on Linux contains an improper path restriction vulnerability in the elevated CoreService, whic |
| CVE-2026-124284 | 9.8 | 2026-11-24 | A critical security vulnerability affects certain authentication methods in Genetec Security Center, including external  |
| CVE-2026-133456 | 7.5 | 2026-11-24 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agent |
| CVE-2026-135814 | 7.4 | 2026-11-24 | A vulnerability has been found in zhblue hustoj up to 26.08.19. This impacts an unknown function of the file trunk/core/ |
| CVE-2026-16663 | 8.4 | 2026-11-24 | MCUboot's encrypted serial-recovery path contains an attacker-controlled out-of-bounds stack write in decrypt_region_inp |
| CVE-2026-16665 | 7.4 | 2026-11-24 | Summary

MCUboot enforces several security-critical invariants on the boot, image-swap, and validation paths using asser |
| CVE-2026-136134 | 7.3 | 2026-11-24 | A flaw has been found in mealie-recipes Mealie up to 3.29.0. Affected is the function get of the file mealie/pkgs/i18n/p |
| CVE-2026-136613 | 7.5 | 2026-11-24 | GNU Inetutils FTP Client File Retrieval Command Injection Remote Code Execution Vulnerability. This vulnerability allows |
| CVE-2026-133462 | 8.7 | 2026-11-25 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agent |
| CVE-2026-136136 | 10.0 | 2026-11-25 | A vulnerability was identified in Netis WF2409E up to 20261026. Affected by this issue is some unknown functionality of  |
| CVE-2026-136448 | 7.3 | 2026-11-25 | A vulnerability was identified in nliautaud pico-content-editor up to 02d5ad6c820c5050c542ab9505819b5e0a0ba1af. Affected |
| CVE-2026-136620 | 7.1 | 2026-11-25 | pain001-mcp 0.0.72 before 0.0.80 contains a path traversal vulnerability in the commit_payment_batch MCP tool that allow |
| CVE-2026-136626 | 8.2 | 2026-11-25 | SRS 4.0.0 before 6.0.194, 7.0.0 before 7.0.214, and 8.0.0 before 8.0.73 contains a heap-based buffer overflow in SrsRtcp |
| CVE-2026-136627 | 7.5 | 2026-11-25 | SRS 4.0.0 before 6.0.194, 7.0.0 before 7.0.214, and 8.0.0 before 8.0.73 contains a reachable assertion in RTCP decoding  |
| CVE-2026-136628 | 7.1 | 2026-11-25 | Wails before 2.17.1 on Linux contains an origin validation error in the sendMessageToBackend WebKitGTK handler that allo |
| CVE-2026-136629 | 7.8 | 2026-11-25 | Nektos act 0.2.92 before 0.2.95 contains an argument injection vulnerability in readProjectArgsFile and projectFlag that |
| CVE-2026-136630 | 7.5 | 2026-11-25 | Electerm before 5.9.0 contains an origin validation vulnerability in the MCP Server widget that allows remote attackers  |
| CVE-2026-136632 | 8.3 | 2026-11-25 | OpenProject 17.2.0 before 17.5.2, 17.6.0 before 17.6.1, 17.7.0 before 17.7.3, 17.8.0 before 17.8.2, and 17.9.0 before 17 |
| CVE-2026-124606 | 7.5 | 2026-11-25 | Improper Limitation of a Pathname to a Restricted Directory Vulnerability in Cosminexus Component Container.

This issue |
| CVE-2026-134283 | 7.5 | 2026-11-25 | Webmin through 2.670 contains an improper certificate validation vulnerability in the http_download function of web-lib- |
| CVE-2026-134326 | 7.5 | 2026-11-25 | Webmin through 2.670 contains a signature verification bypass vulnerability in webmin-lib.pl that allows attackers to in |
| CVE-2026-134438 | 7.5 | 2026-11-25 | Webmin through 2.670 contains an insecure download vulnerability in webmin/upgrade.cgi, cluster-webmin/upgrade.cgi and c |
| CVE-2026-134630 | 7.5 | 2026-11-25 | Webmin through 2.670 contains a remote code execution vulnerability in the Perl Modules (cpan) module, which downloads C |
| CVE-2026-134638 | 7.5 | 2026-11-25 | Webmin through 2.670 contains a missing integrity verification vulnerability in usermin/upgrade.cgi that downloads Userm |
| CVE-2026-134639 | 8.1 | 2026-11-25 | Webmin through 2.670 contains an insecure default configuration in its Windows setup.bat script that provisions an admin |
| CVE-2026-134642 | 7.5 | 2026-11-25 | Webmin through 2.670 contains a missing authentication vulnerability in fastrpc.cgi that allows unauthenticated network  |
| CVE-2026-134644 | 7.4 | 2026-11-25 | Webmin through 2.670 contains a path traversal vulnerability in minecraft/minecraft-lib.pl that allows unauthenticated g |
| CVE-2026-134647 | 7.5 | 2026-11-25 | Webmin through 2.670 contains a cleartext transmission vulnerability in web-lib-funcs.pl and fastrpc.cgi that sends clus |
| CVE-2026-130336 | 7.5 | 2026-11-25 | Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection') in the HWBridge custom methods co |
| CVE-2026-136547 | 10.0 | 2026-11-25 | A vulnerability was determined in Tenda RX3 16.03.13.11_multi. Impacted is the function R7WebsSecurityHandler of the com |
| CVE-2026-136548 | 10.0 | 2026-11-25 | A vulnerability was identified in Tenda RX3 16.03.13.11. The affected element is an unknown function of the file /bin/au |
| CVE-2026-136549 | 10.0 | 2026-11-25 | A security flaw has been discovered in Tenda RX3 16.03.13.11_multi. The impacted element is the function formSetSafeWanW |
| CVE-2026-136550 | 9.1 | 2026-11-25 | A weakness has been identified in Tenda RX3 16.03.13.11_multi. This affects the function fromAdvSetMacMtuWan of the file |
| CVE-2026-136552 | 9.1 | 2026-11-25 | A security vulnerability has been detected in Tenda RX3 16.03.13.11_multi. This impacts the function formSetIPv6status o |
| CVE-2026-136553 | 10.0 | 2026-11-25 | A vulnerability was detected in Tenda RX3 16.03.13.11_multi. Affected is an unknown function of the file /goform/fast_se |
| CVE-2026-134473 | 8.8 | 2026-11-25 | Cross-Site Request Forgery (CSRF) vulnerability in WP ManageNinja LLC WP Social Ninja wp-social-reviews allows Cross Sit |
| CVE-2026-134475 | 8.8 | 2026-11-25 | Cross-Site Request Forgery (CSRF) vulnerability in WPManageNinja FluentCart fluent-cart allows Cross Site Request Forger |
| CVE-2026-134476 | 8.8 | 2026-11-25 | Cross-Site Request Forgery (CSRF) vulnerability in WP ManageNinja LLC Fluent Support fluent-support allows Cross Site Re |
| CVE-2026-134478 | 8.8 | 2026-11-25 | Cross-Site Request Forgery (CSRF) vulnerability in WP ManageNinja LLC Fluent CRM fluent-crm allows Cross Site Request Fo |
| CVE-2026-134942 | 8.8 | 2026-11-25 | Cross-Site Request Forgery (CSRF) vulnerability in 10up ElasticPress elasticpress allows Cross Site Request Forgery.This |
| CVE-2026-80247 | 8.4 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains a Missing Authentication for C |
| CVE-2026-134706 | 8.8 | 2026-11-25 | Cross-Site Request Forgery (CSRF) vulnerability in Soroseo Soro &#8211; SEO Autopilot &amp; AI Content Writer soro-seo a |
| CVE-2026-135008 | 8.8 | 2026-11-25 | Cross-Site Request Forgery (CSRF) vulnerability in Tainacan Community Tainacan tainacan allows Cross Site Request Forger |
| CVE-2026-135040 | 8.8 | 2026-11-25 | Cross-Site Request Forgery (CSRF) vulnerability in Themefic Hydra Booking hydra-booking allows Cross Site Request Forger |
| CVE-2026-135049 | 8.8 | 2026-11-25 | Cross-Site Request Forgery (CSRF) vulnerability in Brainstorm Force Presto Player presto-player allows Cross Site Reques |
| CVE-2026-135840 | 8.8 | 2026-11-25 | Cross-Site Request Forgery (CSRF) vulnerability in Arraytics Timetics timetics allows Cross Site Request Forgery.This is |
| CVE-2026-80267 | 7.8 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains a Use of Hard-coded Credential |
| CVE-2026-80269 | 7.3 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains an Insecure Temporary File vul |
| CVE-2026-80271 | 7.8 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains a Use of Hard-coded Cryptograp |
| CVE-2026-80273 | 8.4 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains an Improper Neutralization of  |
| CVE-2026-80283 | 8.4 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains a Missing Authentication for C |
| CVE-2026-80284 | 7.7 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains an Improper Authentication vul |
| CVE-2026-80285 | 7.8 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains an Execution with Unnecessary  |
| CVE-2026-135932 | 8.8 | 2026-11-25 | Cross-Site Request Forgery (CSRF) vulnerability in WP ManageNinja LLC FluentBoards fluent-boards allows Cross Site Reque |
| CVE-2026-135937 | 8.8 | 2026-11-25 | Cross-Site Request Forgery (CSRF) vulnerability in Groundhogg Groundhogg groundhogg allows Cross Site Request Forgery.Th |
| CVE-2026-135959 | 8.8 | 2026-11-25 | Cross-Site Request Forgery (CSRF) vulnerability in Paul Shield Security wp-simple-firewall allows Cross Site Request For |
| CVE-2026-87753 | 8.1 | 2026-11-25 | Authorization bypass through User-Controlled key vulnerability in İdeal Data Finansal Teknolojiler A.Ş. IDeal WEB allows |
| CVE-2026-125812 | 9.8 | 2026-11-25 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in WP Media WP Rocket wp-ro |
| CVE-2026-136692 | 7.3 | 2026-11-25 | A vulnerability was identified in dayrui XunRuiCMS up to 4.7.4. The impacted element is the function down of the file da |
| CVE-2026-80286 | 7.3 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains an External Control of File Na |
| CVE-2026-80287 | 8.4 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains a Missing Authentication for C |
| CVE-2026-80291 | 8.4 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains a Missing Authentication for C |
| CVE-2026-80296 | 7.3 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains a Path Traversal vulnerability |
| CVE-2026-80297 | 7.3 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains a Path Traversal vulnerability |
| CVE-2026-80361 | 8.4 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains a Missing Authentication for C |
| CVE-2026-80363 | 7.8 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains a Use of Hard-coded Credential |
| CVE-2026-80364 | 7.8 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains a Download of Code Without Int |
| CVE-2026-80365 | 7.8 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains a Use of Externally-Controlled |
| CVE-2026-80367 | 8.4 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains an Out-of-bounds Write vulnera |
| CVE-2026-80369 | 7.8 | 2026-11-25 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains an Uncontrolled Search Path El |
| CVE-2026-133742 | 8.2 | 2026-11-25 | Incorrect permission assignment for critical resource in the media management functionality of Progress Software Sitefin |
| CVE-2026-134873 | 8.8 | 2026-11-25 | Cross-Site Request Forgery (CSRF) vulnerability in Brainstorm Force CartFlows cartflows allows Cross Site Request Forger |
| CVE-2026-134945 | 8.8 | 2026-11-25 | Cross-Site Request Forgery (CSRF) vulnerability in Brainstorm Force SureForms sureforms allows Cross Site Request Forger |
| CVE-2026-135985 | 8.8 | 2026-11-25 | Cross-Site Request Forgery (CSRF) vulnerability in John-Michael L'Allier Create mediavine-create allows Cross Site Reque |
| CVE-2026-136694 | 7.3 | 2026-11-25 | A weakness has been identified in eosphoros-ai DB-GPT up to 0.8.2. This impacts the function skill_upload of the file pa |
| CVE-2026-136916 | 8.1 | 2026-11-25 | HortusFox (hortusfox-web) through 6.4 contains a password reset poisoning vulnerability in UserModel::restorePassword th |
| CVE-2026-136918 | 7.8 | 2026-11-25 | FCEUX before 2.8.0 contains an integer overflow in SetBoardName() in src/unif.cpp that allows crafted UNIF ROM files to  |
| CVE-2026-136919 | 7.8 | 2026-11-25 | FCEUX 2.5.0 before 2.8.0 contains an integer overflow in iNESLoad() in src/ines.cpp that allows a crafted NES 2.0 ROM to |
| CVE-2026-136920 | 8.1 | 2026-11-25 | OneDev before 17.2.4 contains an argument injection vulnerability in commit query handling that allows authenticated att |
| CVE-2026-136922 | 7.8 | 2026-11-25 | PyBioNetGen 0.8.7 contains a code injection vulnerability in ParameterBlock.add_item() and ModelBlock.add_item() that al |
| CVE-2026-136923 | 7.8 | 2026-11-25 | asar-py before 0.1.4 contains a path traversal vulnerability in AsarArchive.extract() and extract_archive() that allows  |
| CVE-2026-82489 | 9.8 | 2026-11-25 | openIMIS before 2026-10 contains an unauthenticated remote code execution vulnerability in the report module (openimis-b |
| CVE-2026-82490 | 8.8 | 2026-11-25 | openIMIS before 2026-10 contains a missing authorization vulnerability in the OpenSearch reporting dashboard proxy, wher |
| CVE-2026-82491 | 8.8 | 2026-11-25 | openIMIS before 2026-10 contains an information disclosure vulnerability in the core export mixin (openimis-be-core_py,  |
| CVE-2026-82492 | 8.8 | 2026-11-25 | openIMIS before 2026-10 contains an improper validation vulnerability in the deduplication service (openimis-be-deduplic |
| CVE-2026-82493 | 8.8 | 2026-11-25 | openIMIS before 2026-10 contains a remote code execution vulnerability in the report module's overrideReport GraphQL mut |
| CVE-2026-82495 | 8.1 | 2026-11-25 | openIMIS before 2026-10 contains a broken access control vulnerability in the FHIR R4 module that allows any authenticat |
| CVE-2026-127280 | 7.8 | 2026-11-25 | C-More EA9 Programming Software V6.80 does not adequately validate data read from a project file before using it in heap |
| CVE-2026-64845 | 8.8 | 2026-11-25 | KubeSphere 4.0.0 through 4.1.3 contains a missing authorization vulnerability in the CertificateSigningRequest controlle |
| CVE-2026-132888 | 7.5 | 2026-11-25 | A flaw was found in librelp. When configured to use Transport Layer Security (TLS) with certificate validation and the G |
| CVE-2026-135133 | 7.8 | 2026-11-25 | An invalid memory release in the MongoDB PHP Driver extension occurs when certain string-typed options or type-mapping s |
| CVE-2026-135144 | 8.1 | 2026-11-25 | A query builder component in a MongoDB integration library for a PHP web framework does not run the query-modification c |
| CVE-2026-135145 | 8.1 | 2026-11-25 | A polymorphic relationship query helper in the MongoDB Eloquent integration for Laravel resolves a record's type identif |
| CVE-2026-135147 | 8.2 | 2026-11-25 | A data-query neutralization weakness in the query builder of the MongoDB integration for a PHP web framework allows valu |
| CVE-2026-135224 | 9.1 | 2026-11-25 | The MongoDB C Driver does not confirm that the party signing a supplied certificate revocation status response is author |
| CVE-2026-135399 | 8.8 | 2026-11-25 | Ever Gauzy is an open source business management platform for ERP, CRM, HRM, ATS, and project management. Prior to 111.4 |
| CVE-2026-135400 | 9.8 | 2026-11-25 | Ever Gauzy is an open source business management platform for ERP, CRM, HRM, ATS, and project management. Prior to 111.4 |
| CVE-2026-135402 | 8.6 | 2026-11-25 | Ever Gauzy is an open source business management platform for ERP, CRM, HRM, ATS, and project management. Prior to 111.4 |
| CVE-2026-135403 | 7.4 | 2026-11-25 | Ever Gauzy is an open source business management platform for ERP, CRM, HRM, ATS, and project management. Prior to 111.4 |
| CVE-2026-135404 | 7.1 | 2026-11-25 | Ever Gauzy is an open source business management platform for ERP, CRM, HRM, ATS, and project management. Prior to 111.4 |
| CVE-2026-136267 | 8.8 | 2026-11-25 | Improper sanitization of mixed data and markup elements when processing content in Kiro Web before 2026-10-30, in combin |
| CVE-2026-136329 | 7.8 | 2026-11-25 | A flaw was found in the file-gif-load plugin in GIMP. When processing a specially crafted JIF image file, a 32-bit integ |
| CVE-2026-136696 | 7.3 | 2026-11-25 | A vulnerability was detected in Zhengzhou Weiwei Information Technology mayicms up to 5.8E. Affected by this vulnerabili |
| CVE-2026-136834 | 8.8 | 2026-11-25 | Sandbox protection in Jenkins Pipeline: Groovy Plugin 4403.v471713a_cea_19 and earlier can be circumvented through inter |
| CVE-2026-136835 | 9.9 | 2026-11-25 | Jenkins Script Security Plugin 1436.v1082791135e4 and earlier does not reject @Builder annotations whose builderStrategy |
| CVE-2026-136836 | 7.1 | 2026-11-25 | Jenkins Gradle Plugin 2.21.1282.v024680ce00a_b_ and earlier does not configure its XML parser to prevent XML external en |
| CVE-2026-136837 | 8.8 | 2026-11-25 | Jenkins Warnings Plugin 13.10251.va_452d3553728 through 13.10365.v85cd7a_c8110b_ (both inclusive) allows defining inline |
| CVE-2026-73517 | 8.8 | 2026-11-25 | KubeSphere 4.0.0 through 4.1.3 contains a command injection vulnerability in the terminal v1alpha2 file download endpoin |
| CVE-2026-135141 | 8.1 | 2026-11-25 | A logic flaw in the query-building layer of the Mongoid object-document mapper causes a model-level default restriction  |
| CVE-2026-135146 | 7.4 | 2026-11-25 | An improper certificate revocation check in the MongoDB Python Driver's optional TLS revocation-checking support allows  |
| CVE-2026-135226 | 7.5 | 2026-11-25 | A type-confusion weakness in the Extended JSON parsing component of BSON for Ruby allows a party who can supply parser i |
| CVE-2026-135227 | 8.2 | 2026-11-25 | An improper restriction of dynamically determined object attributes in the object-document mapping library's association |
| CVE-2026-135898 | 8.2 | 2026-11-25 | An out-of-bounds read in the native C BSON decoding extension of the MongoDB Python Driver may allow an unauthenticated  |
| CVE-2026-136722 | 7.3 | 2026-11-25 | A vulnerability was identified in Zhengzhou Weiwei Information Technology mayicms up to 5.8E. This vulnerability affects |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-103406 | Hewlett Packard Enterprise (HPE) / Juniper Session Smart Conductor and Session Smart Router | 2026-11-25 | 2026-11-28 | Unknown |
| CVE-2026-132224 | Optimizely / Web Experimentation | 2026-11-24 | 2026-11-27 | Unknown |
| CVE-2026-131914 | Idunno / AntiCsrf | 2026-11-24 | 2026-11-27 | Unknown |
| CVE-2026-132165 | Drupal / Core | 2026-11-24 | 2026-11-27 | Unknown |
| CVE-2026-133968 | Project MONAI / MONAI Label | 2026-11-23 | 2026-11-26 | Unknown |
| CVE-2026-134624 | N-able / MailAssure | 2026-11-23 | 2026-11-26 | Unknown |
| CVE-2026-129448 | Apache / Roller | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2026-123890 | Broadcom / VMware vCenter | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2025-42884 | SAP / NetWeaver | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2026-76466 | Cisco / Expressway Series | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2024-10441 | Synology / DiskStation Manager (DSM) | 2026-11-18 | 2026-11-21 | Known |
| CVE-2026-40217 | BerriAI / LiteLLM | 2026-11-18 | 2026-12-02 | Unknown |
| CVE-2026-90817 | Vanderbilt University / Research Electronic Data Capture (REDCap) | 2026-11-18 | 2026-11-21 | Unknown |
| CVE-2026-90436 | Apache / Axis | 2026-11-18 | 2026-11-21 | Unknown |

---

*Total entries in CISA KEV catalog: 1796*