---
categories: [Programming]
date: 2019-04-07
keywords: [engine, xxx, aws, server, overflow, enable, performance, connect, instance,
  high]
lang: en
recommendations: [/note/hello-faust/, /note/hivemall-events-2018-autumn/, /note/data-leaders-summit-europe-2019/]
title: TokuDB in MariaDB (on Ubuntu)
---

[TokuDB](https://github.com/percona/tokudb-engine) is a high-performance, scalable storage engine for MySQL/MariaDB. Since the engine is optimized for a large volume of data, nowadays it would become a reasonable option to build an in-house big data analytics solution.

As the first step toward making sure its effectiveness and efficiency, I simply tried to enable the storage engine in MariaDB running on an AWS EC2 instance. Let me share the whole procedure so that everyone can easily deep-dive into TokuDB itself, rather than some troublesome chores.

First, create an AWS EC2 instance with a security group that accepts `port=3306` inbound request, and install the components as:

```sh
sudo apt-get update
sudo apt-get install mariadb-server mariadb-plugin-tokudb
```

Second, un-comment `plugin-load-add` in `/etc/mysql/mariadb.conf.d/tokudb.cnf`:

```yml
[mariadb]
# See https://mariadb.com/kb/en/how-to-enable-tokudb-in-mariadb/
# for instructions how to enable TokuDB
#
# See https://mariadb.com/kb/en/tokudb-differences/ for differences
# between TokuDB in MariaDB and TokuDB from http://www.tokutek.com/

plugin-load-add=ha_tokudb.so
```

Meanwhile, update `bind-address` configured in `/etc/mysql/mariadb.conf.d/50-server.cnf` as follows:

```yml
# this is read by the standalone daemon and embedded servers
[server]

# this is only for the mysqld standalone daemon
[mysqld]

#
# * Basic Settings
#
user            = mysql
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
port            = 3306
basedir         = /usr
datadir         = /var/lib/mysql
tmpdir          = /tmp
lc-messages-dir = /usr/share/mysql
skip-external-locking

# Instead of skip-networking the default is now to listen only on
# localhost which is more compatible and is not less secure.
bind-address            = 0.0.0.0
```

Run the server:

```sh
# https://support.rackspace.com/how-to/installing-mysql-server-on-ubuntu/
# sudo ufw allow mysql
sudo systemctl restart mysql
sudo mysql
```

Next, create a user in the MySQL console:

```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' WITH GRANT OPTION;
CREATE USER 'username'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'username'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

Create and see a dummy table with the TokuDB engine:

```sql
create database foo;
use foo;

CREATE TABLE sample_tokudb (
  id int NOT NULL AUTO_INCREMENT,
  name varchar(128),
  age integer,
  PRIMARY KEY (id)
) ENGINE=TokuDB;

INSERT INTO sample_tokudb (name, age) VALUES ('Joe', 28);
INSERT INTO sample_tokudb (name, age) VALUES ('Katie', 30);
INSERT INTO sample_tokudb (name, age) VALUES ('Tom', 26);

-- make sure if it's created with the TokuDB engine
SHOW TABLE STATUS WHERE Name = 'sample_tokudb';
```

Finally, we can remotely connect to a TokuDB-enabled table hosted by the MariaDB server:

```sh
mysql -u username -h $EC2_HOST -d sample_tokudb -p
```

We are now ready to play with the high-performance storage engine.

### References

- [Enabling TokuDB engine in MariaDB](http://www.bictor.com/2015/07/19/enabling-tokudb-engine-in-mariadb/)
- [Connect to mysql on Amazon EC2 from a remote server - Stack Overflow](https://stackoverflow.com/questions/9766014/connect-to-mysql-on-amazon-ec2-from-a-remote-server)
- [Host 'xxx.xx.xxx.xxx' is not allowed to connect to this MySQL server - Stack Overflow](https://stackoverflow.com/questions/1559955/host-xxx-xx-xxx-xxx-is-not-allowed-to-connect-to-this-mysql-server)
- [How Do I Enable Remote Access To MySQL Database Server?](https://www.cyberciti.biz/tips/how-do-i-enable-remote-access-to-mysql-database-server.html)