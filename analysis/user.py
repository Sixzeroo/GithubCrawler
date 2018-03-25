#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Sixzeroo
# website: www.liuin.cn

import sys,re
from pymongo import MongoClient

from config import *
from keywordlist import *

GithubBaseUrl = "https://github.com/"

class User(object):

    def __init__(self):
        self.db = MongoClient(MONGODB_HOST, MONGODB_PORT)[MONGODB_DB]
        self.testdb = MongoClient(MONGODB_HOST, MONGODB_PORT)["Test"]
        self.chinadata = self.testdb['user']
        self.data = self.db['user']
        self.file = open('./user.md', 'w')

    def __del__(self):
        self.file.close()

    def followersRank(self, rank=10):
        res = self.data.find().sort('followers_num',-1).limit(rank)
        # 打印当前函数名
        self.file.write(sys._getframe().f_code.co_name+'\n')
        self.file.write("| Avatar | User | Repos | Stars | Followers | Following |\n")
        self.file.write("|--------|------|-------|-------|-----------|-----------|\n")
        for user in res:
            self.file.write("|![](%s) | https://github.com/%s  |   %s | %s | %s | %s |\n"%(user['avatar_url'],
                                                                                user['user_id'],
                                                                                user['reps_num'],
                                                                                user['stars_num'],
                                                                                user['followers_num'],
                                                                                user['following_num']))

    def followingRank(self, rank=10):
        res = self.data.find().sort('following_num',-1).limit(rank)
        self.file.write(sys._getframe().f_code.co_name + '\n')
        self.file.write("| Avatar | User | Repos | Stars | Followers | Following |\n")
        self.file.write("|--------|------|-------|-------|-----------|-----------|\n")
        for user in res:
            self.file.write("|![](%s) | https://github.com/%s  |   %s | %s | %s | %s |\n"%(user['avatar_url'],
                                                                                user['user_id'],
                                                                                user['reps_num'],
                                                                                user['stars_num'],
                                                                                user['followers_num'],
                                                                                user['following_num']))

    def starsRank(self, rank=10):
        res = self.data.find().sort('stars_num',-1).limit(rank)
        self.file.write(sys._getframe().f_code.co_name + '\n')
        self.file.write("| Avatar | User | Repos | Stars | Followers | Following |\n")
        self.file.write("|--------|------|-------|-------|-----------|-----------|\n")
        for user in res:
            self.file.write("|![](%s) | https://github.com/%s  |   %s | %s | %s | %s |\n"%(user['avatar_url'],
                                                                                user['user_id'],
                                                                                user['reps_num'],
                                                                                user['stars_num'],
                                                                                user['followers_num'],
                                                                                user['following_num']))

    def repsRank(self, rank=10):
        res = self.data.find().sort('reps_num', -1).limit(rank)
        self.file.write(sys._getframe().f_code.co_name + '\n')
        self.file.write("| Avatar | User | Repos | Stars | Followers | Following |\n")
        self.file.write("|--------|------|-------|-------|-----------|-----------|\n")
        for user in res:
            self.file.write("|![](%s) | https://github.com/%s  |   %s | %s | %s | %s |\n" % (user['avatar_url'],
                                                                                  user['user_id'],
                                                                                  user['reps_num'],
                                                                                  user['stars_num'],
                                                                                  user['followers_num'],
                                                                                  user['following_num']))

    # 获取所在位置关键词统计，返回排序以后的list
    def getLocationKeywordsInfo(self, nums=100):
        res = self.data.find().limit(nums)
        resdict = {}
        for user in res:
            location = user['location']
            if location is not None:
                location = location.lower()
                splited = re.split('[, ]+', location)
                for i in splited:
                    if i in resdict :
                        resdict[i] = resdict[i] + 1
                    else:
                        resdict[i] = 1
        info = sorted(resdict.items(), key=lambda d:d[1], reverse=True)[:int(nums/20)]
        for i in info:
            print(i[0]+' '+str(i[1]))
        return info

    # 选取认为是中国地区账号拉入新表中
    def selectChinaUser(self):
        users = self.data.find().limit(10000)
        for user in users:
            location = user['location']
            if location is not None:
                location = location.lower()
                splited = re.split('[, ]+', location)
                for i in splited:
                    if i in CHINA_KEYWORD:
                        self.chinadata.insert(user)
                        break



if __name__ == '__main__':
    test = User()
    test.selectChinaUser()