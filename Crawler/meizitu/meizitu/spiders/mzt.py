# -*- coding: utf-8 -*-

from urllib import parse
import re
import json


import scrapy
from scrapy import Request
from scrapy.loader import  ItemLoader
from meizitu.items import MeizituItem
from meizitu.utils import common
import hashlib

class MztSpider(scrapy.Spider):
    name = 'mzt'
    allowed_domains = ['mzitu.com']
    start_urls = ['https://mzitu.com/']

    def parse(self, response):
        meiziUrls = response.xpath("*//ul[@id='pins']/li//a/@href").extract()

        for url in meiziUrls:
            yield Request(url=url, callback=self.parse_detail,priority=10,headers={'referer': response.url})

        nextPage = response.xpath('*//a[@class="next page-numbers"]/@href').extract_first()
        yield Request(url=nextPage, callback=self.parse,headers={'referer': response.url})

    def parse_detail(self,response):
        item = MeizituItem()

        imgUrl = response.xpath('//div[@class="main-image"]//img/@src').extract_first()
        nextPage = response.xpath('*//div[@class="pagenavi"]/a[last()]/@href').extract_first()
        title = response.xpath('*//h2/text()').extract_first()
        title = re.sub('（\d+）','',title)
        postTime = response.xpath('*//div[@class="main-meta"]/span[last()]/text()').extract_first()
        item['url'] = imgUrl
        item['refeUrl'] = response.url
        item['name'] = title
        item['md5'] = common.get_md5(imgUrl)

        yield Request(url=nextPage, callback=self.parse_detail,priority=20, headers={'referer': response.url})
        yield item

        # , meta = {'item': item}, headers = {'referer': response.url}, dont_filter = True
    #     yield Request(url=imgUrl,callback=self.downLoadImage)
    #
    # def downLoadImage(self,response):
    #     item = response.meta.get('item')
    #
    #     pass
    #     yield item