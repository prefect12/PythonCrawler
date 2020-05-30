# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:52:47 2020

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:23:10 2020

@author: Administrator
"""
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://store.steampowered.com/search/?filter=globaltopsellers&os=win'
url2 = 'https://store.steampowered.com/app/578080/PLAYERUNKNOWNS_BATTLEGROUNDS/'
url3 = 'https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/'
url4 = 'https://store.steampowered.com/app/774861/Project_Winter/'
browser = webdriver.Chrome('./chromedriver.exe')

browser.get (url2)
browser.maximize_window()

jsCode = "var q=document.documentElement.scrollTop=20000"
browser.execute_script(jsCode)

time.sleep(3)
#element2 = browser.find_element_by_id('reviews_date_range_menu')

canves = browser.find_element_by_xpath('*//div[@id = "review_histogram_recent"]/canvas')
zeroElement = browser.find_element_by_xpath('*//div[@id="review_histogram_recent"]/div/div[@class="flot-y-axis flot-y1-axis yAxis y1Axis"]/div')
zeroPosition = [ i for i in re.split(';| |:|px',zeroElement.get_attribute('style')) if len(i) != 0]
top = int(zeroPosition[3])
left = int(zeroPosition[5])
#ActionChains(browser).move_to_element(element2).perform()
#for x in range(20,width,1):
#    for y in range(100,height,2):
#        print(x,y)
Xstart = 13
good = []
bad = []

for i in range(31):
    ActionChains(browser).move_to_element_with_offset(zeroElement,xoffset=Xstart+9*i,yoffset=6).perform()
    n = browser.find_element_by_id('review_histogram_tooltip').text
    print(n)
    good.append(n)

for i in range(31):
    ActionChains(browser).move_to_element_with_offset(zeroElement,xoffset=Xstart+9*i,yoffset=8).perform()
    n = browser.find_element_by_id('review_histogram_tooltip').text
    print(n)
    bad.append(n)

print(good,bad)

#title = browser.find_element_by_class_name('new_job_name').text
#time = browser.find_element_by_class_name("job_date").find_element_by_tag_name('span')
#salary = browser.find_element_by_class_name('job_msg').find_element_by_tag_name('span')
#time.screenshot('./image/'+title +'_Time.png')
#salary.screenshot('./image/'+title+'_Salary.png')


#def getSoup(baseUrl):
#    headers = {
#            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#            'accept-encoding': 'gzip, deflate, br',
#            'accept-language': 'zh-CN,zh;q=0.9,en-AU;q=0.8,en;q=0.7',
#            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
#            }
#    
#    r = requests.get(baseUrl,headers=headers)
#    r.encoding = 'utf-8'
#    content = BeautifulSoup(r.text,"html.parser")
#    return r,content
#
#url = 'https://www.shixiseng.com/intern/inn_u4n8q0v6zsrf?pcm=pc_SearchList'
#
#r,soup = getSoup(url)