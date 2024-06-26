---
title: Name Resolution
date: 2021-02-02 06:15
---

## Ways to resolve a name to an IP:
* Local
	+ Can _broadcast_ for name resolution
	+ one-to-one DNS name to IP address resolution possible
* [Hosts](2020-11-16--15-37-38Z--hosts.md) file - Modern hosts automatically map hosts file to the host's _DNS resolver cache_
* DNS - Resolves an IP using DNS

## DNS Server Settings
* Windows: `ipconfig /all`
	+ DNS cache: `ipconfig /displaydns`
* Linux: `cat /etc/resolv.conf`

## Process
Starting with the local DNS server, the device resolves the name by working up
from the root domain and the respective nameservers for those names. 
