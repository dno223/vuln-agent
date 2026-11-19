# Vulnerability Intelligence Report

**Date:** 2026-11-19  
**Generated:** 2026-11-19T17:03:35Z  

---

## Executive Summary

Our environment faces critical exposure across 242 high-severity vulnerabilities, with the most urgent risks centered on JetBrains TeamCity remote code execution flaws scoring 9.9 CVSS, a Zyrabit Platform path traversal at 9.1, and Dell PowerStore storage vulnerabilities reaching 9.6. Seven new CISA Known Exploited Vulnerabilities were added this week, including Synology DSM and Apache Axis, signaling active threat actor exploitation in the wild. Immediate patching and compensating controls are required to prevent ransomware, data exfiltration, and supply chain compromise across development and storage infrastructure.

---

## Risk Narrative

Threat actors are actively targeting development pipelines, storage systems, and AI infrastructure platforms. The JetBrains TeamCity RCE trio represents a severe supply chain risk, as CI/CD compromise enables adversaries to inject malicious code into production builds. CISA KEV additions for Synology DSM and Apache Axis confirm exploitation campaigns targeting network-attached storage and legacy middleware. Dell PowerStore vulnerabilities expose core enterprise storage to peer-level attacks. The Zyrabit and sqlite-mcp flaws highlight emerging risk in AI and MCP ecosystems where security controls are immature. Collectively, these exposures create pathways for ransomware deployment, intellectual property theft, and persistent access across on-premises and cloud-hybrid environments, amplifying potential business disruption and regulatory liability.

---

## Prioritized Action Items

