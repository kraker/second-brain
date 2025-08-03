---
title: Open Shortest Path First
date: 2021-06-26 07:33
tags:
- 'networking'
---

**Open Shortest Path First (OSPF)** is a 
[routing protocol](2020-11-06--15-22-31Z--routing_protocols.md) for 
[Internet Protocol](2020-10-10--17-59-03Z--internet_protocol.md) (IP) networks.
It uses a 
[link-state routing](2021-06-26--13-08-50Z--link-state_routing_protocol.md) (LSR)
algorithm and falls into the group of 
[interior gateway protocols](2021-06-26--13-12-23Z--interior_gateway_protocol.md) (IGPs),
operating within a single 
[autonomous system](2021-06-26--13-16-03Z--autonomous_system_internet.md) (AS).

* Supports the [CIDR](2020-10-26--13-43-51Z--cidr.md) addressing model
* Common in large enterprise networks
* Implements [Dijkstra's algorithm](2021-06-26--13-23-37Z--dijkstra's_algorithm.md), 
	also known as the shortest parth first (SPF) algorithm.
* Calculates the _shortest_ route to a destination through the network.

[Source](https://en.wikipedia.org/wiki/Open_Shortest_Path_First)
