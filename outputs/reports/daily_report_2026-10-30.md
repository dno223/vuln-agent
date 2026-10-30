# Vulnerability Intelligence Report

**Date:** 2026-10-30  
**Generated:** 2026-10-30T14:50:23Z  

---

## Executive Summary

Our environment faces significant exposure across 212 high-severity vulnerabilities, with critical concerns in IBM Langflow OSS, Elastic Cloud Enterprise, and mobile applications. IBM Langflow contains multiple remote code execution and SQL injection flaws (CVSS up to 9.1) affecting versions 1.0.0–1.12.3. Elastic Cloud Enterprise suffers from symlink-following vulnerabilities enabling authentication bypass and data disclosure. Additionally, 10 new CISA Known Exploited Vulnerabilities were added this week—including actively exploited flaws in Cisco Firewall, VMware ESX, GitLab, Linux Kernel, and Adobe Commerce—demanding immediate prioritization. No monitored CVEs were confirmed in the KEV catalog at this time.

---

## Risk Narrative

The current threat landscape reflects a convergence of high-severity unpatched vulnerabilities and confirmed active exploitation. IBM Langflow's multiple remote code execution pathways present severe risk of full system compromise for any internet-accessible deployment. Elastic Cloud Enterprise flaws could allow attackers to bypass authentication and exfiltrate sensitive data at scale. The 10 new CISA KEV additions signal that threat actors are actively weaponizing vulnerabilities in widely deployed enterprise infrastructure—Cisco firewalls, VMware hypervisors, GitLab, and Linux—creating substantial risk of network infiltration, ransomware deployment, and data breaches. Collectively, these exposures threaten business continuity, regulatory compliance, and customer data integrity.

---

## Prioritized Action Items

