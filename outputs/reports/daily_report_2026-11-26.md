# Vulnerability Intelligence Report

**Date:** 2026-11-26  
**Generated:** 2026-11-26T18:07:52Z  

---

## Executive Summary

Our environment faces significant exposure across 234 high-severity vulnerabilities, including two critical-rated CVEs scoring 9.8 and 9.1. Key risks include unsafe code evaluation in CodeSafe, authentication bypass in SeaweedFS SFTP, insecure deserialization in Camunda, and multiple MongoDB driver flaws affecting data integrity and confidentiality. CISA added 19 new exploited vulnerabilities to its KEV catalog this week, signaling an active threat landscape. While none of our monitored CVEs currently appear in KEV, the severity and exploitability of identified issues demand immediate remediation attention to protect critical business data and infrastructure.

---

## Risk Narrative

Threat actors are actively exploiting vulnerabilities across enterprise infrastructure, as evidenced by 19 new CISA KEV additions in seven days. Critical vulnerabilities in widely used components—including MongoDB drivers, distributed storage systems, and workflow automation platforms—expose the organization to data exfiltration, authentication bypass, and remote code execution. The presence of a CVSS 9.8 arbitrary code execution flaw and a CVSS 9.1 authentication bypass represents existential risk to data confidentiality and system integrity. Industrial control system vulnerabilities in Danfoss hardware further signal adversary interest in operational technology targets. Without rapid remediation, the organization faces heightened risk of ransomware deployment, data breach, and regulatory liability.

---

## Prioritized Action Items

