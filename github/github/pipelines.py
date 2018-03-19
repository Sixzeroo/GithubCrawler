# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

from github.items import *

from github.config import *
from github.items import GitHubRepItem,GitHubUserItem


class GithubPipeline(object):
    def __init__(self):
        client = MongoClient(MONGODB_SERVER,
                             MONGODB_PORT)
        db = client[MONGODB_DB]
        self.collection1 = db['user']
        self.collection2 = db['rep']

    def process_item(self, item, spider):
        if(isinstance(item, GitHubUserItem)):
            self.collection1.insert(dict(item))
            return item
        elif(isinstance(item, GitHubRepItem)):
            self.collection2.insert(dict(item))
            return item

    def save(self, item):
        if (isinstance(item, GitHubUserItem)):
            tem_dict = dict(item)
            self.collection1.insert(tem_dict)
            return item
        elif (isinstance(item, GitHubRepItem)):
            tem_dict = dict(item)
            self.collection2.insert(tem_dict)
            return item