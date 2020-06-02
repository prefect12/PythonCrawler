# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter
import MySQLdb

class JobsPipeline(object):
    def process_item(self, item, spider):

        return item


class JobItemMySQLPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1','root','',"job",charset="utf8",use_unicode=True)
        self.cursor = self.conn.cursor()


    def process_item(self,item,spider):
        jobItem = item['jobItem']
        insert_sql = '''insert into job51jobs (jobName,jobUrl,jobLocation,salary,postDate,experience,degree,welfare,jobDesc,companyName) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE jobDesc = values(jobDesc)'''
        jobName = jobItem.get('jobName')

        jobName = jobItem.get('jobName','Not Valid')
        jobUrl = jobItem.get('jobUrl','Not Valid')
        jobLocation = jobItem.get('jobLocation','Not Valid')
        salary = jobItem.get('salary','Not Valid')
        postDate = jobItem.get('postDate','Not Valid')
        experience = jobItem.get('experience','Not Valid')
        degree = jobItem.get('degree','Not Valid')
        welfare = jobItem.get('welfare','Not Valid')
        jobDesc = jobItem.get('jobDesc','Not Valid')
        companyName = jobItem.get('companyName','Not Valid')


        self.cursor.execute(insert_sql,tuple([jobName,jobUrl,jobLocation,salary,postDate,experience,degree,welfare,jobDesc,companyName]))
        self.conn.commit()

        return item


class CompanyItemMySQLPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1','root','',"job",charset="utf8",use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        companyItem = item['companyItem']
        insert_sql = '''insert into job51companies (companyName,companyType,companyScale,companyField,companyLocation,companyInfo,companyUrl) values (%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE companyInfo = values(companyInfo)'''

        companyName = companyItem.get('companyName')
        companyType = companyItem.get('companyType')
        companyScale = companyItem.get('companyScale')
        companyField = companyItem.get('companyField')
        companyLocation = companyItem.get('companyLocation')
        companyInfo = companyItem.get('companyInfo')
        companyUrl = companyItem.get('companyUrl')
        companyHash = companyItem.get('companyHash')

        self.cursor.execute(insert_sql,tuple([companyName,companyType,companyScale,companyField,companyLocation,companyInfo,companyUrl]))
        self.conn.commit()
        return item




class JobItemCsvPipeline(object):
    def __init__(self):
        pass

    def process_item(self,item,spider):
        return item


class CompanyItemCsvPipeline(object):
    def __init__(self):
        pass

    def process_item(self,item,spider):
        return item