1. Patch JetBrains TeamCity to version 2026.1.3 or 2025.11.7 immediately to remediate three CVSS 9.9 remote code execution vulnerabilities exploitable via Perforce integration.
2. Apply Dell PowerStore SDNAS firmware updates to address the CVSS 9.6 out-of-bounds write and CVSS 8.1 authentication-bypass vulnerabilities affecting storage infrastructure.
3. Audit and remediate all seven newly added CISA KEV entries, prioritizing Synology DSM and Apache Axis as these indicate confirmed active exploitation.
4. Upgrade Zyrabit Platform to version 2.4.4 or later and restrict vault import permissions to close the CVSS 9.1 path traversal vulnerability in enterprise RAG infrastructure.
5. Enforce network segmentation and application-layer controls around sqlite-mcp and ownCloud Desktop Client to limit blast radius while patches are scheduled and deployed.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2025-64441 | 8.9 | 2026-11-18 | The ownCloud Desktop Client synchronizes files between an ownCloud server and a desktop. Prior to 6.0.2, an authenticate |
| CVE-2026-116441 | 9.6 | 2026-11-18 | Dell PowerStore SDNAS contains an out-of-bounds write vulnerability in the storage-processor interconnect driver that co |
| CVE-2026-116442 | 8.1 | 2026-11-18 | Dell PowerStore SDNAS contains an authentication-bypass-by-replay vulnerability in the NAS NDMP service that could allow |
| CVE-2026-126675 | 7.3 | 2026-11-18 | Incorrect default permissions in Nitro PDF Pro before 26.4 on Windows allow a local low-privileged user to execute code  |
| CVE-2026-130008 | 8.2 | 2026-11-18 | sqlite-mcp is a Model Context Protocol server for SQLite. Prior to 0.1.2, the default read-only mode can be bypassed thr |
| CVE-2026-130154 | 9.1 | 2026-11-18 | Zyrabit Platform provides sovereign AI infrastructure for enterprise retrieval-augmented generation. Prior to 2.4.4, imp |
| CVE-2026-130156 | 9.4 | 2026-11-18 | Bazarr is a companion application to Sonarr and Radarr. Prior to 1.6.3-beta.11, the /api/subtitles/subtitles-info handle |
| CVE-2026-132231 | 9.9 | 2026-11-18 | In JetBrains TeamCity before 2026.1.3, 2025.11.7 remote code execution was possible via best-fit character mapping in Pe |
| CVE-2026-132232 | 9.9 | 2026-11-18 | In JetBrains TeamCity before 2026.1.3, 2025.11.7 remote code execution was possible via argument injection in Perforce s |
| CVE-2026-132233 | 9.9 | 2026-11-18 | In JetBrains TeamCity before 2026.1.3, 2025.11.7 remote code execution was possible via build attribute injection |
| CVE-2026-132234 | 9.9 | 2026-11-18 | In JetBrains TeamCity before 2026.1.3, 2025.11.7 remote code execution was possible via argument injection in Mercurial  |
| CVE-2026-132235 | 7.2 | 2026-11-18 | In JetBrains TeamCity before 2026.1.3, 2025.11.7 remote code execution was possible via path traversal in project import |
| CVE-2026-132236 | 8.8 | 2026-11-18 | In JetBrains TeamCity before 2026.1.3, 2025.11.7 remote code execution was possible via path traversal in the pipeline Y |
| CVE-2026-132237 | 8.8 | 2026-11-18 | In JetBrains TeamCity before 2026.1.3, 2025.11.7 remote code execution was possible via path traversal in the external a |
| CVE-2026-132238 | 7.7 | 2026-11-18 | In JetBrains TeamCity before 2026.1.3, 2025.11.8 disclosure of password parameter values to project viewers was possible |
| CVE-2026-132239 | 7.6 | 2026-11-18 | In JetBrains TeamCity before 2026.1.3, 2025.11.7 missing authorization in the Kubernetes integration allowed project vie |
| CVE-2026-132240 | 7.7 | 2026-11-18 | In JetBrains TeamCity before 2026.1.3, 2025.11.7 XXE via Maven settings file upload was possible |
| CVE-2026-132241 | 7.3 | 2026-11-18 | In JetBrains TeamCity before 2026.1.3, 2025.11.7 XXE in the .NET build steps auto-discovery was possible |
| CVE-2026-132242 | 7.6 | 2026-11-18 | In JetBrains TeamCity before 2026.1.3, 2025.11.7 stored XSS in the Promote build dialog was possible |
| CVE-2026-132243 | 7.6 | 2026-11-18 | In JetBrains TeamCity before 2026.1.3, 2025.11.7 stored XSS on the Docker Container Info tab was possible |
| CVE-2026-132244 | 8.1 | 2026-11-18 | In JetBrains TeamCity before 2026.1.3, 2025.11.7 stored XSS on the Disk Usage and Build Time pages was possible |
| CVE-2026-132245 | 7.5 | 2026-11-18 | In JetBrains TeamCity before 2026.1.3, 2025.11.7 DoS via agent command results was possible |
| CVE-2026-76411 | 7.5 | 2026-11-18 | A vulnerability in the phishcheck functionality of ClamAV could allow an unauthenticated, remote attacker to cause a DoS |
| CVE-2026-76414 | 7.5 | 2026-11-18 | A vulnerability in Microsoft Compiled HTML Help (CHM) file scanning of ClamAV could allow an unauthenticated, remote att |
| CVE-2026-76415 | 7.5 | 2026-11-18 | A vulnerability in the Yoda'a Crytper (yC) Portable Executable (PE) unpacker of ClamAV could allow an unauthenticated, r |
| CVE-2026-76416 | 7.5 | 2026-11-18 | A vulnerability in the InstallShield file parser of ClamAV could allow an unauthenticated, remote attacker to cause a Do |
| CVE-2026-76417 | 7.5 | 2026-11-18 | A vulnerability in Object Linking and Embedding, 2nd Generation (OLE2) file parser for ClamAV could allow an unauthentic |
| CVE-2026-76421 | 7.5 | 2026-11-18 | A vulnerability in the LZX data algorithm for Microsoft Compiled HTML Help (CHM) file scanning in ClamAV could allow an  |
| CVE-2026-76422 | 7.5 | 2026-11-18 | A vulnerability in the debug logging functionality of ClamAV could allow an unauthenticated, remote attacker to cause a  |
| CVE-2026-76430 | 7.5 | 2026-11-18 | A vulnerability in the Ultimate Packer for eXecutables (UPX) unpacker of ClamAV could allow an unauthenticated, remote a |
| CVE-2026-76515 | 7.5 | 2026-11-18 | A vulnerability in the Object Linking and Embedding, 2nd Generation (OLE2) file parser for ClamAV could allow an unauthe |
| CVE-2026-76516 | 7.5 | 2026-11-18 | A vulnerability in the eXtensible ARchive (XAR) GZIP file parser for ClamAV could allow an unauthenticated, remote attac |
| CVE-2026-132229 | 8.1 | 2026-11-18 | A flaw was found in hypershift-addon. Due to an overly permissive role-based access control (RBAC) configuration that gr |
| CVE-2026-128664 | 8.3 | 2026-11-18 | An insecure password reset vulnerability in the Admin Password Recovery Module of PHPGurukul News Portal Project v4.1 al |
| CVE-2026-130751 | 8.1 | 2026-11-18 | OpenWrt LuCI luci-app-travelmate on master before 3.0.0-1 and on openwrt-25.12 before 2.4.9-6 grants file exec permissio |
| CVE-2026-130753 | 8.8 | 2026-11-18 | heym before 0.0.142 contains a remote code execution vulnerability in the Playwright step-mode node where _resolve_expre |
| CVE-2026-130754 | 9.8 | 2026-11-18 | All versions of LaraDashboard contain an authentication bypass in SocialAuthService::findOrCreateUser(), which links a s |
| CVE-2026-130756 | 9.8 | 2026-11-18 | pnpm exe before 10.34.8 embeds an outdated Node.js runtime that still trusts compromised eMudhra intermediate CA certifi |
| CVE-2026-130757 | 7.4 | 2026-11-18 | Fleet before 4.92.0 contains an improper authentication vulnerability that allows attackers to reuse case-mutated securi |
| CVE-2026-130758 | 7.2 | 2026-11-18 | Fleet before 4.92.0 contains an authorization bypass vulnerability in the deprecated POST /api/latest/fleet/mdm/apple/en |
| CVE-2026-130759 | 9.9 | 2026-11-18 | Fleet from 4.71.0 before 4.88.2 contains an authentication bypass vulnerability in the SAML SSO callback that looks up s |
| CVE-2026-130760 | 7.5 | 2026-11-18 | Fleet before 4.86.2 contains a denial of service vulnerability that allows unauthenticated attackers to exhaust server m |
| CVE-2026-130761 | 7.5 | 2026-11-18 | Fleet before 4.92.0 contains a denial of service vulnerability that allows enrolled hosts to trigger unbounded per-name  |
| CVE-2026-130764 | 7.6 | 2026-11-18 | Obot from 0.8.0 before 0.27.0 contains a server-side request forgery vulnerability that allows Power User accounts to re |
| CVE-2026-130766 | 8.0 | 2026-11-18 | Obot from 0.26.0 before 0.27.0 fails to validate the resource identifier in remote MCP server protected resource metadat |
| CVE-2026-130770 | 8.4 | 2026-11-18 | Incus before 7.6.0 creates the NBD servers used for virtual machine migration and disk export on abstract unix sockets,  |
| CVE-2026-130771 | 9.9 | 2026-11-18 | Incus before 7.6.0 fails to reject special files, hard links, or symlinks in backup or image metadata, allowing restrict |
| CVE-2026-130773 | 9.9 | 2026-11-18 | Incus before 7.6.0 contains an authorization bypass that allows restricted project users to create resources in the unre |
| CVE-2026-130774 | 8.8 | 2026-11-18 | Incus before 7.6.0 contains a privilege escalation vulnerability: rebuilding a never-started unprivileged container make |
| CVE-2026-130776 | 7.1 | 2026-11-18 | Incus before 7.6.0 contains an information disclosure vulnerability that allows clients with project event-view access t |
| CVE-2026-130778 | 10.0 | 2026-11-18 | Incus before 7.6.0 contains an authentication bypass vulnerability that allows remote attackers to authenticate as any t |
| CVE-2026-130779 | 9.6 | 2026-11-18 | Incus before 7.6.0 contains a path traversal vulnerability that allows users permitted to import custom volumes to store |
| CVE-2026-130780 | 9.9 | 2026-11-18 | Incus before 7.6.0 contains a path traversal vulnerability that allows malicious migration peers to write outside intend |
| CVE-2026-130782 | 7.7 | 2026-11-18 | Incus before 7.6.0 contains an improper authorization vulnerability that allows restricted and view-only clients to read |
| CVE-2026-130783 | 9.6 | 2026-11-18 | Incus before 7.6.0 exposes certificate and cluster join token secrets through the default project event stream and skips |
| CVE-2026-130784 | 9.9 | 2026-11-18 | Incus before 7.6.0 contains an authorization bypass vulnerability that allows restricted clients to create and access de |
| CVE-2026-130785 | 8.5 | 2026-11-18 | Incus from 7.3.0 before 7.6.0 contains an authentication bypass vulnerability in the /dev/incus guest API that allows a  |
| CVE-2026-130786 | 9.9 | 2026-11-18 | Incus before 7.6.0 contains a configuration injection vulnerability that allows users who can launch instances from cont |
| CVE-2026-130787 | 7.7 | 2026-11-18 | Frappe ERPNext before 16.35.0 contains a missing authorization vulnerability in financial reporting endpoints that allow |
| CVE-2026-130791 | 8.1 | 2026-11-18 | Finsys Dockhand before 1.0.55 contains a path traversal vulnerability that allows users with stacks:edit permission to m |
| CVE-2026-45142 | 7.1 | 2026-11-18 | Chamilo LMS is an open-source learning management system. Prior to 1.11.40 and 2.0.1, main/lp/lp_ajax_save_objectives.ph |
| CVE-2026-61528 | 8.2 | 2026-11-18 | Chamilo LMS is an open-source learning management system. From 2.0.0 until 2.0.3, the BigBlueButton plugin is vulnerable |
| CVE-2026-61532 | 9.0 | 2026-11-18 | Chamilo LMS is an open-source learning management system. Prior to 1.11.40 and 2.0.3, src/Chamilo/CourseBundle/Component |
| CVE-2026-61581 | 7.4 | 2026-11-18 | The Datadog Agent collects events and metrics from hosts and sends them to Datadog. Prior to datadog-apm-inject 0.66.0,  |
| CVE-2026-71481 | 7.5 | 2026-11-18 | ALTCHA PHP is a lightweight PHP library for creating and verifying ALTCHA challenges. From 2.0.0 until 2.0.3, the verify |
| CVE-2026-71499 | 10.0 | 2026-11-18 | cf-manager is an all-in-one dashboard for managing multiple Cloudflare accounts and services. Prior to 1.1.2, worker/src |
| CVE-2026-73864 | 7.5 | 2026-11-18 | install-artifact-from-github installs prebuilt native artifacts hosted by GitHub without compiling them locally. Prior t |
| CVE-2026-128669 | 7.1 | 2026-11-18 | A Session Fixation vulnerability exists in the admin login endpoint (/admin/index.php) of PHPGurukul News Portal Project |
| CVE-2026-62340 | 8.0 | 2026-11-18 | X-Road is open-source data exchange layer software. Prior to .8.2, 7.7.3, and 7.6.5, the Security Server writes each dow |
| CVE-2026-63129 | 8.8 | 2026-11-18 | mssql-mcp-core is the shared library that powers MSSQL MCP servers. Prior to core and server 0.6.0 and reader and writer |
| CVE-2026-68903 | 7.7 | 2026-11-18 | LLMKube is a Kubernetes operator for self-hosted large language model inference across heterogeneous hardware. Prior to  |
| CVE-2026-76807 | 9.3 | 2026-11-18 | Todoist MCP Server provides tools that allow AI agents to access and modify a Todoist account. Prior to 10.3.3, the opti |
| CVE-2026-111513 | 7.3 | 2026-11-18 | Dell Alienware Command Center (AWCC), versions prior to 6.14.105.0, contain an Improper Verification of Cryptographic Si |
| CVE-2026-111514 | 7.3 | 2026-11-18 | Dell Alienware Command Center (AWCC), versions prior to 6.14.105.0, contain an Incorrect Default Permissions vulnerabili |
| CVE-2026-111515 | 7.1 | 2026-11-18 | Dell Alienware Command Center (AWCC), versions prior to 6.14.105.0, contain an Improper Authorization in Handler for Cus |
| CVE-2026-111520 | 7.3 | 2026-11-18 | Dell Alienware Command Center (AWCC), versions prior to 6.14.105.0, contain a Time-of-check Time-of-use (TOCTOU) Race Co |
| CVE-2026-114585 | 7.6 | 2026-11-18 | IBM Engineering AI Hub 1.0.0 through 1.4.0 could allow a remote authenticated attacker to obtain sensitive information d |
| CVE-2026-127222 | 7.5 | 2026-11-18 | SGLang through 0.5.23, fixed in commit 7b5fb39, contains a missing authorization vulnerability in the POST /load_lora_ad |
| CVE-2026-132139 | 9.9 | 2026-11-18 | A weakness has been identified in DrayTek Vigor2960 up to 1.5.1.6. Affected is the function setSWMProfile of the file /c |
| CVE-2026-132140 | 7.5 | 2026-11-18 | A security vulnerability has been detected in DrayTek Vigor2960 up to 1.5.1.6. Affected by this vulnerability is an unkn |
| CVE-2026-55506 | 9.6 | 2026-11-18 | Wavelog is web-based amateur radio logging software. Prior to 2.5, the filename parameter accepted by POST /qsl/addQsoTo |
| CVE-2026-55508 | 9.4 | 2026-11-18 | Wavelog is web-based amateur radio logging software. Prior to 2.5, the callsign parameter accepted by POST /oqrs/search_ |
| CVE-2026-59975 | 7.5 | 2026-11-18 | SharpIppNext is a .NET Standard library for building Internet Printing Protocol clients and servers. Prior to 4.1.0, ser |
| CVE-2026-73967 | 8.7 | 2026-11-18 | AnsibleForms is a self-hosted web application that turns automation into self-service forms. Prior to 6.2.1, AnsibleForm |
| CVE-2026-73968 | 7.2 | 2026-11-18 | AnsibleForms is a self-hosted web application that turns automation into self-service forms. Prior to 6.2.1, AnsibleForm |
| CVE-2026-73969 | 9.8 | 2026-11-18 | AnsibleForms is a self-hosted web application that turns automation into self-service forms. Prior to 6.2.1, AnsibleForm |
| CVE-2026-75522 | 7.5 | 2026-11-18 | OpenID4VP is an open-source credential parsing library for SD-JWT VC and mDOC/mDL formats. Prior to 0.8.1, src/trust/Cha |
| CVE-2026-76007 | 8.1 | 2026-11-18 | IBM Engineering AI Hub 1.0.0 through 1.4.0 could allow a remote attacker to obtain sensitive information and perform una |
| CVE-2026-76088 | 7.5 | 2026-11-18 | PGPainless is a simple-to-use OpenPGP API based on Bouncy Castle. Prior to 1.7.8 and from 2.0.0 until 2.0.4, pgpainless- |
| CVE-2026-76913 | 8.8 | 2026-11-18 | NotrinosERP is an open-source web-based enterprise resource planning system written in PHP and MySQL. From 1.0.0 until 1 |
| CVE-2026-129987 | 9.9 | 2026-11-18 | Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, the database password validation used by |
| CVE-2026-132141 | 9.9 | 2026-11-18 | A vulnerability was detected in DrayTek Vigor2960 up to 1.5.1.6. Affected by this issue is the function json_load_lock o |
| CVE-2026-132142 | 9.1 | 2026-11-18 | A flaw has been found in DrayTek Vigor2960 up to 1.5.1.6. This affects the function dataflowstatus of the file /cgi-bin/ |
| CVE-2026-132143 | 9.9 | 2026-11-18 | A vulnerability has been found in DrayTek Vigor2960 up to 1.5.1.6. This vulnerability affects the function doWebBackup o |
| CVE-2026-59961 | 8.2 | 2026-11-18 | mini-snmpd is a minimal SNMP agent implementation. Prior to 1.7, the ASN.1 BER parser in protocol.c does not verify that |
| CVE-2026-62964 | 7.8 | 2026-11-18 | Gortex is a high-performance code-intelligence engine for AI agents and integrated development environments. Prior to 0. |
| CVE-2026-73971 | 8.0 | 2026-11-18 | Music Assistant is an open-source media library manager that integrates streaming services with connected speakers. Prio |
| CVE-2026-75612 | 7.5 | 2026-11-18 | yt-mcp is a YouTrack MCP server for Claude Code. Prior to 1.18.1, add_attachment in src/yt_mcp/tools/attachments.py acce |
| CVE-2026-76101 | 7.1 | 2026-11-18 | keystore-go is a Go implementation of the Java KeyStore encoder and decoder. In 2.1.0 and earlier, keystore.Decode in de |
| CVE-2026-76818 | 7.5 | 2026-11-18 | Axon is an agent-agnostic context engine that gives AI coding agents continuous memory across sessions, tools, and machi |
| CVE-2026-129316 | 9.9 | 2026-11-18 | Dokploy is a free, self-hostable Platform as a Service (PaaS). From 0.29.13 until 0.31.0, the Docker terminal, container |
| CVE-2026-129986 | 9.9 | 2026-11-18 | Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, mount.deleteFileMount passes a path cont |
| CVE-2026-129989 | 9.9 | 2026-11-18 | Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, the Nixpacks publishDirectory build sett |
| CVE-2026-129990 | 8.3 | 2026-11-18 | Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, every network.* procedure is only authen |
| CVE-2026-129991 | 9.9 | 2026-11-18 | Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, the backup prefix field is only checked  |
| CVE-2026-71535 | 7.1 | 2026-11-18 | Mareforma is a local verification layer for AI-assisted research. From 0.3.0 until 0.3.7, the _maybe_update_replicated_u |
| CVE-2026-132748 | 7.2 | 2026-11-19 | Vtiger CRM through 8.4.0 contains a PHP code injection vulnerability that allows authenticated administrators to inject  |
| CVE-2026-132751 | 7.8 | 2026-11-19 | yt through 4.4.4 contains a code injection vulnerability that allows attackers to execute Python code by supplying a cra |
| CVE-2026-132756 | 7.8 | 2026-11-19 | Geany through 2.1.0 contains an OS command injection vulnerability that allows attackers to run shell commands by embedd |
| CVE-2026-132773 | 7.1 | 2026-11-19 | Attendize through 2.8.0 contains an authorization bypass vulnerability in EventOrdersController::postCancelOrder() that  |
| CVE-2026-132286 | 7.3 | 2026-11-19 | A security vulnerability has been detected in yangzongzhuan RuoYi up to 4.8.3. The impacted element is an unknown functi |
| CVE-2026-132609 | 7.3 | 2026-11-19 | A vulnerability was identified in SourceCodester Online Food Ordering System 1.0. The affected element is an unknown fun |
| CVE-2026-132610 | 7.3 | 2026-11-19 | A security flaw has been discovered in SourceCodester Simple Form Builder Web App 1.0. The impacted element is the funct |
| CVE-2026-132611 | 7.3 | 2026-11-19 | A security vulnerability has been detected in SourceCodester Simple Form Builder Web App 1.0. This impacts the function  |
| CVE-2026-132622 | 9.1 | 2026-11-19 | A vulnerability was found in GearUP Hyperev up to 20261020. This impacts the function get_wlan_sitesurvey of the file ld |
| CVE-2026-132625 | 7.3 | 2026-11-19 | A vulnerability was determined in SourceCodester Student Project Allocation and Management System 1.0. Affected is an un |
| CVE-2026-132626 | 7.3 | 2026-11-19 | A vulnerability was identified in SourceCodester Modern Ticket Reservation System 1.0. Affected by this vulnerability is |
| CVE-2026-132627 | 7.3 | 2026-11-19 | A security flaw has been discovered in SourceCodester E-Commerce Shopping Cart Web Application 1.0. Affected by this iss |
| CVE-2026-132802 | 9.9 | 2026-11-19 | A malicious actor with access to the network and low privileges could exploit an Improper Link Resolution Before File Ac |
| CVE-2026-132803 | 9.9 | 2026-11-19 | A malicious actor with access to the network and low privileges could exploit a series of authenticated SQL Injection vu |
| CVE-2026-132804 | 9.9 | 2026-11-19 | A malicious actor with access to the network and low privileges could exploit a Server-Side Request Forgery (SSRF) vulne |
| CVE-2026-132805 | 8.3 | 2026-11-19 | A malicious actor with access to the network could exploit a Server-Side Request Forgery (SSRF) vulnerability found in U |
| CVE-2026-132806 | 8.8 | 2026-11-19 | A malicious actor with access to the network and low privileges could exploit an authenticated SQL Injection vulnerabili |
| CVE-2026-132807 | 9.0 | 2026-11-19 | A malicious actor with access to the network and under certain conditions could exploit an Improper Certificate Validati |
| CVE-2026-132808 | 9.9 | 2026-11-19 | A malicious actor with access to the network and low privileges could exploit an Incorrect Authorization vulnerability f |
| CVE-2026-84998 | 7.2 | 2026-11-19 | The NextScripts: Social Networks Auto-Poster plugin for WordPress is vulnerable to Stored Cross-Site Scripting via 'comm |
| CVE-2026-109555 | 8.0 | 2026-11-19 | The WP STAGING and WP STAGING Pro plugins for WordPress are vulnerable to PHP Object Injection in all versions up to, an |
| CVE-2026-132825 | 7.4 | 2026-11-19 | Ruby before 3.3.14, 3.4.13, and 4.0.10 has a heap-based buffer overflow during case conversion. One byte can be written  |
| CVE-2026-128999 | 7.1 | 2026-11-19 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Saphali Saphali Wo |
| CVE-2026-129001 | 7.1 | 2026-11-19 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Gabe Livan Asset C |
| CVE-2026-129013 | 7.5 | 2026-11-19 | Missing Authorization vulnerability in Deepen Bajracharya Video Conferencing with Zoom video-conferencing-with-zoom-api  |
| CVE-2026-129030 | 7.5 | 2026-11-19 | Exposure of Sensitive System Information to an Unauthorized Control Sphere vulnerability in Mamunur Rashid ShopBuilder – |
| CVE-2026-129048 | 9.9 | 2026-11-19 | Improper Control of Generation of Code ('Code Injection') vulnerability in Jacob N. Breetvelt WP Photo Album Plus wp-pho |
| CVE-2026-99320 | 7.0 | 2026-11-19 | In the Linux kernel, the following vulnerability has been resolved:

