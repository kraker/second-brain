---
title: Performance & Optimization
date: 2021-10-13 06:18
tags:
- 'sysadmin'
- 'linux'
---

# Performance & Optimization

## Resources

* [Explanation of what load averages really means][1]
* [Commands you should run in the first 60 seconds on a misbehaving server][2]
* [In-depth analysis of Linux Performance tools][3]
* [30 Linux monitoring tools every sysadmin should know][4]

[1]: https://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html
[2]: https://medium.com/netflix-techblog/linux-performance-analysis-in-60-000-milliseconds-accc10403c55
[3]: https://medium.com/netflix-techblog/netflix-at-velocity-2015-linux-performance-tools-51964ddb81cf
[4]: https://www.cyberciti.biz/tips/top-linux-monitoring-tools.html

## Notes

* [Source][3]
* [Slides from presentation](https://www.slideshare.net/brendangregg/velocity-2015-linux-perf-tools)

[3]: https://medium.com/netflix-techblog/netflix-at-velocity-2015-linux-performance-tools-51964ddb81cf

It's important to have a methodology. I've run these tools in this manner and I
didn't find anything that indicates a performance issue on the server. I think
you should check your code.

### Anti-Methods

Drunk man looking for their keys under a streetlamp because that's where the
light is.

Blame someone else anti-method.

### Actual Methodologies

* Problem statement
* Workload characterization
* USE
* Off-CPU Analysis
* CPU profile
* RTFM Method
* Active Benchmarking
* Static Performance Tuning

#### Problem Statement Method

1. What makes you **think** there is a performance problem?
2. Has this system **ever** performed well?
3. What has **changed** recently?
  a. Software?
  b. Hardware? 
  c. Load?
4. Can the performance degradation be expressed in terms of **latency** or run
   time?
5. Does the problem affect **other** people or applications (or is it just you)?
6. What is the **environment**? Software, hardware, instance types? Versions?
   Configuration?

#### Workload Characterization Method

1. **Who** is causing the load? PID, UID, IP addr, ...
2. **Why** is the load called? code path, stack trace
3. **What** is the load? IOPS, tput, type, r/w
4. **How** is the load changing over time?

#### The USE Method

Only check these 3 things for all of your resources.

For every resource check:

1. Utilization
2. Saturation
3. Errors

Definitions:

* Utilization: busy time
* Saturation: queue length or queued time
* Errors: easy to interpret (objective)

It helps if you have a functional (block) diagram of your system / software /
environment, showing all resources

Start with questions, then find the tools.

##### USE Method: Linux Performance Checklist

[USE Linux](https://www.brendangregg.com/USEmethod/use-linux.html)

#### Off-CPU Analysis

_See slides_

I'm not sure I understand this really...worth more research.

#### CPU Profile Method

1. Take a CPU profile
2. Understand all software in profile > 1%

* Discovers a wide range of performance issues by their CPU usage.
* Narrows software study.

If you profile what's on CPU then narrows down what parts of the software (i.e.
MySQL) is actually turned on and therefore needs to be looked at.

#### RTFM

How to understand performance tools or metrics?

1. Man pages
2. Books
3. Web search
4. Co-workers
5. Talks, slides, videos
6. Support services
7. Source code
8. Experimentation
9. Social

Reading through source code. Writing a bit of code that should tax the resource
in the way we're looking for.

### Tools

Objectives:

* Perform the USE Method for resource utilization
* Perform workload characterization for disks, network
* Perform CPU Profile Method using flame graphs
* Have exposure to various observability tools:
  + Basic: vmstat, iostat, mpstat, ps, top
  + Intermediate: tcpdump, netstat, nicstat, pidstat, sar,
  + Advnaced: ss, slaptop, perf_events, 
* Perform Active Benchmarking
* Understand tuning risks
* Perform Static Performance Tuning

#### Tool Types

| Type          | Types                                                                    |
|---------------|--------------------------------------------------------------------------|
| Observability | Watch activity. Safe: usually, depending on resource overhead.           |
| Benchmarking  | Load test. Caution: production tests can cause issues due to contention. |
| Tuning        | Change. Danger: changes could hurt performance, now or later with load.  |
| Static        | Check configuration. Should be safe.                                     |

#### Basic Observability Tools

* uptime
* top or htop
* ps
* vmstat
* iostat
* mpstat
* free

#### Intermediate Observability Tools

* strace
* tcpdump
* netstat
* nicstat
* pidstat
* swapon
* lsof
* sar - System Activity Reporter
