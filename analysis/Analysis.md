# Github 爬虫数据分析

Github作为世界上最大的"同性"交友网站，可以说是coder的天堂。这里面的数据一定有许多有趣的地方。

这里爬取的数据主要有两大类：用户数据和仓库数据，此次分析的数据量：256171用户数据，434994仓库数据

## 目录

   * [Github 爬虫数据分析](#github-爬虫数据分析)
      * [用户](#用户)
         * [全球用户榜单](#全球用户榜单)
            * [Followers人数榜](#followers人数榜)
            * [Following人数榜](#following人数榜)
            * [Stars榜](#stars榜)
            * [Reps榜](#reps榜)
            * [Contribution榜](#contribution榜)
         * [中国用户榜单](#中国用户榜单)
            * [Followers人数榜](#followers人数榜-1)
            * [Following人数榜](#following人数榜-1)
            * [Stars榜](#stars榜-1)
            * [Reps榜](#reps榜-1)
            * [Contribution榜](#contribution榜-1)
         * [个人网站中顶级域名分布情况](#个人网站中顶级域名分布情况)
         * [用户公布邮箱情况](#用户公布邮箱情况)
         * [用户所在公司情况](#用户所在公司情况)
      * [仓库](#仓库)
         * [Stars榜](#stars榜-2)
         * [Forks榜](#forks榜)
         * [C](#c)
         * [C  ](#c-1)
         * [Java](#java)
         * [Python](#python)
         * [JavaScript](#javascript)
         * [语言使用比例](#语言使用比例)

## 用户

### 全球用户榜单

#### Followers人数榜

| Avatar | User | Repos | Stars | Followers | Following | Contributions|
|--------|------|-------|-------|-----------|-----------|-----------|
|![](https://avatars0.githubusercontent.com/u/1024025) | https://github.com/torvalds  |   6 | 2 | 70400 | 0 | 8 |
|![](https://avatars1.githubusercontent.com/u/66577) | https://github.com/JakeWharton  |   95 | 228 | 45000 | 12 | 3541 |
|![](https://avatars2.githubusercontent.com/u/905434) | https://github.com/ruanyf  |   48 | 206 | 38200 | 0 | 1645 |
|![](https://avatars3.githubusercontent.com/u/25254) | https://github.com/tj  |   273 | 2000 | 34400 | 46 | 3310 |
|![](https://avatars2.githubusercontent.com/u/499550) | https://github.com/yyx990803  |   141 | 779 | 29200 | 90 | 2553 |
|![](https://avatars1.githubusercontent.com/u/110953) | https://github.com/addyosmani  |   295 | 807 | 29000 | 254 | 928 |
|![](https://avatars1.githubusercontent.com/u/810438) | https://github.com/gaearon  |   227 | 1300 | 27200 | 171 | 3019 |
|![](https://avatars3.githubusercontent.com/u/39191) | https://github.com/paulirish  |   266 | 723 | 25600 | 245 | 2375 |
|![](https://avatars2.githubusercontent.com/u/170270) | https://github.com/sindresorhus  |   975 | 2500 | 23600 | 50 | 4753 |
|![](https://avatars1.githubusercontent.com/u/119893) | https://github.com/kennethreitz  |   141 | 1900 | 21200 | 197 | 5626 |

#### Following人数榜

| Avatar | User | Repos | Stars | Followers | Following | Contributions|
|--------|------|-------|-------|-----------|-----------|-----------|
|![](https://avatars2.githubusercontent.com/u/3076393) | https://github.com/KevinHock  |   19 | 198 | 1300 | 284000 | 639 |
|![](https://avatars1.githubusercontent.com/u/5877145) | https://github.com/angusshire  |   8 | 217000 | 10300 | 230000 | 30 |
|![](https://avatars1.githubusercontent.com/u/6508763) | https://github.com/dalinhuang99  |   20 | 75 | 3200 | 162000 | 1293 |
|![](https://avatars2.githubusercontent.com/u/3604053) | https://github.com/cusspvz  |   109 | 1200 | 6600 | 130000 | 90 |
|![](https://avatars2.githubusercontent.com/u/6673982) | https://github.com/MichalPaszkiewicz  |   60 | 558 | 4600 | 72700 | 172 |
|![](https://avatars0.githubusercontent.com/u/418638) | https://github.com/nfultz  |   70 | 2500 | 2600 | 61600 | 2141 |
|![](https://avatars3.githubusercontent.com/u/14251570) | https://github.com/mstraughan86  |   15 | 454 | 3400 | 60500 | 299 |
|![](https://avatars3.githubusercontent.com/u/32831059) | https://github.com/opengiineer  |   19 | 90 | 1600 | 55700 | 46 |
|![](https://avatars1.githubusercontent.com/u/778015) | https://github.com/ahmetabdi  |   130 | 4100 | 448 | 53300 | 1954 |
|![](https://avatars3.githubusercontent.com/u/4107768) | https://github.com/brunocasanova  |   46 | 152 | 2400 | 48300 | 13 |

#### Stars榜

看看谁收藏的仓库最多

| Avatar | User | Repos | Stars | Followers | Following | Contributions|
|--------|------|-------|-------|-----------|-----------|-----------|
|![](https://avatars1.githubusercontent.com/u/5877145) | https://github.com/angusshire  |   8 | 217000 | 10300 | 230000 | 30 |
|![](https://avatars3.githubusercontent.com/u/1610158) | https://github.com/mcanthony  |   4300 | 42500 | 375 | 12700 | 21 |
|![](https://avatars1.githubusercontent.com/u/3947125) | https://github.com/maoabc1818  |   9 | 32200 | 121 | 95 | 2 |
|![](https://avatars1.githubusercontent.com/u/391299) | https://github.com/JT5D  |   210 | 29300 | 276 | 6200 | 0 |
|![](https://avatars2.githubusercontent.com/u/500775) | https://github.com/reduxionist  |   15 | 25800 | 174 | 429 | 62 |
|![](https://avatars0.githubusercontent.com/u/6948067) | https://github.com/pranavlathigara  |   1200 | 24600 | 793 | 14900 | 130 |
|![](https://avatars3.githubusercontent.com/u/2882) | https://github.com/nikolay  |   12 | 23100 | 243 | 349 | 469 |
|![](https://avatars3.githubusercontent.com/u/3759759) | https://github.com/denji  |   1300 | 22500 | 181 | 397 | 305 |
|![](https://avatars3.githubusercontent.com/u/24416962) | https://github.com/roscopecoltran  |   156 | 21000 | 121 | 4400 | 599 |
|![](https://avatars0.githubusercontent.com/u/6257454) | https://github.com/Jerzerak  |   1 | 18900 | 54 | 0 | 3 |

#### Reps榜

Github上创建仓库最多的人在这里

| Avatar | User | Repos | Stars | Followers | Following | Contributions|
|--------|------|-------|-------|-----------|-----------|-----------|
|![](https://avatars0.githubusercontent.com/u/675997) | https://github.com/pombredanne  |   40600 | 6500 | 149 | 87 | 2558 |
|![](https://avatars1.githubusercontent.com/u/1732196) | https://github.com/carriercomm  |   20400 | 12900 | 72 | 176 | 151 |
|![](https://avatars1.githubusercontent.com/u/14135456) | https://github.com/digideskio  |   18000 | 88 | 120 | 3900 | 113 |
|![](https://avatars0.githubusercontent.com/u/431924) | https://github.com/guoyu07  |   11600 | 91 | 20 | 1000 | 112 |
|![](https://avatars2.githubusercontent.com/u/12729391) | https://github.com/modulexcite  |   10700 | 4200 | 30 | 192 | 15 |
|![](https://avatars2.githubusercontent.com/u/1218365) | https://github.com/PlumpMath  |   10100 | 508 | 31 | 147 | 103 |
|![](https://avatars0.githubusercontent.com/u/3380677) | https://github.com/carabina  |   9300 | 8700 | 83 | 5 | 101 |
|![](https://avatars1.githubusercontent.com/u/4687038) | https://github.com/jorik041  |   9200 | 53 | 20 | 129 | 101 |
|![](https://avatars3.githubusercontent.com/u/1332574) | https://github.com/treejames  |   8000 | 6900 | 93 | 897 | 101 |
|![](https://avatars2.githubusercontent.com/u/498130) | https://github.com/mehulsbhatt  |   7400 | 364 | 23 | 9 | 104 |

#### Contribution榜

| Avatar | User | Repos | Stars | Followers | Following | Contributions|
|--------|------|-------|-------|-----------|-----------|-----------|
|![](https://avatars1.githubusercontent.com/u/3244) | https://github.com/robertbrook  |   67 | 32 | 63 | 114 | 539804 |
|![](https://avatars0.githubusercontent.com/u/20975616) | https://github.com/SimiCode  |   24 | 11 | 5 | 15 | 377077 |
|![](https://avatars2.githubusercontent.com/u/751143) | https://github.com/jasoncalabrese  |   75 | 50 | 64 | 19 | 357587 |
|![](https://avatars2.githubusercontent.com/u/56100) | https://github.com/kinlane  |   222 | 242 | 346 | 588 | 199240 |
|![](https://avatars2.githubusercontent.com/u/415831) | https://github.com/talos  |   113 | 95 | 143 | 7 | 115891 |
|![](https://avatars3.githubusercontent.com/u/283441) | https://github.com/honzajavorek  |   87 | 167 | 128 | 93 | 80301 |
|![](https://avatars3.githubusercontent.com/u/1006477) | https://github.com/felixonmars  |   420 | 369 | 806 | 149 | 70179 |
|![](https://avatars1.githubusercontent.com/u/1317792) | https://github.com/xndcn  |   33 | 86 | 67 | 8 | 67634 |
|![](https://avatars1.githubusercontent.com/u/3935007) | https://github.com/ojengwa  |   293 | 469 | 67 | 8 | 49621 |
|![](https://avatars3.githubusercontent.com/u/10103766) | https://github.com/SergioChan  |   47 | 372 | 982 | 598 | 42202 |

365天，天天绿是种怎样的体验？

### 中国用户榜单

这里只是通过location中"China"、"Shanghai"类似的关键词对中国用户进行区分，所以可能有遗漏的地方，还请谅解。此次统计的中国用户数据有18011

#### Followers人数榜

| Avatar | User | Repos | Stars | Followers | Following | Contributions|
|--------|------|-------|-------|-----------|-----------|-----------|
|![](https://avatars2.githubusercontent.com/u/905434) | https://github.com/ruanyf  |   48 | 206 | 38200 | 0 | 1645 |
|![](https://avatars2.githubusercontent.com/u/499550) | https://github.com/yyx990803  |   141 | 779 | 29200 | 90 | 2553 |
|![](https://avatars2.githubusercontent.com/u/2503423) | https://github.com/daimajia  |   63 | 2900 | 20000 | 241 | 21 |
|![](https://avatars1.githubusercontent.com/u/470058) | https://github.com/michaelliao  |   61 | 81 | 19700 | 0 | 297 |
|![](https://avatars0.githubusercontent.com/u/327019) | https://github.com/JacksonTian  |   229 | 583 | 15500 | 151 | 805 |
|![](https://avatars1.githubusercontent.com/u/1169522) | https://github.com/Trinea  |   24 | 1500 | 14100 | 38 | 80 |
|![](https://avatars2.githubusercontent.com/u/2267900) | https://github.com/stormzhang  |   5 | 1500 | 12800 | 91 | 9 |
|![](https://avatars2.githubusercontent.com/u/97227) | https://github.com/lifesinger  |   2 | 278 | 12000 | 13 | 1 |
|![](https://avatars2.githubusercontent.com/u/729648) | https://github.com/cloudwu  |   102 | 63 | 11700 | 1 | 690 |
|![](https://avatars0.githubusercontent.com/u/472311) | https://github.com/phodal  |   254 | 1700 | 11100 | 15 | 5924 |

#### Following人数榜

| Avatar | User | Repos | Stars | Followers | Following | Contributions|
|--------|------|-------|-------|-----------|-----------|-----------|
|![](https://avatars2.githubusercontent.com/u/3693121) | https://github.com/fordream  |   724 | 21 | 919 | 19800 | 1 |
|![](https://avatars2.githubusercontent.com/u/17972943) | https://github.com/Vermisse  |   15 | 25 | 2300 | 10400 | 102 |
|![](https://avatars2.githubusercontent.com/u/93859) | https://github.com/technologiclee  |   149 | 844 | 374 | 9500 | 6 |
|![](https://avatars3.githubusercontent.com/u/15626022) | https://github.com/shenzhoudance  |   599 | 6 | 108 | 7700 | 2373 |
|![](https://avatars0.githubusercontent.com/u/10573715) | https://github.com/kotobukki  |   15 | 68 | 111 | 7500 | 889 |
|![](https://avatars3.githubusercontent.com/u/29220207) | https://github.com/vincentpanqi  |   1800 | 714 | 47 | 5600 | 102 |
|![](https://avatars2.githubusercontent.com/u/1727724) | https://github.com/ovwane  |   220 | 1100 | 120 | 5500 | 329 |
|![](https://avatars0.githubusercontent.com/u/9153294) | https://github.com/pisual  |   39 | 62 | 917 | 4900 | 122 |
|![](https://avatars0.githubusercontent.com/u/23236638) | https://github.com/youkaichao  |   39 | 0 | 58 | 4800 | 113 |
|![](https://avatars0.githubusercontent.com/u/7576876) | https://github.com/bloodycoder  |   73 | 34 | 162 | 4200 | 390 |

#### Stars榜

| Avatar | User | Repos | Stars | Followers | Following | Contributions|
|--------|------|-------|-------|-----------|-----------|-----------|
|![](https://avatars3.githubusercontent.com/u/1041542) | https://github.com/weimingtom  |   2100 | 9100 | 172 | 1800 | 1724 |
|![](https://avatars0.githubusercontent.com/u/2041398) | https://github.com/jiangplus  |   28 | 8800 | 85 | 115 | 13 |
|![](https://avatars3.githubusercontent.com/u/1024948) | https://github.com/DavidAlphaFox  |   346 | 7800 | 167 | 83 | 1122 |
|![](https://avatars1.githubusercontent.com/u/480859) | https://github.com/mayulu  |   12 | 7700 | 133 | 616 | 14 |
|![](https://avatars2.githubusercontent.com/u/4370703) | https://github.com/hzy87email  |   73 | 7700 | 77 | 167 | 3 |
|![](https://avatars3.githubusercontent.com/u/1468284) | https://github.com/se77en  |   197 | 7600 | 119 | 455 | 0 |
|![](https://avatars0.githubusercontent.com/u/12030169) | https://github.com/JaredYeDH  |   166 | 7400 | 45 | 636 | 101 |
|![](https://avatars2.githubusercontent.com/u/10380759) | https://github.com/xhs  |   20 | 7200 | 43 | 119 | 10 |
|![](https://avatars2.githubusercontent.com/u/1881113) | https://github.com/paladin74  |   618 | 7100 | 52 | 901 | 1 |
|![](https://avatars1.githubusercontent.com/u/3856) | https://github.com/mrluanma  |   12 | 7000 | 126 | 541 | 36 |

#### Reps榜

| Avatar | User | Repos | Stars | Followers | Following | Contributions|
|--------|------|-------|-------|-----------|-----------|-----------|
|![](https://avatars3.githubusercontent.com/u/10938976) | https://github.com/skyformat99  |   6000 | 143 | 98 | 3200 | 134 |
|![](https://avatars1.githubusercontent.com/u/1203820) | https://github.com/tempbottle  |   4200 | 59 | 21 | 18 | 101 |
|![](https://avatars3.githubusercontent.com/u/8662447) | https://github.com/JamesLinus  |   4100 | 1600 | 89 | 3300 | 181 |
|![](https://avatars0.githubusercontent.com/u/12955801) | https://github.com/hu19891110  |   3600 | 90 | 11 | 112 | 107 |
|![](https://avatars2.githubusercontent.com/u/452743) | https://github.com/WilliamRen  |   2900 | 3200 | 32 | 5 | 5 |
|![](https://avatars3.githubusercontent.com/u/3414057) | https://github.com/chagge  |   2300 | 8 | 16 | 669 | 101 |
|![](https://avatars2.githubusercontent.com/u/6813552) | https://github.com/forging2012  |   2200 | 789 | 8 | 71 | 151 |
|![](https://avatars3.githubusercontent.com/u/1041542) | https://github.com/weimingtom  |   2100 | 9100 | 172 | 1800 | 1724 |
|![](https://avatars1.githubusercontent.com/u/23429527) | https://github.com/isuhao  |   2000 | 153 | 62 | 2700 | 282 |
|![](https://avatars1.githubusercontent.com/u/5791117) | https://github.com/ycaihua  |   1900 | 109 | 38 | 589 | 133 |

#### Contribution榜

| Avatar | User | Repos | Stars | Followers | Following | Contributions|
|--------|------|-------|-------|-----------|-----------|-----------|
|![](https://avatars3.githubusercontent.com/u/1006477) | https://github.com/felixonmars  |   420 | 369 | 806 | 149 | 70179 |
|![](https://avatars3.githubusercontent.com/u/10103766) | https://github.com/SergioChan  |   47 | 372 | 982 | 598 | 42202 |
|![](https://avatars1.githubusercontent.com/u/12693644) | https://github.com/dragon-yuan  |   16 | 109 | 35 | 50 | 18591 |
|![](https://avatars1.githubusercontent.com/u/8347202) | https://github.com/fengss  |   30 | 67 | 15 | 1 | 12560 |
|![](https://avatars0.githubusercontent.com/u/9410171) | https://github.com/xieguigang  |   41 | 115 | 136 | 143 | 10999 |
|![](https://avatars2.githubusercontent.com/u/9280577) | https://github.com/csjunxu  |   194 | 81 | 35 | 51 | 9935 |
|![](https://avatars3.githubusercontent.com/u/559179) | https://github.com/airyland  |   183 | 1400 | 996 | 175 | 8852 |
|![](https://avatars1.githubusercontent.com/u/11537812) | https://github.com/yutiansut  |   216 | 1100 | 298 | 8 | 7311 |
|![](https://avatars2.githubusercontent.com/u/1826685) | https://github.com/lloydzhou  |   92 | 556 | 52 | 69 | 6729 |
|![](https://avatars1.githubusercontent.com/u/8784712) | https://github.com/egoist  |   647 | 2700 | 3600 | 40 | 6236 |

### 个人网站中顶级域名分布情况

![](https://data2.liuin.cn/2018-04-01-15225621477939.jpg)

### 用户公布邮箱情况

![](https://data2.liuin.cn/2018-04-01-15225624252077.jpg)

### 用户所在公司情况

公布公司的前8

![](https://data2.liuin.cn/2018-04-01-15225631364406.jpg)

云图

![](https://data2.liuin.cn/2018-04-01-15225635127953.jpg)

## 仓库

### Stars榜

| Rep | User | Language | Stars | Fork | Commit |
|--------|------|-------|-------|-----------|-----------|
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | [freeCodeCamp](https://github.com/freeCodeCamp) | JavaScript | 291895 | 13667 | 11334 |
| [twbs/bootstrap](https://github.com/twbs/bootstrap) | [twbs](https://github.com/twbs) | CSS | 123341 | 58717 | 17645 |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | [EbookFoundation](https://github.com/EbookFoundation) |  | 103480 | 26331 | 4634 |
| [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | [tensorflow](https://github.com/tensorflow) | C++ | 95028 | 60694 | 30887 |
| [facebook/react](https://github.com/facebook/react) | [facebook](https://github.com/facebook) | JavaScript | 92602 | 17473 | 9773 |
| [vuejs/vue](https://github.com/vuejs/vue) | [vuejs](https://github.com/vuejs) | JavaScript | 89447 | 13129 | 2581 |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | [sindresorhus](https://github.com/sindresorhus) |  | 82141 | 10785 | 725 |
| [getify/You-Dont-Know-JS](https://github.com/getify/You-Dont-Know-JS) | [getify](https://github.com/getify) |  | 78848 | 14404 | 1465 |
| [d3/d3](https://github.com/d3/d3) | [d3](https://github.com/d3) | JavaScript | 74472 | 19024 | 4132 |
| [airbnb/javascript](https://github.com/airbnb/javascript) | [airbnb](https://github.com/airbnb) | JavaScript | 68833 | 13127 | 1607 |

### Forks榜

| Rep | User | Language | Stars | Fork | Commit |
|--------|------|-------|-------|-----------|-----------|
| [jtleek/datasharing](https://github.com/jtleek/datasharing) | [jtleek](https://github.com/jtleek) |  | 4332 | 184409 | 29 |
| [rdpeng/ProgrammingAssignment2](https://github.com/rdpeng/ProgrammingAssignment2) | [rdpeng](https://github.com/rdpeng) | R | 528 | 110145 | 7 |
| [octocat/Spoon-Knife](https://github.com/octocat/Spoon-Knife) | [octocat](https://github.com/octocat) | HTML | 10043 | 97471 | 3 |
| [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | [tensorflow](https://github.com/tensorflow) | C++ | 95028 | 60694 | 30887 |
| [twbs/bootstrap](https://github.com/twbs/bootstrap) | [twbs](https://github.com/twbs) | CSS | 123341 | 58717 | 17645 |
| [SmartThingsCommunity/SmartThingsPublic](https://github.com/SmartThingsCommunity/SmartThingsPublic) | [SmartThingsCommunity](https://github.com/SmartThingsCommunity) | Groovy | 853 | 38018 | 2448 |
| [rdpeng/RepData_PeerAssessment1](https://github.com/rdpeng/RepData_PeerAssessment1) | [rdpeng](https://github.com/rdpeng) |  | 69 | 29883 | 13 |
| [github/gitignore](https://github.com/github/gitignore) | [github](https://github.com/github) |  | 63853 | 29259 | 2738 |
| [angular/angular.js](https://github.com/angular/angular.js) | [angular](https://github.com/angular) | JavaScript | 58232 | 28872 | 8755 |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | [EbookFoundation](https://github.com/EbookFoundation) |  | 103480 | 26331 | 4634 |

### C

stars排行

| Rep | User | Language | Stars | Fork | Commit |
|--------|------|-------|-------|-----------|-----------|
| [torvalds/linux](https://github.com/torvalds/linux) | [torvalds](https://github.com/torvalds) | C | 57191 | 21032 | 744803 |
| [firehol/netdata](https://github.com/firehol/netdata) | [firehol](https://github.com/firehol) | C | 28607 | 2389 | 6690 |
| [antirez/redis](https://github.com/antirez/redis) | [antirez](https://github.com/antirez) | C | 28340 | 10916 | 6679 |
| [git/git](https://github.com/git/git) | [git](https://github.com/git) | C | 21665 | 12634 | 50674 |
| [Bilibili/ijkplayer](https://github.com/Bilibili/ijkplayer) | [Bilibili](https://github.com/Bilibili) | C | 18374 | 5191 | 2584 |
| [php/php-src](https://github.com/php/php-src) | [php](https://github.com/php) | C | 16996 | 4745 | 107206 |
| [SamyPesse/How-to-Make-a-Computer-Operating-System](https://github.com/SamyPesse/How-to-Make-a-Computer-Operating-System) | [SamyPesse](https://github.com/SamyPesse) | C | 16957 | 3015 | 243 |
| [wg/wrk](https://github.com/wg/wrk) | [wg](https://github.com/wg) | C | 15386 | 1245 | 72 |
| [ggreer/the_silver_searcher](https://github.com/ggreer/the_silver_searcher) | [ggreer](https://github.com/ggreer) | C | 14854 | 954 | 1974 |
| [kripken/emscripten](https://github.com/kripken/emscripten) | [kripken](https://github.com/kripken) | C | 14373 | 1704 | 18154 |

forks排行

| Rep | User | Language | Stars | Fork | Commit |
|--------|------|-------|-------|-----------|-----------|
| [torvalds/linux](https://github.com/torvalds/linux) | [torvalds](https://github.com/torvalds) | C | 57191 | 21032 | 744803 |
| [git/git](https://github.com/git/git) | [git](https://github.com/git) | C | 21665 | 12634 | 50674 |
| [antirez/redis](https://github.com/antirez/redis) | [antirez](https://github.com/antirez) | C | 28340 | 10916 | 6679 |
| [arduino/Arduino](https://github.com/arduino/Arduino) | [arduino](https://github.com/arduino) | C | 7936 | 6184 | 6649 |
| [julycoding/The-Art-Of-Programming-By-July](https://github.com/julycoding/The-Art-Of-Programming-By-July) | [julycoding](https://github.com/julycoding) | C | 13544 | 5666 | 3630 |
| [MarlinFirmware/Marlin](https://github.com/MarlinFirmware/Marlin) | [MarlinFirmware](https://github.com/MarlinFirmware) | C | 3615 | 5340 | 9015 |
| [Bilibili/ijkplayer](https://github.com/Bilibili/ijkplayer) | [Bilibili](https://github.com/Bilibili) | C | 18374 | 5191 | 2584 |
| [php/php-src](https://github.com/php/php-src) | [php](https://github.com/php) | C | 16996 | 4745 | 107206 |
| [esp8266/Arduino](https://github.com/esp8266/Arduino) | [esp8266](https://github.com/esp8266) | C | 7063 | 4378 | 2697 |
| [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) | [FFmpeg](https://github.com/FFmpeg) | C | 10314 | 4377 | 90611 |

### C++

stars排行

| Rep | User | Language | Stars | Fork | Commit |
|--------|------|-------|-------|-----------|-----------|
| [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | [tensorflow](https://github.com/tensorflow) | C++ | 95028 | 60694 | 30887 |
| [electron/electron](https://github.com/electron/electron) | [electron](https://github.com/electron) | C++ | 58531 | 7642 | 18669 |
| [apple/swift](https://github.com/apple/swift) | [apple](https://github.com/apple) | C++ | 43250 | 6795 | 68510 |
| [nwjs/nw.js](https://github.com/nwjs/nw.js) | [nwjs](https://github.com/nwjs) | C++ | 33478 | 3731 | 3188 |
| [x64dbg/x64dbg](https://github.com/x64dbg/x64dbg) | [x64dbg](https://github.com/x64dbg) | C++ | 33242 | 684 | 3923 |
| [bitcoin/bitcoin](https://github.com/bitcoin/bitcoin) | [bitcoin](https://github.com/bitcoin) | C++ | 30209 | 18101 | 16629 |
| [google/protobuf](https://github.com/google/protobuf) | [google](https://github.com/google) | C++ | 24950 | 7150 | 5557 |
| [BVLC/caffe](https://github.com/BVLC/caffe) | [BVLC](https://github.com/BVLC) | C++ | 23550 | 14390 | 4118 |
| [opencv/opencv](https://github.com/opencv/opencv) | [opencv](https://github.com/opencv) | C++ | 23493 | 16901 | 23654 |
| [rethinkdb/rethinkdb](https://github.com/rethinkdb/rethinkdb) | [rethinkdb](https://github.com/rethinkdb) | C++ | 20993 | 1665 | 33382 |

forks排行

| Rep | User | Language | Stars | Fork | Commit |
|--------|------|-------|-------|-----------|-----------|
| [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | [tensorflow](https://github.com/tensorflow) | C++ | 95028 | 60694 | 30887 |
| [bitcoin/bitcoin](https://github.com/bitcoin/bitcoin) | [bitcoin](https://github.com/bitcoin) | C++ | 30209 | 18101 | 16629 |
| [opencv/opencv](https://github.com/opencv/opencv) | [opencv](https://github.com/opencv) | C++ | 23493 | 16901 | 23654 |
| [BVLC/caffe](https://github.com/BVLC/caffe) | [BVLC](https://github.com/BVLC) | C++ | 23550 | 14390 | 4118 |
| [electron/electron](https://github.com/electron/electron) | [electron](https://github.com/electron) | C++ | 58531 | 7642 | 18669 |
| [google/protobuf](https://github.com/google/protobuf) | [google](https://github.com/google) | C++ | 24950 | 7150 | 5557 |
| [apple/swift](https://github.com/apple/swift) | [apple](https://github.com/apple) | C++ | 43250 | 6795 | 68510 |
| [cocos2d/cocos2d-x](https://github.com/cocos2d/cocos2d-x) | [cocos2d](https://github.com/cocos2d) | C++ | 11759 | 6496 | 36641 |
| [ArduPilot/ardupilot](https://github.com/ArduPilot/ardupilot) | [ArduPilot](https://github.com/ArduPilot) | C++ | 3110 | 6153 | 31379 |
| [dmlc/xgboost](https://github.com/dmlc/xgboost) | [dmlc](https://github.com/dmlc) | C++ | 11406 | 5192 | 3254 |

### Java

stars排行

| Rep | User | Language | Stars | Fork | Commit |
|--------|------|-------|-------|-----------|-----------|
| [ReactiveX/RxJava](https://github.com/ReactiveX/RxJava) | [ReactiveX](https://github.com/ReactiveX) | Java | 32001 | 5594 | 5328 |
| [iluwatar/java-design-patterns](https://github.com/iluwatar/java-design-patterns) | [iluwatar](https://github.com/iluwatar) | Java | 31422 | 10072 | 2022 |
| [elastic/elasticsearch](https://github.com/elastic/elasticsearch) | [elastic](https://github.com/elastic) | Java | 29931 | 10408 | 30528 |
| [square/retrofit](https://github.com/square/retrofit) | [square](https://github.com/square) | Java | 27182 | 5311 | 1569 |
| [square/okhttp](https://github.com/square/okhttp) | [square](https://github.com/square) | Java | 25870 | 6054 | 3147 |
| [google/guava](https://github.com/google/guava) | [google](https://github.com/google) | Java | 23154 | 5323 | 4676 |
| [spring-projects/spring-boot](https://github.com/spring-projects/spring-boot) | [spring-projects](https://github.com/spring-projects) | Java | 22927 | 17555 | 16129 |
| [PhilJay/MPAndroidChart](https://github.com/PhilJay/MPAndroidChart) | [PhilJay](https://github.com/PhilJay) | Java | 21393 | 5939 | 1938 |
| [kdn251/interviews](https://github.com/kdn251/interviews) | [kdn251](https://github.com/kdn251) | Java | 21348 | 3503 | 370 |
| [bumptech/glide](https://github.com/bumptech/glide) | [bumptech](https://github.com/bumptech) | Java | 21032 | 4132 | 2190 |

forks排行

| Rep | User | Language | Stars | Fork | Commit |
|--------|------|-------|-------|-----------|-----------|
| [spring-projects/spring-boot](https://github.com/spring-projects/spring-boot) | [spring-projects](https://github.com/spring-projects) | Java | 22927 | 17555 | 16129 |
| [spring-projects/spring-framework](https://github.com/spring-projects/spring-framework) | [spring-projects](https://github.com/spring-projects) | Java | 20126 | 13328 | 16384 |
| [apache/incubator-dubbo](https://github.com/apache/incubator-dubbo) | [apache](https://github.com/apache) | Java | 17706 | 12714 | 2201 |
| [elastic/elasticsearch](https://github.com/elastic/elasticsearch) | [elastic](https://github.com/elastic) | Java | 29931 | 10408 | 30528 |
| [iluwatar/java-design-patterns](https://github.com/iluwatar/java-design-patterns) | [iluwatar](https://github.com/iluwatar) | Java | 31422 | 10072 | 2022 |
| [eugenp/tutorials](https://github.com/eugenp/tutorials) | [eugenp](https://github.com/eugenp) | Java | 4950 | 8411 | 7809 |
| [zxing/zxing](https://github.com/zxing/zxing) | [zxing](https://github.com/zxing) | Java | 18000 | 7345 | 3425 |
| [nostra13/Android-Universal-Image-Loader](https://github.com/nostra13/Android-Universal-Image-Loader) | [nostra13](https://github.com/nostra13) | Java | 16040 | 6476 | 1025 |
| [checkstyle/checkstyle](https://github.com/checkstyle/checkstyle) | [checkstyle](https://github.com/checkstyle) | Java | 3597 | 6402 | 7658 |
| [netty/netty](https://github.com/netty/netty) | [netty](https://github.com/netty) | Java | 13422 | 6122 | 8723 |

### Python

stars排行

| Rep | User | Language | Stars | Fork | Commit |
|--------|------|-------|-------|-----------|-----------|
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | [vinta](https://github.com/vinta) | Python | 47930 | 9270 | 1222 |
| [rg3/youtube-dl](https://github.com/rg3/youtube-dl) | [rg3](https://github.com/rg3) | Python | 35575 | 6532 | 16048 |
| [toddmotto/public-apis](https://github.com/toddmotto/public-apis) | [toddmotto](https://github.com/toddmotto) | Python | 35115 | 3319 | 1760 |
| [jakubroztocil/httpie](https://github.com/jakubroztocil/httpie) | [jakubroztocil](https://github.com/jakubroztocil) | Python | 34746 | 2362 | 965 |
| [nvbn/thefuck](https://github.com/nvbn/thefuck) | [nvbn](https://github.com/nvbn) | Python | 34601 | 1723 | 1463 |
| [pallets/flask](https://github.com/pallets/flask) | [pallets](https://github.com/pallets) | Python | 34411 | 10562 | 3205 |
| [django/django](https://github.com/django/django) | [django](https://github.com/django) | Python | 32956 | 13953 | 25601 |
| [tensorflow/models](https://github.com/tensorflow/models) | [tensorflow](https://github.com/tensorflow) | Python | 32262 | 17985 | 2109 |
| [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | [josephmisiti](https://github.com/josephmisiti) | Python | 31793 | 7780 | 1033 |
| [requests/requests](https://github.com/requests/requests) | [requests](https://github.com/requests) | Python | 31508 | 5824 | 5416 |

forks排行

| Rep | User | Language | Stars | Fork | Commit |
|--------|------|-------|-------|-----------|-----------|
| [tensorflow/models](https://github.com/tensorflow/models) | [tensorflow](https://github.com/tensorflow) | Python | 32262 | 17985 | 2109 |
| [shadowsocks/shadowsocks](https://github.com/shadowsocks/shadowsocks) | [shadowsocks](https://github.com/shadowsocks) | Python | 24278 | 15499 | 1 |
| [django/django](https://github.com/django/django) | [django](https://github.com/django) | Python | 32956 | 13953 | 25601 |
| [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) | [scikit-learn](https://github.com/scikit-learn) | Python | 27088 | 13623 | 22684 |
| [ansible/ansible](https://github.com/ansible/ansible) | [ansible](https://github.com/ansible) | Python | 29373 | 10728 | 36562 |
| [pallets/flask](https://github.com/pallets/flask) | [pallets](https://github.com/pallets) | Python | 34411 | 10562 | 3205 |
| [keras-team/keras](https://github.com/keras-team/keras) | [keras-team](https://github.com/keras-team) | Python | 27833 | 10213 | 4442 |
| [udacity/fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) | [udacity](https://github.com/udacity) | Python | 202 | 9370 | 53 |
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | [vinta](https://github.com/vinta) | Python | 47930 | 9270 | 1222 |
| [odoo/odoo](https://github.com/odoo/odoo) | [odoo](https://github.com/odoo) | Python | 9200 | 7889 | 115520 |

### JavaScript

stars排行

| Rep | User | Language | Stars | Fork | Commit |
|--------|------|-------|-------|-----------|-----------|
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | [freeCodeCamp](https://github.com/freeCodeCamp) | JavaScript | 291895 | 13667 | 11334 |
| [facebook/react](https://github.com/facebook/react) | [facebook](https://github.com/facebook) | JavaScript | 92602 | 17473 | 9773 |
| [vuejs/vue](https://github.com/vuejs/vue) | [vuejs](https://github.com/vuejs) | JavaScript | 89447 | 13129 | 2581 |
| [d3/d3](https://github.com/d3/d3) | [d3](https://github.com/d3) | JavaScript | 74472 | 19024 | 4132 |
| [airbnb/javascript](https://github.com/airbnb/javascript) | [airbnb](https://github.com/airbnb) | JavaScript | 68833 | 13127 | 1607 |
| [facebook/react-native](https://github.com/facebook/react-native) | [facebook](https://github.com/facebook) | JavaScript | 62128 | 14129 | 13166 |
| [angular/angular.js](https://github.com/angular/angular.js) | [angular](https://github.com/angular) | JavaScript | 58232 | 28872 | 8755 |
| [jquery/jquery](https://github.com/jquery/jquery) | [jquery](https://github.com/jquery) | JavaScript | 48560 | 15318 | 6316 |
| [nodejs/node](https://github.com/nodejs/node) | [nodejs](https://github.com/nodejs) | JavaScript | 47212 | 9904 | 21744 |
| [facebook/create-react-app](https://github.com/facebook/create-react-app) | [facebook](https://github.com/facebook) | JavaScript | 46391 | 9259 | 1484 |

forks排行

| Rep | User | Language | Stars | Fork | Commit |
|--------|------|-------|-------|-----------|-----------|
| [angular/angular.js](https://github.com/angular/angular.js) | [angular](https://github.com/angular) | JavaScript | 58232 | 28872 | 8755 |
| [udacity/frontend-nanodegree-resume](https://github.com/udacity/frontend-nanodegree-resume) | [udacity](https://github.com/udacity) | JavaScript | 915 | 25814 | 84 |
| [d3/d3](https://github.com/d3/d3) | [d3](https://github.com/d3) | JavaScript | 74472 | 19024 | 4132 |
| [facebook/react](https://github.com/facebook/react) | [facebook](https://github.com/facebook) | JavaScript | 92602 | 17473 | 9773 |
| [jquery/jquery](https://github.com/jquery/jquery) | [jquery](https://github.com/jquery) | JavaScript | 48560 | 15318 | 6316 |
| [nightscout/cgm-remote-monitor](https://github.com/nightscout/cgm-remote-monitor) | [nightscout](https://github.com/nightscout) | JavaScript | 439 | 15228 | 4505 |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | [mrdoob](https://github.com/mrdoob) | JavaScript | 40668 | 15152 | 22927 |
| [facebook/react-native](https://github.com/facebook/react-native) | [facebook](https://github.com/facebook) | JavaScript | 62128 | 14129 | 13166 |
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | [freeCodeCamp](https://github.com/freeCodeCamp) | JavaScript | 291895 | 13667 | 11334 |
| [vuejs/vue](https://github.com/vuejs/vue) | [vuejs](https://github.com/vuejs) | JavaScript | 89447 | 13129 | 2581 |

### 语言使用比例

stars 超过100的

![](https://data2.liuin.cn/2018-04-06-15229847469176.jpg)

stars 超过1000的

![](https://data2.liuin.cn/2018-04-06-15229848318605.jpg)

stars 超过10000的

![](https://data2.liuin.cn/2018-04-06-15229848710272.jpg)

forks 超过100的

![](https://data2.liuin.cn/2018-04-06-15229849187089.jpg)

forks 超过1000的

![](https://data2.liuin.cn/2018-04-06-15229849529776.jpg)

forks 超过10000的

![](https://data2.liuin.cn/2018-04-06-15229849860861.jpg)