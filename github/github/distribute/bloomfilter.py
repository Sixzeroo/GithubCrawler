#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Sixzeroo
# website: www.liuin.cn

import redis
from hashlib import md5

from github.config import REDIS_HOST, REDIS_PORT

# 根据 开辟内存大小 和 种子，生成不同的hash函数
# 也就是构造上述提到的：Bloom Filter使用k个相互独立的哈希函数，我们记为 **H = { H1( ),  H2( ),  ...,  Hk( ) }**
class SimpleHash(object):
    def __init__(self, bitSize, seed):
        self.bitSize = bitSize
        self.seed = seed

    def hash(self, value):
        ret = 0
        for i in range(len(value)):
            # print(f"value[i] = {value[i]},  ord(value[i]) = {ord(value[i])}")
            ret += self.seed * ret + ord(value[i])
        # 控制hashValue的值在这个内存空间的范围
        hashValue = (self.bitSize - 1) & ret
        # print(f"value = {value}, hashValue = {hashValue}")
        return hashValue


# 在redis中初始化一个大字符串，也可以认为是在redis中开辟了一块内存空间
# 需要指定数据库名， 比如这儿用到的就是db2
# 指定使用数据块个数，也就是开辟几个这样的大字符串。
# 当数据达到非常大时，512M肯定是不够用的，可能每个位都被置为1了，所以需要开辟多个大字符串
# 大字符串名name = (key + int)
class BloomFilter(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, db=2, blockNum=1, key='bloomfilter'):
        """
        :param host: the host of Redis
        :param port: the port of Redis
        :param db: witch db in Redis
        :param blockNum: one blockNum for about 90,000,000; if you have more strings for filtering, increase it.
        :param key: the key's name in Redis
        """
        self.server = redis.Redis(host=host, port=port, db=db)
        # 2^31 = 256M
        # 这是一个限制值，最大为256M，因为在redis中，字符串值可以进行伸展，伸展时，空白位置以0填充。
        self.bit_size = 1 << 31  # Redis的String类型最大容量为512M，现使用256M
        self.seeds = [5, 7, 11, 13, 31, 37, 61]
        self.key = key
        self.blockNum = blockNum
        self.hashfunc = []
        for seed in self.seeds:
            # 根据seed 构造出 k=7 个独立的hash函数
            self.hashfunc.append(SimpleHash(self.bit_size, seed))

    # 判断元素是否在集合中
    def isContains(self, str_input):
        if not str_input:
            return False
        m5 = md5()
        m5.update(str_input.encode('utf-8'))
        # 先取目标字符串的md5值
        str_input = m5.hexdigest()
        ret = True
        name = self.key + str(int(str_input[0:2], 16) % self.blockNum)
        for f in self.hashfunc:
            loc = f.hash(str_input)
            ret = ret & self.server.getbit(name, loc)
        return ret

    # 将str_input映射的结果，写入到大字符串中，也就是置上相关的标志位
    def insert(self, str_input):
        m5 = md5()
        m5.update(str_input.encode('utf-8'))
        str_input = m5.hexdigest()
        name = self.key + str(int(str_input[0:2], 16) % self.blockNum)
        for f in self.hashfunc:
            loc = f.hash(str_input)
            # print(f"name = {name}, loc = {loc}")
            self.server.setbit(name, loc, 1)
