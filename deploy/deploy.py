import subprocess
import sys
import json
import sqlalchemy

#adds proper repo to install MariaDB
subprocess.check_call("""
cat << EOF > /etc/yum.repos.d/MariaDB.repo
# MariaDB 10.1 CentOS repository list - created 2017-01-05 04:38 UTC
# http://downloads.mariadb.org/mariadb/repositories/
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.1/centos7-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
EOF
""",shell=True)
#updates installed packages
subprocess.check_call("yum -y update",shell=True)
#installs MariaDB
subprocess.check_call("yum -y install MariaDB-server", shell=True)
#Starts and enables the service for MariaDB
subprocess.check_call("systemctl enable mariadb", shell=True)
subprocess.check_call("systemctl start mariadb", shell=True)

#connects to MariaDB
engine = sqlalchemy.create_engine('mysql+pymysql://root:password@10.3.1.104', pool_recycle=3600)

#Secures the database by running the commands in the mysql_secure_instalation script manually

#creates the players database
CREATE DATABASE `players` /*!40100 DEFAULT CHARACTER SET latin1 */;

#creates the players.players table
CREATE TABLE `players` (
  `id` int(11) NOT NULL DEFAULT '0',
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email_address` varchar(45) NOT NULL,
  `phone_number` varchar(45) DEFAULT NULL,
  `icon` blob,
  PRIMARY KEY (`id`),
  UNIQUE KEY `player_id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='player information table';
#creates the players.history table
#this should be a view based on the tournaments table

#creates the models database
CREATE DATABASE `models` /*!40100 DEFAULT CHARACTER SET latin1 */;

#creates the models.models table
CREATE TABLE `models` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `point_cost` int(11) NOT NULL,
  `Faction` varchar(45) NOT NULL,
  `type` varchar(45) NOT NULL,
  `image` blob,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
#creates the tournaments database

#creates the tournaments.tournament sample table

#creates the tournaments.tables table

#creates the tournaments.scenarios table


