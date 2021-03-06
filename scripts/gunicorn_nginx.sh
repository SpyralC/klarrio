#!/bin/bash   
#   configure gunicorn & systemd

pip install gunicorn
pip install cryptography 

gunicorn -b 0.0.0.0:5000 wsgi:app &
sudo cp /home/ubuntu/klarrio/configs/klarrio.service /etc/systemd/system/klarrio.service

sudo systemctl daemon-reload
sudo systemctl start klarrio
sudo systemctl enable klarrio

#curl localhost:5000

#   Nginx Webserver

sudo apt-get install nginx -y

sudo systemctl start nginx
sudo systemctl enable nginx

sudo cp /home/ubuntu/klarrio/configs/default /etc/nginx/sites-available/default
sudo systemctl restart nginx