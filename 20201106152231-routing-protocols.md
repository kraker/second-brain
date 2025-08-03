---
title: Routing Protocol
date: 2020-11-06 15:22:31
---

## Dynamic Routing Protocols

| *Protocol* | *Type*          | *IGP or BGP?* | *Notes*                                        |
|------------|-----------------|---------------|------------------------------------------------|
| RIPv1      | Distance vector | IGP           | Old; only used variable subnets within an AS   |
| RIPv2      | Distance vector | IGP           | Supports VLSM and discontiguous subnets        |
| BGP        | Path vector     | BGP           | Used on the Internet, connects AS'             |
| OSPF       | Link State      | IGP           | Fast, popular, uses ARea IDs (Area 0/backbone) |
| IS-IS      | Link state      | IGP           | Alternative to OSPF                            |
| EIGRP      | Hybrid          | IGP           | Cisco proprietary                              |

## Distance Vector

Compares cost of all routes to a particular network ID and chooses the lowest cost.

### RIPv1

See also: [Routing Information Protocol](20210627064814-routing-information-protocol.md) (RIP)

Maximum hop count of 15. Sends routing tables every 30 seconds. Doesn't know how to use variable-length subnet masking (VLSM). Open to attack, no authentication.

### RIPv2

Same as RIPv1 except VLSM and authentication has been added. Only suitable for small private networks. Time to convergence still too long for WANs.

## Path Vector

### BGP

Border Gateway Protocol (BGP)
Current version is BGP-4

* Multitiered structure and at the top sit many Autonomous Systems (AS).
* Each AS is governed by a single dynamic routing protocol.
* AS' deliver data to each other using an Autonomous System Number (ASN) assigned by the IANA.
  + ASNs are 32 bit numbers displayed as 2 16-bit numbers separated by a dot. 1.33457

#### EGP

 communicate with each other using a protocol called the Exterior Gateway Protocol (EGP).
e internet has settled on BGP as the EGP.

#### [Interior gateway protocol](20210626131223-interior-gateway-protocol.md) (IGP)

tworsk with an AS communicate with each other using Interior Gateway Protocols (IGPs).

## Link State

See also:
* [Link-state routing protocol](20210626130850-link-state-routing-protocol.md)
 
### [Open Shortest Path First](20210626073338-open-shortest-path-first.md) (OSPF)

* Most commonly used IGP in the world
* Converges faster and much more efficient than RIP
* Two adjacent routers form a *neighborship* through Hello packets
* Exchange information about routers through *link state advertisement (LSA)* packets.
* OSPF's metric is *cost*, which is a function of bandwidth. Chooses lowest cost.
* Shortest path first, by definition, prevents loops.

### IS-IS

Intermediate System to Intermediate System
Very similar to OSPF, but added advantage that IPv6 was baked in from the start. This is the *de afcto* standard for ISPs.

## EIGRP

Enhanced Interior Gateway Routing Protocol

* Shares aspects of both distance vector and link state protocols.
* Invented by Cisco
* Called an *advanced distance vector protocol*.
