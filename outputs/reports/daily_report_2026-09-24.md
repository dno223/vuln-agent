# Vulnerability Intelligence Report

**Date:** 2026-09-24  
**Generated:** 2026-09-24T13:14:01Z  

---

## Executive Summary

Our environment faces critical exposure across 145 high-severity vulnerabilities, including a CVSS 10.0 remote code execution flaw in SunEditor and a CVSS 9.9 RCE in ZohoCorp ManageEngine OpManager MSP. Apache Tomcat Native and IBM Financial Transaction Manager add further risk. Eight new CISA Known Exploited Vulnerabilities were added this week across network infrastructure products from Arista, F5, Check Point, and Zyxel, signaling active threat actor exploitation in the wild. Immediate patching and mitigation actions are required to reduce organizational exposure.

---

## Risk Narrative

Threat actors are actively exploiting vulnerabilities in network infrastructure and enterprise management platforms, as evidenced by eight new CISA KEV additions in seven days. Critical RCE and authentication bypass flaws in ManageEngine and SunEditor provide attackers with direct pathways to system compromise and lateral movement. Apache Tomcat Native vulnerabilities introduce TLS downgrade and denial-of-service risks to web-facing services. The IBM FTM payment authorization flaw carries significant financial and regulatory consequences. The convergence of critical severity scores, active exploitation of similar platforms in the wild, and the breadth of affected systems elevates overall organizational risk to a high level requiring executive attention and immediate resource allocation.

---

## Prioritized Action Items

