---
title: systemd-journald
date: 2024-10-02 16:40:45 -05:00
tags:
- 'sysadmin'
- 'linux'
modified: 2025-07-28 21:26:11 -05:00
---

# systemd-journald

Writes system logging to a binary file. By default only logs since the last boot.

## journalctl

Most useful journalctl options:

| Option | Use                                                  |
| ------ | ---------------------------------------------------- |
| -f     | Follow the end of journal in real-time, like tail -f |
| -b     | Show the boot logs                                   |
| -x     | Explain each log entry in detail                     |
| -u     | Filter logs for a specific systemd unit              |
| -p     | Filter logs for messages with a specific priority    |
| -e     | Go to end of logs                                    |

## Conf

Systemd-journald conf: `/etc/systemd/journald.conf`

### Configure persistent journal logging

From `man systemd-journald`:

> The journal service stores log data either persistently below /var/log/journal or in a
> volatile way below /run/log/journal/ (in the latter case it is lost at reboot). By
> default, log data is stored persistently if /var/log/journal/ exists during boot

> On systems where /var/log/journal/ does not exist yet but where persistent logging is
> desired (and the default journald.conf is used), it is sufficient to create the
> directory, and ensure it has the correct access modes and ownership:

```bash
mkdir -p /var/log/journal
systemd-tmpfiles --create --prefix /var/log/journal
```

Then switch to persistent logging with:

```bash
journalctl --flush
# or
systemctl restart systemd-journald
```

# See also

* [202405130914-logger](202405130914-logger.md)
