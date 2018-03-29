#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Sixzeroo
# website: www.liuin.cn

import requests
import json,redis
from lxml import etree
try:
    import cookielib
except:
    import http.cookiejar as cookielib

try:
    from github.config import GITHUBACCOUNT,REDIS_HOST,REDIS_PORT,REDIS_COOKIE,REDIS_COOKIE_INFO
except :
    from config import GITHUBACCOUNT,REDIS_HOST,REDIS_PORT,REDIS_COOKIE,REDIS_COOKIE_INFO

BASE_URL = 'https://github.com/login'
LOGIN_URL = 'https://github.com/session'
SESSION = requests.session()


class GithubLogin(object):

    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url ='https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'

        self.session = requests.session()
        self.session.cookies = cookielib.LWPCookieJar(filename='github_cookie')


    def get_param(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        field_one = str(selector.xpath('//*[@name="authenticity_token"]/@value')[0])
        print(field_one)
        return field_one


    def post_param(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.get_param(),
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        return response.cookies.get_dict()


def get_login_cookie(name, passwd):
    githublogin = GithubLogin()
    cookies = githublogin.post_param(name, passwd)
    res = {
        'key': name,
        'value': json.dumps(cookies)
    }
    return res

# 初始化cookies以及使用次数
def init_cookie(account=GITHUBACCOUNT):
    client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=3)
    for i in account:
        cookie = get_login_cookie(i[0], i[1])
        if(client.hset(REDIS_COOKIE, cookie['key'], cookie['value']) == 1):
            print("user %s cookie set"%i[0])
        else:
            print("user %s cookie update"%i[0])

if __name__ == '__main__':
    init_cookie(GITHUBACCOUNT)
