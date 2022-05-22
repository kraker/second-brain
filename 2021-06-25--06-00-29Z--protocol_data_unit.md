---
title: Protocol data unit
date: 2021-06-25 06:00
tags:
- networking
---

In [telecommunications](2021-06-25--06-02-56Z--telecommunications.md), a 
**protocol data unit (PDU)** is a single unit of information transmitted among
peer entities of a [computer network](2021-06-10--05-40-21Z--computer_network.md). 
A PDU is composed of protocol-specific control information and 
[user data](2021-06-25--06-05-29Z--payload_computing.md). In the layered
architectures of [communication protocol](2021-06-25--06-08-56Z--communication_protocol.md) 
stacks, each layer implements protocols tailored to the specific type or mode of
data exchange.

For example, the [Transmission Control Protocol](2020-10-10--18-12-22Z--tcp.md) (TCP)
implements a connection-oriented transfer mode, and the PDU of this protocol is
called a _segment_, while the [User Datagram Protocol](2020-10-11--17-36-54Z--udp.md) (UDP)
uses [datagrams](2021-06-15--06-35-50Z--datagram.md) as protocol units for 
[connectionless communication](2021-06-15--06-12-27Z--connectionless_communication.md).
A layer lower in the [Internet protocol suite](2021-06-15--06-19-15Z--internet_protocol_suite.md),
at the [Internet layer](2020-10-11--17-17-39Z--internet_layer.md), the PDU is
called a [packet](2020-10-10--18-24-24Z--packet.md), irrespective of its payload
type.

# Backlinks

- [Networking](20201006072053-networking.md)
- [Maximum transmission unit](2021-06-26--07-15-02Z--maximum_transmission_unit.md)
