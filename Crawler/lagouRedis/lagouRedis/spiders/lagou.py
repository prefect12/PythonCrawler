# -*- coding: utf-8 -*-
import scrapy

from scrapy_redis.spiders import RedisSpider
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items import jobItem,companyItem
from scrapy import Request
from items import JobLagouItemLoader
from scrapy.loader import ItemLoader
from scrapy.loader import  ItemLoader
from scrapy_redis.spiders import RedisCrawlSpider


class LagouSpider(RedisSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['http://www.lagou.com/']

    cookie_list = 'user_trace_token=20200417145708-d7dd053d-bc57-4e38-8da7-287d117fa771; _ga=GA1.2.1343912069.1587106629; LGUID=20200417145709-06f113ef-7c80-4329-a91d-1c3f36da9b8a; LG_LOGIN_USER_ID=83bde5753abfeee5cd33b6e2060ca3e4ce0c8dc8d7a4df49494fdf054e6768e9; LG_HAS_LOGIN=1; _putrc=77DDAF8DB8F01234123F89F2B170EADC; JSESSIONID=ABAAAECAAEBABII84957BD25CC50631E7564052D597FB2B; login=true; unick=%E6%AD%A6%E6%96%87%E9%9F%AC; WEBTJ-ID=20200417145748-17186edde26118-049a2c9b6afc9b-5313f6f-2073600-17186edde279cb; sensorsdata2015session=%7B%7D; RECOMMEND_TIP=true; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1589341634,1589603603; X_MIDDLE_TOKEN=37ab75d31d8951347cb6b18ea29777ed; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2212157285%22%2C%22%24device_id%22%3A%2217186ed866f2d1-09bdde21c8c025-5313f6f-2073600-17186ed8670a58%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2281.0.4044.122%22%7D%2C%22first_id%22%3A%2217186ed866f2d1-09bdde21c8c025-5313f6f-2073600-17186ed8670a58%22%7D; index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.851687148.1590983350; SEARCH_ID=77589cedd1624a269bc81e24415ff36f; TG-TRACK-CODE=index_hotjob; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F7231209.html%3Fshow%3Df6bb4cd3557349b9a93323256c5c701f; LGSID=20200602222504-0ab6af86-ff04-4165-8245-f5f21b8f21a8; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Futrack%2FtrackMid.html%3Ff%3Dhttps%253A%252F%252Fwww.lagou.com%252Fjobs%252F7231209.html%253Fshow%253Df6bb4cd3557349b9a93323256c5c701f%26t%3D1591099294%26%5Fti%3D1; _gat=1; X_HTTP_TOKEN=b69a11f65f41a6fd5259011951757f54d84d3f65a7; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1591109525; LGRID=20200602225205-8e42e5c1-87f5-46c1-8783-ec1458e31a79'

    custom_settings = {
        "COOKIES_ENABLED": False,
        "AUTOTHROTTLE_ENABLED": True,
        "DOWNLOAD_DELAY": 15,
        "RANDOMIZE_DOWNLOAD_DELAY":True,
        'DEFAULT_REQUEST_HEADERS': {
            ':authority': 'www.lagou.com',
            ':scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-AU;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'www.lagou.com',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }
    }


    def parse(self, response):
        jobPagelist = response.xpath('//div[@class="mainNavs"]//a/@href').extract()
        for jobPage in jobPagelist:
            yield Request(url=jobPage,callback=self.parseJoblist,headers={'referer': response.url},dont_filter=True,priority=50)

    def parseJoblist(self,response):
        nextPage = response.xpath("//a[contains(text(),'下一页')]/@href").extract_first()
        jobs = response.xpath("//li[@class='con_list_item default_list']//a[@class='position_link']/@href").extract()
        for job in jobs:
            yield Request(url=job,callback=self.parseJob,headers={'referer': response.url},dont_filter=True,priority=100)
        yield Request(url=nextPage,callback=self.parseJoblist,headers={'referer': response.url},dont_filter=True,priority=50)




    def parseJob(self,response):

        itemLoader = JobLagouItemLoader(item=jobItem(),response=response)

        itemLoader.add_xpath('jobName','//div[@class="job-name"]/@title')
        itemLoader.add_xpath('jobSalary','//dd[@class="job_request"]//span[1]/text()')
        itemLoader.add_xpath('jobLocation','//dd[@class="job_request"]//span[2]/text()')
        itemLoader.add_xpath('jobExperience','//dd[@class="job_request"]//span[3]/text()')
        itemLoader.add_xpath('jobDegree','//dd[@class="job_request"]//span[4]/text()')
        itemLoader.add_xpath('jobType','//dd[@class="job_request"]//span[5]/text()')
        itemLoader.add_value('jobDetail',''.join(response.xpath('//dl[@class="job_detail"]//text()').extract()))
        # itemLoader.add_xpath('jobDetail','//dl[@class="job_detail"]//text()')
        itemLoader.add_xpath('jobCompanyName','//em[@class="fl-cn"]/text()')
        itemLoader.add_value('jobUrl',response.url)

        jobitem = itemLoader.load_item()
        yield jobitem

        companyUrl = response.xpath('//a[@data-lg-tj-track-code="jobs_logo"]/@href').extract_first()
        yield Request(url=companyUrl,callback=self.parseCompany,headers={'referer': response.url},dont_filter=True,priority=100)


        # jobName = response.xpath('//h1[@class="name"]/text()').extract_first()
        # jobSalary = response.xpath('//dd[@class="job_request"]//span[1]/text()').extract_first()
        # jobLocation = response.xpath('//dd[@class="job_request"]//span[2]/text()').extract_first()
        # jobExperience = response.xpath('//dd[@class="job_request"]//span[3]/text()').extract_first()
        # jobDegree = response.xpath('//dd[@class="job_request"]//span[4]/text()').extract_first()
        # jobType = response.xpath('//dd[@class="job_request"]//span[5]/text()').extract_first()
        # jobDetail = ' '.join(response.xpath('//dd[@class="job_bt"]//text()').extract())
        # jobCompanyName = response.xpath('//em[@class="fl-cn"]/text()').extract_first()
        # jobUrl = response.url
        #
        # jobitem['jobUrl'] = jobUrl
        # jobitem['jobName'] = jobName
        # jobitem['jobSalary'] = jobSalary
        # jobitem['jobLocation'] = jobLocation
        # jobitem['jobExperience'] = jobExperience
        # jobitem['jobDegree'] = jobDegree
        # jobitem['jobType'] = jobType
        # jobitem['jobDetail'] = jobDetail
        # jobitem['jobCompanyName'] = jobCompanyName



    def parseCompany(self,response):

        itemLoader = JobLagouItemLoader(item = companyItem(),response=response)

        itemLoader.add_value('companyUrl',response.url)
        itemLoader.add_xpath('companyName','//h1[@class="company_main_title"]/a/text()')
        itemLoader.add_xpath('companyRealName','//h1[@class="company_main_title"]/a/@title')
        itemLoader.add_xpath('companyHireNumber','//div[@class="company_data"]/ul/li[1]/strong/text()')
        itemLoader.add_xpath('CVprocessingRate','//div[@class="company_data"]/ul/li[2]/strong/text()')
        itemLoader.add_xpath('CVprocessingDay','//div[@class="company_data"]/ul/li[3]/strong/text()')
        itemLoader.add_xpath('commentNumebr','//div[@class="company_data"]/ul/li[4]/strong/text()')
        itemLoader.add_xpath('lastLoginDate','//div[@class="company_data"]/ul/li[5]/strong/text()')
        # companyItemScale = response.xpath('//div[@class="item_container"]//ul/li[3]//text()').extract()
        itemLoader.add_xpath('companyScale','//div[@class="item_container"]//ul/li[3]//text()')
        itemLoader.add_xpath('companyLocation','//div[@class="item_container"]//ul/li[4]//text()')
        itemLoader.add_xpath('companyIntroduce','//span[@class="company_content"]//text()')
        # itemLoader.add_xpath('companyDeveloping','//ul[@class="history_ul"]//text()')

        companyitem = itemLoader.load_item()

        yield companyitem

        # companyUrl = response.url
        # companyName = response.xpath('//h1[@class="company_main_title"]/a/text()').extract()
        # companyRealName = response.xpath('//h1[@class="company_main_title"]/a/@title').extract_first()
        # companyHireNumber = response.xpath("//div[@class='company_data']/ul/li[1]/strong/text()").extract_first()
        # CVprocessingRate = response.xpath('//div[@class="company_data"]/ul/li[2]/strong/text()').extract_first()
        # CVprocessingDay = response.xpath('//div[@class="company_data"]/ul/li[3]/strong/text()').extract_first()
        # commentNumebr = response.xpath('//div[@class="company_data"]/ul/li[4]/strong/text()').extract_first()
        # lastLoginDate = response.xpath('//div[@class="company_data"]/ul/li[5]/strong/text()').extract_first()
        # companyScale = response.xpath('//div[@id="basic_container"]//ul/li[3]//text()').extract_first()
        # companyLocation = response.xpath('//div[@id="basic_container"]//ul/li[4]//text()').extract_first()
        # companyIntroduce = ' '.join(response.xpath('//span[@class="company_content"]//text()').extract())
        # companyDeveloping = ' '.join(response.xpath("//ul[@class='history_ul']//text()").extract())

        # companyitem['companyUrl'] = companyUrl
        # companyitem['companyName'] = companyName
        # companyitem['companyRealName'] = companyRealName
        # companyitem['companyHireNumber'] = companyHireNumber
        # companyitem['CVprocessingRate'] = CVprocessingRate
        # companyitem['CVprocessingDay'] = CVprocessingDay
        # companyitem['commentNumebr'] = commentNumebr
        # companyitem['lastLoginDate'] = lastLoginDate
        # companyitem['companyScale'] = companyScale
        # companyitem['companyLocation'] = companyLocation
        # companyitem['companyIntroduce'] = companyIntroduce
        # companyitem['companyDeveloping'] = companyDeveloping

