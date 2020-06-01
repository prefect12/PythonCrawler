# -*- coding: utf-8 -*-

# Scrapy settings for lagouRedis project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lagouRedis'

SPIDER_MODULES = ['lagouRedis.spiders']
NEWSPIDER_MODULE = 'lagouRedis.spiders'

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lagouRedis (+http://www.yourdomain.com)'

# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'ttext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en-AU;q=0.8,en;q=0.7',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
#     'accept-encoding': 'gzip, deflate, br',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'upgrade-insecure-requests': '1',
#     'cookie': 'user_trace_token=20200417145708-d7dd053d-bc57-4e38-8da7-287d117fa771; _ga=GA1.2.1343912069.1587106629; LGUID=20200417145709-06f113ef-7c80-4329-a91d-1c3f36da9b8a; LG_LOGIN_USER_ID=83bde5753abfeee5cd33b6e2060ca3e4ce0c8dc8d7a4df49494fdf054e6768e9; LG_HAS_LOGIN=1; _putrc=77DDAF8DB8F01234123F89F2B170EADC; JSESSIONID=ABAAAECAAEBABII84957BD25CC50631E7564052D597FB2B; login=true; unick=%E6%AD%A6%E6%96%87%E9%9F%AC; WEBTJ-ID=20200417145748-17186edde26118-049a2c9b6afc9b-5313f6f-2073600-17186edde279cb; sensorsdata2015session=%7B%7D; RECOMMEND_TIP=true; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1589341634,1589603603; X_MIDDLE_TOKEN=37ab75d31d8951347cb6b18ea29777ed; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2212157285%22%2C%22%24device_id%22%3A%2217186ed866f2d1-09bdde21c8c025-5313f6f-2073600-17186ed8670a58%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2281.0.4044.122%22%7D%2C%22first_id%22%3A%2217186ed866f2d1-09bdde21c8c025-5313f6f-2073600-17186ed8670a58%22%7D; index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.851687148.1590983350; LGSID=20200601160105-7e99468d-0880-4563-b084-a402bc604271; TG-TRACK-CODE=index_navigation; SEARCH_ID=186e382dec6c4034a5db037dbda8ff0a; _gat=1; X_HTTP_TOKEN=b69a11f65f41a6fd2227001951757f54d84d3f65a7; LGRID=20200601182702-3b8b9362-971f-4026-b17e-b3948cb224ed; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1591007221'
# }

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lagouRedis.middlewares.LagouredisSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'lagouRedis.middlewares.LagouredisDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'lagouRedis.pipelines.LagouredisPipeline': 100,
    'lagouRedis.pipelines.jobPipeline':50,
    'lagouRedis.pipelines.companyPipeline':100,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# DOWNLOAD_DELAY = 3
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
