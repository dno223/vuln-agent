# Vulnerability Intelligence Report

**Date:** 2026-11-10  
**Generated:** 2026-11-10T16:06:18Z  

---

## Executive Summary

Our environment faces significant exposure across 266 high-severity vulnerabilities, with 7 newly added CISA Known Exploited Vulnerabilities (KEVs) confirmed as actively exploited in the wild. Critical findings include two CVSS 9.8-rated flaws in Tasmota firmware and Redpanda Connect enabling unauthenticated remote code execution, alongside multiple Progress WS_FTP Server vulnerabilities affecting data confidentiality and access control. KEV additions spanning OpenSSH, SonicWall SSLVPN, IBM Aspera Faspex, and GPUStack signal broad, active threat actor campaigns. Immediate remediation of KEV-listed vulnerabilities is required under CISA Binding Operational Directive 22-01.

---

## Risk Narrative

Threat actors are actively exploiting vulnerabilities across widely deployed infrastructure components including VPN gateways, SSH servers, file transfer platforms, and IoT firmware. The presence of unauthenticated RCE flaws in Tasmota and Redpanda Connect dramatically increases the blast radius of potential breaches, enabling lateral movement without initial credential theft. CISA KEV additions reflect real-world exploitation campaigns, not theoretical risk. WS_FTP Server vulnerabilities expose credential data and session tokens, creating pathways for persistent access. WordPress plugin flaws extend risk to customer-facing digital assets. Combined, this landscape increases the probability of data breach, ransomware deployment, and regulatory compliance failures with material financial and reputational consequences.

---

## Prioritized Action Items

