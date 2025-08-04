---
title: Install PrestaShop
date: 2021-04-21T10:19:00Z
---

1. Register/login and choose download at https://www.prestashop.com/en/versions
	 + Copy link with API token
	 + Download using `wget` similar to this:
```
wget \
https://www.prestashop.com/en/file/prestashop_1-7-7-3-zip/download?token=wmPwuAia \
-O prestashop_1-7-7-3.zip 
```

2. `unzip prestashop_1-7-7-3.zip`
3. Create database
```
uapi Mysql create_database name="$(whoami)_newdb"
pass=$(head /dev/urandom | tr -dc _A-Z-a-z-0-9 | head -c15); echo $pass
uapi Mysql create_user name="$(whoami)_newdb" password="$pass"
uapi Mysql set_privileges_on_database user="$(whoami)_newdb" database="$(whoami)_newdb" privileges='ALL PRIVILEGES'
uapi Mysql get_privileges_on_database user="$(whoami)_newdb" database="$(whoami)_newdb" | grep 'ALL PRIVILEGES'
```
4. Launch installer by navigating to domain/site in browser


## References
http://doc.prestashop.com/display/PS17/Installing+PrestaShop
