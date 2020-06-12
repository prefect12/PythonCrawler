# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:57:54 2020

@author: Administrator
"""
import requests
import pandas as pd
from pprint import pprint
from lxml import etree
import time
import warnings
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv

def replaceStr(str):
    return re.sub('\\t|\\n|\u3000','',str)

num = 0
for i in range(1,25):

    tianya = 'https://search.tianya.cn/bbs?q=%E7%BE%8E%E5%9B%BD+%E6%9A%B4%E4%B9%B1&pn=' + str(i)
    respons = requests.get(tianya)
    dom = etree.HTML(respons.text)
    urlList = dom.xpath('//li//h3/a/@href')
    
    for url in urlList:    
        subPage = requests.get(url)
        dom = etree.HTML(subPage.text)
        theme = dom.xpath(".//div[@class='bbs-content clearfix']//text()")
        content = dom.xpath(".//div[@class='bbs-content']//text()")
        theme = replaceStr(' '.join(theme))
        content = replaceStr(' '.join(content))
        with open('tianya.csv', mode='a', newline='', encoding='utf-8-sig') as f:
                csv_writer = csv.writer(f, delimiter=',')
                csv_writer.writerow([theme,content])
        num+=1
        print(num,':',theme)
