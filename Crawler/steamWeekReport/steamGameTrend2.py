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
import time,datetime
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait

#desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
#desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出


class getSteamTrend:
    
    def __init__(self):
        self.hotPage = 'https://store.steampowered.com/search/?filter=globaltopsellers&os=win'
        self.goodPath,self.badPath = self.createCsv()
    
    def createCsv(self):

        dateList = []
        now = datetime.datetime.now()
        dateList.append('gameName')
        dateList.append('url')
        for i in range(0,30):
            DayAgo = (now - datetime.timedelta(days = 30-i))
            oneDay = str(DayAgo.year) + '-' + str(DayAgo.month) + '-' + str(DayAgo.day)
            dateList.append(oneDay)
  
        path = './' + 'data/' + dateList[2] + '-TO-' + dateList[-1] 
        
        df = pd.DataFrame(columns = dateList)
        goodPath = path + 'good.csv'
        badPath = path + 'bad.csv'
        self.timeRange = dateList[2:]
        
        df.to_csv(goodPath,index=False,encoding="UTF-8")
        df.to_csv(badPath,index=False,encoding="UTF-8")
        
        return (goodPath,badPath)
        
    def saveDataToCsv(self,path,url,name,data):
        
        dic = {}
        dic['gameName'] = name
        dic['url'] = url
        data = [[j for j in re.split(' |年|月|日|\(|\)|',i) if len(j) != 0] for i in data]

        dateDic = {}
        for i in data:
            key = i[2] + '-' + i[3] + '-' + i[4]
            dateDic[key] = int(i[0].replace(',',''))
            
        for i in self.timeRange[::-1]:
            if i in dateDic:
                dic[i] = dateDic[i]
            else:
                dic[i] = 0
        print(df)
        df = pd.DataFrame(dic,index=[0])   
        
        try:
            df.to_csv(path, mode="a+", header=None,index=False,encoding="UTF-8")
        except Exception as e:
            print(e)


    def getBrowser(self,url):
        print('='*50)
        print(url)
        
        browser = webdriver.Chrome('./chromedriver.exe')
        browser.get (url)
        browser.maximize_window()


        time.sleep(5)
        return browser
    
    def getSoup(self,url):

        headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en-AU;q=0.8,en;q=0.7',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        }
        
        try:
           r = requests.get(url,headers=headers)
           r.encoding = 'utf-8'
           content = BeautifulSoup(r.text,"html.parser")
           return content
        except Exception as e:
            print(e)
            return None
        
    
    def getTop30GameUrl(self):
        
        soup = self.getSoup(self.hotPage)
        searchResult = soup.find(id='search_resultsRows').find_all('a')[:35]
        
        urlList = []
        for i in searchResult:
            urlList.append((i.find(class_='title').text,i.get('href')))
        return urlList
    
    
    def prapaerPage(self,browser):
        try:
            selector = Select(browser.find_element_by_id('ageYear'))
            selector.select_by_value('1990')
            button = browser.find_element_by_xpath('*//div[@class="main_content_ctn"]/div[@class="agegate_text_container btns"]').find_element_by_tag_name('a')
            ActionChains(browser).click(button).perform()
            time.sleep(5)
        except:
            pass
        
        jsCode = "var q=document.documentElement.scrollTop=5000"
        browser.execute_script(jsCode)
        time.sleep(3)
        
        try:
            button = browser.find_element_by_xpath('*//span[@id="review_show_graph_button"]')
            ActionChains(browser).click(button).perform()
            time.sleep(3)
        except Exception as e:
            print(e)
            pass
        
    
    def getDateFromPage(self,url):
        name = url[0]
        url = url[1]
        browser = self.getBrowser(url)
        
        self.prapaerPage(browser)
        try:
            zeroElement = browser.find_element_by_xpath('*//div[@id="review_histogram_recent"]/div/div[@class="flot-y-axis flot-y1-axis yAxis y1Axis"]/div')
            path = browser.find_element_by_xpath('*//img[@class="game_header_image_full"]').get_attribute('src')

        except Exception as e:
            print(e)
            browser.close()
            return

        Xstart = 15
        Ystart = 6
    
        goodReview,badReview = [],[]
        move = 0
        
        while len(goodReview) != 30 and move < 200: 
            try:
                ActionChains(browser).move_to_element_with_offset(zeroElement,xoffset=Xstart+2*move,yoffset=Ystart).perform()
            except:
                break
            
            move+=1
            review = browser.find_element_by_id('review_histogram_tooltip').text
            if review and review not in goodReview:
                print(review)
                goodReview.append(review)      
        
        move = 0
        while len(badReview) != 30 and move < 200:
            try:
                ActionChains(browser).move_to_element_with_offset(zeroElement,xoffset=Xstart+2*move,yoffset=Ystart+2).perform()
            except:
                break
            move+=1
            review = browser.find_element_by_id('review_histogram_tooltip').text
            if review and review not in badReview:
                print(review)
                badReview.append(review)
        
        self.saveDataToCsv(self.goodPath,path,name,goodReview)
        self.saveDataToCsv(self.badPath,path,name,badReview)
        
        browser.close()
        print('='*50)
        
    def run(self):
        urlList = self.getTop30GameUrl()
        for url in urlList:
            print(url[0])
            self.getDateFromPage(url)

class processor:
    def __init__(self,path):
        try:
            self.df = pd.read_csv(path,encoding = 'UTF-8')
        except Exception as e:
            self.df = pd.read_csv(path,encoding = 'GBK')
    def proces(self):
        df = self.df
        df.drop_duplicates(['gameName'],inplace = True)
        col = np.array(df.columns)[2:]
        for i in range(len(col[1:])):
           df[col[i]] = df[col[i-1]] + df[col[i]]
        
if __name__ == "__main__":
    steam = getSteamTrend()
    steam.run()
#    url = 'https://store.steampowered.com/app/397540/3/'
#    a = getSteamTrend()
#    a.run()

    df = pd.read_csv('./data/2020-4-29-TO-2020-3-31good.csv',encoding = "UTF-8")
    z = df
    df.drop_duplicates(['gameName'],inplace = True)
    col = np.array(df.columns)[2:]
    for i in range(len(col[1:])):
       df[col[i]] = df[col[i-1]] + df[col[i]]
    k.to_csv('./data/test.csv',encoding='utf-8')