1. Immediately patch or isolate systems running CodeSafe (CVE-2026-133467, CVSS 9.8) due to critical remote code execution risk via unsafe AST evaluation.
2. Remediate the SeaweedFS SFTP zero-length password bypass (CVE-2026-133464, CVSS 9.1) to prevent unauthorized access to distributed file storage.
3. Apply vendor patches for Camunda insecure deserialization (CVE-2026-77230, CVSS 8.1) to eliminate workflow platform compromise risk.
4. Update all MongoDB Python Driver and Mongoid dependencies to address authentication, TLS, and out-of-bounds read vulnerabilities (CVE-2026-135141, CVE-2026-135146, CVE-2026-135898).
5. Monitor and assess exposure to the 19 newly added CISA KEV entries, prioritizing Juniper Session Smart and Danfoss AK-SM 800A Series devices for urgent patching.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-135141 | 8.1 | 2026-11-25 | A logic flaw in the query-building layer of the Mongoid object-document mapper causes a model-level default restriction  |
| CVE-2026-135146 | 7.4 | 2026-11-25 | An improper certificate revocation check in the MongoDB Python Driver's optional TLS revocation-checking support allows  |
| CVE-2026-135226 | 7.5 | 2026-11-25 | A type-confusion weakness in the Extended JSON parsing component of BSON for Ruby allows a party who can supply parser i |
| CVE-2026-135227 | 8.2 | 2026-11-25 | An improper restriction of dynamically determined object attributes in the object-document mapping library's association |
| CVE-2026-135898 | 8.2 | 2026-11-25 | An out-of-bounds read in the native C BSON decoding extension of the MongoDB Python Driver may allow an unauthenticated  |
| CVE-2026-136722 | 7.3 | 2026-11-25 | A vulnerability was identified in Zhengzhou Weiwei Information Technology mayicms up to 5.8E. This vulnerability affects |
| CVE-2026-133464 | 9.1 | 2026-11-25 | SeaweedFS is a distributed storage system for files and blobs. Prior to version 4.46, FileStore.ValidatePassword in the  |
| CVE-2026-77230 | 8.1 | 2026-11-25 | Camunda 8.8.0 before 8.8.47, 8.9.0 before 8.9.29, 8.10.0 before 8.10.10, and 8.11.0-alpha1 contain an insecure deseriali |
| CVE-2026-133466 | 7.1 | 2026-11-25 | OpenEXR is the reference implementation and specification for the EXR image format, widely used in the motion picture in |
| CVE-2026-133467 | 9.8 | 2026-11-25 | CodeSafe is an open-source Python library for code encryption, decryption, and safe evaluation using Python's AST module |
| CVE-2026-134070 | 8.0 | 2026-11-25 | Improper input validation in the AWS-managed AWS Systems Manager Automation runbook AWSConfigRemediation-EnableSystemsMa |
| CVE-2026-136733 | 7.3 | 2026-11-25 | A weakness has been identified in EduardoPires EquinoxProject up to 1.10. This vulnerability affects the function BuildT |
| CVE-2026-137056 | 8.8 | 2026-11-25 | DeepSeek-Reasonix before 2.53.0 contains a command execution vulnerability that allows attackers to run commands without |
| CVE-2026-137057 | 7.5 | 2026-11-25 | llama.cpp from b7118 before b12604 contains an integer underflow vulnerability in llama_grammar_parser::parse_sequence() |
| CVE-2026-137058 | 7.5 | 2026-11-25 | Cron-parser through 5.10.0 contains an unbounded memory allocation vulnerability in CronExpressionParser.parse() that al |
| CVE-2026-137060 | 7.8 | 2026-11-25 | paramz through 0.10.0 contains an insecure deserialization vulnerability that allows attackers to execute code by supply |
| CVE-2026-137077 | 7.4 | 2026-11-25 | FreeRDP before 3.33.0 contains a heap out-of-bounds write in h264_context_reset() in libfreerdp/codec/h264.c, which stor |
| CVE-2026-137086 | 8.1 | 2026-11-25 | Teracom TCW122B-CM firmware before 4.07 contains a predictable session cookie vulnerability that allows unauthenticated  |
| CVE-2026-137087 | 7.3 | 2026-11-25 | @irrelon/path 6.2.2 before 7.0.3 contains a prototype pollution vulnerability in merge() and mergeImmutable() that allow |
| CVE-2026-137088 | 7.3 | 2026-11-25 | @oleksii-pavlov/deep-merge before 1.2.4 contains a prototype pollution vulnerability in deepMergeTwoAssignable() that al |
| CVE-2026-137089 | 7.3 | 2026-11-25 | merge-deep-composed through 0.1.4 contains a prototype pollution vulnerability in _mergeDeepOne() that allows remote att |
| CVE-2026-137090 | 9.8 | 2026-11-25 | build-git-clone before 1.0.4 contains an OS command injection vulnerability in the clone() function that allows attacker |
| CVE-2026-137091 | 7.1 | 2026-11-25 | EverOS before 1.8.0 contains a cross-origin local file disclosure vulnerability that allows malicious websites to read l |
| CVE-2026-137092 | 7.0 | 2026-11-25 | Assimp before 6.0.6 contains an out-of-bounds write vulnerability in MD5Importer::MakeDataUnique() that allows attackers |
| CVE-2026-137093 | 7.8 | 2026-11-25 | Assimp before 6.0.6 contains an out-of-bounds write vulnerability in MD5Importer::LoadMD5MeshFile() that allows attacker |
| CVE-2026-102957 | 7.7 | 2026-11-25 | z_impl_pwm_capture_cycles() in drivers/pwm/pwm_capture.c stores its capture context (struct z_pwm_capture_cb_data, inclu |
| CVE-2026-131814 | 7.8 | 2026-11-25 | ChargePoint Home Flex dwnldlogsm tar Command Injection Local Privilege Escalation Vulnerability. This vulnerability allo |
| CVE-2026-131815 | 7.8 | 2026-11-25 | ChargePoint Home Flex uploadsm filetype Link Following Local Privilege Escalation Vulnerability. This vulnerability allo |
| CVE-2026-131817 | 8.8 | 2026-11-25 | ChargePoint Home Flex wpa_passphrase Command Injection Remote Code Execution Vulnerability. This vulnerability allows ne |
| CVE-2026-131818 | 7.8 | 2026-11-25 | ChargePoint Home Flex busybox Unnecessary Privileges Local Privilege Escalation Vulnerability. This vulnerability allows |
| CVE-2026-131827 | 7.8 | 2026-11-25 | RustDesk Client for Windows reg_recovery Missing Authorization Local Privilege Escalation Vulnerability. This vulnerabil |
| CVE-2026-136821 | 9.9 | 2026-11-25 | A flaw has been found in D-Link R32 1.10B02. The affected element is the function SetTimeSettings of the component DHMAP |
| CVE-2026-136822 | 9.9 | 2026-11-25 | A vulnerability has been found in D-Link R32 1.10B02. The impacted element is the function SetDeviceSettings of the file |
| CVE-2026-67209 | 7.1 | 2026-11-25 | metasfresh through 5.175 contains a SQL injection vulnerability in the stressTest_massCacheInvalidation handler of Debug |
| CVE-2026-116681 | 7.5 | 2026-11-25 | NocoDB is software for building databases as spreadsheets. Prior to 2026.08.0, the row-scoped endpoints of a public shar |
| CVE-2026-136823 | 10.0 | 2026-11-25 | A vulnerability was found in D-Link R32 1.10B02. This affects an unknown function of the file /usr/bin/httpd of the comp |
| CVE-2026-66052 | 8.8 | 2026-11-25 | Comviva Revenue Plus (MobiLytix Customer Value Management) 3.0.0 contains an expression language injection vulnerability |
| CVE-2026-69695 | 8.8 | 2026-11-25 | Handesk through 1.5 contains an unrestricted file upload vulnerability in Attachment::storeAttachmentFromRequest() that  |
| CVE-2026-133971 | 9.8 | 2026-11-25 | An authentication bypass vulnerability exists in the web management interface of HPE Networking Management Software (Air |
| CVE-2026-133972 | 9.8 | 2026-11-25 | A vulnerability in system functionality could allow an attacker with network access to bypass authentication. Successful |
| CVE-2026-133973 | 9.8 | 2026-11-25 | A command injection vulnerability exists in the web-based management interface of HPE Networking Management Software (Ai |
| CVE-2026-133974 | 8.8 | 2026-11-25 | A vulnerability in a system functionality could allow a low-privilege authenticated attacker with network access to pote |
| CVE-2026-133975 | 8.8 | 2026-11-25 | Authenticated SQL injection vulnerabilities in the web-based management interface and API of HPE Networking Management S |
| CVE-2026-133976 | 8.8 | 2026-11-25 | A missing integrity verification vulnerability exists in HPE Networking Management Software (Airwave). Successful exploi |
| CVE-2026-133977 | 7.5 | 2026-11-25 | A sensitive information disclosure vulnerability exists in the affected interface of HPE Networking Management Software  |
| CVE-2026-133978 | 7.5 | 2026-11-25 | A command injection vulnerability exists in the web-based management interface of HPE Networking Management Software (Ai |
| CVE-2026-133979 | 7.4 | 2026-11-25 | Improper certificate validation vulnerabilities in the web-based management interface of HPE Networking Management Softw |
| CVE-2026-136500 | 8.1 | 2026-11-25 | To escape a bound parameter, or a name passed to a catalog function, psqlODBC has to know where each multibyte character |
| CVE-2026-136501 | 7.1 | 2026-11-25 | To build positioned updates and to describe columns, psqlODBC matches the names in a statement against the catalog. Wher |
| CVE-2026-136502 | 8.1 | 2026-11-25 | psqlODBC scans statement text itself to substitute parameters, translate ODBC escapes, join batched statements and rewri |
| CVE-2026-136503 | 7.5 | 2026-11-25 | psqlODBC frees memory that is still in use, frees it twice, or writes outside an application buffer in these cases:

- T |
| CVE-2026-136505 | 7.5 | 2026-11-25 | psqlODBC uses sizes and counts without checking their range, or keeps them in types too small for them:

- A row array s |
| CVE-2026-136506 | 7.5 | 2026-11-25 | psqlODBC builds queries of its own from names, and put these names into them without escaping or qualification:

- the d |
| CVE-2026-136507 | 8.1 | 2026-11-25 | psqlODBC parsed and built connection strings in ways that let a value end early:

- In a braced value, such as PWD={…},  |
| CVE-2026-136509 | 7.5 | 2026-11-25 | psqlODBC did not check that a server reply matches the query it sent: that a FETCH returns no more rows than it asked fo |
| CVE-2026-136512 | 7.5 | 2026-11-25 | With SQL_C_DEFAULT, the C type of a bound column or parameter follows its SQL type. An application sizes its buffer from |
| CVE-2026-136515 | 7.5 | 2026-11-25 | psqlODBC rewrites statement text for keyset-driven cursors and ODBC escapes using positions it found in the text. These  |
| CVE-2026-136946 | 7.3 | 2026-11-26 | A vulnerability was identified in philipjscott simple-thumbnail up to 1.6.5. This issue affects the function ffmpegExecu |
| CVE-2026-66784 | 8.7 | 2026-11-26 | A flaw was found in Submariner. In its default Pre-Shared Key (PSK) mode, all gateways within a broker set utilize the s |
| CVE-2026-115576 | 8.8 | 2026-11-26 | NetBird is a zero-trust networking platform that connects people, machines, and AI agents across any network. From versi |
| CVE-2026-136947 | 7.3 | 2026-11-26 | A security flaw has been discovered in msaifulcsse Ticket-Travel-Management-System 28b68cea41b3a9eb8d533db992e0b5ba2db68 |
| CVE-2026-137305 | 8.8 | 2026-11-26 | Grav Form plugin before 9.2.4 contains a code injection vulnerability that allows page authors to write uploads into Twi |
| CVE-2026-137308 | 7.4 | 2026-11-26 | markdownify-mcp before 1.2.0 contains a server-side request forgery vulnerability that allows attackers to bypass URL va |
| CVE-2026-123679 | 7.3 | 2026-11-26 | An improper access control vulnerability exists in a privileged Unix domain socket of StellarProtect Linux and Stellar A |
| CVE-2026-123680 | 7.2 | 2026-11-26 | An authenticated remote code execution vulnerability exists in the firmware update functionality of StellarOne. An attac |
| CVE-2026-123682 | 7.2 | 2026-11-26 | An authenticated remote code execution vulnerability exists in the update functionality of StellarOne due to insufficien |
| CVE-2026-123685 | 8.8 | 2026-11-26 | A remote code execution vulnerability exists in the patch apply functionality of StellarProtect Linux and Stellar Agent  |
| CVE-2026-123687 | 7.2 | 2026-11-26 | An arbitrary file write vulnerability exists in the patch upload functionality of StellarOne due to improper validation  |
| CVE-2026-137043 | 10.0 | 2026-11-26 | A security vulnerability has been detected in TOTOLINK N350RT 9.3.5u.6468_B20250827/9.3.5u.6466_B20250825. The affected  |
| CVE-2026-137046 | 7.3 | 2026-11-26 | A vulnerability was detected in mahmoudai1 school-management-system up to ecec9faaf2fb1a3c5cd096e063f8ef326d09cdfd. The  |
| CVE-2026-137326 | 7.0 | 2026-11-26 | ICU4C through 79.1 contains a use-after-free and double free vulnerability in the x11-compound-text converter because cl |
| CVE-2026-123689 | 8.1 | 2026-11-26 | A SQL injection vulnerability exists in the Search Agents API of StellarOne due to improper sanitization of user-supplie |
| CVE-2026-133525 | 8.8 | 2026-11-26 | Deserialization of Untrusted Data vulnerability in ThemeFusion Fusion Builder fusion-builder allows Object Injection.Thi |
| CVE-2026-135772 | 7.6 | 2026-11-26 | RTL8762C MCU developed by Realtek Semiconductor Corporation has an Improper Protection Against Voltage and Clock Glitche |
| CVE-2026-137324 | 7.3 | 2026-11-26 | A flaw has been found in shemaikuzwe Attendance_Management_system up to b37dbeb5bf4d9eab07480e7b6213db889fc3ebf9. Affect |
| CVE-2026-137389 | 8.8 | 2026-11-26 | MailGates/MailAudit developed by Openfind has a Command Injection vulnerability.Authenticated remote attackers can injec |
| CVE-2026-137390 | 8.8 | 2026-11-26 | Mail2000 developed by Openfind has an OS Command Injection vulnerability.Authenticated remote attackers can inject arbit |
| CVE-2026-124211 | 7.5 | 2026-11-26 | The Ninja Tables – Responsive Table Builder for Data, Pricing & Product Tables plugin for WordPress is vulnerable to SQL |
| CVE-2026-130805 | 8.1 | 2026-11-26 | The Groundhogg plugin for WordPress is vulnerable to Cross-Site Request Forgery in versions up to, and including, 4.11 T |
| CVE-2026-131589 | 7.2 | 2026-11-26 | The AI Engine – MCP Server & AI Chatbot for WordPress, with Claude, ChatGPT & Gemini plugin for WordPress is vulnerable  |
| CVE-2026-135151 | 7.5 | 2026-11-26 | The Download Manager plugin for WordPress is vulnerable to Local File Inclusion in all versions up to, and including, 3. |
| CVE-2026-135266 | 7.5 | 2026-11-26 | The Music Player for WooCommerce plugin for WordPress is vulnerable to Directory Traversal in all versions up to, and in |
| CVE-2026-123903 | 9.8 | 2026-11-26 | VMware vCenter contains an authentication bypass vulnerability in the VMware Directory Service. Broadcom has evaluated t |
| CVE-2026-123904 | 7.5 | 2026-11-26 | VMware vCenter contains an arbitrary file write vulnerability while processing certain archives. Broadcom has evaluated  |
| CVE-2026-123905 | 7.5 | 2026-11-26 | VMware vCenter contains multiple denial-of-service vulnerabilities in the VMware Directory Service. Broadcom has evaluat |
| CVE-2026-123906 | 7.5 | 2026-11-26 | VMware vCenter contains multiple denial-of-service vulnerabilities in the VMware Directory Service. Broadcom has evaluat |
| CVE-2026-123907 | 7.5 | 2026-11-26 | VMware vCenter contains multiple denial-of-service vulnerabilities in the VMware Directory Service. Broadcom has evaluat |
| CVE-2026-123910 | 9.8 | 2026-11-26 | ESX contains a heap out-of-bounds write vulnerability in the I/O filter service. Broadcom has evaluated the severity of  |
| CVE-2026-123911 | 9.8 | 2026-11-26 | ESX contains a use-after-free vulnerability in the I/O filter service. Broadcom has evaluated the severity of this issue |
| CVE-2026-123912 | 9.3 | 2026-11-26 | VMware ESXi, Workstation, and Fusion contain an out-of-bounds write vulnerability in the XHCI USB controller. Broadcom h |
| CVE-2026-123913 | 8.2 | 2026-11-26 | VMware ESX contains a stack-based buffer-overflow vulnerability in the VMkernel. Broadcom has evaluated the severity of  |
| CVE-2026-128111 | 7.2 | 2026-11-26 | The Drag and Drop Multiple File Upload for Contact Form 7 plugin for WordPress is vulnerable to Stored Cross-Site Script |
| CVE-2026-131613 | 7.2 | 2026-11-26 | The Classified Listing – AI-Powered Business Directory & Classified Ads plugin for WordPress is vulnerable to Stored Cro |
| CVE-2026-131688 | 8.1 | 2026-11-26 | The Secure MCP Server for Claude, ChatGPT, Gemini, Cursor and other AI Agents plugin for WordPress is vulnerable to auth |
| CVE-2026-131806 | 7.2 | 2026-11-26 | The CubeWP Forms plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'cwp_custom_form[form_data_id |
| CVE-2026-135655 | 7.2 | 2026-11-26 | The Easy SwipeBox plugin for WordPress is vulnerable to Stored DOM-Based Cross-Site Scripting via the 'title attribute o |
| CVE-2026-136519 | 7.2 | 2026-11-26 | The Advanced Product Fields (Product Addons) for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scr |
| CVE-2026-110702 | 7.2 | 2026-11-26 | The EWWW Image Optimizer plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'comment' parameter i |
| CVE-2026-111846 | 7.2 | 2026-11-26 | Missing Authorization vulnerability in WPExperts NOWPayments for WooCommerce nowpayments-for-woocommerce allows Exploiti |
| CVE-2026-124266 | 8.8 | 2026-11-26 | Deserialization of Untrusted Data vulnerability in Arraytics WP Event Solution wp-event-solution allows Object Injection |
| CVE-2026-124756 | 7.5 | 2026-11-26 | Allocation of Resources Without Limits or Throttling vulnerability in Takashi Kitajima MW WP Form mw-wp-form allows HTTP |
| CVE-2026-127113 | 7.2 | 2026-11-26 | The GeoDirectory – WP Business Directory Plugin and Classified Listings Directory plugin for WordPress is vulnerable to  |
| CVE-2026-128097 | 7.2 | 2026-11-26 | The Lazy Loader plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'author' parameter in all vers |
| CVE-2026-129028 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Datasolution Colis |
| CVE-2026-129329 | 7.2 | 2026-11-26 | The Ocean Extra plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'post_title' parameter in all  |
| CVE-2026-131758 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Brainstorm Force S |
| CVE-2026-131767 | 9.8 | 2026-11-26 | Deserialization of Untrusted Data vulnerability in Aman FunnelKit Automations wp-marketing-automations allows Object Inj |
| CVE-2026-131838 | 7.2 | 2026-11-26 | The MoreConvert Wishlist for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'attr |
| CVE-2026-133409 | 7.2 | 2026-11-26 | The Parsigate plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'trackId (Zibal). Equivalent una |
| CVE-2026-133524 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in lyrathemes Kale ka |
| CVE-2026-133698 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WPVibes AnyWhere E |
| CVE-2026-133986 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in MotoPress Getwid g |
| CVE-2026-134469 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Sayontan Sinha Pho |
| CVE-2026-134479 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Ultimate Member Ul |
| CVE-2026-134481 | 9.8 | 2026-11-26 | Deserialization of Untrusted Data vulnerability in Ultimate Member Ultimate Member ultimate-member allows Object Injecti |
| CVE-2026-134486 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in eMarket Design You |
| CVE-2026-134490 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Imran Tauqeer Cube |
| CVE-2026-134491 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Dimitri Grassi Sal |
| CVE-2026-134719 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Johann Heyne Table |
| CVE-2026-134872 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Seraphinite Soluti |
| CVE-2026-134958 | 7.5 | 2026-11-26 | Insertion of Sensitive Information into Externally-Accessible File or Directory vulnerability in Webdeclic WPMasterToolK |
| CVE-2026-134988 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Nks video carousel |
| CVE-2026-135630 | 7.2 | 2026-11-26 | The Premmerce Brands for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'product_ |
| CVE-2026-135666 | 7.2 | 2026-11-26 | The JetFormBuilder — Dynamic Blocks Form Builder plugin for WordPress is vulnerable to Stored DOM-Based Cross-Site Scrip |
| CVE-2026-135669 | 7.2 | 2026-11-26 | The Everest Forms – Contact Form, Payment Form, Quiz, Survey & Custom Form Builder with AI plugin for WordPress is vulne |
| CVE-2026-135808 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in dudaster ECS – Ele |
| CVE-2026-136221 | 7.2 | 2026-11-26 | The Strong Testimonials plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'custom textarea field |
| CVE-2026-136459 | 7.2 | 2026-11-26 | The Nexter Extension – Security, Performance, Code Snippets & Site Toolkit plugin for WordPress is vulnerable to Stored  |
| CVE-2026-137284 | 7.2 | 2026-11-26 | The JetFormBuilder — Dynamic Blocks Form Builder plugin for WordPress is vulnerable to Stored Cross-Site Scripting via t |
| CVE-2026-129071 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in RomanCode MapSVG m |
| CVE-2026-131590 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in hupe13 Extension f |
| CVE-2026-134474 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in OptiUser Opti-Beha |
| CVE-2026-134711 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Webilia Inc. Listd |
| CVE-2026-135005 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Greg – SiteOrigin  |
| CVE-2026-137403 | 7.3 | 2026-11-26 | A vulnerability was determined in SourceCodester Online Food Ordering System 1.0. This affects an unknown function of th |
| CVE-2026-137566 | 8.8 | 2026-11-26 | Argo Workflows 3.0.0 through 3.7.18, 4.0.0 before 4.0.12, and 4.1.0 before 4.1.4 contains a path traversal vulnerability |
| CVE-2026-137567 | 9.8 | 2026-11-26 | llama.cpp b11450 before b12658 contains an out-of-bounds write vulnerability in the ggml RPC server that allows unauthen |
| CVE-2026-137577 | 8.1 | 2026-11-26 | Iceburg CRM through 5.0.0 contains an authorization bypass vulnerability that allows authenticated low-privileged users  |
| CVE-2026-137584 | 7.4 | 2026-11-26 | Twenty through 2.63.0 in multi-workspace mode contains an authentication bypass vulnerability that allows unauthenticate |
| CVE-2026-137585 | 7.5 | 2026-11-26 | Bazarr 1.4.4 before 1.6.1-beta.29 on Windows contains an unauthenticated path traversal vulnerability in the catch_all() |
| CVE-2026-137586 | 7.5 | 2026-11-26 | LibreChat 0.7.3 before 0.8.9 contains an improper input type validation vulnerability in the requireLdapAuth middleware  |
| CVE-2026-137587 | 7.1 | 2026-11-26 | LIVE555 Streaming Media before 2026.08.25 contains a heap out-of-bounds read vulnerability in parseVorbisOrTheoraConfigS |
| CVE-2026-104998 | 9.8 | 2026-11-26 | The Product Input Fields for WooCommerce plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up  |
| CVE-2026-123827 | 7.2 | 2026-11-26 | The Easy Social Share Buttons for WordPress plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'p |
| CVE-2026-125001 | 7.2 | 2026-11-26 | The NextMove Lite – Thank You Page for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via |
| CVE-2026-126089 | 7.5 | 2026-11-26 | The Drag and Drop Multiple File Upload (Pro) - WooCommerce plugin for WordPress is vulnerable to generic SQL Injection v |
| CVE-2026-130321 | 7.2 | 2026-11-26 | The PDF Invoices & Packing Slips for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via t |
| CVE-2026-130331 | 7.5 | 2026-11-26 | The WP Statistics – Simple, privacy-friendly Google Analytics alternative plugin for WordPress is vulnerable to Local Fi |
| CVE-2026-133951 | 9.1 | 2026-11-26 | The Simple Membership plugin for WordPress is vulnerable to Privilege Escalation in versions up to, and including, 4.8.9 |
| CVE-2026-134173 | 9.1 | 2026-11-26 | The WordPress File Upload plugin for WordPress is vulnerable to Arbitrary File Deletion in versions up to, and including |
| CVE-2026-135035 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WPtouch WPtouch wp |
| CVE-2026-135641 | 9.1 | 2026-11-26 | The WP Job Portal – AI-Powered Recruitment System for Company or Job Board website plugin for WordPress is vulnerable to |
| CVE-2026-135654 | 7.2 | 2026-11-26 | The Lightbox with PhotoSwipe plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'comment' paramet |
| CVE-2026-135675 | 7.2 | 2026-11-26 | The RSS Aggregator by Feedzy – Feed to Post, Autoblogging, News & YouTube Video Feeds Aggregator plugin for WordPress is |
| CVE-2026-136240 | 9.1 | 2026-11-26 | The PDF Invoice for WooCommerce + Drag and Drop Template Builder plugin for WordPress is vulnerable to PHP Object Inject |
| CVE-2026-136488 | 7.5 | 2026-11-26 | The GeoDirectory – WP Business Directory Plugin and Classified Listings Directory plugin for WordPress is vulnerable to  |
| CVE-2026-136610 | 7.2 | 2026-11-26 | The Pixeline’s Email Protector plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'comment' param |
| CVE-2026-137122 | 7.2 | 2026-11-26 | The PDF Invoices & Packing Slips for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via t |
| CVE-2026-93087 | 8.2 | 2026-11-26 | A maliciously modified field in the locally stored JSON description for an update made available by Autodesk, when proce |
| CVE-2026-95810 | 7.2 | 2026-11-26 | The Easy Form Builder by WhiteStudio – Drag & Drop Form Builder plugin for WordPress is vulnerable to Stored Cross-Site  |
| CVE-2026-103886 | 8.1 | 2026-11-26 | The App Builder – Create Native Android & iOS Apps On The Flight plugin for WordPress is vulnerable to Authentication By |
| CVE-2026-109586 | 7.5 | 2026-11-26 | The WP STAGING – Backups & Restore, Migration & Clone Plugin – Cloud Backups, Scheduled Backups plugin for WordPress is  |
| CVE-2026-109921 | 8.8 | 2026-11-26 | Authentication bypass in the system.setPillar and system.getPillar functions in Uyuni before 5.1.35, 5.2.0 before 5.2.25 |
| CVE-2026-119153 | 7.2 | 2026-11-26 | The Swift Performance Lite plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'REQUEST_URI (gated |
| CVE-2026-119159 | 7.2 | 2026-11-26 | The Hide My WP Ghost – Security & Firewall plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'co |
| CVE-2026-122039 | 7.2 | 2026-11-26 | The User Registration & Membership – Free & Paid Memberships, Subscriptions, Content Restriction, User Profile, Custom U |
| CVE-2026-124072 | 7.2 | 2026-11-26 | The User Frontend – Membership, User Registration, User Profile, User Directory & Content Restriction with Frontend Post |
| CVE-2026-126342 | 7.2 | 2026-11-26 | The WPForms (Contact Form by WPForms / wpforms-lite) plugin for WordPress is vulnerable to Stored Cross-Site Scripting v |
| CVE-2026-126984 | 10.0 | 2026-11-26 | A **server-side request forgery** flaw has been found in the get_remote_artifact_url() function in pulp_python/app/model |
| CVE-2026-131803 | 7.2 | 2026-11-26 | The Mang Board plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'content' parameter in all vers |
| CVE-2026-137452 | 7.5 | 2026-11-26 | FreeRDP before 3.33.0 contains a race condition in asynchronous RDPDR IRP processing that allows malicious RDP servers t |
| CVE-2026-137455 | 7.5 | 2026-11-26 | The FreeRDP proxy in FreeRDP before 3.33.0 dereferences a NULL backend client context in pf_server_refresh_rect and pf_s |
| CVE-2026-137456 | 8.2 | 2026-11-26 | FreeRDP before 3.33.0 contains an integer overflow in the client GDI handling of accumulated drawing-order bounds: wrapp |
| CVE-2026-137457 | 7.5 | 2026-11-26 | FreeRDP from 3.0.0 before 3.33.0 contains a missing authentication vulnerability in the shadow server's fast-path input  |
| CVE-2026-137459 | 7.5 | 2026-11-26 | FreeRDP 2.11.2 before 3.33.0 contains unbounded resource consumption in the Progressive codec because progressive_decomp |
| CVE-2026-137460 | 7.5 | 2026-11-26 | FreeRDP from 3.10.0 before 3.33.0 contains an invalid free vulnerability in rdg.c because the websocket context pointer  |
| CVE-2026-137463 | 7.4 | 2026-11-26 | HKUDS nanobot from 0.1.4 before 0.4.1 contains an improper certificate validation vulnerability in the OpenAI Codex prov |
| CVE-2026-137465 | 7.4 | 2026-11-26 | Parse Server 3.10.0 before 8.6.123 and 9.0.0 before 9.11.1-alpha.4 contains an authentication bypass in the Google Play  |
| CVE-2026-137467 | 7.5 | 2026-11-26 | SiYuan before 3.8.11 uses DejaVu sync code that accepts a non-hexadecimal 40-byte remote index ID from WebDAV responses  |
| CVE-2026-137468 | 7.5 | 2026-11-26 | SiYuan from 3.8.0 before 3.8.11 contains a lockout bypass vulnerability that allows remote attackers to brute-force publ |
| CVE-2026-137469 | 7.5 | 2026-11-26 | SiYuan 3.7.0 before 3.8.11 contains a DOM-based cross-site scripting vulnerability in the AI agent chat panel, which ren |
| CVE-2026-137470 | 8.8 | 2026-11-26 | SiYuan before 3.8.11 contains a stored cross-site scripting vulnerability that allows attackers to inject DOM event hand |
| CVE-2026-137471 | 8.3 | 2026-11-26 | SiYuan before 3.8.10 contains a cross-site scripting vulnerability where WebDAV sync error formatting skips HTML escapin |
| CVE-2026-137474 | 7.1 | 2026-11-26 | SiYuan 3.8.8 before 3.8.10 contains an incorrect permission assignment vulnerability that creates workspace directories  |
| CVE-2026-137478 | 8.7 | 2026-11-26 | Traefik before 2.11.62, 3.x before 3.7.18, and 3.8.0-rc.1 contain an authentication bypass in the ForwardAuth middleware |
| CVE-2026-137479 | 7.5 | 2026-11-26 | Traefik 3.1.0 before 3.7.18 and 3.8.0-rc.1 contain a memory exhaustion vulnerability in the Compress middleware, which c |
| CVE-2026-137480 | 8.7 | 2026-11-26 | Traefik 3.7.15 before 3.7.18 and 3.8.0-rc.1 before 3.8.0-rc.2 contains a client certificate authentication bypass in the |
| CVE-2026-137481 | 9.3 | 2026-11-26 | Traefik before 2.11.62, 3.x before 3.7.18, and 3.8.0-rc.1 contain an authorization bypass because the sanitizePath entry |
| CVE-2026-137490 | 8.8 | 2026-11-26 | SurrealDB before 4.0.0 contains an authorization bypass vulnerability that allows restricted subjects to execute arbitra |
| CVE-2026-137491 | 8.1 | 2026-11-26 | Budibase before 4.0.0 contains a query injection vulnerability that allows low-privilege or anonymous users to inject AQ |
| CVE-2026-137492 | 8.8 | 2026-11-26 | Budibase before 4.0.0 contains an authorization bypass vulnerability that allows workspace-scoped builders to access oth |
| CVE-2026-137493 | 8.1 | 2026-11-26 | Budibase server from 3.0.0 before 4.0.0 contains an authorization bypass vulnerability that allows view users and anonym |
| CVE-2026-137494 | 9.9 | 2026-11-26 | Budibase before 4.0.0 contains a broken object-level authorization vulnerability that allows authenticated users with ta |
| CVE-2026-137495 | 7.1 | 2026-11-26 | Budibase before 4.0.0 contains an insecure direct object reference vulnerability in the bulkDestroy function that allows |
| CVE-2026-137496 | 7.6 | 2026-11-26 | Budibase before 4.0.0 contains a server-side template injection vulnerability that allows authenticated users with table |
| CVE-2026-137497 | 7.5 | 2026-11-26 | Budibase before 4.0.0 contains an information disclosure vulnerability that allows unauthenticated attackers to retrieve |
| CVE-2026-137498 | 10.0 | 2026-11-26 | Budibase Server from 3.39.18 before 4.0.0 contains a prototype pollution vulnerability that allows unauthenticated attac |
| CVE-2026-137499 | 9.8 | 2026-11-26 | Budibase from 3.41.0 before 4.0.0 contains an authentication bypass vulnerability that allows unauthenticated attackers  |
| CVE-2026-137500 | 7.2 | 2026-11-26 | Budibase before 4.0.0 contains a privilege escalation vulnerability that allows non-admin Creator or app-builder users t |
| CVE-2026-137503 | 8.1 | 2026-11-26 | Budibase before 4.0.0 contains a JSON injection vulnerability that allows attackers to inject JSON structure into S3 del |
| CVE-2026-137504 | 7.5 | 2026-11-26 | actix-multipart (actix-web) before 0.8.7 contains a resource exhaustion vulnerability in the MultipartForm extractor tha |
| CVE-2026-137508 | 7.5 | 2026-11-26 | Scriban before 7.6.0 contains a memory exhaustion vulnerability in object.to_json that allows template authors to bypass |
| CVE-2026-137509 | 7.5 | 2026-11-26 | Scriban before 7.6.0 contains a resource exhaustion vulnerability that allows template authors to bypass LimitToString b |
| CVE-2026-137510 | 7.5 | 2026-11-26 | Scriban and Scriban.Signed before 7.6.0 allow template authors to bypass the LimitToString string length limit because t |
| CVE-2026-137511 | 7.6 | 2026-11-26 | Scriban before 7.6.0 contains a state isolation vulnerability because TemplateContext.Reset() does not clear the Tags di |
| CVE-2026-137512 | 7.5 | 2026-11-26 | Scriban before 7.6.0 contains a resource exhaustion vulnerability that allows attackers to bypass LoopLimit by supplying |
| CVE-2026-137513 | 7.5 | 2026-11-26 | justhtml before 3.17.0 contains a denial of service vulnerability in decode_entities_in_text that allows unauthenticated |
| CVE-2026-137523 | 8.8 | 2026-11-26 | ToolJet before 3.21.96-LTS contains an authentication bypass in instance-level Google SSO because the id_token audience  |
| CVE-2026-137526 | 8.8 | 2026-11-26 | ToolJet before 3.21.96-LTS contains an authorization bypass in the internal database (TJDB) PostgREST proxy, which grant |
| CVE-2026-137536 | 9.8 | 2026-11-26 | ToolJet before 3.21.94-beta contains an authentication bypass in its server OAuth SSO sign-in module, which resolves Goo |
| CVE-2026-137537 | 7.1 | 2026-11-26 | ToolJet before 3.21.96-LTS contains a missing authorization vulnerability that allows authenticated End Users to execute |
| CVE-2026-137538 | 7.3 | 2026-11-26 | ToolJet before 3.21.96-LTS contains an insufficient session expiration vulnerability that allows attackers to reuse expi |
| CVE-2026-137542 | 7.7 | 2026-11-26 | LaraDashboard before 1.5.2 contains an information disclosure vulnerability in SettingObserver that writes full Setting  |
| CVE-2026-137543 | 7.7 | 2026-11-26 | LaraDashboard before 1.5.2 contains a server-side request forgery vulnerability that allows authenticated users to reach |
| CVE-2026-137544 | 9.1 | 2026-11-26 | LaraDashboard before 1.5.0 contains a path traversal vulnerability in module.json providers and composer.json psr-4 name |
| CVE-2026-137547 | 8.1 | 2026-11-26 | Coder before 2.29.27, 2.30.0 before 2.34.19, 2.35.0 before 2.37.11, 2.38.0 before 2.38.7, and 2.39.0 before 2.39.1 retur |
| CVE-2026-137549 | 7.5 | 2026-11-26 | pypdf before 7.0.1 contains a resource exhaustion vulnerability in image loading because data size estimates for some im |
| CVE-2026-137550 | 9.8 | 2026-11-26 | Frappe Framework before 15.122.0 and 16.x before 16.50.0 contains a missing authorization vulnerability in Document.upda |
| CVE-2026-137551 | 7.2 | 2026-11-26 | Frappe Framework before 15.121.2 and 16.x before 16.36.0 exposes functions imported into module-path-hooked modules as J |
| CVE-2026-137552 | 7.5 | 2026-11-26 | Frappe Framework before 15.121.1 and 16.x before 16.35.0 accepts an undocumented OAuth2 Resource Owner Password Credenti |
| CVE-2026-137556 | 8.8 | 2026-11-26 | Dockhand before 1.0.57 contains a path traversal vulnerability in validateStackPath, which omits the isProtectedPath() c |
| CVE-2026-76075 | 8.8 | 2026-11-26 | The Warehouse Cargo theme for WordPress is vulnerable to Arbitrary File Upload in versions up to, and including, 2.7.4 v |
| CVE-2026-85412 | 7.2 | 2026-11-26 | The Easy Form Builder by WhiteStudio – Drag & Drop Form Builder plugin for WordPress is vulnerable to Stored Cross-Site  |
| CVE-2026-85416 | 7.2 | 2026-11-26 | The Lenix Leads Collector plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Form Field Name in all v |
| CVE-2026-92251 | 7.5 | 2026-11-26 | The ZarinPal Payment Gateway for WooCommerce plugin for WordPress is vulnerable to Insecure Direct Object Reference in v |
| CVE-2026-97345 | 7.5 | 2026-11-26 | The SumUp Payment Gateway For WooCommerce plugin for WordPress is vulnerable to Insecure Direct Object Reference in vers |
| CVE-2026-135205 | 7.4 | 2026-11-26 | @fastify/middie is the plugin that adds Express-style middleware support to the Fastify web framework. In versions 9.3.6 |
| CVE-2026-135230 | 7.4 | 2026-11-26 | @fastify/express is the plugin that lets an application run Express middleware and Express applications inside the Fasti |
| CVE-2026-135264 | 7.4 | 2026-11-26 | @fastify/express is the plugin that lets an application run Express middleware and Express applications inside the Fasti |
| CVE-2026-135270 | 7.4 | 2026-11-26 | @fastify/express is the plugin that lets an application run Express middleware and Express applications inside the Fasti |
| CVE-2026-135279 | 9.1 | 2026-11-26 | @fastify/express is the plugin that lets an application run Express middleware and Express applications inside the Fasti |
| CVE-2026-135280 | 7.4 | 2026-11-26 | @fastify/express is the plugin that lets an application run Express middleware and Express applications inside the Fasti |
| CVE-2026-137409 | 7.3 | 2026-11-26 | A flaw has been found in chuckfairy node-webcam up to 0.8.2. This vulnerability affects the function generateSh of the f |
| CVE-2026-137411 | 7.3 | 2026-11-26 | A vulnerability was found in projectworlds Online Jewellery Shopping System 1.0. Impacted is the function searchItem of  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-103406 | Hewlett Packard Enterprise (HPE) / Juniper Session Smart Conductor and Session Smart Router | 2026-11-25 | 2026-11-28 | Unknown |
| CVE-2026-133469 | Vates / Xen Orchestra | 2026-11-25 | 2026-11-28 | Unknown |
| CVE-2025-41450 | Danfoss / AK-SM 800A Series | 2026-11-25 | 2026-12-09 | Unknown |
| CVE-2023-25914 | Danfoss / AK-SM 800A Series | 2026-11-25 | 2026-11-28 | Unknown |
| CVE-2023-25915 | Danfoss / AK-SM 800A Series | 2026-11-25 | 2026-11-28 | Unknown |
| CVE-2026-133324 | Mitel / MiCollab | 2026-11-25 | 2026-11-28 | Unknown |
| CVE-2026-133275 | Mitel / MiCollab | 2026-11-25 | 2026-11-28 | Unknown |
| CVE-2026-133311 | Mitel / MiCollab | 2026-11-25 | 2026-12-09 | Unknown |
| CVE-2026-133303 | Mitel / MiCollab | 2026-11-25 | 2026-11-28 | Unknown |
| CVE-2026-133323 | Mitel / MiCollab | 2026-11-25 | 2026-11-28 | Unknown |
| CVE-2026-132224 | Optimizely / Web Experimentation | 2026-11-24 | 2026-11-27 | Unknown |
| CVE-2026-131914 | Idunno / AntiCsrf | 2026-11-24 | 2026-11-27 | Unknown |
| CVE-2026-132165 | Drupal / Core | 2026-11-24 | 2026-11-27 | Unknown |
| CVE-2026-133968 | Project MONAI / MONAI Label | 2026-11-23 | 2026-11-26 | Unknown |
| CVE-2026-134624 | N-able / MailAssure | 2026-11-23 | 2026-11-26 | Unknown |
| CVE-2026-129448 | Apache / Roller | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2026-123890 | Broadcom / VMware vCenter | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2025-42884 | SAP / NetWeaver | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2026-76466 | Cisco / Expressway Series | 2026-11-20 | 2026-11-23 | Unknown |

---

*Total entries in CISA KEV catalog: 1805*