# Vulnerability Intelligence Report

**Date:** 2026-08-04  
**Generated:** 2026-08-04T10:37:17Z  

## Pipeline Warnings

- summarizer failed: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}, 'request_id': 'req_011CdhZZzEbREsuNHGmGH9rH'}

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
| CVE-2026-18598 | 8.8 | 2026-08-03 | A vulnerability was detected in GL.iNet GL-MT3000 up to 4.4.5. The affected element is the function logread.get_system_l |
| CVE-2026-18599 | 8.0 | 2026-08-03 | A flaw has been found in GL.iNet GL-MT3000 up to 4.4.5. The impacted element is the function logread.set_config of the f |
| CVE-2026-2346 | 9.8 | 2026-08-03 | Authorization bypass through User-Controlled key vulnerability in Menulux Software Inc. Mobile App allows Software Integ |
| CVE-2026-18089 | 7.5 | 2026-08-03 | Net::SAML2 versions before 0.86 for Perl allow SAML authentication bypass by verifying responses against the response-em |
| CVE-2026-18092 | 8.1 | 2026-08-03 | Net::SAML2 versions before 0.86 for Perl allow SAML authentication bypass via XML signature wrapping because new_from_xm |
| CVE-2026-18108 | 9.8 | 2026-08-03 | Net::SAML2 versions before 0.86 for Perl allow authentication bypass because _verify_encrypted_assertion accepts an Encr |
| CVE-2026-18600 | 8.8 | 2026-08-03 | A vulnerability has been found in GL.iNet GL-MT3000 up to 4.4.5. This affects the function network.switch_info/network.s |
| CVE-2026-18601 | 9.8 | 2026-08-03 | A vulnerability was found in GL.iNet GL-MT3000 up to 4.4.5. This impacts the function ovpn-client.check_config of the fi |
| CVE-2026-18642 | 7.8 | 2026-08-03 | Deserialization of untrusted data vulnerability in TUBITAK BILGEM Software Technologies Research Institute eta-otp-lock  |
| CVE-2026-64827 | 9.8 | 2026-08-03 | Telenia Software TVox 26.5.3 and prior 26.x versions, and 24.9.21 and prior 24.x versions, contain an authentication byp |
| CVE-2026-67608 | 7.2 | 2026-08-03 | Telenia Software TVox 26.5.3 and prior 26.x versions, and 24.9.21 and prior 24.x versions, contain an OS command injecti |
| CVE-2026-68584 | 8.6 | 2026-08-03 | SiYuan versions before v3.7.3 contain an authentication bypass vulnerability in publish mode where content-returning end |
| CVE-2026-68586 | 8.6 | 2026-08-03 | SiYuan before v3.7.3 fails to apply publish-access filters to the getBacklinkDoc and getBackmentionDoc content endpoints |
| CVE-2026-68587 | 8.6 | 2026-08-03 | SiYuan versions before v3.7.3 contain an information disclosure vulnerability in the getHeadingDeleteTransaction, getHea |
| CVE-2026-69083 | 10.0 | 2026-08-03 | SiYuan versions before v3.7.3 contain SQL injection vulnerabilities in the fullTextSearchAssetContent endpoint reachable |
| CVE-2026-69084 | 10.0 | 2026-08-03 | SiYuan versions <= v3.7.2 expose the /api/search/searchEmbedBlock endpoint, which passes a client-supplied SQL statement |
| CVE-2026-69085 | 10.0 | 2026-08-03 | SiYuan before v3.7.3 contains a SQL injection vulnerability in the /api/filetree/searchDocs endpoint, where the caller-s |
| CVE-2026-69086 | 7.7 | 2026-08-03 | SiYuan versions before v3.7.3 fail to validate the avID parameter on all code branches in attribute-view read endpoints, |
| CVE-2026-69088 | 8.1 | 2026-08-03 | Grav CMS versions 2.0.7 through 2.0.10 fail to validate fully-qualified static method calls (Class::method) in blueprint |
| CVE-2026-69089 | 7.5 | 2026-08-03 | Grav CMS 2.0.10 contains a path traversal vulnerability in ImageMedium::watermark(), which passes its unsanitized $image |
| CVE-2026-69091 | 7.5 | 2026-08-03 | Admidio before 5.0.11 contains an authentication bypass vulnerability in the forum module when configured in login-only  |
| CVE-2026-69095 | 7.5 | 2026-08-03 | OpenWrt luci-app-bmx7 before commit 5890760a454dad2cb00389dba2cdc5e779e0ffdd contains a path traversal vulnerability in  |
| CVE-2026-69096 | 8.8 | 2026-08-03 | OpenWrt luci-app-dockerman (LuCI master and openwrt-25.12 snapshots containing the ucode docker_rpc.uc RPC backend after |
| CVE-2026-69097 | 7.0 | 2026-08-03 | GitPython before 3.1.53 fails to properly escape section names in git config files, allowing attackers to inject arbitra |
| CVE-2026-9390 | 9.1 | 2026-08-03 | XML::Sig versions before 0.71 for Perl allow XPath injection in ID lookup.

verify() and _get_signed_xml() in lib/XML/Si |
| CVE-2026-9487 | 9.1 | 2026-08-03 | XML::Sig versions before 0.71 for Perl allow signature wrapping via duplicate ID.

_get_signed_xml() in lib/XML/Sig.pm,  |
| CVE-2026-67609 | 7.8 | 2026-08-03 | Telenia Software TVox 26.5.3 and prior 26.x versions, and 24.9.21 and prior 24.x versions, contain a privilege escalatio |
| CVE-2026-18248 | 9.1 | 2026-08-03 | @fastify/aws-lambda version 6.4.0 decorates each Fastify request with request.awsLambda.event and request.awsLambda.cont |
| CVE-2026-18568 | 7.5 | 2026-08-03 | XML::Sig versions from 0.29 before 0.72 for Perl allow signature verification bypass because verify returns true when ev |
| CVE-2026-18602 | 9.8 | 2026-08-03 | A vulnerability was determined in GL.iNet GL-MT3000 up to 4.4.5. Affected is the function ovpn-client.get_recommend_conf |
| CVE-2026-18605 | 7.0 | 2026-08-03 | A security flaw has been discovered in CheckMAL AppCheck Pro 3.1.43.10. Affected is an unknown function in the library A |
| CVE-2026-18606 | 7.8 | 2026-08-03 | A weakness has been identified in Razer RzUpdateService 1.10.14.0. Affected by this vulnerability is an unknown function |
| CVE-2026-18607 | 8.8 | 2026-08-03 | A security vulnerability has been detected in Wavlink WN572, WN570H, WN573, WN529, WN530, WN531, WN535, etc. WN529, WN53 |
| CVE-2026-18718 | 7.0 | 2026-08-03 | Ghidra contains an arbitrary code execution vulnerability in the Swift demangler analyzer that allows an attacker to exe |
| CVE-2026-39931 | 7.2 | 2026-08-03 | OpenEMR through 8.2.0 contains an authenticated SQL injection vulnerability in the backup configuration import feature t |
| CVE-2026-39932 | 9.1 | 2026-08-03 | OpenEMR through 8.2.0 contains a remote code execution vulnerability in the document category tree component (library/cl |
| CVE-2026-41452 | 9.8 | 2026-08-03 | Krayin CRM 2.2.4 contains a missing authentication vulnerability in the installer middleware that allows unauthenticated |
| CVE-2026-41453 | 8.8 | 2026-08-03 | Krayin CRM before 2.2.4 contains a blind SQL injection vulnerability in the leads DataGrid that allows authenticated use |
| CVE-2026-61372 | 7.5 | 2026-08-03 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache Jena Fuseki.

Thi |
| CVE-2026-67610 | 8.1 | 2026-08-03 | OpenEMR through 8.2.0 contains an improper authentication vulnerability in the OAuth2 dynamic client registration endpoi |
| CVE-2026-67611 | 8.1 | 2026-08-03 | OpenEMR through 8.2.0 contains an authentication bypass vulnerability that allows attackers with valid credentials to ci |
| CVE-2026-69152 | 7.5 | 2026-08-03 | The brace-expansion library generates arbitrary strings containing a common prefix and suffix. Prior to 1.1.18, 2.1.4, 3 |
| CVE-2026-18612 | 9.8 | 2026-08-03 | A flaw has been found in GL-iNet GL-MT3000 up to 4.4.5. This vulnerability affects the function plugins.remove_package/p |
| CVE-2026-18613 | 9.8 | 2026-08-03 | A vulnerability has been found in GL-iNet GL-MT3000 up to 4.4.5. This issue affects the function plugins.set_config of t |
| CVE-2026-61523 | 7.2 | 2026-08-03 | WebsiteBaker CMS before 2.13.10 contains a code injection vulnerability in the Droplets editor that allows authenticated |
| CVE-2026-61524 | 7.2 | 2026-08-03 | WebsiteBaker CMS before 2.13.10 contains an unrestricted file upload vulnerability in the module installation feature th |
| CVE-2026-18614 | 9.8 | 2026-08-03 | A vulnerability was found in GL-iNet GL-MT3000 up to 4.4.5. Impacted is the function s2s.enable_echo_server of the file  |
| CVE-2026-18615 | 9.8 | 2026-08-03 | A vulnerability was determined in GL-iNet GL-MT3000 up to 4.4.5. The affected element is the function wg-server.generate |
| CVE-2026-18616 | 9.8 | 2026-08-03 | A vulnerability was identified in GL-iNet GL-MT3000 up to 4.4.5. The impacted element is the function server.set_peer of |
| CVE-2026-38447 | 9.8 | 2026-08-03 | osTicket 1.18.3 generates API keys using a predictable construction based on MD5 hashing. The use of MD5, combined with  |
| CVE-2026-59912 | 7.8 | 2026-08-03 | Dell Display and Peripheral Manager (DDPM Mac), versions prior to 2.3.0.1005, contain an Improper Access Control vulnera |
| CVE-2026-59913 | 7.8 | 2026-08-03 | Dell Display and Peripheral Manager (DDPM Mac), versions prior to 2.3.0.1005, contain a Missing Authentication for Criti |
| CVE-2026-18641 | 7.3 | 2026-08-03 | A vulnerability was determined in Sangfor Operation and Maintenance Security Management System up to 3.0.13. Affected by |
| CVE-2026-48031 | 9.1 | 2026-08-03 | go-base is a Go RESTful API Boilerplate template with JWT Authentication, backed by PostgreSQL. In versions prior to 202 |
| CVE-2026-67598 | 7.4 | 2026-08-03 | Emlog Pro through 2.6.23 contains a disabled TLS certificate validation vulnerability in include/service/ai.php that all |
| CVE-2026-67599 | 7.2 | 2026-08-03 | ClearOS 7.9 contains an OS command injection vulnerability in the Log Viewer component that allows authenticated attacke |
| CVE-2026-69185 | 7.5 | 2026-08-03 | Socket.IO enables bidirectional and low-latency communication for every platform. Prior to 4.2.7, 3.4.5, and 3.3.6, a sp |
| CVE-2026-18647 | 7.3 | 2026-08-03 | A security vulnerability has been detected in jina-ai reader up to 1574bfd380d249c86c82db4dace0d9c8fe17e2b1. This issue  |
| CVE-2026-18733 | 8.8 | 2026-08-03 | A prompt injection vulnerability in the shell tool in Amazon Strands Agents Tools before 0.8.0 might allow remote actors |
| CVE-2026-41447 | 7.8 | 2026-08-03 | FirmaCheck for Windows before 1.3.16 contains a dll hijacking vulnerability that allows local attackers to execute arbit |
| CVE-2026-69240 | 9.8 | 2026-08-03 | Sequelize is a Node.js ORM tool. Prior to 6.37.4, SQL injection is possible with strings only if dialect is set to oracl |
| CVE-2026-69246 | 7.2 | 2026-08-03 | Guzzle is an extensible PHP HTTP client. Prior to 7.15.2 and 8.0.1, Guzzle gives a transport the request URI as text and |
| CVE-2026-10849 | 8.2 | 2026-08-03 | The hawkBit device management client in subsys/mgmt/hawkbit accumulates the body of an HTTP response from the update ser |
| CVE-2026-18667 | 9.6 | 2026-08-03 | A vulnerability in Tenable Sensor Proxy allows a remote attacker to execute code with elevated privileges by inducing an |
| CVE-2026-18684 | 9.8 | 2026-08-03 | A weakness has been identified in GL.iNet GL-MT3000 up to 4.4.5. This issue affects the function remove_profile of the f |
| CVE-2026-48317 | 9.6 | 2026-08-03 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Directives in Dynamically Evaluated Code ('Eva |
| CVE-2026-48323 | 10.0 | 2026-08-03 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements Used in a Template Engine vul |
| CVE-2026-48326 | 9.9 | 2026-08-03 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL  |
| CVE-2026-48330 | 10.0 | 2026-08-03 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL  |
| CVE-2026-48331 | 10.0 | 2026-08-03 | Adobe Campaign Classic (ACC) is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in priv |
| CVE-2026-48333 | 9.8 | 2026-08-03 | Adobe Campaign Classic (ACC) is affected by an Incorrect Authorization vulnerability that could result in privilege esca |
| CVE-2026-48399 | 7.5 | 2026-08-03 | Adobe Campaign Classic (ACC) is affected by a Violation of Secure Design Principles vulnerability that could result in a |
| CVE-2026-18685 | 9.8 | 2026-08-04 | A security vulnerability has been detected in GL.iNet GL-MT3000 up to 4.4.5. Impacted is the function set_upgrade of the |
| CVE-2026-18686 | 9.8 | 2026-08-04 | A vulnerability was detected in GL.iNet GL-MT3000 up to 4.4.5. The affected element is the function nas-web.add_user of  |
| CVE-2026-62870 | 8.8 | 2026-08-04 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-65802 | 7.4 | 2026-08-04 | External control of file name or path in Microsoft Edge for Android allows an unauthorized attacker to disclose informat |
| CVE-2026-66310 | 7.7 | 2026-08-04 | External control of file name or path in Microsoft Edge for Android allows an unauthorized attacker to disclose informat |
| CVE-2026-66315 | 7.5 | 2026-08-04 | Use after free in Microsoft Edge (Chromium-based) allows an unauthorized attacker to execute code over a network. |
| CVE-2026-66318 | 8.1 | 2026-08-04 | Origin validation error in Microsoft Edge (Chromium-based) allows an unauthorized attacker to disclose information over  |
| CVE-2026-66321 | 7.4 | 2026-08-04 | Access of resource using incompatible type ('type confusion') in Microsoft Edge (Chromium-based) allows an unauthorized  |
| CVE-2026-66322 | 7.1 | 2026-08-04 | Origin validation error in Microsoft Edge (Chromium-based) allows an unauthorized attacker to perform spoofing over a ne |
| CVE-2026-56845 | 7.5 | 2026-08-04 | An unauthenticated path traversal (LFI) vulnerability exists under /custom-sounds/ when CustomSounds storage is configur |
| CVE-2026-56846 | 7.5 | 2026-08-04 | A flaw in Node.js HTTP/2 handling can cause HTTP/2 retained header blocks evade maxSessionMemory and enable remote memor |
| CVE-2026-6837 | 7.2 | 2026-08-04 | A post-authentication command injection vulnerability in the "export-cgi" CGI program in Zyxel WAX650S firmware versions |
| CVE-2026-14818 | 7.2 | 2026-08-04 | A path traversal vulnerability in the CLI command used to execute configuration files in Zyxel ATP series firmware versi |
| CVE-2026-42169 | 7.3 | 2026-08-04 | A heap-buffer-overflow vulnerability exists in the APNG (Animated PNG) file loader of GIMP. This flaw occurs when the `f |
| CVE-2026-18753 | 9.1 | 2026-08-04 | The
product firmware contains an embedded, static RSA private key utilized by the
Lighttpd web server for TLS terminatio |
| CVE-2026-18754 | 9.1 | 2026-08-04 | The
product firmware contains an embedded, static RSA private key utilized by the
Lighttpd web server for TLS terminatio |
| CVE-2026-18755 | 7.3 | 2026-08-04 | A DLL hijacking vulnerability in GeoVision GV-ASManager allows a local attacker with write access to an unsafe search di |
| CVE-2026-67243 | 7.2 | 2026-08-04 | freo2 provided by refirio contains an unrestricted upload of file with dangerous type vulnerability. A user with the hig |
| CVE-2026-14175 | 9.8 | 2026-08-04 | Unrestricted upload of file with dangerous type vulnerability in Bilin Software and Informatics Consultancy Inc. HUMANIS |
| CVE-2026-14804 | 9.1 | 2026-08-04 | Use of hard-coded cryptographic key vulnerability in Bilin Software and Informatics Consultancy Inc. HUMANIST Digital Hu |
| CVE-2026-14838 | 7.4 | 2026-08-04 | Use of GET request method with sensitive query strings vulnerability in Bilin Software and Informatics Consultancy Inc.  |
| CVE-2026-15721 | 9.8 | 2026-08-04 | Cleartext storage of sensitive information vulnerability in Bilin Software and Informatics Consultancy Inc. HUMANIST Dig |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-18577 | N-able / N-central | 2026-08-03 | 2026-08-06 | Unknown |
| CVE-2026-20316 | Cisco / Secure Firewall Management Center (FMC) | 2026-07-29 | 2026-08-01 | Unknown |

---

*Total entries in CISA KEV catalog: 1657*