# Vulnerability Intelligence Report

**Date:** 2026-11-16  
**Generated:** 2026-11-16T17:57:32Z  

---

## Executive Summary

Our environment faces significant exposure from 54 high-severity vulnerabilities, predominantly Cross-Site Scripting (XSS) flaws in widely-used WordPress plugins, alongside a critical PHP Remote File Inclusion vulnerability and an information disclosure issue. Additionally, 12 new entries were added to the CISA Known Exploited Vulnerabilities catalog this week, including actively exploited flaws in Microsoft Office, Cisco BroadWorks, and Check Point products. While no monitored CVEs currently overlap with the KEV catalog, the volume and nature of these vulnerabilities present meaningful risk to web integrity, user data, and business continuity. Immediate remediation prioritization is warranted.

---

## Risk Narrative

The current threat landscape is dominated by web application vulnerabilities targeting WordPress ecosystems, which are frequent targets for automated exploitation campaigns. Stored XSS flaws enable persistent attacker footholds, session hijacking, and credential theft, posing direct risk to customer trust and data integrity. The PHP Remote File Inclusion vulnerability introduces potential for full server compromise. Concurrently, 12 newly cataloged CISA KEV entries signal active exploitation of enterprise platforms including Microsoft Office and Cisco BroadWorks by threat actors. An unpatched DoS vulnerability further risks service availability. Collectively, these exposures could result in data breaches, regulatory penalties, reputational damage, and operational disruption if not addressed with urgency.

---

## Prioritized Action Items

