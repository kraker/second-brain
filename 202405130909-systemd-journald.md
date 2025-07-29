---
title: systemd-journald
date: 2024-10-02 16:40:45 -05:00
tags:
- 'sysadmin'
- 'linux'
modified: 2025-07-28 20:09:24 -05:00
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

# See also

* [202405130914-logger](202405130914-logger.md)
