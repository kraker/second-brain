---
title: Bridge Protocol Data Unit
date: 2021-06-11T06:35:00Z
---

**Bridge Protocol Data Units** (BPDUs) are [frames](20201009144356-frame.md) 
that contain information about the 
[spanning tree protocol](20201016141336-spanning-tree-protocol.md) (STP). 
A switch sends BPDUs using a unique source [MAC Address](20201009143255-mac.md) 
from its origin port to a [multicast address](20210611064541-multicast-address.md) with destination MAC
(01:80:C2:00:00:00,[1] or 01:00:0C:CC:CC:CD for Cisco proprietary Per VLAN
Spanning Tree). 

There are two kinds of BPDUs for 802.1D Spanning Tree:
* Configuration BPDU, sent by root bridges to provide information to all switches.
* TCN (Topology Change Notification), sent by bridges towards the root bridge to notify changes in the topology, such as port up or port down.

By default the BPDUs are sent every 2 seconds. 

Source: https://en.wikipedia.org/wiki/Bridge_Protocol_Data_Unit

