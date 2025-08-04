---
title: Deploying My Blog
date: 2021-09-05T18:41:00Z
tags:
---

Build the site with 
```bash
hugo
```

Deploy to my server with:
```bash
rsync -azvP -e 'ssh -p 36' \
/home/akraker/Public/alexkraker.com/public/ \
kraker@server.alexkraker.net:~/alexkraker.com
```

## git repo

I have a git repo I push this project to:
https://github.com/kraker/alexkraker.com
