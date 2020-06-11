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

url = 'http://www.sina.com.cn/mid/search.shtml?range=all&c=news&q=%E7%BE%8E%E5%9B%BD+%E6%9A%B4%E4%B9%B1&from=home&ie=utf-8'
options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome('./chromedriver.exe',options=options)
browser.get(url)