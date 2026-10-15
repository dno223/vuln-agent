# Vulnerability Intelligence Report

**Date:** 2026-10-15  
**Generated:** 2026-10-15T13:04:35Z  

---

## Executive Summary

Our environment faces critical exposure across multiple attack vectors. Ten high-severity CVEs have been identified, including two rated CVSS 9.8 affecting privilege escalation, deserialization, and missing authentication in production systems. One monitored vulnerability, CVE-2026-76519 in Cisco Secure Email Gateway, is confirmed actively exploited and listed in the CISA Known Exploited Vulnerabilities catalog with a federal remediation deadline of October 17, 2026. Additionally, 11 new KEV entries were added in the past seven days, signaling an elevated threat environment. Immediate action is required to prevent unauthorized access, data theft, and potential full system compromise.

---

## Risk Narrative

The current threat landscape reflects a surge in actively exploited vulnerabilities targeting enterprise infrastructure, web applications, and network appliances. The presence of a CISA KEV entry with an imminent deadline indicates nation-state or sophisticated criminal actors are leveraging known exploits in the wild. Critical flaws enabling privilege escalation, OS command injection, deserialization attacks, and authentication bypass create pathways to complete infrastructure compromise, data exfiltration, and ransomware deployment. The volume of 302 high-severity CVEs compounded by 11 newly cataloged exploited vulnerabilities significantly elevates organizational risk, threatening business continuity, regulatory compliance, and customer data integrity.

---

## Prioritized Action Items

