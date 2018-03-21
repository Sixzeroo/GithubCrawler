# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
import redis
from scrapy.exceptions import DropItem
from scrapy import log

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
        self.collection2 = db['rep']
        # 去重通过MongoDB 实现
                

    def process_item(self, item, spider):
        if(isinstance(item, GitHubUserItem)):
            self.collection1.insert(dict(item))
            return item
        elif(isinstance(item, GitHubRepItem)):
            self.collection2.insert(dict(item))
            return item
