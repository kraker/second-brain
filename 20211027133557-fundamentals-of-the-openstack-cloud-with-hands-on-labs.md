---
title: Fundamentals Of The Openstack Cloud
date: 2021-10-27T13:35:00Z
tags:
- 'work'
---

## 6 Core Projects

A combined total of 45 various projects in the OpenStack _ecosystem_.

There are currently 6 core projects.

1. Nova - Compute service
2. Neutron - Networking
3. Swift - HA & Scalable, Object Storage
4. Glance - Image management services
5. Keystone - Identity service
6. Cinder - Block storage service

## Other Popular OpenStack Projects

1. Horizon - Dashboard
2. Heat - Infra Orchestration
3. Ceilometer - Metering and data collection
4. Rally - Benchmarking
5. Ironic - Bare metal provisioning
6. Designate - DNS as a service
7. Manila - Shared filesystems, NFS etc
8. Trove - Database as a service
9. Kolla - Container deployment
10. Magnum - Container Orchestration Engine Provisioning
11. Murano - Application catalog
12. Sahara - Big Data Processing Framework Provisioning

## Production OpenStack Deployment

* Has one or more nodes.
* A node is usually a physical server on which OpenStack services are run.
  + A node can also be a VM in dev/test environments
* An All-In-One (AIO) node is a single machine that performs all OpenStack cloud
  functions
* Network Node: provides networking
  + Usually runs Neutron services 
* Compute Nodes: 
  + Runs hypervisor
    + Instances are created on this node
  + Note: cpu must support virtualization
  + NUMA support recommended

## Storage Types

1. Block storage
2. File-based storage
3. Object storage

Note, default with OpenStack is _ephemeral_ file-storage that only persists as
long as the VM is running. For persistent storage, the 3 types above are
required.

### Block Storage

Provides persistent storage volumes to VMs.

### File-based storage

Enables VMs to mount a remote file-system and share data. 

Protocols:

* NFS
* CIFS
* GlusterFS
* HDFS

### Object Storage

* Swift is similar to AWS S3.
* Stores and retrieves binary objects. Binary object is any file in any format.
* Provides data replication for reliability.

## Cloud Controller Node

Functions as a control plane for the cloud. 

Runs most of the services required to run the OpenStack Cloud. 

## Compute Node

Runs the hypervisor and where containers are deployed.

## Network Node

Routes traffic, DNS, virtual switches, etc. 
Service it uses is called Neutron.

* Layer3 Agent
* DHCP Agent
* Layer2 Agent
* Metadata Agent

## Storage Node

Contains disks for providing persistent storage to instances.

* LVM + Physical disks
* Managed by Cinder volume
* Uses LVM driver

## Keystone Deep Dive

RBAC
: Role Based Access Control


