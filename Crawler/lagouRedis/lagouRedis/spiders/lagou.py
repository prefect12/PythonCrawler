# -*- coding: utf-8 -*-
import scrapy

from scrapy_redis.spiders import RedisSpider
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items import jobItem,companyItem
from scrapy import Request
from scrapy.loader import  ItemLoader
from scrapy_redis.spiders import RedisCrawlSpider

# class MySpider(RedisSpider):
#     name = 'myspider'
#
#     def parse(self, response):
#         # do stuff
#         pass

class LagouSpider(RedisSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['http://www.lagou.com/']


    cookie_list = "BAIDUID=49CD7FFD2795459E5636D68C031B954A:FG=1;BDORZ=B490B5EBF6F3CD402E515D22BCDA1598;BIDUPSID=49CD7FFD2795459E5636D68C031B954A;HMACCOUNT=74B79914C73B8BB4;HMVT=6bcd52f51e9b3dce32bec4a3997715ac|1542536300|;H_PS_PSSID=1464_21089_26350;Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1542536602;Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1542528328,1542531922;JSESSIONID=ABAAABAAAGFABEF8CAD2AB2C87A80463EDFBEFE83F99314;LGRID=20181118182321-f9106e94-eb1b-11e8-8955-5254005c3644;LGSID=20181118182258-ebc43aeb-eb1b-11e8-a642-525400f775ce;LGUID=20181118160527-b5880c53-eb08-11e8-a631-525400f775ce;LG_LOGIN_USER_ID=e9648477163e6d25128836cde213a8348f196851cc08f5b48dae8f3ba92ce173;PSINO=6;PSTM=1542536505;TG-TRACK-CODE=index_user;X_HTTP_TOKEN=9a090316d567b03a792f6a0bd9c27711;_ga=GA1.2.910298970.1542528328;_gid=GA1.2.138938673.1542528328;_putrc=920F2336999B0934123F89F2B170EADC;delPer=0;gate_login_token=48191040edb4aafbb49d06fe8453642fb39167bf9c61f0ee1ab41ee15ba58cc0;hasDeliver=12;index_location_city=%E5%B9%BF%E5%B7%9E;login=true;sajssdk_2015_cross_new_user=1;sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216725dab2a41f4-03e196f0ddfc75-e313761-1631252-16725dab2a6637%22%2C%22%24device_id%22%3A%2216725dab2a41f4-03e196f0ddfc75-e313761-1631252-16725dab2a6637%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D;showExpriedCompanyHome=1;showExpriedIndex=1;showExpriedMyPublish=1;unick=%E6%9D%8E%E9%93%AD%E8%BE%89;user_trace_token=20181118160527-b5880957-eb08-11e8-a631-525400f775ce"

    custom_settings = {
        "COOKIES_ENABLED": False,
        "DOWNLOAD_DELAY": 10,
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
             'cookie': 'user_trace_token=20200417145708-d7dd053d-bc57-4e38-8da7-287d117fa771; _ga=GA1.2.1343912069.1587106629; LGUID=20200417145709-06f113ef-7c80-4329-a91d-1c3f36da9b8a; LG_LOGIN_USER_ID=83bde5753abfeee5cd33b6e2060ca3e4ce0c8dc8d7a4df49494fdf054e6768e9; LG_HAS_LOGIN=1; _putrc=77DDAF8DB8F01234123F89F2B170EADC; JSESSIONID=ABAAAECAAEBABII84957BD25CC50631E7564052D597FB2B; login=true; unick=%E6%AD%A6%E6%96%87%E9%9F%AC; WEBTJ-ID=20200417145748-17186edde26118-049a2c9b6afc9b-5313f6f-2073600-17186edde279cb; sensorsdata2015session=%7B%7D; RECOMMEND_TIP=true; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1589341634,1589603603; X_MIDDLE_TOKEN=37ab75d31d8951347cb6b18ea29777ed; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2212157285%22%2C%22%24device_id%22%3A%2217186ed866f2d1-09bdde21c8c025-5313f6f-2073600-17186ed8670a58%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2281.0.4044.122%22%7D%2C%22first_id%22%3A%2217186ed866f2d1-09bdde21c8c025-5313f6f-2073600-17186ed8670a58%22%7D; index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.851687148.1590983350; LGSID=20200601160105-7e99468d-0880-4563-b084-a402bc604271; TG-TRACK-CODE=index_navigation; SEARCH_ID=186e382dec6c4034a5db037dbda8ff0a; _gat=1; X_HTTP_TOKEN=b69a11f65f41a6fd2227001951757f54d84d3f65a7; LGRID=20200601182702-3b8b9362-971f-4026-b17e-b3948cb224ed; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1591007221',
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }
    }


    def parse(self, response):
        jobPagelist = response.xpath('//div[@class="mainNavs"]//a/@href').extract()
        for jobPage in jobPagelist[2:3]:
            yield Request(url=jobPage,callback=self.parseJoblist,headers={'referer': response.url},dont_filter=True)

    def parseJoblist(self,response):
        nextPage = response.xpath("//a[contains(text(),'下一页')]/@href").extract_first()
        jobs = response.xpath("//li[@class='con_list_item default_list']//a[@class='position_link']/@href").extract()
        for job in jobs[4:5]:
            yield Request(url=job,callback=self.parseJob,headers={'referer': response.url},dont_filter=True)
        # yield Request(url=nextPage,callback=self.parseJoblist,headers={'referer': response.url},dont_filter=True)




    def parseJob(self,response):
        jobitem = jobItem()

        jobName = response.xpath('//h1[@class="name"]/text()').extract_first()
        jobSalary = response.xpath('//dd[@class="job_request"]//span[1]/text()').extract_first()
        jobLocation = response.xpath('//dd[@class="job_request"]//span[2]/text()').extract_first()
        jobExperience = response.xpath('//dd[@class="job_request"]//span[3]/text()').extract_first()
        jobDegree = response.xpath('//dd[@class="job_request"]//span[4]/text()').extract_first()
        jobType = response.xpath('//dd[@class="job_request"]//span[5]/text()').extract_first()
        jobDetail = ' '.join(response.xpath('//dd[@class="job_bt"]//text()').extract())
        jobCompanyName = response.xpath('//em[@class="fl-cn"]/text()').extract_first()

        jobitem['jobName'] = jobName
        jobitem['jobSalary'] = jobSalary
        jobitem['jobLocation'] = jobLocation
        jobitem['jobExperience'] = jobExperience
        jobitem['jobDegree'] = jobDegree
        jobitem['jobType'] = jobType
        jobitem['jobDetail'] = jobDetail
        jobitem['jobCompanyName'] = jobCompanyName

        # yield {'j':jobItem}

        companyUrl = response.xpath('//a[@data-lg-tj-track-code="jobs_logo"]/@href').extract_first()
        yield Request(url=companyUrl,callback=self.parseCompany,headers={'referer': response.url},dont_filter=True)


    def parseCompany(self,response):
        companyitem = companyItem()

        companyName = response.xpath('//h1[@class="company_main_title"]/a/text()').extract()
        companyRealName = response.xpath('//h1[@class="company_main_title"]/a/@title').extract_first()
        companyHireNumber = response.xpath("//div[@class='company_data']/ul/li[1]/strong/text()").extract_first()
        CVprocessingRate = response.xpath('//div[@class="company_data"]/ul/li[2]/strong/text()').extract_first()
        CVprocessingDay = response.xpath('//div[@class="company_data"]/ul/li[3]/strong/text()').extract_first()
        commentNumebr = response.xpath('//div[@class="company_data"]/ul/li[4]/strong/text()').extract_first()
        lastLoginDate = response.xpath('//div[@class="company_data"]/ul/li[5]/strong/text()').extract_first()
        companyScale = response.xpath('//div[@id="basic_container"]//ul/li[3]//text()').extract_first()
        companyLocation = response.xpath('//div[@id="basic_container"]//ul/li[4]//text()').extract_first()
        companyIntroduce = ' '.join(response.xpath('//span[@class="company_content"]//text()').extract())
        companyDeveloping = ' '.join(response.xpath("//ul[@class='history_ul']//text()").extract())

        companyitem['companyName'] = companyName
        companyitem['companyRealName'] = companyRealName
        companyitem['companyHireNumber'] = companyHireNumber
        companyitem['CVprocessingRate'] = CVprocessingRate
        companyitem['CVprocessingDay'] = CVprocessingDay
        companyitem['commentNumebr'] = commentNumebr
        companyitem['lastLoginDate'] = lastLoginDate
        companyitem['companyScale'] = companyScale
        companyitem['companyLocation'] = companyLocation
        companyitem['companyIntroduce'] = companyIntroduce
        companyitem['companyDeveloping'] = companyDeveloping

        yield companyitem