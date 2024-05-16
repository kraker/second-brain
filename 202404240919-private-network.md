---
title: Private network
date: 2024-04-24 09:19
tags:
- 'networking'
---

# Private network

Computer network that uses the private address space of IP addresses.

## Private IPv4 Addresses

| RFC 1918 name | IP address range              | Number of addresses | Largest [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing "Classless Inter-Domain Routing") block (subnet mask) | Host ID size | Mask bits | _[Classful](https://en.wikipedia.org/wiki/Classful_network "Classful network")_ description[[Note 1]](https://en.wikipedia.org/wiki/Private_network#cite_note-4) |
| ------------- | ----------------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 24-bit block  | 10.0.0.0 – 10.255.255.255     | 16777216            | 10.0.0.0/8 (255.0.0.0)                                                                                                            | 24 bits      | 8 bits    | single class A network                                                                                                                                           |
| 20-bit block  | 172.16.0.0 – 172.31.255.255   | 1048576             | 172.16.0.0/12 (255.240.0.0)                                                                                                       | 20 bits      | 12 bits   | 16 contiguous class B networks                                                                                                                                   |
| 16-bit block  | 192.168.0.0 – 192.168.255.255 | 65536               | 192.168.0.0/16 (255.255.0.0)                                                                                                      | 16 bits      | 16 bits   | 256 contiguous class C networks                                                                                                                                  |
_All other IP addresses are public IP addresses_

Source: [Wikipedia - Private network](https://en.wikipedia.org/wiki/Private_network)