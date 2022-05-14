---
title: Deploying My Second Brain
date: 2021-09-05 13:32
tags:
- #webdev
- #zettelkasten
---

1. Navigate to docroot for dev site
  + Right now that's `~/Public/notes.alexkraker.net`
2. Build site

```bash
hugo
```
3. Copy `public` directory to my server:

```bash
rsync -azvP -e 'ssh -p 36' \
/home/akraker/public/second-brain/public/ \
alexkr@server.alexkraker.net:~/notes.alexkraker.net
```
That's it!

4. URL: [notes.alexkraker.net](http://notes.alexkraker.net)

## gitlab repo

I have a private gitlab repo I push this project to:
* https://gitlab.com/akraker/second-brain
  + _It's probably best not to have this public since I have notes here that could
    be considered sensitive for work._

## Hugo site development

I have my repo configured to use "uglyURLs" since I believe these are more
future proof. See the `config.yml` in the project root.
