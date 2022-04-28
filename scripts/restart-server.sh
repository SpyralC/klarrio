#!/bin/bash

sudo systemctl daemon-reload
sudo systemctl start klarrio
sudo systemctl enable klarrio

sudo systemctl restart nginx

sudo service mysql restart
sudo kill -9 `sudo lsof -t -i:5000`