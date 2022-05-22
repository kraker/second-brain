---
title: In Place Upgrade Ubuntu
date: 2021-11-02 09:11
tags:
- work
---

In-place upgrades aren't recommended for production systems. This could result
in a less stable system and/or cause applications to break. 

Ideally a test system running the newer OS is setup and applications are tested
there. Or a new system is stood-up and applications/data is migrated over with
testing along the way.

Sometimes the customer chooses an in-place upgrade anyways...

## In-Place Upgrade Ubuntu 14.* LTS -> 18.*

### Resources

* <https://www.digitalocean.com/community/tutorials/how-to-upgrade-to-ubuntu-18-04>
* <https://www.cyberciti.biz/faq/ubuntu-bash-do-release-upgrade-command-not-found/>

### Upgrade

_Note: must be run as root, or with `sudo`_

1. Take a snapshot
2. Optional but recommended: Make sure data on system is backed up, or customer
   has backups. Disclaimer, data loss can occur. Backups are strongly
   recommended.
3. Run system updates:

```bash
apt-get update
apt-get upgrade
apt-get dist-upgrade
reboot
```

4. On our containers `do-upgrade-release` isn't installed by default, so install
   it:

```bash
apt install ubuntu-release-upgrader-core
```

5. Run upgrader:

```bash
do-upgrade-release
```

Use best judgement for prompts or keep defaults.

6. Verify upgrade completed successfully:

```bash
uname -a
uname -mrs
lsb_release -a
```
