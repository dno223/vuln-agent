# Vulnerability Intelligence Report

**Date:** 2026-11-03  
**Generated:** 2026-11-03T15:50:11Z  

---

## Executive Summary

Our environment faces significant exposure across 136 high-severity vulnerabilities, with critical risks concentrated in Control Web Panel (CWP) and Krill. The most severe finding is a CVSS 9.8 OS command injection in CWP that enables full system compromise. Eight new CISA Known Exploited Vulnerabilities (KEVs) were added in the past seven days, covering actively exploited flaws in Ivanti Connect Secure, GitLab, Cisco Firewall, and VMware ESX. While no monitored CVEs currently match the KEV catalog, the volume and severity of unpatched vulnerabilities represent substantial organizational risk requiring immediate prioritization.

---

## Risk Narrative

The current threat landscape reflects coordinated attacker interest in widely deployed infrastructure platforms. CWP vulnerabilities expose hosting environments to remote code execution with no authentication required on loopback interfaces. Actively exploited KEV entries across Ivanti, Cisco, VMware, and GitLab indicate nation-state and ransomware actors are targeting perimeter security and virtualization layers. The Krill vulnerabilities introduce privilege escalation and cryptographic weaknesses in RPKI infrastructure, potentially undermining BGP routing security. Collectively, these exposures create pathways for lateral movement, data exfiltration, and critical infrastructure disruption. The absence of KEV matches against monitored assets is a positive indicator but does not eliminate risk from unmonitored shadow IT.

---

## Prioritized Action Items

1. Patch Control Web Panel to version 1.30 or later immediately to remediate the CVSS 9.8 OS command injection vulnerability (CVE-2026-77876) and five additional critical CWP flaws.
2. Audit and update all Ivanti Connect Secure deployments to address two newly KEV-listed vulnerabilities added October 30, 2026, per CISA binding operational directive timelines.
3. Apply available patches or mitigations for the KEV-listed Cisco Secure Firewall ASA and VMware ESX vulnerabilities, which are confirmed to be actively exploited in the wild.
4. Remediate the four Krill vulnerabilities (CVE-2026-109140 through CVE-2026-109142) by upgrading to a patched release and reviewing CA role permission configurations.
5. Patch GitLab CE/EE for CVE-2026-97229 immediately, as active exploitation is confirmed and source code repositories represent high-value targets for threat actors.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-104080 | 8.4 | 2026-11-02 | Control Web Panel (CWP) before webpanel_version 1.30 contains an OS command injection vulnerability in the loopback API  |
| CVE-2026-109140 | 8.4 | 2026-11-02 | The vulnerability is that Krill encrypts every login-session token with a nonce built from a counter that is reset to 0  |
| CVE-2026-109141 | 8.4 | 2026-11-02 | The vulnerability gives a role that is restricted to a list of CAs (cas = [...]) its full permission set for every reque |
| CVE-2026-109142 | 8.4 | 2026-11-02 | When a CA's parent lives on the same Krill server: instead of building and verifying a signed CMS message, it runs the R |
| CVE-2026-77876 | 9.8 | 2026-11-02 | Control Web Panel (CWP) before webpanel_version 1.16 contains an OS command injection vulnerability in the protected_dir |
| CVE-2026-77877 | 8.4 | 2026-11-02 | Control Web Panel (CWP) before webpanel_version 1.30 contains a missing authentication vulnerability that allows attacke |
| CVE-2026-77878 | 8.4 | 2026-11-02 | Control Web Panel (CWP) before webpanel_version 1.30 contains an OS command injection vulnerability in the loopback API  |
| CVE-2026-77879 | 7.7 | 2026-11-02 | Control Web Panel (CWP) before webpanel_version 1.16 contains a SQL injection vulnerability in the loopback API authenti |
| CVE-2026-77880 | 8.4 | 2026-11-02 | Control Web Panel (CWP) before webpanel_version 1.16 contains an OS command injection vulnerability in the loopback API  |
| CVE-2026-88809 | 7.6 | 2026-11-02 | A security vulnerability exists in the SUSE Rancher Manager meta proxy endpoint (/meta/proxy). This endpoint is intended |
| CVE-2026-94290 | 9.1 | 2026-11-02 | SUSE Rancher Fleet clusters reference a kubeconfig secret that the controller uses to install and manage a Fleet agent o |
| CVE-2026-99218 | 7.0 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

coredump: hold RCU while releasing parked threads

 |
