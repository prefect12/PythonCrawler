
# 个人Python爬虫项目展示

项目介绍：
项目主要分为两个部分，第一部分是爬虫项目（Crawler文件夹）。
第二部分是编写代码时碰到的一些反爬机制以及思考过程，和最后的反反爬方法（anti-anti-Crawler）。
还有一个[文件夹](/tools)用来存放一些脚本和工具。

项目文件夹内有详细介绍

****  
### 爬虫项目  

|项目|项目文件夹|技术栈|
|---|---|---
|[前程无忧求职网爬虫](/Crawler/job51Scrapy)|job51Scrapy|Scrapy
|[淘宝网抓取](/Crawler/tb)|tb|Selenium反爬
|[求职网数据分析](/Crawler/jobFinder)|jobFinder|爬虫:多线程+requests + bs4/lxml  可视化：jieba+matplotlib+wordCloud
|[拉钩分布式爬虫](/Crawler/lagouRedis)|lagouRedis|Scrapy-Redis
|[图片网站图片爬取](/Crawler/meizitu)|meizitu|Scrapy + requests + 增量抓取
|[Steam热门游戏好评差评数量抓取](/Crawler/steamWeekReport)|steamWeekReport| Selenium + requests + bs4
|[天猫抓取](/Crawler/tmall)|tmall|Selenium反爬


****
### 反爬项目

|项目|项目名|
|---|---
|[bilibili滑动验证码突破](/anti-anti-Crawler/bilibili滑动验证码突破)|Selenium
|[去哪儿网css偏移反爬突破](/anti-anti-Crawler/去哪儿网css偏移反爬突破)|css分析
|[实习僧字体映射反爬突破](/anti-anti-Crawler/实习僧字体映射反爬突破)|css分析
|[知乎登陆倒立文字英文验证码突破](/anti-anti-Crawler/知乎倒立文字英文验证码突破)|selenium+zheye+超级鹰


****