1. Patch or mitigate CVE-2026-76519 (Cisco Secure Email Gateway) immediately, as it is actively exploited and has a CISA-mandated remediation deadline of October 17, 2026.
2. Remediate CVE-2026-107424 and CVE-2026-108291 (both CVSS 9.8) addressing privilege escalation and deserialization flaws that could allow full system takeover.
3. Address CVE-2026-16740 and CVE-2026-16741 in TR7 ASP appliances, which expose critical authentication bypass and OS command injection vulnerabilities rated CVSS 9.8.
4. Review and patch all 11 newly added CISA KEV entries, prioritizing Palo Alto Networks PAN-OS, Ivanti Connect Secure, and Ahsay AhsayCBS if present in your environment.
5. Conduct a full audit of the remaining 302 high-severity CVEs to identify additional exposures requiring prioritized remediation within the next 30 days.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-105874 | 7.1 | 2026-10-14 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Brainstorm Force S |
| CVE-2026-106599 | 8.8 | 2026-10-14 | Deserialization of Untrusted Data vulnerability in Brainstorm Force SureCart surecart allows Object Injection.This issue |
| CVE-2026-107421 | 7.3 | 2026-10-14 | Session Fixation vulnerability in VideoWhisper.com Broadcast Live Video videowhisper-live-streaming-integration allows S |
| CVE-2026-107424 | 9.8 | 2026-10-14 | Incorrect Privilege Assignment vulnerability in M A Vinoth Kumar Frontend Dashboard frontend-dashboard allows Privilege  |
| CVE-2026-107426 | 7.3 | 2026-10-14 | Missing Authorization vulnerability in VideoWhisper.com Paid Videochat Turnkey Site ppv-live-webcams allows Exploiting I |
| CVE-2026-107867 | 7.1 | 2026-10-14 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Crocoblock JetProd |
| CVE-2026-108291 | 9.8 | 2026-10-14 | Deserialization of Untrusted Data vulnerability in itthinx Affiliates affiliates allows Object Injection.This issue affe |
| CVE-2026-16740 | 9.8 | 2026-10-14 | Missing authentication for critical function vulnerability in TR7 Cyber ​​Defense Inc. TR7 ASP on virtual appliance and  |
| CVE-2026-16741 | 9.8 | 2026-10-14 | Improper neutralization of special elements used in an OS command ('OS command injection') vulnerability in TR7 Cyber ​​ |
| CVE-2026-82026 | 8.8 | 2026-10-14 | Radar before 1.12.2 contains a missing authorization vulnerability in the handleLocalTerminal WebSocket endpoint (/api/l |
| CVE-2026-97278 | 7.2 | 2026-10-14 | Deserialization of Untrusted Data vulnerability in WP SYNTEX Polylang polylang allows Object Injection.This issue affect |
| CVE-2026-107870 | 7.1 | 2026-10-14 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Crocoblock JetEngi |
| CVE-2026-108065 | 9.8 | 2026-10-14 | SQL Injection (CWE-89) in the SOAP GetUser method of the /preapproval.asmx endpoint in Channel Software WebAlliance eCom |
| CVE-2026-110690 | 7.5 | 2026-10-14 | Cloud Commander (cloudcmd) versions 19.20.2 through 19.21.1 contains a path traversal vulnerability in the GET /api/v1/p |
| CVE-2017-20286 | 7.8 | 2026-10-14 | DevIL through 1.8.0 contains a heap-based buffer overflow in iGetPalette() in il_gif.cpp that allows attackers to write  |
| CVE-2020-37281 | 8.1 | 2026-10-14 | Gravitee API Management through 4.12.22 contains an authentication bypass vulnerability that allows unauthenticated remo |
| CVE-2020-37282 | 9.8 | 2026-10-14 | office-converter through 1.0.2 contains an OS command injection vulnerability that allows attackers to execute commands  |
| CVE-2025-71433 | 7.5 | 2026-10-14 | Kaneo before 2.1.6 contains a missing authorization vulnerability that allows authenticated users to access other worksp |
| CVE-2026-104939 | 7.5 | 2026-10-14 | Description
NGINX Ingress Controller has a vulnerability when implementing an externalAuth policy for ingress. NGINX Ing |
| CVE-2026-110599 | 7.1 | 2026-10-14 | L-SMASH through 2.14.5 contains a double free vulnerability in hevc_setup_first_summary() and h264_setup_first_summary() |
| CVE-2026-110612 | 9.8 | 2026-10-14 | vlife through 2.0.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to forge JWTs  |
| CVE-2026-110615 | 7.1 | 2026-10-14 | jshERP through 3.6 contains a missing authorization vulnerability in the POST /user/batchSetStatus endpoint that allows  |
| CVE-2026-110616 | 8.1 | 2026-10-14 | NullHub through 2026.5.29 contains a missing authentication vulnerability that allows unauthenticated attackers to acces |
| CVE-2026-110618 | 8.1 | 2026-10-14 | SmsForwarder through 3.5.0 contains a missing authentication vulnerability in its AndServer HTTP server that allows unau |
| CVE-2026-110621 | 8.8 | 2026-10-14 | Swetrix Cloud before 5.1.0 contains a missing authorization vulnerability in ProjectController.addProject that allows au |
| CVE-2026-110622 | 7.5 | 2026-10-14 | Papermerge Core through 3.5.3 contains a missing authorization vulnerability that allows authenticated users to manipula |
| CVE-2026-110623 | 7.5 | 2026-10-14 | Papermerge Core through 3.5.3 contains a missing authorization vulnerability in the shared nodes API that allows authent |
| CVE-2026-110628 | 8.6 | 2026-10-14 | Kan 0.5.5 through 0.6.0 contains an unauthenticated server-side request forgery vulnerability in the /api/download/attat |
| CVE-2026-110631 | 9.8 | 2026-10-14 | Komodo through 2.3.3 contains an authentication bypass vulnerability in the Periphery agent that allows unauthenticated  |
| CVE-2026-110632 | 8.1 | 2026-10-14 | Report One MyReport Updater through 2.1.1 exposes an unauthenticated gRPC service on TCP port 9095 that allows remote at |
| CVE-2026-110633 | 7.8 | 2026-10-14 | MyReport Updater through 2.1.1 contains a local privilege escalation vulnerability that allows low-privileged users to m |
| CVE-2026-110634 | 9.8 | 2026-10-14 | git-diff before 2.0.7 contains an OS command injection vulnerability that allows attackers to execute shell commands by  |
| CVE-2026-110635 | 9.8 | 2026-10-14 | webp-converter before 3.0.0 contains an OS command injection vulnerability in src/webpconverter.js helpers that run libw |
| CVE-2026-110636 | 9.8 | 2026-10-14 | pypdftk through 0.5 contains an OS command injection vulnerability in fill_form(), dump_data_fields(), and pdftk_cmd_uti |
| CVE-2026-110637 | 7.8 | 2026-10-14 | buildebooks before 0.2.2 contains an OS command injection vulnerability in lib/kindle.js that allows attackers to execut |
| CVE-2026-110638 | 9.8 | 2026-10-14 | doc-recog through 1.1.6 contains an OS command injection vulnerability that allows attackers to execute commands by supp |
| CVE-2026-110639 | 9.8 | 2026-10-14 | @mborne/extract before 0.2.1 contains an OS command injection vulnerability that allows attackers to execute commands by |
| CVE-2026-110640 | 9.8 | 2026-10-14 | Whisper-node through 1.1.1 contains an OS command injection vulnerability that allows attackers to execute commands by s |
| CVE-2026-110641 | 8.8 | 2026-10-14 | @runnerty/executor-decompress through 3.1.1 contains an OS command injection vulnerability that allows attackers to exec |
| CVE-2026-110642 | 7.8 | 2026-10-14 | xhtml2pdf before 0.2.19 contains an OS command injection vulnerability in pisa.startViewer() that allows attackers to ex |
| CVE-2026-110643 | 9.8 | 2026-10-14 | transcribe2texts through 1.0.6 contains an OS command injection vulnerability that allows attackers to execute commands  |
| CVE-2026-110644 | 9.8 | 2026-10-14 | nodejs-whisper through 0.3.1 contains an OS command injection vulnerability in convertToWavType() that allows attackers  |
| CVE-2026-110645 | 9.8 | 2026-10-14 | Video-stitch before 2.0.0-beta.1 contains an OS command injection vulnerability that allows attackers to execute command |
| CVE-2026-110646 | 8.1 | 2026-10-14 | Beganovich snappdf from 1.1.0 before 6.1.0 contains an OS command injection vulnerability on Windows that allows attacke |
| CVE-2026-110647 | 7.8 | 2026-10-14 | Turnpress through 0.4.2 contains an OS command injection vulnerability that allows attackers to execute shell commands b |
| CVE-2026-110648 | 7.8 | 2026-10-14 | @offactory/compress-fonts before 1.1.1 contains an OS command injection vulnerability that allows attackers to execute s |
| CVE-2026-110649 | 9.8 | 2026-10-14 | Stills before 25.24.2 contains an OS command injection vulnerability that allows attackers to execute shell commands by  |
| CVE-2026-110650 | 9.8 | 2026-10-14 | The thumbnail Python package through 1.5 contains an OS command injection vulnerability in generate_thumbnail() that all |
| CVE-2026-15176 | 8.1 | 2026-10-14 | A vulnerability exists in NGINX Plus and NGINX Open Source when a location is configured that uses the alias directive t |
| CVE-2026-53612 | 7.0 | 2026-10-14 | util-linux is a random collection of Linux utilities. In util-linux 2.39 through 2.41.4 and 2.42 through 2.42.1, the SUI |
| CVE-2026-53613 | 7.0 | 2026-10-14 | util-linux is a random collection of Linux utilities. In util-linux 2.17 through 2.41.6 and 2.42 through 2.42.3, and in  |
| CVE-2026-59774 | 9.8 | 2026-10-14 | Gitea's Org-mode markup renderer processes INCLUDE directives supplied to the repository markup endpoint without prevent |
| CVE-2026-66877 | 8.1 | 2026-10-14 | Gitea enforces first-time fork contributor approval by blocking jobs, but some job transition and dispatch paths do not  |
| CVE-2026-71184 | 8.8 | 2026-10-14 | Gitea's pull request review notifier does not attach the pull request to the Actions notification, so the fork workflow  |
| CVE-2026-91184 | 8.8 | 2026-10-14 | Description

NGINX Gateway Fabric has a vulnerability when it renders the spec.basic.realm (and spec.jwt.realm) field of |
| CVE-2026-93479 | 8.1 | 2026-10-14 | A vulnerability exists in NGINX Plus and NGINX Open Source when a map directive uses regex matching and the root directi |
| CVE-2026-94197 | 7.5 | 2026-10-14 | An authentication and authorization bypass vulnerability exists in F5 NGINX Kubernetes Ingress Controller (NIC) when con |
| CVE-2026-97205 | 8.1 | 2026-10-14 | NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_core_module module. When asynchronous file I/O (AI |
| CVE-2026-102695 | 8.2 | 2026-10-14 | OmniFaces is a utility library for Faces. In OmniFaces versions before 1.14.3, 2.7.33, 3.14.23, 4.7.12, and 5.4.2, Combi |
| CVE-2026-103929 | 7.8 | 2026-10-14 | mise manages dev tools like node, python, cmake, and terraform. Prior to 2026.7.14, in the default non-safe mode, mise l |
| CVE-2026-110719 | 7.2 | 2026-10-14 | Portkey AI Gateway 1.14.0 through 1.15.2 contains a server-side request forgery vulnerability that allows unauthenticate |
| CVE-2026-53614 | 7.0 | 2026-10-14 | util-linux is a random collection of Linux utilities. In util-linux 2.39.1 through 2.41.4 and 2.42 through 2.42.1, the S |
| CVE-2026-53615 | 8.0 | 2026-10-14 | util-linux is a random collection of Linux utilities. Before util-linux 2.41.4, `parse_dos_extended()` in `libblkid/src/ |
| CVE-2026-86002 | 9.0 | 2026-10-14 | Dokku is a docker-powered platform as a service. In Dokku versions before 0.38.25, a user with app-level Dokku access an |
| CVE-2026-87093 | 8.8 | 2026-10-14 | Incorrect Permission Assignment for Critical Resource vulnerability in Progress MOVEit Transfer.

This issue affects MOV |
| CVE-2026-89067 | 8.8 | 2026-10-14 | Authentication bypass using an alternate path or channel vulnerability in Progress MOVEit Transfer.

This issue affects  |
| CVE-2026-89068 | 8.1 | 2026-10-14 | Missing critical step in authentication vulnerability in Progress MOVEit Transfer (LDAP module).

This issue affects MOV |
| CVE-2026-89069 | 8.0 | 2026-10-14 | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in Progress MOVEit Tr |
| CVE-2026-89070 | 7.5 | 2026-10-14 | Authentication bypass by capture-replay vulnerability in Progress MOVEit Transfer (OIDC module).

This issue affects MOV |
| CVE-2026-89071 | 7.5 | 2026-10-14 | Improper neutralization of special elements used in an LDAP query ('LDAP injection') vulnerability in Progress MOVEit Tr |
| CVE-2026-89072 | 7.5 | 2026-10-14 | Incorrect Authorization vulnerability in Progress MOVEit Transfer (Client Certificates module).

This issue affects MOVE |
| CVE-2026-89073 | 7.5 | 2026-10-14 | Insufficient Session Expiration vulnerability in Progress MOVEit Transfer.

This issue affects MOVEit Transfer: before 2 |
| CVE-2026-89074 | 7.5 | 2026-10-14 | Improper handling of unicode encoding vulnerability in Progress MOVEit Transfer.

This issue affects MOVEit Transfer: be |
| CVE-2026-89075 | 7.3 | 2026-10-14 | Insecure Storage of Sensitive Information vulnerability in Progress MOVEit Transfer.

This issue affects MOVEit Transfer |
| CVE-2026-89076 | 7.2 | 2026-10-14 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Progress MOVEit Tr |
| CVE-2026-89077 | 7.5 | 2026-10-14 | Incorrect implementation of authentication algorithm vulnerability in Progress MOVEit Transfer (SFTP module).

This issu |
| CVE-2026-91156 | 7.5 | 2026-10-14 | Discourse is an open-source discussion platform. Prior to 2026.9.0, 2026.8.1, 2026.7.3, and 2026.1.9, MessageBus audienc |
| CVE-2026-91157 | 7.5 | 2026-10-14 | Discourse is an open-source discussion platform. Prior to 2026.9.0, 2026.8.1, 2026.7.3, and 2026.1.9, sites with secure  |
| CVE-2026-91159 | 7.7 | 2026-10-14 | Discourse is an open-source discussion platform. Prior to 2026.9.0, 2026.8.1, 2026.7.3, and 2026.1.9, oEmbed processing  |
| CVE-2026-91881 | 9.0 | 2026-10-14 | Dell Terraform Provider for Redfish, versions prior to 1.6.2, contains an Improper Certificate Validation vulnerability  |
| CVE-2026-91882 | 8.6 | 2026-10-14 | Dell Terraform Provider for OME, versions 1.0.0 through 1.2.3, contains an Insertion of Sensitive Information into Exter |
| CVE-2016-15060 | 8.3 | 2026-10-14 | A vulnerability was found in PCMan FTP Server up to 2.0.7. This affects an unknown function of the component PORT Comman |
| CVE-2026-100236 | 8.6 | 2026-10-14 | A flaw was found in the DPDK GSO library. When software GSO copies packet headers into a new mbuf, it does not check tha |
| CVE-2026-101927 | 7.8 | 2026-10-14 | A Heap-based Buffer Overflow vulnerability in eventd of Juniper Networks Junos OS and Junos OS Evolved on all platforms  |
| CVE-2026-101939 | 7.5 | 2026-10-14 | A NULL Pointer Dereference vulnerability in the routing protocol daemon (RPD) of Juniper Networks Junos OS and Junos OS  |
| CVE-2026-101940 | 7.5 | 2026-10-14 | A NULL Pointer Dereference vulnerability in the rpd routing daemon of Juniper Networks Junos OS and Junos OS Evolved all |
| CVE-2026-101941 | 7.5 | 2026-10-14 | A NULL Pointer Dereference vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS  |
| CVE-2026-101942 | 7.5 | 2026-10-14 | An Improper Handling of Length Parameter Inconsistency vulnerability in the routing protocol daemon (rpd) process of Jun |
| CVE-2026-101943 | 7.5 | 2026-10-14 | An Improper Input Validation vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos O |
| CVE-2026-101944 | 7.5 | 2026-10-14 | An Integer Overflow or Wraparound vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Ju |
| CVE-2026-101945 | 7.5 | 2026-10-14 | An Integer Overflow or Wraparound vulnerability in the rpd process of Juniper Networks Junos OS and Junos OS Evolved all |
| CVE-2026-101948 | 7.5 | 2026-10-14 | A NULL Pointer Dereference vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS  |
| CVE-2026-101950 | 9.8 | 2026-10-14 | A Heap-based Buffer Overflow vulnerability in the SVR component of Juniper Networks Junos OS on SRX Series allows an una |
| CVE-2026-101951 | 7.5 | 2026-10-14 | An Improper Validation of Consistency within Input vulnerability in the routing protocol daemon (rpd) of Juniper Network |
| CVE-2026-101955 | 8.1 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the UTM Anti-Spam SBL of Juniper Networks Junos OS on SRX series allows a |
| CVE-2026-101956 | 9.8 | 2026-10-14 | An Improper Authentication vulnerability in the J-Web web management component of Juniper Networks Junos OS allows an un |
| CVE-2026-101957 | 7.5 | 2026-10-14 | An Improper Initialization vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS  |
| CVE-2026-101965 | 8.8 | 2026-10-14 | An Use of Externally-Controlled Format String vulnerability in the gRPC daemon of Juniper Networks Junos OS Evolved allo |
| CVE-2026-101966 | 8.2 | 2026-10-14 | A Use of Externally-Controlled Format String vulnerability in the jti-dialoutd of Juniper Networks Junos OS Evolved allo |
| CVE-2026-101967 | 8.8 | 2026-10-14 | An OS Command Injection vulnerability in the bootzd zero-touch provisioning daemon of Juniper Networks Junos OS Evolved  |
| CVE-2026-101973 | 7.5 | 2026-10-14 | A NULL Pointer Dereference vulnerability in the pkid component of Juniper Networks Junos OS allows an unauthenticated re |
| CVE-2026-101977 | 7.5 | 2026-10-14 | A NULL Pointer Dereference vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS  |
| CVE-2026-101978 | 8.8 | 2026-10-14 | An OS Command Injection vulnerability in the bootzd zero-touch provisioning daemon of Juniper Networks Junos OS Evolved  |
| CVE-2026-101980 | 9.8 | 2026-10-14 | An Integer Underflow vulnerability in the kernel of Juniper Networks Junos OS with Extended Echo configured allows an un |
| CVE-2026-101986 | 9.8 | 2026-10-14 | An  Improper Authentication vulnerability in J-Web of Juniper Networks Junos OS and Junos OS Evolved allows an unauthent |
| CVE-2026-101990 | 9.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos  |
| CVE-2026-101994 | 7.1 | 2026-10-14 | An Improper Handling of Length Parameter Inconsistency vulnerability in the 

l2ald 

daemon of Juniper Networks Junos O |
| CVE-2026-101997 | 8.1 | 2026-10-14 | An Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in ipfd of Juniper |
| CVE-2026-102012 | 7.5 | 2026-10-14 | A Reachable Assertion vulnerability in the na-grpcd process of Juniper Networks Junos OS Evolved allows a remote unauthe |
| CVE-2026-102014 | 8.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the authd process of Juniper Networks Junos OS allows an attacker able to |
| CVE-2026-102015 | 8.8 | 2026-10-14 | A Heap-based Buffer Overflow vulnerability in the secure-dot1xd process of Juniper Networks on Junos OS and Junos OS Evo |
| CVE-2026-102016 | 7.5 | 2026-10-14 | An Improper Validation of Specified Quantity in Input vulnerability in the rpd process of Juniper Networks Junos OS and  |
| CVE-2026-102020 | 7.5 | 2026-10-14 | A Reachable Assertion vulnerability in the rpd process of Juniper Networks Junos OS and Junos OS Evolved allows an authe |
| CVE-2026-102022 | 7.5 | 2026-10-14 | A Reachable Assertion vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS Evolv |
| CVE-2026-102023 | 7.5 | 2026-10-14 | A Reachable Assertion vulnerability in fwstatsd of Juniper Networks Junos OS Evolved allows an authenticated network att |
| CVE-2026-102024 | 7.5 | 2026-10-14 | An Integer Overflow or Wraparound vulnerability in the routing daemon (rpd) of Juniper Networks Junos OS and Junos OS Ev |
| CVE-2026-102025 | 7.5 | 2026-10-14 | A Mismatched Memory Management Routines vulnerability in the routing protocol daemon (rpd) process of Juniper Networks J |
| CVE-2026-102026 | 7.5 | 2026-10-14 | An Improper Control of a Resource Through its Lifetime vulnerability in the routing protocol daemon (rpd) of Juniper Net |
| CVE-2026-102027 | 7.5 | 2026-10-14 | An Incorrect Calculation of Buffer Size vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS  |
| CVE-2026-102028 | 7.5 | 2026-10-14 | A NULL Pointer Dereference vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS  |
| CVE-2026-102029 | 7.5 | 2026-10-14 | A NULL Pointer Dereference vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS  |
| CVE-2026-102030 | 7.5 | 2026-10-14 | An Incomplete Cleanup vulnerability in the rpd process of Juniper Networks Junos OS and Junos OS Evolved allows a config |
| CVE-2026-102031 | 9.8 | 2026-10-14 | An OS Command Injection vulnerability in TACACS of Juniper Networks Junos OS Evolved allows a low-privileged TACACS+-aut |
| CVE-2026-102036 | 7.5 | 2026-10-14 | An Integer Overflow or Wraparound vulnerability in the l2ald process of Juniper Networks Junos OS and Junos OS Evolved a |
| CVE-2026-102037 | 8.1 | 2026-10-14 | An XML Injection vulnerability in the Unified Threat Management daemon (utmd) of Juniper Networks Junos OS on SRX Series |
| CVE-2026-102044 | 7.5 | 2026-10-14 | A Reachable Assertion vulnerability in the rpd process of Juniper Networks Junos OS and Junos OS Evolved allows a config |
| CVE-2026-102046 | 7.5 | 2026-10-14 | A Loop with Unreachable Exit Condition ('Infinite Loop') vulnerability in netsctp.ko of Juniper Networks Junos OS on MX  |
| CVE-2026-102049 | 8.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the l2cpd process of Juniper Networks Junos OS and Junos OS Evolved allow |
| CVE-2026-102050 | 8.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the l2cpd daemon of Juniper Networks Junos OS and Junos OS Evolved allows |
| CVE-2026-102052 | 8.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the jdhcpd process of Juniper Networks Junos OS and Junos OS Evolved plat |
| CVE-2026-102055 | 8.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the cfmd process of Juniper Networks Junos OS on MX Series and Junos OS E |
| CVE-2026-102056 | 7.1 | 2026-10-14 | An Out-of-bounds Read vulnerability in the cfmd process of Juniper Networks Junos OS and Junos OS Evolved allows an unau |
| CVE-2026-102057 | 7.5 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the jdhcpd process of Juniper Networks Junos OS allows an unauthenticated |
| CVE-2026-102059 | 8.8 | 2026-10-14 | An Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in the phone |
| CVE-2026-102061 | 8.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the phone-home daemon (phcd) of Juniper Networks Junos OS and Junos OS Ev |
| CVE-2026-102062 | 8.1 | 2026-10-14 | An Use of Externally-Controlled Format String vulnerability in the ipfd daemon of Juniper Networks Junos OS on SRX Serie |
| CVE-2026-102064 | 7.5 | 2026-10-14 | A Reachable Assertion vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS Evolv |
| CVE-2026-102065 | 7.5 | 2026-10-14 | An Improper Validation of Specified Quantity in Input vulnerability in the routing protocol daemon (rpd) of Juniper Netw |
| CVE-2026-102068 | 7.5 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the kernel of Juniper Networks Junos OS Evolved allows an unauthenticated |
| CVE-2026-102069 | 8.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the dot1x daemon of Juniper Networks Junos OS devices operating as Junos  |
| CVE-2026-102070 | 7.5 | 2026-10-14 | A Reachable Assertion vulnerability in the Two-Way Active Measurement Protocol (TWAMP) client of Juniper Networks Junos  |
| CVE-2026-102079 | 7.8 | 2026-10-14 | An OS command injection vulnerability in the CLI of Juniper Networks Junos OS allows a local, low privileged attacker to |
| CVE-2026-102081 | 7.5 | 2026-10-14 | A Missing Release of Memory after Effective Lifetime vulnerability in the packet forwarding engine (PFE) of Juniper Netw |
| CVE-2026-102084 | 8.1 | 2026-10-14 | An Improper Validation of Syntactic Correctness of Input vulnerability in the VPN daemon of Juniper Networks Junos OS on |
| CVE-2026-102174 | 8.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the iked IKE key-management daemon of Juniper Networks Junos OS on the SR |
| CVE-2026-102175 | 9.8 | 2026-10-14 | A Heap-based Buffer Overflow vulnerability in the sdxd service-deployment daemon of Juniper Networks Junos OS and Junos  |
| CVE-2026-102176 | 8.8 | 2026-10-14 | A Buffer Copy without Checking Size of Input ('Classic Buffer Overflow') vulnerability in the SDK service process of Jun |
| CVE-2026-102177 | 7.6 | 2026-10-14 | An Out-of-bounds Write vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS Evol |
| CVE-2026-102178 | 9.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the BGP routing daemon of Juniper Networks Junos OS and Junos OS Evolved  |
| CVE-2026-102179 | 7.5 | 2026-10-14 | An Out-of-bounds Write vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS Evol |
| CVE-2026-102180 | 7.5 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos  |
| CVE-2026-102182 | 9.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the kmd component of Juniper Networks Junos OS on MX Series allows an una |
| CVE-2026-102183 | 7.5 | 2026-10-14 | An Improper Validation of Specified Quantity in Input vulnerability in the routing protocol daemon (rpd) of Juniper Netw |
| CVE-2026-102184 | 7.5 | 2026-10-14 | An Improper Validation of Specified Quantity in Input vulnerability in the routing protocol daemon (rpd) of Juniper Netw |
| CVE-2026-102185 | 7.5 | 2026-10-14 | A Loop with Unreachable Exit Condition ('Infinite Loop') vulnerability in the routing protocol daemon (rpd) of Juniper N |
| CVE-2026-103946 | 8.3 | 2026-10-14 | An SQL injection vulnerability could allow an authenticated user to read or modify data stored by Nessus. |
| CVE-2026-103994 | 8.8 | 2026-10-14 | A Heap-based Buffer Overflow vulnerability in the VXLAN Gateway Daemon (vgd) of Juniper Networks Junos OS allows a malic |
| CVE-2026-109439 | 9.8 | 2026-10-14 | Lantronix XPress-DR and XPress-DR-I (CoBos-family) firmware through 8.1.0.0 contains a missing authentication vulnerabil |
| CVE-2026-15102 | 7.5 | 2026-10-14 | ADP Desktop SDK contains a vulnerability where sensitive information is transmitted in clear text. Exploitation of this  |
| CVE-2026-19673 | 7.1 | 2026-10-14 | ethernet_recv() in subsys/net/l2/ethernet/ethernet.c validates only that the first net_buf of a received frame holds a p |
| CVE-2026-33789 | 9.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos  |
| CVE-2026-33792 | 9.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the srxpfe process of Juniper Networks Junos OS on SRX Series allows an u |
| CVE-2026-33795 | 7.5 | 2026-10-14 | A Numeric Truncation Error vulnerability in the rpd process of Juniper Networks Junos OS and Junos OS Evolved allows an  |
| CVE-2026-33796 | 9.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos  |
| CVE-2026-33798 | 8.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the srxpfe of Juniper Networks Junos OS and Junos OS Evolved on the SRX S |
| CVE-2026-76519 | 9.8 | 2026-10-14 | A vulnerability in the Advanced Malware Protection (AMP) feature of Cisco Secure Email Gateway could allow an unauthenti |
| CVE-2026-77524 | 9.9 | 2026-10-14 | KEDA is a Kubernetes-based Event Driven Autoscaling component. In version 2.20.2 and earlier, a namespace administrator  |
| CVE-2026-86562 | 7.8 | 2026-10-14 | A flaw was found in DPDK lib/vhost. A TOCTOU double-fetch of control-queue descriptors allows a heap buffer overflow wit |
| CVE-2026-86563 | 7.8 | 2026-10-14 | A flaw was found in DPDK lib/vhost. A double-offset bug in vhost log mapping calculation can lead to incorrect memory ac |
| CVE-2026-86565 | 8.2 | 2026-10-14 | A flaw was found in DPDK lib/vhost. A guest can desynchronize virtqueue size from inflight descriptor table size, causin |
| CVE-2026-92151 | 7.5 | 2026-10-14 | F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applicati |
| CVE-2026-92153 | 7.1 | 2026-10-14 | F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applicati |
| CVE-2026-101949 | 7.5 | 2026-10-14 | A NULL Pointer Dereference vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS  |
| CVE-2026-101952 | 7.5 | 2026-10-14 | An Improper Validation of Consistency within Input vulnerability in the routing protocol daemon (rpd) of Juniper Network |
| CVE-2026-101954 | 9.8 | 2026-10-14 | An Improper Authentication vulnerability in the J-Web management interface and its NETCONF session handling of Juniper N |
| CVE-2026-101961 | 7.5 | 2026-10-14 | A NULL Pointer Dereference vulnerability in the routing-policy nexthop-ECMP matcher of Juniper Networks Junos OS and Jun |
| CVE-2026-101962 | 7.5 | 2026-10-14 | An Improper Handling of Length Parameter Inconsistency vulnerability in the routing protocol daemon (rpd) of Juniper Net |
| CVE-2026-101963 | 7.5 | 2026-10-14 | An Incorrect Calculation vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos EVO a |
| CVE-2026-101976 | 7.5 | 2026-10-14 | An Out-of-bounds Write vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS Evol |
| CVE-2026-101979 | 8.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the authd Juniper Networks Junos OS and Junos OS Evolved allows a network |
| CVE-2026-101981 | 8.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos  |
| CVE-2026-101982 | 9.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the routing protocol daemon (rpd)  of Juniper Networks Junos OS and Junos |
| CVE-2026-101983 | 9.8 | 2026-10-14 | A Stack-based Buffer Overflow vulnerability in the httpd process of Juniper Networks Junos OS and Junos OS Evolved allow |
| CVE-2026-102077 | 7.5 | 2026-10-14 | An Improper Check for Unusual or Exceptional Conditions vulnerability in the Packet Forwarding Engine (PFE) of Juniper N |
| CVE-2026-103081 | 7.5 | 2026-10-14 | Improper Control of Generation of Code ('Code Injection') vulnerability in VillaTheme Salevo woo-boost-sales allows Code |
| CVE-2026-104103 | 8.1 | 2026-10-14 | Ludwig is a low-code framework for building custom LLMs, neural networks, and other AI models. Prior to 0.17.8, ludwig.d |
| CVE-2026-105066 | 7.1 | 2026-10-14 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in SimplyRETS SimplyR |
| CVE-2026-107349 | 7.5 | 2026-10-14 | An infinite loop in PgBouncer 1.20.0 through 1.26.0 allows an unauthenticated remote attacker to cause a denial of servi |
| CVE-2026-107350 | 8.8 | 2026-10-14 | Improper authentication in PgBouncer 1.17.0 through 1.26.0 allows a remote attacker who knows the password of a user lis |
| CVE-2026-108390 | 9.9 | 2026-10-14 | Hestia Control Panel is a lightweight and powerful control panel for the modern web. From version 1.9.7 through 1.10.4,  |
| CVE-2026-108395 | 7.5 | 2026-10-14 | The Model Context Protocol Java SDK is the official Java SDK for Model Context Protocol servers and clients. From versio |
| CVE-2026-108480 | 8.2 | 2026-10-14 | Missing Authorization vulnerability in Skydropx Skydropx skydropx allows Exploiting Incorrectly Configured Access Contro |
| CVE-2026-108483 | 7.1 | 2026-10-14 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in hippooo Hippoo Mob |
| CVE-2026-108484 | 7.1 | 2026-10-14 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WPManageNinja Best |
| CVE-2026-109527 | 7.5 | 2026-10-14 | The Model Context Protocol Python SDK is the official Python SDK for Model Context Protocol servers and clients. In mcp  |
| CVE-2026-54554 | 7.5 | 2026-10-14 | FOG is a free open-source cloning/imaging/rescue suite/inventory management system. Prior to 1.5.10.1870, the management |
| CVE-2026-55572 | 10.0 | 2026-10-14 | e107 is a content management system (CMS). Prior to 2.3.7, the bundled alt_auth plugin's otherdb and e107db authenticati |
| CVE-2026-55573 | 9.8 | 2026-10-14 | e107 is a content management system (CMS). Prior to 2.3.7, install.php decodes the attacker-controlled previous_steps PO |
| CVE-2026-79957 | 8.1 | 2026-10-14 | ServiceNext contains an insecure direct object reference (IDOR) in the /api/Usuario/GetUsuarios endpoint, which accepts  |
| CVE-2026-86461 | 8.8 | 2026-10-14 | The FV Flowplayer Video Player plugin for WordPress is vulnerable to Limited Arbitrary File Upload in all versions up to |
| CVE-2026-86567 | 8.8 | 2026-10-14 | A flaw was found in DPDK lib/vhost. The VDUSE handler fails to invalidate vring pointers when the IOTLB is invalidated,  |
| CVE-2026-86848 | 8.8 | 2026-10-14 | A flaw was found in DPDK lib/vhost vhost-crypto. The indirect-descriptor snapshot double-fetches a guest descriptor next |
| CVE-2026-88164 | 8.8 | 2026-10-14 | Missing authorization in Microsoft Office SharePoint allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-92150 | 7.5 | 2026-10-14 | F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applicati |
| CVE-2026-92154 | 8.1 | 2026-10-14 | F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applicati |
| CVE-2026-92155 | 7.5 | 2026-10-14 | F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applicati |
| CVE-2026-92158 | 7.2 | 2026-10-14 | F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applicati |
| CVE-2026-102944 | 7.5 | 2026-10-14 | cpp-httplib is a C++ header-only HTTP/HTTPS library. Prior to 0.51.0, create_redirect_client() removes Host, Proxy-Autho |
| CVE-2026-110536 | 10.0 | 2026-10-14 | A vulnerability was determined in D-Link DIR-868L 2.01b05. This impacts the function system of the file /htdocs/cgibin o |
| CVE-2026-110667 | 7.3 | 2026-10-14 | A security flaw has been discovered in cemtan sar2html 4.0.0. Affected by this vulnerability is an unknown functionality |
| CVE-2026-110761 | 8.8 | 2026-10-14 | ILIAS before 9.24, 10.12, and 11.5 contains a PHP object injection vulnerability that allows authenticated users with Te |
| CVE-2026-110767 | 7.5 | 2026-10-14 | Gitingest through 0.3.1 contains a symlink following vulnerability in ingest_query single-file blob ingestion that allow |
| CVE-2026-110769 | 8.6 | 2026-10-14 | holaOS through 2026.822.1 contains a missing authorization vulnerability in channel-gateway connectors that allows any m |
| CVE-2026-110770 | 8.1 | 2026-10-14 | Databasus 3.7.0 through 3.61.0 contains an authentication bypass vulnerability that allows unauthenticated attackers to  |
| CVE-2026-53999 | 7.7 | 2026-10-14 | Radius is a cloud-native, portable application platform that makes app development easier for teams building cloud-nativ |
| CVE-2026-54525 | 8.8 | 2026-10-14 | Markdown Preview Enhanced is a Markdown preview extension for Visual Studio Code. Prior to 0.8.28, Markdown Preview Enha |
| CVE-2026-55786 | 8.4 | 2026-10-14 | Flyto2 Core is an execution kernel for automation and AI-agent workflows. From 2.26.2 until 2.26.4, the HTTP MCP POST /m |
| CVE-2026-55787 | 7.1 | 2026-10-14 | Flyto2 Core is an execution kernel for automation and AI-agent workflows. Prior to 2.26.3, validate_url_ssrf and is_priv |
| CVE-2026-63626 | 8.8 | 2026-10-14 | Mongoose is an embedded web server and network library. Prior to 7.23, ppp_handle_ipv6cp() in src/l2_ppp.c trusts the 16 |
| CVE-2026-73252 | 7.5 | 2026-10-14 | Mongoose is an embedded web server and network library. Prior to 7.23, the built-in TLS stack selected by MG_TLS_BUILTIN |
| CVE-2026-73260 | 7.5 | 2026-10-14 | Mongoose is an embedded web server and network library. Prior to 7.23, the built-in TLS certificate parser selected by M |
| CVE-2026-73261 | 7.5 | 2026-10-14 | Mongoose is an embedded web server and network library. Prior to 7.23, the built-in TCP/IP stack enabled by MG_ENABLE_TC |
| CVE-2026-85714 | 9.1 | 2026-10-14 | Stirling-PDF is a locally hosted web application that facilitates various operations on PDF files. Prior to 2.13.2, an a |
| CVE-2026-102986 | 8.1 | 2026-10-14 | Plane is an open-source project management tool. In 1.3.1 and earlier, EntityAssetEndpoint at the public project asset e |
| CVE-2026-110668 | 7.3 | 2026-10-14 | A weakness has been identified in cemtan sar2html 4.0.0. Affected by this issue is the function index of the file sar2ht |
| CVE-2026-55381 | 7.1 | 2026-10-14 | InvoiceShelf is an open-source web & mobile app that helps track expenses, payments and create professional invoices and |
| CVE-2026-55382 | 7.6 | 2026-10-14 | InvoiceShelf is an open-source web & mobile app that helps track expenses, payments and create professional invoices and |
| CVE-2026-55383 | 8.2 | 2026-10-14 | InvoiceShelf is an open-source web & mobile app that helps track expenses, payments and create professional invoices and |
| CVE-2026-55680 | 9.8 | 2026-10-14 | WeGIA is a web manager for charitable institutions. Prior to 3.8.6, unauthenticated POST requests to web/html/socio/sist |
| CVE-2026-55681 | 8.8 | 2026-10-14 | WeGIA is a web manager for charitable institutions. Prior to 3.8.6, an authenticated user with access to the Material &  |
| CVE-2026-55682 | 8.1 | 2026-10-14 | WeGIA is a web manager for charitable institutions. Prior to 3.8.6, the auto-prepended web/html/seguranca/sessionStart.p |
| CVE-2026-55683 | 9.8 | 2026-10-14 | WeGIA is a web manager for charitable institutions. Prior to 3.8.6, the unauthenticated web/html/socio/sistema/cadastro_ |
| CVE-2026-55684 | 9.8 | 2026-10-14 | WeGIA is a web manager for charitable institutions. Prior to 3.8.6, the unauthenticated web/html/socio/sistema/cadastro_ |
| CVE-2026-103977 | 8.1 | 2026-10-14 | FileRise is a self-hosted web-based file manager with multi-file upload, editing, and batch operations. Prior to 3.23.0, |
| CVE-2026-104108 | 8.1 | 2026-10-14 | FileRise is a self-hosted web-based file manager with multi-file upload, editing, and batch operations. Prior to 3.23.0, |
| CVE-2026-110670 | 7.3 | 2026-10-14 | A vulnerability was found in cemtan sar2html 4.0.0. The affected element is the function updateDb of the file sar2html.p |
| CVE-2026-110679 | 7.3 | 2026-10-14 | A vulnerability was determined in OpenSIPS up to 3.6.8/4.0.1. The impacted element is the function rtpproxy_offer/rtppro |
| CVE-2026-57489 | 8.1 | 2026-10-14 | FileRise is a self-hosted web-based file manager with multi-file upload, editing, and batch operations. Prior to 3.16.0, |
| CVE-2026-57490 | 8.1 | 2026-10-14 | FileRise is a self-hosted web-based file manager with multi-file upload, editing, and batch operations. Prior to 3.16.0, |
| CVE-2026-57492 | 7.4 | 2026-10-14 | FileRise is a self-hosted web-based file manager with multi-file upload, editing, and batch operations. Prior to 3.16.0, |
| CVE-2026-61843 | 8.2 | 2026-10-14 | FileRise is a self-hosted web-based file manager with multi-file upload, editing, and batch operations. Prior to 3.18.0, |
| CVE-2026-61844 | 7.1 | 2026-10-14 | FileRise is a self-hosted web-based file manager with multi-file upload, editing, and batch operations. Prior to 3.18.0, |
| CVE-2026-71854 | 8.2 | 2026-10-14 | OpenAEV is an open source platform allowing organizations to plan, schedule and conduct cyber adversary simulation campa |
| CVE-2026-110837 | 7.1 | 2026-10-14 | FreeRDP 2.0.0 before 3.32.0, when built with WITH_LAME=ON and WITH_DSP_FFMPEG=OFF, has a heap-based buffer overflow in f |
| CVE-2026-110838 | 7.5 | 2026-10-14 | FreeRDP shadow server from 3.0.0 before 3.32.0 dispatches input PDUs during the Confirm Active state before authenticati |
| CVE-2026-110839 | 7.1 | 2026-10-14 | FreeRDP 3.3.0 before 3.32.0, when built with WINPR_UTILS_IMAGE_JPEG=ON, has a heap-based out-of-bounds write in winpr_co |
| CVE-2026-110856 | 7.5 | 2026-10-14 | GitPython before 3.2.0 contains a regular expression denial of service vulnerability in the _re_actor_epoch pattern used |
| CVE-2026-110857 | 7.5 | 2026-10-14 | GitPython before 3.2.0 contains a remote code execution vulnerability that allows attackers to run commands because Git. |
| CVE-2026-110858 | 8.1 | 2026-10-14 | GitPython from 3.1.30 before 3.2.0 contains a remote code execution vulnerability in Remote.pull() whose unsafe-option g |
| CVE-2026-110859 | 7.5 | 2026-10-14 | GitPython before 3.2.0 contains an argument injection vulnerability in Head.checkout() that allows remote attackers to r |
| CVE-2026-110862 | 9.1 | 2026-10-14 | Better Auth from 1.4.0-beta.18 before 1.7.7 contains an authentication bypass vulnerability that allows unauthenticated  |
| CVE-2026-110863 | 8.1 | 2026-10-14 | Better Auth @better-auth/sso from 1.7.0-rc.2 before 1.7.3 contains an authentication bypass vulnerability that allows au |
| CVE-2026-110864 | 7.4 | 2026-10-14 | Better Auth from 1.5.0-beta.12 before 1.7.7 contains an authentication bypass vulnerability in the OAuth Proxy plugin th |
| CVE-2026-110865 | 7.1 | 2026-10-14 | Renovate before 44.60.1 contains an allowlist bypass vulnerability that allows repository users to evade the allowedHead |
| CVE-2026-110867 | 8.5 | 2026-10-14 | Renovate before 44.60.1 contains an allowlist bypass vulnerability that allows repositories to set restricted environmen |
| CVE-2026-110868 | 8.5 | 2026-10-14 | Renovate before 44.79.0 contains a server-side request forgery vulnerability that allows users to make the shared HTTP c |
| CVE-2026-110869 | 7.5 | 2026-10-14 | Nodemailer 3.0.0 before 10.0.13 has a regular expression denial of service in SMTPConnection._actionEHLO, whose four AUT |
| CVE-2026-110873 | 7.1 | 2026-10-14 | Heym from 0.0.55 before 0.0.121 contains a privilege escalation vulnerability that allows shared collaborators to overwr |
| CVE-2026-0993 | 7.5 | 2026-10-15 | SODOLA SL902-SWTGW124AS firmware before 200.2.12 contains a buffer overflow vulnerability that allows unauthenticated re |
| CVE-2026-109430 | 7.5 | 2026-10-15 | Ellucian WebAdvisor 3.2 contains an unauthenticated XML External Entity (XXE) injection vulnerability that allows remote |
| CVE-2026-73799 | 7.5 | 2026-10-15 | A security vulnerability in HPE NonStop SNMP Trap Multiplexer may cause memory corruption |
| CVE-2026-76066 | 7.5 | 2026-10-15 | IntentKit through 2.6.3 contains an authorization bypass vulnerability where the executor validates tool calls against t |
| CVE-2026-76659 | 7.5 | 2026-10-15 | A vulnerability in the finger daemon of HPE NonStop TCP/IP UTILITIES could allow an unauthenticated remote attacker to c |
| CVE-2026-76660 | 8.7 | 2026-10-15 | A vulnerability in HPE NonStop CIPSAM allows an out-of-bounds
  write that can corrupt buffer data. |
| CVE-2026-76661 | 7.6 | 2026-10-15 | A vulnerability in HPE NonStop QIOMON allows an out-of-bounds write that can corrupt buffer data. |
| CVE-2026-77931 | 8.8 | 2026-10-15 | MoviePilot through 3.1.5 contains a command injection vulnerability that allows attackers to execute arbitrary OS comman |
| CVE-2026-110907 | 7.5 | 2026-10-15 | Backdrop CMS Core 1.35.x before 1.35.2 and 1.34.x before 1.34.6 mishandles tokens. A token is a small placeholder string |
| CVE-2026-110908 | 8.8 | 2026-10-15 | Netgate pfSense FRR package (pfSense-pkg-frr) 2.0.2_1 and source revision 2.1.2_1 contain an OS command injection vulner |
| CVE-2026-76663 | 7.5 | 2026-10-15 | A stack-based buffer overflow vulnerability in HPE NonStop TELSERV can cause memory corruption that may result in DoS. |
| CVE-2026-110911 | 9.8 | 2026-10-15 | Wheels 1.1.8 through 4.1.1 allows SQL injection when caller-supplied quoted values are parsed again as SQL by dynamic fi |
| CVE-2026-108587 | 9.8 | 2026-10-15 | The 10Web Booster – Website speed optimization, Cache & Page Speed optimizer plugin for WordPress is vulnerable to Arbit |
| CVE-2026-3712 | 7.3 | 2026-10-15 | The PhastPress plugin for WordPress is vulnerable to Server-Side Request Forgery in all versions up to, and including, 3 |
| CVE-2026-76665 | 7.1 | 2026-10-15 | A security vulnerability in HPE NonStop EXPAND may cause out-of-bounds memory read resulting in buffer overflow. |
| CVE-2026-15090 | 7.5 | 2026-10-15 | The Link Library plugin for WordPress is vulnerable to time-based SQL Injection via the 'link_url' parameter in all vers |
| CVE-2026-17031 | 8.1 | 2026-10-15 | The Checkout Field Manager (Checkout Manager) for WooCommerce plugin for WordPress is vulnerable to authorization bypass |
| CVE-2026-18548 | 7.2 | 2026-10-15 | The Groundhogg — CRM, Newsletters, and Marketing Automation plugin for WordPress is vulnerable to Stored Cross-Site Scri |
| CVE-2026-18586 | 7.2 | 2026-10-15 | The Premium Packages – Sell Digital Products Securely plugin for WordPress is vulnerable to Unauthenticated Stored Cross |
| CVE-2026-88043 | 7.2 | 2026-10-15 | The Mang Board WP plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'data_type' parameter in all |
| CVE-2026-109145 | 9.8 | 2026-10-15 | The User Rights Access Manager WordPress plugin through 1.1.3 does not restrict access to one of its AJAX account-regist |
| CVE-2026-74920 | 7.1 | 2026-10-15 | The Document Gallery WordPress plugin through 5.1.1 does not properly sanitise and escape user input before reflecting i |
| CVE-2026-79821 | 8.2 | 2026-10-15 | A security vulnerability in HPE NonStop SOAP 4.0  may cause memory corruption resulting in a system down. |
| CVE-2026-79822 | 7.1 | 2026-10-15 | A security vulnerability in HPE NonStop TNS/X Native Inspect may cause corruption of address and potentially redirect ex |
| CVE-2026-81534 | 8.8 | 2026-10-15 | The Email Customizer for WooCommerce (Pro) plugin for WordPress is vulnerable to Remote Code Execution in versions up to |
| CVE-2026-96537 | 7.5 | 2026-10-15 | The Tutor LMS  WordPress plugin before 4.1.1 does not perform a capability check in a routine that regenerates its manag |
| CVE-2023-32198 | 8.0 | 2026-10-15 | A vulnerability has been identified in Steve where by default it was using an insecure option that did not validate the  |
| CVE-2024-22031 | 8.5 | 2026-10-15 | A vulnerability has been identified within Rancher where a user with the ability to create a project, on a certain clust |
| CVE-2026-101290 | 7.5 | 2026-10-15 | A remote attacker may send a specially crafted network packet that causes the
affected application to perform an out-of- |
| CVE-2026-109855 | 7.5 | 2026-10-15 | undici is an HTTP client library for Node.js. In versions 8.11.0 and 8.11.1, its experimental WebSocket client, which is |
| CVE-2026-79824 | 8.0 | 2026-10-15 | A directory traversal vulnerability in HPE NonStop Python 3.x could allow  attackers to overwrite arbitrary files via a  |
| CVE-2026-79825 | 7.1 | 2026-10-15 | A heap buffer overflow in HPE NonStop NDSREST could corrupt resume-execution address and may potentially redirect execut |
| CVE-2026-79826 | 7.1 | 2026-10-15 | A heap buffer overflow in HPE NonStop OCAX could corrupt address space and may potentially redirect execution flow. |
| CVE-2026-79827 | 7.1 | 2026-10-15 | A heap buffer overflow in HPE NonStop Inspect Subsystem could corrupt resume-execution address and may potentially redir |
| CVE-2026-79828 | 7.1 | 2026-10-15 | A heap buffer overflow in HPE NonStop Debug Utilities  could corrupt resume-execution address and may potentially redire |
| CVE-2026-79829 | 8.2 | 2026-10-15 | A security vulnerability in HPE NonStop HTTP WEBSERVER can cause memory corruption which may result in a system halt. |
| CVE-2026-108491 | 7.1 | 2026-10-15 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Everest Forms Ever |
| CVE-2026-108497 | 9.3 | 2026-10-15 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in TMS Amelia ameliab |
| CVE-2026-108498 | 7.1 | 2026-10-15 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in bannersky BSK PDF  |
| CVE-2026-109694 | 9.8 | 2026-10-15 | Incorrect Privilege Assignment vulnerability in WP ManageNinja LLC Fluent CRM fluent-crm allows Privilege Escalation.Thi |
| CVE-2026-109695 | 7.5 | 2026-10-15 | Insertion of Sensitive Information Into Sent Data vulnerability in WPManageNinja FluentCart fluent-cart allows Retrieve  |
| CVE-2026-79832 | 7.6 | 2026-10-15 | A stack buffer overflow vulnerability in HPE NonStop SQL/MX Executor may potentially result in information disclosure or |
| CVE-2026-79833 | 7.5 | 2026-10-15 | A vulnerability in HPE NonStop ANSI SQLUTIL may allow a remote unauthenticated actor to cause an affected service to ter |
| CVE-2026-79834 | 7.4 | 2026-10-15 | A security vulnerability in HPE NonStop SQL/MX SQLCAT may allow an unauthenticated user to perform unauthorized command  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-105134 | Ahsay / AhsayCBS | 2026-10-14 | 2026-10-17 | Unknown |
| CVE-2026-76519 | Cisco / Secure Email Gateway | 2026-10-14 | 2026-10-17 | Unknown |
| CVE-2026-105133 | Ahsay / AhsayCBS | 2026-10-14 | 2026-10-17 | Unknown |
| CVE-2026-0322 | Palo Alto Networks / PAN-OS | 2026-10-14 | 2026-10-17 | Unknown |
| CVE-2026-104935 | Ivanti / Connect Secure | 2026-10-13 | 2026-10-16 | Unknown |
| CVE-2026-96951 | Microsoft / Windows | 2026-10-13 | 2026-10-16 | Unknown |
| CVE-2015-5477 | ISC / BIND | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2016-3081 | Apache / Struts | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2023-22894 | Strapi / Strapi | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2021-3199 | ONLYOFFICE / Docs | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2015-3306 | ProFTPD / ProFTPD | 2026-10-08 | 2026-10-11 | Unknown |

---

*Total entries in CISA KEV catalog: 1745*