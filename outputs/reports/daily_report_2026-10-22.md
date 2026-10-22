# Vulnerability Intelligence Report

**Date:** 2026-10-22  
**Generated:** 2026-10-22T13:28:12Z  

---

## Executive Summary

Our environment faces significant exposure from 175 high-severity vulnerabilities, including two critical PHP memory-handling flaws (CVSS 9.8) and a perfect-score web shell upload vulnerability in WP Mailster (CVSS 10.0). Nine new entries were added to the CISA Known Exploited Vulnerabilities catalog this week, heavily targeting Plex Media Server. WordPress plugins account for multiple critical findings, including SQL injection and unrestricted file upload risks. While no monitored CVEs currently appear in the KEV catalog, the volume and severity of new findings demand immediate prioritization and remediation action.

---

## Risk Narrative

The current threat landscape reflects a convergence of infrastructure-level and application-layer risks. Critical PHP vulnerabilities expose server-side processing to memory corruption and state manipulation attacks, while multiple WordPress plugins introduce web shell upload and SQL injection vectors that threat actors commonly exploit for initial access and data exfiltration. The rapid addition of five Plex Media Server CVEs to the CISA KEV catalog signals active exploitation in the wild, elevating urgency for organizations running media services. Collectively, these vulnerabilities could enable attackers to achieve full system compromise, exfiltrate sensitive data, or establish persistent footholds, posing serious operational, reputational, and regulatory risk to the business.

---

## Prioritized Action Items

