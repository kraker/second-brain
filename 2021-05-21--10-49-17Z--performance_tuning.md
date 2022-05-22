---
title: Performance Tuning
date: 2021-05-21 10:49
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