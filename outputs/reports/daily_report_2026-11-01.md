# Vulnerability Intelligence Report

**Date:** 2026-11-01  
**Generated:** 2026-11-01T14:44:57Z  

---

## Executive Summary

Our environment faces a critical threat landscape with 22 high-severity CVEs, including two rated CVSS 9.8 and one rated a perfect 10.0. A D-Link device vulnerability allows complete remote code execution, while hard-coded JWT secrets and authentication bypass flaws in Jpom and AJ-Report expose administrative access without credentials. Ten new CISA Known Exploited Vulnerabilities were added this week across Ivanti, GitLab, Cisco, and VMware products, signaling active exploitation in the wild. Immediate patching and compensating controls are required to reduce organizational exposure.

---

## Risk Narrative

Active exploitation of Ivanti, Cisco, GitLab, and VMware products confirmed by CISA KEV additions this week represents an immediate, real-world threat to enterprise infrastructure. Attackers leveraging authentication bypass and hard-coded credential flaws can achieve full administrative compromise with no user interaction. The CVSS 10.0 D-Link vulnerability poses total device takeover risk, threatening network integrity. Stored XSS and CSRF vulnerabilities broaden the attack surface to end users and web-facing services. Compounding these risks, the unsupported Apache MINA deserialization flaw will receive no vendor patch, making compensating controls essential. Collectively, these vulnerabilities increase ransomware, data exfiltration, and lateral movement risk.

---

## Prioritized Action Items

1. Immediately isolate or patch D-Link DIR-505 devices affected by the CVSS 10.0 remote code execution vulnerability CVE-2026-120189.
2. Patch Ivanti Connect Secure systems for CVE-2026-118527 and CVE-2026-111357, both newly added to the CISA KEV catalog indicating active exploitation.
3. Remediate authentication bypass vulnerabilities in Jpom (CVE-2026-120201) and AJ-Report (CVE-2026-120209) to prevent unauthorized super-administrator access.
4. Apply available patches for Cisco Secure Firewall ASA/FTD (CVE-2026-76418) and VMware ESX (CVE-2026-41709) flagged as actively exploited by CISA.
5. Address remaining high-severity CVEs in ShowDoc, Thelia, and libheif through vendor patching or temporary service restrictions to limit attack surface.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-120201 | 9.8 | 2026-10-31 | Jpom 2.10.0 through 2.11.12 contains an authentication bypass vulnerability that allows unauthenticated attackers to gai |
| CVE-2026-120203 | 8.8 | 2026-10-31 | ShowDoc 2.8.14 before 3.9.6 contains a code injection vulnerability in its Mock feature that allows authenticated users  |
| CVE-2026-120205 | 8.0 | 2026-10-31 | Thelia before 3.1.0 contains a stored cross-site scripting vulnerability in ForSomeCustomers::getSummary() that allows u |
| CVE-2026-120207 | 7.1 | 2026-10-31 | Thelia Page Module before 2.0.4 contains a cross-site request forgery vulnerability that allows remote attackers to dele |
| CVE-2026-120208 | 7.5 | 2026-10-31 | libheif 1.18.0 before 1.23.3 contains a heap-based buffer overflow vulnerability in unc_decoder_mixed_interleave::proces |
| CVE-2026-120209 | 9.8 | 2026-10-31 | AJ-Report through 1.7.1 signs share tokens with a hard-coded JWT secret, allowing attackers to forge valid Share-Tokens  |
| CVE-2026-118147 | 7.4 | 2026-10-31 | Improper certificate validation in Visual Studio allows an unauthorized attacker to perform spoofing over a network. |
| CVE-2026-118636 | 9.8 | 2026-10-31 | **UNSUPPORTED WHEN ASSIGNED** 

