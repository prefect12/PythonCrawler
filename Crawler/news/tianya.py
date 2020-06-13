# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:57:54 2020

@author: Administrator
"""
########################################
#                                      #
#           抓取天涯论坛                #
#                                      #
########################################

import requests
import pandas as pd
from pprint import pprint
from lxml import etree
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv

#文字预处理
def replaceStr(str):
    return re.sub('\\t|\\n|\u3000|','',str)

num = 0
#抓取前25页
for i in range(1,25):

    tianya = 'https://search.tianya.cn/bbs?q=%E7%BE%8E%E5%9B%BD+%E6%9A%B4%E4%B9%B1&pn=' + str(i)
    
    #发送请求
    respons = requests.get(tianya)
    dom = etree.HTML(respons.text)
    
    #找到所有url
    urlList = dom.xpath('//li//h3/a/@href')
    
    #遍历url
    for url in urlList:    
        
        #发送请求
        subPage = requests.get(url)
        dom = etree.HTML(subPage.text)
        
        #抓取主题和内容
        theme = dom.xpath(".//div[@class='bbs-content clearfix']//text()")
        content = dom.xpath(".//div[@class='bbs-content']//text()")
        
        #转化为字符串
        theme = replaceStr(' '.join(theme))
        content = replaceStr(' '.join(content))
        
        #保存
        with open('tianya.csv', mode='a', newline='', encoding='utf-8-sig') as f:
                csv_writer = csv.writer(f, delimiter=',')
                csv_writer.writerow([theme,content])
        num+=1
        print(num)
