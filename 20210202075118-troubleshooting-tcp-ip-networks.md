---
title: Troubleshooting TCP/IP Networks
date: 2021-02-02 07:51
---
1. Diagnose the NIC
	+ Use control panel if available to see if it's working
2. Check your NIC's driver. Replace if necessary
3. Diagnose locally
	+ `ping` neighboring systems by IP/domain
	+ If using [NetBIOS](20201116153053-netbios.md)
		run `net view`
4. Check IP address and subnet mask 
	+ Make sure IP address and subnet mask are entered correctly
	+ If you're on [DHCP](20201021131828-dhcp.md), try renewing the lease.
5. Run `netstat` 
	+ Checks current connects to the system
6. Run `netstat -s` or `netstat -b`
7. Diagnose the gateway
	+ `ping` the router, both local and public IPs
8. If you can't `ping` the router it's down or you're not connected.
	+ If you can only ping the near side, something in the router is messed up.
9. Diagnoste to the Internet.
	+ If you can `ping` the router, try to ping something on the Internet. 
	+ If you still can't get through, run a `tracert` or `traceroute` to try to
		diagnose where the issue is. 
