# Vulnerability Intelligence Report

**Date:** 2026-10-06  
**Generated:** 2026-10-06T14:45:29Z  

---

## Executive Summary

Our environment faces significant cybersecurity risk from 245 high-severity vulnerabilities, including multiple critical CVSS 9.8-rated flaws enabling SQL injection and unauthenticated access. Six new actively exploited vulnerabilities were added to CISA's Known Exploited Vulnerabilities catalog this week, affecting widely deployed products including Citrix NetScaler, Fortinet FortiMail, and Cisco SD-WAN. While none of our monitored CVEs currently appear in the KEV catalog, the volume and severity of newly disclosed vulnerabilities demand immediate prioritization and response to prevent potential compromise of critical systems and sensitive data.

---

## Risk Narrative

The current threat landscape reflects a surge in critical vulnerabilities targeting enterprise infrastructure, open-source platforms, and web applications. Attackers are actively exploiting flaws in Citrix, Fortinet, and Cisco products—all confirmed in CISA's KEV catalog—indicating organized, opportunistic threat activity. SQL injection, authentication bypass, and remote code execution vulnerabilities dominate this week's disclosures, exposing organizations to data breaches, ransomware deployment, and operational disruption. Industries relying on CMS platforms, trading systems, and hospital management software face elevated risk. If left unaddressed, these vulnerabilities could result in regulatory penalties, reputational damage, and significant financial losses.

---

## Prioritized Action Items