1. Immediately patch or isolate IBM Langflow OSS instances (versions 1.0.0–1.12.3) to remediate remote code execution and SQL injection vulnerabilities rated up to CVSS 9.1.
2. Apply vendor patches for the three Elastic Cloud Enterprise symlink-following vulnerabilities to prevent authentication bypass, data disclosure, and unauthorized file access.
3. Remediate all 10 newly added CISA KEV entries—prioritizing Cisco Secure Firewall ASA, VMware ESX, and GitLab—within 24–72 hours per federal directive timelines.
4. Assess and patch Adobe Commerce/Magento and Linux Kernel systems against their respective KEV-listed vulnerabilities to reduce active exploitation risk.
5. Conduct an enterprise-wide vulnerability scan to triage all 212 high-severity CVEs, assigning remediation owners and deadlines based on asset criticality and exposure.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-107015 | 9.1 | 2026-10-29 | Insecure permissions in Simple Contacts Pro versionCode 107 allow unauthorized attackers to write and read notes in anot |
| CVE-2026-107020 | 7.5 | 2026-10-29 | An issue in the activity.LoadLinkLaterActivity component of FeedEx / Handy News Reader versionCode 116 allows attackers  |
| CVE-2026-115708 | 7.2 | 2026-10-29 | Improper Link Resolution Before File Access ('Link Following') (CWE-59) in Elastic Cloud Enterprise (ECE) can lead to au |
| CVE-2026-115709 | 8.2 | 2026-10-29 | Improper Link Resolution Before File Access ('Link Following') (CWE-59) in Elastic Cloud Enterprise (ECE) can lead to un |
| CVE-2026-115713 | 7.5 | 2026-10-29 | Improper Link Resolution Before File Access ('Link Following') (CWE-59) in Elastic Cloud Enterprise (ECE) can lead to un |
| CVE-2026-101288 | 8.8 | 2026-10-29 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote authenticated attacker to execute arbitrary code due to impro |
| CVE-2026-103092 | 8.5 | 2026-10-29 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote authenticated attacker to execute arbitrary SQL commands due  |
| CVE-2026-104317 | 8.1 | 2026-10-29 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote attacker who could reach the message broker to execute arbitr |
| CVE-2026-104324 | 8.8 | 2026-10-29 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote authenticated attacker to execute arbitrary code due to deser |
| CVE-2026-104328 | 8.8 | 2026-10-29 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote authenticated attacker to execute arbitrary code due to impro |
| CVE-2026-104339 | 9.8 | 2026-10-29 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote attacker to execute arbitrary code due to improper neutraliza |
| CVE-2026-107026 | 7.5 | 2026-10-29 | Insecure permissions in Share to Clipboard v1.14.1 (versionCode 32) allows unauthorized attackers to arbitrarily overwri |
| CVE-2026-107032 | 9.1 | 2026-10-29 | Insecure permissions in Bulk Share : Location Sender v2.1.0 (versionCode 5) allows unauthorized attackers to invoke an e |
| CVE-2026-107037 | 7.5 | 2026-10-29 | Insecure permissions in the NotificationHelper component of NoNonsense Notes versionCode 72600 allows unauthorized attac |
| CVE-2026-107042 | 7.5 | 2026-10-29 | Insecure permissions in USP Ultimate Screenshot Painter versionCode 240213.009 allows unauthorized attackers to move or  |
| CVE-2026-107326 | 8.8 | 2026-10-29 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to execute arbitrary code due to impro |
| CVE-2026-107327 | 9.9 | 2026-10-29 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to execute arbitrary code due to missi |
| CVE-2026-107328 | 9.9 | 2026-10-29 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to execute arbitrary code due to impro |
| CVE-2026-107329 | 9.9 | 2026-10-29 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to execute arbitrary code due to impro |
| CVE-2026-108494 | 7.1 | 2026-10-29 | Unauthenticated Cross Site Scripting (XSS) in Chained Quiz <= 1.4.1 versions. |
| CVE-2026-110186 | 9.8 | 2026-10-29 | IBM Langflow OSS 1.0.0 through 1.12.8 could allow a remote attacker to execute arbitrary code due to improper control of |
| CVE-2026-110193 | 8.8 | 2026-10-29 | IBM Langflow OSS 1.0.0 through 1.12.8 could allow a remote attacker with a low-privileged authenticated account to cause |
| CVE-2026-110196 | 8.8 | 2026-10-29 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote attacker with a low-privileged authenticated account to bypas |
| CVE-2026-110244 | 8.8 | 2026-10-29 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to obtain sensitive information due to |
| CVE-2026-110245 | 7.5 | 2026-10-29 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote attacker to obtain sensitive information due to improper auth |
| CVE-2026-110309 | 8.8 | 2026-10-29 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to execute arbitrary commands due to i |
| CVE-2026-114148 | 7.8 | 2026-10-29 | Incorrect default permissions in ASP.NET Core allows an authorized attacker to elevate privileges locally. |
| CVE-2026-116864 | 7.2 | 2026-10-29 | Author PHP Object Injection in WPCargo Track & Trace <= 8.0.5 versions. |
| CVE-2026-116865 | 7.2 | 2026-10-29 | Editor PHP Object Injection in Zippy <= 1.7.0 versions. |
| CVE-2026-116866 | 8.8 | 2026-10-29 | Contributor PHP Object Injection in Extra Fees Plugin for WooCommerce <= 4.4.0 versions. |
| CVE-2026-116867 | 8.8 | 2026-10-29 | Contributor PHP Object Injection in Dynamic QR Code &#8211; generator <= 1.0.1 versions. |
| CVE-2026-116868 | 8.8 | 2026-10-29 | Subscriber PHP Object Injection in BuddyPress Xprofile Custom Field Types <= 1.3.1 versions. |
| CVE-2026-116869 | 7.2 | 2026-10-29 | Shop manager PHP Object Injection in myPOS Checkout <= 1.4.5 versions. |
| CVE-2026-118073 | 8.8 | 2026-10-29 | Subscriber PHP Object Injection in News Kit Elementor Addons <= 1.5.0 versions. |
| CVE-2026-118074 | 7.2 | 2026-10-29 | Shop manager PHP Object Injection in Finale Lite <= 2.21.0 versions. |
| CVE-2026-118075 | 8.8 | 2026-10-29 | Contributor PHP Object Injection in WP Media folders <= 1.1.10 versions. |
| CVE-2026-118076 | 8.8 | 2026-10-29 | Contributor PHP Object Injection in Frisbii Pay <= 1.8.19 versions. |
| CVE-2026-118077 | 7.2 | 2026-10-29 | Author PHP Object Injection in Sastra Essential Addons for Elementor <= 1.2.3 versions. |
| CVE-2026-118078 | 7.2 | 2026-10-29 | Shop manager PHP Object Injection in Product Catalog Feed by PixelYourSite <= 3.1.4 versions. |
| CVE-2026-118079 | 7.2 | 2026-10-29 | Shop manager PHP Object Injection in FV Flowplayer Video Player <= 8.3.4 versions. |
| CVE-2026-118080 | 8.8 | 2026-10-29 | Contributor PHP Object Injection in Social Snap <= 1.5.4 versions. |
| CVE-2026-118081 | 8.8 | 2026-10-29 | Contributor PHP Object Injection in 10Web Social Photo Feed <= 1.5.6 versions. |
| CVE-2026-118082 | 8.8 | 2026-10-29 | Subscriber Privilege Escalation in Buddyboss Platform <= 3.5.0 versions. |
| CVE-2026-118083 | 7.5 | 2026-10-29 | Unauthenticated Sensitive Data Exposure in WP Crowdfunding <= 2.2.2 versions. |
| CVE-2026-118085 | 7.1 | 2026-10-29 | Unauthenticated Cross Site Scripting (XSS) in GlobalPayments WooCommerce <= 1.23.3 versions. |
| CVE-2026-119119 | 7.5 | 2026-10-29 | Crawl4AI before 0.9.5 contains a denial of service vulnerability in the Docker API server where _clamp_untrusted() fails |
| CVE-2026-119120 | 7.5 | 2026-10-29 | Crawl4AI from 0.9.0 before 0.9.5 fails to filter the CosineStrategy model_name field in untrusted Docker API request bod |
| CVE-2026-119127 | 8.1 | 2026-10-29 | ZITADEL 4.0.0 before 4.19.5 contains a host header injection vulnerability in the Login V2 UI that allows unauthenticate |
| CVE-2026-119128 | 7.4 | 2026-10-29 | ZITADEL 4.0.0 before 4.19.5 contains an authentication bypass vulnerability in the Login V2 UI that allows unauthenticat |
| CVE-2026-119129 | 8.1 | 2026-10-29 | ZITADEL 3.0.0 through 3.4.15 and 4.0.0 before 4.19.5 contains a missing authorization vulnerability in Login V2 that all |
| CVE-2026-119144 | 8.8 | 2026-10-29 | Frappe Framework before 15.111.0 and 16.x before 16.21.0 contains a server-side template injection vulnerability because |
| CVE-2026-119145 | 9.9 | 2026-10-29 | Frappe before 15.121.0 and 16.x before 16.34.0 contains a path traversal vulnerability because certain file-upload handl |
| CVE-2026-27394 | 7.1 | 2026-10-29 | Unauthenticated Cross Site Scripting (XSS) in Eventer <= 0.1.1 versions. |
| CVE-2026-42692 | 7.1 | 2026-10-29 | Unauthenticated Cross Site Scripting (XSS) in WP Crowdfunding <= 2.2.2 versions. |
| CVE-2026-42701 | 7.2 | 2026-10-29 | Shop manager PHP Object Injection in YayMail <= 4.4.6 versions. |
| CVE-2026-54856 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in RexCoin <= 1.2.6 versions. |
| CVE-2026-54857 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Quirky <= 1.23 versions. |
| CVE-2026-54858 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Printy <= 1.13.0 versions. |
| CVE-2026-54859 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Preservation <= 1.15 versions. |
| CVE-2026-54860 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Ozisti <= 1.1.10 versions. |
| CVE-2026-54864 | 7.1 | 2026-10-29 | Unauthenticated Cross Site Scripting (XSS) in Post Video Players <= 1.165 versions. |
| CVE-2026-54866 | 7.1 | 2026-10-29 | Unauthenticated Cross Site Scripting (XSS) in Razorpay Payment Button Elementor Plugin <= 1.2.8 versions. |
| CVE-2026-61988 | 7.1 | 2026-10-29 | Unauthenticated Cross Site Scripting (XSS) in Auction Nudge – Your eBay on Your Site <= 8.4.0 versions. |
| CVE-2026-61989 | 7.1 | 2026-10-29 | Unauthenticated Cross Site Scripting (XSS) in Easy Property Listings <= 3.5.25 versions. |
| CVE-2026-61991 | 10.0 | 2026-10-29 | Unauthenticated Remote Code Execution (RCE) in AjaxLoadMore Cache <= 3.1.1 versions. |
| CVE-2026-61992 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in GEO my WordPress <= 4.5.5.3 versions. |
| CVE-2026-61993 | 7.1 | 2026-10-29 | Unauthenticated Cross Site Scripting (XSS) in Blockonomics 3.11.0 versions. |
| CVE-2026-61995 | 7.1 | 2026-10-29 | Unauthenticated Cross Site Scripting (XSS) in YouTube Showcase <= 4.1.0 versions. |
| CVE-2026-61996 | 8.5 | 2026-10-29 | Subscriber SQL Injection in MLS On The Fly <= 1.8.1.5 versions. |
| CVE-2026-61997 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Legal Stone <= 1.2.11 versions. |
| CVE-2026-61998 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Le Truffe <= 1.1.7 versions. |
| CVE-2026-62001 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Marcell <= 1.2.14 versions. |
| CVE-2026-62002 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Meals & Wheels <= 1.1.13 versions. |
| CVE-2026-62003 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Mission <= 1.22 versions. |
| CVE-2026-62004 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Motorix <= 1.11 versions. |
| CVE-2026-62005 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Muzicon <= 1.15 versions. |
| CVE-2026-62006 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Nuts <= 1.12 versions. |
| CVE-2026-62008 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Orpheus <= 1.8 versions. |
| CVE-2026-62009 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Filmax <= 1.1.11 versions. |
| CVE-2026-62010 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Avventure <= 1.1.12 versions. |
| CVE-2026-62011 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Bonbon <= 1.11 versions. |
| CVE-2026-62012 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Coinpress <= 1.0.15 versions. |
| CVE-2026-62013 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Edge Decor <= 2.9 versions. |
| CVE-2026-62014 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in EmojiNation <= 1.0.12 versions. |
| CVE-2026-62015 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Gamezone <= 1.1.11 versions. |
| CVE-2026-62016 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Gamic <= 1.19 versions. |
| CVE-2026-62017 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Good Homes <= 1.3.13 versions. |
| CVE-2026-62018 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Gunslinger <= 1.11 versions. |
| CVE-2026-62131 | 9.8 | 2026-10-29 | Unauthenticated PHP Object Injection in Zoho Flow <= 2.14.5 versions. |
| CVE-2026-84294 | 7.7 | 2026-10-29 | Improper limitation of pathname in the Ad Hoc Transfer component of Progress Software WS_FTP Server versions prior to 20 |
| CVE-2026-84295 | 10.0 | 2026-10-29 | Improper authentication in Progress Software WS_FTP Server versions prior to 2024.0.6 and 2025.0.3 on Windows could allo |
| CVE-2026-85890 | 8.8 | 2026-10-29 | Double free in Microsoft Edge (Chromium-based) allows an unauthorized attacker to execute code over a network. |
| CVE-2026-85897 | 8.8 | 2026-10-29 | Heap-based buffer overflow in Microsoft Edge (Chromium-based) allows an unauthorized attacker to execute code over a net |
| CVE-2026-85899 | 8.1 | 2026-10-29 | Use after free in Microsoft Edge (Chromium-based) allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-88077 | 8.8 | 2026-10-29 | Integer overflow or wraparound in Microsoft Edge (Chromium-based) allows an unauthorized attacker to elevate privileges  |
| CVE-2026-90863 | 9.1 | 2026-10-29 | Missing authorization in the administrative interface of Progress Software WS_FTP Server versions prior to 2024.0.7 and  |
| CVE-2026-90864 | 9.1 | 2026-10-29 | A path traversal vulnerability in Progress Software WS_FTP Server versions prior to 2024.0.7 and 2025.0.4 on Windows cou |
| CVE-2026-90865 | 9.0 | 2026-10-29 | An OS command injection vulnerability in Progress Software WS_FTP Server versions prior to 2024.0.7 and 2025.0.4 on Wind |
| CVE-2026-90866 | 9.1 | 2026-10-29 | A path traversal vulnerability in Progress Software WS_FTP Server versions prior to 2024.0.7 and 2025.0.4 on Windows cou |
| CVE-2026-90867 | 8.1 | 2026-10-29 | Improper access control in the Web Admin console of Progress Software WS_FTP Server versions prior to 2024.0.7 and 2025. |
| CVE-2026-90868 | 9.9 | 2026-10-29 | An OS command injection vulnerability in Progress Software WS_FTP Server versions prior to 2024.0.7 and 2025.0.4 on Wind |
| CVE-2026-90869 | 7.5 | 2026-10-29 | A remote attacker who knows a valid account's enrolled SSH public key can terminate the shared SSH service in Progress S |
| CVE-2026-93680 | 9.8 | 2026-10-29 | IBM Langflow OSS 1.0.0 through 1.12.8 could allow a remote attacker to bypass security restrictions due to improper auth |
| CVE-2026-96187 | 7.4 | 2026-10-29 | Access of resource using incompatible type ('type confusion') in Microsoft Edge (Chromium-based) allows an unauthorized  |
| CVE-2026-96192 | 8.8 | 2026-10-29 | Use after free in Microsoft Edge for iOS allows an unauthorized attacker to execute code over a network. |
| CVE-2026-96196 | 8.8 | 2026-10-29 | Incomplete list of disallowed inputs in Microsoft Edge (Chromium-based) allows an unauthorized attacker to bypass a secu |
| CVE-2026-96198 | 8.8 | 2026-10-29 | Heap-based buffer overflow in Microsoft Edge (Chromium-based) allows an unauthorized attacker to execute code over a net |
| CVE-2026-96199 | 8.8 | 2026-10-29 | Heap-based buffer overflow in Microsoft Edge (Chromium-based) allows an unauthorized attacker to execute code over a net |
| CVE-2026-96203 | 8.8 | 2026-10-29 | Use after free in Microsoft Edge (Chromium-based) allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-107047 | 7.5 | 2026-10-29 | Insecure permissions in mendhak GPSLogger versionCode 137 allows unauthorized attackers to arbitrarily manipulate the ap |
| CVE-2026-107052 | 7.5 | 2026-10-29 | Insecure permissions in the AIDL interface of ProjectMAXS MAXS Module FileRead versionCode 27 allows unauthorized attack |
| CVE-2026-107058 | 9.8 | 2026-10-29 | An issue in Shelter versionCode 445 allows attackers to register their own auth_key and execute a takeover of another us |
| CVE-2026-115805 | 7.8 | 2026-10-29 | Improper handling of local filesystem paths in Rapid7 Insight Agent on Linux and macOS may allow authenticated local use |
| CVE-2026-118758 | 7.5 | 2026-10-29 | Kubeflow Pipelines enables users to build and deploy portable, scalable machine learning workflows. Prior to 2.18.0, the |
| CVE-2026-118759 | 7.5 | 2026-10-29 | Kubeflow Pipelines enables users to build and deploy portable, scalable machine learning workflows. Prior to 2.18.0, the |
| CVE-2026-118761 | 7.5 | 2026-10-29 | Kubeflow Pipelines enables users to build and deploy portable, scalable machine learning workflows. Prior to 2.18.0, the |
| CVE-2026-118762 | 9.3 | 2026-10-29 | Monkeytype is a minimalistic and customizable typing test. Prior to 26.43.0, the .github/workflows/fix-formatting.yml wo |
| CVE-2026-118763 | 7.4 | 2026-10-29 | sigstore-js provides JavaScript libraries for interacting with Sigstore services. Prior to 0.7.2, packages/oci/src/regis |
| CVE-2026-119115 | 8.5 | 2026-10-29 | Incorrect authorization in the issuer resolution logic in AWS Private CA Connector for Kubernetes (aws-privateca-issuer) |
| CVE-2026-11587 | 7.2 | 2026-10-29 | SQL injection allowing an authenticated user with access to ACL management to read and modify the Centreon database |
| CVE-2026-107347 | 8.4 | 2026-10-29 | HashiCorp Nomad and Nomad Enterprise are vulnerable to symlink following during dispatch payload and executor log writes |
| CVE-2026-118772 | 7.5 | 2026-10-29 | joi is a schema description language and data validator for JavaScript. From 17.1.1 until 17.13.9 and 18.3.1, the Joi.st |
| CVE-2026-118779 | 7.5 | 2026-10-29 | Forge (also called node-forge) is a native implementation of Transport Layer Security in JavaScript. Prior to 1.4.1, the |
| CVE-2026-118782 | 7.5 | 2026-10-29 | Forge (also called node-forge) is a native implementation of Transport Layer Security in JavaScript. Prior to 1.4.1, nod |
| CVE-2026-119168 | 8.8 | 2026-10-29 | HashiCorp Nomad and Nomad Enterprise are vulnerable to symlink following during same-client allocation data migration th |
| CVE-2026-119249 | 7.5 | 2026-10-29 | A malicious actor with access to the network could exploit a Binding to an Unrestricted IP Address vulnerability found i |
| CVE-2026-119250 | 7.8 | 2026-10-29 | A malicious actor with local access and low privileges could exploit an External Control of File Name or Path vulnerabil |
| CVE-2026-41216 | 7.5 | 2026-10-29 | An invalid pointer dereference vulnerability exists in the vtkPNGReader::ExecuteInformation functionality of vtk 9.6. A  |
| CVE-2026-42057 | 7.5 | 2026-10-29 | An invalid pointer dereference vulnerability exists in the vtkPNGReader::vtkPNGReaderUpdate2 functionality of vtk 9.6. A |
| CVE-2026-8822 | 7.5 | 2026-10-29 | A memory corruption vulnerability exists in the vtkDEMReader ReadProfiles functionality of vtk (version(s): 9.6.1). A sp |
| CVE-2026-8824 | 7.5 | 2026-10-29 | A memory corruption vulnerability exists in the vtkBMPReader ExecuteDataWithInformation functionality of vtk (version(s) |
| CVE-2026-9535 | 8.2 | 2026-10-29 | A out-of-bounds read vulnerability exists in the vtkChacoReader InputGraph2 functionality of vtk (version(s): 9.6.1). A  |
| CVE-2026-9536 | 7.5 | 2026-10-29 | A heap-based buffer overflow vulnerability exists in the vtkWindBladeReader FindVariableOffsets functionality of vtk (ve |
| CVE-2026-119187 | 7.5 | 2026-10-29 | Forge (also called node-forge) is a native implementation of Transport Layer Security in JavaScript. Prior to 1.4.1, the |
| CVE-2026-119188 | 7.5 | 2026-10-29 | Forge (also called node-forge) is a native implementation of Transport Layer Security in JavaScript. Prior to 1.4.1, the |
| CVE-2026-119190 | 7.4 | 2026-10-29 | Forge (also called node-forge) is a native implementation of Transport Layer Security in JavaScript. Prior to 1.4.1, nod |
| CVE-2026-119191 | 7.5 | 2026-10-29 | Forge (also called node-forge) is a native implementation of Transport Layer Security in JavaScript. Prior to 1.4.1, the |
| CVE-2026-119194 | 7.5 | 2026-10-29 | pyasn1 is a generic ASN.1 library for Python. From 0.3.3 until 0.6.5, schemaless container decoding stores every decoded |
| CVE-2026-119195 | 7.5 | 2026-10-29 | pyasn1 is a generic ASN.1 library for Python. Prior to 0.6.5, constructed string and indefinite-length ANY decoding repe |
| CVE-2026-119196 | 7.5 | 2026-10-29 | pyasn1 is a generic ASN.1 library for Python. Prior to 0.6.5, constructed BIT STRING decoding repeatedly shifts and copi |
| CVE-2026-119197 | 7.5 | 2026-10-29 | pyasn1 is a generic ASN.1 library for Python. Prior to 0.6.5, binary REAL decoding builds a large mantissa one octet at  |
| CVE-2026-92092 | 7.4 | 2026-10-29 | A flaw was found in openshift-ansible. The installer container's `run` script downloads and executes remote inventory an |
| CVE-2026-119202 | 7.5 | 2026-10-29 | @hapi/content provides HTTP Content-* header parsing. From 3.0.6 until 6.0.3, Content.disposition() uses an unanchored p |
| CVE-2026-119325 | 7.5 | 2026-10-29 | Bricks Theme 2.4 and before for WordPress contains an unauthenticated broken access control vulnerability in the load_po |
| CVE-2026-13303 | 8.7 | 2026-10-29 | HashiCorp Boundary and Boundary Enterprise are vulnerable to a server-side request forgery in the Vault credential store |
| CVE-2026-119283 | 7.5 | 2026-10-29 | joserfc is a Python library that provides an implementation of several JSON Object Signing and Encryption (JOSE) standar |
| CVE-2026-119286 | 7.5 | 2026-10-29 | GraphQL-core is a Python port of the GraphQL.js reference implementation. From 3.3.0a3 until 3.3.1, validate() reuses a  |
| CVE-2026-45049 | 8.3 | 2026-10-29 | Open Access Management (OpenAM) is an access management solution. Prior to 16.1.1, the `Cross-Domain Single Sign-On` (`C |
| CVE-2026-61645 | 9.1 | 2026-10-29 | Docat is a tool for hosting versioned static documentation. In the affected implementation, an arbitrary file upload vul |
| CVE-2026-61671 | 8.1 | 2026-10-29 | WeGIA is a web manager for charitable institutions. Prior to the advisory's stated patched version 3.8.7, the `/controle |
| CVE-2026-61707 | 9.0 | 2026-10-29 | SOCFortress CoPilot focuses on providing a single pane of glass for all your security operations needs. Prior to 0.1.76, |
| CVE-2026-61719 | 8.9 | 2026-10-29 | WeGIA is a web manager for charitable institutions. Prior to 3.8.7, a stored cross-site scripting vulnerability in `saud |
| CVE-2026-119260 | 8.8 | 2026-10-30 | Use after free in Frames in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-119261 | 9.6 | 2026-10-30 | Improper input validation in Skia in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to potentially execu |
| CVE-2026-119262 | 8.8 | 2026-10-30 | Improper input validation in V8 in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to potentially execute |
| CVE-2026-119263 | 9.6 | 2026-10-30 | Memory corruption in GarbageCollection in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to potentially  |
| CVE-2026-119264 | 8.8 | 2026-10-30 | Memory corruption in Dawn in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to potentially execute arbit |
| CVE-2026-119265 | 8.8 | 2026-10-30 | Memory corruption in Quota in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to potentially execute arbi |
| CVE-2026-119266 | 8.8 | 2026-10-30 | Use after free in Quota in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to potentially execute arbitra |
| CVE-2026-119267 | 8.8 | 2026-10-30 | Memory corruption in DOM in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to potentially execute arbitr |
| CVE-2026-119268 | 8.8 | 2026-10-30 | Integer overflow in Editing in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to potentially execute arb |
| CVE-2026-119269 | 8.8 | 2026-10-30 | Use after free in Blink in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to execute arbitrary code insi |
| CVE-2026-119270 | 8.8 | 2026-10-30 | Improper input validation in CacheStorage in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to potential |
| CVE-2026-119271 | 8.8 | 2026-10-30 | Use after free in Skia in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to execute arbitrary code insid |
| CVE-2026-76025 | 8.8 | 2026-10-30 | Use after free in FileSystem in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to execute arbitrary code |
| CVE-2026-76026 | 8.8 | 2026-10-30 | Memory corruption in Autofill in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to execute arbitrary cod |
| CVE-2026-76028 | 8.8 | 2026-10-30 | Use after free in FileSystem in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to execute arbitrary code |
| CVE-2026-76029 | 8.8 | 2026-10-30 | Memory corruption in Network in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to potentially execute ar |
| CVE-2026-76030 | 8.8 | 2026-10-30 | Memory corruption in FileSystem in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to potentially execute |
| CVE-2026-76031 | 8.8 | 2026-10-30 | Use after free in Input in Google Chrome prior to 156.0.8078.79 allowed a remote attacker to execute arbitrary code insi |
| CVE-2026-103963 | 7.5 | 2026-10-30 | A flaw was found in glib-networking. When establishing connections using Transport Layer Security (TLS) version 1.3, the |
| CVE-2026-104368 | 8.8 | 2026-10-30 | The Export and Import Users and Customers plugin for WordPress is vulnerable to Privilege Escalation in all versions up  |
| CVE-2026-114422 | 7.5 | 2026-10-30 | The Enable Media Replace WordPress plugin before 4.2.3 does not restrict the classes allowed when deserializing stored m |
| CVE-2026-114443 | 7.5 | 2026-10-30 | The Security Plugin, Firewall & Malware Scanner with Auto Removal WordPress plugin before 2.191 does not verify the acco |
| CVE-2026-117571 | 8.8 | 2026-10-30 | The WP Visitor Statistics (Real Time Traffic) WordPress plugin before 8.8 does not sanitize and escape tracking data der |
| CVE-2026-103039 | 9.8 | 2026-10-30 | The Gravity Forms plugin for WordPress is vulnerable to PHP Object Injection in all versions up to, and including, 3.1.2 |
| CVE-2026-110732 | 7.5 | 2026-10-30 | The AI Engine – The Chatbot, AI Framework & MCP for WordPress plugin for WordPress is vulnerable to Missing Authorizatio |
| CVE-2026-116622 | 7.2 | 2026-10-30 | The Food Store – Online Food Delivery & Pickup plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the |
| CVE-2026-89435 | 8.8 | 2026-10-30 | The Formidable Forms – WordPress Form Builder for Contact Forms, Calculators, Quizzes & More plugin for WordPress is vul |
| CVE-2026-90437 | 7.2 | 2026-10-30 | The Gravity Forms plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Post Excerpt / Post Custom Field |
| CVE-2026-97645 | 7.2 | 2026-10-30 | The Gravity Forms plugin for WordPress is vulnerable to Stored Cross-Site Scripting via List Field in all versions up to |
| CVE-2026-59387 | 8.8 | 2026-10-30 | The Nginx routing configuration for Cloud Controller blocks unauthenticated access to /internal/v4/ and /internal/v5/ en |
| CVE-2025-31704 | 9.8 | 2026-10-30 | A vulnerability has been found in the Dahua Intelligent Connection Center. A remote attacker could send a specially craf |
| CVE-2026-101210 | 7.2 | 2026-10-30 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Neutralization of Special Elements used in an  |
| CVE-2026-101213 | 7.8 | 2026-10-30 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Privilege Management vulnerability. A low priv |
| CVE-2026-101214 | 7.2 | 2026-10-30 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Neutralization of Special Elements used in an  |
| CVE-2026-111504 | 7.2 | 2026-10-30 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Neutralization of Argument Delimiters in a Com |
| CVE-2026-111505 | 8.8 | 2026-10-30 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Neutralization of Special Elements used in an  |
| CVE-2026-119373 | 7.8 | 2026-10-30 | SQLite before 3.54.0 built with FTS5 contains a heap buffer overflow in fts5MergeRowidLists() that undersizes the output |
| CVE-2026-119374 | 7.8 | 2026-10-30 | SQLite before 3.54.0 built with FTS5 contains a heap buffer overflow in fts5DoSecureDelete() that allows attackers to wr |
| CVE-2026-119379 | 7.8 | 2026-10-30 | SQLite before 3.54.0 built with the session extension contains a heap buffer overflow vulnerability in sqlite3changeset_ |
| CVE-2026-119407 | 7.1 | 2026-10-30 | Element Web and Element Desktop before 1.12.32 accept guest credentials from URL fragment parameters in loadSession, all |
| CVE-2026-119408 | 8.8 | 2026-10-30 | n8n before 2.42.6, 2.43.x before 2.43.3, and 3.x before 3.0.1 contains a remote code execution vulnerability via depreca |
| CVE-2026-119409 | 7.2 | 2026-10-30 | OPNsense before 26.7.8 contains a command injection vulnerability that allows authenticated users with the System: Firmw |
| CVE-2026-119418 | 8.1 | 2026-10-30 | CakePHP through 5.4.3 contains an sql injection vulnerability that allows attackers to inject SQL by supplying unvalidat |
| CVE-2026-119419 | 8.1 | 2026-10-30 | CakePHP through 5.4.3 contains an sql injection vulnerability that allows attackers to inject SQL by supplying unvalidat |
| CVE-2026-119420 | 8.8 | 2026-10-30 | Lago through 1.55.0 contains an authentication bypass vulnerability that allows organization administrators to obtain se |
| CVE-2026-119426 | 7.5 | 2026-10-30 | phpMyAdmin through 5.2.3 contains a cross-site request forgery vulnerability that allows remote attackers to execute arb |
| CVE-2026-119549 | 7.1 | 2026-10-30 | Jellyfin through 12.4 contains a server-side request forgery vulnerability that lets authenticated users bypass SvgSecur |
| CVE-2026-119568 | 7.4 | 2026-10-30 | vsftpd through 3.0.5 contains an authentication bypass vulnerability in ssl_data_accept() that allows unauthenticated at |
| CVE-2026-119586 | 7.8 | 2026-10-30 | SQLite command-line shell through 3.54.1 contains a command injection vulnerability in the .recover command that emits a |
| CVE-2026-111503 | 7.1 | 2026-10-30 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Neutralization of Special Elements used in an  |
| CVE-2026-91917 | 8.0 | 2026-10-30 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Input Validation vulnerability. A low privileg |
| CVE-2026-112347 | 7.6 | 2026-10-30 | Kirki plugin for WordPress before 6.4.1 contains a broken object-level access control vulnerability in its page REST API |
| CVE-2026-119528 | 7.8 | 2026-10-30 | A flaw was found in GIMP. The PSD plug-in’s image resource header loader uses an incorrect destination size when copying |
| CVE-2026-119572 | 8.7 | 2026-10-30 | Traefik from 3.7.0-ea.1 before 3.7.15 contains an authentication bypass vulnerability in the Kubernetes Ingress NGINX pr |
| CVE-2026-119578 | 7.8 | 2026-10-30 | MONAI from 1.6.0 before 1.6.1 contains a remote code execution vulnerability in Auto3DSeg algo_from_json() that allows a |
| CVE-2026-119597 | 9.8 | 2026-10-30 | OpenDeepWiki through 2.0.6 contains a hard-coded JWT signing key vulnerability that allows unauthenticated attackers to  |
| CVE-2026-86715 | 7.1 | 2026-10-30 | Plaintext storage of a password vulnerability in Crypttech Crypto and Informatics Technologies Industry and Trade Inc. V |
| CVE-2026-91912 | 7.3 | 2026-10-30 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Use of Hard-coded Cryptographic Key vulnerability. A lo |
| CVE-2026-91913 | 8.8 | 2026-10-30 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Neutralization of Special Elements used in an  |
| CVE-2026-91914 | 7.1 | 2026-10-30 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Authentication Bypass by Spoofing vulnerability. An una |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-97229 | GitLab / Community Edition and Enterprise Edition | 2026-10-29 | 2026-11-01 | Unknown |
| CVE-2026-76418 | Cisco / Secure Firewall ASA Software and Cisco Secure FTD Software | 2026-10-29 | 2026-11-01 | Unknown |
| CVE-2026-41709 | Broadcom / VMware ESX | 2026-10-28 | 2026-11-11 | Unknown |
| CVE-2026-46300 | Linux / Kernel | 2026-10-28 | 2026-10-31 | Unknown |
| CVE-2026-48356 | Adobe / Commerce and Magento | 2026-10-27 | 2026-11-10 | Unknown |
| CVE-2026-111497 | Google / Brotli | 2026-10-27 | 2026-11-10 | Unknown |
| CVE-2026-109618 | PHP Group / PHP | 2026-10-26 | 2026-10-29 | Unknown |
| CVE-2026-109619 | PHP Group / PHP | 2026-10-26 | 2026-10-29 | Unknown |
| CVE-2026-114625 | Arista / VeloCloud Orchestrator | 2026-10-23 | 2026-10-26 | Unknown |
| CVE-2026-110447 | Collabora / Collabora Online – Built-in CODE Server | 2026-10-23 | 2026-10-26 | Unknown |

---

*Total entries in CISA KEV catalog: 1764*