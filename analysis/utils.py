#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Sixzeroo
# website: www.liuin.cn

import re

# TODO: 域名解析

def parseDomain(url):
    '''
    解析domain，返回顶级域名
    :param domain: url（str）
    :return: 顶级域名（str）
    '''
    url = url.lower()
    try:
        domain = re.split('//', url)[1]
        domain = re.split('/', domain)[0]
        top_domain = re.split('\.', domain)[-1]
    except:
        return -1
    # 排除github.io
    if(top_domain == 'io' and re.split('\.', domain)[-2] == 'github'):
        return -1
    return top_domain