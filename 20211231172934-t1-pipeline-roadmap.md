---
title: T1 Pipeline Roadmap
date: 2021-12-31 17:29
tags:
- #work
- #learning
- #training
---

_Note: This is a work in progress. Feedback is appreciated. Feel free to email
me at alex@alexkraker.com_

This _roadmap_ assumes no real prior knowledge of Linux, web-hosting, web
development, or IT.  This isn't intended to be an exhaustive guide, but rather a
suggested list of resources that should allow any beginner or beginner to
intermediate skill level (i.e. "noob") to acquire the necessary skills qualify
for a Tier 1 Technical Support role working in a web-hosting (Linux) centric
environment. (Those interested in supporting Windows based environments may still
benefit from the resources included here, but would probably be best served by
seeking out a guide that addresses a Windows centric IT support role.)

It's assumed that if you're reading this, that you're a self-starter, and able
to _fill in the gaps_ by doing your own research (i.e. google-fu) if something
doesn't make sense. This is a roadmap not an exhaustive tutorial. Other authors
and teachers have done a much better job of creating learning materials and
tutorials than I could ever do myself. Just like with most open source software
I'm going to borrow heavily from things that have been built by people much more
capable and experienced than myself. This is the open source way after all. 

This is curated list of what I consider to be essential skills along with the
best free resources available to learn those skills.  This collection is
inspired by guide's like the [Teach Yourself Computer
Science](https://teachyourselfcs.com/) and [Open Source Society
University](https://github.com/ossu/computer-science). The primary difference
being this is intended to provide a foundation for the aspiring Linux System
Administrator. While there's quite a bit of overlap between Computer Science and
System Administration, there are skills and fundamentals that seem to be the
foundation for competency in IT and System Administration.

## Linux CLI Fundamentals

* Gold-standard tutorial: [Command Line Crash Course](https://learnpythonthehardway.org/book/appendixa.html)
  + By Zed Shaw
* Also-good, is [Learning the Shell](https://linuxcommand.org/lc3_learning_the_shell.php)
* Best in class, video lecture: [The Missing Semester: Course Overview + the Shell](https://missing.csail.mit.edu/2020/course-shell/)

## Learn cPanel Basics

_This section is web hosting centric. If you're not looking to work in web
hosting, feel free to skip this section._

It's hard to beat the official cPanel university certifications for learning the
fundamentals of their platform. If you haven't already I recommend registering
an account at [cPanel University](https://university.cpanel.net/). 

* Complete the _cPanel Professional Certification (CPP)_

It helps if you have access to a cPanel in order to try out the things in
cPanel. If you don't already have access to cPanel, this author recommends
finding a budget host (there are some for as little as $1/mo) and getting a 1
month subscription to start. It's a few bucks to further your education.

## Install a WordPress site

_This skill is web hosting centric. If not looking to work in web-hosting, or
you have no interest in front-end development, feel free to skip this section._

* Best overall tutorial: [How to Install WordPress](https://wordpress.org/support/article/how-to-install-wordpress/)

## Concepts, Software, and Protocol fundamentals

* Port
  + A port is a number. It's the port that a server uses to send/receive
  requests. It's part of the Internet Protocol. Whenever your computer connects
  to a server for any reason, it does so through an open port on that server. 
* FTP - File Transfer Protocol
  + Used to transfer files. It's in the name.  
  + Uses port 21
* SSH - Secure Shell
  + Uses an encrypted tunnel to provide a secure connection to a remote terminal 
  (CLI) 
  + Uses port 22
* HTTP - Hyper-text Transfer Protocol
  + Most of the web uses HTTP (or HTTPS). If you're reading this in a browser
  it's being served using HTTP by a web server. 
  + Uses port 80
* HTTPS - Hyper-text Transfer Protocol Security
  + This is the secure version of HTTP and runs on a different port number.u
  Anytime you see that _insecure_ warning in your browser it's usually because 
  the site you visited isn't sing HTTPS and is therefore insecure. HTTPS uses an 
  _SSL Certificate_ to create an encrypted connection to the web server that's 
  running the website you visited. 
  + Uses port 443

### Apache Web Server

[Apache](https://httpd.apache.org/) is the most commonly used free open source
web server in use on the internet. Most servers that host websites run Apache.
This is the software that _serves_ web-pages over the HTTP and HTTPS protocols
(ports 80 and 443 respectively).

### Linux

Linux is an operating system. It's like Windows, MacOS, or Android. It's the
most common operating system in use on servers. It's free and open source (FOSS)
meaning anyone can download, install it, and use it however they see fit. You
can custom compile the Linux Kernel to your own needs if you want. 

Most Linux operating systems are what's known as a distribution which is a
bundle or package of software that ships with the Linux Kernal, usually
containing an installer, and a few other _nice-to-haves._ 

In the web hosting space [CentOS](https://www.centos.org/) is a commonly used 
Linux Distribution that's used for web servers. The main reason being it's
reputation for long-term stability. It's the free open source (unlicensed)
version of _RedHat Enterprise Linux (RHEL)_ that's known for it's stability and
is backed by the support that RedHat offers. 

Another common Linux Distribution that's often used for web-hosting servers and
which you may have heard of is [Ubuntu Server](https://ubuntu.com/server).

### Recommended Learning

- [ ] Download a common FTP client for your OS whether that's Windows or MacOS and
  figure out how to connect to an FTP server with it. 
- [ ] Download an SSH client and connect to a Linux server using SSH

#### Optional

- [ ] Find a Linux Distribution that you like and if you have old hardware
  laying around, figure out how to install it and run it.

## Networking/DNS

STUB

### Commands to learn

- `dig`
- `host`
- `whois`
- `ping`
- `traceroute`

### DNS

* Video tutorials
  + Really good, but long: https://www.youtube.com/watch?v=WDutOk8Piu8
    + Recommended by Paul K.
  + Basic intro: https://www.youtube.com/watch?v=uOfonONtIuk

### Recommended exercises to learn DNS

1. Create an **A** record that points your root domain to the server IP where your site is hosted.
2. Create a **CNAME** record that aliases the `www` subdomain to your root domain. i.e. www.yourdomain.com
3. Create the appropriate **MX** record to route email to your mailserver
4. Create an additional A record (or CNAME) record for the mail subdomain. 
5. Create both of the **TXT** records that you need to ensure good email deliverability. These are the DKIM and SPF records. These validate the server that the server that the emails were sent from as a valid sender of emails from your domain.
6. Make sure you verify that your root domain, and www resolve to your website
7. Test sending/receiving email and verify that that all works as it should
8. Use `whois`, `dig`, `host` to verify the DNS records that you created

#### Examples

```bash
[alexkr@ash-sys-pro-js3:~]$ dig thisinterestingmind.com

; <<>> DiG 9.8.2rc1-RedHat-9.8.2-0.68.rc1.el6.11.cloudlinux.els <<>> thisinterestingmind.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 17150
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;thisinterestingmind.com.       IN      A

;; ANSWER SECTION:
thisinterestingmind.com. 641    IN      A       209.182.195.45

;; Query time: 0 msec
;; SERVER: 198.46.80.58#53(198.46.80.58)
;; WHEN: Tue Jan  4 13:55:01 2022
;; MSG SIZE  rcvd: 57
```

```bash
[alexkr@ash-sys-pro-js3:~]$ dig cname www.thisinterestingmind.com

; <<>> DiG 9.8.2rc1-RedHat-9.8.2-0.68.rc1.el6.11.cloudlinux.els <<>> cname www.thisinterestingmind.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 63532
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;www.thisinterestingmind.com.   IN      CNAME

;; ANSWER SECTION:
www.thisinterestingmind.com. 900 IN     CNAME   thisinterestingmind.com.

;; Query time: 1 msec
;; SERVER: 198.46.80.58#53(198.46.80.58)
;; WHEN: Tue Jan  4 13:55:34 2022
;; MSG SIZE  rcvd: 59
```

```bash
[alexkr@ash-sys-pro-js3:~]$ dig mx thisinterestingmind.com

; <<>> DiG 9.8.2rc1-RedHat-9.8.2-0.68.rc1.el6.11.cloudlinux.els <<>> mx thisinterestingmind.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 33380
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;thisinterestingmind.com.       IN      MX

;; ANSWER SECTION:
thisinterestingmind.com. 623    IN      MX      0 thisinterestingmind.com.

;; Query time: 0 msec
;; SERVER: 198.46.80.58#53(198.46.80.58)
;; WHEN: Tue Jan  4 13:55:52 2022
;; MSG SIZE  rcvd: 57
```

```bash
[alexkr@ash-sys-pro-js3:~]$ dig txt thisinterestingmind.com

; <<>> DiG 9.8.2rc1-RedHat-9.8.2-0.68.rc1.el6.11.cloudlinux.els <<>> txt thisinterestingmind.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 20328
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;thisinterestingmind.com.       IN      TXT

;; ANSWER SECTION:
thisinterestingmind.com. 900    IN      TXT     "v=spf1 +a +mx +ip4:209.182.195.45 ~all"

;; Query time: 1 msec
;; SERVER: 198.46.80.58#53(198.46.80.58)
;; WHEN: Tue Jan  4 14:07:58 2022
;; MSG SIZE  rcvd: 92
```

#### DNS Records

* [DNS Record Types](2020-11-17--15-28-31Z--dns_record.md) 

## Learn HTML/CSS (Optional)

While it's not strictly necessary to learn HTML/CSS in order to become a
competent Linux System administrator. HTML is such a universal thing, that it
helps to understand it at least a little bit. CSS is really only relevant if you
have any interest at all in front-end. That said, it's definitely helpful to
have some awareness of what's possible with HTML/CSS and what it does if you intend
to work in any part of web hosting. The best way to learn is by doing. 

* Best crash-course in HTML/CSS, should only take a few hours: [Learn to Code
HTML & CSS](https://learn.shayhowe.com/)
* Create an account at [freecodecamp.org](https://freecodecamp.org) and the first two sections of the
_Responsive Web Design_ course, do a pretty decent job of covering HTML/CSS.
* Recommended book: [Head First HTML and
CSS](https://www.oreilly.com/library/view/head-first-html/9781449324469/)
  + Don't just take my word for it, read this: [Should You Learn Programming?
  Yes.](https://sive.rs/prog) by Derek Sivers

## Learning Strategies (Optional)

Just some recommendations for learning.

* [Learning Strategies](20220104103406-learning-strategies.md)

## Notes from Paul K.

* https://www.freecodecamp.org/news/learn-the-50-most-used-linux-terminal-commands/
* https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Bash-Variables
* https://learncodethehardway.org/unix/bash_cheat_sheet.pdf

## Alex's Notes

* [Applying, interviewing, and such](20220104072206-applying-interviewing-and-such.md)