1. Immediately patch or isolate systems affected by CVE-2026-59167 (CVSS 10.0) and CVE-2026-19599 (CVSS 9.9) as both enable unauthenticated remote code execution.
2. Apply vendor patches for CVE-2026-86246 (CVSS 9.1) in Apache Tomcat Native to eliminate insecure default TLS configurations.
3. Audit and remediate ZohoCorp ManageEngine OpManager and Firewall Analyzer instances vulnerable to authentication bypass and command injection (CVE-2026-75825, CVE-2026-76978).
4. Review and patch all network perimeter devices matching the eight new CISA KEV entries, prioritizing F5 BIG-IP APM and Check Point products due to known active exploitation.
5. Assess IBM Financial Transaction Manager deployments for CVE-2026-18177 to prevent unauthorized payment actions and implement compensating authorization controls immediately.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-19599 | 9.9 | 2026-09-23 | ZohoCorp ManageEngine OpManager MSP versions 12.8.709 and below were vulnerable to a Remote Code Execution vulnerability |
| CVE-2026-75825 | 8.8 | 2026-09-23 | ZohoCorp ManageEngine OpManager versions 12.8.710 and below with the Application Manager Plugin enabled were vulnerable  |
| CVE-2026-76978 | 8.8 | 2026-09-23 | ZohoCorp ManageEngine OpManager and Firewall Analyzer versions 12.8.709 and below were vulnerable to a Command Injection |
| CVE-2026-76979 | 7.7 | 2026-09-23 | ZohoCorp ManageEngine OpManager and Firewall Analyzer versions 12.8.709 and below were vulnerable to an XML Injection vu |
| CVE-2026-76980 | 7.4 | 2026-09-23 | ZohoCorp ManageEngine OpManager and Firewall Analyzer versions 12.8.709 and below were vulnerable to a Data Exposure vul |
| CVE-2026-86243 | 7.5 | 2026-09-23 | Buffer over-read vulnerability in Apache Tomcat Native during the TLS handshake permits a malicious user to trigger a Do |
| CVE-2026-86246 | 9.1 | 2026-09-23 | Initialization of a resource with an insecure default vulnerability in Apache Tomcat Native enabled insecure options by  |
| CVE-2026-86247 | 7.4 | 2026-09-23 | Race condition within a thread vulnerability in Apache Tomcat Native allowed client certificate verification requirement |
| CVE-2026-18177 | 7.1 | 2026-09-23 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to execute unauthorized payme |
| CVE-2026-59167 | 10.0 | 2026-09-23 | SunEditor is a lightweight and powerful WYSIWYG editor in vanilla JavaScript with no dependencies. Prior to 2.47.11, the |
| CVE-2026-86677 | 8.8 | 2026-09-23 | ZohoCorp ManageEngine Applications Manager versions 182000 and below allowed a low-privileged user to run unauthorized S |
| CVE-2026-86678 | 8.8 | 2026-09-23 | ZohoCorp ManageEngine Applications Manager versions 182000 and below allowed a low-privileged user to obtain an administ |
| CVE-2026-86679 | 7.1 | 2026-09-23 | ZohoCorp ManageEngine Applications Manager versions 182000 and below were vulnerable to a permissions validation issue t |
| CVE-2026-86681 | 7.6 | 2026-09-23 | ZohoCorp ManageEngine Applications Manager versions 182200 and below were vulnerable to a permissions validation issue t |
| CVE-2026-86683 | 8.1 | 2026-09-23 | ZohoCorp ManageEngine Applications Manager versions 182000 and below allowed a low-privileged user to change the proxy s |
| CVE-2026-86708 | 10.0 | 2026-09-23 | ZohoCorp ManageEngine Applications Manager versions 182200 and below were vulnerable to exposure of a Google Cloud servi |
| CVE-2026-96512 | 7.8 | 2026-09-23 | A flaw was found in sudo. When sudoers rules use NOTBEFORE or NOTAFTER time-based access restrictions with timestamps th |
| CVE-2026-96560 | 9.8 | 2026-09-23 | LightLLM through 1.2.0 contains a remote code execution vulnerability in the KV-transfer worker when started with --pd_t |
| CVE-2026-55610 | 8.7 | 2026-09-23 | InvoiceShelf is an open-source web & mobile app that helps track expenses, payments and create professional invoices and |
| CVE-2026-73588 | 7.4 | 2026-09-23 | Dell Secure Connect Gateway (SCG) Policy Manager, versions prior to 5.34.00.16, contains a Missing Authentication for Cr |
| CVE-2026-73591 | 7.5 | 2026-09-23 | Dell Secure Connect Gateway (SCG) Policy Manager, versions prior to 5.34.00.16, contains an Inclusion of Sensitive Infor |
| CVE-2026-96275 | 8.8 | 2026-09-23 | A malicious or compromised Flatpak repository can write attacker-controlled content to arbitrary locations on the host f |
| CVE-2026-96276 | 9.8 | 2026-09-23 | If a malicious SDK container declares an extension point with a crafted `directory` path, and a developer runs `flatpak  |
| CVE-2026-18181 | 8.1 | 2026-09-23 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to bypass authentication and  |
| CVE-2026-18184 | 7.4 | 2026-09-23 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to obtain sensitive informati |
| CVE-2026-18185 | 7.3 | 2026-09-23 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to access sensitive informati |
| CVE-2026-18490 | 8.8 | 2026-09-23 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift is vulnerable to unauthenticated remote code execution via  |
| CVE-2026-18872 | 9.3 | 2026-09-23 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift is vulnerable to stored cross-site scripting (CWE-79) in th |
| CVE-2026-18875 | 7.3 | 2026-09-23 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift is vulnerable to RAG poisoning via unauthenticated runbook  |
| CVE-2026-19179 | 8.2 | 2026-09-23 | IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to manipulate database querie |
| CVE-2026-79310 | 8.5 | 2026-09-23 | webpy web.py 0.76 is vulnerable to server-side template injection (SSTI). The template engine can be tricked into execut |
| CVE-2026-96673 | 7.5 | 2026-09-23 | Photoview through 2.4.0 contains an SQL injection vulnerability in the album download route that allows unauthenticated  |
| CVE-2025-63564 | 9.8 | 2026-09-23 | SQL injection vulnerability in Moodle Socialwall plugin v.3.0 through v.3.3 allows an attacker to execute arbitrary code |
| CVE-2026-19888 | 7.5 | 2026-09-23 | Missing validation of a mandatory attribute in the SCRAM client-final-message parser in PgBouncer through 1.25.2 allows  |
| CVE-2026-6668 | 7.5 | 2026-09-23 | Integer overflow in the packet buffer growth logic in PgBouncer through 1.25.2 allows an unauthenticated remote attacker |
| CVE-2026-85724 | 9.6 | 2026-09-23 | Moquette is a lightweight Java MQTT broker. Prior to 0.18.1, when pattern-based ACL rules are configured, Authorizations |
| CVE-2026-88830 | 7.5 | 2026-09-23 | A unit confusion in BusyBox TLS Montgomery reduction buffer allocation causes a pre-authentication heap buffer overflow  |
| CVE-2026-88832 | 7.3 | 2026-09-23 | BusyBox romfs volume ID parsing uses unbounded strlen on attacker-controlled metadata, causing a heap buffer overflow wh |
| CVE-2026-93349 | 8.8 | 2026-09-23 | Frictionless through 5.20.0rc1 contains an OS command injection vulnerability in the explore console command that allows |
| CVE-2026-96513 | 7.3 | 2026-09-23 | A security flaw has been discovered in Neethuharii CafeManagement. This issue affects some unknown processing of the fil |
| CVE-2026-96514 | 7.3 | 2026-09-23 | A weakness has been identified in Neethuharii CafeManagement. Impacted is an unknown function of the file CafePortalLogi |
| CVE-2026-96656 | 7.2 | 2026-09-23 | Plex Media Server before 1.43.3.10861 allows an admin user to write arbitrary files that may be executed on load. The pr |
| CVE-2026-96754 | 9.8 | 2026-09-23 | orval versions before 8.29.0 contain a code injection vulnerability in the @orval/hono generator that fails to escape Op |
| CVE-2026-96755 | 9.8 | 2026-09-23 | orval versions 8.14.0 through 8.28.1 contain a code injection vulnerability in the @orval/effect generator that converts |
| CVE-2026-96756 | 8.1 | 2026-09-23 | orval versions before 8.30.0 contain a code injection vulnerability in the @orval/core factory generator that fails to e |
| CVE-2026-96757 | 9.8 | 2026-09-23 | orval before 8.29.0 fails to escape OpenAPI media-type keys when emitting them into single-quoted Content-Type string li |
| CVE-2026-96758 | 9.8 | 2026-09-23 | orval @orval/core before 8.28.0 contains a code injection vulnerability in the form-data serializer that fails to escape |
| CVE-2026-96759 | 9.8 | 2026-09-23 | orval before 8.29.0 fails to escape the operationId parameter when emitting it into generated TanStack Query mutator opt |
| CVE-2026-96775 | 8.8 | 2026-09-23 | MLflow's dspy flavor, versions >= 2.0,  applies the MLFLOW_ALLOW_PICKLE_DESERIALIZATION=False security control only when |
| CVE-2026-96804 | 8.8 | 2026-09-23 | MLflow's statsmodel flavor, versions 2.1.0 to 3.14.0, omits the MLFLOW_ALLOW_PICKLE_DESERIALIZATION=False security contr |
| CVE-2026-96808 | 7.4 | 2026-09-23 | In Flatpak before 1.18.1, the revokefs writer, used by the flatpak-system-helper to receive repository data from unprivi |
| CVE-2026-59990 | 7.5 | 2026-09-23 | Jawn is an open source JSON parser. Prior to 1.7.0, Jawn parse methods accept arbitrarily deep JSON array and object nes |
| CVE-2026-61695 | 7.5 | 2026-09-23 | Wire provides gRPC and protocol buffers for Android, Kotlin, Swift, and Java. Prior to 6.4.1 and 7.0.0-alpha04, Wire's S |
| CVE-2026-61814 | 7.5 | 2026-09-23 | Jawn is an open source JSON parser. Prior to 1.7.0, Jawn's AsyncParser can perform quadratic work when a single JSON tok |
| CVE-2026-75131 | 7.8 | 2026-09-23 | NetworkManager-l2tp through 1.52.4, fixed in 1.52.6, contains a privilege escalation vulnerability that allows local use |
| CVE-2026-76086 | 8.5 | 2026-09-23 | Formie is a Craft CMS plugin for creating forms. Prior to 2.2.23 and 3.1.31, Formie's formie/integrations/form-settings  |
| CVE-2026-76087 | 8.2 | 2026-09-23 | Formie is a Craft CMS plugin for creating forms. Prior to 2.2.23 and 3.1.31, Formie's anonymous formie/submissions/submi |
| CVE-2026-76089 | 7.7 | 2026-09-23 | Formie is a Craft CMS plugin for creating forms. Prior to 2.2.23 and 3.1.31, Formie's formie/sent-notifications/get-rese |
| CVE-2026-76648 | 8.5 | 2026-09-23 | CopyAPIView (awx/awx/api/generics.py:873) sets permission_classes =
(IsAuthenticated,), so DRF's get_object() performs n |
| CVE-2026-77394 | 7.6 | 2026-09-23 | OpenC3 COSMOS provides the functionality needed to send commands to and receive data from one or more embedded systems.  |
| CVE-2026-77422 | 7.5 | 2026-09-23 | JLine is a Java library for handling console input. From 3.0.0 until 3.30.15 and 4.3.1, the JLine built-in grep command  |
| CVE-2026-77423 | 7.5 | 2026-09-23 | JLine is a Java library for handling console input. From 3.0.0 until 3.30.15 and 4.3.1, the JLine built-in less viewer p |
| CVE-2026-77601 | 8.8 | 2026-09-23 | OpenC3 COSMOS provides the functionality needed to send commands to and receive data from one or more embedded systems.  |
| CVE-2026-77602 | 9.9 | 2026-09-23 | OpenC3 COSMOS provides the functionality needed to send commands to and receive data from one or more embedded systems.  |
| CVE-2026-84474 | 9.9 | 2026-09-23 | A flaw was found in Red Hat Ansible Automation Platform's automation-
controller. The provisioning-callback secret (host |
| CVE-2026-84486 | 8.2 | 2026-09-23 | A flaw was found in Red Hat Ansible Automation Platform's automation-
controller. Four debug views that trigger the inte |
| CVE-2026-84499 | 7.7 | 2026-09-23 | A flaw was found in Red Hat Ansible Automation Platform's automation-
controller. Survey questions of type password are  |
| CVE-2026-84502 | 9.9 | 2026-09-23 | A flaw was found in Red Hat Ansible Automation Platform's automation-
controller. The Project scm_url field is not valid |
| CVE-2026-93526 | 7.1 | 2026-09-23 | Unauthenticated Cross Site Scripting (XSS) in Event Tickets <= 5.29.4 versions. |
| CVE-2026-93527 | 8.5 | 2026-09-23 | Contributor SQL Injection in Live Copy Paste for Elementor <= 1.5.10 versions. |
| CVE-2026-93622 | 7.1 | 2026-09-23 | Unauthenticated Cross Site Scripting (XSS) in WPS Limit Login <= 1.5.9.3 versions. |
| CVE-2026-93773 | 8.5 | 2026-09-23 | Contributor SQL Injection in Mollie Forms <= 2.11.0 versions. |
| CVE-2026-93774 | 7.1 | 2026-09-23 | Unauthenticated Cross Site Scripting (XSS) in WP Photo Album Plus <= 9.3.02.002 versions. |
| CVE-2026-94124 | 8.5 | 2026-09-23 | Contributor SQL Injection in WP EasyCart <= 5.9.4 versions. |
| CVE-2026-94174 | 7.6 | 2026-09-23 | Administrator SQL Injection in Email Log <= 2.63 versions. |
| CVE-2026-94176 | 7.1 | 2026-09-23 | Unauthenticated Cross Site Scripting (XSS) in Mang Board WP <= 2.4.1 versions. |
| CVE-2026-94179 | 7.1 | 2026-09-23 | Unauthenticated Cross Site Scripting (XSS) in Razorpay Payment Button <= 2.4.9 versions. |
| CVE-2026-94181 | 7.4 | 2026-09-23 | An address bar spoofing issue in affected versions of Arc could allow an attacker to spoof the browser address bar via a |
| CVE-2026-94487 | 8.1 | 2026-09-23 | Unauthenticated Cross Site Request Forgery (CSRF) in PublishPress Capabilities <= 2.50.1 versions. |
| CVE-2026-95513 | 7.5 | 2026-09-23 | Unauthenticated Broken Access Control in Online Booking & Scheduling Calendar for WordPress by vcita <= 4.6.0 versions. |
| CVE-2026-95515 | 7.1 | 2026-09-23 | Unauthenticated Cross Site Scripting (XSS) in Ninja Forms <= 3.15.3 versions. |
| CVE-2026-95522 | 7.6 | 2026-09-23 | Shop manager SQL Injection in Easy Digital Downloads <= 3.7.0 versions. |
| CVE-2026-95528 | 7.1 | 2026-09-23 | Unauthenticated Cross Site Scripting (XSS) in Core Web Vitals & PageSpeed Booster <= 1.0.31 versions. |
| CVE-2026-95529 | 7.1 | 2026-09-23 | Unauthenticated Cross Site Scripting (XSS) in Calculated Fields Form <= 5.5.1.1 versions. |
| CVE-2026-95590 | 7.1 | 2026-09-23 | Subscriber SQL Injection in Tainacan <= 1.2.0 versions. |
| CVE-2026-95593 | 7.6 | 2026-09-23 | Editor SQL Injection in Ultimeter <= 3.0.8 versions. |
| CVE-2026-95601 | 9.3 | 2026-09-23 | Unauthenticated SQL Injection in Product Filter by WBW <= 3.1.7 versions. |
| CVE-2026-95603 | 7.2 | 2026-09-23 | Shop manager PHP Object Injection in Reycob Product Import Export <= 2.3.0 versions. |
| CVE-2026-95604 | 7.5 | 2026-09-23 | Unauthenticated Broken Access Control in Loops & Logic <= 4.2.4 versions. |
| CVE-2026-96541 | 7.5 | 2026-09-23 | A denial-of-service flaw was found in gnome-remote-desktop. An unauthenticated remote attacker can open RDP connections  |
| CVE-2026-75884 | 9.1 | 2026-09-23 | A flaw was found in AWX. The container group pod_spec_override field uses an incomplete blocklist that only restricts au |
| CVE-2026-84683 | 8.7 | 2026-09-23 | A flaw was found in Red Hat Ansible Automation Platform's automation-
controller. The HTML view of job, ad hoc command,  |
| CVE-2026-84691 | 8.7 | 2026-09-23 | A flaw was found in Red Hat Ansible Automation Platform's automation-
controller. The setting that formats the log messa |
| CVE-2026-84706 | 7.6 | 2026-09-23 | A flaw was found in Ansible Automation Platform's automation-controller. The custom
Credential Type environment-variable |
| CVE-2026-84714 | 7.1 | 2026-09-23 | A flaw was found in the automation-controller input-validation
                  guard sanitize_jinja(). The function us |
| CVE-2026-84719 | 9.9 | 2026-09-23 | A flaw was found in the Ansible Automation Platform automation-controller. When a
WorkflowJobTemplate is copied, the dee |
| CVE-2026-85475 | 7.2 | 2026-09-23 | A flaw was found in the Ansible Automation Platform automation controller. The
external logging (rsyslog) configuration  |
| CVE-2026-86064 | 8.6 | 2026-09-23 | Klever-Go is the Go implementation of the Klever blockchain protocol. Prior to 1.7.20, the default-open GET /log WebSock |
| CVE-2026-86065 | 7.5 | 2026-09-23 | Klever-Go is the Go implementation of the Klever blockchain protocol. Prior to 1.7.20, the default-open GET /subscribe e |
| CVE-2026-94183 | 7.4 | 2026-09-23 | Arc Search for Android before version 1.12.10 does not display a fullscreen notification when a page enters fullscreen m |
| CVE-2026-96826 | 7.6 | 2026-09-23 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Shazzad Hossain Kh |
| CVE-2026-96889 | 7.8 | 2026-09-23 | A flaw was found in librsvg. When processing an SVG document containing nested XML inclusions (Xincludes) with duplicate |
| CVE-2026-6721 | 9.8 | 2026-09-23 | IBM Concert 1.0.0 through 3.0.0 allows an unauthenticated remote attacker can supply specially crafted input that is inc |
| CVE-2026-6730 | 9.8 | 2026-09-23 | IBM Concert 1.0.0 through 3.0.0 is vulnerable to a buffer overflow, caused by improper bounds checking. A local user cou |
| CVE-2026-6794 | 7.8 | 2026-09-23 | IBM Concert 1.0.0 through 3.0.0 has a double free vulnerability that exists due to incorrect memory management. A local  |
| CVE-2026-6928 | 9.8 | 2026-09-23 | IBM Concert 1.0.0 through 3.0.0 references or accesses memory after it has been freed. This allows an attacker who can i |
| CVE-2026-6935 | 7.8 | 2026-09-23 | IBM Concert 1.0.0 through 3.0.0 invokes operating system commands without fully qualifying executable paths or adequatel |
| CVE-2026-75886 | 7.2 | 2026-09-23 | A flaw was found in openshift/console. An unauthenticated remote attacker can exploit a misconfiguration in the Catalogd |
| CVE-2026-80379 | 8.8 | 2026-09-23 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary commands du |
| CVE-2026-80412 | 8.8 | 2026-09-23 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary code due to |
| CVE-2026-80425 | 8.8 | 2026-09-23 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary commands du |
| CVE-2026-96556 | 7.3 | 2026-09-23 | A flaw has been found in Neethuharii CafeManagement. Affected by this vulnerability is the function addcashier of the fi |
| CVE-2026-19125 | 8.1 | 2026-09-23 | The EthPress – Web3 Login plugin for WordPress is vulnerable to Authentication Bypass in all versions up to, and includi |
| CVE-2026-75887 | 7.5 | 2026-09-23 | A flaw was found in the OpenShift console. An unauthenticated attacker can exploit a path traversal vulnerability by man |
| CVE-2026-80423 | 8.8 | 2026-09-23 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to obtain sensitive information  |
| CVE-2026-81208 | 7.7 | 2026-09-23 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow an authenticated user to access sensitive information due to imp |
| CVE-2026-81536 | 7.7 | 2026-09-23 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to obtain sensitive information  |
| CVE-2026-81537 | 8.8 | 2026-09-23 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary code due to |
| CVE-2026-86583 | 8.8 | 2026-09-23 | The Import and export users and customers plugin for WordPress is vulnerable to Privilege Escalation in all versions up  |
| CVE-2026-93352 | 9.8 | 2026-09-23 | Laravel-Mediable 7.0.0 before 7.0.2 contains an incomplete patch for CVE-2026-49972 in which the .pht extension is absen |
| CVE-2026-96601 | 7.3 | 2026-09-23 | A vulnerability was detected in Abdurrab5 online-makeup-store. This affects an unknown function of the file index.php of |
| CVE-2026-96602 | 7.3 | 2026-09-23 | A flaw has been found in Abdurrab5 online-makeup-store. This impacts an unknown function of the file customerSignin.php  |
| CVE-2026-96603 | 7.3 | 2026-09-23 | A vulnerability has been found in Abdurrab5 online-makeup-store. Affected is the function confirm_logged_in/confirm_user |
| CVE-2026-96604 | 7.3 | 2026-09-23 | A vulnerability was identified in SoftNews Media Group DataLife Engine 18.0. This affects the function strip_data of the |
| CVE-2026-70125 | 8.8 | 2026-09-23 | Microsoft Outlook Remote Code Execution Vulnerability |
| CVE-2026-89078 | 9.9 | 2026-09-24 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 19.2 before 19.2.7, 19.3 before 19.3.3, and 1 |
| CVE-2026-92470 | 7.7 | 2026-09-24 | GitLab has remediated an issue in GitLab EE affecting all versions from 18.7 before 19.2.7, 19.3 before 19.3.3, and 19.4 |
| CVE-2026-93577 | 9.9 | 2026-09-24 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 19.2 before 19.2.7, 19.3 before 19.3.3, and 1 |
| CVE-2026-96751 | 7.3 | 2026-09-24 | A vulnerability has been found in pmTicket Project-Management-Software up to 078fa56a782490c5059a0814f84df27984f4d7e2. T |
| CVE-2026-96762 | 7.3 | 2026-09-24 | A vulnerability was determined in kvcache-ai mooncake up to 0.3.12/0.3.13.post1. This affects the function UnmountSegmen |
| CVE-2026-18467 | 9.8 | 2026-09-24 | The Paytium: Mollie payment forms & donations plugin for WordPress is vulnerable to Privilege Escalation in all versions |
| CVE-2026-96803 | 7.3 | 2026-09-24 | A vulnerability was identified in java110 MicroCommunity up to 2.0. Affected is the function QueryServiceSMOImpl.fallBac |
| CVE-2026-97055 | 8.1 | 2026-09-24 | SigNoz from v0.8.0 before v0.143.0 defaults the JWT tokenizer signing secret (tokenizer::jwt::secret, set via SIGNOZ_TOK |
| CVE-2026-96891 | 9.8 | 2026-09-24 | A vulnerability was identified in D-Link DIR-825 3.00b32. Affected is the function tunnel_set_params of the file tunnel. |
| CVE-2026-96898 | 7.3 | 2026-09-24 | A vulnerability was detected in yhx070424 ShopXO up to 2.2.7. Affected by this vulnerability is an unknown functionality |
| CVE-2026-80513 | 7.5 | 2026-09-24 | The wpForo Forum WordPress plugin before 3.1.6 does not restrict which classes may be instantiated when it deserializes  |
| CVE-2026-88843 | 7.2 | 2026-09-24 | The MasterStudy LMS WordPress Plugin  WordPress plugin before 3.7.50 does not validate one of its display-style settings |
| CVE-2026-77193 | 7.5 | 2026-09-24 | The eesy_ID2WP – Publish InDesign HTML5 plugin for WordPress is vulnerable to Path Traversal in all versions up to, and  |
| CVE-2026-78308 | 9.8 | 2026-09-24 | Improper Authentication vulnerability in DIAEnergie allows Authentication Bypass.

This issue affects DIAEnergie: before |
| CVE-2026-78309 | 8.8 | 2026-09-24 | SQL Injection vulnerability in DIAEnergie.

This issue affects DIAEnergie: before 1.11.00.022. |
| CVE-2026-78311 | 8.8 | 2026-09-24 | SQL Injection vulnerability in DIAEnergie.

This issue affects DIAEnergie: before 1.11.00.022. |
| CVE-2026-78312 | 9.1 | 2026-09-24 | Path Traversal in DIAEnergie.

This issue affects DIAEnergie: before 1.11.00.022. |
| CVE-2026-85682 | 8.8 | 2026-09-24 | The YOP Poll plugin for WordPress is vulnerable to Origin Validation Error in all versions up to, and including, 7.0.10. |
| CVE-2026-97185 | 7.8 | 2026-09-24 | A flaw was found in GIMP. When processing a specially crafted GIMPressionist preset file, the plug-in does not properly  |
| CVE-2026-12227 | 9.8 | 2026-09-24 | The Visual Composer Website Builder plugin for WordPress is vulnerable to Local File Inclusion in all versions up to, an |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-93952 | Arista / VeloCloud Orchestrator | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-94127 | F5 / BIG-IP APM | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-93616 | Check Point / Multiple Products | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-85102 | Check Point / Multiple Products | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-7273 | Zyxel / GS1900 Series Switches | 2026-09-21 | 2026-09-24 | Unknown |
| CVE-2025-39964 | Linux / Kernel | 2026-09-18 | 2026-09-21 | Unknown |
| CVE-2026-53266 | Linux / Kernel | 2026-09-18 | 2026-09-21 | Unknown |
| CVE-2025-39682 | Linux / Kernel | 2026-09-18 | 2026-09-21 | Unknown |

---

*Total entries in CISA KEV catalog: 1721*