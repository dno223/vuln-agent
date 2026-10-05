# Vulnerability Intelligence Report

**Date:** 2026-10-05  
**Generated:** 2026-10-05T16:48:43Z  

---

## Executive Summary

Our environment faces 52 high-severity vulnerabilities, with critical exposure in TLS certificate validation failures across multiple libraries (go-micro, gopay, gist, Google Maps Laravel package) that enable man-in-the-middle attacks on encrypted communications. Additionally, 6 new CISA Known Exploited Vulnerabilities were added this week affecting Citrix NetScaler, Fortinet FortiMail, Cisco SD-WAN, and Zammad — all actively exploited in the wild. No monitored CVEs currently overlap with the KEV catalog, but the KEV additions demand immediate attention given confirmed exploitation. The combination of weak cryptographic validation and actively exploited infrastructure vulnerabilities presents elevated business risk.

---

## Risk Narrative

The threat landscape reflects two compounding risk categories. First, actively exploited vulnerabilities in widely deployed enterprise products — Citrix, Fortinet, and Cisco — signal organized threat actor activity targeting network perimeter and communication infrastructure. Second, systemic TLS certificate validation failures across multiple open-source libraries create persistent interception risk across development pipelines and production APIs. If exploited, these weaknesses could enable credential theft, data exfiltration, and lateral movement. The food-waste-management-system SQL injection flaws, while lower-profile, indicate third-party supply chain risk. Collectively, these vulnerabilities threaten data confidentiality, service integrity, and regulatory compliance obligations.

---

## Prioritized Action Items

