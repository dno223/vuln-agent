# Vulnerability Intelligence Report

**Date:** 2026-10-26  
**Generated:** 2026-10-26T14:51:30Z  

---

## Executive Summary

Our environment faces 49 high-severity vulnerabilities alongside 8 newly added CISA Known Exploited Vulnerabilities (KEVs) added in the past seven days. Notable exposure includes flaws in Yoosee cameras, EyouCMS, Plex Media Server, Arista VeloCloud Orchestrator, and Collabora Online. The Yoosee Secure Boot bypass (CVSS 8.2) and the Japan Ministry infrastructure file-handling flaw (CVSS 7.8) represent the highest individual risk scores. While no monitored CVEs currently appear in the KEV catalog, the volume and diversity of newly exploited vulnerabilities demands immediate prioritization and remediation action across network, web, and IoT assets.

---

## Risk Narrative

The threat landscape reflects active adversary exploitation of widely deployed platforms, particularly media servers and network orchestration tools now listed in CISA's KEV catalog. IoT and camera firmware vulnerabilities such as the Yoosee Secure Boot bypass create persistent, hard-to-remediate footholds. Web application flaws across multiple open-source and commercial CMS platforms broaden the attack surface for data exfiltration and server compromise. The concentration of CVSS 7.3–8.2 scores across 49 vulnerabilities, combined with 8 KEV additions in one week, signals an accelerating exploitation tempo. Business risks include unauthorized data access, operational disruption, regulatory exposure, and potential supply-chain compromise through third-party software components.

---

## Prioritized Action Items

