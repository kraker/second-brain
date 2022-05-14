---
title: IP Addressing and Ethernet
date: 2020-10-22 14:33:28 
---

* Due to encapsulations, the source/dest 
	[IP addresses](2020-10-10--18-03-22Z--ip_address.md) are hidden in an ethernet
	[frame](2020-10-09--14-43-56Z--frame.md).
* The sending device sends out a [ARP](2020-10-22--14-40-29Z--arp.md) to
	FF-FF-FF-FF-FF-FF (universal broadcast address) asking for the [MAC
	address](2020-10-09--14-32-55Z--mac.md) associated with an [IP
	address](2020-10-10--18-03-22Z--ip_address.md).
* Once the sending device has the MAC address for the receiving device it starts
	sending [unicast frames](2020-10-22--14-38-32Z--unicast_frame.md).
* You can run `arp -a` to see OS' current ARP cache.
	+ [arp](2020-10-22--14-42-07Z--arp_command.md)
