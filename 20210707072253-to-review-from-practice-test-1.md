---
title: To Review from Practice Test 1
date: 2021-07-07T07:22:00Z
---

* Network problems:
	+ [Initialization vector](20210716104627-initialization-vector.md) attack
	+ [Replay attack](20210717110020-replay-attack.md) 
	+ Virus infection:
		- What's the best tool to use if virus is suspected of infecting network and
			using large amounts of bw?
			- Network sniffer
			- [Packet analyzer](20210717114150-packet-analyzer.md)
* Network hardening:
	+ Avoid using privileged accounts
	+ Track hardware and software for patch reqs
	+ Keep account roles separated to avoid conflicts of interest
	+ It's ok to save certs, pw's, and keys in the same protected vault
	+ Review incident preparation and management
		- Preparation for incidents is a multifaceted process that includes which
			tasks?
			- Vulnerability scanning
			- Penetration testing
* Review how TCP closes connections
	+ Sends _FIN_ 
* Security:
	+ Review smurf attack
	+ Encryption:
		- Review asymmetric encryption
			- What are two examples of asymmetric encryption?
				- Elliptic Curve Cryptography
				- Rivest-Shamir-Adleman
* Wireless:
	+ WPS is used for what purpose?
		- Automatically configures a wireless device to connect to a WAP
* Ethernet standards:
	+ Review what the letters mean at the end of the designation:
		- 10GBaseSW: _S_ stands for _short-range_ and _W_ stands for _WAN_
		- 10GBaseSR: _S_ stands for _short-range_ and _R_ means it works with
			existing Ethernet standards.
		- Does _L_ stand for _long-range_?	
	+ 1000BaseSX:
		- supports runs of up to 500 m over MMF.
		- Doesn't support 10km runs.
		- Remember _S_ stands for _short-range_
	+ 1000BaseLX:
		- Runs MMF and has maximum length of 550 meters
	+ What networking technology is also known as _Fast Ethernet_?
		- 100Base_XY_
		- Anything with _100_ in it is good for _Fast Ethernet_
	+ Gigabit Ethernet standards
		- 1000Base-CX
			- uses copper cabling and is limited to 25 meters
* Port forwarding _allows_ outside access to hosts on the LAN side of the NAT
	router.
* Fiber-optic:
	+ Review multi-modal distortion
* Protocol analyzers:
	+ Wireshark:
		- Protocol analyzers _can't_ generate packets and frames. Can only capture
			and display them. 

_Up to here reviewed_
* IP
	+ Routing:
		- Subnetting:
			- Subnet masks are never sent out of a host, they're not part of the IP
				header.
			- Review subnet masks
	+ Review IPv6
* Cabling
	+ Coaxial
		- RG-58 impedence: 50 ohms
		- RG-8 impedence: 50 ohms
* SNMP
	+ Get, Response, Set, and Trap are communications that occur between an SNMP
		manager and an SNMP managed device. These communications are examples of
		what?
		- PDU's
		- The commands and responses passed between SNMP managers and devices are
			sent as protocol data units (PDU).
		- Review SNMP
		- Review PDU
* Review HA
	+ Common techniques to acheive HA are?
		- Install RAID
		- Redundant Systems
		- Aggregate links
