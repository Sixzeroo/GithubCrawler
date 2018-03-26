# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GitHubUserItem(scrapy.Item):
    user_id = scrapy.Field()
    user_name= scrapy.Field()
    email = scrapy.Field()
    location = scrapy.Field()
    url = scrapy.Field()
    intro = scrapy.Field()
    avatar_url = scrapy.Field()
    company = scrapy.Field()
    reps_num = scrapy.Field()
    stars_num = scrapy.Field()
    followers_num = scrapy.Field()
    following_num = scrapy.Field()
    contr_num = scrapy.Field()

    def getFromDict(self, user):
        self['user_id'] = user['user_id']
        self['user_name'] = user['user_name']
        self['email'] = user['email']
        self['location'] = user['location']
        self['url'] = user['url']
        self['intro'] = user['intro']
        self['avatar_url'] = user['avatar_url']
        self['company'] = user['company']
        self['reps_num'] = user['reps_num']
        self['stars_num'] = user['stars_num']
        self['followers_num'] = user['followers_num']
        self['following_num'] = user['following_num']
        self['contr_num'] = user['contr_num']

    def convertDict(self):
        res = {}
        res['user_name'] = self.user_name
        res['email'] = self.email
        res['location'] = self.location
        res['url'] = self.url
        res['intro'] = self.intro
        res['avatar_url'] = set.avatar_url
        res['company'] = self.company
        res['reps_nums'] = self.reps_nums
        res['starts_num'] = self.starts_num
        res['followers_num'] = self.followers_num
        res['following_num'] = self.following_num

class GitHubRepItem(scrapy.Item):
    user_id = scrapy.Field()
    rep_name = scrapy.Field()
    rep_lang = scrapy.Field()
    rep_id = scrapy.Field()
    commits_num = scrapy.Field()
    forks_num =scrapy.Field()
    stars_num = scrapy.Field()
    forked = scrapy.Field()

    def getFromDict(self, rep):
        self['user_id'] = rep['user_id']
        self['rep_name'] = rep['rep_name']
        self['rep_lang'] = rep['rep_lang']
        self['rep_id'] = rep['rep_id']
        self['commits_num'] = rep['commits_num']
        self['forks_num'] = rep['forks_num']
        self['stars_num'] = rep['stars_num']
        self['forked'] = rep['forked']
