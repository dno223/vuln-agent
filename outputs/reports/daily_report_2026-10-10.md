# Vulnerability Intelligence Report

**Date:** 2026-10-10  
**Generated:** 2026-10-10T14:14:27Z  

---

## Executive Summary

Our environment faces significant exposure across 135 high-severity vulnerabilities, including critical flaws in openPDC and openHistorian systems (CVSS 9.8) enabling unauthenticated remote code execution via deserialization. Six previously known vulnerabilities have been newly added to CISA's Known Exploited Vulnerabilities catalog, indicating active real-world exploitation of legacy software including ISC BIND, Apache Struts, and ProFTPD. WordPress plugin vulnerabilities introduce additional web-layer risk. No monitored CVEs currently overlap with the KEV catalog, but the volume and severity of open issues demands immediate prioritization and structured remediation.

---

## Risk Narrative

The threat landscape reflects both emerging and legacy exploitation risks. The CVSS 9.8 deserialization flaw in openPDC and openHistorian represents a critical infrastructure risk, potentially enabling full system compromise without authentication. The addition of six entries to CISA's KEV catalog signals active threat actor exploitation of older vulnerabilities in widely deployed software, increasing the likelihood of opportunistic attacks. WordPress-based vulnerabilities expand the web attack surface, exposing organizational assets to data theft, defacement, and lateral movement. Without rapid remediation and enhanced monitoring, the organization faces elevated risk of ransomware deployment, data exfiltration, and operational disruption.

---

## Prioritized Action Items