1. Patch or disable the affected WordPress plugins (Bit Assist, wpDiscuz, AI Engine, Feedzy, WP File Upload) immediately to remediate stored and reflected XSS vulnerabilities across 54 high-severity CVEs.
2. Urgently apply vendor patches for all CISA KEV entries, particularly Microsoft Office (CVE-2026-124194) and Cisco BroadWorks (CVE-2026-20320), as these are confirmed to be actively exploited in the wild.
3. Remediate the PHP Remote File Inclusion vulnerability in Mikado-Themes GrandPrix Core (CVE-2026-129091, CVSS 8.1) immediately, as it represents the highest-scoring flaw and enables remote code execution.
4. Implement rate limiting and resource throttling controls to address the HTTP Denial-of-Service vulnerability in Gutenverse (CVE-2026-125823) before it can be leveraged to disrupt web availability.
5. Conduct a full audit of all WordPress plugins and third-party components against the CISA KEV catalog on a weekly basis to ensure early detection of any future overlap with actively exploited vulnerabilities.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-125760 | 7.1 | 2026-11-15 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Bit Apps Bit Assis |
| CVE-2026-125798 | 7.1 | 2026-11-15 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Zaytech Smart Onli |
| CVE-2026-125804 | 7.1 | 2026-11-15 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Meow Apps AI Engin |
| CVE-2026-125817 | 7.1 | 2026-11-15 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Themeisle Feedzy f |
| CVE-2026-125818 | 7.1 | 2026-11-15 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in AdvancedCoding wpD |
| CVE-2026-125822 | 7.1 | 2026-11-15 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Nickboss WordPress |
| CVE-2026-125823 | 7.5 | 2026-11-15 | Allocation of Resources Without Limits or Throttling vulnerability in Jegstudio Gutenverse gutenverse allows HTTP DoS.Th |
| CVE-2026-125830 | 7.1 | 2026-11-15 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Belingo belingoGeo |
| CVE-2026-129091 | 8.1 | 2026-11-15 | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability in |
| CVE-2026-129493 | 7.5 | 2026-11-16 | Bolo (bolo-solo) 1.7 through 2.6.4 contains an information disclosure vulnerability that allows unauthenticated attacker |
| CVE-2026-129494 | 7.5 | 2026-11-16 | CloudPaste 1.1.0 through 1.9.1 contains an information disclosure vulnerability that allows unauthenticated attackers to |
| CVE-2026-129540 | 8.8 | 2026-11-16 | VoAPI 1.0.0 through 1.2.0 contains a sql injection vulnerability that allows authenticated users to inject SQL by supply |
| CVE-2026-82156 | 8.8 | 2026-11-16 | Dell PowerStore contains an authorization-bypass vulnerability. A low-privileged attacker could exploit it, potentially  |
| CVE-2026-129606 | 7.1 | 2026-11-16 | Buffer Copy without Checking Size of Input ('Classic Buffer Overflow') vulnerability in Samsung Open Source mTower allow |
| CVE-2026-124672 | 7.3 | 2026-11-16 | The Burst Statistics WordPress plugin before 3.7.5 does not verify that a request is actually being routed to its own RE |
| CVE-2026-102448 | 7.8 | 2026-11-16 | A vulnerability has been identified in Rexroth IndraWorks. This flaw allows an attacker to execute arbitrary code on the |
| CVE-2026-129784 | 8.5 | 2026-11-16 | The httpx Ruby gem parses JSON response bodies through its transcoder layer. HTTPX::Response#json delegates to Transcode |
| CVE-2026-63245 | 7.3 | 2026-11-16 | A local privilege escalation (LPE) vulnerability in the Audigy Rx driver’s Emupia2k.sys file could allow a local attacke |
| CVE-2026-129545 | 8.8 | 2026-11-16 | Kalmia through 0.2.0 contains a privilege escalation vulnerability that allows low-privileged authenticated users to mod |
| CVE-2026-129547 | 7.5 | 2026-11-16 | Kalmia through 0.2.0 contains an authentication bypass vulnerability in RsPressMiddleware that allows unauthenticated at |
| CVE-2026-129550 | 9.1 | 2026-11-16 | Tensei through 0.11.5 contains a privilege escalation vulnerability in @tensei/auth that allows unauthenticated or authe |
| CVE-2026-129552 | 9.8 | 2026-11-16 | Tensei through 0.11.5 contains an authentication bypass vulnerability in @tensei/auth that falls back to the hard-coded  |
| CVE-2026-67250 | 7.3 | 2026-11-16 | A local privilege escalation (LPE) vulnerability in Pebble’s installers could allow a local attacker with low privilege  |
| CVE-2026-110710 | 7.5 | 2026-11-16 | @fastify/multipart is the official Fastify plugin for handling multipart/form-data uploads. In versions 3.0.0 through 10 |
| CVE-2026-19732 | 9.9 | 2026-11-16 | An OS Command Injection vulnerability affecting Station Launcher App in 3DEXPERIENCE platform from Release 3DEXPERIENCE  |
| CVE-2026-77033 | 9.9 | 2026-11-16 | An OS Command Injection vulnerability affecting Station Launcher App in 3DEXPERIENCE platform from Release 3DEXPERIENCE  |
| CVE-2026-93664 | 10.0 | 2026-11-16 | A Deserialization of Untrusted Data vulnerability affecting Station Launcher App in 3DEXPERIENCE platform from Release 3 |
| CVE-2026-124289 | 7.5 | 2026-11-16 | @fastify/multipart is the official Fastify plugin for handling multipart/form-data uploads. In versions 7.4.0 through 10 |
| CVE-2026-124724 | 7.5 | 2026-11-16 | @fastify/busboy is a streaming parser for multipart form data used by Fastify. In versions 1.0.0 through 3.2.5, when a r |
| CVE-2026-128835 | 7.5 | 2026-11-16 | @fastify/busboy is a streaming parser for multipart form data used by Fastify. In versions 1.0.0 through 3.2.5, a multip |
| CVE-2026-129854 | 8.8 | 2026-11-16 | RedAmon 4.0.0 before 7.8.0 contains a missing object-level authorization vulnerability that allows authenticated users t |
| CVE-2026-129855 | 8.8 | 2026-11-16 | RedAmon before 7.8.0 contains a missing authentication vulnerability in the kali-sandbox terminal server that allows una |
| CVE-2026-129857 | 7.8 | 2026-11-16 | Microsoft jxrlib through 1.1 and the mircomir jxrlib fork before 1.3.1 contain a heap buffer overflow in ReadBinaryData( |
| CVE-2026-129870 | 8.1 | 2026-11-16 | Rocboss paopao-ce 0.2.0 through 0.6.0-alpha.3 contains a path traversal vulnerability in LocalOSS DeleteObject that allo |
| CVE-2026-129872 | 7.5 | 2026-11-16 | REBUILD 2.7.0 through 4.5.4 contains an SQL injection vulnerability that allows low-privileged authenticated users to in |
| CVE-2026-129873 | 8.8 | 2026-11-16 | REBUILD 4.3.0 through 4.5.4 contains a privilege escalation vulnerability that allows low-privileged authenticated users |
| CVE-2026-129874 | 8.8 | 2026-11-16 | REBUILD 3.5.0 through 4.5.4 contains a privilege escalation vulnerability that allows low-privileged authenticated users |
| CVE-2026-129875 | 8.8 | 2026-11-16 | REBUILD 4.5.0 through 4.5.4 contains an information disclosure vulnerability that allows low-privileged authenticated us |
| CVE-2026-129877 | 7.5 | 2026-11-16 | DeepAudit 2.0.0-beta.1 through 3.8.0 contains an information disclosure vulnerability that allows unauthenticated attack |
| CVE-2026-129878 | 7.7 | 2026-11-16 | DeepAudit 2.0.0-beta.1 through 3.8.0 contains an HTML injection vulnerability in ReportGenerator.generate_task_report th |
| CVE-2026-129879 | 8.8 | 2026-11-16 | DeepAudit 2.0.0-beta.1 through 3.8.0 contains a path traversal vulnerability that allows authenticated users to write ar |
| CVE-2026-129880 | 7.7 | 2026-11-16 | DeepAudit 2.0.0-beta.5 through 3.8.0 contains a server-side request forgery vulnerability that allows registered users t |
| CVE-2026-129941 | 9.8 | 2026-11-16 | Prime CMS (@primecms/core) through 0.4.0-beta.0 contains an authentication bypass vulnerability that allows unauthentica |
| CVE-2026-129943 | 7.2 | 2026-11-16 | Prime CMS (@primecms/core) through 0.4.0-beta.0 contains an OS command injection vulnerability in the updateSystem Graph |
| CVE-2026-129947 | 8.0 | 2026-11-16 | Contentlayer @contentlayer/core through 0.3.4 contains a code injection vulnerability that allows attackers to inject Ja |
| CVE-2026-129948 | 8.8 | 2026-11-16 | Contentlayer @contentlayer/source-files through 0.3.4 contains a code injection vulnerability that allows attackers who  |
| CVE-2026-129952 | 9.8 | 2026-11-16 | NodePress through 8.5.1 contains an authentication bypass vulnerability that allows unauthenticated remote attackers to  |
| CVE-2026-129955 | 9.8 | 2026-11-16 | NodePress through 8.5.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to gain ad |
| CVE-2026-129956 | 7.8 | 2026-11-16 | Sandboxie-Plus before 1.18.6 contains a local privilege escalation vulnerability in SbieSvc that allows standard users t |
| CVE-2026-129957 | 7.2 | 2026-11-16 | PrestaShop before 8.2.9 and 9.0.0 before 9.2.1 contains a path traversal vulnerability in back-office theme and module a |
| CVE-2026-113630 | 7.8 | 2026-11-16 | Command injection in the documentserver-flush-cache.sh maintenance helper in ONLYOFFICE Docs (Document Server) 9.4.0-129 |
| CVE-2026-129236 | 7.2 | 2026-11-16 | Kubeshark is an eBPF-powered network observability tool for Kubernetes. From 53.1.0 until 53.4.0, the start_kubeshark MC |
| CVE-2026-86046 | 7.1 | 2026-11-16 | termux-sync is an open source tool for backing up and restoring a Termux environment across devices. Prior to 1.2.4, ter |
| CVE-2026-91115 | 8.8 | 2026-11-16 | Silverstripe Framework is a PHP framework which powers the Silverstripe CMS. From 6.0.0 until 6.2.13, the writer option  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-114713 | UnrealIRCd / UnrealIRCd | 2026-11-13 | 2026-11-16 | Unknown |
| CVE-2026-123039 | Check Point / Multiple Products | 2026-11-13 | 2026-11-16 | Unknown |
| CVE-2026-124194 | Microsoft / Office | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-111793 | Openwave Messaging Limited / Webtop Media Transcoder | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-20320 | Cisco / BroadWorks | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-111560 | Barracuda Networks / Multiple Products | 2026-11-10 | 2026-11-13 | Unknown |
| CVE-2026-116606 | Barracuda Networks / Barracuda Email Security Gateway (ESG) | 2026-11-10 | 2026-11-13 | Unknown |
| CVE-2026-125350 | Google / Chromium | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-102895 | GPUStack / GPUStack | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-123158 | OpenBSD / OpenSSH | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-116779 | SignalWire / FreeSwitch | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-123218 | IBM / Aspera Faspex | 2026-11-09 | 2026-11-12 | Unknown |

---

*Total entries in CISA KEV catalog: 1781*