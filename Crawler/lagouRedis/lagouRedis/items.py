# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import re
import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst,Identity,Join
from scrapy.loader import ItemLoader
class LagouredisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class getString(object):
    def __call__(self, values):
        for value in values:
            if value is not None and value != '':
                value = re.sub('\\n|/| |/\|//','',value)
                return value

# def get_string(value):
#     value = re.sub('\\n|/| |/\|//','',value)
#     return value


class JobLagouItemLoader(ItemLoader):
    default_input_processor = getString()
    default_output_processor = TakeFirst()

class jobItem(scrapy.Item):
    jobUrl = scrapy.Field(input_processor = Identity())
    jobName = scrapy.Field()
    jobSalary = scrapy.Field()
    jobLocation = scrapy.Field()
    jobExperience = scrapy.Field()
    jobDegree = scrapy.Field()
    jobType = scrapy.Field()
    jobDetail = scrapy.Field(output_processor = Join())
    jobCompanyName = scrapy.Field()

class companyItem(scrapy.Item):
    companyUrl = scrapy.Field(input_processor = Identity())
    companyName = scrapy.Field()
    companyRealName = scrapy.Field()
    companyHireNumber = scrapy.Field()
    CVprocessingRate = scrapy.Field()
    CVprocessingDay = scrapy.Field()
    commentNumebr = scrapy.Field()
    lastLoginDate = scrapy.Field()
    companyScale = scrapy.Field()
    companyLocation = scrapy.Field()
    companyIntroduce = scrapy.Field(output_processor = Join())
    companyDeveloping = scrapy.Field(output_processor = Join())
