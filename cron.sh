#!/bin/bash

sudo docker run -v /home/ubuntu/github_crawler/github:/code -d --name github_cookie_update sixzeroo/github_crawler:0.1 bash -c 'yacron -c crontab.yaml'
