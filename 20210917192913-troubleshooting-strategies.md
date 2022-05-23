---
title: Troubleshooting Strategies
date: 2021-09-17 19:29
tags:
- 'bash'
---

* Use syntax highlighting to spot syntax errors
* Missing or unexpected tokens
    + Don't forget `;` and to close `if` and loops.
* Quote expansions in `test` to avoid errors
    + `[ "$number" = 1 ]`
    + **ALWAYS** enclose variables and command substitutions in double
      quotes unless word splitting is needed.
* Logical Errors
  1.  Incorrect conditional expressions
  2.  "Off by one" errors. *counters in loops*
  3.  Unanticipated situations Program encounters data or situations
      unforeseen.
