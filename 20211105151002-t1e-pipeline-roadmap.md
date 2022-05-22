---
title: T1E Pipeline "Roadmap"
date: 2021-11-05 15:10
tags:
- work
---

## Linux CLI Basics

* Gold-standard tutorial: [Command Line Crash Course](https://learnpythonthehardway.org/book/appendixa.html)
  + By Zed Shaw
* Also-good, is [Learning the Shell](https://linuxcommand.org/lc3_learning_the_shell.php)
* Best in class, video lecture: [The Missing Semester: Course Overview + the
Shell](https://missing.csail.mit.edu/2020/course-shell/)

### Commands

* `pwd`
* `cd`
* `ls`
* `clear`
* `cat`
* `less`
* `tail`
* `touch`
* `cp`
* `mv`
* `rm`
* `mkdir`
* `rmdir`
* `which`
* `help`
* `man`
* `find`
* `grep`
* `echo`
* `exit`
* `sudo`

#### Optional

* `hostname`
* `export`
* `env`
* `apropos`
* `xargs`
* `file` 
* `type`

### Proposed Lab

* Sean L's python CLI text-adventure game?
* [Terminus CLI Game](http://web.mit.edu/mprat/Public/web/Terminus/Web/main.html)?
* Live screen session share where a coach/mentor asks questions to determine
  whether or not agent is proficient in the terminal, answers questions, and shows
  appropriate answers, if agent is confused?
  + This should probably only take about 20-30 minutes. 
  + This is similar to the practical exams that London taxi-drivers have to take
    where they have an oral exam given by a proctor. 
  + How else do we measure true understanding/proficiency with basic CLI skills?

## MySQL Basics

### Import/Export

Use `mysql` and `mysqldump` to import/export databases.

### Introduce basic mysql shell commands

```
mysql -u root -p
```

```
SHOW DATABASES;
USE db_name;
SELECT * FROM tbl_name;
CREATE DATABASE db_name;
DROP DATABASE db_name;
SHOW tables;
DESCRIBE tbl_name;
...
```

A good reference to draw from might be:

* [Digital Ocean - Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)

## WordPress

### WP-CLI

IIRC some wp-cli is covered in training, but a more in-depth treatment of common
tasks done with the wp-cli might be covered here.

### Life of a Frond-end WordPress Request

_I'm not sure if this would be useful, I need to review this guide more in
depth, but this was recommended to me by a WP dev, so could be a good intro to
the WP application which may facilitate troubleshooting WP issues._

* [Life of a Front-end WordPress Request](https://roots.io/routing-wp-requests/)

## Proposed lab:

* Clone a WP site using only the CLI.
* Disable plugins
* Purge W3TC
* Activate different theme

## Basic Networking

* `dig`
* `host`

## Intro to disk utilization

* `du`
* `df`

## Intro to yum

Using `yum` and running system updates

### Installing PHP packages with yum, pecl, or pear

## Mail log searching and parsing

An overview on `grep`

## Status monitoring 

Anything that needs root basically.

## Ideas from Reece O.

Cover .htaccess, *.ini files, and php-fpm.


