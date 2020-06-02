import re
import json


import scrapy
from scrapy import Request
from scrapy.loader import  ItemLoader
from items import JobsItem,CompaniesItem
from tools.stringProcess import listProcess
from tools.common import get_md5
import time
from scrapy.spiders import  CrawlSpider
import hashlib
from scrapy import signals
from fake_useragent import UserAgent
from tools.crawl_xici import GetIP
from selenium import webdriver
from scrapy.http import HtmlResponse
import time
from scrapy.xlib.pydispatch import dispatcher

class Job51Spider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['search.51job.com','jobs.51job.com']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE,2,1.html?']

    # def __init__(self):
    #     self.browser = webdriver.Chrome('I:\PythonHighLevelScrapy\\notes\ScrapyPoroject\jobs\jobs\chromedriver.exe')
    #     super(Job51Spider,self).__init__()
    #     dispatcher.connect(self.spider_closed,signals.spider_closed)

    # def spider_closed(self,spider):
    #     print('spider closed')
    #     self.browser.quit()

    def parse(self, response):
        totalPages = int(response.xpath("//div[@class='p_in']//input[@id='hidTotalPage']/@value").extract_first())
        url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE,2,{page}.html?'
        for pageNum in range(1,totalPages):
            yield Request(url=url.format(page = pageNum),callback=self.parse_page,headers={'referer': response.url},dont_filter=True)

    def parse_page(self,response):
        jobNodes = response.xpath("//div[@class='dw_table']//div[@class='el']")[1:]
        for job in jobNodes:
            jobItem = JobsItem()
            jobItem["jobName"] = job.xpath(".//p/span/a/@title").extract_first()
            jobItem['jobCity'] = job.xpath('.//span[@class="t3"]/text()').extract_first()
            jobItem['jobUrl'] = job.xpath('.//p/span/a/@href').extract_first()
            jobItem['salary'] = job.xpath('.//span[@class="t4"]/text()').extract_first()
            jobItem['postDate'] = str(time.localtime()[0])+ '-' + job.xpath('.//span[@class="t5"]/text()').extract_first()
            yield Request(url = jobItem['jobUrl'],callback=self.parse_detail,meta={'jobItem':jobItem})



    def parse_detail(self,response):
        companyItem = CompaniesItem()
        jobItem = response.meta.get('jobItem')

        itemList = response.xpath("//p[@class='msg ltype']/text()").extract()
        itemList = listProcess(itemList)
        jobItem['experience'] = itemList[1]
        jobItem['degree'] = itemList[2]
        jobItem['welfare'] = ' '.join(response.xpath('//span[@class="sp4"]/text()').extract())
        jobItem['jobLocation'] = response.xpath('//div[@class="bmsg inbox"]/p/text()').extract_first()
        itemList = response.xpath('//div[@class="bmsg job_msg inbox"]//text()').extract()
        itemList = listProcess(itemList)
        jobItem['jobDesc'] = ' '.join(itemList)
        companyName = response.xpath("*//div[@class='tCompany_sidebar']//a//p/@title").extract_first()
        jobItem['companyName'] = companyName

        companyItem['companyName'] = companyName
        inforList = response.xpath("*//div[@class='tCompany_sidebar']//div[@class='com_tag']/p/@title").extract()
        companyItem['companyType'] = inforList[0]
        companyItem['companyScale'] = inforList[1]
        companyItem['companyField'] = inforList[2]
        companyItem['companyLocation'] = response.xpath('//div[@class="bmsg inbox"]/p/text()').extract_first()

        inforList = response.xpath("*//div[@class='tmsg inbox']/text()").extract()
        itemList = listProcess(inforList)
        companyItem['companyInfo'] = ' '.join(itemList)

        companyItem['companyUrl'] = response.xpath('*//div[@class="com_msg"]/a/@href').extract_first()
        companyItem['companyHash'] = get_md5(companyItem['companyName'])

        yield {'jobItem':jobItem,'companyItem':companyItem}


