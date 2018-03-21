#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Sixzeroo
# website: www.liuin.cn

from github.items import GitHubRepItem,GitHubUserItem

# follower、star数目记录
def strNumtoInt(input_str):
    if(type(input_str) is not str):
        return 0
    input_str = input_str.strip()
    try:
        res_num = int(input_str[:-1])*1000 if(input_str[-1] == 'k') else int(input_str)
    except ValueError:
        res_num = int(float(input_str[:-1])*1000)
    return res_num

# 给非None 类型的String 加上.strip，None类型为空字符串
def stringStrip(input_str):
    if(input_str is not  None):
        return input_str.strip()
    else:
        return ""

# 打印字典信息
def printDict(input_dict):
    print("{")
    for key in input_dict:
        print("%s: %s,"%(key, input_dict[key]))
    print("}")

# 精简图片URL
def simplifyAvaUrl(url):
    if url is None:
        return ""
    return url.split('?')[0]

def convertUserDicttoItem(user):
    github_user_item = GitHubUserItem()
    github_user_item['user_id'] = user['user_id']
    github_user_item['user_name'] = user['user_name']
    github_user_item['email'] = user['email']
    github_user_item['location'] = user['location']
    github_user_item['url'] = user['url']
    github_user_item['company'] = user['company']
    github_user_item['reps_num'] = user['reps_num']
    github_user_item['stars_num'] = user['stars_num']
    github_user_item['followers_num'] = user['followers_num']
    github_user_item['following_num'] = user['following_num']
    return github_user_item

def convertRepDicttoItem(rep):
    github_rep_item = GitHubRepItem()
    github_rep_item['user_id'] = rep['user_id']
    github_rep_item['rep_name'] = rep['rep_name']
    github_rep_item['rep_lang'] = rep['rep_lang']
    github_rep_item['commits_num'] = rep['commits_num']
    github_rep_item['forks_num'] = rep['forks_num']
    github_rep_item['stars_num'] = rep['stars_num']
    return github_rep_item