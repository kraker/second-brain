---
title: Saving Variables
date: 2021-10-02 07:13
tags:
- #python
---

Variables can be saved or made to persist after the program has closed with the
**shelve module**. 

```python
i>>> import shelve
i>>> shelfFile = shelve.open('mydata')
i>>> cats = ['Zophie', 'Pooka', 'Simon']
i>>> shelfFile['cats'] = cats
i>>> shelfFile.close()
i>>> shelfFile = shelve.open('mydata')
i>>> type(shelfFile)
<class 'shelve.DbfilenameShelf'>
i>>> shelfFile['cats']
['Zophie', 'Pooka', 'Simon']
i>>> shelfFile.close()
```

Shelf files are like [dictionaries](20210923051842-dictionary-data-type.md) and
use _keys()_ and _values()_ to return keys and values.

```python
i>>> shelfFile = shelve.open('mydata')
i>>> list(shelfFile.keys())
['cats']
i>>> list(shelfFile.values())
[['Zophie', 'Pooka', 'Simon']]
i>>> shelfFile.close()
```
