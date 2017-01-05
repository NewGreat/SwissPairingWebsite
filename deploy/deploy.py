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
subprocess.check_call("yum -y install MariaDB-server MariaDB-client", shell=True)
#Starts and enables the service for MariaDB
subprocess.check_call("systemctl start mariadb", shell=True)
subprocess.check_call("systemctl enable mariadb", shell=True)

#connects to MariaDB

#Secures the database by running the commands in the mysql_secure_instalation script manually

#creates the players database

#creates the players.players table

#creates the players.history table

#creates the models database

#creates the models.models table

#creates the tournaments database

#creates the tournaments.tournament sample table

#creates the tournaments.tables table

#creates the tournaments.scenarios table