1. Immediately audit and patch Citrix NetScaler, Fortinet FortiMail, and Cisco Catalyst SD-WAN Manager systems to address actively exploited CISA KEV vulnerabilities within 24–72 hours.
2. Patch or update Zammad GmbH Zammad instances to remediate both CVE-2026-102489 and CVE-2026-102490, which were added to the KEV catalog this week.
3. Upgrade go-micro to version 6.0.0 or later, gopay to 1.5.119 or later, gist RubyGem to 6.1.0 or later, and disable ssl_verify override in the Google Maps Laravel package to eliminate man-in-the-middle attack vectors.
4. Restrict or sandbox Twine 2 desktop usage and update to a patched version to mitigate the XSS vulnerability that executes arbitrary markup from imported files.
5. Conduct a full dependency audit across development and production environments to identify additional libraries with disabled TLS verification or improper certificate validation.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-105216 | 7.4 | 2026-10-04 | go-micro before 6.0.0 contains an improper certificate validation vulnerability that allows network attackers to imperso |
| CVE-2026-105218 | 7.4 | 2026-10-04 | gopay before 1.5.119 disables TLS certificate verification in defaultClient() in pkg/xhttp/client.go, allowing man-in-th |
| CVE-2026-105219 | 7.5 | 2026-10-04 | Mammoth.js 1.3.0 before 1.12.3 contains a regular expression denial of service vulnerability in the style map tokeniser  |
| CVE-2026-105166 | 7.3 | 2026-10-04 | A vulnerability was found in kishor-23 food-waste-management-system 411989e3ecb82895e53dca7865f72145f03d7d93/b3a70b2c492 |
| CVE-2026-105167 | 7.3 | 2026-10-04 | A vulnerability was determined in kishor-23 food-waste-management-system 411989e3ecb82895e53dca7865f72145f03d7d93/b3a70b |
| CVE-2026-105220 | 7.8 | 2026-10-04 | Twine 2 desktop through 2.12.0 contains a cross-site scripting vulnerability in importStories() that executes markup fro |
| CVE-2026-105221 | 7.4 | 2026-10-04 | The gist RubyGem before 6.1.0 contains an improper certificate validation vulnerability that allows on-path attackers to |
| CVE-2026-105222 | 7.4 | 2026-10-04 | The alexpechkarev/google-maps Laravel package through 12.16 disables TLS certificate verification by default because the |
| CVE-2026-105169 | 7.3 | 2026-10-05 | A security flaw has been discovered in kishor-23 food-waste-management-system 411989e3ecb82895e53dca7865f72145f03d7d93/b |
| CVE-2026-105170 | 7.3 | 2026-10-05 | A weakness has been identified in kishor-23 food-waste-management-system 411989e3ecb82895e53dca7865f72145f03d7d93/b3a70b |
| CVE-2026-105172 | 7.3 | 2026-10-05 | A vulnerability was detected in itsourcecode Online Admission System 1.0. Affected by this issue is some unknown functio |
| CVE-2026-105175 | 7.3 | 2026-10-05 | A vulnerability was found in SourceCodester Drug Recommendation System 1.0. This issue affects some unknown processing o |
| CVE-2026-105223 | 7.4 | 2026-10-05 | maclof kubernetes-client 0.17.0 before 0.32.0 disables TLS certificate verification in parseKubeconfig() and parseKubeco |
| CVE-2026-105293 | 8.1 | 2026-10-05 | Legcord 1.1.0 through 1.3.0 contains a path traversal vulnerability in theme IPC handlers that allows script in the Disc |
| CVE-2026-105294 | 7.4 | 2026-10-05 | Legcord 1.1.0 through 1.3.0 contains a configuration injection vulnerability that allows script in the Discord page to w |
| CVE-2026-105295 | 7.5 | 2026-10-05 | GitAhead 2.5.0 through 2.7.1 contains an insecure update mechanism that installs downloaded updates without integrity or |
| CVE-2026-20519 | 7.5 | 2026-10-05 | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote escalation of |
| CVE-2026-20520 | 7.5 | 2026-10-05 | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote escalation of |
| CVE-2026-20521 | 8.4 | 2026-10-05 | In Video HAL, there is a possible escalation of privilege due to a missing bounds check. This could lead to local escala |
| CVE-2026-20522 | 8.4 | 2026-10-05 | In neuropilot, there is a possible out of bounds write due to a missing bounds check. This could lead to local escalatio |
| CVE-2026-20523 | 8.4 | 2026-10-05 | In neuropilot, there is a possible out of bounds write due to a missing bounds check. This could lead to local escalatio |
| CVE-2026-20524 | 8.4 | 2026-10-05 | In apu, there is a possible memory corruption due to improper input validation. This could lead to local escalation of p |
| CVE-2026-20526 | 7.5 | 2026-10-05 | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote escalation of |
| CVE-2026-20531 | 8.4 | 2026-10-05 | In apu, there is a possible memory corruption due to use after free. This could lead to local escalation of privilege wi |
| CVE-2026-20586 | 8.8 | 2026-10-05 | In vdec, there is a possible out of bounds write due to a missing bounds check. This could lead to remote escalation of  |
| CVE-2026-105182 | 7.3 | 2026-10-05 | A security flaw has been discovered in SourceCodester Online Reviewer Management System 1.0. Impacted is an unknown func |
| CVE-2026-105183 | 7.3 | 2026-10-05 | A weakness has been identified in itsourcecode Online Admission System 1.0. The affected element is an unknown function  |
| CVE-2026-105184 | 7.3 | 2026-10-05 | A security vulnerability has been detected in itsourcecode Online Admission System 1.0. The impacted element is an unkno |
| CVE-2026-105185 | 7.3 | 2026-10-05 | A vulnerability was detected in itsourcecode Online Admission System 1.0. This affects an unknown function of the file / |
| CVE-2026-105229 | 7.3 | 2026-10-05 | A weakness has been identified in kishor-23 food-waste-management-system 411989e3ecb82895e53dca7865f72145f03d7d93/b3a70b |
| CVE-2026-105230 | 7.3 | 2026-10-05 | A security vulnerability has been detected in kishor-23 food-waste-management-system 411989e3ecb82895e53dca7865f72145f03 |
| CVE-2026-105231 | 7.3 | 2026-10-05 | A vulnerability was detected in kishor-23 food-waste-management-system 411989e3ecb82895e53dca7865f72145f03d7d93/b3a70b2c |
| CVE-2026-105232 | 7.3 | 2026-10-05 | A flaw has been found in kishor-23 food-waste-management-system 411989e3ecb82895e53dca7865f72145f03d7d93/b3a70b2c492dc99 |
| CVE-2026-105238 | 7.3 | 2026-10-05 | A flaw has been found in ChatGPTNextWeb NextChat up to 2.16.1. This vulnerability affects the function proxyHandler of t |
| CVE-2026-105246 | 7.3 | 2026-10-05 | A vulnerability was found in SourceCodester Online Reviewer Management System 1.0. Impacted is an unknown function of th |
| CVE-2026-105247 | 7.3 | 2026-10-05 | A vulnerability was determined in SourceCodester Online Reviewer Management System 1.0. The affected element is an unkno |
| CVE-2026-105314 | 7.5 | 2026-10-05 | Papermerge 3.5.3 allows remote code execution by a standard user via directory traversal in a /api/documents/upload call |
| CVE-2026-104389 | 8.5 | 2026-10-05 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Sirv Sirv sirv all |
| CVE-2026-104407 | 7.1 | 2026-10-05 | Cross-Site Request Forgery (CSRF) vulnerability in Blubrry Podcasting PowerPress Podcasting powerpress allows Cross Site |
| CVE-2026-104408 | 7.6 | 2026-10-05 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Groundhogg Groundh |
| CVE-2026-105253 | 7.3 | 2026-10-05 | A vulnerability was determined in itsourcecode Online Admission System Project 1.0. This issue affects some unknown proc |
| CVE-2026-105284 | 10.0 | 2026-10-05 | A weakness has been identified in Totolink A3002MU 1.0.0-B20230403.1455. The impacted element is the function sub_40FCFC |
| CVE-2026-19184 | 8.4 | 2026-10-05 | The NXP GAU ADC driver (drivers/adc/adc_mcux_gau_adc.c) validated the caller-supplied sequence->buffer_size, which is ex |
| CVE-2026-19185 | 7.8 | 2026-10-05 | The system-call verifier for i3c_do_ccc() in drivers/i3c/i3c_handlers.c validated the outer struct i3c_ccc_payload, the  |
| CVE-2026-105285 | 10.0 | 2026-10-05 | A security vulnerability has been detected in Totolink A3002MU 1.0.0-B20230403.1455. This affects an unknown function of |
| CVE-2026-105290 | 7.3 | 2026-10-05 | A vulnerability was determined in feelec-yishu feelcrm-os 1.0.0. This affects an unknown part of the file App/Feelcrm/In |
| CVE-2026-105307 | 7.3 | 2026-10-05 | A vulnerability was detected in Casdoor up to 3.161.1. Affected is the function ApiFilter of the file routers/authz_filt |
| CVE-2026-77805 | 7.9 | 2026-10-05 | In Progress® Telerik® Fiddler® Classic for Windows, versions prior to v6.0.20262.10021, the integrity check applied to t |
| CVE-2026-92931 | 8.8 | 2026-10-05 | CWE-918: Server-Side Request Forgery in the Progress @progress/sitefinity-nextjs-sdk npm package versions 15.1.8326 thro |
| CVE-2026-79820 | 9.0 | 2026-10-05 | A remote user validation failure vulnerability exists in HPE Integrated Lights-Out (iLO) 7 firmware. |
| CVE-2026-104890 | 7.2 | 2026-10-05 | Kunstmaan CMS is an open source content management system based on the Symfony framework. Prior to 7.3.2, src/Kunstmaan/ |
| CVE-2026-104891 | 7.5 | 2026-10-05 | mppx-condition-gate provides conditional free-access wrappers for mppx payment methods. Prior to @insumermodel/mppx-cond |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-88779 | Citrix / NetScaler | 2026-10-04 | 2026-10-07 | Unknown |
| CVE-2026-102490 | Zammad GmbH / Zammad | 2026-10-02 | 2026-10-05 | Unknown |
| CVE-2026-102489 | Zammad GmbH / Zammad | 2026-10-02 | 2026-10-05 | Unknown |
| CVE-2026-104286 | Fortinet / FortiMail | 2026-10-01 | 2026-10-04 | Unknown |
| CVE-2026-76504 | Cisco / Catalyst SD-WAN Manager | 2026-09-30 | 2026-10-03 | Unknown |
| CVE-2026-86950 | Apple / Multiple Products | 2026-09-29 | 2026-10-02 | Unknown |

---

*Total entries in CISA KEV catalog: 1734*