
# 个人Python爬虫项目展示

项目介绍：
项目主要分为两个部分，第一部分是爬虫项目（Crawler文件夹）。
第二部分是编写代码时碰到的一些反爬机制以及思考过程，和最后的反反爬方法（anti-anti-Crawler）。  
还有一个[文件夹](/tools)用来存放一些脚本和工具。



****  
### 爬虫项目
其中[淘宝网抓取](/Crawler/tb)，[求职网数据分析](/Crawler/jobFinder)，[拉钩分布式爬虫](/Crawler/lagouRedis)有详细介绍。

|项目|简介|技术栈|
|---|---|---
|[淘宝网抓取](/Crawler/tb)|通过关键字搜索并且获取淘宝商品数据，存入csv文档|Selenium反爬
|[求职网数据分析](/Crawler/jobFinder)|抓取前程无忧，实习僧招聘网站，存入csv进行数据清洗，降维，可视化|爬虫:多线程 + requests + bs4/lxml  可视化：jieba + W2V + PAC降维 + matplotlib + wordCloud
|[拉钩分布式爬虫](/Crawler/lagouRedis)|拉勾网抓取，使用分布式框架，支持整站抓取，增量抓取，拉钩反爬|Scrapy-Redis
|[拉勾网全站爬虫](/Crawler/job51Scrapy)|抓取职位以及公司数据，可以存入csv文件或数据库|Scrapy + 整站抓取
|[图片网站图片爬取](/Crawler/meizitu)|图片网站整站抓取+定期增量抓取|Scrapy + requests + 增量抓取
|[Steam热门游戏好评差评数量抓取](/Crawler/steamWeekReport)|Steam抓取当前热门游戏的好评/差评数量，通过selenium突破认证并抓取canvas元素| Selenium + requests + bs4
|[天猫抓取](/Crawler/tmall)|通过selenium突破反爬，抓取天猫商品数据存入csv|Selenium反爬


****
### 反爬项目

具体分析过程以及流程图可以点开文件夹，其中有详细介绍。
重点解释了，[知乎登陆倒立文字英文验证码突破](/anti-anti-Crawler/知乎倒立文字英文验证码突破)，[bilibili滑动验证码突破](/anti-anti-Crawler/bilibili滑动验证码突破)

|项目|技巧|
|---|---
|[bilibili滑动验证码突破](/anti-anti-Crawler/bilibili滑动验证码突破)|Selenium模拟操作
|[去哪儿网css偏移反爬突破](/anti-anti-Crawler/去哪儿网css偏移反爬突破)|css分析
|[实习僧字体映射反爬突破](/anti-anti-Crawler/实习僧字体映射反爬突破)|css分析
|[知乎登陆倒立文字英文验证码突破](/anti-anti-Crawler/知乎倒立文字英文验证码突破)|selenium+验证码识别(zheye+超级鹰)


****
### 工具(/tools)

|工具|作用|
|---|---
|屏幕坐标获取器|使用selenium分析滑动验证码时识别距离
|IP池构建|抓取免费IP代理存入数据库并检查可用性