1. Immediately patch or isolate all systems affected by the 7 newly added CISA KEV vulnerabilities, prioritizing OpenSSH, SonicWall SSLVPN, and IBM Aspera Faspex as these are actively exploited and internet-facing.
2. Upgrade Tasmota firmware past commit e97e1e4 and Redpanda Connect to a version above 4.110 to remediate the two CVSS 9.8 unauthenticated remote code execution vulnerabilities.
3. Upgrade Progress WS_FTP Server to version 2025.0.5 or later to address all four high-severity CVEs including credential exposure, session interception, and unauthorized access.
4. Audit and remediate the WordPress AI Workflow Automation plugin (CVE-2026-121576) to prevent privilege escalation attacks against web properties.
5. Conduct a full inventory scan to identify all vulnerable asset instances across the 266 high-severity CVEs and establish a 30-day remediation SLA for critical and high findings.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-115338 | 8.1 | 2026-11-09 | Insufficient protection of communications in Progress WS_FTP Server versions prior to 2025.0.5 could allow a network att |
| CVE-2026-115339 | 7.5 | 2026-11-09 | Insufficient resource limits in Progress Software WS_FTP Server releases prior to 2025.0.5 on Windows could allow an una |
| CVE-2026-115340 | 7.1 | 2026-11-09 | Progress Software WS_FTP Server versions prior to 2025.0.5 on Windows may write sensitive user credential and session da |
| CVE-2026-115341 | 7.7 | 2026-11-09 | Improper access restrictions in the Thin Client Web Transfer component of Progress Software WS_FTP Server versions prior |
| CVE-2026-121576 | 8.8 | 2026-11-09 | Incorrect Privilege Assignment vulnerability in AtlasAiDev MCP Server for WordPress ai-workflow-automation-ai-agent-hub  |
| CVE-2026-122664 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in VideoWhisper.com B |
| CVE-2026-123482 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Crocoblock JetForm |
| CVE-2026-119755 | 7.5 | 2026-11-09 | Tasmota through 16.0.0, fixed in commit 1cb7ebc, contains a cross-site request forgery vulnerability that allows unauthe |
| CVE-2026-119756 | 9.8 | 2026-11-09 | Tasmota through 16.0.0, fixed in commit e97e1e4, contains a heap out-of-bounds write vulnerability in SendReceiveDeviceG |
| CVE-2026-123270 | 9.8 | 2026-11-09 | Redpanda Connect versions 4.39 to 4.110 contain a missing authentication vulnerability that enables unauthenticated remo |
| CVE-2026-123367 | 7.4 | 2026-11-09 | Thor Vector Graphics (ThorVG) is a production-ready vector graphics engine. Prior to 1.1.2, the bundled jpgd JPEG decode |
| CVE-2026-123797 | 7.5 | 2026-11-09 | SuperTokens Core is an open source authentication server. Prior to 11.3.6, 11.4.6, and 12.0.8, app-specific management r |
| CVE-2026-19706 | 8.3 | 2026-11-09 | During ABI bootstrap, the bootstrap node's approve-csr.service approves and signs every CSR without identity validation. |
| CVE-2026-112314 | 7.5 | 2026-11-09 | clnttcp_call() in lib/rpc/clnt_tcp.c in MIT Kerberos 5 (aka krb5) does not free the RPC reply verifier between retries,  |
| CVE-2026-112320 | 7.5 | 2026-11-09 | The GSS-RPC transport layer in MIT Kerberos 5 (aka krb5) 1.4 and later does not release the previous authentication cont |
| CVE-2026-112321 | 7.5 | 2026-11-09 | The AUTH_GSSAPI handler in lib/rpc/svc_auth_gssapi.c in MIT Kerberos 5 (aka krb5) does not free decoded arguments on cer |
| CVE-2026-112322 | 7.5 | 2026-11-09 | clean_client() in lib/rpc/svc_auth_gssapi.c in MIT Kerberos 5 (aka krb5) restarts its scan from the head of the client l |
| CVE-2026-112323 | 7.5 | 2026-11-09 | The AUTH_GSSAPI handler in lib/rpc/svc_auth_gssapi.c in MIT Kerberos 5 (aka krb5) 1.5.2 and later allows remote attacker |
| CVE-2026-119079 | 7.5 | 2026-11-09 | decode_sequence_of() in lib/krb5/asn.1/asn1_encode.c in MIT Kerberos 5 (aka krb5) 1.11 and later grows the decoded eleme |
| CVE-2026-120834 | 7.3 | 2026-11-09 | Incorrect Privilege Assignment vulnerability in Tobias WP2LEADS wp2leads allows Privilege Escalation.This issue affects  |
| CVE-2026-121769 | 8.5 | 2026-11-09 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in axew3.com WP w3all |
| CVE-2026-123798 | 8.1 | 2026-11-09 | SuperTokens Core is an open source authentication server. From 11.3.0 until 11.3.7, 11.4.7, and 12.0.10, SAML.verifySaml |
| CVE-2026-123799 | 7.4 | 2026-11-09 | SuperTokens Core is an open source authentication server. From 11.0.0 until 11.0.9, 11.1.4, 11.2.4, 11.3.8, 11.4.8, 12.0 |
| CVE-2026-123800 | 9.9 | 2026-11-09 | SuperTokens Core is an open source authentication server. From 6.0.0 until 6.0.24, 7.0.23, 8.0.7, 9.0.6, 9.1.6, 9.2.7, 9 |
| CVE-2026-123801 | 7.4 | 2026-11-09 | SuperTokens Core is an open source authentication server. From 11.3.0 until 11.3.8, 11.4.8, 12.0.11, 12.1.2, 12.2.1, and |
| CVE-2026-123802 | 8.1 | 2026-11-09 | SuperTokens Core is an open source authentication server. From 11.3.0 until 11.3.8, 11.4.8, 12.0.11, 12.1.2, 12.2.1, and |
| CVE-2026-123803 | 8.1 | 2026-11-09 | SuperTokens Core is an open source authentication server. From 10.1.0 until 11.0.9, 11.1.4, 11.2.4, 11.3.8, 11.4.8, 12.0 |
| CVE-2026-123999 | 7.5 | 2026-11-09 | NASA JPL ION-DTN 3.6.2 through 4.2.0 contains a heap-based buffer overflow in the Network Management daemon (nm_mgr) str |
| CVE-2026-124001 | 8.1 | 2026-11-09 | NASA JPL ION-DTN 2.2.1b through 4.2.0 contains an integer overflow vulnerability in the Datagram Retransmission (DGR) co |
| CVE-2026-125181 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains an out-of-bounds write vulnerability in flic_decode_frame_15_16BPP() in libavcodec/flicvid |
| CVE-2026-125196 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in liboapve_encode() in libavcodec/liboapvenc.c that  |
| CVE-2026-125201 | 7.0 | 2026-11-09 | FFmpeg 7.0 before 8.1.3 and 9.x before 9.0.2 contains a heap out-of-bounds write vulnerability in vk_av1_decode_slice()  |
| CVE-2026-125202 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in vaapi_hevc_start_frame() in libavcodec/vaapi_hevc. |
| CVE-2026-125203 | 7.8 | 2026-11-09 | FFmpeg before 8.1.3 and 9.x before 9.0.2 contains a heap buffer overflow vulnerability in the Cook multichannel decoder  |
| CVE-2026-125204 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains a heap buffer overflow in ff_libwebp_get_frame() in libwebpenc_common.c that lets attacker |
| CVE-2026-125208 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains an out-of-bounds write vulnerability in v4l2_buffer_swframe_to_buf() in libavcodec/v4l2_bu |
| CVE-2026-125209 | 7.8 | 2026-11-09 | FFmpeg before 8.1.3 and 9.x before 9.0.2 contains a heap buffer overflow vulnerability in the DVD subtitle encoder that  |
| CVE-2026-125210 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in aribcaption_trans_text_subtitle() in libavcodec/li |
| CVE-2026-125211 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains an out-of-bounds read and invalid free vulnerability in aribcaption_trans_ass_subtitle() i |
| CVE-2026-125212 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in libavcodec/videotoolboxenc.c that copies frames la |
| CVE-2026-125213 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in the PSD decoder in libavcodec/psd.c that allows at |
| CVE-2026-125214 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in pcm_bluray_decode_frame() in libavcodec/pcm-bluray |
| CVE-2026-125218 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in the APNG encoder's encode_apng() function in libav |
| CVE-2026-125219 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in vdpau_hevc_start_frame() in libavcodec/vdpau_hevc. |
| CVE-2026-125222 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains an integer overflow vulnerability in hap_parse_frame_header() in libavcodec/hapdec.c that  |
| CVE-2026-125227 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains an integer overflow in cbs_jpeg_write_scan() in libavcodec/cbs_jpeg.c that causes a heap b |
| CVE-2026-125229 | 7.8 | 2026-11-09 | FFmpeg through 9.0.2 contains an out-of-bounds memory access vulnerability in the encode_frame() function of libavcodec/ |
| CVE-2026-125233 | 7.8 | 2026-11-09 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in dvbsub_encode() in libavcodec/dvbsubenc.c that und |
| CVE-2026-125235 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains a heap overflow vulnerability in libavcodec/qsvenc.c that allows attackers to corrupt memo |
| CVE-2026-125239 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in ff_dxva2_hevc_fill_picture_parameters() that allow |
| CVE-2026-125241 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in libavcodec/flicvideo.c that allows attackers to wr |
| CVE-2026-125244 | 7.8 | 2026-11-09 | FFmpeg before 8.1.3 and 9.x before 9.0.2 contains an out-of-bounds write vulnerability in the VVC decoder's sh_entry_poi |
| CVE-2026-125248 | 7.0 | 2026-11-09 | FFmpeg 9.0 through 9.0.2 contains an integer overflow vulnerability in libavcodec/ffv1enc_vulkan.c that undersizes the f |
| CVE-2026-125249 | 7.0 | 2026-11-09 | FFmpeg 7.1 through 9.0.2 contains an integer overflow in ff_vk_decode_add_slice() in libavcodec/vulkan_decode.c that mis |
| CVE-2026-125250 | 7.8 | 2026-11-09 | FFmpeg through 9.0.2 contains a heap buffer overflow in the GIF encoder's gif_image_write_image() in libavcodec/gif.c be |
| CVE-2026-125251 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains an integer overflow vulnerability in the VVC decoder alloc_frame() function in libavcodec/ |
| CVE-2026-12977 | 8.8 | 2026-11-09 | A flaw was found in the deployment-operation family of WildFly Core. Certain handlers, such as upload-deployment-url, la |
| CVE-2026-123805 | 7.5 | 2026-11-09 | SIPSorcery is a WebRTC, SIP, and VoIP library for C# and .NET. Prior to 10.0.14, SctpSackChunk.ParseChunk reads the numG |
| CVE-2026-125256 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in ff_llvidenc_diff_bytes_rvv() that allows attackers |
| CVE-2026-125257 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains an off-by-one heap overflow vulnerability in get_exponent_dynamic() in libavcodec/nellymos |
| CVE-2026-125259 | 7.8 | 2026-11-09 | FFmpeg through 9.0.2 contains an integer overflow vulnerability in ff_prores_kostya_encode_init() that miscalculates fra |
| CVE-2026-125260 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in libavcodec/exrenc.c that allows attackers to corru |
| CVE-2026-125262 | 7.8 | 2026-11-09 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in libavcodec/lcevcdec.c because LCEVC output picture |
| CVE-2026-125267 | 7.8 | 2026-11-09 | FFmpeg before 8.1.3 and 9.x before 9.0.2 contains a heap out-of-bounds write vulnerability in the APAC decoder in libavc |
| CVE-2026-125269 | 7.0 | 2026-11-09 | FFmpeg through 9.0.2 contains a double free vulnerability in libavcodec/cbs_sei.c where cbs_sei_delete_message() leaves  |
| CVE-2026-102643 | 8.8 | 2026-11-09 | AsyncSSH is a Python package which provides an asynchronous client and server implementation of the SSHv2 protocol on to |
| CVE-2026-113961 | 7.5 | 2026-11-09 | An authorization issue was addressed with improved validation. This issue is fixed in iOS 26.7.3 and iPadOS 26.7.3, iOS  |
| CVE-2026-113970 | 8.8 | 2026-11-09 | A use-after-free issue was addressed with improved memory management. This issue is fixed in iOS 18.7.12 and iPadOS 18.7 |
| CVE-2026-114031 | 7.8 | 2026-11-09 | Incorrect permission assignment allows local privilege escalation to SYSTEM on affected releases of the Illumio VEN for  |
| CVE-2026-114032 | 7.8 | 2026-11-09 | The OpenSSL library bundled with the Illumio VEN for Windows is affected by an uncontrolled search path vulnerability. A |
| CVE-2026-119759 | 8.1 | 2026-11-09 | TrailBase 0.28.2 before 0.35.10 contains an insecure direct object reference vulnerability that allows authenticated att |
| CVE-2026-123807 | 9.8 | 2026-11-09 | Signal K Server is a server application that runs on a central hub in a boat. From 2.0.0 until 2.34.0 for Signal K Serve |
| CVE-2026-123811 | 7.5 | 2026-11-09 | Dynatrace MCP Server is an MCP server for Dynatrace Observability. Prior to 2.0.0, a server started with the --http opti |
| CVE-2026-123813 | 7.5 | 2026-11-09 | pyLoad is a free and open-source download manager written in Python. Prior to 0.5.0b3.dev102, pyLoad does not invalidate |
| CVE-2026-123816 | 8.1 | 2026-11-09 | pyLoad is a free and open-source download manager written in Python. Prior to 0.5.0b3.dev101, Api.check_apikey caches su |
| CVE-2026-123818 | 7.5 | 2026-11-09 | LMDeploy is a toolkit for compressing, deploying, and serving large language models. From 0.12.3 until 0.15.0, _is_safe_ |
| CVE-2026-125107 | 7.5 | 2026-11-09 | Muhammara is a node module with c/cpp bindings to modify PDF with JavaScript for node or electron. Prior to 6.0.5, Muham |
| CVE-2026-125111 | 7.5 | 2026-11-09 | Rack is a modular Ruby web server interface. Prior to 2.2.25, 3.1.23, and 3.2.8, Rack::Multipart::Parser can retain pars |
| CVE-2026-56712 | 8.5 | 2026-11-09 | Replicate Cog through 0.23.1 contains a server-side request forgery vulnerability that allows attackers to cause the Cog |
| CVE-2026-63496 | 7.8 | 2026-11-09 | augment-vir is a collection of helper functions. Prior to version 31.73.5, the grep() function exported by @augment-vir/ |
| CVE-2026-63644 | 7.5 | 2026-11-09 | bird-lg-go is a BIRD looking glass in Go. Prior to version 1.4.7, unsanitized input path enables arbitrary local file re |
| CVE-2026-73857 | 7.5 | 2026-11-09 | ModSecurity is an open source, cross platform web application firewall (WAF) engine for Apache, IIS and Nginx. From 3.0. |
| CVE-2026-90586 | 7.8 | 2026-11-09 | The Xtensa MMU userspace port never initialized the per-thread page-table pointer thread->arch.ptables during thread set |
| CVE-2026-90591 | 7.5 | 2026-11-09 | The NXP ENET-QOS Ethernet driver's receive work handler eth_nxp_enet_qos_rx() in drivers/ethernet/eth_nxp_enet_qos hands |
| CVE-2026-115934 | 9.8 | 2026-11-09 | An unauthenticated SQL injection can occur on the front end of any site that uses craft.search to perform a search, allo |
| CVE-2026-124035 | 7.1 | 2026-11-09 | Unsafe reflection in the error mitigation schema validation in Amazon Braket Schemas before 1.32.2 might allow a remote  |
| CVE-2026-125074 | 7.3 | 2026-11-09 | A flaw has been found in SourceCodester Smart Attendance System with QR Code Scanner 1.0. This affects an unknown functi |
| CVE-2026-125075 | 7.3 | 2026-11-09 | A vulnerability has been found in SourceCodester Smart Attendance System with QR Code Scanner 1.0. This impacts the func |
| CVE-2026-125117 | 8.2 | 2026-11-09 | Mongoose is a MongoDB object modeling tool designed to work in an asynchronous environment. Prior to 6.13.12, 7.8.13, 8. |
| CVE-2026-125119 | 7.5 | 2026-11-09 | Mongoose is a MongoDB object modeling tool designed to work in an asynchronous environment. From 6.0.0 until 6.13.12, 7. |
| CVE-2026-125120 | 9.8 | 2026-11-09 | Mongoose is a MongoDB object modeling tool designed to work in an asynchronous environment. Prior to 6.13.11, 7.8.12, 8. |
| CVE-2026-125076 | 7.3 | 2026-11-10 | A vulnerability was found in SourceCodester Smart Attendance System with QR Code Scanner 1.0. Affected is an unknown fun |
| CVE-2026-125358 | 8.1 | 2026-11-10 | Universal-modder before commit e88f6876745427321eb755ebc98276063a962d8a contains a missing WebSocket Origin validation v |
| CVE-2026-125360 | 7.2 | 2026-11-10 | Storyden through 1.26.16 contains a privilege escalation vulnerability that allows users holding MANAGE_ROLES to grant t |
| CVE-2026-125364 | 8.1 | 2026-11-10 | frab through 0.9.1 contains a privilege escalation vulnerability that allows authenticated crew users to grant themselve |
| CVE-2026-125368 | 7.5 | 2026-11-10 | OmniAgent through commit 12b98c5 contains an approval bypass vulnerability in ReflexionAgent._is_safe_bash_command that  |
| CVE-2026-125370 | 9.8 | 2026-11-10 | Kubero 3.0.0 through 3.1.1 contains an authentication bypass vulnerability that allows unauthenticated remote attackers  |
| CVE-2026-125382 | 7.2 | 2026-11-10 | Map-OS 5.0.0 to before 5.2.2 contains a privilege escalation vulnerability in the REST users API that allows non-adminis |
| CVE-2026-125383 | 9.8 | 2026-11-10 | INDOTALENT WHMS (Asp.Net-Core-Inventory-Order-Management-System) before 10.20261109 contains an authentication bypass vu |
| CVE-2026-125384 | 9.8 | 2026-11-10 | INDOTALENT WHMS before 10.20261109 contains a default credentials vulnerability that allows unauthenticated attackers to |
| CVE-2026-125391 | 7.2 | 2026-11-10 | Webmin through 2.670 contains an OS command injection vulnerability in samba/save_euser.cgi that allows authenticated Sa |
| CVE-2026-125396 | 7.8 | 2026-11-10 | Ghostscript before 10.08.0 contains a -dSAFER bypass vulnerability in the .putgstringcopy procedure in gs_fonts.ps, whic |
| CVE-2026-125397 | 7.1 | 2026-11-10 | NocoBase plugin-ai 2.1.0 through 2.2.41 contains an authorization bypass vulnerability in getAccessibleAIEmployee() that |
| CVE-2026-125398 | 7.1 | 2026-11-10 | Instatic before 0.0.21 contains an authorization bypass vulnerability in handleRowAuthor that allows authenticated users |
| CVE-2026-125399 | 8.0 | 2026-11-10 | Fluxion before 6.39 contains an OS command injection vulnerability in the fluxion.sh target scanner, which decodes acces |
| CVE-2026-125400 | 8.8 | 2026-11-10 | Ettercap through 0.8.4.1 contains a use-after-free vulnerability in func_pcre() in src/ec_filter.c that reads the PCRE2  |
| CVE-2026-125401 | 8.1 | 2026-11-10 | Ettercap through 0.8.4.1 contains a heap buffer overflow vulnerability in gg_get_version() in src/dissectors/ec_gg.c tha |
| CVE-2026-125402 | 8.1 | 2026-11-10 | Ettercap through 0.8.4.1 contains a heap out-of-bounds read vulnerability in sslw_get_clienthello_sni() in src/ec_sslwra |
| CVE-2026-125403 | 8.1 | 2026-11-10 | Ettercap through 0.8.4.1 contains an out-of-bounds read and size_t underflow vulnerability in sslw_remove_sts() in src/e |
| CVE-2026-125404 | 7.5 | 2026-11-10 | Ettercap through 0.8.4.1 contains an integer underflow in ccmp_decrypt() in src/ec_encryption_ccmp.c that subtracts the  |
| CVE-2026-125405 | 8.1 | 2026-11-10 | Ettercap through 0.8.4.1 contains an out-of-bounds read vulnerability in Parse_NTLM_Auth() in src/dissectors/ec_http.c d |
| CVE-2026-125406 | 8.8 | 2026-11-10 | Ettercap through 0.8.4.1 contains a stack buffer underwrite vulnerability in the telnet dissector in src/dissectors/ec_t |
| CVE-2026-107240 | 7.6 | 2026-11-10 | The Node.js web service on VOS (previously Versa FlexVNF) is used for URL-based Zero Touch Provisioning (ZTP) of the VOS |
| CVE-2026-107241 | 7.6 | 2026-11-10 | The Node.js web service on VOS (previously Versa FlexVNF) is used for URL-based Zero Touch Provisioning (ZTP) of the VOS |
| CVE-2026-107243 | 7.6 | 2026-11-10 | The Node.js web service on VOS (previously Versa FlexVNF) is used for URL-based Zero Touch Provisioning (ZTP) of the VOS |
| CVE-2026-107244 | 7.6 | 2026-11-10 | The Node.js web service on VOS (previously Versa FlexVNF) is used for URL-based Zero Touch Provisioning (ZTP) of the VOS |
| CVE-2026-109793 | 7.5 | 2026-11-10 | SAP NetWeaver Application Server ABAP and SAP Web Dispatcher do not sufficiently validate certain header values processe |
| CVE-2026-109794 | 7.5 | 2026-11-10 | SAP NetWeaver Application Server ABAP, ABAP Platform, and SAP Web Dispatcher do not sufficiently handle resource consump |
| CVE-2026-109795 | 9.9 | 2026-11-10 | SAP NetWeaver does not perform necessary authorization checks and lacks sufficient input validation in certain remote-en |
| CVE-2026-109797 | 7.1 | 2026-11-10 | In SAP/astonish, an authenticated user could potentially identify and operate on another team�s sandbox containers becau |
| CVE-2026-109798 | 9.1 | 2026-11-10 | SAP BusinessObjects Business Intelligence Platform (Web Intelligence) does not properly restrict external entity resolut |
| CVE-2026-109799 | 7.5 | 2026-11-10 | The SAP Cloud SDK for Python contains an improper cryptographic signature verification vulnerability (CWE-347) in IASCon |
| CVE-2026-109800 | 7.7 | 2026-11-10 | SAP Web Dispatcher does not sufficiently validate certain inputs during processing, which could lead to memory corruptio |
| CVE-2026-109803 | 9.9 | 2026-11-10 | SAP NetWeaver Knowledge Management (XML Forms) does not sufficiently restrict the selection of XSL transformations proce |
| CVE-2026-109804 | 7.5 | 2026-11-10 | SAP Message Server does not properly handle certain malformed requests, which could be leveraged by an unauthenticated a |
| CVE-2026-109806 | 7.5 | 2026-11-10 | SAP NetWeaver (Internet Graphics Service) does not sufficiently validate certain input values within incoming requests.  |
| CVE-2026-109807 | 7.5 | 2026-11-10 | SAP NetWeaver (Internet Graphics Service) does not sufficiently validate certain input values within incoming requests.  |
| CVE-2026-120008 | 8.2 | 2026-11-10 | SAP NetWeaver (Internet Graphics Service) does not sufficiently validate certain input values within incoming requests.  |
| CVE-2026-120009 | 7.2 | 2026-11-10 | SAP ABAP Developer Tools (AMDP Data Preview) does not perform sufficient validation and authorization checks within cert |
| CVE-2026-120010 | 7.5 | 2026-11-10 | SAP NetWeaver Application Server (SAP Message Server) does not properly size memory allocations when handling certain HT |
| CVE-2026-120014 | 7.6 | 2026-11-10 | SAP HANA XSA Web Dispatcher does not perform sufficient request validation in certain administrative functionality. In t |
| CVE-2026-120015 | 7.5 | 2026-11-10 | SAP Host Agent does not sufficiently validate certain inputs. Under certain condition, an attacker with low privileges c |
| CVE-2026-120017 | 10.0 | 2026-11-10 | SAP NetWeaver AS ABAP and ABAP Platform does not perform sufficient verification of incoming authentication assertions u |
| CVE-2026-124598 | 7.5 | 2026-11-10 | An
API key is hardcoded and retrievable from the GV-Face package. Since
Android applications can be reverse engineered,  |
| CVE-2026-125086 | 10.0 | 2026-11-10 | A vulnerability has been found in D-Link M60 1.12.B01. Impacted is the function system of the file /etc/emDaemon/mosquit |
| CVE-2026-125087 | 7.3 | 2026-11-10 | A vulnerability was found in Michael-A-Kuykendall Shimmy up to 2.6.4. The affected element is an unknown function of the |
| CVE-2026-76964 | 10.0 | 2026-11-10 | SAP NetWeaver Application Server ABAP does not sufficiently validate certain network input processed by an internal comp |
| CVE-2026-76965 | 9.9 | 2026-11-10 | SAP NetWeaver Application Server ABAP and ABAP Platform does not perform necessary authorization checks for certain inte |
| CVE-2026-76966 | 8.9 | 2026-11-10 | Due to improper RFC protocol validation in the SAP Kernel used by the Application Server ABAP of SAP NetWeaver and ABAP  |
| CVE-2026-76970 | 7.5 | 2026-11-10 | Due to a Memory Corruption vulnerability in Application Server ABAP for SAP NetWeaver and ABAP Platform, an unauthentica |
| CVE-2026-76973 | 7.5 | 2026-11-10 | Due to a Memory Corruption vulnerability in Application Server ABAP of SAP NetWeaver and ABAP Platform, an unauthenticat |
| CVE-2026-89103 | 10.0 | 2026-11-10 | SAP Gateway activates the default Access Control List with high privileges allowing categorization of external attacker  |
| CVE-2026-89114 | 7.5 | 2026-11-10 | SAP NetWeaver AS Java EDM Application does not perform an authentication check for certain web service requests. An unau |
| CVE-2026-89119 | 9.6 | 2026-11-10 | SAP Web Dispatcher and SAP NetWeaver Application Server ABAP (Internet Communication Manager) do not perform sufficient  |
| CVE-2026-89126 | 10.0 | 2026-11-10 | SAP Web Dispatcher does not sufficiently validate certain network input processed by an internal component. An unauthent |
| CVE-2026-125612 | 8.8 | 2026-11-10 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Deltaww DIAEnergie |
| CVE-2026-112125 | 7.3 | 2026-11-10 | Incorrect Permission Assignment for Critical Resource Vulnerability in HA Monitor.

