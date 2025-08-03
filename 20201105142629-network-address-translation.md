---
title: Network Address Translation (NAT)
tags:
- 'networking'
---

# NAT

NAT replaces the source IP address of a device with the source IP from the outside router.

## [Port Address Translation (PAT)](20201105143031-port-address-translation-pat.md)

# [Port Forwarding](20201105143809-port-forwarding.md)

## Static NAT (SNAT)

Maps a single routable IP address (public) to a single machine on the network on a one-to-one basis.

## Dynamic NAT (DNAT)

Uses a pool of IP addresses to serve a larger number of devices on the LAN. This still needs many true routable IP addresses which can be expensive. And if more devices try to connect than are available in the IP pool, then a device won't be able to connect.

## Resources

* [CompTIA - What is NAT?](https://www.comptia.org/content/guides/what-is-network-address-translation)