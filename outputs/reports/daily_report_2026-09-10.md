# Vulnerability Intelligence Report

**Date:** 2026-09-10  
**Generated:** 2026-09-10T12:42:54Z  

## Pipeline Warnings

- summarizer failed: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}, 'request_id': 'req_011Ceun5XWkVQe1mbU5sxFAr'}

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
| CVE-2026-85102 | 9.8 | 2026-09-09 | Improper certificate trust validation during VPN negotiation in Check Point Quantum Security Gateway may allow an unauth |
| CVE-2026-85103 | 9.8 | 2026-09-09 | A heap-based buffer overflow in VPN certificate ASN.1 decoding may allow an unauthenticated remote attacker to execute a |
| CVE-2023-54355 | 7.5 | 2026-09-09 | PocketMine-MP versions before 5.3.1 and 4.23.1 fail to validate that the identityPublicKey in LoginPacket uses the requi |
| CVE-2023-54390 | 7.5 | 2026-09-09 | PocketMine-MP versions before 5.3.1 and 4.23.1 contain a denial of service vulnerability in LoginPacket JSON parsing due |
| CVE-2023-54393 | 7.5 | 2026-09-09 | PocketMine-MP versions before 4.20.5 contain a denial of service vulnerability in LoginPacket JSON parsing due to improp |
| CVE-2024-58381 | 7.5 | 2026-09-09 | PocketMine-MP before 5.11.1 contains a denial of service vulnerability in LoginPacket JSON processing that allows remote |
| CVE-2024-58382 | 7.5 | 2026-09-09 | league/commonmark versions before 2.6.0 contain polynomial time complexity vulnerabilities in Markdown parsing that allo |
| CVE-2026-56711 | 8.8 | 2026-09-09 | VLC media player computes the size of a picture buffer with 32-bit arithmetic and allocates from the wrapped result. In  |
| CVE-2026-79738 | 7.5 | 2026-09-09 | Dell SCG 5.0 Appliance versions prior to 5.36.00.16 and Dell SCG 5.0 Application versions prior to 5.36.00.00, contains  |
| CVE-2026-79740 | 7.5 | 2026-09-09 | Dell SCG 5.0 Appliance versions prior to 5.36.00.16 and Dell SCG 5.0 Application versions prior to 5.36.00.00, contains  |
| CVE-2026-79950 | 7.5 | 2026-09-09 | Dell SCG 5.0 Appliance versions prior to 5.36.00.16 and Dell SCG 5.0 Application versions prior to 5.36.00.00, contains  |
| CVE-2026-86099 | 8.2 | 2026-09-09 | Chainlit through 2.12.0 fails to validate the client-supplied socket.io sessionId parameter, allowing unauthenticated at |
| CVE-2026-86199 | 7.5 | 2026-09-09 | PocketMine-MP versions before 5.43.1 fail to properly validate the Certificate field during offline login authentication |
| CVE-2026-86201 | 7.5 | 2026-09-09 | PocketMine-MP before 5.41.1 contains a denial of service vulnerability in LoginPacket processing where large or complex  |
| CVE-2026-86741 | 8.5 | 2026-09-09 | Snipe-IT versions before 8.7.0 fail to sanitize the category EULA text field before rendering it in checkout confirmatio |
| CVE-2026-86750 | 7.7 | 2026-09-09 | Snipe-IT versions <= 8.6.3 (fixed in 8.7.0) do not validate company assignment authorization before persisting user reco |
| CVE-2026-86751 | 8.5 | 2026-09-09 | Snipe-IT before 8.7.0 fails to properly sanitize markdown image syntax in note fields, allowing authenticated users to r |
| CVE-2026-86754 | 7.3 | 2026-09-09 | Snipe-IT before 8.7.0 fails to properly gate Laravel Passport's OAuth client management routes, allowing any authenticat |
| CVE-2026-86759 | 7.1 | 2026-09-09 | Snipe-IT versions before 8.7.0 fail to authorize the POST /hardware/history endpoint, allowing any authenticated user to |
| CVE-2026-86762 | 8.1 | 2026-09-09 | Snipe-IT before 8.7.0 does not apply the CheckUserIsActivated middleware to the `api` middleware group in app/Http/Kerne |
| CVE-2026-86770 | 8.1 | 2026-09-09 | Snipe-IT before 8.7.0 fails to validate username case sensitivity during SAML authentication, allowing attackers to auth |
| CVE-2026-86771 | 7.6 | 2026-09-09 | Snipe-IT versions before 8.7.0 fail to HTML-escape the employee_num field in the acceptance PDF generator, allowing atta |
| CVE-2026-86775 | 8.6 | 2026-09-09 | knowns (npm package) versions <= 0.29.1 contain a path traversal vulnerability in the Document API. The HTTP handler in  |
| CVE-2026-26212 | 7.2 | 2026-09-09 | Rara One Click Demo Import plugin for WordPress before 1.3.5 contains an arbitrary file upload vulnerability that allows |
| CVE-2026-79617 | 7.1 | 2026-09-09 | Incorrect Permission Assignment for Critical Resource vulnerability in TÜBİTAK BİLGEM Software Technologies Research Ins |
| CVE-2026-87822 | 7.5 | 2026-09-09 | t-digest versions 3.1 through 3.3 fail to validate centroid means during deserialization in MergingDigest.fromBytes, all |
| CVE-2026-87823 | 8.2 | 2026-09-09 | zstd-jni before 1.5.7-14 performs 32-bit signed bounds checks on three direct-ByteBuffer frame-size native methods, allo |
| CVE-2026-87824 | 7.5 | 2026-09-09 | zstd-jni before 1.5.7-14 fails to validate the samples buffer capacity in Zstd.trainFromBufferDirect, allowing attackers |
| CVE-2026-87825 | 7.7 | 2026-09-09 | zstd-jni before 1.5.7-14 contains a use-after-free vulnerability where streams and contexts hold a dictionary's shared l |
| CVE-2026-87877 | 7.7 | 2026-09-09 | zstd-jni versions before 1.5.7-14 fail to validate closed state in setDict, setLongMax, setLevel and setRefMultipleDDict |
| CVE-2026-22590 | 9.1 | 2026-09-09 | eprosima Fast DDS is a C++ implementation of the DDS (Data Distribution Service) standard of the OMG (Object Management  |
| CVE-2026-22591 | 7.5 | 2026-09-09 | eprosima Fast DDS is a C++ implementation of the DDS (Data Distribution Service) standard of the OMG (Object Management  |
| CVE-2026-67401 | 9.9 | 2026-09-09 | A vulnerability in cPanel allows a mail-enabled account to achieve remote code execution as root through SQLi in EmailTr |
| CVE-2026-77974 | 8.0 | 2026-09-09 | After spoofing the device and obtaining one user confirmation, an attacker may be able to cause the application to trans |
| CVE-2026-81640 | 8.8 | 2026-09-09 | An attacker could derive the camera's Wi-Fi password and connect to its wireless network. This weakens or eliminates the |
| CVE-2026-82563 | 7.6 | 2026-09-09 | An attacker could impersonate the camera and place themselves in a man-in-the-middle or device-emulation position. This  |
| CVE-2026-18147 | 8.1 | 2026-09-09 | A flaw was found in FreeIPA. An unauthenticated remote attacker could exploit a DOM Cross-Site Scripting (XSS) vulnerabi |
| CVE-2026-23855 | 7.2 | 2026-09-09 | Dell iDRAC9, 14G versions prior to 7.00.00.184, 15G/16G versions prior to 7.30.10.50, and Dell iDRAC10, 17G versions pri |
| CVE-2026-80914 | 8.8 | 2026-09-09 | In the Linux kernel, the following vulnerability has been resolved:

Bluetooth: ISO: fix use-after-free of listener sock |
| CVE-2026-80921 | 8.8 | 2026-09-09 | In the Linux kernel, the following vulnerability has been resolved:

KVM: s390: vsie: zero stale crypto bits

When shado |
| CVE-2026-80924 | 7.5 | 2026-09-09 | In the Linux kernel, the following vulnerability has been resolved:

crypto: krb5 - use kfree_sensitive() for derived ke |
| CVE-2026-87853 | 7.5 | 2026-09-09 | A flaw was found in SSSD's IdP authentication provider. The eval_access_token_buf() function compares the OIDC subject i |
| CVE-2026-87874 | 8.1 | 2026-09-09 | A flaw was found in the memcached cache plugin of the community.general Ansible
collection. Although its documentation s |
| CVE-2026-87927 | 8.2 | 2026-09-09 | MaxSite CMS through 109.6 contains a local file inclusion vulnerability in the ajax and require-maxsite dispatchers that |
| CVE-2026-87929 | 9.8 | 2026-09-09 | MaxSite CMS through 109.6 ships with a hardcoded session encryption key in application/config/config.php that is never c |
| CVE-2026-87930 | 8.1 | 2026-09-09 | MaxSite CMS through 109.6 passes the ci_session cookie to unserialize() without class restrictions, allowing unauthentic |
| CVE-2026-54694 | 9.6 | 2026-09-09 | SkillTree is a micro-learning gamification platform. Prior to version 4.4.2, two independent code flaws combine into a s |
| CVE-2026-79322 | 8.6 | 2026-09-09 | SQL injection in the RelatedProduct block in Mageplaza Blog for Magento 2 (mageplaza/magento-2-blog-extension) through 4 |
| CVE-2026-79323 | 7.5 | 2026-09-09 | Information disclosure in the blogComments GraphQL query in Magefan Blog GraphQL for Magento 2 (magefan/module-blog-grap |
| CVE-2026-73769 | 7.2 | 2026-09-09 | A vulnerability in the web-based management interface of vulnerable CPPM systems could allow an authenticated remote att |
| CVE-2026-73786 | 7.5 | 2026-09-09 | A vulnerability in the web-based management interface of CPPM could allow an unauthenticated remote attacker to conduct  |
| CVE-2026-73787 | 7.2 | 2026-09-09 | A vulnerability in the CPPM web interface could allow an authenticated remote attacker to access directory information o |
| CVE-2026-79324 | 7.5 | 2026-09-09 | Missing authorization in the Address Delete controller in Mageplaza GDPR for Magento 2 (mageplaza/module-gdpr) through 4 |
| CVE-2026-87911 | 9.6 | 2026-09-09 | An OS command injection weakness in the read-only enforcement of the SQL validation component in Amazon awslabs postgres |
| CVE-2026-87011 | 7.5 | 2026-09-09 | Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform. From 0.9.0 until 0.11.1, the unaut |
| CVE-2026-15913 | 7.7 | 2026-09-09 | In versions prior to 7.10.2 a path traversal vulnerability in the /attachRemoteFiles endpoint of Fortra's GoAnywhere MFT |
| CVE-2026-87016 | 8.1 | 2026-09-09 | Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform. From 0.6.41 until 0.11.1, get_user |
| CVE-2026-87921 | 7.3 | 2026-09-09 | A vulnerability was identified in Rizwan17 inventory-management-system up to bfe78a330d01bb26b9daec5dc9ecd5c77900e03f. A |
| CVE-2026-87922 | 7.3 | 2026-09-09 | A security flaw has been discovered in Rizwan17 inventory-management-system up to bfe78a330d01bb26b9daec5dc9ecd5c77900e0 |
| CVE-2026-87995 | 8.7 | 2026-09-09 | Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform. From 0.8.11 until 0.11.1, src/lib/ |
| CVE-2026-87996 | 7.7 | 2026-09-09 | Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform. From 0.9.6 until 0.11.1, SafePlayw |
| CVE-2026-87998 | 7.1 | 2026-09-09 | Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform. From 0.10.0 until 0.11.1, DELETE / |
| CVE-2026-87999 | 7.1 | 2026-09-09 | Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform. Prior to 0.11.1, POST /api/v1/retr |
| CVE-2026-87925 | 7.3 | 2026-09-10 | A vulnerability was detected in Rizwan17 inventory-management-system up to bfe78a330d01bb26b9daec5dc9ecd5c77900e03f. Thi |
| CVE-2026-87931 | 9.6 | 2026-09-10 | A vulnerability has been found in Behavioral Technology Group Pavlok Behavioral Conditioning Wearable up to 20260707. Im |
| CVE-2026-87933 | 7.3 | 2026-09-10 | A vulnerability was found in DaveGamble cJSON up to 1.7.19. The affected element is the function cJSONUtils_MergePatch o |
| CVE-2026-18351 | 9.8 | 2026-09-10 | The Drag and Drop File Upload for Elementor Forms plugin for WordPress is vulnerable to Arbitrary File Upload in all ver |
| CVE-2026-19583 | 9.9 | 2026-09-10 | Velociraptor allows some sensitive artifacts to be gated by additional permissions. For example, the Linux.Sys.BashShell |
| CVE-2026-19584 | 7.7 | 2026-09-10 | Velociraptor allows for the creation of notebook backups in its default enabled daily backup feature. When Velociraptor  |
| CVE-2026-14873 | 8.0 | 2026-09-10 | The Bulk Password Reset plugin for WordPress is vulnerable to privilege escalation via account takeover in all versions  |
| CVE-2026-15019 | 7.5 | 2026-09-10 | The Direct Download for WooCommerce plugin for WordPress is vulnerable to Directory Traversal in all versions up to, and |
| CVE-2026-76562 | 7.2 | 2026-09-10 | The Sidebar Manager Light plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'sbm_description' pa |
| CVE-2026-7188 | 9.8 | 2026-09-10 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Armiya Information |
| CVE-2026-42804 | 7.6 | 2026-09-10 | A stack-based buffer overflow vulnerability exists in the Bosch Sensortec BHI360 SensorAPI(C-Library) in versions up to  |
| CVE-2026-42805 | 8.4 | 2026-09-10 | A stack-based buffer overflow vulnerability exists in the Bosch Sensortec BHI385 SensorAPI (C library) within the debug  |
| CVE-2026-42807 | 8.0 | 2026-09-10 | A heap-based buffer overflow vulnerability in the PC bridge protocol decoder of BoschSensortec COINES_SDK (versions 2.10 |
| CVE-2026-44950 | 9.0 | 2026-09-10 | fs_read_glyphs() in the libXfont2 font-server client (src/fc/fserve.c) copies each glyph's bitmap into a single buffer.  |
| CVE-2026-59679 | 9.0 | 2026-09-10 | fs_read_glyphs() in the libXfont2 font-server client (src/fc/fserve.c) indexes the per-character encoding[] array using  |
| CVE-2026-84042 | 7.8 | 2026-09-10 | A flaw was found in crun. When crun is built with libkrun and a container is started rootful with passt networking (krun |
| CVE-2026-88271 | 8.8 | 2026-09-10 | GeoVision GV-LPC2211 V1.13 allows a Guest user to overwrite device configuration and replace the administrator password  |
| CVE-2026-88272 | 7.2 | 2026-09-10 | GeoVision GV-LPC2211 V1.13 allows an administrator-controlled username containing shell metacharacters to be executed as |
| CVE-2026-88273 | 7.2 | 2026-09-10 | GeoVision GV-LPC2211 V1.13 allows an administrator-controlled PPPoE username to escape a sourced shell configuration ass |
| CVE-2026-88274 | 7.2 | 2026-09-10 | GeoVision GV-LPC2211 V1.13 allows an administrator-controlled wireless SSID containing shell syntax to execute arbitrary |
| CVE-2026-88275 | 7.2 | 2026-09-10 | GeoVision GV-LPC2211 V1.13 allows an administrator-controlled WPA-PSK containing shell syntax to execute arbitrary comma |
| CVE-2026-88276 | 7.2 | 2026-09-10 | GeoVision GV-LPC2211 V1.13 allows administrator-controlled WEP key values containing shell syntax to execute arbitrary c |
| CVE-2026-88277 | 8.8 | 2026-09-10 | GeoVision GV-LPC2211 V1.13 allows an authenticated ONVIF user to inject shell commands through ConsumerReference.Address |
| CVE-2026-88278 | 9.8 | 2026-09-10 | GeoVision GV-LPC2211 V1.13 fails to enforce WS-Security UsernameToken freshness or nonce reuse protection, allowing a ca |
| CVE-2026-88282 | 7.2 | 2026-09-10 | GeoVision GV-LPC2211 V1.13 allows an administrator-controlled FTP username containing shell metacharacters to be execute |
| CVE-2026-88285 | 9.4 | 2026-09-10 | GeoVision GV-LPC2211 V1.13 exposes a network-accessible PTZ control service without authentication, allowing remote clie |
| CVE-2026-88286 | 7.5 | 2026-09-10 | GeoVision GV-LPC2211 V1.13 improperly manages PTZ connection state, allowing an unauthenticated remote client to block t |
| CVE-2026-88287 | 7.5 | 2026-09-10 | GeoVision GV-LPC2211 V1.13 fails to bound the number of Scopes tokens in unauthenticated ONVIF WS-Discovery Probe reques |
| CVE-2026-88289 | 7.5 | 2026-09-10 | GeoVision GV-LPC2211 V1.14 (260903) fails to validate attacker-controlled variable-length fields before copying them int |
| CVE-2026-88290 | 7.5 | 2026-09-10 | GeoVision GV-LPC2211 V1.14 (260903) allows unauthenticated clients to declare unbounded VLSVR frame lengths and indefini |
| CVE-2026-8323 | 9.3 | 2026-09-10 | URL redirection to untrusted site ('open redirect') vulnerability in Armiya Information Technologies Ltd. Co. Access Con |
| CVE-2026-87803 | 7.1 | 2026-09-10 | An authorization bypass vulnerability exists in the Countly Server DBViewer due to flawed sub-pipeline detection in the  |
| CVE-2026-87961 | 7.1 | 2026-09-10 | ESP32-audioI2S versions 3.4.4 through 4.0.0 contain a heap-based out-of-bounds read vulnerability in the read_ID3_Header |
| CVE-2026-87962 | 7.5 | 2026-09-10 | t-digest versions 3.1 through 3.3 contain a denial of service vulnerability in MergingDigest.fromBytes that fails to val |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-19490 | Citrix / NetScaler | 2026-09-09 | 2026-09-12 | Unknown |
| CVE-2025-25249 | Fortinet / Multiple Products | 2026-09-09 | 2026-09-12 | Unknown |
| CVE-2026-87491 | Google / Chromium V8 | 2026-09-09 | 2026-09-23 | Unknown |
| CVE-2026-20079 | Cisco / Secure Firewall Management Center (FMC) and Security Cloud Control (SCC) Firewall Management | 2026-09-09 | 2026-09-12 | Unknown |
| CVE-2026-75650 | Adobe / Commerce and Magento | 2026-09-08 | 2026-09-11 | Unknown |
| CVE-2026-81963 | Microsoft / Windows | 2026-09-08 | 2026-09-22 | Unknown |
| CVE-2026-86218 | N-able / N-central | 2026-09-08 | 2026-09-11 | Unknown |
| CVE-2026-85880 | Microsoft / Windows | 2026-09-08 | 2026-09-22 | Unknown |
| CVE-2026-85046 | Google / Chromium V8 | 2026-09-04 | 2026-09-18 | Unknown |

---

*Total entries in CISA KEV catalog: 1703*