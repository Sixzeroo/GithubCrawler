# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
import redis
from scrapy.exceptions import DropItem

from github.config import *
from github.items import GitHubRepItem,GitHubUserItem


class GithubPipeline(object):

    def __init__(self):
        # MongoDB
        client = MongoClient(MONGODB_SERVER,
                             MONGODB_PORT)
        db = client[MONGODB_DB]
        self.collection1 = db['user']
        self.collection2 = db['rep']
        # Reids 配置
        pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=1)
        self.redis_server = redis.Redis(connection_pool=pool)
        # Redis中导入MongoDB初始数据
        if(self.redis_server.exists("working") == 0):
            self.redis_server.set("working", '0')
        if(self.redis_server.get("working") == '0'):
            self.redis_server.delete(REDIS_DATA_REP)
            self.redis_server.delete(REDIS_DATA_USER)
            self.redis_server.set("working", '1')
        if(self.redis_server.hlen(REDIS_DATA_USER) == 0):
            user_list = self.collection1.find({},{'user_id':1})
            for user in user_list:
                self.redis_server.hset(REDIS_DATA_USER, user['user_id'], 0)
        if(self.redis_server.hlen(REDIS_DATA_REP) == 0):
            rep_list = self.collection2.find({},{'user_id':1,'rep_name':1})
            for rep in rep_list:
                self.redis_server.hset(REDIS_DATA_REP, rep['user_id']+'/'+rep['rep_name'], 0)
                

    def process_item(self, item, spider):
        if(isinstance(item, GitHubUserItem)):
            # 用户去重
            if(self.redis_server.hexists(REDIS_DATA_USER, item['user_id'])):
                raise DropItem("Duplicate item found: %s" % item)
            self.collection1.insert(dict(item))
            self.redis_server.hset(REDIS_DATA_USER, item['user_id'], 0)
            return item
        elif(isinstance(item, GitHubRepItem)):
            # 仓库去重
            if(self.redis_server.hexists(REDIS_DATA_REP, item['user_id']+'/'+item['rep_name'])):
                raise DropItem("Duplicate item found: %s" % item)
            self.collection2.insert(dict(item))
            self.redis_server.hset(REDIS_DATA_REP, item['user_id']+'/'+item['rep_name'], 0)
            return item
