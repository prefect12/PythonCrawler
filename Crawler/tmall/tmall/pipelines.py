# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import pandas as pd
import re
class TmallPipeline(object):

    def process_item(self, item, spider):
        path = item['path']
        item = item['item']
        headUrl = "https:"

        col_names = ['itemTitle','itemPrice','itemShop','itemUrl','itemSale','itemComment','shopUrl','itemHash']
        df = pd.DataFrame(columns=col_names)
        dic = dict()

        dic['itemTitle'] = item.get('itemTitle','')
        dic['itemPrice'] = item.get('itemPrice','')
        dic['itemShop'] = re.sub(r'|\n| ','',item.get('itemShop',''))
        dic['itemUrl'] = headUrl + item.get('itemUrl','')
        dic['itemSale'] = item.get('itemSale','')
        dic['itemComment'] = item.get('itemComment','')
        dic['shopUrl'] = item.get('shopUrl','')
        dic['itemHash'] = item.get('itemHash','')


        df = df.append(dic,ignore_index=True)
        try:
            if 'itemTitle' in item:
                df.to_csv(path, mode="a+", header=False, index=False, encoding="GB18030")
                print(item['itemTitle'],'写入成功')
        except Exception as e:
            print(e)
            print(item['itemUrl'],"当页数据写入失败")

        return item
