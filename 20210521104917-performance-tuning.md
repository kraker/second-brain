---
title: 20210521104917-performance-tuning
date: 2021-05-21T10:49:00Z
modified: 2025-08-08T23:10:19Z
---

## Show Running Processes

```
mysqladmin pr
mysqladmin stat
mysqladmin pr stat
```

## Run mysqltuner.pl

```
curl -sL https://raw.github.com/major/MySQLTuner-perl/master/mysqltuner.pl | perl
```

## Enable "Sys Schema"

### MariaDB

https://github.com/FromDual/mariadb-sys
