---
title: ARP cache poisoning
date: 2021-07-18 10:34
---

**ARP cache poisoning** is when a malicious device sends false ARP frames to
devices on a network entering it's own data into the ARP caches on those
devices. This can allow that device to perform a type of 
[Man-in-the-middle attack](2021-07-17--11-14-33Z--man-in-the-middle_attack.md)
or other types of attacks. 

## Prevention

### Dynamic ARP Inspection (DAI)

DAI is a Cisco technology that allows switches to keep track of ARP infomration
and compile a list of known good IP and MAC addresses. If an ARP poisoner
attacks the network the DAI-capable device can block those unknown ARP commands
and block them.

### DHCP Snooping

* Shares the same database as DAI
* If an unknonw MAC address starts sending DHCP server messages the DHCP
	snoop-capable device will block that device and thus stopping all unauthorized
	DHCP traffic.
