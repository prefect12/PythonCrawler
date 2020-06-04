# -*- coding: utf-8 -*-
import time
import scrapy
from scrapy import Request
import urllib
from tools.common import get_md5
from items import goodsItem
from scrapy.loader import ItemLoader
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random

import os,sys
import pandas as pd

class TianmaoSpider(scrapy.Spider):
    name = 'tianmao'
    allowed_domains = ['https://list.tmall.com/']
    custom_settings = {
        "COOKIES_ENABLED": False,
        # "AUTOTHROTTLE_ENABLED": True,
        "DOWNLOAD_DELAY": 15,
        # 'REDIRECT_ENABLED':True,
        "RANDOMIZE_DOWNLOAD_DELAY":True,
        'DEFAULT_REQUEST_HEADERS': {
            ':authority': 'list.tmall.com',
            ':scheme': 'https',
            'cookie': 't=5fef69b77b1f07797b87c9f016df82f6; enc=lv6YPlJRrRtj3W%2FE43rrsE1Fys2MXPT0jPq34DaknLwUjbIPQUrvo8LuUonm9DZ8UHH5x2Wz2jDwZXgeL64byg%3D%3D; _tb_token_=f5d3beef6587e; cookie2=1176dd8817bbfa9a07197d56f94f487a; hng=CN%7Czh-CN%7CCNY%7C156; cna=/CQ8E2EcRz8CAWfZp9yXWZWi; dnk=tb829919_44; uc1=cookie14=UoTV7XuLVJ34tw%3D%3D&pas=0&cookie15=UIHiLt3xD8xYTw%3D%3D&cookie21=URm48syIZJfmYzXrEixrAg%3D%3D&existShop=false&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D; uc3=lg2=W5iHLLyFOGW7aA%3D%3D&id2=UoH8VdwqvbMCzA%3D%3D&nk2=F5RNZ%2Bnk6R%2FsqM0%3D&vt3=F8dBxGerloIhAeRTbbo%3D; tracknick=tb829919_44; lid=tb829919_44; uc4=nk4=0%40FY4GsEkrFR4kcfc%2Bu8jzBfjoCMLTrA%3D%3D&id4=0%40UOnjlS31%2F2tX3xw2RCUFhl0VWo1H; lgc=tb829919_44; sgcookie=EpeU5wvShwb4w%2FmdxzLI%2B; csg=df9b31b8; _med=dw:1920&dh:1080&pw:1920&ph:1080&ist:0; cq=ccp%3D1; pnm_cku822=098%23E1hvtQvUvbpvUQCkvvvvvjiPnLzhgjn8PLqpsjnEPmPvQjrUR2sZ0jlWPLL90j3bRLsU2QhvCPMMvvvCvpvVvUCvpvvvmphvLv89O7ha%2B2Kzr2E9ZRAn%2BbeAhj3mAXZTKFyzOvxrz8TJ%2Bul68fmxdXuK5kx%2FzjZ7%2Bu0fjomUFfwzhBODNr1l5d8re160kU6BHdoJEcTtvpvIvvCvz9vvvmWvvhZtvvmCR9vvBGwvvvUwvvCj1Qvvv3QvvhcEvvmCaIyCvvOCvhE2gWAivpvUvvCCW%2F5GMC%2BtvpvhvvCvp8wCvvpvvhHh; res=scroll%3A1387*5461-client%3A1387*884-offset%3A1387*5461-screen%3A1920*1080; l=eBQlk8UmQ02EMgwLBOfwnurza77tsIRAguPzaNbMiOCPOefp5LvcWZvu_2L9CnGVh6-kR35QyF69BeYBqS475O9StBALuzDmn; isg=BNbWf8u6lHYBmqDXeAMsRYtIJ4zYdxqxnEKYYkA_xblVA3adqANUwJpxn5_vqxLJ',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-AU;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }
    }

    def __init__(self,item=None,*args,**kwargs):
        super(TianmaoSpider,self).__init__(*args,*kwargs)
        self.item = item
        self.url = 'https://list.tmall.com/search_product.htm?s=%d&q=%s&sort=s&style=g&type=pc'
        # self.startUrl = self.url%(0,self.item)
        self.path = './%s.csv'%(item)
        self.createFile()

        # print(self.startUrl)

    def createFile(self):
        if not os.path.exists(self.path):
            col_names = ['itemTitle','itemPrice','itemShop','itemUrl','itemSale','itemComment','shopUrl','itemHash']

            df = pd.DataFrame(columns = col_names)
            df.to_csv(path_or_buf = self.path ,encoding='GB18030',index=False)

    def start_requests(self):
        yield Request(url='https://list.tmall.com/search_product.htm?q=' + self.item)

        # for i in range(1,100):
        #     yield Request(url=self.url%(60*i,self.item))

    def parse(self, response):
        'https://list.tmall.com/search_product.htm?s=0&q=%E6%8B%96%E9%9E%8B&sort=s&style=g&type=pc'

        items = response.xpath('//div[@class="product-iWrap"]')
        for item in items:
            goodsitem = goodsItem()
            goodsitem['itemTitle'] = item.xpath('.//p[@class="productTitle"]//a/@title').extract_first()
            goodsitem['itemPrice'] = item.xpath('.//p[@class="productPrice"]//em/@title').extract_first()
            goodsitem['itemShop'] = item.xpath('.//div[@class="productShop"]/a/text()').extract_first()
            goodsitem['itemUrl'] = item.xpath('.//p[@class="productTitle"]//a/@href').extract_first()
            goodsitem['shopUrl'] = item.xpath('.//div[@class="productShop"]/a/@href').extract_first()
            goodsitem['itemSale'] = item.xpath('./p[@class="productStatus"]//em/text()').extract_first()
            goodsitem['itemComment'] = item.xpath('./p[@class="productStatus"]//a/text()').extract_first()
            goodsitem['itemHash'] = get_md5(goodsitem['itemUrl'])
            yield {'path': self.path, 'item': goodsitem}

        self.browser = webdriver.Chrome('./chromedriver.exe')
        self.browser.get(response.url)
        time.sleep(3)

        jsCode = "var q=document.documentElement.scrollTop=50000"
        self.browser.execute_script(jsCode)
        time.sleep(10)
        nextPageElement = self.browser.find_element_by_xpath('//a[@class="ui-page-next"]')
        ActionChains(self.browser).move_to_element(nextPageElement).perform()
        time.sleep(10)
        try:
            nextPage = self.browser.find_element_by_xpath('//a[@class="ui-page-next"]').get_attribute('href')
        except Exception as e:
            print(e)
            pass
        # urlHeader = 'https://list.tmall.com/search_product.htm?'
        # # nextPage = response.xpath('//a[@class="ui-page-next"]/@href').extract_first()
        # url = urlHeader + nextPage
        # print(url)

        yield Request(url = nextPage,headers={'referer': response.url},dont_filter=True,callback=self.parse)