This issue affects HA Monitor: from  |
| CVE-2026-115646 | 9.8 | 2026-11-10 | Partial String Comparison Vulnerability in HiRDB.


This issue affects HiRDB Server Version 10: from 10-00 before 10-12- |
| CVE-2026-86578 | 7.3 | 2026-11-10 | Link Following Vulnerability in Hitachi Dynamic Link Manager for Windows.

This issue affects Hitachi Dynamic Link Manag |
| CVE-2026-86579 | 8.2 | 2026-11-10 | Binary Planting Vulnerability in Hitachi Dynamic Link Manager for Windows.

This issue affects Hitachi Dynamic Link Mana |
| CVE-2026-91754 | 8.1 | 2026-11-10 | Stack-based Buffer Overflow Vulnerability in Hitachi Dynamic Link Manager for VMware.

This issue affects Hitachi Dynami |
| CVE-2026-91755 | 8.1 | 2026-11-10 | Integer Overflow Vulnerability in Hitachi Dynamic Link Manager for VMware.

This issue affects Hitachi Dynamic Link Mana |
| CVE-2026-91756 | 8.1 | 2026-11-10 | OS Command Injection Vulnerability in Hitachi Dynamic Link Manager for VMware.

This issue affects Hitachi Dynamic Link  |
| CVE-2026-91757 | 7.1 | 2026-11-10 | OS Command Injection Vulnerability in Hitachi Dynamic Link Manager for VMware.