1. Immediately audit and patch or isolate HPE iLO 7 firmware and any Citrix NetScaler, Fortinet FortiMail, and Cisco SD-WAN Manager systems to remediate actively exploited KEV vulnerabilities.
2. Prioritize patching the two CVSS 9.8 vulnerabilities—CVE-2026-88391 (H2 Console exposure) and CVE-2026-88395 (SQL Injection in GouGuOA)—as they allow full system compromise.
3. Conduct an emergency inventory of all externally facing applications to identify exposure to the 245 high-severity CVEs and enforce network segmentation where patching is not immediately possible.
4. Update vulnerability monitoring rules to include all six new KEV entries and configure automated alerting if any monitored assets match future KEV additions.
5. Establish a 72-hour SLA for critical and high-severity CVE remediation and report compliance metrics to leadership weekly to reduce organizational risk exposure.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-79820 | 9.0 | 2026-10-05 | A remote user validation failure vulnerability exists in HPE Integrated Lights-Out (iLO) 7 firmware. |
| CVE-2026-88391 | 9.8 | 2026-10-05 | Northstar (dromara/northstar, quantitative trading platform) <= 9.1.1 enables the H2 Console but its auth interceptor on |
| CVE-2026-104890 | 7.2 | 2026-10-05 | Kunstmaan CMS is an open source content management system based on the Symfony framework. Prior to 7.3.2, src/Kunstmaan/ |
| CVE-2026-104891 | 7.5 | 2026-10-05 | mppx-condition-gate provides conditional free-access wrappers for mppx payment methods. Prior to @insumermodel/mppx-cond |
| CVE-2026-88395 | 9.8 | 2026-10-05 | GouGuOA v6.0.5 and before is vulnerable to SQL Injection in /home/message/rubbish via the keywords parameter. |
| CVE-2026-102282 | 7.1 | 2026-10-05 | adm-zip is a JavaScript library for creating and extracting ZIP archives in Node.js. Prior to 0.6.1, adm-zip applies the |
| CVE-2026-104970 | 8.1 | 2026-10-05 | Plane is an open-source project management tool. From 0.13 until 1.4.0, InstanceAdminSignUpEndpoint in apps/api/plane/li |
| CVE-2026-105382 | 7.3 | 2026-10-05 | A flaw has been found in onetwothreeneth HospitalManagementSystem up to 9ef91ed6007314b6473110ed699dff76d158f61d. This a |
| CVE-2026-105383 | 7.3 | 2026-10-05 | A vulnerability has been found in onetwothreeneth HospitalManagementSystem up to 9ef91ed6007314b6473110ed699dff76d158f61 |
| CVE-2026-12171 | 7.8 | 2026-10-05 | auto-changelog before 2.6.1 merges configuration from inside the target repository (the .auto-changelog file and the aut |
| CVE-2025-15643 | 7.1 | 2026-10-05 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Jose Fernandez Ads |
| CVE-2026-101919 | 8.8 | 2026-10-05 | A flaw was found in the HyperShift operator. The operator copies user-provided Kubernetes configuration (kubeconfig) sec |
| CVE-2026-104905 | 8.1 | 2026-10-05 | FacturaScripts before version 2026.7 contains a PHP object injection vulnerability in WidgetSelect::processFormData() th |
| CVE-2026-104971 | 8.5 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, DuplicateAssetEndpoint fetches a source FileAsset witho |
| CVE-2026-104973 | 7.6 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, the fix for CVE-2026-30242 validates webhook IP address |
| CVE-2026-104974 | 8.1 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, a user whose account has been deactivated by setting is |
| CVE-2026-104975 | 7.1 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, Plane's dashboard asset endpoints in plane/app/views/as |
| CVE-2026-104977 | 7.7 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, the fix for CVE-2026-27706 and GHSA-jcc6-f9v6-f7jw, an  |
| CVE-2026-104978 | 8.2 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, Plane's project invitation list endpoint is accessible  |
| CVE-2026-104979 | 8.7 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, IntakeIssuePublicViewSet.create in Plane v1.3.1 writes  |
| CVE-2026-105384 | 7.3 | 2026-10-05 | A vulnerability was found in UNION HospitalManagementSystem up to 9ef91ed6007314b6473110ed699dff76d158f61d. Affected is  |
| CVE-2026-105385 | 7.3 | 2026-10-05 | A vulnerability was determined in onetwothreeneth HospitalManagementSystem up to 9ef91ed6007314b6473110ed699dff76d158f61 |
| CVE-2026-105628 | 7.6 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, Plane's OAuth avatar synchronization flow fetches avata |
| CVE-2026-105629 | 7.1 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, BulkEstimatePointEndpoint.destroy resolves an estimate  |
| CVE-2026-105630 | 8.7 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, an authenticated low-privilege workspace member, includ |
| CVE-2026-105631 | 7.5 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, WorkspaceFileAssetEndpoint.get and WorkspaceAssetDownlo |
| CVE-2026-105633 | 7.1 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, the V2 issue-attachment PATCH endpoint accepts issue_id |
| CVE-2026-100515 | 7.1 | 2026-10-05 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in VillaTheme Photo R |
| CVE-2026-103334 | 7.5 | 2026-10-05 | Insertion of Sensitive Information Into Sent Data vulnerability in Etoile Web Design Incorporated Five Star Restaurant R |
| CVE-2026-103349 | 7.2 | 2026-10-05 | Deserialization of Untrusted Data vulnerability in Rymera Web Co Product Feed PRO for WooCommerce woo-product-feed-pro a |
| CVE-2026-103352 | 9.3 | 2026-10-05 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in WP BASE WP BASE Bo |
| CVE-2026-105386 | 7.3 | 2026-10-05 | A vulnerability was identified in onetwothreeneth HospitalManagementSystem up to 9ef91ed6007314b6473110ed699dff76d158f61 |
| CVE-2026-105387 | 7.3 | 2026-10-05 | A security flaw has been discovered in girishsaraf Online-Appointment-Booking-System up to f427b4757128ca253d33d0cc4e87b |
| CVE-2026-105634 | 8.1 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.3.0, the ProjectMemberViewSet.partial_update method allows a |
| CVE-2026-105635 | 7.4 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, ProjectJoinEndpoint at GET /api/workspaces/{slug}/proje |
| CVE-2026-105636 | 9.9 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, the webhook delivery task in apps/api/plane/bgtasks/web |
| CVE-2026-105637 | 9.6 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, ProjectBulkAssetEndpoint.post in apps/api/plane/app/vie |
| CVE-2026-105638 | 9.1 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, Plane's magic-code email login uses a six-digit numeric |
| CVE-2026-105639 | 9.8 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, Plane's signup flow creates a logged-in User row for an |
| CVE-2026-105640 | 9.1 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, Plane trusts email addresses returned by Gitea OAuth an |
| CVE-2026-105641 | 9.8 | 2026-10-05 | Plane is an open-source project management tool. Prior to 1.4.0, the deployments/aio/community/ and deployments/cli/comm |
| CVE-2026-105642 | 8.8 | 2026-10-05 | Ghost is a Node.js content management system. From 6.56.0 until 6.67.0, an image processing library bundled with Ghost c |
| CVE-2026-105643 | 7.3 | 2026-10-05 | Ghost is a Node.js content management system. From version 6.34.0 until 6.67.0, embed cards in the Ghost editor could by |
| CVE-2026-28625 | 7.8 | 2026-10-05 | In multiple locations, there is a possible permission bypass due to a logic error in the code. This could lead to local  |
| CVE-2026-28640 | 7.8 | 2026-10-05 | In checkCallerIsCertInstallerOrSelfInProfile of CredentialStorageActivity.java, there is a possible permission bypass du |
| CVE-2026-28641 | 7.8 | 2026-10-05 | In shouldDisableUninstallButton of ApplicationActionButtonsPreferenceController.java, there is a possible permission byp |
| CVE-2026-28647 | 7.8 | 2026-10-05 | In updateState of DeviceAdminAppsPreferenceController.java, there is a possible permission bypass due to a logic error i |
| CVE-2026-28648 | 7.8 | 2026-10-05 | In Settings, there is a possible permission bypass due to a confused deputy. This could lead to local escalation of priv |
| CVE-2026-45524 | 8.8 | 2026-10-05 | In isSystem of WifiPermissionsUtil.java, there is a possible sandbox escape due to a missing permission check. This coul |
| CVE-2026-49878 | 7.2 | 2026-10-05 | In wpas_handle_robust_av_scs_recv_action of robust_av.c, there is a possible out-of-bounds write due to a logic error in |
| CVE-2026-49885 | 7.8 | 2026-10-05 | In rw_t4t_update_file of rw_t4t.cc, there is a possible out-of-bounds write due to an integer overflow. This could lead  |
| CVE-2026-49933 | 7.8 | 2026-10-05 | In handle_le_monitor_device_event of msft.cc, there is a possible control-flow hijack in the privileged bluetooth proces |
| CVE-2026-49937 | 7.8 | 2026-10-05 | In multiple functions of MessageQueueBase.h, there is a possible out of bounds read due to an incorrect bounds check. Th |
| CVE-2026-55266 | 7.8 | 2026-10-05 | In qsort of libufdt_sysdeps_vendor.c, there is a possible out-of-bounds write due to resource exhaustion. This could lea |
| CVE-2026-55269 | 7.8 | 2026-10-05 | In FilterCapturedPacket of snoop_logger.cc, there is a possible memory safety issue due to improper input validation. Th |
| CVE-2026-55270 | 7.8 | 2026-10-05 | In dialInternal in multiple locations, there is a possible permission bypass due to a confused deputy. This could lead t |
| CVE-2026-55280 | 8.8 | 2026-10-05 | In multiple locations, there is a possible out-of-bounds write due to uninitialized data. This could lead to remote esca |
| CVE-2026-55286 | 7.8 | 2026-10-05 | In stpropnci_process of stpropnci.cc, there is a possible out of bounds write due to an incorrect bounds check. This cou |
| CVE-2026-58815 | 7.8 | 2026-10-05 | In multiple locations, there is a possible out of bounds write due to an incorrect bounds check. This could lead to loca |
| CVE-2026-58835 | 8.8 | 2026-10-05 | In cfg2prop of btif_storage.cc, there is a possible out-of-bounds write due to a heap buffer overflow. This could lead t |
| CVE-2026-58841 | 7.8 | 2026-10-05 | In multiple functions of VirtualAudioControllerTest.java, there is a possible permission bypass due to a logic error in  |
| CVE-2026-58854 | 7.8 | 2026-10-05 | In multiple locations, there is a possible memory corruption due to type confusion. This could lead to local escalation  |
| CVE-2026-58859 | 7.8 | 2026-10-05 | In multiple places, there is a possible  denial of service due to an uncaught exception. This could lead to local escala |
| CVE-2026-58865 | 7.5 | 2026-10-05 | In multiple functions of PduParser.java, there is a possible persistent denial of service due to a missing bounds check. |
| CVE-2026-58880 | 7.0 | 2026-10-05 | In handle_app_val_response of btif_rc.cc, there is a possible way to achieve code execution due to a race condition. Thi |
| CVE-2026-97283 | 9.8 | 2026-10-05 | Deserialization of Untrusted Data vulnerability in Liquid Web / StellarWP Advanced Post Manager advanced-post-manager al |
| CVE-2026-97303 | 7.6 | 2026-10-05 | Missing Authorization vulnerability in Apps Mav Scratch & Win – Giveaways and Contests scratch-win-giveaways-for-website |
| CVE-2026-100506 | 7.2 | 2026-10-05 | Deserialization of Untrusted Data vulnerability in WP Spell Check WP Spell Check wp-spell-check allows Object Injection. |
| CVE-2026-100511 | 8.8 | 2026-10-05 | Deserialization of Untrusted Data vulnerability in Vektor Inc. VK Google Job Posting Manager vk-google-job-posting-manag |
| CVE-2026-103066 | 8.5 | 2026-10-05 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in WP BASE WP BASE Bo |
| CVE-2026-103348 | 7.2 | 2026-10-05 | Deserialization of Untrusted Data vulnerability in Smackcoders Inc. WP Ultimate Exporter wp-ultimate-exporter allows Obj |
| CVE-2026-105392 | 7.3 | 2026-10-05 | A vulnerability has been found in Lybbn Django-Vue-Lyadmin up to 3.2.12. The impacted element is an unknown function of  |
| CVE-2026-105649 | 7.3 | 2026-10-05 | Ghost is a Node.js content management system. From 4.22.0 until 6.65.0, SVG media thumbnails and SVG images uploaded wit |
| CVE-2026-105650 | 8.1 | 2026-10-05 | Ghost is a Node.js content management system. From 2.1.0 until 6.64.0, embedding a URL from an attacker-controlled websi |
| CVE-2026-105651 | 7.3 | 2026-10-05 | Ghost is a Node.js content management system. From 5.94.0 until 6.64.0, when creating a bookmark card, Ghost could store |
| CVE-2026-105675 | 7.5 | 2026-10-05 | Ghost is a Node.js content management system. From 4.39.0 until 6.64.0, staff users with permission to view staff invite |
| CVE-2026-105677 | 7.2 | 2026-10-05 | Ghost is a Node.js content management system. From 6.10.3 until 6.64.0, a vulnerability in how Ghost loads theme transla |
| CVE-2026-105679 | 7.3 | 2026-10-05 | Ghost is a Node.js content management system. From 6.22.1 until 6.64.0, Ghost restricted the content type used to serve  |
| CVE-2026-105691 | 9.9 | 2026-10-05 | Penpot is an open-source design and prototyping platform. Prior to 2.18.0, the SVG exporter places an attacker-controlle |
| CVE-2026-93617 | 7.2 | 2026-10-05 | Deserialization of Untrusted Data vulnerability in WP Sunshine Sunshine Photo Cart sunshine-photo-cart allows Object Inj |
| CVE-2026-95263 | 7.2 | 2026-10-05 | Feehi CMS 2.1.1 is vulnerable to Incorrect Access Control. A low-privilege backend administrator with administrator-upda |
| CVE-2026-97257 | 8.8 | 2026-10-05 | Deserialization of Untrusted Data vulnerability in PressTigers Simple Event Planner simple-event-planner allows Object I |
| CVE-2026-102262 | 7.3 | 2026-10-05 | Newell Brands DYMO ID 1.5.1.71 resolves its plugin Modules directory relative to the process working directory. An attac |
| CVE-2026-105697 | 9.9 | 2026-10-05 | Langflow is a tool for building and deploying AI-powered agents and workflows. Before Langflow 1.10.3, the MCP stdio tra |
| CVE-2026-105740 | 9.9 | 2026-10-05 | Langflow is a tool for building and deploying AI-powered agents and workflows. Prior to 1.9.0, any authenticated Langflo |
| CVE-2026-105741 | 7.1 | 2026-10-05 | Langflow is a tool for building and deploying AI-powered agents and workflows. From 1.5.0 until 1.10.3, an IP spoofing v |
| CVE-2026-105773 | 7.0 | 2026-10-05 | Canimaan Software ClamXAV versions 3.3 - 3.11 contains a local privilege escalation vulnerability in the Privileged Help |
| CVE-2026-77226 | 8.1 | 2026-10-05 | Camunda 7.24.0 before 7.24.15 contains an incorrect authorization vulnerability in the Admin web application's first-run |
| CVE-2026-105468 | 7.3 | 2026-10-05 | A vulnerability was found in girishsaraf Online-Appointment-Booking-System up to f427b4757128ca253d33d0cc4e87bbb9c999a4d |
| CVE-2026-105744 | 7.5 | 2026-10-05 | Docling simplifies document processing by parsing diverse formats and providing integrations with the generative AI ecos |
| CVE-2026-105469 | 7.3 | 2026-10-05 | A vulnerability was determined in girishsaraf Online-Appointment-Booking-System up to f427b4757128ca253d33d0cc4e87bbb9c9 |
| CVE-2026-105470 | 7.3 | 2026-10-05 | A vulnerability was identified in girishsaraf Online-Appointment-Booking-System up to f427b4757128ca253d33d0cc4e87bbb9c9 |
| CVE-2026-105761 | 7.1 | 2026-10-05 | Dify is an open-source LLM app development platform. Prior to 1.16.0, the PUT /console/api/apps/&lt;app_id&gt;/server en |
| CVE-2026-105471 | 7.3 | 2026-10-06 | A security flaw has been discovered in girishsaraf Online-Appointment-Booking-System up to f427b4757128ca253d33d0cc4e87b |
| CVE-2026-105762 | 8.3 | 2026-10-06 | Dify is an open-source LLM app development platform. Prior to 1.13.0, the /console/api/remote-files/upload endpoint in a |
| CVE-2026-105763 | 9.6 | 2026-10-06 | Twenty is an open-source CRM (customer relationship management) platform. From 1.20.10 until 2.7.0, the /metadata GraphQ |
| CVE-2026-105782 | 7.5 | 2026-10-06 | Scrapy is a high-level web crawling and scraping framework for Python. From 1.4.0 until 2.14.2, RefererMiddleware in scr |
| CVE-2026-105783 | 8.0 | 2026-10-06 | Joplin is an open source note-taking and to-do application that organises notes and lists into notebooks. Prior to 3.7.1 |
| CVE-2026-82988 | 7.5 | 2026-10-06 | There exists an arbitrary file download in vCast APK delivery mechanism in ViewSonic ViewBoard unknown allows a remote,  |
| CVE-2026-82989 | 9.8 | 2026-10-06 | There is an input injection in vCast exposed network services in ViewSonic ViewBoard that allows a remote, unauthenticat |
| CVE-2026-105484 | 10.0 | 2026-10-06 | A security vulnerability has been detected in TOTOLINK X6000R 9.4.0cu.652_B20230116. The impacted element is the functio |
| CVE-2026-105486 | 7.3 | 2026-10-06 | A vulnerability was detected in OSSRS srs up to 7.0-a1. This affects the function systemAPI.Run of the file internal/pro |
| CVE-2026-105571 | 7.3 | 2026-10-06 | A flaw has been found in PickMall Lilishop up to 4.2.4. The impacted element is an unknown function of the file /buyer/p |
| CVE-2026-105704 | 7.3 | 2026-10-06 | A vulnerability was identified in SourceCodester Drug Recommendation System 1.0. This affects an unknown function of the |
| CVE-2026-105072 | 7.5 | 2026-10-06 | Unauthenticated Broken Access Control in FluentBooking Pro < 2.5.0 versions. |
| CVE-2026-39723 | 7.5 | 2026-10-06 | Unauthenticated Broken Access Control in Morning for WooCommerce <= 2.4.1 versions. |
| CVE-2026-39760 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Real 3D FlipBook <= 5.5 versions. |
| CVE-2026-39789 | 7.5 | 2026-10-06 | Unauthenticated Broken Access Control in Fluent Affiliate Pro <= 1.6.4 versions. |
| CVE-2026-41558 | 7.5 | 2026-10-06 | Subscriber Bypass Vulnerability in WP Migration Plugin DB & Files – WP Synchro <= 1.16.1 versions. |
| CVE-2026-41563 | 7.5 | 2026-10-06 | Unauthenticated Sensitive Data Exposure in Sitemovr <= 1.0.1 versions. |
| CVE-2026-75962 | 7.2 | 2026-10-06 | The Post SMTP – Complete Email Deliverability and SMTP Solution with Email Logs, Alerts, Backup SMTP & Mobile App plugin |
| CVE-2026-105701 | 8.8 | 2026-10-06 | The ACPT (Premium) plugin for WordPress is vulnerable to Remote Code Execution in all versions up to, and including, 2.0 |
| CVE-2026-105776 | 7.3 | 2026-10-06 | A flaw has been found in bhagya3929 Employee-Movement-Tracking-and-Monitoring-Website-for-IOCL up to ae783195ba7e0390d3b |
| CVE-2026-105778 | 9.9 | 2026-10-06 | A vulnerability has been found in Tenda AC5 02.03.01.111_multi. Affected by this issue is some unknown functionality of  |
| CVE-2026-25267 | 7.8 | 2026-10-06 | Memory corruption when non-secure loader rewrites page tables before secure memory initialization. |
| CVE-2026-25291 | 7.8 | 2026-10-06 | Memory corruption when performing concurrent operations on shared memory page lists due to lack of proper synchronizatio |
| CVE-2026-25302 | 7.1 | 2026-10-06 | Cryptographic Issue when processing non-ELF partitions, authentication and signature checks are bypassed, allowing unsig |
| CVE-2026-57537 | 7.8 | 2026-10-06 | Memory Corruption when accessing and modifying geographic mapping data concurrently without proper synchronization. |
| CVE-2026-57545 | 7.8 | 2026-10-06 | Memory corruption when processing draw objects of incorrect type during graphics command list execution. |
| CVE-2026-57546 | 7.5 | 2026-10-06 | Transient DOS when processing a continuous receive command with a zero-sized global configuration override. |
| CVE-2026-57554 | 7.8 | 2026-10-06 | Memory Corruption when asynchronous threads access shared performance counter data simultaneously during FastRPC invocat |
| CVE-2026-57555 | 7.8 | 2026-10-06 | Memory Corruption when executing system service routines due to improper handling of user input buffers. |
| CVE-2026-57559 | 7.8 | 2026-10-06 | Memory corruption while processing service requests. |
| CVE-2026-94293 | 9.8 | 2026-10-06 | An unauthenticated remote attacker can modify Asset Administration Shell submodel data via PATCH requests and can read a |
| CVE-2026-105807 | 7.3 | 2026-10-06 | A vulnerability was found in SourceCodester Simple Student Information System 1.0. This affects an unknown part of the f |
| CVE-2026-102387 | 7.5 | 2026-10-06 | Unauthenticated Sensitive Data Exposure in Xserver Migrator <= 1.6.6 versions. |
| CVE-2026-102915 | 8.5 | 2026-10-06 | Subscriber Broken Access Control in WPO365 <= 44.1 versions. |
| CVE-2026-103346 | 7.1 | 2026-10-06 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Tomlister Payflex  |
| CVE-2026-104385 | 7.5 | 2026-10-06 | Unauthenticated Sensitive Data Exposure in Groundhogg <= 4.8.3 versions. |
| CVE-2026-104387 | 7.2 | 2026-10-06 | Unauthenticated Broken Access Control in PowerPress Podcasting <= 11.17.9 versions. |
| CVE-2026-104394 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Charitable <= 1.8.12.3 versions. |
| CVE-2026-104395 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in picu <= 3.10.1 versions. |
| CVE-2026-104405 | 8.1 | 2026-10-06 | Unauthenticated Privilege Escalation in GiveWP <= 4.17.0 versions. |
| CVE-2026-104406 | 7.3 | 2026-10-06 | Unauthenticated Broken Access Control in picu <= 3.10.1 versions. |
| CVE-2026-104670 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in LearnPress <= 4.4.9 versions. |
| CVE-2026-104672 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in GiveWP <= 4.17.0 versions. |
| CVE-2026-104747 | 8.1 | 2026-10-06 | Unauthenticated PHP Object Injection in Haaken <= 1.5 versions. |
| CVE-2026-104757 | 7.2 | 2026-10-06 | Editor Privilege Escalation in Import and export users and customers <= 2.5.5 versions. |
| CVE-2026-104814 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Form Block <= 1.8.1 versions. |
| CVE-2026-105058 | 8.8 | 2026-10-06 | Subscriber Privilege Escalation in WP User Profiles <= 2.7.3 versions. |
| CVE-2026-105061 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in WP Mailster <= 1.9.0.0 versions. |
| CVE-2026-105070 | 8.8 | 2026-10-06 | Unauthenticated Privilege Escalation in Salon booking system <= 10.31.7 versions. |
| CVE-2026-105071 | 7.5 | 2026-10-06 | Unauthenticated Sensitive Data Exposure in SiteVault – Backup, Restore, Migration &amp; Cloning <= 1.5.17 versions. |
| CVE-2026-105317 | 8.5 | 2026-10-06 | Subscriber SQL Injection in Paid Member Subscriptions <= 3.1.1 versions. |
| CVE-2026-25433 | 7.1 | 2026-10-06 | Subscriber Broken Access Control in WP2LEADS <= 3.5.7 versions. |
| CVE-2026-25434 | 8.5 | 2026-10-06 | Subscriber SQL Injection in WP2LEADS <= 3.5.7 versions. |
| CVE-2026-32557 | 9.3 | 2026-10-06 | Unauthenticated SQL Injection in WooCommerce Appointments <= 5.3.2 versions. |
| CVE-2026-32568 | 9.9 | 2026-10-06 | Subscriber Remote Code Execution (RCE) in WooCommerce Designer Pro <= 1.9.33 versions. |
| CVE-2026-32569 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in WP Media folder <= 6.2.2 versions. |
| CVE-2026-32570 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Progressify - Progressive Web App (PWA) <= 1.6.0 versions. |
| CVE-2026-32572 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in WP User Frontend Pro <= 4.2.13 versions. |
| CVE-2026-32574 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Smart Forms <= 2.6.104 versions. |
| CVE-2026-32575 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in SUMO Affiliates Pro <= 11.7.0 versions. |
| CVE-2026-32577 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Frontend File Manager <= 23.6 versions. |
| CVE-2026-32578 | 7.1 | 2026-10-06 | Subscriber Broken Access Control in ECPay Ecommerce for WooCommerce <= 1.1.2606090 versions. |
| CVE-2026-32579 | 10.0 | 2026-10-06 | Unauthenticated Arbitrary File Upload in Kognetiks Chatbot for WordPress <= 2.4.9 versions. |
| CVE-2026-32580 | 7.5 | 2026-10-06 | Unauthenticated SQL Injection in WooCommerce Lottery <= 2.2.9 versions. |
| CVE-2026-32581 | 7.1 | 2026-10-06 | Subscriber SQL Injection in Mooberry Book Manager 4.16.2 versions. |
| CVE-2026-39719 | 7.2 | 2026-10-06 | Unauthenticated Server Side Request Forgery (SSRF) in PDF Smart Viewer for Elementor <= 1.0.4 versions. |
| CVE-2026-39720 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Mapster WP Maps <= 2.0.4 versions. |
| CVE-2026-39722 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in WPLMS  <= 4.972 versions. |
| CVE-2026-39724 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in HTTP Requests Manager <= 1.3.11 versions. |
| CVE-2026-39725 | 8.8 | 2026-10-06 | Contributor Remote Code Execution (RCE) in Content Visibility for Divi Builder <= 5.03 versions. |
| CVE-2026-39726 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Lumise Product Designer <= 2.1.1 versions. |
| CVE-2026-39728 | 7.2 | 2026-10-06 | Unauthenticated Server Side Request Forgery (SSRF) in Instapage Plugin <= 3.7.2 versions. |
| CVE-2026-39729 | 7.2 | 2026-10-06 | Unauthenticated Sensitive Data Exposure in Edwiser Bridge <= 4.3.4 versions. |
| CVE-2026-39730 | 7.1 | 2026-10-06 | Missing Authorization vulnerability in Marcin Wise Chat wise-chat allows Exploiting Incorrectly Configured Access Contro |
| CVE-2026-39731 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Database for CF7 <= 1.2.6 versions. |
| CVE-2026-39745 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Contact Form to DB by BestWebSoft <= 1.7.6 versions. |
| CVE-2026-39746 | 9.3 | 2026-10-06 | Unauthenticated SQL Injection in Booknetic <= 4.8.5 versions. |
| CVE-2026-39747 | 8.5 | 2026-10-06 | Subscriber SQL Injection in Woffice <= 5.4.35 versions. |
| CVE-2026-39748 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in EduMall <= 4.5.3 versions. |
| CVE-2026-39750 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in StoreGrowth: Smart Sales Booster for WooCommerce \| BOGO, Upsells, Direct C |
| CVE-2026-39751 | 7.5 | 2026-10-06 | Unauthenticated Broken Access Control in PayPlug for WooCommerce (Official) <= 3.1.0 versions. |
| CVE-2026-39752 | 7.7 | 2026-10-06 | Contributor Arbitrary File Deletion in Jobs for WordPress <= 2.8.2 versions. |
| CVE-2026-39753 | 9.8 | 2026-10-06 | Unauthenticated Privilege Escalation in Taskbot <= 6.6 versions. |
| CVE-2026-39755 | 9.9 | 2026-10-06 | Subscriber Arbitrary File Upload in WP Duplicate <= 1.1.11 versions. |
| CVE-2026-39757 | 9.9 | 2026-10-06 | Subscriber Arbitrary File Upload in Taskbot <= 6.6 versions. |
| CVE-2026-39758 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Midtrans-WooCommerce <= 2.32.3 versions. |
| CVE-2026-39759 | 9.9 | 2026-10-06 | Employer / Sales Representative Arbitrary File Upload in Workreap Core <= 3.4.5 versions. |
| CVE-2026-39761 | 9.8 | 2026-10-06 | Unauthenticated Privilege Escalation in Meta Box AIO <= 3.7.1 versions. |
| CVE-2026-39764 | 9.3 | 2026-10-06 | Unauthenticated SQL Injection in Radius Booking — Booking Calendar for Appointments &amp; Services <= 1.0.19 versions. |
| CVE-2026-39765 | 7.2 | 2026-10-06 | Shop Manager Privilege Escalation in Challan <= 3.7.88 versions. |
| CVE-2026-39766 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in ARForms <= 7.1.2 versions. |
| CVE-2026-39768 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Security & Malware scan by CleanTalk <= 2.189 versions. |
| CVE-2026-39769 | 7.5 | 2026-10-06 | Unauthenticated Broken Authentication in Graphina <= 3.1.12 versions. |
| CVE-2026-39770 | 10.0 | 2026-10-06 | Unauthenticated Arbitrary File Upload in Doctreat <= 1.7.0 versions. |
| CVE-2026-39771 | 8.5 | 2026-10-06 | Subscriber SQL Injection in Buddyboss Platform <= 3.1.0 versions. |
| CVE-2026-39773 | 10.0 | 2026-10-06 | Unauthenticated Privilege Escalation in Doctreat Core <= 1.7.0 versions. |
| CVE-2026-39774 | 8.8 | 2026-10-06 | Unauthenticated Privilege Escalation in Tourfic Pro <= 1.17.3 versions. |
| CVE-2026-39775 | 8.8 | 2026-10-06 | Subscriber Privilege Escalation in JobZilla - Job Board WordPress Theme <= 2.2 versions. |
| CVE-2026-39776 | 8.0 | 2026-10-06 | Editor Remote Code Execution (RCE) in Tabs <= 2.5 versions. |
| CVE-2026-39778 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Ansar Import – One Click Starter Sites – for Elementor &amp; Themes <= 2.1 |
| CVE-2026-39780 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Youzify <= 1.3.7 versions. |
| CVE-2026-39781 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Document Gallery <= 5.1.1 versions. |
| CVE-2026-39784 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Hotel Booking <= 3.8 versions. |
| CVE-2026-39785 | 9.3 | 2026-10-06 | Unauthenticated SQL Injection in Gmedia Photo Gallery <= 1.25.1 versions. |
| CVE-2026-39790 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in VikRentCar <= 1.4.6 versions. |
| CVE-2026-39792 | 8.6 | 2026-10-06 | Unauthenticated Arbitrary File Deletion in Simple File List <= 6.3.11 versions. |
| CVE-2026-39793 | 8.8 | 2026-10-06 | Subscriber Broken Authentication in Simple JWT Login 4.0.0 versions. |
| CVE-2026-39794 | 7.5 | 2026-10-06 | Unauthenticated Broken Access Control in WooCommerce Multivendor Marketplace – REST API <= 1.6.3 versions. |
| CVE-2026-39795 | 9.3 | 2026-10-06 | Unauthenticated SQL Injection in SendPress Newsletters <= 1.26.1.20 versions. |
| CVE-2026-39796 | 7.5 | 2026-10-06 | Unauthenticated Broken Access Control in Advanced Posts Listing – Show Post List Easily <= 1.0.8 versions. |
| CVE-2026-39797 | 9.8 | 2026-10-06 | Unauthenticated PHP Object Injection in GDPR Framework By Data443 <= 2.5.0 versions. |
| CVE-2026-40806 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Blog, Posts and Category Filter for Elementor <= 2.1.0 versions. |
| CVE-2026-40807 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in CF7 Views &#8211; Complete Entry Management for Contact Form 7 <= 3.2.6 ve |
| CVE-2026-41555 | 9.3 | 2026-10-06 | Unauthenticated SQL Injection in Newsletter Subscription Form – User Subscriptions Form, Capture Email <= 1.5.9 versions |
| CVE-2026-41559 | 7.5 | 2026-10-06 | Unauthenticated Sensitive Data Exposure in SafeSnap – Verified WordPress Backup &amp; Restore <= 2.1.2 versions. |
| CVE-2026-41560 | 7.5 | 2026-10-06 | Unauthenticated Broken Access Control in WXD Backup Lite <= 1.0.2 versions. |
| CVE-2026-41561 | 7.5 | 2026-10-06 | Unauthenticated Sensitive Data Exposure in Museder RestoreOne <= 2.7.276 versions. |
| CVE-2026-41562 | 7.5 | 2026-10-06 | Unauthenticated Sensitive Data Exposure in Norvis Backup <= 1.1.0 versions. |
| CVE-2026-42413 | 7.5 | 2026-10-06 | Unauthenticated Sensitive Data Exposure in Snapshotify &#8211; All-in-One Backup &amp; Restore &amp; Migrate <= 1.3.2 ve |
| CVE-2026-42414 | 8.5 | 2026-10-06 | Subscriber SQL Injection in ListingPro <= 2.9.12 versions. |
| CVE-2026-42415 | 9.3 | 2026-10-06 | Unauthenticated SQL Injection in Porto Theme - Functionality <= 3.9.3 versions. |
| CVE-2026-42416 | 8.5 | 2026-10-06 | Subscriber SQL Injection in UDesign Core <= 4.15.0 versions. |
| CVE-2026-42417 | 9.3 | 2026-10-06 | Unauthenticated SQL Injection in ARMember Premium <= 7.8 versions. |
| CVE-2026-42418 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Social Rocket <= 1.3.5 versions. |
| CVE-2026-42634 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Video Background Block – Use video as background in the section. <= 2.0.3  |
| CVE-2026-42635 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in WooCommerce Simple Auctions <= 3.0.10 versions. |
| CVE-2026-42636 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in WP Cookie Notice for GDPR, CCPA & ePrivacy Consent <= 4.4.6 versions. |
| CVE-2026-42638 | 7.5 | 2026-10-06 | Unauthenticated Broken Access Control in Easy Digital Downloads <= 3.7.1 versions. |
| CVE-2026-48197 | 7.2 | 2026-10-06 | Incorrect Privilege Assignment vulnerability in PublishPress PublishPress Capabilities capability-manager-enhanced allow |
| CVE-2026-48199 | 7.5 | 2026-10-06 | Unauthenticated Broken Access Control in Sermon'e <= 1.0.2 versions. |
| CVE-2026-62072 | 8.8 | 2026-10-06 | Subscriber Broken Access Control in Progress Planner <= 1.10.0 versions. |
| CVE-2026-66588 | 7.5 | 2026-10-06 | Unauthenticated Broken Access Control in The7 <= 14.2.2 versions. |
| CVE-2026-94675 | 7.1 | 2026-10-06 | Unauthenticated Cross Site Scripting (XSS) in Fluent Forms Pro Add On Pack <= 6.2.13 versions. |
| CVE-2026-95526 | 7.3 | 2026-10-06 | Unauthenticated Broken Access Control in BEAR <= 1.2.2 versions. |
| CVE-2026-95594 | 8.1 | 2026-10-06 | Unauthenticated Privilege Escalation in SMS Alert Order Notifications <= 4.0.0 versions. |
| CVE-2026-84854 | 7.0 | 2026-10-06 | In the WibuKey driver for Windows below Version 6.72, insufficient validation of user input when calculating the size of |
| CVE-2026-105985 | 8.8 | 2026-10-06 | Craft CMS 5.10.13.2 contains an authenticated remote code execution vulnerability in the Control Panel action app/render |
| CVE-2026-105918 | 7.3 | 2026-10-06 | A vulnerability has been found in Kusalkasilva Learning-Management-System up to ffeb873f8803f1e9664384ff75000c7da45466d2 |
| CVE-2026-105835 | 7.4 | 2026-10-06 | PLANKA 2.2.0 through 2.2.1 fails to limit incorrect TOTP codes submitted to POST /api/access-tokens/verify-totp, allowin |
| CVE-2026-105919 | 7.3 | 2026-10-06 | A vulnerability was found in Kusalkasilva Learning-Management-System up to ffeb873f8803f1e9664384ff75000c7da45466d2. The |
| CVE-2026-82531 | 8.1 | 2026-10-06 | Smarty before 4.5.8 and 5.x before 5.8.5 contains a code injection vulnerability where the top-level nocache_hash is nev |
| CVE-2026-105788 | 8.8 | 2026-10-06 | Microsoft UFO is an open-source framework for intelligent automation across devices and platforms. Prior to 3.0.10, the  |
| CVE-2026-105837 | 7.8 | 2026-10-06 | libmikmod before 3.3.14 contains an integer overflow vulnerability in DSM_Load() in load_dsm.c that allows attackers to  |
| CVE-2026-105839 | 7.8 | 2026-10-06 | libmikmod before 3.3.14 contains an integer overflow in the Oktalyzer loader OKT_doPBOD() that allows attackers to cause |
| CVE-2026-105840 | 7.5 | 2026-10-06 | lrzsz before 0.13.0 contains a path traversal vulnerability in the lrz receive utility's restricted mode that allows mal |
| CVE-2026-105841 | 7.5 | 2026-10-06 | lrzsz before 0.13.0 contains an OS command injection vulnerability in the lrz receive utility's pipe mode that allows re |
| CVE-2026-105920 | 7.3 | 2026-10-06 | A vulnerability was determined in Kusalkasilva Learning-Management-System up to ffeb873f8803f1e9664384ff75000c7da45466d2 |
| CVE-2026-106037 | 9.8 | 2026-10-06 | Mooncake through 0.3.13.post1 contains a missing authentication vulnerability in the Store REST service, which binds to  |
| CVE-2026-106038 | 8.2 | 2026-10-06 | Mooncake Store master through 0.3.13.post1 contains a missing authentication vulnerability that allows unauthenticated a |
| CVE-2026-106040 | 8.2 | 2026-10-06 | Mooncake Store master through 0.3.13.post1 contains a missing authorization vulnerability that allows unauthenticated at |
| CVE-2026-85523 | 8.8 | 2026-10-06 | Improper neutralization of special elements used in an OS command ('OS command injection') vulnerability in Felisify Inf |
| CVE-2026-91140 | 9.6 | 2026-10-06 | An OS command injection vulnerability in the shell-based temporary-file cleanup instructions in Progress Software Autono |

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