---
title: Webmin Installation
date: 2021-05-21 16:45
---

https://doxfer.webmin.com/Webmin/Installation

## Install

### yum - CentOS/RedHat/Fedora

```
(echo "[Webmin]
name=Webmin Distribution Neutral
baseurl=http://download.webmin.com/download/yum
enabled=1
gpgcheck=1
gpgkey=http://www.webmin.com/jcameron-key.asc" >/etc/yum.repos.d/webmin.repo;
yum -y install webmin)
```

### Post install

1. `hostname -i` to get the server IP (if you don't already have)
2. Poke a hole in the firewall for port 10000

```
firewall-cmd --zone=public --add-port=10000/tcp --permanent
firewall-cmd --reload
```

3. Navigate to https://ip_addr:10000
	+ Note default username is `root` and the password is whatever the root user
		password is. 

#### Optional

Navigate to "Unused Modules" click "Usermin" and install Usermin.
