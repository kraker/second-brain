---
title: Migrations And Upgrades
date: 2021-09-24 09:01
tags:
- #work
---

## Checklist

- [ ] Same PHP versions?
- [ ] All sites that worked on old server work on new server?

`hostsfilemods --all`

```bash
for site in $(grep 199.250 /etc/hosts | awk '{print $2}'); do 
    xdg-open http://$site 
done
```

- [ ] Configure **WHM >> Backup Configuration**, same as on old server?

```bash
whmapi1 --output=jsonpretty backup_config_get
```

```
/var/cpanel/backups/config
```

- [ ] PHP-FPM configs?
- [ ] Apache Configs?
- [ ] Nginx Configs?
