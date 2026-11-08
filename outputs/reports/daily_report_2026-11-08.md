# Vulnerability Intelligence Report

**Date:** 2026-11-08  
**Generated:** 2026-11-08T14:46:13Z  

---

## Executive Summary

Our environment faces significant exposure across 92 high-severity CVEs, including four critical TOTOLINK network device vulnerabilities scoring 9.1 that enable remote command execution. Additionally, three new entries were added to CISA's Known Exploited Vulnerabilities catalog this week, covering SonicWall VPN, Apple products, and WordPress Core — all actively exploited in the wild. Deserialization flaws in Treeio, SQL injection risks in DataEase, and privilege escalation in Vikunja further broaden the attack surface. Immediate action is required to prioritize patching and reduce organizational risk before adversaries can leverage these weaknesses.

---

## Risk Narrative

The current threat landscape reflects a convergence of network infrastructure weaknesses, application-layer vulnerabilities, and actively exploited flaws. Critical TOTOLINK device vulnerabilities expose network perimeters to unauthenticated remote attackers, while CISA KEV additions confirm active exploitation of SonicWall VPN and WordPress Core — common enterprise staples. Deserialization and injection flaws in DataEase and Treeio create pathways for data theft and lateral movement. Privilege escalation in Vikunja threatens data confidentiality across collaborative environments. Collectively, these vulnerabilities create compounding business risks including operational disruption, regulatory non-compliance, reputational harm, and potential data breach costs that could significantly impact revenue and stakeholder trust.

---

## Prioritized Action Items

