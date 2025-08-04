---
title: Install GCC for gRPC dependency
date: 2021-06-15T10:52:00Z
---

_Credit: Roger Sm._

```
yum install centos-release-scl-rh
yum install devtoolset-3-gcc devtoolset-3-gcc-c++
scl enable devtoolset-10 bash
```

Then run pecl installer for every version of PHP per:
https://support.cpanel.net/hc/en-us/articles/360050028094-How-to-install-PHP-extensions-using-PECL

Example:
```
/opt/cpanel/ea-php73/root/usr/bin/pecl install xmldiff
```