JavaNativeMessageDecoder in the MINA 3.0 codec module calls ObjectInputStream.readObject |
| CVE-2026-120189 | 10.0 | 2026-11-01 | A vulnerability was identified in D-Link DIR-505 1.10B02. Affected is the function save_upload_file/mp_upload_file of th |
| CVE-2026-120191 | 7.3 | 2026-11-01 | A weakness has been identified in Presenton up to 0.9.11-beta. Affected by this issue is some unknown functionality of t |
| CVE-2026-120195 | 10.0 | 2026-11-01 | A security vulnerability has been detected in WAVLINK WL-WN579A3-A 2026-03-10-94f93d4. The impacted element is the funct |
| CVE-2026-120196 | 9.9 | 2026-11-01 | A vulnerability was detected in WAVLINK WN579X3-D V250402. This affects the function port_forward of the file /cgi-bin/w |
| CVE-2026-120197 | 9.9 | 2026-11-01 | A flaw has been found in WAVLINK WL-WN530HG4B M_V260724. This impacts the function port_forward of the file /cgi-bin/wap |
| CVE-2026-120198 | 10.0 | 2026-11-01 | A vulnerability has been found in WAVLINK WL-WN530BE1-A V251117. Affected is the function con_check_read_finish of the f |
| CVE-2026-120224 | 9.9 | 2026-11-01 | A security flaw has been discovered in Oray Pugongying X5 Pro up to 7.6.1. Affected is the function run_apis_by_json/run |
| CVE-2026-120225 | 9.1 | 2026-11-01 | A weakness has been identified in Oray Pugongying X5 Pro up to 7.6.1. Affected by this vulnerability is the function con |
| CVE-2026-120227 | 9.9 | 2026-11-01 | A vulnerability was detected in WAVLINK WN701AE M01AE_V260105. This affects the function del_staticrule of the file stat |
| CVE-2026-120306 | 9.9 | 2026-11-01 | Beta9 turns each shell command in a tenant image definition into a Dockerfile RUN line and executes it with Buildah on t |
| CVE-2026-120307 | 9.9 | 2026-11-01 | The Beta9 worker serves the sandbox file API from outside the container. getHostPathFromContainerPath turns the tenant's |
| CVE-2026-120308 | 9.9 | 2026-11-01 | A Beta9 tenant can attach a volume when deploying a function, endpoint, or task queue. The gateway builds the host path  |
| CVE-2026-120228 | 9.9 | 2026-11-01 | A flaw has been found in WAVLINK WN553X1-B V260403_2.0.0. This vulnerability affects the function sub_416D88 of the file |
| CVE-2026-120229 | 9.1 | 2026-11-01 | A vulnerability has been found in WAVLINK WN553X1-B 260403_2.0.0. This issue affects the function sub_416B50 of the file |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-118527 | Ivanti / Connect Secure | 2026-10-30 | 2026-11-13 | Unknown |
| CVE-2026-111357 | Ivanti / Connect Secure | 2026-10-30 | 2026-11-02 | Unknown |
| CVE-2026-97229 | GitLab / Community Edition and Enterprise Edition | 2026-10-29 | 2026-11-01 | Unknown |
| CVE-2026-76418 | Cisco / Secure Firewall ASA Software and Cisco Secure FTD Software | 2026-10-29 | 2026-11-01 | Unknown |
| CVE-2026-41709 | Broadcom / VMware ESX | 2026-10-28 | 2026-11-11 | Unknown |
| CVE-2026-46300 | Linux / Kernel | 2026-10-28 | 2026-10-31 | Unknown |
| CVE-2026-48356 | Adobe / Commerce and Magento | 2026-10-27 | 2026-11-10 | Unknown |
| CVE-2026-111497 | Google / Brotli | 2026-10-27 | 2026-11-10 | Unknown |
| CVE-2026-109618 | PHP Group / PHP | 2026-10-26 | 2026-10-29 | Unknown |
| CVE-2026-109619 | PHP Group / PHP | 2026-10-26 | 2026-10-29 | Unknown |

---

*Total entries in CISA KEV catalog: 1766*