import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random
from PIL import Image

class biliLogin():
    name = 'bili'
    login_url = 'https://passport.bilibili.com/login'
    def __init__(self):
        self.browser = webdriver.Chrome('./chromedriver.exe')
        self.user_name = 'userName'
        self.pass_word = 'password'

    def crop_image(self,image_file_name = '1'):
        #截取验证码图片
        time.sleep(2)
        img = self.browser.find_element_by_xpath('//div[@class="geetest_slicebg geetest_absolute"]')
        location = img.location
        print('图片位置: ',location)
        path = './' + image_file_name + '.png'
        img.screenshot(path)
        size = img.size


        # img.get_screenshot_as_file('./test.png')
        # path = './' + image_file_name + '/img.png'

    def get_track(self,left):

        # 拖动图片
        # 根据偏移量获取移动轨迹
        # 一开始加速，然后减速，生长曲线，且加入点随机变动
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = left * 3 / 4
        # 间隔时间
        t = 0.1
        v = 0
        while current < left:
            if current < mid:
                a = random.randint(2, 3)
            else:
                a = - random.randint(6, 7)
            v0 = v
            # 当前速度
            v = v0 + a * t
            # 移动距离
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            track.append(round(move))
        return track

    def check_login(self):
        try:
            self.browser.find_element_by_xpath("//span[contains(text(),'创作中心')]")
            return True
        except Exception as e:
            return False

    def login(self):
        try:
            self.browser.maximize_window()
        except Exception:
            pass

        while not self.check_login():
            self.browser.get(self.login_url)
            username_ele = self.browser.find_element_by_xpath('//input[@id="login-username"]')
            password_ele = self.browser.find_element_by_xpath('//input[@id="login-passwd"]')
            username_ele.send_keys(self.user_name)
            password_ele.send_keys(self.pass_word)

            #1.点击登陆调出滑动验证码
            login_btn = self.browser.find_element_by_xpath('//a[@class="btn btn-login"]')
            login_btn.click()

            #等待滑动验证码
            time.sleep(2)

            #执行js，改变css样式，显示没有缺口的图
            self.crop_image('before')

            self.browser.execute_script('document.querySelectorAll("canvas")[3].style=""')

            self.crop_image('after')

            left = self.compare()
            track = self.get_track(left)


            slider = self.browser.find_element_by_css_selector(".geetest_slider_button")
            ActionChains(self.browser).click_and_hold(slider).perform()
            for x in track:
                ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
            time.sleep(0.5)
            ActionChains(self.browser).release().perform()
            time.sleep(5)

            Cookies = self.browser.get_cookies()
            print(Cookies)



    def compare(self):

        capture1 = Image.open('./before.png')
        capture2 = Image.open('./after.png')

        #获取缺口位置
        left = 60
        has_find = False
        for i in range(60,capture1.size[0]):
            if has_find:
                break
            for j in range(capture1.size[1]):
                if not self.compare_pixel(capture1,capture2,i,j):
                    left = i
                    has_find = True
                    break
        left -= 6
        return left

    def compare_pixel(self,image1,image2,x,y):
        #判断两个像素是否相同
        pixel1 = image1.load()[x,y]
        pixel2 = image2.load()[x,y]

        threshold = 60
        if abs(pixel1[0]-pixel2[0]) < threshold and abs(pixel1[1]-pixel2[1]) < threshold and abs(pixel1[2]-pixel2[2]) < threshold:
            return True
        else:
            return False


if __name__ =="__main__":
    b = biliLogin()
    b.login()

