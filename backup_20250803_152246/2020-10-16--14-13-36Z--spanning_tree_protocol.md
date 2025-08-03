---
title: Spanning Tree Protocol 
date: 2020-10-16 14:13:36
---

**Spanning Tree Protocol (STP)**

Because you can connect switches together in any fashion you can create
redundant connections called *bridging loops* or *switching loops*.

* In the early days of switches a [frame](2020-10-09--14-43-56Z--frame.md)
  could get caught in a loop and bring the network down.
* STP uses special [frames](2020-10-09--14-43-56Z--frame.md) called BPDUs to
  communicate with other switches
  + **BPDU:** Bridge Protocol Data Unit
* Configuration BPDUs elect one switch as *root bridge* to act as center of
  STP.
* There can be redundant links for fault tolerance but certain ports will be
  placed in a *blocking* state and will not send/receive frames.
* If a link or device goes down a special BPDU called a TCN will be sent out
  allowing *blocking* ports to move to a forward state if they're needed.
  + **TCN:** Topology Change Notification
* RSTP is currently in use, STP was retired in 2001.
  + **RSTP:** Rapid Spanning Tree Protocol
  + Allows rapid convergence time following some kind of network change.