1. Immediately patch or isolate Plex Media Server instances affected by CVE-2026-96655 and CVE-2026-96656, as active exploitation is confirmed by CISA KEV listing.
2. Remediate Arista VeloCloud Orchestrator (CVE-2026-114625) and Collabora Online (CVE-2026-110447) within 48 hours per CISA KEV mandated timelines.
3. Address the Yoosee camera Secure Boot bypass (CVE-2026-116116, CVSS 8.2) by applying vendor firmware updates or removing devices from network access.
4. Patch or restrict access to EyouCMS installations affected by CVE-2026-116094 to prevent remote file manipulation and potential system compromise.
5. Conduct an inventory audit of all SourceCodester Performance Indicator System 1.0 deployments and apply patches or retire instances to eliminate the cluster of high-severity web vulnerabilities.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-116060 | 7.3 | 2026-10-25 | A vulnerability was determined in SourceCodester Performance Indicator System 1.0. This affects an unknown part of the f |
| CVE-2026-116061 | 7.3 | 2026-10-25 | A vulnerability was identified in SourceCodester Performance Indicator System 1.0. This vulnerability affects unknown co |
| CVE-2026-116062 | 7.3 | 2026-10-25 | A security flaw has been discovered in SourceCodester Performance Indicator System 1.0. This issue affects some unknown  |
| CVE-2026-116094 | 7.3 | 2026-10-25 | A vulnerability was determined in EyouCMS up to 1.8.3. This impacts the function remote_file_to_local of the file applic |
| CVE-2026-116106 | 7.3 | 2026-10-26 | A security vulnerability has been detected in HeyCyan App 1.0.103 on Android. Affected by this vulnerability is an unkno |
| CVE-2026-116110 | 7.3 | 2026-10-26 | A vulnerability was found in GiantappMan LiveWallPaper 2.6.8.0 on Windows. This issue affects some unknown processing of |
| CVE-2026-116112 | 7.3 | 2026-10-26 | A vulnerability was identified in HashenUdara edoc-doctor-appointment-system up to cc258425b915d1af9e298777ccd26d160493e |
| CVE-2026-116116 | 8.2 | 2026-10-26 | A vulnerability was detected in Yoosee GM8135S Camera 21.00.01.36. Affected is an unknown function of the component Secu |
| CVE-2026-113345 | 7.8 | 2026-10-26 | Electronic delivery item Inspection Support System provided by Japan's Ministry of Land, Infrastructure, Transport and T |
| CVE-2026-116117 | 7.3 | 2026-10-26 | A flaw has been found in halo-dev halo up to 2.27.0-beta.1. Affected by this vulnerability is the function run.halo.app. |
| CVE-2026-107894 | 7.8 | 2026-10-26 | V-SFT provided by FUJI ELECTRIC CO., LTD. contains a stack-based buffer overflow vulnerability. Opening a crafted V7 fil |
| CVE-2026-107895 | 7.8 | 2026-10-26 | V-SFT provided by FUJI ELECTRIC CO., LTD. contains an out-of-bounds write vulnerability. Opening a crafted V7 file may l |
| CVE-2026-107896 | 7.8 | 2026-10-26 | V-SFT provided by FUJI ELECTRIC CO., LTD. contains an out-of-bounds read vulnerability in VS6ComFile!load_gr_item. Openi |
| CVE-2026-107897 | 7.8 | 2026-10-26 | V-SFT provided by FUJI ELECTRIC CO., LTD. contains an out-of-bounds read vulnerability in VS6MemInIF!set_temp_type_defau |
| CVE-2026-107898 | 7.8 | 2026-10-26 | V-SFT provided by FUJI ELECTRIC CO., LTD. contains an out-of-bounds read vulnerability in VS6EditData!CDataRomErrorCheck |
| CVE-2026-107899 | 7.8 | 2026-10-26 | V-SFT provided by FUJI ELECTRIC CO., LTD. contains an out-of-bounds read vulnerability in VS6EditData!CDataRomErrorCheck |
| CVE-2026-107900 | 7.8 | 2026-10-26 | V-SFT provided by FUJI ELECTRIC CO., LTD. contains an out-of-bounds read vulnerability in VS6ComFile!CCheck::ItemCheck.  |
| CVE-2026-116231 | 9.9 | 2026-10-26 | A security flaw has been discovered in Oray Pugongying X5 Pro 7.6.1. The impacted element is an unknown function of the  |
| CVE-2026-116232 | 9.9 | 2026-10-26 | A weakness has been identified in Oray Pugongying X5 Pro 7.6.1. This affects the function snmp_set of the component SNMP |
| CVE-2026-111841 | 8.8 | 2026-10-26 | Cross-Site Request Forgery (CSRF) vulnerability in Aman FunnelKit Automations wp-marketing-automations allows Cross Site |
| CVE-2026-116233 | 9.1 | 2026-10-26 | A security vulnerability has been detected in Oray Pugongying X5 Pro 7.6.1. This impacts an unknown function of the comp |
| CVE-2026-116234 | 9.1 | 2026-10-26 | A vulnerability was detected in Oray Pugongying X5 Pro 7.6.1. Affected is an unknown function of the file /etc/ipsec.con |
| CVE-2026-116235 | 9.1 | 2026-10-26 | A flaw has been found in Oray Pugongying X5 Pro 7.6.1. Affected by this vulnerability is an unknown functionality of the |
| CVE-2026-116236 | 7.2 | 2026-10-26 | A vulnerability has been found in Oray Pugongying X5 Pro 7.6.1. Affected by this issue is the function plugin_init of th |
| CVE-2026-70388 | 8.3 | 2026-10-26 | SOEM version 2.0.0 and earlier contains vulnerabilities where a malicious device on the network can send specially craft |
| CVE-2026-82944 | 8.8 | 2026-10-26 | SOEM version 2.0.0 and earlier contains a vulnerability in multi-segment data transfers where a malicious device can ove |
| CVE-2026-82947 | 7.1 | 2026-10-26 | SOEM version 2.0.0 and earlier contains multiple vulnerabilities in frame processing where a malicious device can cause  |
| CVE-2026-116237 | 8.4 | 2026-10-26 | A vulnerability was found in Oray Pugongying X5 Pro 7.6.1. This affects an unknown part of the component Dnsmasq. Perfor |
| CVE-2026-116253 | 7.3 | 2026-10-26 | A vulnerability was determined in DedeCMS 5.7.118. This vulnerability affects the function common.inc.php::_RunMagicQuot |
| CVE-2026-115608 | 8.5 | 2026-10-26 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Crocoblock JetEngi |
| CVE-2026-115948 | 8.5 | 2026-10-26 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in David Lingren Medi |
| CVE-2026-116256 | 7.3 | 2026-10-26 | A vulnerability was found in geesondog RhaPHP up to 7ae639ccf8dcb627faace096d030bd4cb4cfb905. Affected by this vulnerabi |
| CVE-2026-116257 | 7.3 | 2026-10-26 | A vulnerability was determined in BillaBear up to 2025.01.03. Affected by this issue is the function processInstall of t |
| CVE-2026-115717 | 7.7 | 2026-10-26 | Frappe Builder versions before 1.36.1 contain a server-side request forgery vulnerability in the convert_to_webp API end |
| CVE-2026-116260 | 7.3 | 2026-10-26 | A weakness has been identified in libimobiledevice up to 1.4.0. This issue affects the function service_receive of the f |
| CVE-2026-94380 | 8.1 | 2026-10-26 | Weak Password Recovery Mechanism for Forgotten Password vulnerability in HAVELSAN Inc. Liman MYS allows Password Recover |
| CVE-2026-107656 | 9.8 | 2026-10-26 | An authentication bypass using an alternate path or channel vulnerability in Fortinet FortiSandbox 5.0.0 through 5.0.6,  |
| CVE-2026-115188 | 9.9 | 2026-10-26 | An unrestricted file upload vulnerability exists in the campaign import feature of Mautic 7. When processing an uploaded |
| CVE-2026-115189 | 8.8 | 2026-10-26 | A server-side template injection vulnerability exists in the Twig theme rendering sandbox of Mautic. The sandbox introdu |
| CVE-2026-115190 | 8.0 | 2026-10-26 | An insecure deserialization (PHP object injection) vulnerability exists in Mautic's handling of segment filters and cust |
| CVE-2026-115191 | 7.1 | 2026-10-26 | A SQL injection vulnerability exists in a contact lookup AJAX endpoint of the Mautic administration interface (/s/ajax). |
| CVE-2026-115192 | 7.1 | 2026-10-26 | An SQL Injection vulnerability exists in the dashboard widget data API endpoint (/api/data/{type}). Chart filter paramet |
| CVE-2026-115193 | 8.2 | 2026-10-26 | A stored Cross-Site Scripting (XSS) vulnerability exists in the contact detail view of Mautic 7. Values of HTML-type cus |
| CVE-2026-116214 | 9.1 | 2026-10-26 | MacCMS v10 before 2026.1000.4054 contains an authentication bypass vulnerability that allows unauthenticated attackers t |
| CVE-2026-116218 | 7.6 | 2026-10-26 | Dolibarr ERP CRM 19.0.0 before 23.0.4 contains an SQL injection vulnerability that allows authenticated API users to inj |
| CVE-2026-116219 | 7.2 | 2026-10-26 | Dolibarr ERP CRM before 24.0.0 contains an OS command injection vulnerability in htdocs/admin/tools/export.php that lets |
| CVE-2026-116485 | 9.8 | 2026-10-26 | danmu_api before 1.21.7 contains an authentication bypass vulnerability that allows unauthenticated attackers to modify  |
| CVE-2026-59106 | 9.8 | 2026-10-26 | A security vulnerability has been identified in the WolfProt interface implementation. Insufficient neutralization of us |
| CVE-2026-59107 | 9.8 | 2026-10-26 | A security vulnerability has been identified in the vSolution Matrix file sharing feature. A shared cryptographic trust  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-114625 | Arista / VeloCloud Orchestrator | 2026-10-23 | 2026-10-26 | Unknown |
| CVE-2026-110447 | Collabora / Collabora Online – Built-in CODE Server | 2026-10-23 | 2026-10-26 | Unknown |
| CVE-2026-106931 | EG Secure Solutions / SiteGuard Server Edition | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96656 | Plex / Media Server | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96655 | Plex / Media Server | 2026-10-20 | 2026-11-03 | Unknown |
| CVE-2026-96654 | Plex / Media Server | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96652 | Plex / Media Server | 2026-10-20 | 2026-11-03 | Unknown |
| CVE-2026-110936 | Siemens / Software Center | 2026-10-20 | 2026-11-03 | Unknown |

---

*Total entries in CISA KEV catalog: 1756*