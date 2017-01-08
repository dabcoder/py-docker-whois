#!/bin/bash

sudo docker stop $(docker ps -a -q)
sudo docker rm $(docker ps -a -q)

sudo docker build -t my_application_img .
sudo docker run -d -p 80:80 my_application_img

