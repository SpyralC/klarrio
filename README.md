# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* This repository is for a technical exercise to write a web form application which allows users to submit pairs of name and age to the database.

### Summary ###

* The main program is written with the flask framework, Python3.9. Flask provides a package named flask_wtf, which allows me to write a form validation easily. I also add CSRF Protect to the application.
* The database I use is MySQL Ver 8.0.28. I create a localhost user 'jimmy' with necessary privileges. There is no user-login table now, so anyone can write to the database.
* Dependencies are shown in requirements.txt
* I use gunicorn and nginx to expose the application to the internet.
* I write a MySQL auto restart script named 'mysqlmon.sh' and add it to contrab, so the application can restart successfully when the database is down or the ec2 instance is rebooted.
* I wirte a script named 'get-metrics.sh' to get metrics.
* I create an IAM user and grant permission to allow it to push ssh keys to the ec2 instance. The ttl of the key is 1 minute. Then we can ssh to the instance with customized keys.
