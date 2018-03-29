#!/bin/bash

sudo docker run -v ./github : /code --name github_cookie_update sixzeroo/github_crawler:0.1 "yacron -c crontab.yaml"
