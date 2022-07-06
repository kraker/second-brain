---
title: Bash Scripting Style
date: 2021-09-17 15:14
tags:
- 'bash'
---

Write scripts easy to read and maintain.

## Resources

* [Google - Shell Style Guide](https://google.github.io/styleguide/shellguide.html)
  * This should really be the _defacto standard_.

## Use long option names to improve readability

``` bash
[me@linuxbox ~]$ ls -ad     # is equivalent to:
[me@linuxbox ~]$ ls --all --directory
```

