# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouredisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class jobItem(scrapy.Item):
    jobName = scrapy.Field()
    jobSalary = scrapy.Field()
    jobLocation = scrapy.Field()
    jobExperience = scrapy.Field()
    jobDegree = scrapy.Field()
    jobType = scrapy.Field()
    jobDetail = scrapy.Field()
    jobCompanyName = scrapy.Field()

class companyItem(scrapy.Item):
    companyName = scrapy.Field()
    companyRealName = scrapy.Field()
    companyHireNumber = scrapy.Field()
    CVprocessingRate = scrapy.Field()
    CVprocessingDay = scrapy.Field()
    commentNumebr = scrapy.Field()
    lastLoginDate = scrapy.Field()
    companyScale = scrapy.Field()
    companyLocation = scrapy.Field()
    companyIntroduce = scrapy.Field()
    companyDeveloping = scrapy.Field()
