#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Sixzeroo
# website: www.liuin.cn

import sys,re,csv
from pymongo import MongoClient

from config import *
from keywordlist import *
from utils import *

GithubBaseUrl = "https://github.com/"

class User(object):

    def __init__(self):
        self.db = MongoClient(MONGODB_HOST, MONGODB_PORT)[MONGODB_DB]
        self.data = self.db['user']
        self.testdb = MongoClient(MONGODB_HOST, MONGODB_PORT)["Test"]
        self.chinadata = self.testdb['user']
        self.file = open('./user.md', 'w')
        self.csvfile = open("result.csv", "w")
        self.csv = csv.writer(self.csvfile)

    def __del__(self):
        self.file.close()
        self.csvfile.close()

    # 打印排行
    def printOut(self, res):
        self.file.write("| Avatar | User | Repos | Stars | Followers | Following | Contributions|\n")
        self.file.write("|--------|------|-------|-------|-----------|-----------|-----------|\n")
        for user in res:
            self.file.write("|![](%s) | https://github.com/%s  |   %s | %s | %s | %s | %s |\n" % (user['avatar_url'],
                                                                                                  user['user_id'],
                                                                                                  user['reps_num'],
                                                                                                  user['stars_num'],
                                                                                                  user['followers_num'],
                                                                                                  user['following_num'],
                                                                                                  user['contr_num']))
    def followersRank(self, rank=10):
        res = self.data.find().sort('followers_num',-1).limit(rank)
        # 打印当前函数名
        self.file.write(sys._getframe().f_code.co_name + '\n')
        self.printOut(res)


    def followingRank(self, rank=10):
        res = self.data.find().sort('following_num',-1).limit(rank)
        self.file.write(sys._getframe().f_code.co_name + '\n')
        self.printOut(res)

    def starsRank(self, rank=10):
        res = self.data.find().sort('stars_num',-1).limit(rank)
        self.file.write(sys._getframe().f_code.co_name + '\n')
        self.printOut(res)


    def repsRank(self, rank=10):
        res = self.data.find().sort('reps_num', -1).limit(rank)
        self.file.write(sys._getframe().f_code.co_name + '\n')
        self.printOut(res)


    # 生成贡献排行
    def contriRank(self, rank = 10):
        res = self.data.find().sort('contr_num', -1).limit(rank)
        self.file.write(sys._getframe().f_code.co_name + '\n')
        self.printOut(res)


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
        # dict 中按照value排序
        info = sorted(resdict.items(), key=lambda d:d[1], reverse=True)[:int(nums/20)]
        for i in info:
            print(i[0]+' '+str(i[1]))
        return info


    # 选取认为是中国地区账号拉入新表中
    def selectChinaUser(self):
        users = self.data.find()
        for user in users:
            location = user['location']
            if location is not None:
                location = location.lower()
                splited = re.split('[, ]+', location)
                for i in splited:
                    if i in CHINA_KEYWORD:
                        self.chinadata.insert(user)
                        print("完成%s用户复制"%user['user_id'])
                        break


    # 获取个人网站顶级域名使用情况
    def getSiteDomainInfo(self, limit = None):
        '''
        统计数据库中的域名信息
        :return: 各种统计域名的tuple 数组
        '''
        if limit is not None:
            users = self.data.find().limit(limit)
        else:
            users = self.data.find()
        top_domain_dict = {}
        sum_num = 0
        for user in users:
            url = user['url']
            if url is not None:
                domain = parseDomain(url)
                # 排除github.io
                if(domain == -1):
                    continue
                sum_num = sum_num + 1
                if domain in top_domain_dict:
                    top_domain_dict[domain] = top_domain_dict[domain] + 1
                else:
                    top_domain_dict[domain] = 1
        top_domain_info =sorted(top_domain_dict.items(), key=lambda d: d[1], reverse=True)
        self.csv.writerow(['domain', 'num'])
        for domain in top_domain_info[:10]:
            self.csv.writerow([domain[0], str(domain[1])])
            sum_num = sum_num - domain[1]
        self.csv.writerow(['others', sum_num])
        return top_domain_info


    # 获取个人邮箱统计情况
    def getEmailInfo(self, limit = None):
        '''
        统计数据库中的个人邮箱信息
        :return: 包含邮箱和频数的dict
        '''
        if limit is not None:
            users = self.data.find().limit(limit)
        else:
            users = self.data.find()
        email_dict = {}
        sum_num = 0
        for user in users:
            email = user['email']
            if email is None:
                continue
            try:
                email = re.split('@', email)[1]
            except IndexError:
                continue
            sum_num = sum_num + 1
            if email in email_dict:
                email_dict[email] = email_dict[email] + 1
            else:
                email_dict[email] = 1
        email_info = sorted(email_dict.items(), key= lambda d: d[1], reverse=True)
        self.csv.writerow(['email', 'num'])
        for email in email_info[:10]:
            self.csv.writerow([email[0], str(email[1])])
            sum_num = sum_num - email[1]
        self.csv.writerow(['others', str(sum_num)])
        return email_info


    # 统计各个公司人数
    def getCompanyInfo(self, limit = None):
        if limit is not None:
            users = self.data.find().limit(limit)
        else:
            users = self.data.find()
        company_dict = {}
        for user in users:
            company_list = user['company']
            if len(company_list) == 0:
                continue
            for company in company_list:
                company = company.lower()
                company = company[1:]
                if company in company_dict:
                    company_dict[company] = company_dict[company] + 1
                else:
                    company_dict[company] = 1
        company_info = sorted(company_dict.items(), key= lambda d: d[1], reverse=True)
        self.csv.writerow(['company', 'num'])
        for company in company_info[:100]:
            self.csv.writerow([company[0], str(company[1])])
        return company_info


    # TODO: 统计某公司内的location信息
    def getLocationInfoByCompany(self):
        pass


    # TODO: 统计个人介绍
    def getIntroInfo(self):
        pass


class ChinaUser(User):

    def __init__(self):
        self.db = MongoClient(MONGODB_HOST, MONGODB_PORT)["Test"]
        self.data = self.db['user']
        self.file = open('./chinauser.md', 'w')

    def __del__(self):
        try:
            self.file.close()
        except AttributeError:
            pass


if __name__ == '__main__':
    test = User()
    test.getCompanyInfo()
