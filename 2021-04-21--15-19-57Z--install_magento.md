---
title: Install Magento
date: 2021-04-21 15:19
---

[Official Docs](https://docs.magento.com/user-guide/magento/installation.html)
[Other official docs](https://devdocs.magento.com/guides/v2.4/install-gde/install-flow-diagram.html)

## Installation

1. [Check System Requirements](https://devdocs.magento.com/guides/v2.4/install-gde/system-requirements.html?_ga=2.166245821.2031650980.1619039800-254307176.1619039800)
2. [Install Elasticsearch](2021-04-21--15-25-23Z--install_elasticsearch.md) 
3. Prerequisite check
	 + https://devdocs.magento.com/guides/v2.4/install-gde/prereq/prereq-overview.html?_ga=2.212551060.1841983948.1624978202-1797079552.1624639640
	 + `httpd -v`
	 + mysql --version
4. [Install Composer](2021-06-29--08-55-27Z--install_composer.md) using version for compatibility with system
```
wget https://getcomposer.org/installer -O composer-setup.php

php -r "if (hash_file('sha384', 'composer-setup.php') === '756890a4488ce9024fc62c56153228907f1545c228516cbf63f885e036d37e9a59d27d63f46af1d4d07ee0f76181c7d3') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"

php -d allow_url_fopen=On composer-setup.php --filename=composer
```
5. Run updoots
	 + `yum update`

7. Install database
```
(
user=$(whoami)
read -p "Database Name: " db
uapi Mysql create_database name="${user}_${db}"
pass=$(head /dev/urandom | tr -dc _A-Z-a-z-0-9 | head -c15)
uapi Mysql create_user name="${user}_${db}" password="$pass"
uapi Mysql set_privileges_on_database user="${user}_${db}" database="${user}_${db}" privileges='ALL PRIVILEGES'
uapi Mysql get_privileges_on_database user="${user}_${db}" database="${user}_${db}" | grep 'ALL PRIVILEGES'
echo $pass
echo "${user}_${db}"
)
```

8. Get authentication keys to the Magento Composer repo
	 + https://devdocs.magento.com/guides/v2.4/install-gde/prereq/connect-auth.html

9. Directory must be empty to install repo
	 + Move composer out of the way `mv ./composer ../composer`
	 + Make sure you're in the docroot and run `rm -rf ./*`
10. Install repo:
```
 composer create-project --repository-url=https://repo.magento.com/ magento/project-community-edition <install-directory-name>
```
11. You might need to [install libsodium](2021-06-29--11-18-05Z--install_libsodium.md) before installing the Magento app
12. Install Magento App:
```
bin/magento setup:install \
--base-url=http://localhost/magento2ee \
--db-host=localhost \
--db-name=magento \
--db-user=magento \
--db-password=magento \
--admin-firstname=admin \
--admin-lastname=admin \
--admin-email=admin@admin.com \
--admin-user=admin \
--admin-password=admin123 \
--language=en_US \
--currency=USD \
--timezone=America/Chicago \
--use-rewrites=1
```

1. Optional, check for PHP modules:
```
# /usr/local/bin/ea-php74 -m | grep -E 'bcmath|ctype|curl|dom|gd|hash|iconv|intl|mbstring|openssl|pdo_mysql|simplexml|soap|xsl|zip|sockets'
bcmath
ctype
curl
dom
gd
hash
iconv
intl
mbstring
openssl
pdo_mysql
soap
sockets
xsl
zip
```
