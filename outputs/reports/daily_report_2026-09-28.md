# Vulnerability Intelligence Report

**Date:** 2026-09-28  
**Generated:** 2026-09-28T16:28:09Z  

---

## Executive Summary

Our environment faces critical exposure from 91 high-severity vulnerabilities, with two actively exploited Citrix NetScaler flaws (CVE-2026-88771 and CVE-2026-88772) listed on CISA's Known Exploited Vulnerabilities catalog and requiring remediation by September 30, 2026. A perfect CVSS 10.0 HTTP smuggling vulnerability (CVE-2026-88773) and a second CVSS 9.8 memory overflow (CVE-2026-88775) compound the Citrix risk. Additional exposures in pnpm, Fleet, and Python HTTP libraries expand the attack surface. Threat actors are actively weaponizing these vulnerabilities in the wild, making immediate action essential to protect network infrastructure and application delivery systems.

---

## Risk Narrative

Adversaries are actively exploiting Citrix NetScaler vulnerabilities confirmed in CISA's KEV catalog, targeting network access infrastructure that if compromised could grant broad lateral movement and data exfiltration capabilities. The CVSS 10.0 HTTP smuggling flaw poses existential risk to application delivery integrity. Simultaneously, supply-chain vulnerabilities in widely used package managers (pnpm, pacquet) and SSRF flaws in HTTP utility libraries create pathways for credential theft and internal network pivoting. The combination of perimeter-level and developer-toolchain exposures represents a layered threat landscape where a single successful exploit could cascade into enterprise-wide compromise, regulatory liability, and operational disruption.

---

## Prioritized Action Items

