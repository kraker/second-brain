---
title: Install Apache SVN
date: 2021-08-12T07:09:00Z
---


## Installation

1. Check if `sqlite` and `mod_dav` are installed/provisioned 
```
php -m | grep sqlite
httpd -M | grep dav
```
If they're already installed you should get something like the following:
```
root@server [/]# php -m | grep sqlite && httpd -M | grep dav
pdo_sqlite
sqlite3
 dav_module (shared)
```
	* Using EA4 or `yum` install/provision the `sqlite` PHP module and `mod_dav`
	  extension for Apache if not already installed
	* `yum install ea-apache24-mod_dav`

2. `cd /usr/local/src/` 

4. Get the latest release of Subversion from the [downloads
	 page](https://subversion.apache.org/download/) 
```
wget https://downloads.apache.org/subversion/subversion-1.14.1.tar.gz
```

5. Unzip it.
```
tar xvzf subversion-1.14.1.tar.gz
```
6. `cd subversion-1.14.1`

7. You probably need to install these dependencies
```
yum install epel-release ea-apr-devel ea-apr-util-devel lz4-devel utf8proc-devel ea-apache24-devel
```

8. Get other dependencies
```
./get-deps.sh
```

9. Configure
```
./configure --with-apxs=/usr/bin/apxs --with-apr=/opt/cpanel/ea-apr16/bin/apr-1-config --with-apr-util=/opt/cpanel/ea-apr16/bin/apu-1-config
```

10. make and install
```
make clean
make
make install
```

11. Add LoadModules to WHM >> Apache Configuration >> Pre-Main Include >> All
	 Versions, or by editing `/etc/apache2/conf.d/includes/pre_main_global.conf`
```
LoadModule dav_svn_module /usr/local/libexec/mod_dav_svn.so
LoadModule authz_svn_module /usr/local/libexec/mod_authz_svn.so
```
Rebuild apache conf and restart apache

## Test

1. Get location of user confs for apache
```
cat /usr/local/apache/conf/httpd.conf | grep /etc/apache2/conf.d/userdata
```

2. Make dir where you're going to put your SVN conf
```
mkdir -p /etc/apache2/conf.d/userdata/std/2_4/cpuser/example.com/
```

3. Make SVN conf by creating and editing the following file using your favorite
	 text editor:
```
/etc/apache2/conf.d/userdata/std/2_4/cpuser/example.com/svn.conf
```

Insert the following adjusting `cpuser` etc.
```
SecRuleRemoveById 960013
SecRuleRemoveById 960032

<IfModule mod_dav_svn.c>
    <Location /svn>
        DAV svn
        SVNPath /home/cpuser/public_html/svn 
    </Location>
</IfModule>
```

5. Update apache conf
```
/scripts/ensure_vhost_includes –all-users
service httpd restart
```

6. Create repository files
```
switch cpuser
cd public_html/
svnadmin create svn
chmod 775 -R svn/
```

7. View test page http://example.com/svn

## See Also
https://forums.cpanel.net/threads/svn-install-on-centos-7-ea4.613563/
https://forums.cpanel.net/threads/location-path-for-apr-util-apr-1-config-using-ea4.608959/#post-2471127

