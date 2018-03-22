#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Sixzeroo
# website: www.liuin.cn

import scrapy

from scrapy.http import Request, FormRequest, HtmlResponse

from github import config
from github.utils.handle import *
from github.pipelines import GithubPipeline
from github.items import GitHubUserItem,GitHubRepItem


startURL = config.START_URL_LIST

githubBaseURL = "https://github.com"


class GithubSpider(scrapy.Spider):
    name = "github"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "https://github.com/session"
    }
    cookiejar = 1
    githubUser = config.GITHUBUSER
    passwd = config.GITHUBPASSWD
    login = True

    def start_requests(self):
        if(self.login):
            yield scrapy.Request('https://github.com/login', meta={'cookiejar':1}, callback=self.parse_login)
        else:
            yield scrapy.Request(startURL[0], headers=self.headers, meta={'cookiejar': self.cookiejar},
                                 callback=self.parse)
            yield scrapy.Request(startURL[1], headers=self.headers, meta={'cookiejar': self.cookiejar},
                                 callback=self.parse)

    # 登录模块
    def parse_login(self, response):
        authenticity_token = response.css('form input[name="authenticity_token"]::attr(value)').extract_first()
        self.log('authenticity_token:' + authenticity_token)
        return [FormRequest.from_response(
            response,
            url='https://github.com/session',
            headers=self.headers,
            meta={'cookiejar': response.meta['cookiejar']},
            formdata={
                'commit': 'Sign+in',
                'utf8': '✓',
                'authenticity_token': authenticity_token,
                'login': self.githubUser,
                'password': self.passwd
            },
            callback=self.after_login,
            dont_filter=True
        )]

    # 登录之后
    def after_login(self, response):
        self.cookiejar = response.meta['cookiejar']
        self.log("使用账户%s登录成功\n"%self.githubUser)
        yield scrapy.Request(startURL[0], headers=self.headers, meta={'cookiejar':self.cookiejar}, callback=self.parse)
        yield scrapy.Request(startURL[1], headers=self.headers, meta={'cookiejar':self.cookiejar}, callback=self.parse)


    # 解析个人界面信息
    def parse(self, response):
        # 个人基本信息
        name = response.xpath('//*[@class="p-name vcard-fullname d-block overflow-hidden"]/text()').extract_first()
        id = response.xpath('//*[@class="p-nickname vcard-username d-block"]/text()').extract_first()
        # email 需要登录才能查看
        email = response.xpath('//*[@class="u-email"]/text()').extract_first()
        location = response.xpath('//*[@class="p-label"]/text()').extract_first()
        url = response.xpath('//*[@class="u-url"]/text()').extract_first()
        intro = response.xpath('//*[@class="p-note user-profile-bio"]/div/text()').extract_first()
        intro = stringStrip(intro)
        avatar_url = response.xpath('//*[@class="avatar width-full rounded-2"]/@src').extract_first()
        avatar_url = simplifyAvaUrl(avatar_url)

        # 获取公司信息
        company = []
        companyList = response.xpath('//*[@class="user-mention"]/text()')
        if(companyList is not None):
            for item in companyList:
                company.append(item.extract())
        else:
            otherCompany = response.xpath('//*[@class="p-org"]/text()').extract_first()
            if(otherCompany is not None):
                company.append(otherCompany)

        # 计数类
        counters = response.xpath('//*[@class="Counter"]/text()')
        repsNum = strNumtoInt(counters[0].extract())
        starsNum = strNumtoInt(counters[1].extract())
        followersNum = strNumtoInt(counters[2].extract())
        followingNum = strNumtoInt(counters[3].extract())

        user_info = {
            'user_name' : name,
            'user_id': id,
            'email': email,
            'location' : location,
            'url' : url,
            'intro': intro,
            'avatar_url': avatar_url,
            'company': company,
            'reps_num' : repsNum,
            'stars_num' : starsNum,
            'followers_num' : followersNum,
            'following_num' : followingNum
        }
        # convert to Item
        github_user_item = GitHubUserItem()
        github_user_item.getFromDict(user_info)
        yield github_user_item

        # printDict(user_info)

        # 收藏列表解析
        starsListURL = "https://github.com/"+id+"?tab=stars"
        yield Request(url=starsListURL,
                      headers=self.headers,
                      meta={'cookiejar':self.cookiejar},
                      callback=self.parse_stars_list)

        # 仓库列表解析
        repsListURL = "https://github.com/"+id+"?tab=repositories"
        yield Request(url=repsListURL,
                      headers=self.headers,
                      meta={'cookiejar':self.cookiejar, 'user_id':id},
                      callback=self.parse_reps_list
                      )


        # fllower和flllowing进行解析
        followersListURL = "https://github.com/"+id+"?tab=followers"
        yield Request(url=followersListURL,
                      headers=self.headers,
                      meta={'cookiejar':self.cookiejar},
                      callback=self.parse_fllower_list
                      )

        followingsListURL = "https://github.com/" + id + "?tab=following"
        yield Request(url=followingsListURL,
                      headers=self.headers,
                      meta={'cookiejar': self.cookiejar},
                      callback=self.parse_fllowing_list
                      )

    # 解析具体的仓库rep
    def parse_rep(self, response):
        user_id = response.xpath('//*[@class="url fn"]/text()').extract_first()
        rep_lang = response.meta['rep_lang']
        rep_name = response.xpath('//*[@itemprop="name"]/a/text()').extract_first()
        rep_id = user_id+'/'+rep_name
        commits_num = stringStrip(response.xpath('//*[@class="num text-emphasized"]/text()').extract_first())
        commits_num = strNumtoInt(commits_num)
        if (self.login == True) :
            forks_num = stringStrip(response.xpath('//*[@class="social-count"]/text()').extract_first())
        else:
            forks_num = stringStrip(response.xpath('//*[@class="social-count"]/text()').extract()[1])
        forks_num = strNumtoInt(forks_num)
        stars_num = stringStrip(response.xpath('//*[@class="social-count js-social-count"]/text()').extract_first())
        stars_num = strNumtoInt(stars_num)

        rep_info = {
            'user_id': user_id,
            'rep_name': rep_name,
            'rep_lang': rep_lang,
            'rep_id': rep_id,
            'commits_num': commits_num,
            'forks_num': forks_num,
            'stars_num': stars_num
        }
        github_rep_item = GitHubRepItem()
        github_rep_item.getFromDict(rep_info)
        yield github_rep_item
        # printDict(rep_info)

    # 解析stars 列表
    def parse_stars_list(self, response):
        stars_div_list = response.xpath('//*[@class="col-12 d-block width-full py-4 border-bottom"]')
        for stars_div in stars_div_list:
            rep_href = stars_div.xpath('./div/h3/a/@href').extract_first()
            rep_url = githubBaseURL + rep_href
            rep_lang = stars_div.xpath('./div/span/text()').extract_first()
            rep_lang = stringStrip(rep_lang)
            # 解析这个仓库
            yield Request(url=rep_url,
                          headers=self.headers,
                          meta={'cookiejar': self.cookiejar,
                                'rep_lang': rep_lang},
                          callback=self.parse_rep
                          )

        # 获取下一个列表地址
        next_href = response.xpath('//*[@class="next_page"]/@href').extract_first()
        if (next_href is not None):
            next_stars_list_url = githubBaseURL + next_href
            yield Request(url=next_stars_list_url,
                          headers=self.headers,
                          meta={'cookiejar': self.cookiejar},
                          callback=self.parse_reps_list
                          )

    # 解析reps 列表
    def parse_reps_list(self, response):
        reps_li_list = response.xpath('//*[@itemprop="owns"]')
        for reps_li in reps_li_list:
            rep_name = stringStrip(reps_li.xpath('./div/h3/a/text()').extract_first())
            rep_href = stringStrip(reps_li.xpath('./div/h3/a/@href').extract_first())
            rep_url = githubBaseURL + rep_href
            rep_lang = reps_li.xpath('./div/span/text()').extract()
            if (len(rep_lang) == 0):
                rep_lang = ""
            elif (stringStrip(rep_lang[0]) == 'Forked from'):
                try:
                    rep_lang = stringStrip(rep_lang[2])
                except IndexError:
                    rep_lang = ""
            else:
                rep_lang = stringStrip(rep_lang[0])
            # 解析这个仓库
            yield Request(url=rep_url,
                          headers=self.headers,
                          meta={'cookiejar': self.cookiejar,
                                'rep_lang': rep_lang,
                                'user_id': response.meta['user_id'],
                                'rep_name': rep_name},
                          callback=self.parse_rep
                          )

        # 获取下一个列表地址
        next_href = response.xpath('//*[@class="next_page"]/@href').extract_first()
        if(next_href is not None):
            next_reps_list_url = githubBaseURL + next_href
            yield Request(url=next_reps_list_url,
                          headers=self.headers,
                          meta={'cookiejar': self.cookiejar,
                                'user_id': response.meta['user_id']},
                          callback=self.parse_reps_list
                          )




    # 解析fllower 列表
    def parse_fllower_list(self, response):
        person_hrefs = response.xpath('//*[@class="d-table col-12 width-full py-4 border-bottom border-gray-light"]/div[2]/a/@href').extract()
        for href in person_hrefs:
            url = "https://github.com"+href
            yield Request(url=url,
                      headers=self.headers,
                      meta={'cookiejar': self.cookiejar},
                      callback=self.parse
                      )
        # 获取下一个列表
        buttom_text = response.xpath('//*[@class="paginate-container"]/div/a/text()').extract()
        if((len(buttom_text) == 1 and buttom_text[0] == 'Next') or(len(buttom_text) == 2 and buttom_text[1] == 'Next')):
            next_list_url = response.xpath('//*[@class="paginate-container"]/div/a/@href').extract_first()
            yield Request(url=next_list_url,
                          headers=self.headers,
                          meta={'cookiejar': self.cookiejar},
                          callback=self.parse_fllower_list
                          )


    # 解析fllowing 列表
    def parse_fllowing_list(self, response):
        person_hrefs = response.xpath('//*[@class="d-table col-12 width-full py-4 border-bottom border-gray-light"]/div[2]/a/@href').extract()
        for href in person_hrefs:
            url = "https://github.com"+href
            yield Request(url=url,
                      headers=self.headers,
                      meta={'cookiejar': self.cookiejar},
                      callback=self.parse
                      )
        # 获取下一个列表
        buttom_text = response.xpath('//*[@class="paginate-container"]/div/a/text()').extract()
        if ((len(buttom_text) == 1 and buttom_text[0] == 'Next') or (len(buttom_text) == 2 and buttom_text[1] == 'Next')):
            next_list_url = response.xpath('//*[@class="paginate-container"]/div/a/@href').extract_first()
            yield Request(url=next_list_url,
                          headers=self.headers,
                          meta={'cookiejar': self.cookiejar},
                          callback=self.parse_fllowing_list
                          )

