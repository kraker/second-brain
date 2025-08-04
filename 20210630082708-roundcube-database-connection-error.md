---
title: RoundCube Database Connection Error
date: 2021-06-30T08:27:00Z
---

Fix RoundCube database connection error:

```
DATABASE ERROR: CONNECTION FAILED!
Unable to connect to the database!
Please contact your server-administrator.
```

## The fix

Run these:

```
rpm -e --nodeps cpanel-roundcubemail
/usr/local/cpanel/scripts/check_cpanel_rpms --fix
```

Or try renaming sqlite dbs:
https://support.cpanel.net/hc/en-us/articles/360051956994-How-To-Fix-A-Corrupted-RoundCube-SQLite-Database
