---
title: FTP Server Setup
date: 2021-05-20 12:46
---

ZD: 5666044

## Reqs

1. FTP service running on a cloud VPS with some type of Linux OS.
2. Transition from your existing Windows FTP host to our hosting needs to be
	 seamless
3. Usernames and passwords that you have currently (in the XLS file) need to
	 stay the same
4. File permissions, file access, and folder access for those FTP accounts needs
	 to be mapped over from your existing FTP server
5. It also sounds like you require some type of GUI interface or "dashboard" for
	 administrative users to manage the FTP server


## Q's

1. Are they planning on using existing cVPS, or are we provisioning an
	 additional one?
	 They're going to use existing cVPS
3. How do their client's typically currently access their existing FTP server?
	 Some type of FTP client accesses FTP accounts. 

## FTP Servers

https://www.linuxlinks.com/best-free-open-source-linux-ftp-servers/

### FileZilla FTP Server

Note: currently using FileZilla FTP server, but this doesn't support Linux, only runs on Windows.
https://filezilla-project.org/download.php?show_all=1&type=server

### ProFTPD

https://wiki.archlinux.org/title/ProFTPD
http://proftpd.org
* GPL license allows for commercial use

### Pure-FTPd

https://wiki.archlinux.org/title/Pure-FTPd
https://www.pureftpd.org/project/pure-ftpd/

### Very Secure FTP Daemon

https://wiki.archlinux.org/title/Very_Secure_FTP_Daemon
https://security.appspot.com/vsftpd.html

### Bftpd
http://bftpd.sourceforge.net/

## FTP admin panels

### Webmin

webmin.com
https://forums.centos.org/viewtopic.php?t=46257
* webmin ProFTPd module: http://doxfer.webmin.com/Webmin/ProFTPD_Server
	+ Works out of the box with ProFTPD
* License allows commercial use

### Control Webpanel (AKA CentOS Webpanel)

http://centos-webpanel.com


## Other considerations

* We'll want some type of firewall and maybe even login protection, to prevent
	FTP service getting hammered.
	
* What's the best way to map accounts to file-paths, files, and provide access
	perms?

## OS?

* CentOS for stability/maintainability?

## Misc.

CrushFTP is enterprise grade, but has some _nice-to-have's_
https://www.crushftp.com/case_studies.html

## Linux Administration

### [Bind mount](2021-06-23--10-41-54Z--bind_mount.md)

* [mount](2021-06-10--11-33-47Z--mount.md)

### [Users and groups](2021-06-23--14-27-42Z--users_and_groups.md)
#### [User management](202106-23143339-user_management.md)