1. Patch Citrix NetScaler ADC and Gateway to version 14.1-73.37 or later immediately to address CISA KEV-mandated CVE-2026-88771 and CVE-2026-88772 before the September 30, 2026 deadline.
2. Apply mitigations or compensating controls for CVE-2026-88773 (CVSS 10.0 HTTP smuggling) and CVE-2026-88775 (CVSS 9.8 memory overflow) in Citrix NetScaler on an emergency basis.
3. Upgrade pnpm to version 11.11.0 or 10.34.5 and pacquet to 12.0.0-alpha.5 or later to eliminate supply-chain credential exposure risks.
4. Remediate SSRF vulnerabilities in python-utcp and utcp-http by upgrading to version 1.1.4 or later to prevent credential redirection attacks.
5. Audit and regenerate Fleet macOS app install scripts created before 2026-08-19 to remove malicious Homebrew cask metadata injection risk.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-88771 | 9.8 | 2026-09-27 | Improper input validation vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: b |
| CVE-2026-88772 | 8.1 | 2026-09-27 | Vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 1 |
| CVE-2026-88773 | 10.0 | 2026-09-27 | Inconsistent interpretation of HTTP requests ('HTTP Request/Response smuggling') vulnerability in Citrix NetScaler ADC a |
| CVE-2026-88774 | 7.2 | 2026-09-27 | Vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 1 |
| CVE-2026-88775 | 9.8 | 2026-09-27 | Memory overflow vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1 |
| CVE-2026-101043 | 7.4 | 2026-09-27 | pnpm versions 11.0.0 before 11.11.0 and 10.7.0 before 10.34.5 expand ${VAR} environment-variable placeholders in the htt |
| CVE-2026-101044 | 7.1 | 2026-09-27 | pacquet, the Rust package-manager component shipped in the pnpm npm package versions >=12.0.0-alpha.0 and <12.0.0-alpha. |
| CVE-2026-101045 | 8.0 | 2026-09-27 | Fleet-maintained app install and uninstall scripts for macOS are generated from Homebrew cask metadata. In manifests gen |
| CVE-2026-101059 | 7.1 | 2026-09-27 | utcp-http before 1.1.4 fails to validate the OAuth2 tokenUrl field from remote OpenAPI specifications, allowing attacker |
| CVE-2026-101060 | 8.2 | 2026-09-27 | python-utcp versions before 1.1.4 contain a server-side request forgery vulnerability in HttpCommunicationProtocol.call_ |
| CVE-2026-100874 | 7.3 | 2026-09-27 | A flaw has been found in mathurvishal CloudClassroom-PHP-Project up to 5dadec098bfbbf3300d60c3494db3fb95b66e7be. This af |
| CVE-2026-100875 | 7.3 | 2026-09-27 | A vulnerability has been found in mathurvishal CloudClassroom-PHP-Project up to 5dadec098bfbbf3300d60c3494db3fb95b66e7be |
| CVE-2026-101062 | 8.8 | 2026-09-27 | Obot before v0.23.0 (affected versions <= v0.22.1) running with OBOT_SERVER_ENABLE_AUTHENTICATION=true exposes OAuth dyn |
| CVE-2026-101064 | 7.6 | 2026-09-27 | Obot before v0.23.0 contains a server-side request forgery vulnerability in remote MCP server registration that allows p |
| CVE-2026-101065 | 9.8 | 2026-09-27 | Obot is an open-source AI agent/MCP platform. In all versions up to and including commit d7e6970, the Docker quickstart  |
| CVE-2026-101084 | 9.6 | 2026-09-27 | obot versions before v0.21.1 fail to enforce Access Control Rules on the /mcp-connect endpoint, allowing any authenticat |
| CVE-2026-101090 | 9.8 | 2026-09-27 | Nezha 2.2.3 contains a Host header injection regression in the OAuth2 redirect endpoint. When the new optional dashboard |
| CVE-2026-96280 | 7.5 | 2026-09-27 | The OCI delta stream parser read sizes as guint64 but passed them to GLib I/O and allocation functions expecting gsize ( |
| CVE-2026-100885 | 7.3 | 2026-09-27 | A vulnerability was found in Krayin laravel-crm up to 2.2.4. This affects an unknown function of the file packages/Webku |
| CVE-2026-100886 | 10.0 | 2026-09-27 | A vulnerability was identified in Seetong T8108, T8108P, T8116 and T8232 4.6.1.4-build202604241011. The affected element |
| CVE-2026-100888 | 7.3 | 2026-09-28 | A weakness has been identified in Trusted Domain Project OpenDKIM up to 2.11.0. This affects the function dkim_canon_sel |
| CVE-2026-100889 | 7.3 | 2026-09-28 | A vulnerability was detected in Trusted Domain Project OpenDKIM up to 2.11.0. Affected is the function dkim_qp_decode of |
| CVE-2026-100891 | 7.3 | 2026-09-28 | A vulnerability has been found in Trusted Domain Project OpenDMARC up to 1.4.2. Affected by this issue is the function o |
| CVE-2026-100893 | 7.3 | 2026-09-28 | A vulnerability was determined in Privoce VoceChat Server up to 0.5.36. This vulnerability affects the function open_gra |
| CVE-2026-100896 | 9.9 | 2026-09-28 | A weakness has been identified in TOTOLINK N150RT 3.4.0-B20201030. The affected element is the function system of the fi |
| CVE-2026-100901 | 7.3 | 2026-09-28 | A vulnerability was found in athlon1600 youtube-downloader up to 4.0.1. Affected by this vulnerability is the function s |
| CVE-2026-100908 | 7.5 | 2026-09-28 | A vulnerability has been found in Eyeplus 57.0.0.0308. This affects an unknown function of the component p2pcam HTTP Par |
| CVE-2026-100909 | 7.3 | 2026-09-28 | A vulnerability was found in OctoberCMS up to 4.1.19/4.2.25/4.3.4. The impacted element is the function getSourcePathFor |
| CVE-2026-101000 | 10.0 | 2026-09-28 | A vulnerability was determined in Netcore NBR100V2 1.3.240614.030928. This affects the function uci.apply of the file /u |
| CVE-2026-101001 | 10.0 | 2026-09-28 | A vulnerability was identified in Netcore NBR200V2 1.3.241127.071246. This impacts the function eval of the file /www/cg |
| CVE-2026-101002 | 9.9 | 2026-09-28 | A security flaw has been discovered in Netcore NBR200V2 1.3.241127.071246. Affected is the function system of the file / |
| CVE-2026-101005 | 7.3 | 2026-09-28 | A vulnerability was detected in October CMS up to 4.3.4. This affects the function validateExternalImageHost of the file |
| CVE-2026-101007 | 8.4 | 2026-09-28 | A vulnerability has been found in aaPanel BaoTa up to 11.8.0. This issue affects the function InputSql of the file class |
| CVE-2026-101008 | 9.1 | 2026-09-28 | A vulnerability was found in aaPanel BaoTa up to 11.8.0. Impacted is the function merge_split_file of the file /www/serv |
| CVE-2026-101009 | 8.4 | 2026-09-28 | A vulnerability was determined in aaPanel BaoTa up to 11.8.0. The affected element is the function panelTask.bt_task._un |
| CVE-2026-101012 | 7.3 | 2026-09-28 | A weakness has been identified in mathurvishal CloudClassroom-PHP-Project up to 5dadec098bfbbf3300d60c3494db3fb95b66e7be |
| CVE-2026-101013 | 7.3 | 2026-09-28 | A security vulnerability has been detected in mathurvishal CloudClassroom-PHP-Project up to 5dadec098bfbbf3300d60c3494db |
| CVE-2026-82348 | 7.7 | 2026-09-28 | Authorization Bypass Through User-Controlled Key in Apache Roller 6.1.5 allows an authenticated user with authoring righ |
| CVE-2026-82375 | 7.4 | 2026-09-28 | Server-Side Request Forgery (SSRF) in Apache Roller 6.1.5 allows an authenticated user with entry-editing rights on a we |
| CVE-2026-82376 | 7.7 | 2026-09-28 | Improper Restriction of XML External Entity Reference in Apache Roller 6.1.5 allows a user with entry-editing rights on  |
| CVE-2026-82377 | 9.9 | 2026-09-28 | Missing Authorization in Apache Roller 6.1.5 allows an authenticated user to read, modify, or delete weblog content belo |
| CVE-2026-82378 | 9.0 | 2026-09-28 | Incorrect Authorization in the OAuth 1.0a authorization endpoint of Apache Roller 6.1.5 allows an unauthenticated remote |
| CVE-2026-82379 | 7.7 | 2026-09-28 | Authentication Bypass by Capture-replay in Apache Roller 6.1.5 allows an attacker who captures a valid WSSE digest authe |
| CVE-2026-82380 | 8.1 | 2026-09-28 | Cross-Site Request Forgery (CSRF) in Apache Roller 6.1.5 allows a remote attacker to cause a logged-in user to perform s |
| CVE-2026-82383 | 8.2 | 2026-09-28 | Missing Authentication for Critical Function in Apache Roller 6.1.5 allows an unauthenticated remote attacker to persist |
| CVE-2026-82384 | 9.8 | 2026-09-28 | Deserialization of Untrusted Data in Apache Roller 6.1.5 allows an unauthenticated remote attacker to cause deserializat |
| CVE-2026-82386 | 7.7 | 2026-09-28 | Improper Restriction of XML External Entity Reference in Apache Roller 6.1.5 allows a weblog administrator to read files |
| CVE-2026-101014 | 7.3 | 2026-09-28 | A vulnerability was detected in Trusted Domain Project OpenDMARC up to 1.4.2. Affected by this vulnerability is the func |
| CVE-2026-101015 | 7.3 | 2026-09-28 | A flaw has been found in Trusted Domain Project OpenDMARC up to 1.4.2. Affected by this issue is some unknown functional |
| CVE-2026-85134 | 8.8 | 2026-09-28 | Unrestricted upload of file with dangerous type vulnerability in Bimser Solution Software Trade Inc. EBA Plus Document a |
| CVE-2026-86530 | 7.2 | 2026-09-28 | BUFFALO Wi-Fi products handle some web form input improperly to assemble command line strings internally. An administrat |
| CVE-2026-94286 | 7.1 | 2026-09-28 | An out-of-bounds read in libXtst's RECORD reply parser in libXtst before 1.2.6 could be used by malicious X servers to c |
| CVE-2026-95104 | 7.5 | 2026-09-28 | Stack-based buffer overflow vulnerability exists in BUFFALO Wi-Fi products. A non-authenticated crafted HTTP request may |
| CVE-2026-101037 | 9.9 | 2026-09-28 | A vulnerability was found in FAST FAC1200R 5.0_20201119_1.0.2. Affected is the function parse_advertisement_frame of the |
| CVE-2026-101038 | 9.9 | 2026-09-28 | A vulnerability was determined in FAST FAC1200R 5.0_20201119_1.0.2. Affected by this vulnerability is the function MmtAt |
| CVE-2026-101039 | 10.0 | 2026-09-28 | A vulnerability was identified in FAST FAC1900R 20190827_2.0.2. Affected by this issue is the function copy_msg_element  |
| CVE-2026-12267 | 7.2 | 2026-09-28 | ManageEngine DDI Central versions below 6201 are vulnerable to Command injection in Windows DNS Query Resolution Policy  |
| CVE-2026-12268 | 8.8 | 2026-09-28 | ManageEngine DDI Central versions below 6201 are vulnerable to PowerShell command injection in Windows DNS SPF/TXT recor |
| CVE-2026-12269 | 8.8 | 2026-09-28 | Zohocorp ManageEngine DDI Central 6.2.0 build below 6201 had a Keepalived configuration injection vulnerability in the H |
| CVE-2026-101052 | 7.3 | 2026-09-28 | A security vulnerability has been detected in refly-ai refly up to 1.1.0. This issue affects some unknown processing of  |
| CVE-2026-101053 | 7.3 | 2026-09-28 | A vulnerability was determined in Thinkware U3000 up to 1.02.04. This impacts the function PUT_FILE of the file /tmp/wpa |
| CVE-2026-12264 | 8.8 | 2026-09-28 | Zohocorp ManageEngine DDI Central versions before 6201 are vulnerable to Arbitrary file write via HA Failover Config syn |
| CVE-2026-78424 | 8.8 | 2026-09-28 | Improper parameter handling in NeuVector allows any authenticated user who holds the namespaced Runtime Policies (write) |
| CVE-2026-101066 | 7.3 | 2026-09-28 | A vulnerability was determined in dbgate up to 7.3.1. The impacted element is the function createLink of the file packag |
| CVE-2026-101067 | 7.3 | 2026-09-28 | A vulnerability was identified in dbgate up to 6.8.1/7.0.2/7.1.8/7.2.5/7.3.1. This affects the function saveUploadedFile |
| CVE-2026-101292 | 8.2 | 2026-09-28 | Apache ActiveMQ Artemis before 2.34.0 contains an unsafe reflection vulnerability in FederationStreamConnectMessage.getF |
| CVE-2026-12265 | 8.8 | 2026-09-28 | Zohocorp ManageEngine DDI Central versions before 6201 are vulnerable to Insufficient access control in HA failover endp |
| CVE-2026-82323 | 8.1 | 2026-09-28 | Authorization bypass through User-Controlled key vulnerability in Enocta Educational Technologies Inc. Enocta Platform a |
| CVE-2026-86330 | 7.2 | 2026-09-28 | An OS command injection flaw was found in the set_hostname_internal function of NooBaa's cluster_internal_api. This comp |
| CVE-2026-101072 | 10.0 | 2026-09-28 | A vulnerability was identified in Netcore NR289-GE 1.4.5102. This issue affects the function system of the file /ap_ip.c |
| CVE-2026-85185 | 9.6 | 2026-09-28 | Path traversal in the btrfs storage driver in Canonical LXD versions 4.0.2 and later (fixed in 4.0.14, 5.0.10, 5.21.8 an |
| CVE-2026-85526 | 9.9 | 2026-09-28 | Path traversal in the Btrfs storage driver (unpackVolume) in Canonical LXD on Linux allows an authenticated user with in |
| CVE-2026-86595 | 8.8 | 2026-09-28 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Iron Mountain Arch |
| CVE-2026-87799 | 9.9 | 2026-09-28 | Improper link resolution in the migration receive path in Canonical LXD versions 4.0 and later (fixed in 4.0.14, 5.0.10, |
| CVE-2026-90924 | 9.8 | 2026-09-28 | Use of default credentials vulnerability in Innotim Software, Telecommunications and Consultancy Trade Ltd. Co. Logsign  |
| CVE-2026-90925 | 7.1 | 2026-09-28 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Innotim Software, Teleco |
| CVE-2026-90926 | 8.8 | 2026-09-28 | Improper Control of Generation of Code ('Code Injection') vulnerability in Innotim Software, Telecommunications and Cons |
| CVE-2026-97335 | 7.7 | 2026-09-28 | Incorrect authorization in the custom storage volume creation endpoint in Canonical LXD versions 5.0.0 and later (fixed  |
| CVE-2026-101073 | 8.3 | 2026-09-28 | A security flaw has been discovered in Netcore NR289-GE 1.4.5102. Impacted is an unknown function of the file /bin/boa o |
| CVE-2026-101074 | 9.8 | 2026-09-28 | A weakness has been identified in Netcore NR289-GE 1.4.5102. The affected element is the function password-check of the  |
| CVE-2026-101075 | 10.0 | 2026-09-28 | A security vulnerability has been detected in Netcore NR289-GE 1.4.5102. The impacted element is the function system of  |
| CVE-2026-4556 | 7.8 | 2026-09-28 | Exam4 is affected by a local privilege escalation vulnerability in the com.extegrity.LogTool privileged helper, which co |
| CVE-2026-80357 | 7.0 | 2026-09-28 | Dell Boot Optimized Server Storage (BOSS), versions prior to 2.2.13.2038, contains an On-Chip Debug and Test Interface W |
| CVE-2026-93538 | 7.1 | 2026-09-28 | A cross-tenant authorization issue was discovered in SUSE Rancher Fleet. During agent-initiated cluster registration, cl |
| CVE-2026-101076 | 10.0 | 2026-09-28 | A vulnerability was detected in Netcore NR289-GE 1.4.5102. This affects the function system of the file /set_ntp_server_ |
| CVE-2026-101077 | 10.0 | 2026-09-28 | A flaw has been found in Netcore NR289-GE 1.4.5102. This impacts the function process_request of the component boa_temp  |
| CVE-2026-12342 | 9.6 | 2026-09-28 | This vulnerability
impacts all versions of IdentityIQ and allows an unauthenticated user remote
code execution on the Id |
| CVE-2026-88804 | 9.6 | 2026-09-28 | An unauthenticated update of public UI settings could be used by remote attackers to execute a stored cross-site scripti |
| CVE-2026-88805 | 8.1 | 2026-09-28 | Incorrect credential cleaning on logout could be used by remote attackers to keep access credentials even after the acco |
| CVE-2026-88808 | 8.8 | 2026-09-28 | A vulnerability has been identified within Rancher Manager where the Fleet agent wrote resources to downstream clusters  |
| CVE-2026-93348 | 8.1 | 2026-09-28 | Unsloth Zoo versions 2025.9.9 before 2026.8.14, as implemented in Unsloth 2025.9.9 through 2026.8.19, contains a code in |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-88772 | Citrix / NetScaler | 2026-09-27 | 2026-09-30 | Unknown |
| CVE-2026-88771 | Citrix / NetScaler | 2026-09-27 | 2026-09-30 | Unknown |
| CVE-2026-67279 | MikroTik / RouterOS | 2026-09-25 | 2026-09-28 | Unknown |
| CVE-2026-65660 | Microsoft / SharePoint | 2026-09-25 | 2026-09-28 | Unknown |
| CVE-2026-87902 | WordPress / Core | 2026-09-25 | 2026-09-28 | Unknown |
| CVE-2026-5430 | WSO2 / Multiple Products | 2026-09-24 | 2026-09-27 | Unknown |
| CVE-2026-71362 | Adobe / Commerce and Magento  | 2026-09-24 | 2026-09-27 | Unknown |
| CVE-2026-93952 | Arista / VeloCloud Orchestrator | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-94127 | F5 / BIG-IP APM | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-93616 | Check Point / Multiple Products | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-85102 | Check Point / Multiple Products | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-7273 | Zyxel / GS1900 Series Switches | 2026-09-21 | 2026-09-24 | Unknown |

---

*Total entries in CISA KEV catalog: 1728*