---
title: Open Shortest Path First
date: 2021-06-26T07:33:00Z
tags:
- 'networking'
---

**Open Shortest Path First (OSPF)** is a 
[routing protocol](20201106152231-routing-protocols.md) for 
[Internet Protocol](20201010175903-internet-protocol.md) (IP) networks.
It uses a 
[link-state routing](20210626130850-link-state-routing-protocol.md) (LSR)
algorithm and falls into the group of 
[interior gateway protocols](20210626131223-interior-gateway-protocol.md) (IGPs),
operating within a single 
[autonomous system](20210626131603-autonomous-system-internet.md) (AS).

* Supports the [CIDR](20201026134351-cidr.md) addressing model
* Common in large enterprise networks
* Implements [Dijkstra's algorithm](20210626132337-dijkstra's-algorithm.md), 
	also known as the shortest parth first (SPF) algorithm.
* Calculates the _shortest_ route to a destination through the network.

[Source](https://en.wikipedia.org/wiki/Open_Shortest_Path_First)
