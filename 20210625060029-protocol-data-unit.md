---
title: Protocol data unit
date: 2021-06-25T06:00:00Z
tags:
- 'networking'
---

In [telecommunications](20210625060256-telecommunications.md), a 
**protocol data unit (PDU)** is a single unit of information transmitted among
peer entities of a [computer network](20210610054021-computer-network.md). 
A PDU is composed of protocol-specific control information and 
[user data](20210625060529-payload-computing.md). In the layered
architectures of [communication protocol](20210625060856-communication-protocol.md) 
stacks, each layer implements protocols tailored to the specific type or mode of
data exchange.

For example, the [Transmission Control Protocol](20201010181222-tcp.md) (TCP)
implements a connection-oriented transfer mode, and the PDU of this protocol is
called a _segment_, while the [User Datagram Protocol](20201011173654-udp.md) (UDP)
uses [datagrams](20210615063550-datagram.md) as protocol units for 
[connectionless communication](20210615061227-connectionless-communication.md).
A layer lower in the [Internet protocol suite](20210615061915-internet-protocol-suite.md),
at the [Internet layer](20201011171739-internet-layer.md), the PDU is
called a [packet](20201010182424-packet.md), irrespective of its payload
type.

# Backlinks

- [Networking](20201006072053-networking.md)
- [Maximum transmission unit](20210626071502-maximum-transmission-unit.md)
