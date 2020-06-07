# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 14:09:38 2020

@author: Administrator
"""

import time
import requests
from lxml import etree
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

url = 'https://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=武汉&searchArrivalAirport=北京&searchDepartureTime=2020-06-08&searchArrivalTime=2020-06-10&nextNDays=0&startSearch=true&fromCode=BJS&toCode=SHA&from=flight_dom_search&lowestPrice=null'

options = Options()
mobile_emulation = {"deviceName": "iPhone X"}
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option("mobileEmulation", mobile_emulation)
browser = webdriver.Chrome('./chromedriver.exe',options=options)

#browser = webdriver.Chrome('./chromedriver.exe')
browser.get(url)
browser.maximize_window()
time.sleep(10)

content = browser.page_source

fly = content.xpath('//div[@class="b-airfly"]')