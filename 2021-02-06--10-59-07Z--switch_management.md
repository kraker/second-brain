---
title: Switch Management
date: 2021-02-06 10:59
---
1. Directly plug into a serial interface and use a virtual terminal program to
	 connect to a command-line interface.
2. Get the switch on the network and then use a virtual terminal over SSH to
	 connect to the same command-line interface.
3. Get the switch on the network and use the switch's built-in Web interface.
* You configure the default gateway by telling the switch the 
	[IP Address](2020-10-10--18-03-22Z--ip_address.md) of the 
	[router](2020-10-10--18-08-51Z--router.md). 
* Common to dedicate one port on every managed device as the _management port_.
	+ _Interface configuration_ can be done only by connecting to this port.
	+ This is an example of _out-of-band management_.
* _In-band management_
	+ Well protected HTTPS/management URL
	+ Telephone modem connected to _console port_
