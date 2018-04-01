#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Sixzeroo
# website: www.liuin.cn

import csv,sys

from pymongo import MongoClient

from config import *

GithubBaseUrl = "https://github.com/"

class Rep(object):

    def __init__(self):
        self.db = MongoClient(MONGODB_HOST, MONGODB_PORT)[MONGODB_DB]
        self.data = self.db['rep']
        self.file = open('./rep.md', 'w')
        self.csvfile = open("result.csv", "w")
        self.csv = csv.writer(self.csvfile)


    def __del__(self):
        self.file.close()
        self.csvfile.close()

    # 打印排行
    def printOut(self, res):
        self.file.write("| Rep | User | Language | Stars | Fork | Commit | \n")
        self.file.write("|--------|------|-------|-------|-----------|-----------|\n")
        for rep in res:
            self.file.write("|[%s](%s)|[%s](%s)|%s|%s|%s|%s|\n"%(rep['rep_id'], GithubBaseUrl+rep['rep_id'],
                                                               rep['user_id'], GithubBaseUrl+rep['user_id'],
                                                               rep['rep_lang'], rep['stars_num'], rep['forks_num'],                                                     rep['commits_num']))


    # 被收藏仓库排行
    def starsRank(self, rank=10):
        res = self.data.find({'forked': 0}).sort('stars_num', -1).limit(rank)
        # 打印当前函数名
        self.file.write(sys._getframe().f_code.co_name + '\n')
        self.printOut(res)


    # 指定语言被收藏仓库排行
    def starsLangRank(self, lang, rank=10):
        res = self.data.find({'forked': 0, 'lang': lang}).sort('stars_num', -1).limit(rank)
        # 打印当前函数名
        self.file.write(sys._getframe().f_code.co_name + '\n')
        self.printOut(res)

    # Fork排行
    def forkRank(self, rank=10):
        res = self.data.find({'forked': 0}).sort('forks_num', -1).limit(rank)
        # 打印当前函数名
        self.file.write(sys._getframe().f_code.co_name + '\n')
        self.printOut(res)

    # 指定语言被Fork排行
    def forkLangRank(self, lang, rank=10):
        res = self.data.find({'forked': 0, 'lang': lang}).sort('forks_num', -1).limit(rank)
        # 打印当前函数名
        self.file.write(sys._getframe().f_code.co_name + '\n')
        self.printOut(res)

    # 根据stars统计的语言分布情况
    def langInfoByStars(self, limit = None):
        if limit is not None:
            res = self.data.find({'forked': 0, 'stars_num': {'$gte': limit}})
        else:
            res = self.data.find({'forked': 0})
        resdict = {}
        sum_num = 0
        for rep in res:
            lang = rep['lang']
            sum_num = sum_num + 1
            if lang in resdict :
                resdict[lang] = resdict[lang] + 1
            else:
                resdict[lang] = 1
        lang_info = sorted(resdict.items(), key=lambda d:d[1], reverse=True)
        self.csv.writerow(['lang', 'num'])
        for lang in lang_info:
            self.csv.writerow([lang[0], str(lang[1])])
        return lang_info

    # 根据forked统计的语言分布情况
    def langInfoByForked(self, limit=None):
        if limit is not None:
            res = self.data.find({'forked': 0, 'forks_num': {'$gte': limit}})
        else:
            res = self.data.find({'forked': 0})
        resdict = {}
        sum_num = 0
        for rep in res:
            lang = rep['lang']
            sum_num = sum_num + 1
            if lang in resdict:
                resdict[lang] = resdict[lang] + 1
            else:
                resdict[lang] = 1
        lang_info = sorted(resdict.items(), key=lambda d: d[1], reverse=True)
        self.csv.writerow(['lang', 'num'])
        for lang in lang_info:
            self.csv.writerow([lang[0], str(lang[1])])
        return lang_info



if __name__ == '__main__':
    test = Rep()
    test.starsRank()
    test.forkRank()