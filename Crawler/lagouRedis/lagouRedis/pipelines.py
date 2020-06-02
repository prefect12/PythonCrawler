# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from items import jobItem,companyItem
import pandas as pd
import time
import os



class jobPipeline(object):
    path = './lagouJobs.csv'

    def __init__(self):
        if not os.path.exists('./lagouJobs.csv'):
            col_names =    ['jobUrl','jobName','jobSalary','jobLocation','jobExperience','jobDegree' ,'jobType' ,'jobDetail' ,'jobCompanyName']
            df = pd.DataFrame(columns = col_names)
            df.to_csv(path_or_buf = self.path ,encoding='GB18030',index=False)


    def process_item(self,item,spider):
        if isinstance(item,jobItem):

            col_names = ['jobUrl', 'jobName', 'jobSalary', 'jobLocation', 'jobExperience', 'jobDegree', 'jobType','jobDetail', 'jobCompanyName']
            df = pd.DataFrame(columns=col_names)
            dic = dict()

            dic['jobUrl'] = item.get('jobUrl','')
            dic['jobName'] = item.get('jobName','')
            dic['jobSalary'] = item.get('jobSalary','')
            dic['jobLocation'] = item.get('jobLocation','')
            dic['jobExperience'] = item.get('jobExperience','')
            dic['jobDegree'] = item.get('jobDegree','')
            dic['jobType'] = item.get('jobType','')
            dic['jobDetail'] = item.get('jobDetail','')
            dic['jobCompanyName'] = item.get('jobCompanyName','')

            df = df.append(dic,ignore_index=True)
            try:
                if 'jobName' in item:
                    df.to_csv(self.path, mode="a+", header=False, index=False, encoding="GB18030")
                    print(item['jobName'],'写入成功')
            except Exception as e:
                print(e)
                print(item['jobUrl'],"当页数据写入失败")

        return item


class companyPipeline(object):
    path = './lagouCompany.csv'

    def __init__(self):
        if not os.path.exists('./lagouJobs.csv'):
            col_names = ['companyUrl','companyName','companyRealName','companyHireNumber','CVprocessingRate','CVprocessingDay','commentNumebr','lastLoginDate','companyScale','companyLocation','companyIntroduce','companyDeveloping']
            df = pd.DataFrame(columns = col_names)
            df.to_csv(path_or_buf = self.path,encoding='GB18030',index=False)


    def process_item(self,item,spider):

        if isinstance(item, companyItem):
            col_names = ['companyUrl','companyName','companyRealName','companyHireNumber','CVprocessingRate','CVprocessingDay','commentNumebr','lastLoginDate','companyScale','companyLocation','companyIntroduce','companyDeveloping']
            df = pd.DataFrame(columns=col_names)
            dic = dict()

            dic['companyUrl'] = item.get('companyUrl','')
            dic['companyName'] = item.get('companyName','')
            dic['companyRealName'] = item.get('companyRealName','')
            dic['companyHireNumber'] = item.get('companyHireNumber','')
            dic['CVprocessingRate'] = item.get('CVprocessingRate','')
            dic['CVprocessingDay'] = item.get('CVprocessingDay','')
            dic['commentNumebr'] = item.get('commentNumebr','')
            dic['lastLoginDate'] = item.get('lastLoginDate','')
            dic['companyScale'] = item.get('companyScale','')
            dic['companyLocation'] = item.get('companyLocation','')
            dic['companyIntroduce'] = item.get('companyIntroduce','')
            dic['companyDeveloping'] = item.get('companyDeveloping', '')

            df = df.append(df,ignore_index=True)
            try:
                if 'companyName' in item:
                    df.to_csv(self.path, mode="a+", header=False, index=False, encoding="GB18030")
                    print(item['companyName'],'写入成功')
            except Exception as e:
                print(e)
                print(item['companyName'],"当页数据写入失败")


        pass

        return item