This issue affects Hitachi Dynamic Link  |
| CVE-2026-91758 | 7.8 | 2026-11-10 | Out-of-bounds Read and Write Vulnerability in Hitachi Dynamic Link Manager for Linux.

This issue affects Hitachi Dynami |
| CVE-2026-91759 | 7.8 | 2026-11-10 | Out-of-Bounds Write Vulnerability in Hitachi Dynamic Link Manager for Linux.


This issue affects Hitachi Dynamic Link M |
| CVE-2026-91760 | 7.0 | 2026-11-10 | Heap-based Buffer Overflow Vulnerability in Hitachi Dynamic Link Manager for Linux.


This issue affects Hitachi Dynamic |
| CVE-2026-91761 | 8.2 | 2026-11-10 | UNIX Symbolic Link (Symlink) Following Vulnerability in Hitachi Dynamic Link Manager for Linux.

This issue affects Hita |
| CVE-2026-91762 | 7.9 | 2026-11-10 | UNIX Symbolic Link (Symlink) Following Vulnerability in Hitachi Dynamic Link Manager for Linux.


This issue affects Hit |
| CVE-2026-91763 | 8.2 | 2026-11-10 | UNIX Symbolic Link (Symlink) Following Vulnerability in Hitachi Dynamic Link Manager for Linux.
This issue affects Hitac |
| CVE-2026-91764 | 8.1 | 2026-11-10 | Improper Link Resolution Before File Access Vulnerability in Hitachi Dynamic Link Manager for Linux.


