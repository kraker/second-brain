---
title: Install Python 2.x
date: 2021-07-15 14:55
---

# Installing legacy Python 2.x

The last release of Python 2 is 2.7.18. Download url: https://www.python.org/downloads/release/python-2718/

## Install

```bash
wget https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz
tar xvzf Python-2.7.18.tgz
cd Python-2.7.18/
./configure
make
make altinstall
```

### Install pip

```bash
python2.7 -m ensurepip --upgrade
```

## Install Python 2.6

Not sure why anyone would need to do this anymore...

https://ask.puppet.com/question/32558/how-do-i-install-python-26x-on-a-centos-7-machine-using-puppetyumepel/
