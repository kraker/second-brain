---
title: VLAN Trunking Protocol
date: 2021-02-08 08:46
---
_VTP_
Used to automate the the updating of multiple
[VLAN](2021-02-06--11-07-41Z--vlan.md) switches.
* Cisco proprietary protocol
* Switches can be: server, client, transparent
	+ Changes made to the _server_ switch automatically updates _client_ switches
		connected to the network.
	+ Transparent switch hold their manual VLAN configurations and do not update
