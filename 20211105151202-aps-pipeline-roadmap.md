---
title: APS Pipeline "Roadmap"
date: 2021-11-05T15:12:00Z
tags:
- 'work'
---

## Linux System Administration Basics

* [Linux System Administration Basics](https://www.linode.com/docs/guides/linux-system-administration-basics/)

## Intermediate Linux CLI

* Gold-standard book: [The Linux Command Line](https://www.linuxcommand.org/tlcl.php)
  + Free PDF download, but purchase optional
  + By William Shotts
  + Sections 1 and 2. Section 3 is bash scripting which is also helpful to know,
  but more in the scope of T2S/MH pipeline.

### Commands

* `ftp` and `lftp`
* `scp` ?
* `ssh`

## Bash

### I/O Redirection

##### Standard Output

##### Standard Input

##### Pipes 

#### Expansion

##### Pathname Expansion

##### Tilde Expansion

##### Brace Expansion

##### Parameter Expansion

##### Command Substitution

#### Quoting

##### Double Quotes

##### Single Quotes

#### Escaping Characters

## Basic Regex

* Gold-standard tutorial: [regexone.com](https://regexone.com)

## Basic Text Processing

* `sort`
* `uniq`
* `grep`
* `head`
* `tail`
* `tr`
* `cut`

### Intro to Sed and Awk

* `sed`
* `awk`

#### Optional

* `fmt`
* `pr`

## Permissions

* `stat`
* `chmod`
* `su`
* `sudo`
* `chown`
* `chgrp`

### File perms

### User Management

## Job Control

* `ps`
* `kill`
* `jobs`
* `bg`
* `fg`

## Finding Files

* `find`
* `locate`

## Disk utilization

* `du`
* `df`

## Security

### Sessions

* `ssh`
* `screen`

#### Firewalls

* `apf`
* `csf`
 
## Backups and Archives

* `tar`
* `rsync`

### Proposed lab:

Perform a migration:

* Setup SSH keys
* Poke a hole in the firewall
* Create a tar ball
* migrate with rsync

## Basic Performance Troubleshooting

* `top` & `htop`
* `free`
* `uptime`
* `sar`

### Apache Domlogs

* dedrads: `nlp`

## LAMP

* `apachectl`
* `mysql`
* `php` CLI

### Proposed lab:

Install a lamp stack from scratch, configure vhosts, setup mysql, install PHP
and modules and get a WP site served on a unique domain with hosts file mod.
