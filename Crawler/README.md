# 爬虫项目文件夹

****  
### 爬虫项目
其中[求职网数据分析](/Crawler/jobFinder)，[淘宝网抓取](/Crawler/tb)，[拉钩分布式爬虫](/Crawler/lagouRedis)有详细介绍。

|项目|简介|技术栈|
|---|---|---
|[求职网数据分析](/Crawler/jobFinder)|抓取前程无忧，实习僧招聘网站，存入csv进行数据清洗，降维，可视化|爬虫:多线程 + requests + bs4/lxml  可视化：jieba + W2V + PAC降维 + matplotlib + wordCloud
|[淘宝网抓取](/Crawler/tb)|通过关键字搜索并且获取淘宝商品数据，存入csv文档|Selenium反爬
|[拉钩分布式爬虫](/Crawler/lagouRedis)|拉勾网抓取，使用分布式框架，支持整站抓取，增量抓取，拉钩反爬|Scrapy-Redis
|[拉勾网全站爬虫](/Crawler/job51Scrapy)|抓取职位以及公司数据，可以存入csv文件或数据库|Scrapy + 规则整站抓取
|[图片网站图片爬取](/Crawler/meizitu)|图片网站整站抓取+定期增量抓取|Scrapy + requests + 增量抓取
|[Steam热门游戏好评差评数量抓取](/Crawler/steamWeekReport)|Steam抓取当前热门游戏的好评/差评数量，通过selenium突破认证并抓取canvas元素| Selenium + requests + bs4
|[天猫抓取](/Crawler/tmall)|通过selenium突破反爬，抓取天猫商品数据存入csv|Selenium反爬
