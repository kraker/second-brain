---
title: Install WordPress
date: 2021-04-20T17:23:00Z
---

Switch to their user
1. [Create subdomain with cPanel uapi](20210629085947-create-subdomain-with-cpanel-uapi.md)
`uapi SubDomain addsubdomain domain='subdomain' rootdomain='example.com'`

`cd` into docroot

```
wget https://wordpress.org/latest.tar.gz
tar -xzvf latest.tar.gz
mv wordpress/* ./
rmdir wordpress/
rm -f latest.tar.gz
```

```
uapi Mysql create_database name="$(whoami)_newdb"
pass=$(head /dev/urandom | tr -dc _A-Z-a-z-0-9 | head -c15); echo $pass
uapi Mysql create_user name="$(whoami)_newdb" password="$pass"
uapi Mysql set_privileges_on_database user="$(whoami)_newdb" database="$(whoami)_newdb" privileges='ALL PRIVILEGES'
uapi Mysql get_privileges_on_database user="$(whoami)_newdb" database="$(whoami)_newdb" | grep 'ALL PRIVILEGES'
```

```
wp config create --dbname="$(whoami)_wp1" --dbuser="$(whoami)_wp1" --dbpass="$pass" --dbprefix="wp1"
grep -iE 'db|_prefix' wp-config.php && grep -i -A16 Salts wp-config.php
```
