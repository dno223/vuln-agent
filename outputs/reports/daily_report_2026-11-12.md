# Vulnerability Intelligence Report

**Date:** 2026-11-12  
**Generated:** 2026-11-12T16:35:03Z  

---

## Executive Summary

Our environment faces significant exposure across 296 high-severity vulnerabilities, with 11 newly added CISA Known Exploited Vulnerabilities (KEVs) requiring immediate remediation. The most critical finding is CVE-2026-110697, a CVSS 9.9 SQL injection flaw in Quay that could allow attackers to manipulate database queries via robot account functions. Multiple Progress Kendo UI for jQuery vulnerabilities introduce cross-site scripting risks across widely used UI components. Additionally, Lenovo device vulnerabilities expose endpoints to privilege escalation. The active exploitation of Microsoft Office, Cisco BroadWorks, and Barracuda products—confirmed by CISA KEV additions—heightens our overall risk posture and demands prioritized patching action.

---

## Risk Narrative

The current threat landscape reflects active exploitation of enterprise platforms including Microsoft Office, Cisco BroadWorks, and Barracuda security appliances—products commonly trusted at the network perimeter. CISA's KEV additions signal confirmed, real-world exploitation, dramatically increasing the likelihood of breach if unpatched. The near-perfect CVSS 9.9 SQL injection in Quay poses critical data integrity and confidentiality risks for container registry operations. Widespread Kendo UI XSS vulnerabilities could enable session hijacking and credential theft across web-facing applications. Lenovo privilege escalation flaws on endpoints provide attackers a foothold for lateral movement. Collectively, these vulnerabilities span the attack surface from endpoints to servers to web applications, creating compounded business risk including data breach, operational disruption, and regulatory non-compliance.

---

## Prioritized Action Items

