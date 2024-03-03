---
title: Job Scheduling
date: 2024-03-03 10:50
tags:
- 'linux'
- 'sysadmin'
---

# Job Scheduling

Job scheduling and execution is taken care of by two service daemons:

* at (1)               - queue, examine, or delete jobs for later execution
* atd (8)              - run jobs queued for later execution
* cron (8)             - daemon to execute scheduled commands
* crond (8)            - daemon to execute scheduled commands

```bash
[root@server1 ~]# ls -ld /etc/{at,cron}*
-rw-r--r--. 1 root root   1 Apr  4  2022 /etc/at.deny
drwxr-xr-x. 2 root root  21 Feb 16 09:08 /etc/cron.d
drwxr-xr-x. 2 root root   6 Mar 23  2022 /etc/cron.daily
-rw-r--r--. 1 root root   0 Jul 11  2022 /etc/cron.deny
drwxr-xr-x. 2 root root  22 Mar 23  2022 /etc/cron.hourly
drwxr-xr-x. 2 root root   6 Mar 23  2022 /etc/cron.monthly
-rw-r--r--. 1 root root 451 Mar 23  2022 /etc/crontab
drwxr-xr-x. 2 root root   6 Mar 23  2022 /etc/cron.weekly
```

By default all users are allowed to schedule jobs with the `at` and `cron` services, but this can be controlled with the `/etc/at.{allow,deny}` and `/etc/cron.{allow,deny}` files specifically.

