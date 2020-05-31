import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import hashlib
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

def zheye():
    pass

def numEnglish():
    pass


class zhihu:
    def __init__(self):
        option = ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.browser = webdriver.Chrome('./chromedriver.exe',options=option)

        url = 'https://www.zhihu.com/signin?next=%2F'
        self.browser.get(url)

        self.userName = '13429829919'
        self.passWord = 'wwt19960731'

    def zheye(self,path):
        pass

    def charNum(self,path):
        pass

    def downloadImage(self):
        img = self.browser.find_element_by_xpath('//img[@data-tooltip="看不清楚？换一张"]')
        size = img.size
        name = hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()
        if size['width'] > 100:
            type = 1
            path = './/倒立文字//'+ name + '.png'
        else:
            type = 2
            path = './/英文数字//'+ name + '.png'
        img.screenshot(path)
        return type,path

    def login(self):
        password_button = self.browser.find_element_by_xpath('//div[@class="SignFlow-tab"]')
        password_button.click()

        user_name = self.browser.find_element_by_xpath('//input[@name="username"]')
        pass_word = self.browser.find_element_by_xpath('//input[@name="password"]')
        login_btn = self.browser.find_element_by_xpath('//button[@class="Button SignFlow-submitButton Button--primary Button--blue"]')


        user_name.send_keys(self.userName)
        pass_word.send_keys(self.passWord)
        login_btn.click()
        time.sleep(1)
        # while 1:
        type,path = self.downloadImage()
            # svg = self.browser.find_element_by_xpath('//svg[@class="Zi Zi--Refresh"]')
            # svg.click()
            # time.sleep(1)

        if type == 1:
            clickLocation = self.zheye(path)
            pass
        if type == 2:
            chars = self.charNum(path)
            pass


        login_btn.click()

if __name__ == '__main__':
    s = zhihu()
    s.login()