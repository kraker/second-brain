---
title: Apache Reverse Proxy Setup
date: 2021-09-09T08:32:00Z
tags:
 - 'wiki'
---

## Overview

### Resources

* [Apache Mod Proxy](https://httpd.apache.org/docs/2.4/mod/mod_proxy.html)
* [cPanel - Apache Vhosts](https://docs.cpanel.net/ea4/apache/modify-apache-virtual-hosts-with-include-files/)
* [Tomcat Proxies](https://docs.cpanel.net/ea4/tomcat/tomcat-proxies/)

## Process

### Determine where to place the configuration changes

Determine the location where the files should be placed by checking the Apache
configuration file for the location of the virtual host include paths.

```bash
grep /etc/apache2/conf.d/userdata /usr/local/apache/conf/httpd.conf
```

The output should appear similar to what you see below.

```bash
root@server [/]# grep /etc/apache2/conf.d/userdata /usr/local/apache/conf/httpd.conf
  Include "/etc/apache2/conf.d/userdata/std/2_4/user1/domain.com/*.conf"
  # Include "/etc/apache2/conf.d/userdata/std/2_4/user1/domain.com/*.conf"
  # Include "/etc/apache2/conf.d/userdata/ssl/2_4/user2/sub1.domain.com/*.conf"
    Include "/etc/apache2/conf.d/userdata/ssl/2_4/user1/domain.com/*.conf"
  # Include "/etc/apache2/conf.d/userdata/ssl/2_4/user1/domain.com/*.conf"
  # Include "/etc/apache2/conf.d/userdata/std/2_4/user2/sub1.domain.com/*.conf"
  # Include "/etc/apache2/conf.d/userdata/std/2_4/user3/sub2.domain.com/*.conf"
  # Include "/etc/apache2/conf.d/userdata/ssl/2_4/user3/sub2.domain.com/*.conf"
```

As you can see in the resulting list above, every domain has an include path within the folders `/etc/apache2/conf.d/userdata/ssl/2_4/` and `/etc/apache2/conf.d/userdata/std/2_4/` followed by a folder matching the cPanel user name and then a folder matching the virtual host name. 

For example, in the line containing `Include "/etc/apache2/conf.d/userdata/std/2_4/user1/domain.com/*.conf"`, this is the include path for domain.com which is owned by user1.

Many of the lines are commented out, but if you place a .conf file in that path and rebuild Apache, the line containing that path will be uncommented automatically. The reason we double check the path is because some servers use `/etc/apache2/conf.d/userdata/ssl/2/` and `/etc/apache2/conf.d/userdata/std/2/` instead.

*Note: The folder for an addon domain will go by the name of the Virtual Host which will match the subdomain tied to that addon when it's created in cPanel.*

The path under ssl/ is for HTTPS and the path under std/ is for HTTP. I recommend placing the proxy under the ssl path, and then forcing HTTPS in the std path or .htaccess file.

### Making Reverse Proxy Configuration Changes for a Domain

Create the folders that match the appropriate include path for the domain you're working with, similar to below.

```
mkdir -p /etc/apache2/conf.d/userdata/ssl/2_4/cpuser2/subdomain.domain2.com/
```

Now create a file in that path with the text editor of your choosing and place the proxy directives within that file.

```
vim /etc/apache2/conf.d/userdata/ssl/2_4/cpuser2/subdomain.domain2.com/proxy.conf
```

A very simple reverse proxy configuration will look something like this, with 10000 being the port number of the application you wish to serve.

```
ProxyPass           "/"   "http://localhost:10000/"
ProxyPassReverse    "/"   "http://localhost:10000/"
```
#### Set up Redirect for HTTPS

Finally, we will force HTTPS in the .htaccess file within the document root of that domain.

```
vim /home/cpuser2/subdomain.domain2.com/.htaccess
```

Place the following contents in the file.

```
RewriteEngine On 
RewriteCond %{HTTPS} !on 
RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

Alternatively, you could place that in an include file such as `/etc/apache2/conf.d/userdata/std/2_4/cpuser2/subdomain.domain2.com/ssl.conf`

At the time of writing this, it isn't a common practice for Managed Hosting, but if you would like to do a kindness for our Customer Success department, leave a comment in the domain's .htaccess file to let them know about the configuration changes and where they are located. This could save the customer and the agent time in diagnosing a website issue that is out of scope for Support/APS.

```
## This domain has rewrites to force HTTPS and a reverse proxy to port 10000 configured by Managed Hosting. 
## The configuration for this setup is found in the files below:
## /etc/apache2/conf.d/userdata/std/2/cpuser2/subdomain.domain2.com/ssl.conf
## /etc/apache2/conf.d/userdata/ssl/2/cpuser2/subdomain.domain2.com/proxy.conf
```

#### Apply the configuration changes

Rebuild and restart Apache to apply the changes above. 

```
/scripts/rebuildhttpdconf && /scripts/restartsrv_httpd
```

Then test the domain to see if the proxy worked. As long as the application does not limit external access, you can try comparing the domain with the application as it appears when accessing the service directly via the port number. IE Using the examples above, we would visit http://server.hostname.com:10000 and compare with subdomain.domain2.com.

## Common Issues

**When navigating to other pages on the site, 404 errors occur.**

First, check how the site appears on the application behind the proxy in case
this is a development related issue. Then, check the URL that you are directed
to or the 404 error itself if it provides the path to the resource not found. Is
there an extra trailing slash in the path/URL?

It's possible you may need to remove the trailing slash at the end of the path
and/or localhost URL in the proxy. It depends on how the paths are configured in
the application itself.

For example, you may start with the following config.

```
ProxyPass           "/"   "http://localhost:10000/"
ProxyPassReverse    "/"   "http://localhost:10000/"
```

If you change it to what you see below, you might find the application works.

``` xml
ProxyPass           "/"   "http://localhost:10000"
ProxyPassReverse    "/"   "http://localhost:10000"
```

Alternatively, if you started with what you see below and have difficulties

``` xml
ProxyPass           "/app/"   "http://localhost:10000/app1/"
ProxyPassReverse    "/app/"   "http://localhost:10000/app1/"
```

You may want to try removing the trailing slashes like so.

``` xml
ProxyPass           "/app"   "http://localhost:10000/app1"
ProxyPassReverse    "/app"   "http://localhost:10000/app1"
```

**When accessing the application through the proxy, items cannot get added to the cart, and the user cannot log in despite there being no message indicating authentication failure.**
It's possible you need to add additional directives to the proxy configuration to ensure that the cookies on the site are functioning properly. 

This problem is common when the path on URL behind the proxy differs from the path on the external URL. Here is an example. 

``` xml
ProxyPass           "/"   "http://localhost:10000/subdir/"
ProxyPassReverse    "/"   "http://localhost:10000/subdir/"
```

Let's say this configuration was added for the virtual host somedomain.com. If this site uses cookies, internally the URL to that cookie will be something like localhost:10000/subdir/my-cookie, but externally the URL should be somedomain.com/my-cookie. The relative path to the cookie might still be considered subdir/my-cookie, so the request for the cookie when we access somedomain.com in a browser ends up being somedomain.com/subdir/my-cookie, which does not exit.

Here's the solution to establish the appropriate paths and domain for cookies which was lost in translation going through the proxy.

``` xml
   ProxyPass           "/"   "http://localhost:10000/subdir/"
   ProxyPassReverse    "/"   "http://localhost:10000/subdir/"
   ProxyPassReverseCookiePath /subdir /
   ProxyPassReverseCookieDomain localhost somedomain.com
```

It's possible you may need to place a trailing slash in the directives for ProxyPassReverseCookiePath to get things working. As mentioned in a previous section, it seems to depend how the application is coded.

## Additional Configuration

### Location Blocks

Sometimes the ProxyPass and ProxyPassReverse directives are container in Location blocks similar to what you see below.

``` xml
<Location "/">
   ProxyPass "http://localhost:10000/"
   ProxyPassReverse "http://localhost:10000/"
</Location>
```

As you can see, when contained within a Location block, these directives take
only one argument, because the first is aready specified in the <Location> tags.
Official Apache documentation recommends that you do not mix the two contexts. 

If there are proxy directives in Location blocks already, then any additional
proxy settings should be contained within its own appropriate location block. In
reverse, if there is existing configuration within a virtual host containing
proxy pass directives that are not contained within Location blocks, then
additional proxy pass directives should be added in the same fashion.

This is acceptable.

```
<Location "/">
   ProxyPass "http://localhost:10000/"
   ProxyPassReverse "http://localhost:10000/"
</Location>

<Location "/subdir/">
   ProxyPass "http://localhost:10000/subdir/"
   ProxyPassReverse "http://localhost:10000/subdir/"
</Location>
```

This is also acceptable.
```
ProxyPass           "/subdir/"   "http://localhost:10000/"
ProxyPassReverse    "/subdir/"   "http://localhost:10000/"

ProxyPass           "/"   "http://localhost:10000/"
ProxyPassReverse    "/"   "http://localhost:10000/"
```

Something like this will potentially cause confusion, and official Apache documentation discourages it.
```
ProxyPass           "/subdir/"   "http://localhost:10000/"
ProxyPassReverse    "/subdir/"   "http://localhost:10000/"

<Location "/">
   ProxyPass "http://localhost:10000/"
   ProxyPassReverse "http://localhost:10000/"
</Location>
```

### Loading order
You might run into a set up where the URLs in multiple proxy configuration overlap. 

For example, I might want `https://mydomain.com` to load an application at `http://localhost:10000/mystore` but I also want `https://mydomain.com/blog` to load an application at `http://localhost:10000/blog`. 

This can cause conflict potentially because the URL mydomain.com/blog is a subdirectory of mydomain.com/ which has a proxy set up for a different app. 
Fortunately, if you place the ProxyPass directives in the correct order, this shouldn't cause issues. The order changes, however, depending on if you are using Location blocks or not.

#### Loading Order - No Location Block
For proxy rules that are not contained within a location block, you want the longest path/URL first. So in the example above, your configuration file would look like this.

```
ProxyPass           "/blog/"   "http://localhost:10000/blog/"
ProxyPassReverse    "/blog/"   "http://localhost:10000/blog/"

ProxyPass           "/"   "http://localhost:10000/mystore/"
ProxyPassReverse    "/"   "http://localhost:10000/mystore/"
```

#### Loading Order - Location Block
For proxy rules that are contained within location blocks, you will need to start with the shorter path/URL. In the example above, your configuration file would look like this if you're using location blocks.

```
<Location "/">
   ProxyPass "http://localhost:10000/mystore/"
   ProxyPassReverse "http://localhost:10000/mystore/"
</Location>

<Location "/blog/">
   ProxyPass "http://localhost:10000/blog/"
   ProxyPassReverse "http://localhost:10000/blog/"
</Location>
```

