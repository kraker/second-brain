---
title: Bash Script Header
date: 2021-09-17 14:21
tags:
- 'bash'
---

```bash
#!/bin/bash

# This is our first script.

echo 'Hello World!'
```

Usually has some variation of the "shebang" `#!/bin/bash`

Below is an often used alternative to the above. In production scripts it's
probably better to use this variation.

```bash
#!/usr/bin/env bash
```
