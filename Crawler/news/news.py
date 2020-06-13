# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:29:34 2020

@author: Administrator
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import re
import csv

import requests
from lxml import etree
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import pandas as pd
import csv

########################################
#                                      #
#           抓取中国新闻网              #
#                                      #
########################################

#预处理，替换字符串
def replaceStr(str):
    return re.sub('\n|。|[|？| |*-|\r|\|\'|-|“|"|-|【|】|]|！|!\\t|\\n|\u3000|[a-z]*','',str)


#调用selenium抓取数据
xinlang = 'http://sou.chinanews.com/search.do?q=%E7%BE%8E%E5%9B%BD%20%E6%9A%B4%E4%B9%B1'
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome('./chromedriver.exe',options=options)
browser.get(xinlang)
time.sleep(2)


num = 0
#抓取前10页新闻
for i in range(10):
    
    #找到新闻的url
    news = browser.find_elements_by_xpath('//li[@class="news_title"]/a')
    news = [i.get_attribute('href') for i in news]
    
    #遍历新闻
    for url in news:
        #发起请求
        r = requests.get(url)
        r.encoding='utf-8'
        
        #使用dom处理
        dom = etree.HTML(r.text)
        
        #预处理标题和正文
        title = replaceStr(''.join(dom.xpath('//div[@class="content"]/h1/text()')))
        content = replaceStr(''.join(dom.xpath('//div[@class="left_zw"]//text()')))
        
        #设置编码
        content.encode('GB18030')
        
        #保存进csv
        with open('xinlang.csv', mode='a', newline='', encoding='utf-8-sig') as f:
            csv_writer = csv.writer(f, delimiter=',')
            csv_writer.writerow([title,content])
        num+=1
        print(num)

    #点击下一页
    browser.find_element_by_xpath('//div[@id="pagediv"]/a[contains(text(),"下一页")]').click()

    time.sleep(3)
