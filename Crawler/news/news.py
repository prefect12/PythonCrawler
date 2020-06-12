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


xinlang = 'http://www.sina.com.cn/mid/search.shtml?range=all&c=news&q=%E7%BE%8E%E5%9B%BD+%E6%9A%B4%E4%B9%B1&from=home&ie=utf-8'

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome('./chromedriver.exe',options=options)
browser.get(xinlang)
search = browser.find_element_by_xpath('.//div[@class="search_type clearfix"]')
first = search.find_elements_by_xpath("./a")[1]
second = search.find_elements_by_xpath("./a")[0]
first.click()
second.click()
downLoadLinks = []

for i in range(20):
    time.sleep(2)
    news = browser.find_elements_by_xpath('.//div[@class="result"]//a')[1:]
    links = list(set([i.get_attribute("href") for i in news if i.get_attribute("href") != 'javascript:;']))
    downLoadLinks.extend(links)

    browser.find_elements_by_xpath('//div[@class="pagebox"]/a')[-1].click()
    time.sleep(3)

    
downLoadLinks = list(set(downLoadLinks))
print(downLoadLinks)