1. Immediately patch or disable WP Mailster and Mang Board WP plugins to eliminate CVSS 10.0 and 9.9 web shell upload vulnerabilities that allow full server compromise.
2. Apply available PHP patches or implement OOM error mitigations to address two CVSS 9.8 memory-handling vulnerabilities that could allow arbitrary code execution.
3. Patch or isolate all Plex Media Server instances immediately, as five related CVEs were added to the CISA KEV catalog this week indicating active exploitation.
4. Remediate the SQL injection vulnerability in Ajax Search Lite (CVSS 9.3) and the path traversal flaw in weForms (CVSS 7.5) to prevent unauthorized data access.
5. Conduct a full audit of all WordPress plugins in the environment and enforce a plugin approval policy to reduce ongoing exposure from third-party plugin vulnerabilities.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-109618 | 9.8 | 2026-10-21 | PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some co |
| CVE-2026-109619 | 9.8 | 2026-10-21 | PHP has various global state that temporarily points into request memory. In some scenarios, global state may not be cor |
| CVE-2026-114249 | 7.3 | 2026-10-21 | A vulnerability was detected in dhikshitha29 Insurance-Management-System 91de5edda5baa109ad8e9baf03ce6a3ceda84183/125362 |
| CVE-2026-111832 | 10.0 | 2026-10-21 | Unrestricted Upload of File with Dangerous Type vulnerability in WP Mailster WP Mailster wp-mailster allows Upload a Web |
| CVE-2026-111833 | 7.5 | 2026-10-21 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Bold Grid weForms weform |
| CVE-2026-111834 | 9.9 | 2026-10-21 | Unrestricted Upload of File with Dangerous Type vulnerability in Kitae Park Mang Board WP mangboard allows Upload a Web  |
| CVE-2026-111838 | 7.1 | 2026-10-21 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in ThemeHunk ThemeHun |
| CVE-2026-111840 | 7.1 | 2026-10-21 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in VideoWhisper.com P |
| CVE-2026-111848 | 7.1 | 2026-10-21 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Dylan Kuhn  Geo Ma |
| CVE-2026-111852 | 9.3 | 2026-10-21 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in WPdreams Ajax Sear |
| CVE-2026-112221 | 7.1 | 2026-10-21 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Brainstorm Force S |
| CVE-2026-113779 | 8.8 | 2026-10-21 | The pfSense REST API package is an unofficial, open-source REST and GraphQL API for pfSense CE and pfSense Plus firewall |
| CVE-2026-102483 | 7.5 | 2026-10-21 | Reachable exit in NTPsec ntpd 1.1.4 through 1.2.5 allows a remote attacker to terminate the daemon via an NTS request wi |
| CVE-2026-102486 | 7.5 | 2026-10-21 | Out-of-bounds read in NTS extension field parsing in NTPsec ntpd 1.1.4 through 1.2.5 allows a remote attacker to crash t |
| CVE-2026-114254 | 7.3 | 2026-10-21 | A vulnerability was identified in oretnom23 file-management-system-php up to 2e3c1ebe60f121e8df4fb3f544f0e9591d9a01e4. T |
| CVE-2026-114255 | 7.3 | 2026-10-21 | A security flaw has been discovered in oretnom23 file-management-system-php up to 2e3c1ebe60f121e8df4fb3f544f0e9591d9a01 |
| CVE-2026-114256 | 7.3 | 2026-10-21 | A weakness has been identified in oretnom23 file-management-system-php up to 2e3c1ebe60f121e8df4fb3f544f0e9591d9a01e4. A |
| CVE-2026-114257 | 7.3 | 2026-10-21 | A security vulnerability has been detected in oretnom23 file-management-system-php up to 2e3c1ebe60f121e8df4fb3f544f0e95 |
| CVE-2026-114476 | 7.5 | 2026-10-21 | Incorrect authorization in the REST administration API of Progressive Robot hMailServer 6.3.4 through 6.3.6 allows a rem |
| CVE-2026-114489 | 8.1 | 2026-10-21 | Missing authorization in the REST and COM administration APIs of Progressive Robot hMailServer 6.0.0 through 6.3.6 allow |
| CVE-2026-114490 | 7.8 | 2026-10-21 | Incorrect authorization in the COM administration API of Progressive Robot hMailServer 6.3.4 through 6.3.6 allows an acc |
| CVE-2026-114123 | 7.5 | 2026-10-21 | D365 F&O MCP Server is a Model Context Protocol server for querying Dynamics 365 Finance & Operations X++ code and metad |
| CVE-2026-114258 | 7.3 | 2026-10-21 | A vulnerability was detected in oretnom23 file-management-system-php up to 2e3c1ebe60f121e8df4fb3f544f0e9591d9a01e4. Aff |
| CVE-2026-114259 | 7.3 | 2026-10-21 | A flaw has been found in oretnom23 file-management-system-php up to 2e3c1ebe60f121e8df4fb3f544f0e9591d9a01e4. This affec |
| CVE-2026-114261 | 7.3 | 2026-10-21 | A vulnerability was found in MomoTommy file-management-system dc9ce1bf27f94b23d906cb1e86ce374dc94ca5df. This issue affec |
| CVE-2026-20043 | 9.0 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco owned Open Source Snort 3 Sof |
| CVE-2026-20236 | 7.5 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco owned Open Source Snort 3 Sof |
| CVE-2026-20291 | 7.8 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco owned Open Source Snort 3 Sof |
| CVE-2026-20356 | 7.5 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco owned Open Source Snort 3 Sof |
| CVE-2026-76466 | 9.8 | 2026-10-21 | A vulnerability in the database service feature of Cisco Expressway Series could allow an unauthenticated, remote attack |
| CVE-2026-76473 | 9.8 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, engineering teams for Cisco Emergency R |
| CVE-2026-76474 | 9.8 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, engineering teams for Cisco Emergency R |
| CVE-2026-76475 | 9.3 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, engineering teams for Cisco Emergency R |
| CVE-2026-76476 | 8.8 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, engineering teams for Cisco Emergency R |
| CVE-2026-76477 | 8.8 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, engineering teams for Cisco Emergency R |
| CVE-2026-76478 | 8.8 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, engineering teams for Cisco Emergency R |
| CVE-2026-76479 | 7.8 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, engineering teams for Cisco Emergency R |
| CVE-2026-76481 | 7.5 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, engineering teams for Cisco Emergency R |
| CVE-2026-76490 | 8.6 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Expressway Series software en |
| CVE-2026-76491 | 7.5 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Expressway Series software en |
| CVE-2026-76492 | 7.5 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Expressway Series software en |
| CVE-2026-76493 | 7.5 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Expressway Series software en |
| CVE-2026-76494 | 7.8 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Expressway Series software en |
| CVE-2026-76495 | 7.8 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Expressway Series software en |
| CVE-2026-76496 | 7.0 | 2026-10-21 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Expressway Series software en |
| CVE-2026-76505 | 7.5 | 2026-10-21 | A vulnerability in the IPv4 packet processing functionality of Cisco IOS XR Software that affects Cisco ASR 9000 and 990 |
| CVE-2026-76524 | 7.8 | 2026-10-21 | A vulnerability in the control channel socket implementation of&nbsp;Open Source Snort 3 could allow an authenticated, l |
| CVE-2026-110744 | 7.2 | 2026-10-21 | A flaw was found in multicluster-global-hub-operator-bundle. The operator is configured with overly broad role-based acc |
| CVE-2026-111183 | 9.8 | 2026-10-21 | GStreamer rtpL16depay Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote a |
| CVE-2026-111184 | 7.8 | 2026-10-21 | NoMachine Named Pipe Incorrect Permission Assignment Local Privilege Escalation Vulnerability. This vulnerability allows |
| CVE-2026-114262 | 7.3 | 2026-10-21 | A vulnerability was determined in file-management-system dc9ce1bf27f94b23d906cb1e86ce374dc94ca5df. Impacted is the funct |
| CVE-2026-114263 | 7.3 | 2026-10-21 | A vulnerability was identified in ProjectWorlds Advanced Library Management System 1.0. The affected element is the func |
| CVE-2026-114493 | 8.6 | 2026-10-21 | LocalAI v4.6.0 through v4.11.0 contains a server-side request forgery vulnerability in core/gallery/gallery.go that vali |
| CVE-2026-89035 | 7.4 | 2026-10-21 | MikroTik RouterOS through 7.24.5 contains a session token replay vulnerability in the WebFig interface that allows attac |
| CVE-2026-92183 | 7.8 | 2026-10-21 | GIMP APNG File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote |
| CVE-2026-92202 | 7.8 | 2026-10-21 | Luxion KeyShot BIP File Parsing Uncontrolled Search Path Element Remote Code Execution Vulnerability. This vulnerability |
| CVE-2026-92203 | 7.7 | 2026-10-21 | Airbyte SharePoint Connector _get_shared_drive_object Server-Side Request Forgery Information Disclosure Vulnerability.  |
| CVE-2026-92204 | 7.7 | 2026-10-21 | Airbyte OneDrive Connector _get_shared_drive_object Server-Side Request Forgery Information Disclosure Vulnerability. Th |
| CVE-2026-92206 | 8.8 | 2026-10-21 | CrewAI crewAI Framework Agent Loading Unsafe Reflection Remote Code Execution Vulnerability. This vulnerability allows r |
| CVE-2026-92207 | 8.8 | 2026-10-21 | MindsDB OpenBBtable Code Injection Remote Code Execution Vulnerability. This vulnerability allows remote attackers to ex |
| CVE-2026-92208 | 8.8 | 2026-10-21 | NoMachine mDNS Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows network-adjacen |
| CVE-2026-92209 | 7.8 | 2026-10-21 | NoMachine Redis Improper Authentication Local Privilege Escalation Vulnerability. This vulnerability allows local attack |
| CVE-2026-92210 | 7.2 | 2026-10-21 | NoMachine nxhtd Server-Side Request Forgery Information Disclosure Vulnerability. This vulnerability allows remote attac |
| CVE-2025-31699 | 8.9 | 2026-10-21 | Apache Traffic Server can return an origin connection to the shared pool while the origin is still waiting on a request  |
| CVE-2025-55702 | 8.7 | 2026-10-21 | When a client sends a POST with Expect: 100-continue and the origin answers before reading the body, Apache Traffic Serv |
| CVE-2026-111804 | 8.2 | 2026-10-21 | Apache Traffic Server's experimental wasm plugin has a use-after-free in its transaction-close handler and forwards unva |
| CVE-2026-111813 | 10.0 | 2026-10-21 | Apache Traffic Server's experimental magick plugin lets an unauthenticated client control ImageMagick convert arguments  |
| CVE-2026-111816 | 9.3 | 2026-10-21 | Apache Traffic Server forwarded a malformed 302 response that should have been rejected as a parse error, because the Tr |
| CVE-2026-113870 | 8.8 | 2026-10-21 | MongoDB Compass improperly escapes certain BSON values when converting a stored view’s aggregation pipeline into editabl |
| CVE-2026-114267 | 7.3 | 2026-10-21 | A vulnerability was detected in SourceCodester Food Order Management System 1.0. Affected is an unknown function of the  |
| CVE-2026-114268 | 9.9 | 2026-10-21 | A flaw has been found in Tenda BE3L Pro 16.03.60.62. Affected by this vulnerability is the function formWifiBasicSet of  |
| CVE-2026-19676 | 7.8 | 2026-10-21 | The user-mode verifier for the peci_transfer() system call, z_vrfy_peci_transfer() in drivers/peci/peci_handlers.c, chec |
| CVE-2026-78118 | 7.0 | 2026-10-21 | The kernel helper z_waitq_head() (kernel/include/wait_q.h) reads the head of a thread wait queue, but on SMP systems it  |
| CVE-2026-79976 | 7.1 | 2026-10-21 | The MCTP-over-I2C+GPIO target binding in subsys/pmci/mctp/mctp_i2c_gpio_target.c emulates a small pseudo-register file,  |
| CVE-2026-111805 | 8.6 | 2026-10-21 | Apache Traffic Server can be used to exhaust an HTTP/1.1 origin's worker pool via a truncated HTTP/2 Content-Length valu |
| CVE-2026-111808 | 8.6 | 2026-10-21 | Apache Traffic Server can be used to exhaust an HTTP/1.1 origin's worker pool via a malformed padded HTTP/2 DATA frame.
 |
