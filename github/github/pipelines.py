# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient,DESCENDING,IndexModel
from pymongo.errors import DuplicateKeyError
import redis
from scrapy.exceptions import DropItem

from github.config import *
from github.items import GitHubRepItem,GitHubUserItem


# MongDB 存储数据
class GithubPipeline(object):

    def __init__(self):
        # MongoDB
        client = MongoClient(MONGODB_SERVER,
                             MONGODB_PORT)
        db = client[MONGODB_DB]
        self.collection1 = db['user']
        # 建立唯一降序索引，实现数据库端去重
        self.collection1.create_index([("user_id",DESCENDING)], unique=True)
        index1 = IndexModel([('stars_num',DESCENDING)])
        index2 = IndexModel([('reps_num',DESCENDING)])
        index3 = IndexModel([('following_num',DESCENDING)])
        index4 = IndexModel([('follower_num',DESCENDING)])
        self.collection1.create_indexes([index1, index2, index3, index4])
        self.collection2 = db['rep']
        self.collection2.create_index([("rep_id", DESCENDING)], unique=True)
        index1 = IndexModel([('stars_num', DESCENDING)])
        index2 = IndexModel([('commits_num', DESCENDING)])
        index3 = IndexModel([('forks_num', DESCENDING)])
        self.collection2.create_indexes([index1, index2, index3])
                

    def process_item(self, item, spider):
        if(isinstance(item, GitHubUserItem)):
            try:
                self.collection1.insert(dict(item))
            except DuplicateKeyError as e:
                pass
            return item
        elif(isinstance(item, GitHubRepItem)):
            try:
                self.collection2.insert(dict(item))
            except DuplicateKeyError as e:
                pass
            return item
