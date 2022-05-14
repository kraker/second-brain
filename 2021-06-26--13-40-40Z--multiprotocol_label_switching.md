---
title: Multiprotocol Label Switching
date: 2021-06-26 13:40
---

**Multiprotocol Label Switching (MPLS)** is a routing technique in
[telecommunications networks](2021-06-26--13-42-37Z--telecommunications_network.md) 
that directs data from one [node](2021-06-26--13-44-38Z--node_networking.md) to
the next based on the short path labels rather than long network addresses, thus
avoiding complex lookups in a [routing table](2020-11-05--13-33-55Z--routing_tables.md)
and speeding traffic flows.

* Labels identify virtual links (paths) between distant nodes rather than
	endpoints. 
* Can encapsulate packets of various network protocols, hence _multiprotocol_.

In a MPLS network, data packets are assigned lables. Packet forwarding decisions
are made solely on the contents of this label, without the need to examine the
packet itself.

[Source](https://en.wikipedia.org/wiki/Multiprotocol_Label_Switching)