1. Immediately patch or mitigate CVE-2026-110697 (CVSS 9.9) in Quay by restricting robot account namespace inputs and applying vendor fixes to prevent SQL injection exploitation.
2. Apply all available patches for the 11 newly added CISA KEV entries, prioritizing Microsoft Office, Barracuda ESG, and Cisco BroadWorks systems within 24–48 hours per CISA binding guidance.
3. Upgrade Progress Kendo UI for jQuery to version 2026.4.1111 or later to remediate all six identified XSS and markup injection vulnerabilities across UI components.
4. Deploy patches for Lenovo vulnerabilities CVE-2026-116633 and CVE-2026-77873 to prevent local privilege escalation and unauthorized file write attacks on Lenovo endpoints.
5. Conduct a full audit of the remaining high-severity CVE backlog to identify any additional assets matching KEV catalog entries and establish a risk-prioritized remediation roadmap.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-110697 | 9.9 | 2026-11-11 | A flaw was found in Quay where the robot account listing function constructs a SQL LIKE pattern from user-controlled nam |
| CVE-2026-116633 | 7.1 | 2026-11-11 | A potential vulnerability was reported in some Lenovo Tablets that could allow a third-party application to perform an a |
| CVE-2026-124687 | 7.1 | 2026-11-11 | In Progress® Kendo® UI for jQuery versions from 2022.2.621 prior to 2026.4.1111 the DropDownButton and SplitButton allow |
| CVE-2026-124688 | 7.1 | 2026-11-11 | In Progress® Kendo® UI for jQuery prior to 2026.4.1111 the TabStrip, PanelBar, and Menu widgets support mapping a dataSo |
| CVE-2026-124689 | 7.1 | 2026-11-11 | In Progress Kendo UI for jQuery versions 2026.3.1014 up to, but not including, 2026.4.1110, ActionSheet does not encode  |
| CVE-2026-124690 | 7.1 | 2026-11-11 | In Progress Kendo UI for jQuery, sanitizeSvgContent() parses custom icon markup into a live DOM before filtering it. An  |
| CVE-2026-124692 | 7.1 | 2026-11-11 | In Progress Kendo UI for jQuery versions 2026.3.1015 up to, but not including, 2026.4.1110, the Grid and TreeList column |
| CVE-2026-124693 | 7.1 | 2026-11-11 | In Progress Kendo UI for jQuery versions 2026.3.1015 up to, but not including, 2026.4.1110, PivotGrid and PivotConfigura |
| CVE-2026-124694 | 7.1 | 2026-11-11 | In Progress Kendo UI for jQuery versions 2026.3.1015 up to, but not including, 2026.4.1110, PropertyGrid does not encode |
| CVE-2026-77873 | 7.3 | 2026-11-11 | An improper permissions vulnerability was reported in Lenovo System Update that could allow a local authenticated user t |
| CVE-2026-77882 | 7.8 | 2026-11-11 | A deserialization of untrusted data vulnerability was discovered in Lenovo System Update that could allow a local authen |
| CVE-2026-89061 | 7.8 | 2026-11-11 | During an internal security assessment, a potential vulnerability was discovered in Lenovo PC Manager, distributed exclu |
| CVE-2026-106137 | 8.6 | 2026-11-11 | In affected versions of Progress® Telerik® UI for ASP.NET MVC `2012.2.710` through `2026.3.811`, ClassFactory updates a  |
| CVE-2026-106152 | 8.8 | 2026-11-11 | In Progress® Telerik® Report Server prior to version 12.3.26.1110, an external control of a system configuration setting |
| CVE-2026-106156 | 8.6 | 2026-11-11 | In Progress® Telerik® UI for ASP.NET Core versions `2015.1.318` through `2026.3.811`, repeated server-side aggregation r |
| CVE-2026-107247 | 8.1 | 2026-11-11 | An authorization bypass in Revive Adserver 6.0.0 through 6.0.8 allows an authenticated manager restricted to one agency  |
| CVE-2026-107662 | 8.8 | 2026-11-11 | Blind SQL injection in Revive Adserver 6.0.8 and earlier allows an authenticated manager restricted to one agency to ext |
| CVE-2026-62971 | 7.2 | 2026-11-11 | The OWASP core rule set (CRS) is a set of generic attack detection rules for use with compatible web application firewal |
| CVE-2026-91870 | 7.4 | 2026-11-11 | Dell Ansible Storage for PowerFlex, versions prior to 3.2.0, contains an Improper Certificate Validation vulnerability i |
| CVE-2026-91871 | 7.4 | 2026-11-11 | Dell Ansible Storage for PowerStore, versions prior to 3.9.0, contains an Improper Certificate Validation vulnerability  |
| CVE-2026-91879 | 8.8 | 2026-11-11 | Dell Terraform for ObjectScale and Powerstore, versions prior to 1.1.1 (ObjectScale) and versions 1.2.1 through 1.3.0 (P |
| CVE-2026-91890 | 8.7 | 2026-11-11 | Dell Ansible Storage for Unity , versions prior to 1.2.13 contains an Improper Certificate Validation vulnerability in t |
| CVE-2026-108472 | 7.8 | 2026-11-11 | A flaw was found in the xfs_admin utility in xfsprogs. The tool does not properly validate user-supplied parameters, all |
| CVE-2026-123747 | 7.3 | 2026-11-11 | A flaw was found in pappl-retrofit. The application fails to properly sanitize user-supplied filenames when handling the |
| CVE-2026-123863 | 8.2 | 2026-11-11 | A reachable assertion in Node.js HTTP/2 session teardown lets any unauthenticated client abort the server, over both TLS |
| CVE-2026-123864 | 8.1 | 2026-11-11 | A re-entrancy flaw in Node.js HTTPS lets an unauthenticated client read memory belonging to other connections, including |
| CVE-2026-123865 | 7.5 | 2026-11-11 | An unauthenticated HTTP/2 client can permanently leak Node.js server memory and file descriptors. If a peer triggers a p |
| CVE-2026-123866 | 7.5 | 2026-11-11 | A use-after-free in Node.js HTTP/2 stream teardown can leak response memory, including the contents of other connections |
| CVE-2026-123872 | 8.1 | 2026-11-11 | A client certificate authentication bypass in Node.js TLS lets a client change the servername during TLS 1.2 renegotiati |
| CVE-2026-123874 | 7.5 | 2026-11-11 | A use-after-free in Node.js HTTP/2 lets an unauthenticated client corrupt server memory, over both TLS and cleartext, wh |
| CVE-2026-126051 | 7.5 | 2026-11-11 | A deferred-callback use-after-destroy in Node.js TLS server handshake handling allows a remote, unauthenticated attacker |
| CVE-2026-126768 | 9.8 | 2026-11-11 | OpsTree REMS through 1.0.0 contains an authentication bypass vulnerability that allows unauthenticated attackers to obta |
| CVE-2026-126769 | 7.5 | 2026-11-11 | OpsTree REMS through 1.0.0 contains a missing authentication vulnerability that allows unauthenticated remote attackers  |
| CVE-2026-126774 | 8.2 | 2026-11-11 | @tinacms/mdx before 2.4.2 contains a code injection vulnerability in its MDX serializer, which writes rich-text values i |
| CVE-2026-126777 | 7.4 | 2026-11-11 | Traccar 3.15 before 6.17.0 contains an authentication bypass vulnerability in LdapProvider.login() that fails to reject  |
| CVE-2026-126779 | 7.5 | 2026-11-11 | Spatie Browsershot 2.2.0 before 5.5.0 contains a local file read vulnerability that allows attackers to read server file |
| CVE-2026-126780 | 7.2 | 2026-11-11 | Webmin through 2.670 contains a privilege escalation vulnerability in acl/save_group.cgi that allows delegated administr |
| CVE-2026-126781 | 7.5 | 2026-11-11 | Webmin through 2.670 contains a users file injection vulnerability in acl/cert_issue.cgi that allows authenticated Webmi |
| CVE-2026-58505 | 7.5 | 2026-11-11 | geojson-vt is a JavaScript library for slicing GeoJSON data into vector tiles on the fly, primarily designed to enable r |
| CVE-2026-65840 | 9.6 | 2026-11-11 | Fider is a feedback portal for feature requests and suggestions. Prior to version 0.36.0, in multi-tenant mode (HOST_MOD |
| CVE-2026-65967 | 7.1 | 2026-11-11 | Fider is a feedback portal for feature requests and suggestions. Prior to version 0.34.0, a Server-Side Request Forgery  |
| CVE-2026-76079 | 7.2 | 2026-11-11 | Probo is a self-hostable governance, risk, and compliance (GRC) platform built for engineering and security teams. Prior |
| CVE-2026-91150 | 7.5 | 2026-11-11 | A flaw was found in Cockpit. This vulnerability allows a remote attacker, without prior authentication, to send speciall |
| CVE-2026-91873 | 8.7 | 2026-11-11 | Dell OpenManage Ansible Modules, versions 2.1.2 through 10.0.3, contains an Improper Certificate Validation vulnerabilit |
| CVE-2026-91874 | 8.7 | 2026-11-11 | Dell OpenManage Ansible Modules, versions 5.0.0 through 10.0.3, contains an Improper Certificate Validation vulnerabilit |
| CVE-2026-91875 | 8.7 | 2026-11-11 | Dell OpenManage Ansible Modules, versions 9.2.0 through 10.0.3, contains an Improper Certificate Validation vulnerabilit |
| CVE-2026-91877 | 7.6 | 2026-11-11 | Dell OpenManage Ansible Modules, versions 2.0.2 through 10.0.3, contains an Improper Neutralization of Special Elements  |
| CVE-2026-91878 | 7.6 | 2026-11-11 | Dell OpenManage Ansible Modules, versions 6.0.0 through 10.0.3, contains an Improper Neutralization of Special Elements  |
| CVE-2026-91880 | 8.9 | 2026-11-11 | Dell Terraform Provider for PowerFlex, versions 1.5.0 through 1.8.0, contains an Improper Certificate Validation vulnera |
| CVE-2026-91891 | 7.5 | 2026-11-11 | Dell Terraform Provider for PowerStore, versions prior to 1.3.1 , contains a  vulnerability that may cause sensitive aut |
| CVE-2026-122095 | 7.6 | 2026-11-11 | AsiaInfo BSS Platform 9.2 before 9.2.38 has a stored cross-site scripting (XSS) vulnerability in the menu icon upload fu |
| CVE-2026-126815 | 8.1 | 2026-11-11 | Pre-account hijacking in the authentication flow in Lagarto Chivato 0.4.1 and earlier on Web allows remote unauthenticat |
| CVE-2026-91151 | 7.3 | 2026-11-11 | A flaw was found in Cockpit. A local authenticated user with control over a target account's home directory can exploit  |
| CVE-2026-100307 | 8.8 | 2026-11-11 | Missing authorization in the external management API in Amazon mcp-gateway-registry 1.0.9 through 1.24.7 might allow an  |
| CVE-2026-125926 | 8.5 | 2026-11-11 | Server-side request forgery (SSRF) in the server registration and update API in Amazon mcp-gateway-registry before 1.35. |
| CVE-2026-126797 | 9.8 | 2026-11-11 | NextScan 1.1.0 through 1.2.0 contains an authentication bypass vulnerability in ns-admin that allows unauthenticated att |
| CVE-2026-126799 | 7.5 | 2026-11-11 | Gotenberg 8.31.0 before 8.38.0 contains a server-side request forgery vulnerability in IsPublicIP() that allows unauthen |
| CVE-2026-126800 | 8.7 | 2026-11-11 | Hydro @hydrooj/ui-default before 4.59.1 contains a stored cross-site scripting vulnerability that allows registered user |
| CVE-2026-126801 | 8.8 | 2026-11-11 | Rote 1.2.0 through 2.6.0 contains an authorization bypass in the OAuth bind/merge endpoint that allows authenticated use |
| CVE-2026-126802 | 8.2 | 2026-11-11 | NextScan 1.1.0 through 1.2.0 contains hardcoded HTTP Basic Auth credentials in ns-admin's AuthAgent and AuthExternal rou |
| CVE-2026-126803 | 7.2 | 2026-11-11 | Rote through 2.6.0 contains a privilege escalation vulnerability that allows authenticated admins to obtain super_admin  |
| CVE-2026-126804 | 8.1 | 2026-11-11 | WWBN AVideo 12.4 through 29.7.1 contains a path traversal vulnerability in the ADs plugin deleteImage.json.php that allo |
| CVE-2026-126805 | 7.2 | 2026-11-11 | WWBN AVideo through 29.7.1 contains an incorrect authorization vulnerability that allows delegated Videos Admin users to |
| CVE-2026-126806 | 8.7 | 2026-11-11 | WWBN AVideo 14.3 through 29.7.1 contains a stored cross-site scripting vulnerability that allows uploaders to inject scr |
| CVE-2026-126809 | 7.1 | 2026-11-11 | WWBN AVideo through 29.7.1 contains a missing authorization vulnerability in objects/import.json.php that allows uploade |
| CVE-2026-126812 | 9.8 | 2026-11-11 | blueprintUE Self-Hosted Edition before 4.3.7 contains an insecure default configuration in its Docker Compose examples t |
| CVE-2026-111521 | 7.0 | 2026-11-11 | Dell Display and Peripheral Manager (DDPM Windows), versions prior to 2.4.0.17, contain a Time-of-check Time-of-use (TOC |
| CVE-2026-121528 | 8.1 | 2026-11-11 | A improper certificate validation vulnerability in Fortinet FortiOS 7.6.0 through 7.6.4, FortiOS 7.4.0 through 7.4.9, Fo |
| CVE-2026-126144 | 8.8 | 2026-11-11 | A improper neutralization of special elements used in an os command ('os command injection') vulnerability in Fortinet F |
| CVE-2026-126145 | 7.2 | 2026-11-11 | A improper neutralization of special elements used in an os command ('os command injection') vulnerability in Fortinet F |
| CVE-2026-126146 | 7.2 | 2026-11-11 | A improper neutralization of special elements used in an os command ('os command injection') vulnerability in Fortinet F |
| CVE-2026-126147 | 9.8 | 2026-11-11 | A improper limitation of a pathname to a restricted directory ('path traversal') vulnerability in Fortinet FortiMail 8.0 |
| CVE-2026-126148 | 9.8 | 2026-11-11 | A improper neutralization of special elements used in an os command ('os command injection') vulnerability in Fortinet F |
| CVE-2026-126149 | 7.5 | 2026-11-11 | A integer overflow or wraparound vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 through 7.6.6, |
| CVE-2026-126150 | 9.1 | 2026-11-11 | A weak password recovery mechanism for forgotten password vulnerability in Fortinet FortiMail 8.0.0, FortiMail 7.6.0 thr |
| CVE-2026-126151 | 7.5 | 2026-11-11 | A incorrect implementation of authentication algorithm vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMai |
| CVE-2026-126152 | 7.6 | 2026-11-11 | A authorization bypass through user-controlled key vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7. |
| CVE-2026-126153 | 7.5 | 2026-11-11 | A improper limitation of a pathname to a restricted directory ('path traversal') vulnerability in Fortinet FortiMail 8.0 |
| CVE-2026-126154 | 7.5 | 2026-11-11 | A out-of-bounds write vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 through 7.6.6, FortiMail  |
| CVE-2026-126155 | 9.1 | 2026-11-11 | A incorrect authorization vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 through 7.6.6, FortiM |
| CVE-2026-126156 | 9.1 | 2026-11-11 | A authorization bypass through user-controlled key vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7. |
| CVE-2026-126157 | 9.1 | 2026-11-11 | A improper authentication vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 through 7.6.6, FortiM |
| CVE-2026-126158 | 7.2 | 2026-11-11 | A improper neutralization of special elements used in an os command ('os command injection') vulnerability in Fortinet F |
| CVE-2026-126159 | 7.5 | 2026-11-11 | A authorization bypass through user-controlled key vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7. |
| CVE-2026-126160 | 8.2 | 2026-11-11 | A improper authentication vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 through 7.6.6, FortiM |
| CVE-2026-126161 | 7.5 | 2026-11-11 | A uncontrolled resource consumption vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 through 7.6 |
| CVE-2026-126162 | 8.7 | 2026-11-11 | A xml injection (aka blind xpath injection) vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 thr |
| CVE-2026-126163 | 8.1 | 2026-11-11 | A use of externally-controlled format string vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1 may allow a remote  |
| CVE-2026-126164 | 9.4 | 2026-11-11 | A improper neutralization of special elements used in an sql command ('sql injection') vulnerability in Fortinet FortiMa |
| CVE-2026-126165 | 7.5 | 2026-11-11 | A memory allocation with excessive size value vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 t |
| CVE-2026-126166 | 7.2 | 2026-11-11 | A improper neutralization of argument delimiters in a command ('argument injection') vulnerability in Fortinet FortiMail |
| CVE-2026-126167 | 7.2 | 2026-11-11 | A improper neutralization of special elements used in a command ('command injection') vulnerability in Fortinet FortiMai |
| CVE-2026-126168 | 7.2 | 2026-11-11 | A improper neutralization of argument delimiters in a command ('argument injection') vulnerability in Fortinet FortiMail |
| CVE-2026-126169 | 7.2 | 2026-11-11 | A improper neutralization of argument delimiters in a command ('argument injection') vulnerability in Fortinet FortiMail |
| CVE-2026-126170 | 9.8 | 2026-11-11 | A improper encoding or escaping of output vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.2, FortiAnalyzer 7.6 |
| CVE-2026-126171 | 7.2 | 2026-11-11 | A use of externally-controlled format string vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, FortiAnalyzer  |
| CVE-2026-126175 | 8.8 | 2026-11-11 | A improper neutralization of special elements used in an sql command ('sql injection') vulnerability in Fortinet FortiAn |
| CVE-2026-126176 | 8.1 | 2026-11-11 | A xml injection (aka blind xpath injection) vulnerability in Fortinet FortiAnalyzer 8.0.0, FortiAnalyzer 7.6.0 through 7 |
| CVE-2026-126177 | 8.1 | 2026-11-11 | A xml injection (aka blind xpath injection) vulnerability in Fortinet FortiAnalyzer 8.0.0, FortiAnalyzer 7.6.0 through 7 |
| CVE-2026-126178 | 7.2 | 2026-11-11 | A heap-based buffer overflow vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, FortiAnalyzer 7.6.0 through 7. |
| CVE-2026-126179 | 7.2 | 2026-11-11 | A improper neutralization of special elements used in an os command ('os command injection') vulnerability in Fortinet F |
| CVE-2026-126180 | 8.4 | 2026-11-11 | A improper neutralization of special elements used in a template engine vulnerability in Fortinet FortiManager 8.0.0 thr |
| CVE-2026-126181 | 8.0 | 2026-11-11 | A use of hard-coded credentials vulnerability in Fortinet FortiManager 8.0.0 through 8.0.1, FortiManager 7.6.0 through 7 |
| CVE-2026-126182 | 7.2 | 2026-11-11 | A improper control of generation of code ('code injection') vulnerability in Fortinet FortiManager 8.0.0 through 8.0.1,  |
| CVE-2026-126183 | 8.7 | 2026-11-11 | A authorization bypass through user-controlled key vulnerability in Fortinet FortiManager 8.0.0 through 8.0.1, FortiMana |
| CVE-2026-126184 | 8.2 | 2026-11-11 | A authentication bypass by spoofing vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, FortiAnalyzer 7.6.0 thr |
| CVE-2026-126185 | 7.2 | 2026-11-11 | A improper control of generation of code ('code injection') vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, |
| CVE-2026-126211 | 7.2 | 2026-11-11 | A improper privilege management vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, FortiAnalyzer 7.6.1 through |
| CVE-2026-126212 | 7.2 | 2026-11-11 | A heap-based buffer overflow vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, FortiAnalyzer 7.6.0 through 7. |
| CVE-2026-126213 | 7.1 | 2026-11-11 | A improper neutralization of special elements used in an sql command ('sql injection') vulnerability in Fortinet FortiAn |
| CVE-2026-126214 | 7.2 | 2026-11-11 | A authentication bypass by spoofing vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, FortiAnalyzer 7.6.0 thr |
| CVE-2026-126215 | 8.2 | 2026-11-11 | A incorrect authorization vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, FortiAnalyzer 7.6.0 through 7.6.7 |
| CVE-2026-126217 | 8.7 | 2026-11-11 | A incorrect authorization vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, FortiAnalyzer 7.6.0 through 7.6.7 |
| CVE-2026-126218 | 8.2 | 2026-11-11 | A authorization bypass through user-controlled key vulnerability in Fortinet FortiManager 8.0.0 through 8.0.1, FortiMana |
| CVE-2026-126219 | 7.2 | 2026-11-11 | A improper limitation of a pathname to a restricted directory ('path traversal') vulnerability in Fortinet FortiAnalyzer |
| CVE-2026-126220 | 7.2 | 2026-11-11 | A improper neutralization of special elements in output used by a downstream component ('injection') vulnerability in Fo |
| CVE-2026-126221 | 7.2 | 2026-11-11 | A improper neutralization of special elements in output used by a downstream component ('injection') vulnerability in Fo |
| CVE-2026-126222 | 7.2 | 2026-11-11 | A improper limitation of a pathname to a restricted directory ('path traversal') vulnerability in Fortinet FortiAnalyzer |
| CVE-2026-126223 | 7.2 | 2026-11-11 | A stack-based buffer overflow vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, FortiAnalyzer 7.6.0 through 7 |
| CVE-2026-126224 | 7.2 | 2026-11-11 | A improper neutralization of argument delimiters in a command ('argument injection') vulnerability in Fortinet FortiAnal |
| CVE-2026-126225 | 7.1 | 2026-11-11 | A missing authorization vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, FortiAnalyzer 7.6.7, FortiAnalyzer  |
| CVE-2026-126226 | 7.2 | 2026-11-11 | A improper neutralization of special elements used in an os command ('os command injection') vulnerability in Fortinet F |
| CVE-2026-126227 | 7.2 | 2026-11-11 | A unintended proxy or intermediary ('confused deputy') vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, Fort |
| CVE-2026-126228 | 7.2 | 2026-11-11 | A out-of-bounds write vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, FortiAnalyzer 7.6.0 through 7.6.7, Fo |
| CVE-2026-126229 | 9.1 | 2026-11-11 | A authorization bypass through user-controlled key vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, FortiAna |
| CVE-2026-126230 | 7.2 | 2026-11-11 | A use of externally-controlled format string vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, FortiAnalyzer  |
| CVE-2026-126231 | 7.2 | 2026-11-11 | A improper neutralization of special elements used in an os command ('os command injection') vulnerability in Fortinet F |
| CVE-2026-126232 | 7.5 | 2026-11-11 | A improper certificate validation vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, FortiAnalyzer 7.6.0 throu |
| CVE-2026-126233 | 7.2 | 2026-11-11 | A unrestricted upload of file with dangerous type vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, FortiAnal |
| CVE-2026-126234 | 7.2 | 2026-11-11 | A improper neutralization of special elements used in a template engine vulnerability in Fortinet FortiAnalyzer 8.0.0, F |
| CVE-2026-126235 | 7.2 | 2026-11-11 | A improper limitation of a pathname to a restricted directory ('path traversal') vulnerability in Fortinet FortiAnalyzer |
| CVE-2026-126236 | 7.2 | 2026-11-11 | A improper neutralization of special elements used in an os command ('os command injection') vulnerability in Fortinet F |
| CVE-2026-126237 | 7.5 | 2026-11-11 | A loop with unreachable exit condition ('infinite loop') vulnerability in Fortinet FortiAuthenticator 8.0.0 through 8.0. |
| CVE-2026-126238 | 8.6 | 2026-11-11 | A incorrect authorization vulnerability in Fortinet FortiAuthenticator 8.0.0 through 8.0.3, FortiAuthenticator 6.6.0 thr |
| CVE-2026-126239 | 7.5 | 2026-11-11 | A stack-based buffer overflow vulnerability in Fortinet FortiAuthenticator 8.0.0 through 8.0.3, FortiAuthenticator 6.6.0 |
| CVE-2026-126240 | 8.2 | 2026-11-11 | A improper neutralization of special elements used in an ldap query ('ldap injection') vulnerability in Fortinet FortiAu |
| CVE-2026-126241 | 8.8 | 2026-11-11 | A improper neutralization of special elements used in an sql command ('sql injection') vulnerability in Fortinet FortiAu |
| CVE-2026-126242 | 7.4 | 2026-11-11 | A incorrect authorization vulnerability in Fortinet FortiAuthenticator 8.0.0 through 8.0.3, FortiAuthenticator 6.6.0 thr |
| CVE-2026-126243 | 7.2 | 2026-11-11 | A incorrect authorization vulnerability in Fortinet FortiAuthenticator 8.0.0 through 8.0.3, FortiAuthenticator 6.6.0 thr |
| CVE-2026-126244 | 7.5 | 2026-11-11 | A allocation of resources without limits or throttling vulnerability in Fortinet FortiAuthenticator 8.0.0 through 8.0.3, |
| CVE-2026-126245 | 8.1 | 2026-11-11 | A out-of-bounds write vulnerability in Fortinet FortiAuthenticator 8.0.0 through 8.0.3, FortiAuthenticator 6.6.0 through |
| CVE-2026-126246 | 7.5 | 2026-11-11 | A null pointer dereference vulnerability in Fortinet FortiAuthenticator 8.0.0 through 8.0.3, FortiAuthenticator 6.6.0 th |
| CVE-2026-126247 | 7.2 | 2026-11-11 | A use of externally-controlled format string vulnerability in Fortinet FortiAuthenticator 8.0.0 through 8.0.3, FortiAuth |
| CVE-2026-126248 | 7.5 | 2026-11-11 | A insufficiently protected credentials vulnerability in Fortinet FortiAuthenticator 8.0.0 through 8.0.3, FortiAuthentica |
| CVE-2026-126249 | 7.2 | 2026-11-11 | A improper privilege management vulnerability in Fortinet FortiAuthenticator 8.0.0 through 8.0.3, FortiAuthenticator 6.6 |
| CVE-2026-126250 | 8.2 | 2026-11-11 | A incorrect authorization vulnerability in Fortinet FortiAuthenticator 8.0.0 through 8.0.3, FortiAuthenticator 6.6.0 thr |
| CVE-2026-126251 | 9.1 | 2026-11-11 | A incorrect authorization vulnerability in Fortinet FortiAuthenticator 8.0.0 through 8.0.3, FortiAuthenticator 6.6.0 thr |
| CVE-2026-126252 | 8.3 | 2026-11-11 | A improper neutralization of special elements used in an sql command ('sql injection') vulnerability in Fortinet FortiAu |
| CVE-2026-126253 | 9.3 | 2026-11-11 | A authentication bypass by primary weakness vulnerability in Fortinet FortiOS 8.0.0 through 8.0.1, FortiOS 7.6.0 through |
| CVE-2026-126254 | 9.6 | 2026-11-11 | A numeric truncation error vulnerability in Fortinet FortiOS 8.0.0 through 8.0.1, FortiOS 7.6.0 through 7.6.7, FortiOS 7 |
| CVE-2026-126255 | 7.4 | 2026-11-11 | A path traversal: '../filedir' vulnerability in Fortinet FortiOS 8.0.0 through 8.0.1, FortiOS 7.6.0 through 7.6.7, Forti |
| CVE-2026-126256 | 7.4 | 2026-11-11 | A out-of-bounds read vulnerability in Fortinet FortiOS 8.0.0 through 8.0.1, FortiOS 7.6.0 through 7.6.7, FortiOS 7.4.0 t |
| CVE-2026-126257 | 9.0 | 2026-11-11 | A use of hard-coded password vulnerability in Fortinet FortiAuthenticator 8.0.0 through 8.0.3, FortiAuthenticator 6.6.0  |
| CVE-2026-126258 | 7.5 | 2026-11-11 | A stack-based buffer overflow vulnerability in Fortinet FortiOS 8.0.0, FortiOS 7.6.7 may allow an unauthenticated attack |
| CVE-2026-126259 | 9.8 | 2026-11-11 | A missing authentication for critical function vulnerability in Fortinet FortiOS 8.0.0, FortiOS 7.6.0 through 7.6.7, For |
| CVE-2026-126262 | 9.8 | 2026-11-11 | A improper neutralization of special elements used in an sql command ('sql injection') vulnerability in Fortinet FortiAn |
| CVE-2026-126263 | 9.8 | 2026-11-11 | A improper neutralization of special elements used in an sql command ('sql injection') vulnerability in Fortinet FortiMa |
| CVE-2026-65949 | 7.2 | 2026-11-11 | Improper neutralization of special elements used in an OS command in Lenovo XClarity Integrator for Microsoft Windows Ad |
| CVE-2026-65952 | 8.5 | 2026-11-11 | Improper neutralization of special elements used in an OS command in the remote SSH operation functionality of Lenovo XC |
| CVE-2026-65971 | 7.6 | 2026-11-11 | Livewire PowerGrid creates data tables based on Laravel Livewire library. From version 6.0.0 to before version 6.10.4, t |
| CVE-2026-67449 | 9.8 | 2026-11-11 | Portabase is a database backup and restore tool for PostgreSQL, MySQL, MsSQL, MariaDB, Firebird SQL, SQLite, MongoDB, Re |
| CVE-2026-67541 | 8.1 | 2026-11-11 | Heym builds and runs agentic systems and business-process automations on self-hosted infrastructure. Prior to version 0. |
| CVE-2026-67542 | 7.1 | 2026-11-11 | Heym builds and runs agentic systems and business-process automations on self-hosted infrastructure. Prior to version 0. |
| CVE-2026-67543 | 8.8 | 2026-11-11 | Heym builds and runs agentic systems and business-process automations on self-hosted infrastructure. Prior to version 0. |
| CVE-2026-67544 | 8.8 | 2026-11-11 | Heym builds and runs agentic systems and business-process automations on self-hosted infrastructure. Prior to version 0. |
| CVE-2026-67545 | 7.4 | 2026-11-11 | Heym builds and runs agentic systems and business-process automations on self-hosted infrastructure. Prior to version 0. |
| CVE-2026-67546 | 8.8 | 2026-11-11 | Heym builds and runs agentic systems and business-process automations on self-hosted infrastructure. Prior to version 0. |
| CVE-2026-67547 | 8.8 | 2026-11-11 | taOS is a self-hosted AI agent OS. Prior to version 1.0.0-beta.23, the POST /api/skill-exec/{skill_id}/call endpoint in  |
| CVE-2026-67548 | 8.3 | 2026-11-11 | taOS is a self-hosted AI agent OS. Prior to version 1.0.0-beta.25, tinyagentos (taOS) registers all system settings rout |
| CVE-2026-68538 | 7.5 | 2026-11-11 | fulgur converts untrusted HTML/CSS into PDF, commonly on a server that processes input supplied by many tenants. From ve |
| CVE-2026-68539 | 7.5 | 2026-11-11 | fulgur converts untrusted HTML/CSS into PDF, commonly on a server that processes input supplied by many tenants. From ve |
| CVE-2026-68540 | 7.5 | 2026-11-11 | fulgur converts untrusted HTML/CSS into PDF, commonly on a server that processes input supplied by many tenants. From ve |
| CVE-2026-125637 | 7.2 | 2026-11-11 | A flaw was found in the Konflux UI proxy. Hostname values defined in the KonfluxUI custom resource are inserted directly |
| CVE-2026-126877 | 7.5 | 2026-11-11 | Use after free in Dawn in Google Chrome prior to 157.0.8103.78 allowed a remote attacker who had compromised the rendere |
| CVE-2026-126883 | 7.5 | 2026-11-11 | Use after free in Core in Google Chrome on on Windows prior to 157.0.8103.78 allowed a remote attacker who had compromis |
| CVE-2026-126902 | 7.5 | 2026-11-11 | Incorrect reference resolution in Browser in Google Chrome on on Mac prior to 157.0.8103.78 allowed a remote attacker wh |
| CVE-2026-126904 | 7.5 | 2026-11-11 | Use after free in Compositing in Google Chrome prior to 157.0.8103.78 allowed a remote attacker who had compromised the  |
| CVE-2026-126915 | 7.5 | 2026-11-11 | Use of uninitialized variable in Skia in Google Chrome on on Android prior to 157.0.8103.78 allowed a remote attacker wh |
| CVE-2026-126785 | 8.8 | 2026-11-12 | A vulnerability has been found in rmalright TR-VISION HOME 2.0.5. Impacted is the function sub_11504 in the library WFan |
| CVE-2025-10935 | 7.8 | 2026-11-12 | libilbm ILBM File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows remo |
| CVE-2026-114556 | 7.4 | 2026-11-12 | MailEnable Save Directory Traversal Arbitrary File Creation Vulnerability. This vulnerability allows remote attackers to |
| CVE-2026-114558 | 7.8 | 2026-11-12 | OriginLab Origin Viewer OPJU File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability. This vulnerability al |
| CVE-2026-114559 | 7.8 | 2026-11-12 | OriginLab Origin Viewer OGG File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability. This vulnerability all |
| CVE-2026-114560 | 7.8 | 2026-11-12 | OriginLab Origin Viewer OPJ File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability. This vulnerability all |
| CVE-2026-114561 | 7.8 | 2026-11-12 | OriginLab Origin Viewer OPJU File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability. This vulnerability al |
| CVE-2026-114562 | 7.8 | 2026-11-12 | OriginLab Origin Viewer OGWU File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability. This vulnerability al |
| CVE-2026-114563 | 7.8 | 2026-11-12 | OriginLab Origin Viewer OGWU File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerab |
| CVE-2026-114564 | 7.8 | 2026-11-12 | OriginLab Origin Viewer OGG File Parsing Out-Of-Bounds Write  Remote Code Execution Vulnerability. This vulnerability al |
| CVE-2026-114565 | 7.8 | 2026-11-12 | OriginLab Origin Viewer OGG File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability. This vulnerability all |
| CVE-2026-114566 | 7.8 | 2026-11-12 | OriginLab Origin Viewer OGM File Parsing Memory Corruption Remote Code Execution Vulnerability. This vulnerability allow |
| CVE-2026-114567 | 7.8 | 2026-11-12 | OriginLab Origin Viewer OGWU File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability. This vulnerability al |
| CVE-2026-114568 | 7.8 | 2026-11-12 | OriginLab Origin Viewer OPJ File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerabil |
| CVE-2026-114569 | 7.8 | 2026-11-12 | OriginLab Origin Viewer OGWU File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerabi |
| CVE-2026-118632 | 8.0 | 2026-11-12 | Philips Hue Bridge Pro SQL Injection Remote Code Execution Vulnerability. This vulnerability allows network-adjacent att |
| CVE-2026-121741 | 7.8 | 2026-11-12 | Trimble SketchUp SKP File Parsing Use-After-Free Remote Code Execution Vulnerability. This vulnerability allows remote a |
| CVE-2026-121742 | 7.8 | 2026-11-12 | Ashlar-Vellum Cobalt XE File Parsing Use-After-Free Remote Code Execution Vulnerability. This vulnerability allows remot |
| CVE-2026-121743 | 7.8 | 2026-11-12 | Ashlar-Vellum Cobalt AR File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability  |
| CVE-2026-121744 | 7.8 | 2026-11-12 | Ashlar-Vellum Cobalt XE File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability |
| CVE-2026-121752 | 7.8 | 2026-11-12 | Ashlar-Vellum Cobalt LI File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability  |
| CVE-2026-121753 | 7.8 | 2026-11-12 | Ashlar-Vellum Cobalt XE File Parsing Use-After-Free Remote Code Execution Vulnerability. This vulnerability allows remot |
| CVE-2026-122044 | 8.8 | 2026-11-12 | Philips Hue Bridge Pro Protection Mechanism Failure Authentication Bypass Vulnerability. This vulnerability allows netwo |
| CVE-2026-126795 | 7.3 | 2026-11-12 | A vulnerability was determined in ToolJet up to 3.20.256-lts/3.21.93-beta. The impacted element is the function activate |
| CVE-2026-13269 | 7.5 | 2026-11-12 | Quest NetVault Backup StnzCreateKey Numeric Truncation Error Denial-of-Service Vulnerability. This vulnerability allows  |
| CVE-2026-13270 | 7.5 | 2026-11-12 | Quest NetVault Backup nvpmgr Integer Underflow Denial-of-Service Vulnerability. This vulnerability allows remote attacke |
| CVE-2026-111433 | 8.6 | 2026-11-12 | UNIX symbolic link (symlink) following vulnerability in openEuler iSulad on Linux.

This vulnerability is associated wit |
| CVE-2026-111435 | 7.4 | 2026-11-12 | Relative path traversal vulnerability in openEuler iSulad on Linux.

This vulnerability is associated with program file  |
| CVE-2026-117687 | 7.3 | 2026-11-12 | Movable Type provided by Six Apart Ltd. contains a code injection vulnerability in its Dynamic Publishing functionality. |
| CVE-2026-13672 | 8.8 | 2026-11-12 | An authorization bypass through user-controlled key vulnerability in the SSOAuth in Synology DiskStation Manager (DSM) b |
| CVE-2026-18596 | 8.1 | 2026-11-12 | An authentication bypass using an alternate path or channel vulnerability in the OTP in Synology DiskStation Manager (DS |
| CVE-2026-18633 | 7.5 | 2026-11-12 | An access of uninitialized pointer vulnerability in the nfsd in Synology DiskStation Manager (DSM) before 7.3.2-86009-5  |
| CVE-2026-18792 | 8.8 | 2026-11-12 | An improper limitation of a pathname to a restricted directory vulnerability in the Sharing API in Synology DiskStation  |
| CVE-2026-19048 | 8.1 | 2026-11-12 | An improper link resolution before file access vulnerability in the thumb in Synology DiskStation Manager (DSM) before 7 |
| CVE-2026-74857 | 8.8 | 2026-11-12 | A missing critical step in authentication vulnerability in the Auth API in Synology DiskStation Manager (DSM) before 7.3 |
| CVE-2026-75785 | 7.2 | 2026-11-12 | An improper neutralization of special elements used in an OS command vulnerability in the VPN API in Synology DiskStatio |
| CVE-2026-76954 | 9.8 | 2026-11-12 | An improper neutralization of special elements used in an SQL command vulnerability in the Auth API in Synology DiskStat |
| CVE-2026-81584 | 8.1 | 2026-11-12 | An improper neutralization of special elements used in an SQL command vulnerability in the User API in Synology DiskStat |
| CVE-2026-85101 | 8.6 | 2026-11-12 | An authentication bypass using an alternate path or channel vulnerability in the rsync in Synology DiskStation Manager ( |
| CVE-2026-101107 | 8.0 | 2026-11-12 | An OS command Injection issue exists in Air Terminal 6 provided by SoftBank Corp. Arbitrary commands may be executed wit |
| CVE-2026-110959 | 9.8 | 2026-11-12 | The Descope WordPress plugin before 1.2.0 does not validate the authentication token it receives before creating a WordP |
| CVE-2026-119040 | 7.5 | 2026-11-12 | The Defender Security  WordPress plugin before 6.4.1 does not limit the number of failed two-factor authentication attem |
| CVE-2026-122003 | 8.8 | 2026-11-12 | The Abilities Bridge WordPress plugin before 1.4.2 does not require a valid nonce before re-authenticating a REST API re |
| CVE-2026-123044 | 7.5 | 2026-11-12 | The ContentPen WordPress plugin before 1.1.1 discloses its REST API key to unauthenticated users, who can then use it to |
| CVE-2026-123092 | 7.5 | 2026-11-12 | The WP Remote Users Sync WordPress plugin before 2.3.0 does not restrict which user metadata keys may be written through |
| CVE-2026-124647 | 8.6 | 2026-11-12 | The TI WooCommerce Wishlist WordPress plugin before 2.0.7 does not sanitise and escape user input before using it in a S |
| CVE-2026-124814 | 9.8 | 2026-11-12 | The Ultimate Addons for Elementor Forms WordPress plugin before 1.0.8 does not properly validate the extension of upload |
| CVE-2026-124815 | 10.0 | 2026-11-12 | The Clockinator Lite WordPress plugin before 1.1.0 does not restrict access to several of its record deletion actions, a |
| CVE-2026-76792 | 8.1 | 2026-11-12 | The User Verification by PickPlugins WordPress plugin before 2.0.49 does not rate limit the verification step of its one |
| CVE-2026-12507 | 9.1 | 2026-11-12 | Zohocorp ManageEngine AssetExplorer versions below 7860, ServiceDesk Plus versions below 15290, ServiceDesk Plus MSP ver |
| CVE-2026-12591 | 9.9 | 2026-11-12 | Zohocorp ManageEngine M365 Manager Plus versions below 4818 is affected by an authenticated technician may exploit insuf |
| CVE-2026-87772 | 7.8 | 2026-11-12 | Incorrect Authorization vulnerability in TÜBİTAK BİLGEM Software Technologies Research Institute Pardus About allows Pri |
| CVE-2026-125836 | 8.8 | 2026-11-12 | Cross-Site Request Forgery (CSRF) vulnerability in Nicu Micle Simple JWT Login simple-jwt-login allows Cross Site Reques |
| CVE-2026-106140 | 7.3 | 2026-11-12 | In Progress® Telerik® Reporting prior to version 20.3.26.1110, a deserialization of untrusted data vulnerability in the  |
| CVE-2026-124699 | 7.8 | 2026-11-12 | In Telerik UI for WinForms, versions prior to 2026.4.1111, an improper control of code generation vulnerability exists t |
| CVE-2026-124701 | 7.8 | 2026-11-12 | In Telerik UI for WinForms, versions prior to 2026.4.1111, a deserialization of untrusted data vulnerability exists that |
| CVE-2026-124703 | 7.8 | 2026-11-12 | In Telerik UI for WPF, versions prior to 2026.4.1110, an improper control of code generation vulnerability exists that a |
| CVE-2026-124704 | 7.8 | 2026-11-12 | In Telerik UI for WPF, versions prior to 2026.4.1110, a deserialization of untrusted data vulnerability exists that allo |
| CVE-2026-124705 | 7.8 | 2026-11-12 | In Progress® Telerik® UI for .NET MAUI prior to version 16.0.0, an untrusted URL redirection vulnerability in the RadRic |
| CVE-2026-13764 | 8.8 | 2026-11-12 | The Masterstudy - Education WordPress Theme theme for WordPress is vulnerable to Privilege Escalation in all versions up |
| CVE-2026-15309 | 8.8 | 2026-11-12 | The CourseCure Courses plugin for WordPress is vulnerable to Privilege Escalation in versions up to, and including, 1.5. |
| CVE-2026-16135 | 8.8 | 2026-11-12 | The VibeBP plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 1.9.9.8.1. T |
| CVE-2026-19421 | 8.8 | 2026-11-12 | Zohocorp ManageEngine DDI Central versions below 6301 is affected by a PowerShell injection vulnerability due to insuffi |
| CVE-2026-110951 | 7.5 | 2026-11-12 | Weak Password Recovery Mechanism for Forgotten Password vulnerability in Hyper Teknoloji Ltd. Şti. Hyper E-Commerce Infr |
| CVE-2026-111552 | 7.1 | 2026-11-12 | Use of single-factor authentication vulnerability in Hyper Teknoloji Ltd. Şti. Hyper E-Commerce Infrastructure, Hyper Te |
| CVE-2026-127056 | 7.5 | 2026-11-12 | PapaParse before 5.7.1 contains an inefficient algorithmic complexity vulnerability that allows remote unauthenticated a |
| CVE-2026-19422 | 9.1 | 2026-11-12 | Zohocorp ManageEngine DDI Central versions below 6301 is affected by an authentication bypass vulnerability in Windows D |
| CVE-2026-75864 | 8.1 | 2026-11-12 | Zohocorp ManageEngine DDI Central versions below 6301 is affected by an improper authorization vulnerability that allowe |
| CVE-2026-75867 | 8.1 | 2026-11-12 | Zohocorp ManageEngine DDI Central versions below 6301 is affected by an authorization bypass vulnerability that allowed  |
| CVE-2026-75868 | 8.1 | 2026-11-12 | Zohocorp ManageEngine DDI Central versions below 6301 is affected by an authorization bypass vulnerability that allowed  |
| CVE-2026-75869 | 8.8 | 2026-11-12 | Zohocorp ManageEngine DDI Central versions below 6301 is affected by an authorization bypass and PowerShell command inje |
| CVE-2026-107484 | 7.3 | 2026-11-12 | An input and authorization validation vulnerability in Gaia Portal backend handlers could allow an authenticated, non-ad |
| CVE-2026-123039 | 7.8 | 2026-11-12 | The Gaia OS DynamicCLI daemon runs as root and listens on a world-writable local socket (/tmp/dynamic_socket) without au |
| CVE-2026-124018 | 7.1 | 2026-11-12 | Gutenverse Form plugin for WordPress before 3.2.2 contains a CSV formula injection vulnerability that allows unauthentic |
| CVE-2026-92083 | 7.8 | 2026-11-12 | Missing Authorization vulnerability in TÜBİTAK BİLGEM Yazılım Teknolojileri Araştırma Enstitüsü pardus-image-writer allo |
| CVE-2026-116304 | 8.8 | 2026-11-12 | Use after free in PostgreSQL coordination of anonymous RECORD type identifiers among parallel workers allows a database  |
| CVE-2026-116306 | 8.8 | 2026-11-12 | Type confusion in PostgreSQL composite-value field assignment allows an object creator to execute arbitrary code as the  |
| CVE-2026-116307 | 8.8 | 2026-11-12 | Use after free in PostgreSQL plperl allows an object creator to execute arbitrary code as the operating system user runn |
| CVE-2026-116309 | 8.8 | 2026-11-12 | Type confusion in PostgreSQL plperl may allow an object creator to execute arbitrary code, via blessing a non-hash refer |
| CVE-2026-116313 | 7.2 | 2026-11-12 | Untrusted search path in PostgreSQL vacuumdb allows a database owner to execute arbitrary SQL as the database user runni |
| CVE-2026-116314 | 8.8 | 2026-11-12 | Improper input validation in PostgreSQL pg_restore allows a non-plain archive provider to execute arbitrary code as the  |
| CVE-2026-116315 | 8.8 | 2026-11-12 | Heap-based buffer overflow in PostgreSQL tsvector_delete() allows a database user to execute arbitrary code as the opera |
| CVE-2026-116316 | 8.8 | 2026-11-12 | Improper protection of alternate path in PostgreSQL security-restricted operations allows an object creator to execute a |
| CVE-2026-116317 | 8.8 | 2026-11-12 | Heap-based buffer overflow in PostgreSQL ts_rank_cd() may allow a database user to execute arbitrary code as the operati |
| CVE-2026-116318 | 8.8 | 2026-11-12 | SQL injection in PostgreSQL pg_dump allows an object creator to execute arbitrary SQL as the user restoring the dump, vi |
| CVE-2026-116319 | 8.8 | 2026-11-12 | Use after free in PostgreSQL plperl allows an object creator to execute arbitrary code as the operating system user runn |
| CVE-2026-116320 | 8.8 | 2026-11-12 | Use after free in PostgreSQL plperl allows an object creator to execute arbitrary code as the operating system user runn |
| CVE-2026-116323 | 8.8 | 2026-11-12 | Use after free in PostgreSQL pltcl allows an object creator to execute arbitrary code as the operating system user runni |
| CVE-2026-116325 | 8.0 | 2026-11-12 | SQL injection in PostgreSQL reindexdb allows an object creator to execute arbitrary SQL as the database user running rei |
| CVE-2026-116326 | 8.8 | 2026-11-12 | Uncaught exceptions in PostgreSQL plperl allow an object creator to cause use of a stale sigjmp_buf, via a tied Perl obj |
| CVE-2026-116328 | 8.8 | 2026-11-12 | Integer wraparound in PostgreSQL generation memory contexts allows a database user to execute arbitrary code as the oper |
| CVE-2026-116329 | 8.8 | 2026-11-12 | Type confusion in PostgreSQL statistics import allows a table maintainer to execute arbitrary code as the operating syst |
| CVE-2026-116330 | 8.8 | 2026-11-12 | Untrusted data inclusion in PostgreSQL pg_dump tar-format restore.sql allows a compromised origin server to execute arbi |
| CVE-2026-116331 | 8.8 | 2026-11-12 | Type confusion in PostgreSQL min/max aggregate optimization allows an object creator to execute arbitrary code as the op |
| CVE-2026-116332 | 8.8 | 2026-11-12 | Use after free in PostgreSQL portal setup allows an object creator to execute arbitrary code as the operating system use |
| CVE-2026-116335 | 8.8 | 2026-11-12 | Type confusion in PostgreSQL operator commutator and negator links allows an object creator to execute arbitrary code as |
| CVE-2026-116336 | 8.8 | 2026-11-12 | Operation on a dropped index in PostgreSQL REINDEX CONCURRENTLY allows an object creator to execute arbitrary code as th |
| CVE-2026-120139 | 8.8 | 2026-11-12 | Integer wraparound in PostgreSQL in-memory tuple-size calculations allows a database user to execute arbitrary code as t |
| CVE-2026-120141 | 8.8 | 2026-11-12 | Type confusion in PostgreSQL materialized set-returning functions allows a database user to execute arbitrary code as th |
| CVE-2026-120142 | 8.8 | 2026-11-12 | Type confusion in PostgreSQL anonymous RECORD types allows an object creator to execute arbitrary code as the operating  |
| CVE-2026-120143 | 8.8 | 2026-11-12 | Use after free in PostgreSQL trigger functions allows an object creator to execute arbitrary code as the operating syste |
| CVE-2026-120144 | 8.8 | 2026-11-12 | Type confusion from incomplete PostgreSQL type-cache invalidation allows an object creator to execute arbitrary code as  |
| CVE-2026-120145 | 8.8 | 2026-11-12 | Missing authorization in PostgreSQL logical replication allows a compromised publisher to execute arbitrary code as the  |
| CVE-2026-120147 | 8.8 | 2026-11-12 | Use after free in the PostgreSQL dblink extension allows an object creator to execute arbitrary code as the operating sy |
| CVE-2026-120148 | 8.1 | 2026-11-12 | Type confusion in PostgreSQL extended statistics allows an object creator to execute arbitrary code as the operating sys |
| CVE-2026-120149 | 8.8 | 2026-11-12 | Heap-based buffer overflow in PostgreSQL foreign batch inserts allows a foreign server to execute arbitrary code, via re |
| CVE-2026-120150 | 8.8 | 2026-11-12 | Use after free in PostgreSQL expanded-record domain checks allows an object creator to execute arbitrary code as the ope |
| CVE-2026-120151 | 8.8 | 2026-11-12 | Type confusion in PostgreSQL plpgsql record-field assignment allows an object creator to execute arbitrary code as the o |
| CVE-2026-120153 | 7.2 | 2026-11-12 | SQL injection in PostgreSQL extension-script substitutions allows an attacker with database-level CREATE privilege to ex |
| CVE-2026-126997 | 7.3 | 2026-11-12 | A vulnerability was identified in JeecgBoot up to 3.9.6. This affects the function RestTemplate.exchange of the file org |
| CVE-2026-126998 | 7.3 | 2026-11-12 | A security flaw has been discovered in JeecgBoot up to 3.9.5. This vulnerability affects the function OpenApiController. |
| CVE-2026-14661 | 8.1 | 2026-11-12 | External control of file name in PostgreSQL dblink and CREATE/ALTER SUBSCRIPTION allows a user to achieve persistent den |
| CVE-2026-18447 | 8.8 | 2026-11-12 | Type confusion in PostgreSQL SQL-language functions allows an object creator to execute arbitrary code as the operating  |
| CVE-2026-6460 | 8.8 | 2026-11-12 | Type confusion in PostgreSQL allows an object creator to execute arbitrary code as the operating system user running the |
| CVE-2026-6467 | 7.2 | 2026-11-12 | Uncontrolled search path element in PostgreSQL CREATE EXTENSION allows an attacker with database-level CREATE privilege  |
| CVE-2026-127111 | 7.4 | 2026-11-12 | SOGo before 5.12.13 contains an improper restriction of excessive authentication attempts vulnerability that allows unau |
| CVE-2026-127131 | 7.4 | 2026-11-12 | SOGo before 5.12.13 contains a missing rate limiting vulnerability in its web login TOTP verification that allows attack |
| CVE-2026-91007 | 7.8 | 2026-11-12 | The user-mode syscall verifiers for the charger driver API in drivers/charger/charger_handlers.c did not inspect the pro |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-124194 | Microsoft / Office | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-111793 | Openwave Messaging Limited / Webtop Media Transcoder | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-20320 | Cisco / BroadWorks | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-111560 | Barracuda Networks / Multiple Products | 2026-11-10 | 2026-11-13 | Unknown |
| CVE-2026-116606 | Barracuda Networks / Barracuda Email Security Gateway (ESG) | 2026-11-10 | 2026-11-13 | Unknown |
| CVE-2026-125350 | Google / Chromium | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-102895 | GPUStack / GPUStack | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-123158 | OpenBSD / OpenSSH | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-116779 | SignalWire / FreeSwitch | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-123218 | IBM / Aspera Faspex | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-19868 | SonicWall / SonicOS SSLVPN | 2026-11-06 | 2026-11-20 | Unknown |

---

*Total entries in CISA KEV catalog: 1779*