| CVE-2026-99224 | 7.0 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

keys: Protect the type name while describing a key
 |
| CVE-2026-99227 | 7.8 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

io_uring/waitid: prevent cancel reference wrap

io_ |
| CVE-2026-99231 | 7.8 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

io_uring/waitid: own the request before clearing -> |
| CVE-2026-99233 | 7.8 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

tracing/histograms: Verify event_call identity when |
| CVE-2026-99235 | 7.8 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

tracing: Save the event file instead of the compati |
| CVE-2026-99236 | 7.8 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

tracing: Reject incomplete event filter expressions |
| CVE-2026-99237 | 7.8 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

tracing: Hold trace_types_lock when resetting last  |
| CVE-2026-99238 | 7.8 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

tracing: Hold trace_types_lock when updating module |
| CVE-2026-99239 | 7.8 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

Bluetooth: L2CAP: refuse __l2cap_chan_add if chan a |
| CVE-2026-105769 | 9.3 | 2026-11-02 | kaniko before 1.25.20 can send a Microsoft Entra ID (Azure AD) access token for Azure Resource Manager to an attacker-co |
| CVE-2026-106803 | 9.8 | 2026-11-02 | A stack-based buffer overflow exists in Kamailio v6.1.3 and v6.1.4 in the ims_registrar_pcscf module. When processing a  |
| CVE-2026-106804 | 7.5 | 2026-11-02 | A stack-based buffer overflow exists in Kamailio v6.1.3 and v6.1.4 in the ims_qos_npn module. The w_rx_aar_register() fu |
| CVE-2026-119301 | 7.9 | 2026-11-02 | Improper neutralization of quoting syntax in SQL identifier construction in the Apache Iceberg write component in AWS SD |
| CVE-2026-120596 | 7.5 | 2026-11-02 | A remotely exploitable denial-of-service vulnerability exists in the TCP options parser of the Nut/Net TCP/IP stack incl |
| CVE-2026-88810 | 7.2 | 2026-11-02 | A privilege escalation issue was discovered in Rancher Manager's role-based access control. The inheritedNamespacedRules |
| CVE-2026-88811 | 9.1 | 2026-11-02 | Missing filtering in the SUSE Rancher Manager meta proxy could cause passed in rancher credentials to be leaked to cloud |
| CVE-2026-106808 | 7.5 | 2026-11-02 | OpenAirInterface Core Network v2.2.1 has a stack-based buffer overflow vulnerability in the OAI CN5G UDM Nudm_UEAU Gener |
| CVE-2026-119085 | 8.8 | 2026-11-02 | Improper neutralization of special elements used in a template engine in the publishing component of Amazon Virtual Engi |
| CVE-2026-117069 | 7.5 | 2026-11-02 | An integer truncation vulnerability in the NAS decoder of OpenAirInterface (OAI) CN5G AMF v2.2.1 allows an unauthenticat |
| CVE-2026-119731 | 7.5 | 2026-11-02 | Munshi (by Petpooja) before 2026-06-30 contained a payment bypass vulnerability in its subscription payment webhook at P |
| CVE-2026-119733 | 8.1 | 2026-11-02 | Munshi (by Petpooja) before 2026-07-07 contained a missing authorization vulnerability in its company deletion workflow  |
| CVE-2026-119736 | 8.2 | 2026-11-02 | Attendo (formerly Petpooja Payroll) Admin Android application version 3.0.13 and earlier contains a hard-coded credentia |
| CVE-2026-120057 | 7.5 | 2026-11-02 | psqlODBC copies the reply to a large-object read (loread) into the application's buffer using the length sent by the ser |
| CVE-2026-120058 | 7.5 | 2026-11-02 | psqlODBC sizes its row cache from the column count of a cursor's first result, but recomputes the column count from each |
| CVE-2026-120061 | 7.5 | 2026-11-02 | The psqlODBC parser for ODBC escape sequences in application SQL text writes the argument offsets of a {fn} escape into  |
| CVE-2026-120062 | 7.5 | 2026-11-02 | SQLSpecialColumns in psqlODBC splices the table and schema names it receives into its catalog query without escaping the |
| CVE-2026-120064 | 7.5 | 2026-11-02 | Several psqlODBC entry points use an application-supplied column number or row index as an array index without validatin |
| CVE-2026-120065 | 7.1 | 2026-11-02 | For an updatable cursor over a table without OIDs that has an auto-increment int4 column, psqlODBC uses that column to i |
| CVE-2026-81938 | 7.7 | 2026-11-02 | Grafana Mimir's Alertmanager rejects tenant-supplied receiver configurations that reference local files, but the check d |
| CVE-2026-102435 | 9.8 | 2026-11-02 | The Ultra Addons for Contact Form 7 plugin for WordPress is vulnerable to arbitrary file deletion due to insufficient fi |
| CVE-2026-119737 | 7.8 | 2026-11-02 | The pppoe_wrapper vendor daemon from the Amlogic Android SDK, as shipped on Nexbox A95X (Amlogic S905/S905X) TV boxes, c |
| CVE-2026-28588 | 8.4 | 2026-11-02 | In shouldBlockDirectoryFromTree of ExternalStorageProvider.java, there is a possible way to access protected data due to |
| CVE-2026-28597 | 8.4 | 2026-11-02 | In writeGrantedUriPermissions of UriGrantsManagerService.java, there is a possible permission bypass due to improper inp |
| CVE-2026-45514 | 8.4 | 2026-11-02 | In multiple functions of SaveUi.java, there is a possible bypass of package installation requirements due to a logic err |
| CVE-2026-49922 | 8.4 | 2026-11-02 | In queryRemoteConnectionServices of ConnectionServiceWrapper.java, there is a possible permission bypass due to a confus |
| CVE-2026-49923 | 8.4 | 2026-11-02 | In onResult of AccountManagerService.java, there is a possible untrusted/misleading UI issue due to a logic error in the |
| CVE-2026-49931 | 8.4 | 2026-11-02 | In onActivityResult in multiple locations, there is a possible contact leak from protected profile due to a confused dep |
| CVE-2026-55257 | 8.4 | 2026-11-02 | In UsbDialogHelper of UsbDialogHelper.java, there is a possible UI confusion due to misleading or insufficient UI. This  |
| CVE-2026-55262 | 8.4 | 2026-11-02 | In setNotificationListenerAccessGrantedForUserInternal of NotificationManagerService.java, there is a possible  policy d |
| CVE-2026-55271 | 8.4 | 2026-11-02 | In forwardToPreferredActionPickHandler of ContactsPickerActivity.kt, there is a possible intent redirection due to a con |
| CVE-2026-55275 | 8.4 | 2026-11-02 | In multiple locations, there is a possible use-after-free due to a race condition. This could lead to remote escalation  |
| CVE-2026-55283 | 8.4 | 2026-11-02 | In multiple locations, there is a possible memory safety issue due to a use-after-free. This could lead to remote escala |
| CVE-2026-55287 | 8.4 | 2026-11-02 | In onCreate of GrantCredentialsPermissionActivity.java, there is a possible way to trick the user into granting account  |
| CVE-2026-55289 | 8.4 | 2026-11-02 | In multiple functions in multiple locations, there is a possible execution of sensitive USSD codes due to a confused dep |
| CVE-2026-58825 | 8.4 | 2026-11-02 | In multiple functions of fork.c, there is a possible use after free due to a logic error in the code. This could lead to |
| CVE-2026-58826 | 8.4 | 2026-11-02 | In ksys_unshare of fork.c, there is a possible memory corruption due to a use after free. This could lead to local escal |
| CVE-2026-58827 | 8.4 | 2026-11-02 | In multiple functions of dma-buf.c, there is a possible use after free due to a race condition. This could lead to local |
| CVE-2026-58828 | 8.4 | 2026-11-02 | In multiple functions of base.c, there is a possible use-after-free due to a race condition. This could lead to local es |
| CVE-2026-58829 | 8.4 | 2026-11-02 | In fuse_backing_mmap of backing.c, there is a possible memory corruption due to a use after free. This could lead to loc |
| CVE-2026-58836 | 7.8 | 2026-11-02 | In handlePackagePostInstall of InstallPackageHelper.java, there is a possible Enhanced Confirmation Mode (ECM) bypass vu |
| CVE-2026-58837 | 8.4 | 2026-11-02 | In multiple locations, there is a possible background activity launch due to a logic error in the code. This could lead  |
| CVE-2026-58853 | 7.5 | 2026-11-02 | In multiple functions of ipphelper.c, there is a possible stack bugger overflow due to a missing bounds check. This coul |
| CVE-2026-58866 | 8.4 | 2026-11-02 | In setAccessibilityWindowAttributes of AccessibilityWindowManager.java, there is a possible untrusted/misleading UI issu |
| CVE-2026-58884 | 8.4 | 2026-11-02 | In startTetheredHotspotRequest of WifiServiceImpl.java, there is a possible permission bypass due to a confused deputy.  |
| CVE-2026-58885 | 8.4 | 2026-11-02 | In multiple locations, there is a possible permission bypass due to a confused deputy. This could lead to local escalati |
| CVE-2026-58934 | 8.4 | 2026-11-02 | In prepareWindowToDisplayDuringRelayout of WindowState.java, there is a possible permission bypass due to a logic error  |
| CVE-2026-58942 | 8.4 | 2026-11-02 | In do_fault_around of memory.c, there is a possible use after free due to a logic error in the code. This could lead to  |
| CVE-2026-58943 | 8.4 | 2026-11-02 | In run of AddAccountSettings.java, there is a possible background activity launch due to a confused deputy. This could l |
| CVE-2026-58944 | 8.4 | 2026-11-02 | In moveTaskToFrontLocked of ActivityTaskManagerService.java, there is a possible background application launch (bal) iss |
| CVE-2026-58946 | 8.4 | 2026-11-02 | In navigateUpTo of ActivityClientController.java, there is a possible permission bypass due to a logic error in the code |
| CVE-2026-58957 | 8.4 | 2026-11-02 | In resolveToHeavyWeightSwitcherIfNeeded of ActivityStarter.java, there is a possible background activity launch due to a |
| CVE-2026-58965 | 8.4 | 2026-11-02 | In handleAudioEffectBroadcast of MusicFxHelper.java, there is a possible permission bypass due to a confused deputy. Thi |
| CVE-2026-58970 | 8.4 | 2026-11-02 | In deliverResult of AppTimeTracker.java, there is a possible background activity launch due to a confused deputy. This c |
| CVE-2026-58984 | 8.4 | 2026-11-02 | In multiple locations, there is a possible memory corruption due to a use-after-free. This could lead to local escalatio |
| CVE-2026-59000 | 8.4 | 2026-11-02 | In multiple locations, there is a possible permission bypass due to a confused deputy. This could lead to local escalati |
| CVE-2026-59028 | 8.4 | 2026-11-02 | In resolveAidConflictLocked of RegisteredAidCache.java, there is a possible permission bypass due to a confused deputy.  |
| CVE-2026-59044 | 8.4 | 2026-11-02 | In multiple locations, there is a possible use-after-free due to a logic error in the code. This could lead to local esc |
| CVE-2026-91893 | 7.8 | 2026-11-02 | Dell Alienware Command Center (AWCC), versions prior to 6.14.54.0, contain an Improper Privilege Management vulnerabilit |
| CVE-2026-91895 | 7.1 | 2026-11-02 | Dell Alienware Command Center (AWCC), versions prior to 6.14.54.0, contain an Incorrect Default Permissions vulnerabilit |
| CVE-2026-91898 | 8.1 | 2026-11-02 | Dell Alienware Command Center (AWCC), versions prior to 6.14.54.0, contain an Improper Verification of Cryptographic Sig |
| CVE-2026-105476 | 8.8 | 2026-11-02 | Improper link resolution before file access in cPanel allows remote authenticated users to write arbitrary root-owned fi |
| CVE-2026-29508 | 8.8 | 2026-11-02 | ReadyMedia (formerly MiniDLNA) versions 1.3.0 through 1.3.3 contain a stack-based buffer overflow vulnerability that all |
| CVE-2026-58873 | 8.4 | 2026-11-02 | In addDragDropListener of WindowManagerService.java, there is a possible permission bypass due to a missing permission c |
| CVE-2026-86596 | 9.8 | 2026-11-02 | The s2Member plugin for WordPress is vulnerable to Remote Code Execution in all versions up to, and including, <= 260927 |
| CVE-2026-120752 | 7.5 | 2026-11-02 | PyMuPDF 1.25.3 before 2.0 contains a stack-based buffer overflow vulnerability in JM_set_annot_callout_line() that copie |
| CVE-2026-120830 | 7.4 | 2026-11-03 | A flaw was found in libslirp in icmp_forward_error(). When building an ICMP error response, the length of the quoted ori |
| CVE-2026-120833 | 7.8 | 2026-11-03 | labbench before 0.46.1 contains a deserialization of untrusted data vulnerability in read() and read_relational() that p |
| CVE-2026-107441 | 8.8 | 2026-11-03 | An out-of-bounds write vulnerability in the CGI program of Zyxel GS1900-24E firmware versions through 2.90(AAHK.2)C0 cou |
| CVE-2026-76955 | 8.8 | 2026-11-03 | A buffer overflow vulnerability in the zdp_wtp binary in Zyxel NWA110AX firmware versions through 7.12(ABTG.0)C0 could a |
| CVE-2026-120518 | 9.1 | 2026-11-03 | The BuddyPress XProfile Image Field plugin for WordPress is vulnerable to arbitrary file deletion in all versions up to, |
| CVE-2026-120534 | 9.8 | 2026-11-03 | The Advanced Custom Fields: Extended PRO plugin for WordPress is vulnerable to Limited Code Injection in all versions up |
| CVE-2026-120538 | 8.1 | 2026-11-03 | The Easy Digital Downloads plugin for WordPress is vulnerable to authentication bypass leading to administrator account  |
| CVE-2026-120558 | 7.2 | 2026-11-03 | The Advanced Shipment Tracking for WooCommerce plugin for WordPress is vulnerable to SQL Injection via the `tracking_pro |
| CVE-2026-120559 | 7.5 | 2026-11-03 | The Contact Form Extender for Divi Builder plugin for WordPress is vulnerable to Arbitrary File Deletion due to insuffic |
| CVE-2026-120574 | 8.1 | 2026-11-03 | The SureCart plugin for WordPress is vulnerable to unauthenticated account takeover in all versions up to, and including |
| CVE-2026-120577 | 8.1 | 2026-11-03 | The FluentCart A New Era of eCommerce – Faster, Lighter, and Simpler plugin for WordPress is vulnerable to arbitrary fil |
| CVE-2026-77799 | 7.4 | 2026-11-03 | ManageEngine Key Manager Plus versions before 7150 are vulnerable to a Two-Factor Authentication bypass that allows atta |
| CVE-2026-77800 | 7.7 | 2026-11-03 | ManageEngine Key Manager Plus versions before 7151 are vulnerable to a SAML authentication bypass that allows attackers  |
| CVE-2026-13594 | 9.1 | 2026-11-03 | Zoho Corporation's ManageEngine Log360 and EventLog Analyzer versions 13062 and below are vulnerable to an issue that co |
| CVE-2026-16900 | 7.5 | 2026-11-03 | Zohocorp ManageEngine Log360 and EventLog Analyzer versions 13071 and below are vulnerable to an authentication bypass i |
| CVE-2026-4052 | 9.8 | 2026-11-03 | This issue only impacts deployments where WSO2 Identity Server is configured as a Resident Key Manager with database sha |
| CVE-2026-105978 | 7.2 | 2026-11-03 | Improper input validation in management control functions may allow a remote attacker with high privileges to inject ope |
| CVE-2026-105979 | 7.2 | 2026-11-03 | Improper input validation in the ZeroTier VPN function may allow a remote attacker with high privileges to inject system |
| CVE-2026-105980 | 7.2 | 2026-11-03 | Improper input validation in the WireGuard VPN function may allow a remote attacker with high privileges to inject syste |
| CVE-2026-105981 | 7.2 | 2026-11-03 | Improper input validation in the Digital I/O function may allow a remote attacker with high privileges to inject operati |
| CVE-2026-105982 | 7.2 | 2026-11-03 | Improper input validation in the IPsec VPN function may allow a remote attacker with high privileges to inject system co |
| CVE-2026-121022 | 8.1 | 2026-11-03 | Use of Default Password (CWE-1393) in the web client in AxxonSoft Axxon One before 3.0.0 on Windows and Linux allows a r |
| CVE-2026-77691 | 8.1 | 2026-11-03 | ZohoCorp ManageEngine Key Manager Plus versions before 7151 allow authenticated users to enter malicious input when conf |
| CVE-2026-77777 | 7.1 | 2026-11-03 | ManageEngine Key Manager Plus versions before 7151 are vulnerable to an improper access control issue that allow authent |
| CVE-2026-77778 | 7.1 | 2026-11-03 | ZohoCorp ManageEngine Key Manager Plus versions up to 7150 allow authenticated users to export certificates belonging to |
| CVE-2026-76124 | 8.8 | 2026-11-03 | The BuddyBoss App plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 3.2. |
| CVE-2026-119179 | 7.0 | 2026-11-03 | A flaw in the connection management layer of the MongoDB Node.js driver can leave a pooled network connection in the poo |
| CVE-2026-119742 | 7.2 | 2026-11-03 | Nagios XI before 2026R2 contains an OS command injection vulnerability in the MIB upload feature where the install_mib() |
| CVE-2026-120572 | 8.8 | 2026-11-03 | Incorrect boundary conditions in the Layout: Block and Inline component. This vulnerability was fixed in Firefox 159.0.1 |
| CVE-2026-85035 | 8.8 | 2026-11-03 | The can_add_rx_filter_msgq() system call installs a CAN RX filter whose callback (can_msgq_put() in drivers/can/can_comm |
| CVE-2026-106991 | 7.1 | 2026-11-03 | hustoj >=24.09.10 and <=26.08.19 is vulnerable to Incorrect Access Control. Any registered user can delete, lock, or sti |
| CVE-2026-118489 | 7.5 | 2026-11-03 | In Eclipse Vert.x versions [4.0.0,4.5.35] or [5.0.0,5.2.2], when one `CachingWebClient` is shared across users — the doc |
| CVE-2026-121386 | 7.5 | 2026-11-03 | FreeRDP before 3.32.2 contains a denial of service vulnerability in WinPR's winpr_read_png_from_buffer() and winpr_conve |
| CVE-2026-121392 | 7.4 | 2026-11-03 | FreeRDP before 3.32.2 contains an improper certificate validation vulnerability in tls_verify_certificate() that accepts |
| CVE-2026-121416 | 7.1 | 2026-11-03 | SurrealDB 2.0.0 before 3.3.1 does not enforce --deny-funcs restrictions on method-style function calls in the streaming  |
| CVE-2026-121417 | 7.8 | 2026-11-03 | SurrealDB before 3.3.0 contains a use-after-free vulnerability in surrealdb-core KV backends that pass borrowed transact |
| CVE-2026-121419 | 8.1 | 2026-11-03 | SurrealDB from 3.1.0 before 3.3.0 contains an improper authentication vulnerability where the MCP BoundSubject fingerpri |
| CVE-2026-121427 | 7.5 | 2026-11-03 | AzuraCast through 0.23.8 fails to remove frontend_config.custom_config in PUT /station/{id}/profile/edit for users lacki |
| CVE-2026-121428 | 8.8 | 2026-11-03 | AzuraCast through 0.23.8 contains a remote code execution vulnerability that allows authenticated station managers to in |
| CVE-2026-121429 | 8.8 | 2026-11-03 | AzuraCast through 0.23.8 contains a command injection vulnerability that allows station users with Profile permission to |
| CVE-2026-121436 | 7.2 | 2026-11-03 | Froxlor from 2.3.8 before 2.3.15 contains an information disclosure vulnerability that allows administrators with custom |
| CVE-2026-121437 | 7.5 | 2026-11-03 | Mistune from 3.3.0 before 3.3.4 contains a denial of service vulnerability that allows remote attackers to exhaust CPU t |
| CVE-2026-121444 | 7.5 | 2026-11-03 | svg-sanitizer from 0.11.0 before 1.1.0 contains an algorithmic complexity denial of service vulnerability in hasInfinite |
| CVE-2026-121448 | 8.3 | 2026-11-03 | Dockhand before 1.0.54 contains a path traversal vulnerability that allows authenticated users to read, overwrite, and d |
| CVE-2026-121506 | 7.4 | 2026-11-03 | An out-of-bounds read and write in NTS client extension field parsing (extens_client_recv) in NTPsec before 1.2.5 allows |
| CVE-2026-121510 | 7.5 | 2026-11-03 | Remote Unauthenticated Heap Out-of-Bounds Write in µD3TN BPv6 Administrative Record Parser allows Unauthenticated Remote |
| CVE-2026-121511 | 7.1 | 2026-11-03 | Heap Out-of-Bounds Read in µD3TN BPv6/BPv7 Fragmenter allows Local Attacker to Read Memory and Reliably Cause DoS |
| CVE-2026-121512 | 7.5 | 2026-11-03 | Memory Leak with Amplification in µD3TN BPv6 EID Reference Handling allows Unauthenticated Remote Attacker to Cause DoS |
| CVE-2026-121513 | 7.5 | 2026-11-03 | Off-by-one Heap Overflow in µD3TN v0.15.1 SPP Parser allows Unauthenticated Remote Attacker to Reliably Cause DoS |

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

---

*Total entries in CISA KEV catalog: 1766*