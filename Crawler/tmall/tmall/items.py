# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TmallItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class goodsItem(scrapy.Item):
    itemTitle = scrapy.Field()
    itemPrice = scrapy.Field()
    itemShop = scrapy.Field()
    itemUrl = scrapy.Field()
    itemSale = scrapy.Field()
    itemComment = scrapy.Field()
    shopUrl = scrapy.Field()
    itemHash = scrapy.Field()