1. Immediately audit and patch or isolate all TOTOLINK CA300-PoE devices running firmware 6.2c.884 to remediate the four critical remote code execution vulnerabilities (CVSS 9.1).
2. Apply available patches or mitigations for all three newly added CISA KEV entries — SonicWall SonicOS SSLVPN, Apple Multiple Products, and WordPress Core — within 24 to 48 hours.
3. Remediate the insecure deserialization vulnerabilities in Treeio and the SQL injection flaws in DataEase to prevent potential data exfiltration or system compromise.
4. Upgrade Vikunja to version 2.7.1 or later to close the privilege escalation and authorization bypass vulnerabilities affecting authenticated users.
5. Establish a continuous vulnerability prioritization process that cross-references all identified CVEs against the CISA KEV catalog to ensure the fastest response to actively exploited threats.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-124318 | 7.2 | 2026-11-07 | Treeio through 2.0 contains an insecure deserialization vulnerability in UpdateRecord.get_format_strings and ModuleSetti |
| CVE-2026-123990 | 7.3 | 2026-11-07 | A security vulnerability has been detected in DataEase up to 2.10.27/3.1.0. Affected is the function ExtWhere2Str.extWhe |
| CVE-2026-123991 | 7.3 | 2026-11-07 | A vulnerability was detected in DataEase up to 2.10.27. Affected by this vulnerability is the function WhitelistUtils.en |
| CVE-2026-124057 | 9.1 | 2026-11-07 | A security flaw has been discovered in TOTOLINK CA300-PoE 6.2c.884. This impacts the function setWiFiMultipleConfig of t |
| CVE-2026-124058 | 9.1 | 2026-11-07 | A weakness has been identified in TOTOLINK CA300-PoE 6.2c.884. Affected is the function setWiFiRepeaterConfig of the fil |
| CVE-2026-124059 | 9.1 | 2026-11-07 | A security vulnerability has been detected in TOTOLINK CA300-PoE 6.2c.884. Affected by this vulnerability is the functio |
| CVE-2026-124060 | 9.1 | 2026-11-07 | A vulnerability was detected in TOTOLINK CA300-PoE 6.2c.884. Affected by this issue is the function UploadCustomModule o |
| CVE-2026-120531 | 7.2 | 2026-11-07 | The Subscribe2 – Form, Email Subscribers & Newsletters plugin for WordPress is vulnerable to Stored Cross-Site Scripting |
| CVE-2026-123520 | 7.1 | 2026-11-08 | Vikunja from 0.18.0 before 2.7.1 contains a privilege escalation vulnerability that allows team owners to gain admin or  |
| CVE-2026-123522 | 7.1 | 2026-11-08 | Vikunja before 2.7.1 contains an authorization bypass vulnerability that allows authenticated users to read any task by  |
| CVE-2026-123531 | 8.8 | 2026-11-08 | Vikunja from 1.0.0 before 2.7.1 contains an uncontrolled resource consumption vulnerability that allows authenticated us |
| CVE-2026-123543 | 7.5 | 2026-11-08 | OpenAM before 16.1.4 contains a denial of service vulnerability that allows unauthenticated attackers to exhaust server  |
| CVE-2026-123545 | 7.1 | 2026-11-08 | OpenAM from 14.5.1 before 16.1.4 contains a cross-site request forgery vulnerability in the OAuth 2.0 device authorizati |
| CVE-2026-123549 | 9.8 | 2026-11-08 | OpenAM before 16.1.4 fails to enforce the Valid Creation Attributes list during self-registration, allowing anonymous at |
| CVE-2026-123550 | 9.8 | 2026-11-08 | OpenAM before 16.1.4 contains an authentication bypass vulnerability in its SAML v2.0 service provider that accepts unsi |
| CVE-2026-123551 | 10.0 | 2026-11-08 | OpenAM from 14.0.0 before 16.1.4 contains an information disclosure vulnerability that allows unauthenticated attackers  |
| CVE-2026-123554 | 7.5 | 2026-11-08 | Zebra zebrad 6.4.0 before 7.0.0 performs quadratic work in the mempool coinbase-maturity check because Transaction::coin |
| CVE-2026-123555 | 7.5 | 2026-11-08 | Zebra from 2.3.0 before 7.0.0 contains a denial of service vulnerability that allows unauthenticated peers to evade misb |
| CVE-2026-123558 | 7.5 | 2026-11-08 | Zebra zebrad before 7.0.0 contains a denial of service vulnerability that allows a malicious peer to stall checkpoint sy |
| CVE-2026-123559 | 7.5 | 2026-11-08 | Zebra before 7.0.0 contains an inefficient algorithmic complexity vulnerability that allows unauthenticated peers to exh |
| CVE-2026-123560 | 7.5 | 2026-11-08 | Zebra before 7.0.0 contains an incomplete cleanup vulnerability that allows unauthenticated peers to stall initial sync  |
| CVE-2026-123562 | 7.5 | 2026-11-08 | devalue (sveltejs/devalue) 5.8.0 before 5.9.3 contains an unhandled promise rejection in stringifyAsync: when serializin |
| CVE-2026-123563 | 7.5 | 2026-11-08 | Devalue before 5.9.3 contains a validation bypass vulnerability that allows custom ArrayBuffer revivers to skip typed-ar |
| CVE-2026-123564 | 7.5 | 2026-11-08 | Sveltejs devalue from 1.0.0 before 5.9.3 contains a memory exhaustion flaw in uneval, whose generated code for sparse ar |
| CVE-2026-123565 | 7.5 | 2026-11-08 | Sveltejs devalue before 5.9.3 contains a resource exhaustion vulnerability where repeated primitive strings cause quadra |
| CVE-2026-123566 | 7.5 | 2026-11-08 | Sveltejs devalue before 5.9.3 contains a denial of service vulnerability that allows attackers to cause CPU amplificatio |
| CVE-2026-123569 | 7.5 | 2026-11-08 | The devalue package for npm before 5.6.3 can consume excessive CPU and memory when serializing sparse arrays with uneval |
| CVE-2026-123570 | 7.5 | 2026-11-08 | The DNS wire-format message parser in hickory-proto (Hickory DNS) 0.18 before 0.26.2 preallocates record vectors sized b |
| CVE-2026-123571 | 7.5 | 2026-11-08 | Hickory DNS from 0.26.0 before 0.26.2 contains an integer underflow vulnerability in TSIG RDATA decoding that allows rem |
| CVE-2026-123572 | 7.5 | 2026-11-08 | Hickory-dns from 0.20.1 before 0.26.2 contains a denial of service vulnerability in the hickory-proto SVCB and HTTPS rec |
| CVE-2026-123573 | 7.5 | 2026-11-08 | hickory-dns from 0.20.1 before 0.26.2 contains a denial of service vulnerability in the hickory-proto SVCB and HTTPS rec |
| CVE-2026-123574 | 7.5 | 2026-11-08 | The zone file parser in the hickory-proto crate of Hickory DNS 0.24.0 before 0.26.2 panics when a single token in a zone |
| CVE-2026-123575 | 7.5 | 2026-11-08 | Hickory DNS before 0.26.2 contains a resource exhaustion vulnerability in its DNS-over-HTTPS HTTP/2 server that lacks su |
| CVE-2026-123576 | 7.5 | 2026-11-08 | Hickory DNS 0.24.0 through 0.26.1 contains a memory exhaustion vulnerability that allows remote attackers to consume ser |
| CVE-2026-123577 | 7.5 | 2026-11-08 | Hickory DNS from 0.24.0 before 0.26.2 contains a resource exhaustion vulnerability that allows remote attackers to consu |
| CVE-2026-123580 | 7.5 | 2026-11-08 | Hickory DNS hickory-net 0.26.0-beta.1 before 0.26.2 and hickory-proto through 0.26.0-alpha.1 perform insufficient checks |
| CVE-2026-123586 | 7.5 | 2026-11-08 | Hickory DNS 0.25.0-alpha.3 through 0.25.2 contains a query amplification vulnerability in its recursive resolver, which  |
| CVE-2026-123588 | 7.5 | 2026-11-08 | The recursive resolver in Hickory DNS (all versions of the hickory-recursor crate, and hickory-resolver 0.26.0 before 0. |
| CVE-2026-123595 | 8.8 | 2026-11-08 | Hickory DNS hickory-proto 0.25 through 0.26.0-alpha.1 and hickory-net 0.26.0-beta.1 before 0.26.2 contain a DNSSEC valid |
| CVE-2026-123596 | 8.8 | 2026-11-08 | Hickory DNS hickory-proto through 0.26.0-alpha.1 and hickory-net 0.26.0-beta.1 before 0.26.2 contain a DNSSEC validation |
| CVE-2026-123604 | 7.5 | 2026-11-08 | Hickory DNS hickory-resolver 0.26.0-beta.1 before 0.26.2 contains an unbounded retry loop in NameServerPool::try_send, w |
| CVE-2026-123605 | 8.8 | 2026-11-08 | Hickory DNS hickory-proto 0.1 through 0.25.0-alpha.3 and hickory-net before 0.26.2 contain a DNSSEC validation bypass be |
| CVE-2026-123606 | 7.5 | 2026-11-08 | The hickory-dns recursor in hickory-recursor 0.25.0-alpha.3 through 0.25.2 and hickory-resolver 0.26.0-alpha.1 before 0. |
| CVE-2026-123607 | 7.5 | 2026-11-08 | Hickory DNS hickory-proto 0.25.0-alpha.3 through 0.25.2 and hickory-net before 0.26.1 contain an unbounded loop vulnerab |
| CVE-2026-123608 | 7.5 | 2026-11-08 | Hickory DNS hickory-proto from 0.3.1 before 0.26.1 contains a denial of service vulnerability in BinEncoder that allows  |
| CVE-2026-123614 | 9.8 | 2026-11-08 | imgproxy from 4.0.0 before 4.0.16 contains an integer overflow in the ICO loader that allows remote attackers to trigger |
| CVE-2026-123615 | 7.5 | 2026-11-08 | imgproxy 3.3.0 before 4.0.17 contains an out-of-bounds heap read and write in the ICO loader's BMP header reconstruction |
| CVE-2026-123616 | 7.5 | 2026-11-08 | imgproxy from 3.3.0 before 4.0.16 contains an unbounded memory allocation vulnerability in the ICO loader that fails to  |
| CVE-2026-114713 | 8.6 | 2026-11-08 | The labeled-response module in UnrealIRCd 6.0.0 before 6.2.7.1 does not escape the IRCv3 "label" message tag when echoin |
| CVE-2026-124328 | 7.4 | 2026-11-08 | A vulnerability has been found in FlowCI flow-core-x up to 1.23.49. The affected element is the function ConditionManage |
| CVE-2026-124331 | 7.3 | 2026-11-08 | A vulnerability was identified in Jinher OA C6. This impacts an unknown function of the file /C6/JHSoft.Web.Project/Offi |
| CVE-2026-124424 | 7.1 | 2026-11-08 | WWBN AVideo contains a path traversal vulnerability in plugin/AI/receiveAsync.json.php that allows holders of any valid  |
| CVE-2026-124427 | 9.8 | 2026-11-08 | Craft CMS from 5.0.0 before 5.11.2 contains an authorization bypass vulnerability that allows anonymous GraphQL clients  |
| CVE-2026-124429 | 7.5 | 2026-11-08 | Craft CMS from 5.0.0 before 5.11.2 contains a privilege escalation vulnerability that allows unauthenticated public regi |
| CVE-2026-124430 | 8.8 | 2026-11-08 | Craft CMS from 5.10.0 before 5.11.2 contains a remote code execution vulnerability that allows non-administrator control |
| CVE-2026-124432 | 7.3 | 2026-11-08 | phpMyFAQ 4.1.9 before 4.1.11 and 4.2.0 pre-releases before 4.2.0-beta.3 contain an account enumeration vulnerability in  |
| CVE-2026-124434 | 7.1 | 2026-11-08 | Grav Lightbox Gallery plugin 1.1.0 before 1.3.2 on Grav 2.x calls any medium method named in image, thumb or thumb_optio |
| CVE-2026-124436 | 8.0 | 2026-11-08 | OpenRemote before 1.32.2 contains an improper authorization vulnerability that allows realm administrators to access and |
| CVE-2026-124437 | 7.5 | 2026-11-08 | Scriban before 7.5.3 contains a resource exhaustion vulnerability that allows untrusted template authors to exhaust memo |
| CVE-2026-124438 | 7.4 | 2026-11-08 | Scriban before 7.5.2 contains an information disclosure and object manipulation vulnerability that allows template autho |
| CVE-2026-124439 | 7.5 | 2026-11-08 | Scriban and Scriban.Signed before 7.5.3 contain uncontrolled recursion flaws in which postfix member, indexer, and call  |
| CVE-2026-124440 | 9.9 | 2026-11-08 | Kyverno from 1.19.1 before 1.19.2 contains an authorization bypass vulnerability in the apiCall namespace clamp that all |
| CVE-2026-124441 | 8.8 | 2026-11-08 | Kyverno before 1.19.2 contains an authorization bypass vulnerability that allows namespaced tenants to generate any reso |
| CVE-2026-124444 | 7.1 | 2026-11-08 | OpenEMR before 8.4.0 contains a mass assignment vulnerability in the patient portal OnsiteDocument query API that lets r |
| CVE-2026-124445 | 9.8 | 2026-11-08 | OpenEMR from 7.0.1 before 8.4.0 contains a flaw in src/Common/Auth/OneTimeAuth.php that ignores the enforce_onetime_use  |
| CVE-2026-124446 | 8.8 | 2026-11-08 | OpenEMR before 8.3.0 contains a path traversal vulnerability in the FaxSMS module's RCFaxClient and SignalWireClient dis |
| CVE-2026-124447 | 8.1 | 2026-11-08 | OpenEMR before 8.3.0 contains an insecure direct object reference vulnerability in OnsitePortalActivityController::Updat |
| CVE-2026-124448 | 7.6 | 2026-11-08 | OpenEMR before 8.3.0 contains a stored cross-site scripting vulnerability in the CCDA/CCD preview stylesheets, where cda |
| CVE-2026-124450 | 9.9 | 2026-11-08 | OpenEMR before 8.3.0 contains a broken access control and path traversal vulnerability in the fax/sms module disposeDocu |
| CVE-2026-124453 | 7.1 | 2026-11-08 | OpenEMR before 8.3.0 contains an insecure direct object reference vulnerability in portal/lib/persist.php that allows au |
| CVE-2026-124456 | 7.1 | 2026-11-08 | OpenEMR before 8.3.0 contains missing authorization and insecure direct object reference vulnerabilities in the oe-modul |
| CVE-2026-124457 | 7.6 | 2026-11-08 | OpenEMR before 8.3.0 contains a path traversal vulnerability in interface/billing/sl_eob_process.php that allows authent |
| CVE-2026-124459 | 8.1 | 2026-11-08 | OpenEMR before 8.3.0 contains an insecure direct object reference vulnerability in many encounter-form view and save end |
| CVE-2026-124461 | 8.1 | 2026-11-08 | OpenEMR before 8.3.0 contains a missing authorization vulnerability in library/ajax/upload.php that allows any authentic |
| CVE-2026-124463 | 8.7 | 2026-11-08 | OpenEMR before 8.3.0 contains a stored cross-site scripting vulnerability that allows authenticated users with CAMOS acc |
| CVE-2026-124466 | 7.2 | 2026-11-08 | OpenEMR before 8.4.0 contains a server-side request forgery vulnerability that allows unauthenticated attackers to make  |
| CVE-2026-124467 | 8.8 | 2026-11-08 | OpenEMR before 8.4.0 contains a local file inclusion in the ESign router (library/ESign/Router.php), which passes the un |
| CVE-2026-124468 | 7.1 | 2026-11-08 | OpenEMR before 8.3.0 contains an SQL injection vulnerability in the Standard REST API patient insurance and employer sea |
| CVE-2026-124469 | 9.9 | 2026-11-08 | OpenEMR before 8.3.0 contains an SQL injection vulnerability in the Fee Sheet drug-inventory lookup (DrugSalesService::s |
| CVE-2026-124471 | 8.1 | 2026-11-08 | OpenEMR before 8.3.0 contains a missing authorization vulnerability in interface/billing/sl_eob_invoice.php that allows  |
| CVE-2026-124472 | 8.1 | 2026-11-08 | OpenEMR before 8.3.0 contains a missing authorization vulnerability in interface/billing/sl_eob_patient_note.php that al |
| CVE-2026-124473 | 7.1 | 2026-11-08 | OpenEMR before 8.3.0 contains a broken object-level authorization vulnerability in the SOAP note update API, which does  |
| CVE-2026-124475 | 7.1 | 2026-11-08 | OpenEMR before 8.3.0 contains an insecure direct object reference vulnerability in portal/lib/persist.php that allows au |
| CVE-2026-124477 | 8.8 | 2026-11-08 | OpenEMR before 8.3.0 contains a missing authorization vulnerability that allows low-privileged authenticated users to de |
| CVE-2026-124480 | 8.8 | 2026-11-08 | OpenEMR before 8.4.0 contains an authorization bypass vulnerability that allows low-privileged authenticated users to re |
| CVE-2026-124483 | 8.3 | 2026-11-08 | OpenEMR before 8.4.0 contains an incorrect authorization vulnerability because the prescription REST API routes check th |
| CVE-2026-124484 | 8.8 | 2026-11-08 | OpenEMR before 8.4.0 contains a missing authorization vulnerability in portal onsite-document APIs that allows any authe |
| CVE-2026-124486 | 8.8 | 2026-11-08 | OpenEMR before 8.3.0 contains a missing authorization vulnerability in the classic document controller that allows low-p |
| CVE-2026-124488 | 8.1 | 2026-11-08 | OpenEMR before 8.3.0 contains an authorization bypass vulnerability that allows authenticated clinicians lacking high-se |
| CVE-2026-124489 | 7.1 | 2026-11-08 | OpenEMR before 8.3.0 contains a broken access control vulnerability in portal/portal_payment.php that allows low-privile |
| CVE-2026-124490 | 9.1 | 2026-11-08 | OpenEMR before 8.3.0 contains a path traversal vulnerability in the RingCentral RCFaxClient disposeDocument() method of  |
| CVE-2026-124492 | 7.6 | 2026-11-08 | SunEditor before 3.4.0 contains a stored cross-site scripting vulnerability in ModalAnchorEditor's #createBookmarkList,  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-19868 | SonicWall / SonicOS SSLVPN | 2026-11-06 | 2026-11-20 | Unknown |
| CVE-2024-27834 | Apple / Multiple Products | 2026-11-04 | 2026-11-18 | Unknown |
| CVE-2026-119977 | WordPress / WordPress Core | 2026-11-03 | 2026-11-06 | Unknown |

---

*Total entries in CISA KEV catalog: 1769*