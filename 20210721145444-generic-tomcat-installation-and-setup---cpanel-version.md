---
title: Generic Tomcat Installation and Setup - cPanel version
date: 2021-07-21 14:54
---

## Resources

cPanel Documentation:
* [Introduction to Tomcat](https://docs.cpanel.net/ea4/tomcat/tomcat/)
* [Tomcat Proxies](https://docs.cpanel.net/ea4/tomcat/tomcat-proxies/)
* [Tomcat Private Instances](https://docs.cpanel.net/ea4/tomcat/tomcat-private-instances/)

## Installation

You can install Tomcat through EasyApache 4 in WHM or on the CLI with:
```
yum -y install ea-tomcat85
```

### Removal

Removal can be done through EasyApache 4 in WHM or on the CLI with:
```
yum -y remove ea-tomcat85
```

## Configuration

### Enable for cPanel User

```
/usr/local/cpanel/scripts/ea-tomcat85 add <cpuser>
```

### User-Specific Configuration Files

```
/home/<cpuser>/ea-tomcat85/conf
```
_Note: The cPanel user must be added to the Tomcat user list with the `add`
command above. Until then the _ea-tomcat85_ folder doesn't exist._

### Check Assigned Ports

When you add the user to the Tomcat Manager the user is automatically assinged 2
ports for the Tomcat setup. To determine what those ports are run:
```
cat /etc/cpanel/cpuser_port_authority.json | grep -B 1 <cpuser>
```
This will return the user and the ports assigned to that user. It should look
somethign like this:
```
   "10000" : {
  	"owner" : "cpuser",
--
   "10001" : {
  	"owner" : "cpuser",
```
In this case, ports 10000 and 10001 have been assigned to the cPanel user
_cpuser_. These ports must be opened in the firewall if a proxy is _not_ going
to be set up for use. Otherwise, the ports can remain closed. 

### Apache Proxy Setup

You can follow the steps in this guide.

## Stop/Restart

_Note: This applies to all cPanel users configured to use Tomcat._

```
/usr/local/cpanel/scripts/ea-tomcat85 all restart
```

### Enable Start/Stop for cPanel Users

To enable the ability for users to start/stop/status of Tomcat, add the
following to the users `.bashrc` file:
```
export PATH=$(dirname $(readlink /usr/local/cpanel/3rdparty/bin/perl)):$PATH
```

Make sure you add this to the `~/.bashrc` file for the user:
```
echo "export PATH=$(dirname $(readlink /usr/local/cpanel/3rdparty/bin/perl)):$PATH" >> ~/.bashrc
```

Then, the user can run the following commands:

```
ubic status ea-tomcat85
ubic start ea-tomcat85
ubic stop ea-tomcat85
ubic restart ea-tomcat85
```

## Testing the Setup

To test the Tomcat setup, copy the _test.jsp_ file from the system to the user's
Tomcat directory, as follows:
```
cp /opt/cpanel/ea-tomcat85/test.jsp /home/<cpuser>/ea-tomcat85/webapps/ROOT
```

Then you can visit the site, with _test.jsp_ appended, to see the setup.

## Explanation of Tomcat under cPanel

_Note: This was written in a way to be able to copy-and-paste to the customer._

>The way that Tomcat has been installed on the domain is done as a Private Instance of Tomcat and as a result, it's more secure, which also includes integration into WHM and cPanel.  There's no Tomcat Manager as a result since the Tomcat Manager is for all users on the server, whereas Tomcat installed on the domain is strictly for the cPanel user and nobody else.
>
>To gain access to the Tomcat Manager for the whole server, you need to login to Root WHM and search, under the WHM logo, for "tomcat" and you'll see Tomcat Manager.
>
>The location where Tomcat applications are deployed in this installation is at (note the <cpuser> entry is where the cPanel username should be):
>
>/home/<cpuser>/ea-tomcat85/webapps/ROOT/
>
>The installation of Tomcat onto the whole server is done completely separate from WHM/cPanel and as a result provides you with access to the Tomcat Manager as a completely separate, isolated login from WHM and cPanel.  This confirmation is less secure as a result because anyone could have access to the Tomcat Manager since it's fully public-facing.
>
>The location of where you need to place your Tomcat applications for this type of installation would be something like:
>
>/opt/tomcat85/webapps/ROOT/
>
>Which requires Root access via the command line or FTP in order to manage since no cPanel user’s File Manager application can access this location.

