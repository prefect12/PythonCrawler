# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from items import jobItem,companyItem

class LagouredisPipeline(object):

    def process_item(self, item, spider):
        print('LagouredisPipeline',item)
        return item


class jobPipeline(object):

    def process_item(self,item,spider):
        if isinstance(item,jobItem):
            print(item['jobName'])
        pass

        return item


class companyPipeline(object):

    def process_item(self,item,spider):
        if isinstance(item, companyItem):
            print(item['companyName'])
        pass

        return item