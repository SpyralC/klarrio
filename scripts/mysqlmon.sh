#!/bin/bash

# Check if MySQL is running
sudo service mysql status > /dev/null 2>&1

# Restart the MySQL service if it's not running.
if [ $? != 0 ]; then
    echo -e "MySQL Service was down. Restarting now...\n"
    sudo service mysql restart
else
    echo -e "MySQL Service is running already. Nothing to do here.\n"
fi