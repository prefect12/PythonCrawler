# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['http://www.lagou.com/']

    rules = (
        Rule(LinkExtractor(allow=r'zhaopin/.*'),follow=True),
        Rule(LinkExtractor(allow=r'gongsi/j\d+.html'), callback='parse_company', follow=True),
        Rule(LinkExtractor(allow=r'jobs/d+.html'), callback='parse_jobs', follow=True),
    )

    def parse_company(self,response):
        item = {}

        return item

    def parse_job(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item

    # def parse_job_list(self,response):
    #     item = {}
    #     pageNum = int(response.xpath("//div[@class='pager_container']/a[last()-1]/@data-index").extract())
    #
    #
    #     pass
    #     return item