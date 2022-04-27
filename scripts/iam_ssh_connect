#!/bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install ec2-instance-connect


aws iam create-policy --policy-name ec2-iam-ssh-policy --policy-document file://iamssh.json

aws iam attach-user-policy --policy-arn arn:aws:iam::045524232087:policy/ec2-iam-ssh-policy --user-name klarrio

ssh-keygen -t rsa -f my_key

aws ec2-instance-connect send-ssh-public-key \
    --instance-id i-0e42b00269c28164f \
    --instance-os-user klarrio \
    --ssh-public-key file://my_key.pub

ssh -o "IdentitiesOnly=yes" -i my_key klarrio@ec2-52-64-47-124.ap-southeast-2.compute.amazonaws.com