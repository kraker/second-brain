---
title: Associative Arrays
date: 2021-09-18T08:46:00Z
tags:
- 'bash'
---

Supported by bash 4.0+ Use strings rather than integers as array indexes.

```bash
declare -A colors
colors["red"]="#ff0000"
colors["green"]="#00ff00"
colors["blue"]="#0000ff"

echo ${colors["blue"]}
```
