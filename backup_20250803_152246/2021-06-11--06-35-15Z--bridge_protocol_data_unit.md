---
title: Bridge Protocol Data Unit
date: 2021-06-11 06:35
---

**Bridge Protocol Data Units** (BPDUs) are [frames](2020-10-09--14-43-56Z--frame.md) 
that contain information about the 
[spanning tree protocol](2020-10-16--14-13-36Z--spanning_tree_protocol.md) (STP). 
A switch sends BPDUs using a unique source [MAC Address](2020-10-09--14-32-55Z--mac.md) 
from its origin port to a [multicast address](2021-06-11--06-45-41Z--multicast_address.md) with destination MAC
(01:80:C2:00:00:00,[1] or 01:00:0C:CC:CC:CD for Cisco proprietary Per VLAN
Spanning Tree). 

There are two kinds of BPDUs for 802.1D Spanning Tree:
* Configuration BPDU, sent by root bridges to provide information to all switches.
* TCN (Topology Change Notification), sent by bridges towards the root bridge to notify changes in the topology, such as port up or port down.

By default the BPDUs are sent every 2 seconds. 

Source: https://en.wikipedia.org/wiki/Bridge_Protocol_Data_Unit

