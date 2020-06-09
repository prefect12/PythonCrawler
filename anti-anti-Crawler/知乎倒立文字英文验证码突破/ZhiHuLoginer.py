import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import hashlib
from selenium.webdriver import ChromeOptions
from zheye1 import zheye
import base64
import requests
from hashlib import md5
from chaojiying import Chaojiying_Client

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])



class zhihu:
    def __init__(self):
        '''
        方法一
        因为知乎反扒，selenium的webdriver必须用60版本
        或手动启动chrome监听模式

        方法二
        手动启动chrome并使用debugger模式监听
        chrome.exe --remote-debugging-port=9222
        启动后如果能成功访问
        127.0.0.1:9222/json说明启动成功

        '''

        #
        option = ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_argument('--disable-extensions')

        #若选择方法二打开注释
        # option.add_experimental_option('debuggerAddress','127.0.0.1:9222')

        self.browser = webdriver.Chrome('./chromedriver.exe',options=option)

        url = 'https://www.zhihu.com/signin?next=%2F'
        self.browser.get(url)

        try:
            self.browser.maximize_window()
        except:
            pass

        self.userName = 'zhihuUsername'
        self.passWord = 'zhihuPassword'

    def zheye(self,path):
        z = zheye()
        position = z.Recognize(path)
        return position

    def charNum(self,path):
        chaojiying = Chaojiying_Client('username', 'password', '1902')  # 用户中心>>软件ID 生成一个替换 96001
        im = open(path, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        mystr = chaojiying.PostPic(im, 1902)['pic_str']
#        return mystr
        return 'word'
        
    #下载图片
    def downloadImage(self):
        img = self.browser.find_element_by_xpath('//img[@data-tooltip="看不清楚？换一张"]')
        self.img_ele = img

        size = img.size
        name = hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()
        if size['width'] > 100:
            type = 1
            path = './/倒立文字//'+ name + '.jpeg'
            base64_text = img.get_attribute('src')
            code = base64_text.replace('data:image/jpg;base64,','').replace('%0A',"")
            fh = open(path,'wb')
            fh.write(base64.b64decode(code))
            fh.close()
        else:
            type = 2
            path = './/英文数字//'+ name + '.jpeg'
            base64_text = img.get_attribute('src')
            code = base64_text.replace('data:image/jpg;base64,','').replace('%0A',"")
            fh = open(path,'wb')
            fh.write(base64.b64decode(code))
            fh.close()

        return type,path

    #点击文字
    def clickWords(self,clickLocation):
        ele = self.img_ele
        for word in clickLocation:
            x = word[1]//2
            y = word[0]//2
            ActionChains(self.browser).move_to_element_with_offset(ele, xoffset=x,yoffset=y).click().perform()
            time.sleep(0.5)

    #输入字符串
    def inputChar(self,char):
        input_box = self.browser.find_element_by_xpath('//input[@name="captcha"]')
        input_box.send_keys(char)

    # 登陆主程序
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
        type,path = self.downloadImage()


        if type == 1:
            clickLocation = self.zheye(path)
            self.clickWords(clickLocation)
        if type == 2:
            chars = self.charNum(path)
            self.inputChar(chars)

        login_btn.click()
        time.sleep(3)


    def check(self):
        try:
            notify = self.browser.find_element_by_xpath('lable[@class="SearchBar-input Input-wrapper Input-wrapper--grey"]')
            return True
        except:
            self.browser.refresh()
            return False

    def run(self):
        Coocik =  None
        while not self.check():
            Coocik = self.login()
        return Coocik




if __name__ == '__main__':
    a = zhihu()
    Cookie = a.run()
