---
title: Install Elasticsearch
date: 2021-10-15T12:38:00Z
tags:
- 'work'
---

## Resources

* [Install Elasticsearch 7.15 with RPM][1]

[1]: https://www.elastic.co/guide/en/elasticsearch/reference/7.15/rpm.html

## Installation

As of this writing latest version is 7.15. This is how to install the latest
version.  For installation of previous versions, see the official docs.

Elasticsearch ships with a bundled version of OpenJDK, so it's no longer
necessary to install this separately (unless you want to).

### Import the Elasticsearch GPG Key

```bash
rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
```

### Installing from the RPM repository

Create the following file:

```bash
touch /etc/yum.repos.d/elasticsearch.repo
```

Add the following to the file:

```bash
cat > /etc/yum.repos.d/elasticsearch.repo << EOF
[elasticsearch]
name=Elasticsearch repository for 7.x packages
baseurl=https://artifacts.elastic.co/packages/7.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=0
autorefresh=1
type=rpm-md
EOF
```

Note, this sets up the Elasticsearch repository for whatever the latest version
of _7.x_ is.  If a newer version of ES has been released, that will be
installed instead of v7.15.

Install using `yum`:

```bash
yum install --enablerepo=elasticsearch elasticsearch
```

### Run and enable Elasticsearch with systemd

```bash
systemctl daemon-reload
systemctl enable elasticsearch
systemctl start elasticsearch
```

### Check that Elasticsearch is running

```bash
curl -X GET "localhost:9200"
```

Example:

```bash
[root@server:/]$ curl -X GET "localhost:9200"
{
  "name" : "server.alexkraker.net",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "OYADWA3AR6y6hYSZD72-FA",
  "version" : {
    "number" : "7.15.1",
    "build_flavor" : "default",
    "build_type" : "rpm",
    "build_hash" : "83c34f456ae29d60e94d886e455e6a3409bba9ed",
    "build_date" : "2021-10-07T21:56:19.031608185Z",
    "build_snapshot" : false,
    "lucene_version" : "8.9.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```