| CVE-2026-111809 | 9.3 | 2026-10-21 | Apache Traffic Server allows request smuggling via HEAD requests that carry Content-Length or Transfer-Encoding.



This |
| CVE-2026-111810 | 7.5 | 2026-10-21 | Apache Traffic Server 9.2.15, 10.1.4 and 10.2.0 write one unthrottled diagnostic log line for every internal @ header th |
| CVE-2026-111811 | 9.0 | 2026-10-21 | Apache Traffic Server's experimental tsmemcache plugin allows unauthenticated network read, write, and deletion of the s |
| CVE-2026-111812 | 10.0 | 2026-10-21 | Apache Traffic Server's origin_server_auth plugin lets a client force signing of attacker-chosen AWS request headers und |
| CVE-2026-111814 | 10.0 | 2026-10-21 | Apache Traffic Server's default outbound session-sharing policy can reuse a pooled TLS session authenticated with one cl |
| CVE-2026-111815 | 10.0 | 2026-10-21 | Apache Traffic Server can resume a TLS session across SNI virtual hosts without re-verifying a client certificate requir |
| CVE-2026-112408 | 8.1 | 2026-10-21 | Missing verification of source of a communication channel in the default_bucket() function in Amazon SageMaker Python SD |
| CVE-2026-114135 | 8.8 | 2026-10-21 | Jupyter Server is the backend for Jupyter web applications. From 2.0.0 until 2.6.0, enabling GatewayClient.url replaced  |
| CVE-2026-114136 | 7.5 | 2026-10-21 | Django REST framework is a toolkit for building Web APIs. From 3.6.4 until 3.18.2, JSONParser.parse in rest_framework/pa |
| CVE-2026-114137 | 7.4 | 2026-10-21 | Django REST framework is a toolkit for building Web APIs. From 3.12.0 until 3.18.2, TokenProxy.delete() in rest_framewor |
| CVE-2026-114138 | 7.5 | 2026-10-21 | Django REST framework is a toolkit for building Web APIs. Prior to 3.18.2, DefaultContentNegotiation.get_accept_list in  |
| CVE-2026-114144 | 7.5 | 2026-10-21 | toml-node is a TOML parser for Node.js and the browser. Prior to 5.0.1, toml.parse() passes unbounded hexadecimal, octal |
| CVE-2026-114145 | 7.5 | 2026-10-21 | GitPython is a python library used to interact with Git repositories. Prior to 3.2.1, create_submodule() in git/objects/ |
| CVE-2026-29001 | 7.2 | 2026-10-21 | TastyIgniter through 4.4.5 contain a PHP object injection vulnerability that allows authenticated administrators to achi |
| CVE-2026-96639 | 9.8 | 2026-10-21 | Pillow is a Python imaging library. From 11.0.0 until 13.0.0, multi-frame loaders can retain an ImagingCore allocation c |
| CVE-2026-114382 | 10.0 | 2026-10-21 | A security flaw has been discovered in TOTOLINK EX200 5.2.3c.7200. This affects the function setStaticDhcpConfig of the  |
| CVE-2026-114383 | 10.0 | 2026-10-21 | A weakness has been identified in TOTOLINK EX200 5.2.3c.7200. This impacts the function setWiFiAclAddConfig of the file  |
| CVE-2026-91403 | 9.1 | 2026-10-21 | Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition product of Oracle Java SE |
| CVE-2026-114439 | 7.3 | 2026-10-21 | A vulnerability was determined in oretnom23 php-travel-agency-system. Affected by this issue is some unknown functionali |
| CVE-2026-114440 | 7.3 | 2026-10-21 | A vulnerability was identified in oretnom23 php-travel-agency-system. This affects an unknown part of the file admin/del |
| CVE-2026-114441 | 7.3 | 2026-10-21 | A weakness has been identified in oretnom23 php-travel-agency-system. This issue affects some unknown processing of the  |
| CVE-2026-76288 | 7.5 | 2026-10-21 | In Splunk Enterprise versions below 10.4.4, 10.2.8, 10.0.11, and 9.4.16, an unauthenticated user could send a single cra |
| CVE-2026-76290 | 7.5 | 2026-10-21 | In Splunk Enterprise versions below 10.4.4, 10.2.8, and 10.0.11, an unauthenticated user could send repeated requests to |
| CVE-2026-76291 | 8.8 | 2026-10-21 | In Splunk Enterprise versions below 10.4.4, 10.2.8, 10.0.11, and 9.4.16, a user that holds a role with the schedule_sear |
| CVE-2026-76293 | 7.2 | 2026-10-21 | In Splunk Enterprise versions below 10.4.3, 10.2.8, 10.0.11, and 9.4.16, a user that holds a role with the edit_manager_ |
| CVE-2026-76298 | 8.8 | 2026-10-21 | In Splunk Enterprise versions below 10.4.4 and 10.2.8, a user who does not hold the "admin" or "power" Splunk roles coul |
| CVE-2026-76306 | 7.5 | 2026-10-21 | In Splunk SOAR versions below 8.7.0, a user that has the "Observer" role could use query filters in the Representational |
| CVE-2026-76307 | 7.2 | 2026-10-21 | In Splunk SOAR versions below 8.7.0, a user that holds a role with the Users and Roles view permission could use the Rep |
| CVE-2026-110264 | 10.0 | 2026-10-22 | An issue has been discovered in GitLab CE/EE affecting all versions from 7.0 before 18.11.13, 19.0 before 19.0.10, 19.1  |
| CVE-2026-112212 | 7.5 | 2026-10-22 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 18.3 before 19.3.6, 19.4 before 19.4.3, and 1 |
| CVE-2026-114575 | 10.0 | 2026-10-22 | A flaw has been found in TOTOLINK A950RG 4.1.2cu.5268_B20221104. Affected by this issue is the function UploadCustomModu |
| CVE-2026-15723 | 8.2 | 2026-10-22 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 10.1 before 19.3.6, 19.4 before 19.4.3, and 1 |
| CVE-2026-114577 | 7.3 | 2026-10-22 | A vulnerability was found in oretnom23 php-travel-agency-system. This vulnerability affects unknown code of the file adm |
| CVE-2026-114635 | 8.7 | 2026-10-22 | Traefik before v2.11.58 and v3.7.14 contains an authentication bypass vulnerability in its SNI check, which is skipped w |
| CVE-2026-114636 | 8.7 | 2026-10-22 | Traefik v3.7.13 before v3.7.14 contains an access-control bypass in the Kubernetes Ingress NGINX provider, where the HTT |
| CVE-2026-114637 | 8.7 | 2026-10-22 | Traefik from v3.2.0 before v3.7.14 contains an authentication bypass vulnerability in the experimental FastProxy connect |
| CVE-2026-114638 | 8.7 | 2026-10-22 | Traefik v3.7.0 before v3.7.14 contains an improper authentication vulnerability in the Kubernetes Ingress NGINX provider |
| CVE-2026-114639 | 8.7 | 2026-10-22 | Traefik 2.11.0 before 2.11.58 and 3.0.0 before 3.7.14 contains an authentication bypass because a first request preauthe |
| CVE-2026-114640 | 8.7 | 2026-10-22 | Traefik from v3.7.0 before v3.7.14 contains an authentication bypass vulnerability in its Kubernetes Ingress-NGINX provi |
| CVE-2026-114642 | 8.7 | 2026-10-22 | Traefik 2.11.0 before 2.11.58 and 3.0.0 before 3.7.14 stores its NTLM/Kerberos backend round tripper in a client-connect |
| CVE-2026-114656 | 7.5 | 2026-10-22 | Traefik before 2.11.58 and 3.7.13 contains an authentication bypass vulnerability that allows unauthenticated clients to |
| CVE-2026-114658 | 8.8 | 2026-10-22 | Grav Login plugin from 3.6.0 before 3.9.13 contains a missing authorization vulnerability in the login.invite task that  |
| CVE-2026-114661 | 8.5 | 2026-10-22 | OpenRemote 1.2.0 before 1.31.0 contains a missing authorization vulnerability in GatewayServiceResource that allows any  |
| CVE-2026-114662 | 8.1 | 2026-10-22 | Obot before 0.26.0 contains an authentication bypass vulnerability in the CLI login flow that allows unauthenticated att |
| CVE-2026-114663 | 8.4 | 2026-10-22 | Vyper 0.4.0b1 through 0.5.0b1 miscompiles unfoldable constants and omitted default arguments from imported modules, beca |
| CVE-2026-114664 | 7.1 | 2026-10-22 | Frappe Framework before 16.33.0 contains a blind SQL injection vulnerability in the frappe.desk.doctype.event.event.get_ |
| CVE-2026-114716 | 8.5 | 2026-10-22 | Roundcube Webmail before 1.6.20 and 1.7.x before 1.7.5 is affected by a mail header injection vulnerability. rcmail_send |
| CVE-2026-114720 | 7.1 | 2026-10-22 | Roundcube Webmail before 1.6.20 and 1.7.x before 1.7.5 is affected by an IMAP command injection vulnerability. A remote  |
| CVE-2026-114724 | 7.4 | 2026-10-22 | Roundcube Webmail before 1.6.20 and 1.7.x before 1.7.5 contains an object injection primitive in rcube_session::unserial |
| CVE-2026-114727 | 8.3 | 2026-10-22 | Roundcube Webmail before 1.6.20 and 1.7.x before 1.7.5 passes potentially unsafe content into ImageMagick when resizing  |
| CVE-2026-110353 | 7.5 | 2026-10-22 | HAProxy 3.2 before 3.4.6 allows a remote unauthenticated attacker to cause a denial of service (worker-thread CPU exhaus |
| CVE-2026-110354 | 7.5 | 2026-10-22 | HAProxy 3 before 3.4.6 allows a remote unauthenticated attacker to cause a denial of service (persistent worker-thread C |
| CVE-2026-114730 | 7.2 | 2026-10-22 | Roundcube Webmail 1.6.14 before 1.6.20 and 1.7.0 before 1.7.5 is affected by a server-side request forgery filter bypass |
| CVE-2026-114219 | 7.4 | 2026-10-22 | NT OneAPP developed by NewType Infortech has a Hard-coded Credentials vulnerability. Unauthenticated remote attackers ca |
| CVE-2026-114220 | 9.1 | 2026-10-22 | NT OneAPP developed by NewType Infortech has an Improper Certificate Validation vulnerability. Unauthenticated network-a |
| CVE-2026-114221 | 7.4 | 2026-10-22 | NT OneAPP developed by NewType Infortech has a Credential Disclosure vulnerability. Unauthenticated remote attackers can |
| CVE-2026-109927 | 7.2 | 2026-10-22 | The HIPAA Forms WordPress plugin before 3.3.2 does not perform a capability check when handling a request that rebuilds  |
| CVE-2026-109987 | 7.2 | 2026-10-22 | The PixelYourSite  WordPress plugin before 11.4.3, PixelYourSite Pro WordPress plugin before 12.6.8 do not sanitise and  |
| CVE-2026-111958 | 7.5 | 2026-10-22 | The Royal MCP  WordPress plugin before 1.5.7 does not limit a preview-link token to the single preview it was issued for |
| CVE-2026-97328 | 7.5 | 2026-10-22 | The WebP Express WordPress plugin before 0.25.16 does not escape values that its bundled HTML parser re-emits into eleme |
| CVE-2026-114177 | 8.8 | 2026-10-22 | Cross-Site Request Forgery (CSRF) vulnerability in Xpro Xpro Elementor Addons xpro-elementor-addons allows Cross Site Re |
| CVE-2026-111830 | 7.1 | 2026-10-22 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WP Mailster WP Mai |
| CVE-2026-111851 | 7.6 | 2026-10-22 | Use of Externally-Controlled Input to Select Classes or Code ('Unsafe Reflection') vulnerability in WProyal Royal Elemen |
| CVE-2026-112241 | 9.8 | 2026-10-22 | Authentication Bypass by Spoofing vulnerability in Brainstorm Force SureCart surecart allows Authentication Abuse.This i |
| CVE-2026-112242 | 8.8 | 2026-10-22 | Incorrect Privilege Assignment vulnerability in Cozmoslabs Profile Builder profile-builder allows Privilege Escalation.T |
| CVE-2026-112312 | 7.5 | 2026-10-22 | Missing Authorization vulnerability in ACF Extended ACF Extended acf-extended allows Exploiting Incorrectly Configured A |
| CVE-2026-112327 | 9.3 | 2026-10-22 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in TMS Amelia ameliab |
| CVE-2026-112379 | 7.1 | 2026-10-22 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Codepeople Contact |
| CVE-2026-112085 | 8.2 | 2026-10-22 | webpack-dev-server is a development server that provides live reloading for webpack projects. In versions before 5.2.7 a |
| CVE-2017-20287 | 7.5 | 2026-10-22 | Javo Spot theme for WordPress before 3.0.0 contains a path traversal vulnerability that allows unauthenticated attackers |
| CVE-2017-20289 | 7.5 | 2026-10-22 | Broadstreet Ad Widget plugin for WordPress 2.2.0 before 2.12.0 contains a local file inclusion vulnerability that allows |
| CVE-2018-25438 | 7.5 | 2026-10-22 | Intermesh Group-Office 3.3.0 before 3.5.5 contains an unauthenticated path traversal vulnerability in compress.php that  |
| CVE-2018-25439 | 7.5 | 2026-10-22 | MetInfo CMS 6.0.0 before 6.1.1 contains a path traversal vulnerability in /include/thumb.php that allows unauthenticated |
| CVE-2019-25778 | 8.2 | 2026-10-22 | SeaCMS through 8.7 contains an unauthenticated SQL injection vulnerability that allows remote attackers to manipulate da |
| CVE-2019-25779 | 7.5 | 2026-10-22 | WooThemes Diarise through 1.5.9 contains a file read vulnerability that allows unauthenticated attackers to read arbitra |
| CVE-2021-48013 | 7.5 | 2026-10-22 | Weaver E-cology 8.0 contains a path traversal vulnerability that allows unauthenticated attackers to read arbitrary file |
| CVE-2021-48014 | 9.8 | 2026-10-22 | FineReport 9.0 contains a path traversal vulnerability in the /WebReport/ReportServer design_save_svg operation that all |
| CVE-2021-48015 | 7.5 | 2026-10-22 | JeeWMS before commit 0a610e8 contains an unauthenticated path traversal vulnerability that allows remote attackers to re |
| CVE-2021-48016 | 9.8 | 2026-10-22 | DedeCMS through 5.8.1-beta contains a PHP code injection vulnerability in ShowMsg() where the HTTP Referer header is wri |
| CVE-2021-48017 | 7.5 | 2026-10-22 | OrbiTeam BSCW Server 5.x before 5.2.5 and 7.x before 7.4.4 contains an unauthenticated path traversal vulnerability in t |
| CVE-2022-51021 | 8.2 | 2026-10-22 | NotificationX plugin for WordPress 2.0.0 before 2.3.12 contains an unauthenticated SQL injection vulnerability that allo |
| CVE-2022-51022 | 9.1 | 2026-10-22 | YiShaAdmin 2.2 through 3.1, fixed in commit 025b062, contains an unauthenticated path traversal vulnerability in the /ad |
| CVE-2022-51023 | 8.2 | 2026-10-22 | PHPOK 4.5.000 before 5.4.081 contains an SQL injection vulnerability that allows unauthenticated attackers to manipulate |
| CVE-2022-51024 | 7.5 | 2026-10-22 | Kavita 0.5.2 before 0.5.4.1 contains a path traversal vulnerability that allows unauthenticated attackers to read arbitr |
| CVE-2024-58393 | 8.2 | 2026-10-22 | i-Netsolution Readymade Unilevel Ecommerce MLM (2024-03-15 build) contains an SQL injection vulnerability that allows un |
| CVE-2024-58396 | 7.5 | 2026-10-22 | YouDataSum CPAS Audit Management System V4 contains a path traversal vulnerability that allows unauthenticated attackers |
| CVE-2025-71434 | 8.2 | 2026-10-22 | Weaver E-cology 8.0, 9.0, and 10.0 prior to 10.76 contains an unauthenticated SQL injection vulnerability in the /api/do |
| CVE-2026-111079 | 7.4 | 2026-10-22 | A flaw was found in Goose. When the terminal integration feature is enabled, the application captures shell command hist |
| CVE-2026-112313 | 7.1 | 2026-10-22 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in ACF Extended ACF E |
| CVE-2026-112820 | 8.1 | 2026-10-22 | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability in |
| CVE-2026-112822 | 8.5 | 2026-10-22 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in AmentoTech Workrea |
| CVE-2026-112832 | 9.8 | 2026-10-22 | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability in |
| CVE-2026-115323 | 7.3 | 2026-10-22 | EverShop 1.2.2 before 2.2.1 contains a missing authorization vulnerability in the customer address API that allows unaut |
| CVE-2026-115324 | 8.1 | 2026-10-22 | mem0 0.1.117 before 1.0.8 contains an sql injection vulnerability in mem0/vector_stores/databricks.py that allows attack |
| CVE-2026-115325 | 8.3 | 2026-10-22 | Netmaker through 1.7.0 contains an authorization bypass vulnerability in the updateExtClient handler that allows network |
| CVE-2026-115328 | 8.8 | 2026-10-22 | JSON-SCADA before 0.65-alpha contains an sql injection vulnerability in opcApi() in src/server_realtime_auth/index.js th |
| CVE-2026-115330 | 8.8 | 2026-10-22 | Lotus through 0.10.2 contains an sql injection vulnerability that allows authenticated organization users to execute arb |
| CVE-2026-115331 | 8.8 | 2026-10-22 | Lotus through 0.10.2 contains an sql injection vulnerability that allows authenticated organization users to inject SQL  |
| CVE-2026-115332 | 8.8 | 2026-10-22 | Lotus through 0.10.2 contains an sql injection vulnerability that allows authenticated organization users to inject SQL  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-106931 | EG Secure Solutions / SiteGuard Server Edition | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96656 | Plex / Media Server | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96655 | Plex / Media Server | 2026-10-20 | 2026-11-03 | Unknown |
| CVE-2026-96654 | Plex / Media Server | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96652 | Plex / Media Server | 2026-10-20 | 2026-11-03 | Unknown |
| CVE-2026-110936 | Siemens / Software Center | 2026-10-20 | 2026-11-03 | Unknown |
| CVE-2026-102764 | BeyondTrust / Remote Support | 2026-10-16 | 2026-10-19 | Unknown |
| CVE-2025-61624 | Fortinet / Multiple Products | 2026-10-16 | 2026-10-19 | Unknown |
| CVE-2026-21589 | Atlassian / Multiple Products | 2026-10-15 | 2026-10-18 | Unknown |

---

*Total entries in CISA KEV catalog: 1754*