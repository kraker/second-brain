---
title: VLAN Trunking Protocol
date: 2021-02-08T08:46:00Z
---
_VTP_
Used to automate the the updating of multiple
[VLAN](20210206110741-vlan.md) switches.
* Cisco proprietary protocol
* Switches can be: server, client, transparent
	+ Changes made to the _server_ switch automatically updates _client_ switches
		connected to the network.
	+ Transparent switch hold their manual VLAN configurations and do not update
