---
title: Multiprotocol Label Switching
date: 2021-06-26 13:40
---

**Multiprotocol Label Switching (MPLS)** is a routing technique in
[telecommunications networks](20210626134237-telecommunications-network.md) 
that directs data from one [node](20210626134438-node-networking.md) to
the next based on the short path labels rather than long network addresses, thus
avoiding complex lookups in a [routing table](20201105133355-routing-tables.md)
and speeding traffic flows.

* Labels identify virtual links (paths) between distant nodes rather than
	endpoints. 
* Can encapsulate packets of various network protocols, hence _multiprotocol_.

In a MPLS network, data packets are assigned lables. Packet forwarding decisions
are made solely on the contents of this label, without the need to examine the
packet itself.

[Source](https://en.wikipedia.org/wiki/Multiprotocol_Label_Switching)
