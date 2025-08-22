---
title: IP Addressing and Ethernet
date: 2020-10-22 14:33:28 
---

* Due to encapsulations, the source/dest 
	[IP addresses](20201010180322-ip-address.md) are hidden in an ethernet
	[frame](20201009144356-frame.md).
* The sending device sends out a [ARP](20201022144029-arp.md) to
	FF-FF-FF-FF-FF-FF (universal broadcast address) asking for the [](20201009143255-mac-address.md) associated with an [IP
	address](20201010180322-ip-address.md).
* Once the sending device has the MAC address for the receiving device it starts
	sending [unicast frames](20201022143832-unicast-frame.md).
* You can run `arp -a` to see OS' current ARP cache.
	+ [arp](20201022144207-arp-command.md)
