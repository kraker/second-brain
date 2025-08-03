---
title: Link-state advertisement
date: 2021-06-26 07:32
---

The **link-state advertisement (LSA)** is a basic communication means of the 
[OSPF](20210626073338-open-shortest-path-first.md) routing protocol for
the [Internet Protocol](20201010175903-internet-protocol.md) (IP). It
communicates the router's local routing topology to all other local routers in
the same OSPF area. OSPF is designed for scalability, so some LSAs are not
flooded out on all interfaces, but only on those that belong to the appropriate
area. In this way detailed information can be kept localized, while summary
information is flooded to the rest of the network. 

Source: https://en.wikipedia.org/wiki/Link-state_advertisement
