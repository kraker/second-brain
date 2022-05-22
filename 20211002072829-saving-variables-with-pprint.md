---
title: Saving Variables With pprint.pformat() Function
date: 2021-10-02 07:28
tags:
- 'python'
---

You can use pprint.pformat() to return a string that can be stored in a `.py`
file and will be syntactically correct.

```python
i>>> import pprint
i>>> cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
i>>> pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
i>>> fileObj = open('myCats.py', 'w')
i>>> fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
83
i>>> fileObj.close()
i>>> import myCats
i>>> myCats.cats
[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]
i>>> myCats.cats[0]
{'desc': 'chubby', 'name': 'Zophie'}
i>>> myCats.cats[0]['name']
'Zophie'
```

Only basic data types such as integers, floats, strings, lists, and dictionaries
can be written to a file as simple text.
