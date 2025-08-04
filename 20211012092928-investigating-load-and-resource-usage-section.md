---
title: Investigating Load And Resource Usage Section
date: 2021-10-12T09:29:00Z
tags:
---

## Investigating Load/Resource Usage

I've honestly never used any of the dedrads given to analyze resource
utilization. I actually only recently became aware of some of these.

* `check_user`
* `check_server`
* `check_apache`
* `fpm_status`

These are just wrappers for other utilities that I would argue are part of the
fundamentals we should be teaching as part of the APS pipeline. 

Things like `ps`, `sar`, `top`, `htop`, `free`, `uptime`, `apachectl`,
`mysqladmin`, and reviewing both the Apache and PHP-FPM logs for issues should
be the focus here. 

`exim` and/or `eximstats` might be appropriate here as well.

We can introduce our wrappers outlined above after we've taught the
fundamentals. 

The `nlp` script, although it's a bit broken is also helpful for understanding
resource usage spikes related to specific sites. Introducing the Apache domlogs
is probably a good thing to cover here.

For resource utilization issues on shared, I've actually used the
`check_software` script more often than any of the scripts provided above. If
anything that script might be a candidate for introduction here, but probably
more appropriate in the T1E training, if I'm honest. 

I would argue that `nlp` and `check_software` are better candidates for
introduction here as opposed to the four dedrads that are actually introduced,
if we're going to introduce dedrads in the pipeline at all. I really think we
need to make the pipeline dedrads and cPanel scripts agnostic. Linux and
sysadmin fundamentals that can be more or less universally applied skills should
be the focus. We want agents who know how to reason through problems rather than
just use the tools we've built. Our dedrads or cPanel scripts can become a
crutch otherwise.

This section introduces GTMetrix as a tool to analyze performance issues. That's
a useful tool, but again the official T1E training should probably introduce
this. I feel like competency in diagnosing performance issues on websites even
if it's just to advise a developer is something a competent T1E should already
know how to do. 

APS is where we need to learn how to diagnose, troubleshoot, and mitigate
performance issues on the server level. 
