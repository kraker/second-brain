---
title: Managed Hosting FAQ
date: 2021-09-15 10:24
tags:
- #mh
- work
---

1. Does Managed Hosting provide support for virtualization software and
   virtualized environments? Examples include VMWare's ESXi, Proxmox VE, OpenVZ,
   Virtuozzo, etc.

   Managed Hosting can facilitate the initial provisioning and setup of a Bare
   Metal Dedicated or Commercial Class server where the customer intends to
   host virtualization software. Generally speaking _Type 1 Hypervisors_ (ESXi,
   Proxmox, etc) are installed using a bootable installation media. Our DC
   technicians have been pretty good about installing custom OS's from bootable
   installation media in the past when the installer is provided and any
   applicable licenses are provided. But, this is done as a courtesy, and these
   requests are reviewed on a _case-by-case_ basis by our DC techs. 

   Beyond the initial provisioning of the server and setup with an OS, Managed
   Hosting **doesn't** provide support for managing or configuring their server
   running virtualization software. The onus is on the customer to administer
   their system beyond the initial setup or obtain support for their system from
   a 3rd party. 

   For a _managed_ virtualized environment hosted solution, Flexmetal is the
   closest we offer for something like that. It's in Beta and is geared towards
   a specific type of customer so it may only be a good fit for certain types of
   customers. 

2. Does Managed Hosting provide support for Microsoft Server or other Microsoft
   products? For example: SQL Server, Microsoft Exchange Server, etc.

   No, unfortunately Managed Hosting doesn't provide support for any Microsoft
   operating systems or server products. The exception being any Microsoft
   product that supports installation in a Linux environment, _.NET CORE_ for
   example. If the customer wishes to use a Microsoft server product on their hardware we
   can provision a bare metal server with a KVM and they can install whatever
   Microsoft OS they would like. Note, this requires purchase of a separate KVM
   subscription along with their Bare Metal. The customer is completely
   responsible for administering their own system or obtaining support for it
   from a 3rd party.

3. Does Managed Hosting provide support for _.NET CORE_? 

   Yes, Managed Hosting provides limited support for _.NET_ in that we can
   install it on Linux servers. But any configuration of .NET or development of
   applications built in .NET would be outside of our scope of support. 

4. Shared Package limits

5. VPS Package limits

6. Server monitoring

7. Maintenance ongoing upkeep of website/server over time.

1. Do you support Docker on VPS?

   No, due to how Docker configures the actual Linux kernel and how our
   Virtuozzo nodes are setup, this is incompatible with our VPS packages and we
   recommend a Bare Metal server if they want to run Docker.

1. Does MH perform email migrations?

   All internal email migrations are handled by WTR with the exception of Cloud
   VPS or Bare Metal Dedi.
   External full cPanel migrations that include email are also handled by WTR.
   External non-cPanel migrations are handled by Managed Hosting. 


