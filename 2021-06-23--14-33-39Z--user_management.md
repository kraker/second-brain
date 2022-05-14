---
title: User management
date: 2021-06-23 14:33
---

* List users currently logged in: `who`
* List all existing user accounts w/properties: `passwd -Sa` (as root)
* To add a new user, use the `useradd` command:

```
# useradd -m -G {additional_groups} -s {login_shell} {username}
```

`-m/--create-home` 
the user's home directory is created as `/home/username`.

`-G/--groups`
a comma separated list of supplementary groups which the user is also a member
of.

`-s/--shell`
a path to the user's login shell.

## Example adding a user

Add a new user creating it's home directory and otherwise using all defaults:
```
# useradd -m archie
# passwd archie
```

Add a new administrative user with `sudo` powers:
```
# useradd -m -G wheel archie
# passwd archie
```

Source: https://wiki.archlinux.org/title/Users_and_groups#User_management

## Additional Resources

https://www.redhat.com/sysadmin/linux-user-account-management
