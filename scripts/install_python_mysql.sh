#!/bin/bash
# git clone
ssh-keygen -o
cat /home/ubuntu/.ssh/id_rsa.pub
# then add shh key to github, restart terminal
git clone git@github.com:SpyralC/klarrio.git

#   install python3.9
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9 -y
python3.9 --version

#   set python3.9 as default
cd /usr/bin
sudo su
ls -lrth python*
unlink python
ln -s /usr/bin/python3.9 python
unlink python3
ln -s /usr/bin/python3.9 python3
python --version
exit

#   install pip for python3.9
sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py

#   reinstall python3-apt
sudo apt remove python3-apt -y
sudo apt autoclean
sudo apt install python3-apt

#   install python3.9-venv
sudo apt-get install python3.9-venv
cd /home/ubuntu/klarrio
python3.9 -m venv venv1
source venv1/bin/activate


#   install mysql
sudo apt update
sudo apt install mysql-server -y
sudo systemctl start mysql.service
sudo mysql_secure_installation

#   create mysql user and database
sudo mysql
CREATE USER 'jimmy'@'localhost' IDENTIFIED BY '741111.As';
#DROP USER 'jimmy'@'localhost';
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT on *.* TO 'jimmy'@'localhost' WITH GRANT OPTION;

create database klarrio;
use klarrio
create table peopleAge (id int not null auto_increment, name varchar(50), age int, primary key (id));
quit

# then add database and table to mysql
create database klarrio;
use klarrio
CREATE TABLE peopleAge (id int auto_increment, name VARCHAR(20), age int(3), primary key(id));

# make sure mysql will be restarted
sudo nano /home/ubuntu/klarrio/scripts/mysqlmon.sh
sudo chmod +x /home/ubuntu/klarrio/scripts/mysqlmon.sh
# To test the cript, let's stop mysql and try this bash
# sudo service mysql stop
# sudo /home/ubuntu/klarrio/scripts/mysqlmon.sh

# Add the MySQL Auto Restart Script to Crontab
sudo crontab -e
# Choose nano. In crontab, add the following line to the bottom of the file.
# * * * * * /home/ubuntu/klarrio/scripts/mysqlmon.sh > /dev/null 2>&1

# monitor metrics script
chmod -x /home/ubuntu/klarrio/scripts/get-metrics.sh
sh /home/ubuntu/klarrio/scripts/get-metrics.sh

#   install flask app dependencies
sudo apt update 
source venv1/bin/activate
pip3 install -r requirements.txt

#   test app
python wsgi.py

#   Done