1. Immediately patch or isolate openPDC and openHistorian instances to remediate the CVSS 9.8 deserialization vulnerability (CVE-2026-100730) allowing unauthenticated remote code execution.
2. Audit all environments for presence of CISA KEV-listed software (ISC BIND, Apache Struts, ProFTPD, Strapi, ONLYOFFICE) and apply available patches or mitigations within 24–48 hours.
3. Restrict network access to the openPDC internal data publisher (CVE-2026-105281) by enforcing authentication and applying firewall controls immediately.
4. Remediate WordPress plugin vulnerabilities including object injection and PHP remote file inclusion flaws (CVE-2026-94064, CVE-2026-94065, CVE-2026-94067) by updating or disabling affected themes and plugins.
5. Establish a continuous KEV monitoring process to receive real-time alerts when any internal assets match newly cataloged exploited vulnerabilities.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-100730 | 9.8 | 2026-10-09 | A service console interface on openPDC and openHistorian deserializes a client-supplied data structure. On systems using |
| CVE-2026-104629 | 8.8 | 2026-10-09 | A component loading mechanism in openPDC and openHistorian will construct and run any specified type, which may be an in |
| CVE-2026-105281 | 7.5 | 2026-10-09 | The internal data publisher on openPDC accepts network connections without authentication in its default configuration.  |
| CVE-2026-62026 | 7.1 | 2026-10-09 | Cross-Site Request Forgery (CSRF) vulnerability in MIGHTYminnow Dashboard Notes dashboard-notes allows Cross Site Reques |
| CVE-2026-94063 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in ThemeREX Education |
| CVE-2026-94064 | 8.8 | 2026-10-09 | Deserialization of Untrusted Data vulnerability in BuddhaThemes Neo \| Barber Shop WordPress Theme neocut allows Object I |
| CVE-2026-94065 | 8.8 | 2026-10-09 | Deserialization of Untrusted Data vulnerability in BuddhaThemes ColorFolio colorit allows Object Injection.This issue af |
| CVE-2026-94066 | 7.1 | 2026-10-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in SpabRice Pond pond |
| CVE-2026-94067 | 8.1 | 2026-10-09 | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability in |
| CVE-2026-104081 | 8.1 | 2026-10-09 | KodExplorer before 4.55 contains a path traversal vulnerability in the unzip_pre_name() function within app/function/hel |
| CVE-2026-105278 | 9.8 | 2026-10-09 | The published Docker image for openPDC includes a fixed administrative credential with no forced change on first use. An |
| CVE-2026-107805 | 7.5 | 2026-10-09 | Nginx UI is a web user interface for the Nginx web server. From 2.5.0 until 2.6.0, the node-signature authentication pat |
| CVE-2026-108101 | 7.5 | 2026-10-09 | HortusFox (hortusfox-web) through 6.3 contains an unrestricted file upload vulnerability in PlantAttachmentModel that al |
| CVE-2026-108106 | 7.5 | 2026-10-09 | Xerial snappy-java before 1.1.10.9 contains an unbounded memory allocation vulnerability that allows attackers to exhaus |
| CVE-2026-108107 | 9.8 | 2026-10-09 | PHPNuxBill through 2025.3.20 contains an unauthenticated SQL injection vulnerability in the radius.php FreeRADIUS REST e |
| CVE-2026-108108 | 7.1 | 2026-10-09 | PHPNuxBill through 2025.3.20 contains an authentication bypass vulnerability in RADIUS CHAP verification because Passwor |
| CVE-2026-108109 | 9.1 | 2026-10-09 | PHPNuxBill through 2025.3.20 contains an account takeover vulnerability in the customer password reset flow in system/co |
| CVE-2026-15340 | 9.8 | 2026-10-09 | lwIP SMTP client does not check the size of inputs, potentially allowing a buffer overflow. |
| CVE-2026-28745 | 7.5 | 2026-10-09 | Usernames and passwords, including the default credentials, are stored in the configuration file using weak encryption.  |
| CVE-2026-29797 | 7.1 | 2026-10-09 | No authentication is required when updating firmware or bootloader, making it easy for malicious files to be pushed to t |
| CVE-2026-33367 | 8.1 | 2026-10-09 | SNMP can be used to perform administrative actions such as retrieving configuration files, modifying user accounts or de |
| CVE-2026-39453 | 8.3 | 2026-10-09 | Navigating to a certain URL on the switch’s web server causes the switch to reboot. This can be automated using a tool l |
| CVE-2026-39460 | 8.1 | 2026-10-09 | Usernames and passwords, including the default factory credentials, are stored in plaintext within the configuration fil |
| CVE-2026-78795 | 7.5 | 2026-10-09 | An issue in Netcore B11 Enterprise-level full Gigabit 9-port shop wireless router v1.3.241114.024540 and before allows a |
| CVE-2026-104082 | 7.2 | 2026-10-09 | SmarterMail before build 9777 contains a remote code execution vulnerability that allows an attacker holding a SysAdmin- |
| CVE-2026-104084 | 8.8 | 2026-10-09 | SmarterMail before build 9777 contains a privilege escalation vulnerability where JWT access and refresh tokens embed a  |
| CVE-2026-107807 | 8.8 | 2026-10-09 | Nginx UI is a web user interface for the Nginx web server. From 2.0.0 until 2.5.0, Nginx UI accepts the Node.Secret mast |
| CVE-2026-107808 | 8.1 | 2026-10-09 | Nginx UI is a web user interface for the Nginx web server. From 2.0.0 until 2.5.0, POST /api/login checks EnabledOTP but |
| CVE-2026-107809 | 8.8 | 2026-10-09 | Nginx UI is a web user interface for the Nginx web server. From 2.0.0 until 2.5.0, AuthRequired accepts a browser-manage |
| CVE-2026-107810 | 8.1 | 2026-10-09 | Nginx UI is a web user interface for the Nginx web server. From 2.0.0 until 2.5.0, internal/backup/restore.go extracts i |
| CVE-2026-107811 | 8.8 | 2026-10-09 | Nginx UI is a web user interface for the Nginx web server. From 2.0.0 until 2.5.0, ordinary authenticated users can acce |
| CVE-2026-107812 | 7.5 | 2026-10-09 | Nginx UI is a web user interface for the Nginx web server. From 2.0.0 until 2.5.0, the self-upgrade mechanism validates  |
| CVE-2026-107813 | 8.8 | 2026-10-09 | Nginx UI is a web user interface for the Nginx web server. From 2.0.0 until 2.5.0, the api/cluster router exposes node a |
| CVE-2026-107814 | 8.4 | 2026-10-09 | MariaDB server is a community developed fork of MySQL server. From 10.6.1 until 10.6.28, 10.11.19, 11.4.13, 11.8.9, 12.3 |
| CVE-2026-108113 | 8.8 | 2026-10-09 | ILIAS before 9.24, 10.12, and 11.5 contains an unrestricted file upload vulnerability in QTI question import image handl |
| CVE-2026-75345 | 7.5 | 2026-10-09 | OpENer v2.3.0 / commit 76b95cf contains an out-of-bounds read in the unconnected explicit messaging path. This allows a  |
| CVE-2026-75346 | 7.5 | 2026-10-09 | An out-of-bounds read vulnerability exists in EIPStackGroup OpENer v2.3 and master through commit 76b95cf in the server- |
| CVE-2026-75348 | 7.5 | 2026-10-09 | An out-of-bounds read vulnerability exists in EIPStackGroup OpENer v2.3 and master up to commit 76b95cf in the EtherNet/ |
| CVE-2026-75349 | 7.5 | 2026-10-09 | EIPStackGroup OpENer v2.3.0/master up to commit 76b95cf contains an out-of-bounds read vulnerability in Connection Manag |
| CVE-2026-90983 | 8.2 | 2026-10-09 | Use of Client-Side authentication vulnerability in Hayat Health Facilities Inc. (Hayat Hospital) Hayat Mobile allows Aut |
| CVE-2026-107815 | 8.5 | 2026-10-09 | MariaDB server is a community developed fork of MySQL server. From 10.6.1 until 10.6.28, 10.11.19, 11.4.13, 11.8.9, 12.3 |
| CVE-2026-108156 | 7.1 | 2026-10-09 | LobsterAI 2026.5.27 through 2026.9.23 contains an external control of file path vulnerability in the skills:delete IPC h |
| CVE-2026-108157 | 8.1 | 2026-10-09 | Pingvin Share X from 0.19.0 before 1.22.0 contains an improper authentication vulnerability that allows remote unauthent |
| CVE-2026-108159 | 7.5 | 2026-10-09 | AstronRPA through 1.1.6 contains a cross-site scripting vulnerability in the desktop client's smart-component chat that  |
| CVE-2026-108160 | 7.5 | 2026-10-09 | AstronRPA through 1.1.6 contains a download of code without integrity check vulnerability that allows network attackers  |
| CVE-2026-55797 | 8.8 | 2026-10-09 | Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. From 2.11.0 until 3.3.15, 3.4.10, 3.5.4, and 3 |
| CVE-2026-75347 | 7.5 | 2026-10-09 | EIPStackGroup OpENer v2.3 and master up to commit 76b95cf contain an expired pointer dereference vulnerability in the Et |
| CVE-2026-107818 | 8.4 | 2026-10-09 | MariaDB server is a community developed fork of MySQL server. From 10.6.1 until 10.6.28, 10.11.19, 11.4.13, 11.8.9, 12.3 |
| CVE-2026-107821 | 8.0 | 2026-10-09 | MariaDB server is a community developed fork of MySQL server. From 10.6.1 until 10.6.28, 10.11.19, 11.4.13, 11.8.9, 12.3 |
| CVE-2026-107823 | 7.2 | 2026-10-09 | MariaDB server is a community developed fork of MySQL server. From 10.6.1 until 10.6.28, 10.11.19, 11.4.13, 11.8.9, 12.3 |
| CVE-2026-107826 | 7.5 | 2026-10-09 | OWASP Coraza WAF is a golang modsecurity compatible web application firewall library. From 3.0.0 until 3.8.1, readJSON i |
| CVE-2026-107837 | 8.2 | 2026-10-09 | RIOT is an open-source microcontroller operating system designed for Internet of Things devices and other embedded syste |
| CVE-2026-107838 | 7.5 | 2026-10-09 | RIOT is an open-source microcontroller operating system designed for Internet of Things devices and other embedded syste |
| CVE-2026-107839 | 7.5 | 2026-10-09 | ageLANServer provides a cross-platform web server and launcher for offline multiplayer in several Age of Empires and Age |
| CVE-2026-107840 | 7.5 | 2026-10-09 | yopass is a service for securely sharing secrets, passwords, and files. Prior to version 14.7.0, the Prometheus metrics  |
| CVE-2026-75350 | 7.5 | 2026-10-09 | EIPStackGroup OpENer v2.3 / master commit 76b95cf contains a buffer overflow in the GetAttributeList() implementation fo |
| CVE-2026-75351 | 7.5 | 2026-10-09 | OpENer v2.3/commit 76b95cf, contains an out-of-bounds read in the server-side EtherNet/IP ForwardOpen connection-path pa |
| CVE-2026-107845 | 9.3 | 2026-10-09 | Contao is an Open Source CMS. From version 4.0.0 until 5.3.50 and 5.7.12, an unauthenticated visitor can submit a commen |
| CVE-2026-108259 | 8.2 | 2026-10-09 | Tina is a headless content management system. Prior to 3.0.0, @tinacms/cli reads Git branch values from VERCEL_GIT_COMMI |
| CVE-2026-108260 | 7.6 | 2026-10-09 | Tina is a headless content management system. Prior to 0.2.1, the tina-markdown element in packages/@tinacms/web-compone |
| CVE-2026-108261 | 9.3 | 2026-10-09 | Tina is a headless content management system. Prior to tinacms 3.14.0 and @tinacms/app 2.5.14, the /~/* admin preview ro |
| CVE-2026-108263 | 9.9 | 2026-10-09 | Astron Agent is an agentic workflow platform for building and running AI agents. Prior to 1.1.2, the default workflow co |
| CVE-2026-108264 | 9.1 | 2026-10-09 | Wizarr is an advanced user invitation and management system for Jellyfin, Plex, Emby, and other media servers. Prior to  |
| CVE-2026-57458 | 8.1 | 2026-10-09 | Vikunja is an open-source self-hosted task management platform. In version 2.3.0, a scoped API token limited to the `oau |
| CVE-2026-62376 | 8.1 | 2026-10-09 | Vikunja is an open-source self-hosted task management platform. Versions prior to 2.4.0 store password-reset, email-conf |
| CVE-2026-92705 | 7.8 | 2026-10-09 | Aegisub is a cross-platform advanced subtitle editor. From 3.2.0 to 3.4.2, Aegisub automatically loads Automation script |
| CVE-2026-108474 | 9.8 | 2026-10-10 | In JetBrains Exposed before 1.5.1 sQL injection was possible via unescaped string arguments of several SQL functions |
| CVE-2026-104732 | 9.8 | 2026-10-10 | The Advanced IP Blocker plugin for WordPress is vulnerable to Authentication Bypass in all versions up to, and including |
| CVE-2026-104797 | 8.1 | 2026-10-10 | The Advanced Form Integration — Connect Forms to 300+ Apps plugin for WordPress is vulnerable to Authentication Bypass v |
| CVE-2026-107645 | 9.1 | 2026-10-10 | The Blocksy Companion plugin for WordPress is vulnerable to privilege escalation in versions up to, and including, 2.1.5 |
| CVE-2026-94589 | 9.8 | 2026-10-10 | The Extensions For CF7 (Contact form 7 Database, Conditional Fields and Redirection) plugin for WordPress is vulnerable  |
| CVE-2026-103889 | 9.8 | 2026-10-10 | The 3D Product configurator for WooCommerce plugin for WordPress is vulnerable to Remote Code Execution in all versions  |
| CVE-2026-104021 | 7.2 | 2026-10-10 | The Fastcache by Host.it plugin for WordPress is vulnerable to Code Injection in all versions up to, and including, 1.7. |
| CVE-2026-89301 | 7.5 | 2026-10-10 | The rtMedia for WordPress, BuddyPress and bbPress plugin for WordPress is vulnerable to limited file deletion due to ins |
| CVE-2026-97670 | 9.1 | 2026-10-10 | The Avada (Fusion) Builder plugin for WordPress is vulnerable to authorization bypass in all versions up to, and includi |
| CVE-2026-104723 | 8.8 | 2026-10-10 | The LifterLMS – WP LMS for eLearning, Online Courses, & Quizzes plugin for WordPress is vulnerable to PHP Object Injecti |
| CVE-2026-104725 | 8.8 | 2026-10-10 | The Groundhogg — CRM, Newsletters, and Marketing Automation plugin for WordPress is vulnerable to Privilege Escalation i |
| CVE-2026-104752 | 7.2 | 2026-10-10 | The Rank Math SEO  WordPress plugin before 1.0.280 does not correctly validate the type of a file uploaded through its s |
| CVE-2026-104766 | 8.8 | 2026-10-10 | The Appointment Booking Plugin – LatePoint \| Calendar & Scheduling for WordPress plugin for WordPress is vulnerable to P |
| CVE-2026-104899 | 8.1 | 2026-10-10 | The GeoDirectory – WP Business Directory Plugin and Classified Listings Directory plugin for WordPress is vulnerable to  |
| CVE-2026-14335 | 7.2 | 2026-10-10 | The Easy Digital Downloads – eCommerce Payments and Subscriptions made easy plugin for WordPress is vulnerable to Stored |
| CVE-2026-77183 | 8.8 | 2026-10-10 | The FooSales – Point of Sale (POS) for WooCommerce plugin for WordPress is vulnerable to privilege escalation via accoun |
| CVE-2026-83526 | 8.8 | 2026-10-10 | The FV Player 8 plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 8.1.7  |
| CVE-2026-87780 | 8.8 | 2026-10-10 | The LTL Freight Quotes  WordPress plugin before 4.2.19 does not sanitise and escape values submitted through an unauthen |
| CVE-2026-87781 | 8.6 | 2026-10-10 | The LTL Freight Quotes  WordPress plugin before 4.2.19 does not sanitise and escape a parameter before using it in a SQL |
| CVE-2026-92975 | 8.1 | 2026-10-10 | The Groundhogg — CRM, Newsletters, and Marketing Automation plugin for WordPress is vulnerable to Privilege Escalation i |
| CVE-2026-93775 | 7.2 | 2026-10-10 | The Podlove Podcast Publisher plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Auphonic Webhook in  |
| CVE-2026-94256 | 8.1 | 2026-10-10 | The SMS Alert  WordPress plugin before 4.0.1 does not verify that the account being logged in is the one the verified on |
| CVE-2026-94257 | 8.1 | 2026-10-10 | The SMS Alert  WordPress plugin before 4.0.1 does not bind the account whose password is being changed to the phone numb |
| CVE-2026-96667 | 7.2 | 2026-10-10 | The Real Estate Manager – Property Listing and Agent Management plugin for WordPress is vulnerable to Stored Cross-Site  |
| CVE-2026-96682 | 7.2 | 2026-10-10 | The Presto Player plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Comment Content via <presto-play |
| CVE-2026-100161 | 7.2 | 2026-10-10 | The Photo Reviews for WooCommerce plugin for WordPress is vulnerable to Stored DOM-Based Cross-Site Scripting via the 'w |
| CVE-2026-100196 | 7.2 | 2026-10-10 | The LazyLoad Plugin – Lazy Load Images, Videos, and Iframes plugin for WordPress is vulnerable to Stored Cross-Site Scri |
| CVE-2026-104801 | 9.1 | 2026-10-10 | The PPOM – Product Addons & Custom Fields for WooCommerce plugin for WordPress is vulnerable to arbitrary file deletion  |
| CVE-2026-107742 | 7.2 | 2026-10-10 | The 10Web Booster – Website speed optimization, Cache & Page Speed optimizer plugin for WordPress is vulnerable to Store |
| CVE-2026-12626 | 7.2 | 2026-10-10 | The Online Scheduling and Appointment Booking System – Bookly plugin for WordPress is vulnerable to PHP Object Injection |
| CVE-2026-94538 | 8.1 | 2026-10-10 | The WP File Download plugin for WordPress is vulnerable to authorization bypass in all versions up to, and including, 6. |
| CVE-2026-95684 | 7.2 | 2026-10-10 | The VikBooking Hotel Booking Engine & PMS plugin for WordPress is vulnerable to Stored Cross-Site Scripting via 'attachm |
| CVE-2026-96558 | 7.2 | 2026-10-10 | The Quiz and Survey Master (QSM) – Quiz Maker & Survey Maker plugin for WordPress is vulnerable to Stored DOM-Based Cros |
| CVE-2026-96572 | 7.2 | 2026-10-10 | The WP Meteor Website Speed Optimization Addon plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Com |
| CVE-2026-96840 | 7.2 | 2026-10-10 | The Post Grid Gutenberg Blocks – PostX plugin for WordPress is vulnerable to Stored Cross-Site Scripting via display_nam |
| CVE-2026-100147 | 7.2 | 2026-10-10 | The FunnelKit – Funnel Builder for WooCommerce Checkout plugin for WordPress is vulnerable to Stored Cross-Site Scriptin |
| CVE-2026-100178 | 7.2 | 2026-10-10 | The WPAdverts – Classifieds Plugin plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'adverts_lo |
| CVE-2026-101920 | 7.2 | 2026-10-10 | The Molongui Authorship – Author Boxes, Guest Authors & Co-Authors for WordPress plugin for WordPress is vulnerable to S |
| CVE-2026-104759 | 8.1 | 2026-10-10 | The WPO365 \| SEAMLESS WORDPRESS + MICROSOFT INTEGRATION (WPO365 \| LOGIN) plugin for WordPress is vulnerable to Authentic |
| CVE-2026-104803 | 9.8 | 2026-10-10 | The WPCOM Member plugin for WordPress is vulnerable to Authentication Bypass in all versions up to, and including, 1.7.2 |
| CVE-2026-106606 | 7.2 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in YITH YITH WooCommerce Affiliates yith-woocommerce-affiliates allows O |
| CVE-2026-62045 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Booklovers booklovers allows Object Injection.This iss |
| CVE-2026-62046 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Gutentype gutentype allows Object Injection.This issue |
| CVE-2026-93746 | 7.5 | 2026-10-10 | The WebToffee WooCommerce PDF Invoices, Packing Slips, Delivery Notes & Shipping Labels plugin for WordPress is vulnerab |
| CVE-2026-93927 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in Axiomthemes Veto veto allows Object Injection.This issue affects Veto |
| CVE-2026-93929 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Travesia travesia allows Object Injection.This issue a |
| CVE-2026-93930 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Tantra tantra allows Object Injection.This issue affec |
| CVE-2026-93931 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Smash smash allows Object Injection.This issue affects |
| CVE-2026-93932 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Smart Casa smart-casa allows Object Injection.This iss |
| CVE-2026-93933 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Rosalinda rosalinda allows Object Injection.This issue |
| CVE-2026-93934 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Partiso partiso allows Object Injection.This issue aff |
| CVE-2026-93935 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Let's Play playhockey allows Object Injection.This iss |
| CVE-2026-93936 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in ThemeREX Group IPharm ipharm allows Object Injection.This issue affec |
| CVE-2026-93937 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Hygia hygia allows Object Injection.This issue affects |
| CVE-2026-93938 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Hogwords hogwords allows Object Injection.This issue a |
| CVE-2026-93940 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Greeny greeny allows Object Injection.This issue affec |
| CVE-2026-93941 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Edema edema allows Object Injection.This issue affects |
| CVE-2026-93942 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Dwell dwell allows Object Injection.This issue affects |
| CVE-2026-93943 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Convex convex allows Object Injection.This issue affec |
| CVE-2026-93944 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Camelia camelia allows Object Injection.This issue aff |
| CVE-2026-93945 | 9.8 | 2026-10-10 | Deserialization of Untrusted Data vulnerability in Axiomthemes Balance balance allows Object Injection.This issue affect |
| CVE-2026-93949 | 7.1 | 2026-10-10 | Authentication Bypass Using an Alternate Path or Channel vulnerability in Omegathemes Grocery Shopping Store grocery-sho |
| CVE-2026-93950 | 7.5 | 2026-10-10 | Missing Authorization vulnerability in StylemixThemes Motors motors allows Exploiting Incorrectly Configured Access Cont |
| CVE-2026-93951 | 7.1 | 2026-10-10 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Bracketweb Zeinet  |
| CVE-2026-96278 | 7.2 | 2026-10-10 | The WP Photo Album Plus plugin for WordPress is vulnerable to Stored Cross-Site Scripting via REQUEST_URI Session Histor |
| CVE-2026-96662 | 7.5 | 2026-10-10 | The Appointment Booking Plugin – LatePoint \| Calendar & Scheduling for WordPress plugin for WordPress is vulnerable to g |
| CVE-2026-96765 | 7.2 | 2026-10-10 | The WPO365 \| SEAMLESS WORDPRESS + MICROSOFT INTEGRATION (WPO365 \| LOGIN) plugin for WordPress is vulnerable to Stored Cr |
| CVE-2026-107657 | 7.2 | 2026-10-10 | The HivePress – Business Directory, Listings & Classified Ads Plugin plugin for WordPress is vulnerable to Stored Cross- |
| CVE-2026-91136 | 7.5 | 2026-10-10 | The Divi Plus plugin for WordPress is vulnerable to Arbitrary File Read in versions up to, and including, 2.4.0 via the  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2015-5477 | ISC / BIND | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2016-3081 | Apache / Struts | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2023-22894 | Strapi / Strapi | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2021-3199 | ONLYOFFICE / Docs | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2015-3306 | ProFTPD / ProFTPD | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2026-88779 | Citrix / NetScaler | 2026-10-04 | 2026-10-07 | Unknown |

---

*Total entries in CISA KEV catalog: 1739*