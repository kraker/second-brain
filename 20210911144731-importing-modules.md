---
title: Importing Modules
date: 2021-09-11 14:47
tags:
- #python
---

**import** statement consists of the following:

* The _import_ keyword
* The name of the module
* Optionally, more module names, as long as they are separated by commas

Example: 

```python
import random
for i in range(5):
    print(random.randint(1, 10))
```

_Note: don't overwrite module names like os, sys, random, etc._

Alternative form:

```python
from random import *
```

Importing multiple modules:

```python
import random, sys, os, math
```


