---
title: 
date: 2020-11-07T15:38:21Z
---

# Cisco Console Cable

Typically called a *rollover or Yost cable*

## Connection settings

-   9600 baud
-   8 data bits
-   1 stop bit
-   No parity

# Cisco IOS

Internetwork Operating System (IOS)

# Console access

For Cisco routers, this is proprietary, hopefully only have to do once

# Web access

Usually some form of 192.168.x.x

# Network Management Software (NMS)

These can be used to manage routers, switches, and devices on a larger network

-   Usually a web-based interface
-   OpenNMS is a popular open source one

# Basic Router Configuration

1.  Setup WAN side
    a. If you have a static IP enter information given
    b. If not, then set to DHCP
2.  Setup LANs
    a. can be some arbitrarily chosen private range
3.  Establish Routes
    a. most routers build routing table automatically, but you can set these up manually if you wish
4.  (Optional): Configure a Dynamic Protocol
    a. If you have more than one router on the network, configure what dynamic routing protocol you're going to use
5.  Document and Back Up
    a. Once you've configured your routes document what you've done for future reference
    b. Backup the configs in the router