This issue affect |
| CVE-2026-92863 | 7.0 | 2026-11-10 | Integer Overflow Vulnerability in Hitachi Dynamic Link Manager for AIX (for the Japanese market).

This issue affects Hi |
| CVE-2026-92864 | 7.3 | 2026-11-10 | Insecure Temporary File Vulnerability in Hitachi Dynamic Link Manager for AIX (for markets outside Japan) and Hitachi Dy |
| CVE-2026-12389 | 8.4 | 2026-11-10 | A vulnerability that could lead to a high privileged authenticated user performing a remote code execution attack. |
| CVE-2026-12963 | 7.4 | 2026-11-10 | A vulnerability that could allow a viewer account to gain unauthorized access to network attached storage devices on the |
| CVE-2026-12964 | 8.0 | 2026-11-10 | A vulnerability allowing for privileged escalation of the viewer account to gain administrator privileges. |
| CVE-2026-13312 | 9.9 | 2026-11-10 | A vulnerability that could allow an attacker to compromise a system. |
| CVE-2026-4762 | 8.8 | 2026-11-10 | A vulnerability to perform a privilege escalation attack on the server as a non-admin user. |
| CVE-2026-63288 | 8.3 | 2026-11-10 | A WebSocket request sent to a specific API endpoint allows unauthorized access to a separate API endpoint. This bypasses |
| CVE-2026-8372 | 8.8 | 2026-11-10 | A vulnerability that could allow an attacker to gain unauthorized access. |
| CVE-2026-100386 | 7.5 | 2026-11-10 | The Ultra Addons for Contact Form 7 plugin for WordPress is vulnerable to Directory Traversal in all versions up to, and |
| CVE-2026-120513 | 8.2 | 2026-11-10 | The Everest Forms – Contact Form, Payment Form, Quiz, Survey & Custom Form Builder with AI plugin for WordPress is vulne |
| CVE-2026-76877 | 8.1 | 2026-11-10 | The WPML Multilingual CMS plugin for WordPress is vulnerable to Authentication Bypass via Race Condition in versions up  |
| CVE-2026-84938 | 7.2 | 2026-11-10 | The Avada (Fusion) Builder plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Form Notification Dynam |
| CVE-2026-93427 | 7.2 | 2026-11-10 | The ARMember Premium – Membership Plugin, Content Restriction, Member Levels, User Profile & User signup plugin for Word |
| CVE-2026-120012 | 7.5 | 2026-11-10 | SAP Cloud SDK for AI (Node.js) could inadvertently include sensitive authentication credentials in error messages genera |
| CVE-2026-120013 | 7.5 | 2026-11-10 | The agent_memory module accepts a caller-supplied tenant parameter in create_client(tenant=...). Prior to version 0.50.0 |
| CVE-2026-60035 | 7.2 | 2026-11-10 | A high privileged remote attacker can perform a code injection in the backends network auth function leading to code exe |
| CVE-2026-60036 | 7.2 | 2026-11-10 | A high privileged remote attacker can perform a code injection in the backends patch activate function leading to code e |
| CVE-2026-60037 | 7.2 | 2026-11-10 | A high privileged remote attacker can perform an OpenSSL code injection in the frontends device importer function leadin |
| CVE-2026-60038 | 7.2 | 2026-11-10 | A high privileged remote attacker can perform an OpenSSL code injection in the backends ImportPKCS12 function leading to |
| CVE-2026-60039 | 7.2 | 2026-11-10 | A high privileged remote attacker can perform a code injection in the backends backup restore function leading to code e |
| CVE-2026-60040 | 7.5 | 2026-11-10 | An unauthenticated remote attacker can perform a DoS in the backends backup creation function. This can result in a tota |
| CVE-2026-60041 | 8.1 | 2026-11-10 | An unauthenticated remote attacker can perform a CSRF attack on a logged in backend user allowing for execution of multi |
| CVE-2026-60043 | 9.3 | 2026-11-10 | An unauthenticated remote attacker can perform a XSS attack on a logged in backend user allowing for execution of multip |
| CVE-2026-60044 | 7.5 | 2026-11-10 | The backups created by the application use a weak static password allowing an unauthenticated remote attacker to access  |
| CVE-2026-60046 | 7.5 | 2026-11-10 | An unauthenticated remote attacker can perform password resets for any user with known username and email without rate l |
| CVE-2026-104619 | 7.8 | 2026-11-10 | Untrusted users could roll back security updates when using the PackageKit Zypp Backend before 1.4.1, allowing privilege |
| CVE-2026-125704 | 7.5 | 2026-11-10 | A use-after-free flaw was found in GStreamer core buffer value deserialization. When serialized buffer text contains an  |
| CVE-2026-95646 | 8.0 | 2026-11-10 | Zoho Corporation ManageEngine DDI Central versions 6500 and below are vulnerable to a Unicode-based command injection vu |
| CVE-2026-95651 | 7.5 | 2026-11-10 | Zoho Corporation ManageEngine DDI Central versions 6500 and below are vulnerable to an unauthenticated GSS-TSIG keytab u |
| CVE-2026-109097 | 8.2 | 2026-11-10 | A vulnerability has been identified in ROS# (All versions < V2.3.1). Affected systems do not properly escape text of mes |
| CVE-2026-109830 | 7.3 | 2026-11-10 | A vulnerability has been identified in meta-iot2050 (All versions >= V01.03.01). Affected devices take parts from a conf |
| CVE-2026-112136 | 8.8 | 2026-11-10 | A vulnerability has been identified in Mendix Studio Pro 11 (All versions >= V11.15.0 < V11.16.0), Mendix Studio Pro 11. |
| CVE-2026-125712 | 7.5 | 2026-11-10 | A flaw was found in GStreamer's gst-plugins-base RTCP SDES packet parser. A remote sender able to reach an active media  |
| CVE-2026-125742 | 7.8 | 2026-11-10 | 7-Zip before 26.06 contains a heap out-of-bounds write vulnerability in the LZX decoder that lets attackers corrupt memo |
| CVE-2026-12266 | 7.6 | 2026-11-10 | Zoho Corporation ManageEngine DDI Central versions 6200 and below are vulnerable to LDAP bind password exposure through  |
| CVE-2026-12572 | 7.2 | 2026-11-10 | Zoho Corporation ManageEngine DDI Central version below 6201 is vulnerable to SQL injection in HA replication username h |
| CVE-2026-12573 | 8.8 | 2026-11-10 | Zoho Corporation ManageEngine DDI Central versions 6200 and below are vulnerable to Cisco IOS command injection via DHCP |
| CVE-2026-12574 | 8.1 | 2026-11-10 | Zoho Corporation ManageEngine DDI Central versions 6200 and below are vulnerable to Server-side HTML/JavaScript injectio |
| CVE-2026-58114 | 7.5 | 2026-11-10 | A vulnerability has been identified in SIMATIC BATCH V9.1 (All versions), SIMATIC Information Server 2020 (All versions) |
| CVE-2026-59082 | 7.8 | 2026-11-10 | A vulnerability has been identified in SIMATIC WinCC V7.5 (All versions), SIMATIC WinCC V8.0 (All versions), SIMATIC Win |
| CVE-2026-121267 | 7.8 | 2026-11-10 | Incorrect default permissions vulnerability in TÜBİTAK BİLGEM Software Technologies Research Institute eta-remote allows |
| CVE-2026-124747 | 7.5 | 2026-11-10 | A flaw was found in BusyBox. When resuming a download over File Transfer Protocol (FTP), the wget utility fails to verif |
| CVE-2026-16478 | 7.0 | 2026-11-10 | Permissive list of allowed inputs vulnerability in TÜBİTAK BİLGEM Software Technologies Research Institute pardus-nvidia |
| CVE-2026-120399 | 7.5 | 2026-11-10 | A flaw was found in flightctl. A TLS handshake is performed synchronously in the HTTP server’s connection-context callba |
| CVE-2026-124852 | 8.8 | 2026-11-10 | Incorrect boundary conditions in the Graphics: CanvasWebGL component. This vulnerability was fixed in Firefox 160. |
| CVE-2026-124853 | 9.6 | 2026-11-10 | Sandbox escape due to incorrect boundary conditions in the Graphics: Text component. This vulnerability was fixed in Fir |
| CVE-2026-124856 | 8.8 | 2026-11-10 | Incorrect boundary conditions in the Networking: HTTP component. This vulnerability was fixed in Firefox 160 and Firefox |
| CVE-2026-124857 | 8.8 | 2026-11-10 | Use-after-free in the Graphics: Canvas2D component. This vulnerability was fixed in Firefox 160, Firefox ESR 115.45, and |
| CVE-2026-124858 | 8.8 | 2026-11-10 | Use-after-free in the DOM: HTML Parser component. This vulnerability was fixed in Firefox 160, Firefox ESR 115.45, and F |
| CVE-2026-124859 | 9.6 | 2026-11-10 | Sandbox escape due to incorrect boundary conditions in the Storage: Cache API component. This vulnerability was fixed in |
| CVE-2026-124860 | 8.8 | 2026-11-10 | Use-after-free in the Audio/Video component. This vulnerability was fixed in Firefox 160, Firefox ESR 115.45, and Firefo |
| CVE-2026-124861 | 9.6 | 2026-11-10 | Sandbox escape due to use-after-free in the Audio/Video: cubeb component. This vulnerability was fixed in Firefox 160, F |
| CVE-2026-124862 | 8.8 | 2026-11-10 | Use-after-free in the DOM: Core & HTML component. This vulnerability was fixed in Firefox 160 and Firefox ESR 153.7. |
| CVE-2026-124863 | 8.8 | 2026-11-10 | Use-after-free in the DOM: HTML Parser component. This vulnerability was fixed in Firefox 160, Firefox ESR 115.45, and F |
| CVE-2026-124864 | 9.6 | 2026-11-10 | Sandbox escape due to use-after-free in the DOM: Service Workers component. This vulnerability was fixed in Firefox 160, |
| CVE-2026-124865 | 8.8 | 2026-11-10 | Use-after-free in the Audio/Video component. This vulnerability was fixed in Firefox 160, Firefox ESR 115.45, and Firefo |
| CVE-2026-124866 | 8.8 | 2026-11-10 | Use-after-free in the Layout component. This vulnerability was fixed in Firefox 160 and Firefox ESR 153.7. |
| CVE-2026-124867 | 8.8 | 2026-11-10 | Use-after-free in the DOM: Editor component. This vulnerability was fixed in Firefox 160. |
| CVE-2026-124868 | 8.8 | 2026-11-10 | Incorrect boundary conditions in the DOM: Core & HTML component. This vulnerability was fixed in Firefox 160 and Firefox |
| CVE-2026-124869 | 8.8 | 2026-11-10 | Use-after-free in the DOM: Core & HTML component. This vulnerability was fixed in Firefox 160 and Firefox ESR 153.7. |
| CVE-2026-124870 | 8.8 | 2026-11-10 | Incorrect boundary conditions in the JavaScript: GC component. This vulnerability was fixed in Firefox 160 and Firefox E |
| CVE-2026-124871 | 8.8 | 2026-11-10 | Use-after-free in the DOM: HTML Parser component. This vulnerability was fixed in Firefox 160. |
| CVE-2026-124872 | 8.8 | 2026-11-10 | Use-after-free in the Cycle Collector component. This vulnerability was fixed in Firefox 160, Firefox ESR 115.45, and Fi |
| CVE-2026-124875 | 8.8 | 2026-11-10 | Incorrect boundary conditions in the DOM: CSS Object Model component. This vulnerability was fixed in Firefox 160, Firef |
| CVE-2026-124876 | 8.8 | 2026-11-10 | Use-after-free in the CSS Parsing and Computation component. This vulnerability was fixed in Firefox 160, Firefox ESR 11 |
| CVE-2026-124877 | 8.8 | 2026-11-10 | Use-after-free in the Layout: Positioned component. This vulnerability was fixed in Firefox 160, Firefox ESR 115.45, and |
| CVE-2026-124878 | 8.8 | 2026-11-10 | Use-after-free in the Layout: Positioned component. This vulnerability was fixed in Firefox 160. |
| CVE-2026-124880 | 8.8 | 2026-11-10 | Use-after-free in the DOM: Core & HTML component. This vulnerability was fixed in Firefox 160, Firefox ESR 115.45, and F |
| CVE-2026-124881 | 8.8 | 2026-11-10 | Use-after-free in the CSS Parsing and Computation component. This vulnerability was fixed in Firefox 160, Firefox ESR 11 |
| CVE-2026-124882 | 8.8 | 2026-11-10 | Use-after-free in the CSS Parsing and Computation component. This vulnerability was fixed in Firefox 160, Firefox ESR 11 |
| CVE-2026-124883 | 8.8 | 2026-11-10 | Use-after-free in the DOM: Core & HTML component. This vulnerability was fixed in Firefox 160 and Firefox ESR 153.7. |
| CVE-2026-124884 | 8.8 | 2026-11-10 | Use-after-free in the JavaScript: GC component. This vulnerability was fixed in Firefox 160 and Firefox ESR 153.7. |
| CVE-2026-124885 | 8.8 | 2026-11-10 | Use-after-free in the Graphics: Text component. This vulnerability was fixed in Firefox 160, Firefox ESR 115.45, and Fir |
| CVE-2026-124887 | 8.8 | 2026-11-10 | Incorrect boundary conditions in the Layout: Text and Fonts component. This vulnerability was fixed in Firefox 160 and F |
| CVE-2026-124888 | 8.8 | 2026-11-10 | Incorrect boundary conditions in the Layout: Text and Fonts component. This vulnerability was fixed in Firefox 160 and F |
| CVE-2026-124889 | 8.8 | 2026-11-10 | Use-after-free in the CSS Parsing and Computation component. This vulnerability was fixed in Firefox 160 and Firefox ESR |
| CVE-2026-124890 | 8.8 | 2026-11-10 | Use-after-free in the DOM: Core & HTML component. This vulnerability was fixed in Firefox 160, Firefox ESR 115.45, and F |
| CVE-2026-124891 | 8.8 | 2026-11-10 | Incorrect boundary conditions in the DOM: Selection component. This vulnerability was fixed in Firefox 160 and Firefox E |
| CVE-2026-124892 | 8.8 | 2026-11-10 | Use-after-free in the JavaScript: GC component. This vulnerability was fixed in Firefox 160 and Firefox ESR 153.7. |
| CVE-2026-124893 | 8.8 | 2026-11-10 | Use-after-free in the DOM: Workers component. This vulnerability was fixed in Firefox 160 and Firefox ESR 153.7. |
| CVE-2026-124894 | 8.8 | 2026-11-10 | Use-after-free in the Networking: Cookies component. This vulnerability was fixed in Firefox 160 and Firefox ESR 153.7. |
| CVE-2026-124895 | 8.8 | 2026-11-10 | Use-after-free in the Storage: localStorage & sessionStorage component. This vulnerability was fixed in Firefox 160, Fir |
| CVE-2026-124897 | 8.8 | 2026-11-10 | Use-after-free in the JavaScript: GC component. This vulnerability was fixed in Firefox 160 and Firefox ESR 153.7. |
| CVE-2026-124898 | 8.8 | 2026-11-10 | Use-after-free in the DOM: Editor component. This vulnerability was fixed in Firefox 160, Firefox ESR 115.45, and Firefo |
| CVE-2026-124899 | 8.8 | 2026-11-10 | Use-after-free in the Layout: Text and Fonts component. This vulnerability was fixed in Firefox 160, Firefox ESR 115.45, |
| CVE-2026-124900 | 9.6 | 2026-11-10 | Sandbox escape due to use-after-free in the DOM: Service Workers component. This vulnerability was fixed in Firefox 160. |
| CVE-2026-124903 | 9.6 | 2026-11-10 | Sandbox escape due to use-after-free in the IPC component. This vulnerability was fixed in Firefox 160, Firefox ESR 115. |
| CVE-2026-124904 | 8.8 | 2026-11-10 | Use-after-free in the SVG component. This vulnerability was fixed in Firefox 160. |
| CVE-2026-124906 | 8.8 | 2026-11-10 | Use-after-free in the Graphics: WebRender component. This vulnerability was fixed in Firefox 160 and Firefox ESR 153.7. |
| CVE-2026-124907 | 8.8 | 2026-11-10 | Privilege escalation, sandbox escape due to use-after-free in the Graphics: CanvasWebGL component. This vulnerability wa |
| CVE-2026-124908 | 8.8 | 2026-11-10 | Use-after-free in the CSS Parsing and Computation component. This vulnerability was fixed in Firefox 160. |
| CVE-2026-124915 | 8.8 | 2026-11-10 | Incorrect boundary conditions in the Graphics: WebGPU component. This vulnerability was fixed in Firefox 160 and Firefox |
| CVE-2026-124917 | 9.6 | 2026-11-10 | Sandbox escape due to use-after-free in the Widget: Gtk component. This vulnerability was fixed in Firefox 160 and Firef |
| CVE-2026-124918 | 8.8 | 2026-11-10 | Privilege escalation due to incorrect boundary conditions in the Graphics: WebRender component. This vulnerability was f |
| CVE-2026-124919 | 8.8 | 2026-11-10 | Privilege escalation due to use-after-free in the WebRTC: Networking component. This vulnerability was fixed in Firefox  |
| CVE-2026-124922 | 8.8 | 2026-11-10 | Use-after-free in the CSS Transitions and Animations component. This vulnerability was fixed in Firefox 160 and Firefox  |
| CVE-2026-124924 | 8.8 | 2026-11-10 | Incorrect boundary conditions in the Graphics: WebRender component. This vulnerability was fixed in Firefox 160 and Fire |
| CVE-2026-124926 | 8.8 | 2026-11-10 | Incorrect boundary conditions in the WebRTC component. This vulnerability was fixed in Firefox 160 and Firefox ESR 153.7 |
| CVE-2026-124932 | 8.8 | 2026-11-10 | Use-after-free in the Graphics component. This vulnerability was fixed in Firefox 160 and Firefox ESR 153.7. |
| CVE-2026-124943 | 8.8 | 2026-11-10 | Use-after-free in the Layout component. This vulnerability was fixed in Firefox 160. |
| CVE-2026-124947 | 8.8 | 2026-11-10 | Incorrect boundary conditions in the Graphics component. This vulnerability was fixed in Firefox 160. |
| CVE-2026-124948 | 8.8 | 2026-11-10 | Incorrect boundary conditions, use-after-free in the Graphics component. This vulnerability was fixed in Firefox 160 and |
| CVE-2026-124952 | 8.8 | 2026-11-10 | Use-after-free in the Audio/Video component. This vulnerability was fixed in Firefox ESR 115.45. |
| CVE-2026-82509 | 7.4 | 2026-11-10 | V programming language standard library net.http through version 0.5.2 prior to commit 4077484 contains a TLS certificat |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-102895 | GPUStack / GPUStack | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-123158 | OpenBSD / OpenSSH | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-116779 | SignalWire / FreeSwitch | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-123218 | IBM / Aspera Faspex | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-19868 | SonicWall / SonicOS SSLVPN | 2026-11-06 | 2026-11-20 | Unknown |
| CVE-2024-27834 | Apple / Multiple Products | 2026-11-04 | 2026-11-18 | Unknown |
| CVE-2026-119977 | WordPress / WordPress Core | 2026-11-03 | 2026-11-06 | Unknown |

---

*Total entries in CISA KEV catalog: 1773*