ipv6: raw: fix use-after-free in rawv6_send_hdrinc( |
| CVE-2026-126631 | 7.1 | 2026-11-19 | A flaw was found in OpenSCAP. This vulnerability allows for information disclosure when performing offline scans of untr |
| CVE-2026-14491 | 7.5 | 2026-11-19 | The WP Duplicate – WordPress Migration Plugin plugin for WordPress is vulnerable to Directory Traversal in all versions  |
| CVE-2026-14492 | 9.8 | 2026-11-19 | The WP Duplicate – WordPress Migration Plugin plugin for WordPress is vulnerable to Remote Code Execution in all version |
| CVE-2026-85776 | 7.5 | 2026-11-19 | The WP Duplicate – WordPress Migration Plugin plugin for WordPress is vulnerable to Missing Authorization in versions up |
| CVE-2026-132891 | 9.8 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 remote code execution was possible via external pull requests |
| CVE-2026-132892 | 8.1 | 2026-11-19 | In JetBrains TeamCity before 2026.2 privilege escalation was possible via the authorization flow |
| CVE-2026-132893 | 7.7 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 an SSRF via pipeline repository branch listing was possible |
| CVE-2026-132894 | 7.7 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 an SSRF in AWS connection settings could expose server credenti |
| CVE-2026-132895 | 7.5 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 remote code execution was possible via Subversion VCS root sett |
| CVE-2026-132896 | 7.2 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4 remote code execution was possible via Kubernetes Executor settings |
| CVE-2026-132897 | 7.7 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 improper authorization allowed access to credentials of other p |
| CVE-2026-132898 | 7.2 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 arbitrary file write on the server was possible via Kotlin DSL  |
| CVE-2026-132899 | 7.6 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 stored XSS in the NPM Registry build feature was possible |
| CVE-2026-132900 | 7.5 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 secure parameter values were disclosed to project viewers in pi |
| CVE-2026-132901 | 7.7 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 improper authorization allowed publishing packages to NuGet fee |
| CVE-2026-132902 | 7.7 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 access keys of parent project AWS connections could be disclose |
| CVE-2026-132903 | 8.1 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 missing authorization allowed any authenticated user to start a |
| CVE-2026-132904 | 8.1 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 missing authorization allowed project viewers to remove VCS roo |
| CVE-2026-132905 | 7.6 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 stored XSS in the AWS Credentials build feature was possible |
| CVE-2026-132906 | 8.8 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 remote code execution was possible via native code loading in t |
| CVE-2026-132907 | 8.1 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 project viewers could redirect GitHub App connection credential |
| CVE-2026-132908 | 7.5 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 remote code execution was possible via Mercurial VCS root setti |
| CVE-2026-132909 | 8.8 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 remote code execution was possible via Mercurial repository con |
| CVE-2026-132910 | 7.5 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 unauthenticated DoS via the agent protocol was possible |
| CVE-2026-132911 | 7.5 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 remote code execution was possible via build access codes discl |
| CVE-2026-132912 | 7.2 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 remote code execution was possible via class injection in the K |
| CVE-2026-132913 | 8.4 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 stored XSS on the P4 Code Review build tab was possible |
| CVE-2026-132914 | 8.0 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 stored XSS on the Issue Log tab was possible |
| CVE-2026-132915 | 7.1 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 an LDAP injection allowed bypassing login restrictions |
| CVE-2026-132916 | 7.1 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 arbitrary file deletion on the server was possible via the Kotl |
| CVE-2026-132917 | 8.8 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 remote code execution was possible via a file write bypass in t |
| CVE-2026-132918 | 7.6 | 2026-11-19 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 stored XSS on build and queue pages was possible |
| CVE-2026-115677 | 7.5 | 2026-11-19 | Buffer Copy without Checking Size of Input ('Classic Buffer Overflow') vulnerability in AirTies Kablosuz İletişim Sanayi |
| CVE-2026-123058 | 9.0 | 2026-11-19 | The web installer of JTL-Shop executes its
state-changing installation tasks without checking whether the shop is alread |
| CVE-2026-123968 | 7.2 | 2026-11-19 | The Slimbox plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'comment (anchor title within comm |
| CVE-2026-123972 | 7.2 | 2026-11-19 | The WP-Slimbox2 Plugin plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'comment' parameter in  |
| CVE-2026-125060 | 8.2 | 2026-11-19 | The checkout of JTL-Shop stores the delivery address
ID submitted by the customer in the session and adopts it into the  |
| CVE-2026-125061 | 8.7 | 2026-11-19 | The administration page "Offene
Bestellungen" (open orders) of the JTL PayPal Checkout plugin for JTL-Shop outputs the
c |
| CVE-2026-132128 | 7.4 | 2026-11-19 | @fastify/middie is the middleware engine that adds Express and Connect style middleware support to Fastify. In versions  |
| CVE-2026-132131 | 7.4 | 2026-11-19 | @fastify/middie is the middleware engine that adds Express and Connect style middleware support to Fastify. In versions  |
| CVE-2026-133014 | 7.2 | 2026-11-19 | In JetBrains TeamCity before 2026.2.1, 2026.1.5 remote code execution was possible via public reflection in the Kotlin D |
| CVE-2026-133015 | 8.8 | 2026-11-19 | In JetBrains TeamCity before 2026.2.1, 2026.1.5 remote code execution was possible via boot classpath libraries in the K |
| CVE-2026-133016 | 8.8 | 2026-11-19 | In JetBrains TeamCity before 2026.2.1, 2026.1.5 remote code execution was possible via script definitions in the Kotlin  |
| CVE-2026-133017 | 8.0 | 2026-11-19 | In JetBrains TeamCity before 2026.2.1, 2026.1.5 remote code execution was possible via Git VCS root settings |
| CVE-2026-133018 | 8.8 | 2026-11-19 | In JetBrains TeamCity before 2026.2.1, 2026.1.5 remote code execution was possible via a UI patches callback in the Kotl |
| CVE-2026-133019 | 8.8 | 2026-11-19 | In JetBrains TeamCity before 2026.2.1, 2026.1.5 remote code execution was possible via a context parameters callback in  |
| CVE-2026-133020 | 7.4 | 2026-11-19 | In JetBrains TeamCity before 2026.1.5 untrusted build approval for GitHub fork pull requests could be bypassed |
| CVE-2026-133021 | 7.5 | 2026-11-19 | In JetBrains TeamCity before 2026.2.1, 2026.1.5 remote code execution was possible via Mercurial subrepository paths |
| CVE-2026-133022 | 7.5 | 2026-11-19 | In JetBrains TeamCity before 2026.2.1 remote code execution was possible via the Notification Rules form |
| CVE-2026-133023 | 7.2 | 2026-11-19 | In JetBrains TeamCity before 2026.2.1, 2026.1.5 remote code execution was possible via Kotlin DSL compiler arguments |
| CVE-2026-133024 | 7.5 | 2026-11-19 | In JetBrains TeamCity before 2026.2.1, 2026.1.5 remote code execution was possible via personal builds with versioned se |
| CVE-2026-133025 | 7.7 | 2026-11-19 | In JetBrains TeamCity before 2026.2.1 missing authorization allowed project viewers to download project settings |
| CVE-2026-133026 | 7.2 | 2026-11-19 | In JetBrains TeamCity before 2026.2.1, 2026.1.5 code injection in generated Kotlin DSL was possible via matrix build par |
| CVE-2026-133027 | 8.8 | 2026-11-19 | In JetBrains TeamCity before 2026.2.1, 2026.1.5 privilege escalation was possible via username handling in token authent |
| CVE-2026-22311 | 7.5 | 2026-11-19 | The failed-login limiter of the JTL-Wawi
synchronisation interface of JTL-Shop derives the client identity from the
clie |
| CVE-2026-111509 | 9.1 | 2026-11-19 | Dell PowerStore SDNAS contains a cryptographically weak PRNG vulnerability that could allow a network attacker to decryp |
| CVE-2026-116439 | 9.8 | 2026-11-19 | Dell PowerStore SDNAS contains a path traversal vulnerability that could allow an unauthenticated attacker to read, modi |
| CVE-2026-116440 | 9.8 | 2026-11-19 | Dell PowerStore SDNAS contains a buffer overflow vulnerability that could allow an unauthenticated remote attacker to ca |
| CVE-2026-129034 | 7.1 | 2026-11-19 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WP Chill Strong Te |
| CVE-2026-133076 | 7.5 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via local repository URLs in Subversi |
| CVE-2026-133077 | 7.2 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 privilege escalation to system administrator was possible via Project Im |
| CVE-2026-133078 | 7.2 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via security context spoofing in the  |
| CVE-2026-133079 | 7.2 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via Maven dependencies of Kotlin DSL  |
| CVE-2026-133080 | 8.8 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via Maven repository settings |
| CVE-2026-133081 | 7.5 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via Git VCS root URLs |
| CVE-2026-133082 | 7.5 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 a DoS attack was possible via unauthenticated multipart requests |
| CVE-2026-133083 | 8.0 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 stored XSS in Server Health reports was possible |
| CVE-2026-133084 | 7.7 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 vCS root credentials could be exposed via change viewer links |
| CVE-2026-133085 | 7.6 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 an XXE was possible in the TFS helper process |
| CVE-2026-133086 | 8.8 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via a URL stream handler in the Kotli |
| CVE-2026-133087 | 8.8 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via a time zone callback in the Kotli |
| CVE-2026-133088 | 7.2 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via FreeMarker notification templates |
| CVE-2026-133089 | 8.1 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 the TFS helper process exposed an unauthenticated command server |
| CVE-2026-133090 | 7.2 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 improper authorization allowed overwriting versioned settings of other p |
| CVE-2026-133091 | 8.0 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 stored XSS on the Users page was possible |
| CVE-2026-133092 | 8.8 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via Git submodule URLs |
| CVE-2026-133093 | 7.2 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 code injection in parent project Kotlin DSL was possible via subproject  |
| CVE-2026-133094 | 7.7 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2 missing authorization allowed project developers to read arbitrary HashiCorp Vault |
| CVE-2026-133095 | 8.1 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 a CSRF attack was possible on the Hub integration settings |
| CVE-2026-133096 | 7.1 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 improper authorization allowed queuing builds with personal changes of o |
| CVE-2026-133097 | 7.4 | 2026-11-19 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 agent Push authorization keys were predictable |
| CVE-2026-133117 | 8.2 | 2026-11-19 | WebToffee Product Feed before 2.4.4 for WordPress contains a use of hard-coded cryptographic key vulnerability that allo |
| CVE-2026-111506 | 8.8 | 2026-11-19 | Dell PowerStore contains a Missing Authentication vulnerability that a network-adjacent attacker could exploit to bypass |
| CVE-2026-126826 | 7.8 | 2026-11-19 | A maliciously crafted SBSAR file, when imported or loaded through the Substance in 3ds Max plugin in Autodesk 3ds Max, c |
| CVE-2026-132858 | 7.8 | 2026-11-19 | A flaw was found in gdm. The CreateRemoteDisplay D-Bus method fails to perform proper authorization checks when initiati |
| CVE-2026-123890 | 9.8 | 2026-11-19 | VMware vCenter contains an authentication bypass vulnerability in the VMware Directory Service.
Affected versions: 9.1.x |
| CVE-2026-123891 | 8.1 | 2026-11-19 | SDDC Manager contains an SQL-injection vulnerability due to improper sanitization of user-supplied input.
Affected versi |
| CVE-2026-123892 | 7.2 | 2026-11-19 | SDDC Manager contains an authenticated command-injection vulnerability due to improper sanitization of user-supplied inp |
| CVE-2026-133161 | 7.5 | 2026-11-19 | ### Summary ui

With `strip_ansi=True`, Pydantic AI Harness's `ToolOutputLimits` capability removes ANSI escape sequence |
| CVE-2026-133168 | 7.8 | 2026-11-19 | OFFIS DCMTK 3.7.1 contains a heap buffer overflow vulnerability in togglePlanarConfiguration8 and togglePlanarConfigurat |
| CVE-2026-133172 | 8.8 | 2026-11-19 | Cozy Cloud cozy-stack 1.6.62 before 1.6.69 contains an authorization bypass vulnerability in the shared-drive move handl |
| CVE-2026-133185 | 7.4 | 2026-11-19 | Goproxy before 1.9.4 contains a weak key generation vulnerability in NewCounterEncryptorRandFromKey that derives RSA and |
| CVE-2026-133195 | 7.5 | 2026-11-19 | In JetBrains Junie CLI before 26.6.29 files outside the project directory could be modified by agent file tools |
| CVE-2026-133198 | 7.8 | 2026-11-19 | In JetBrains Junie before 252.819.35, 253.819.35 code execution was possible via terminal environment settings in projec |
| CVE-2026-131807 | 7.5 | 2026-11-19 | United Chargers Grizzl-E Smart 40A OCPP GetConfiguration Stack-based Buffer Overflow Remote Code Execution Vulnerability |
| CVE-2026-131809 | 7.6 | 2026-11-19 | United Chargers Grizzl-E Smart 40A OCPP Backend Configuration Authentication Bypass Vulnerability. This vulnerability al |
| CVE-2026-131810 | 7.5 | 2026-11-19 | United Chargers Grizzl-E Smart 40A Download of Code Without Integrity Check Remote Code Execution Vulnerability. This vu |
| CVE-2026-131811 | 7.6 | 2026-11-19 | United Chargers Grizzl-E Smart 40A OCPP Backend Configuration Hard-Coded Credentials Authentication Bypass Vulnerability |
| CVE-2026-131812 | 7.5 | 2026-11-19 | United Chargers Grizzl-E Smart 40A FTP URL Path Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability. |
| CVE-2026-131813 | 7.5 | 2026-11-19 | United Chargers Grizzl-E Smart 40A OCPP UpdateFirmware Out-Of-Bounds Write Remote Code Execution Vulnerability. This vul |
| CVE-2026-133062 | 7.5 | 2026-11-19 | A flaw was found in Moodle's external database enrolment plugin. Insufficient sanitization of data passed to queries aga |
| CVE-2026-133234 | 7.5 | 2026-11-19 | Stoatchat before 0.16.5 contains an unbounded JXL image decoding vulnerability in revolt_files decode_image that allows  |
| CVE-2026-133235 | 7.7 | 2026-11-19 | Tandoor Recipes before 2.7.4 contains a server-side request forgery vulnerability that allows space admins to reach inte |
| CVE-2026-133243 | 8.2 | 2026-11-19 | node-soap before 1.14.1 contains a prototype pollution vulnerability in WSDL.xmlToObject that allows unauthenticated att |
| CVE-2026-133245 | 7.5 | 2026-11-19 | parse5 7.0.0 before 8.1.1 contains an uncaught exception vulnerability in Preprocessor#_processSurrogate that allows rem |
| CVE-2026-133246 | 7.2 | 2026-11-19 | modified eCommerce Shopsoftware through 3.3.0 contains a local file inclusion vulnerability that allows administrators t |
| CVE-2026-133253 | 7.4 | 2026-11-19 | In JetBrains IntelliJ IDEA before 2026.3 untrusted projects could read files of other open projects via the built-in web |
| CVE-2026-133254 | 8.3 | 2026-11-19 | In JetBrains IntelliJ IDEA before 2026.3, 2026.2.4 code execution was possible in untrusted projects via the Code Proven |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2024-10441 | Synology / DiskStation Manager (DSM) | 2026-11-18 | 2026-11-21 | Unknown |
| CVE-2026-40217 | BerriAI / LiteLLM | 2026-11-18 | 2026-12-02 | Unknown |
| CVE-2026-90817 | Vanderbilt University / Research Electronic Data Capture (REDCap) | 2026-11-18 | 2026-11-21 | Unknown |
| CVE-2026-90436 | Apache / Axis | 2026-11-18 | 2026-11-21 | Unknown |
| CVE-2026-115731 | Perforce / Puppet Enterprise | 2026-11-17 | 2026-12-01 | Unknown |
| CVE-2026-114713 | UnrealIRCd / UnrealIRCd | 2026-11-13 | 2026-11-16 | Unknown |
| CVE-2026-123039 | Check Point / Multiple Products | 2026-11-13 | 2026-11-16 | Unknown |

---

*Total entries in CISA KEV catalog: 1786*