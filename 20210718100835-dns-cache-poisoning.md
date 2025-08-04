---
title: DNS Cache Poisoning
date: 2021-07-18T10:08:00Z
tags: 
- 'networking'
- 'security'
---

**DNS cache poisoning** is when an attacker targets a DNS server to query a
malicious DNS server. The Malicious server can then tell the target DNS server
spoofed DNS information and the DNS server will _cache_ that spoofed
information.

The solution is to use 
[Domain Name System Security Extensions (DNSSEC)](20201202154313-dns-security-extensions.md) 
for domain name resolution.

cite: CompTIA Network+
