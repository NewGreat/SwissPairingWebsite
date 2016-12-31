




yum localinstall https://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm
yum install mysql-community-server
systemctl start mysqld.service
systemctl enable mysqld.service