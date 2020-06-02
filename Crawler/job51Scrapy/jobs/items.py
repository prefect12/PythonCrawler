# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = scrapy.Field()
    jobUrl = scrapy.Field()
    jobCity = scrapy.Field()
    jobLocation = scrapy.Field()
    salary = scrapy.Field()
    postDate = scrapy.Field()
    experience = scrapy.Field()
    degree = scrapy.Field()
    welfare = scrapy.Field()
    jobDesc = scrapy.Field()

    companyName = scrapy.Field()



class CompaniesItem(scrapy.Item):
    companyName = scrapy.Field()
    companyType = scrapy.Field()
    companyScale = scrapy.Field()
    companyField = scrapy.Field()
    companyLocation = scrapy.Field()
    companyInfo = scrapy.Field()
    companyUrl = scrapy.Field()
    companyHash = scrapy.Field()