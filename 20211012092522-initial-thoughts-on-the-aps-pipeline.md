---
title: Initial Thoughts On The Aps Pipeline
date: 2021-10-12T09:25:00Z
tags:
---

I feel like this reads more like a different version of APS training rather than
a pipeline for skills-building that prepares an agent to apply for APS and take
the APS training. 

My personal feelings is that we should teach the universal way to diagnose
issues that doesn't rely on internally built scripts. We should teach the general
best-practices way that a sysadmin would troubleshoot a server using tools, logs
and utilities, that are commonly available. This introduces
good sysadmin skills and prepares the agent for tackling the types of problems
that might be something they've never seen before and which aren't easily
diagnosed unless they possess working understanding of how a web-server system
works. After those core skills have been developed then we can introduce our
internally built scripts, dedrads, etc as tools that can be used. Then these
tools can be used with a foundational understanding of what type of information
and diagnostics they are providing and which can be used to diagnose issues.

Otherwise we've obfuscated what's actually happening _under-the-hood_. 

For example learning how to use things like `sar`, `top`, `uptime`,
`apachectl`, review logs, etc. 

Scripts that are wrappers for things like `apachectl` while helpful, don't
encourage learning and understanding the utilities they're based on which are
critical tools one should know how to use. 

Beginner and Intermediate CLI proficiency is a pre-requisite to being ready to
apply for APS and take the APS training. 

The APS pipeline should endeavor to bring agents up to speed in terms of
intermediate Linux CLI skills. 

Significant chunks of this training are also covered by cPanel University. Why
not avoid having to re-invent the wheel, and make the 1st level cPanel
University cert part of the pipeline? It's a pretty foundational introduction to
most of the sysadmin skills and tools that an agent should be aware of and have
a working understanding of as an APS agent. Specifically as applies to a cPanel
server. 

If this were a text adventure game, obtaining that cert is like a _side quest_.

