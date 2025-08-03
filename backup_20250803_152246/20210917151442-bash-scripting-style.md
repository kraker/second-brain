---
title: Bash Scripting Style
date: 2021-09-17 15:14
tags:
- 'bash'
---

Write scripts easy to read and maintain.

## Resources

* [Google - Shell Style Guide](https://google.github.io/styleguide/shellguide.html)
  * It's easy to understate how useful this style-guide is. It's basically become my style bible as of late.
  * This should really be the _defacto standard_.

## Use long option names to improve readability

``` bash
[me@linuxbox ~]$ ls -ad     # is equivalent to:
[me@linuxbox ~]$ ls --all --directory
```

