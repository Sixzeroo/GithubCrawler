#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Sixzeroo
# website: www.liuin.cn

from pymongo import MongoClient

from config import *

GithubBaseUrl = "https://github.com/"

class User(object):

    def __init__(self):
        self.db = MongoClient(MONGODB_HOST, MONGODB_PORT)[MONGODB_DB]
        self.data = self.db['user']

    def followersRank(self, rank=10):
        res = self.data.find().sort('followers_num',-1).limit(rank)
        print("| Avatar | User | Repos | Stars | Followers | Following |")
        print("|--------|------|-------|-------|-----------|-----------|")
        for user in res:
            print("|![](%s]) | https://github.com/%s  |   %s | %s | %s | %s |"%(user['avatar_url'],
                                                                                user['user_id'],
                                                                                user['reps_num'],
                                                                                user['stars_num'],
                                                                                user['followers_num'],
                                                                                user['following_num']))

    def repsRank(self, rank=10):
        res = self.data.find().sort('reps', -1).limit(rank)
        print("| Avatar | User | Repos | Stars | Followers | Following |")
        print("|--------|------|-------|-------|-----------|-----------|")
        for user in res:
            print("|![](%s]) | https://github.com/%s  |   %s | %s | %s | %s |" % (user['avatar_url'],
                                                                                  user['user_id'],
                                                                                  user['reps_num'],
                                                                                  user['stars_num'],
                                                                                  user['followers_num'],
                                                                                  user['following_num']))


if __name__ == '__main__':
    test = User()
    test.repsRank()