from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import re
import csv
#
#options = Options()
## mobile_emulation = {"deviceName": "iPhone X"}
## options.add_experimental_option("mobileEmulation", mobile_emulation)
#
#
##url = 'https://www.taobao.com/'
##browser.get(url)
##browser.maximize_window()
#
#class taobao:
#    def __init__(self):
#        url = 'https://www.taobao.com/'
#        options.add_experimental_option('excludeSwitches', ['enable-automation'])
#        
#        self.browser = webdriver.Chrome('./chromedriver.exe',options=options)
#        self.browser.get(url)
#        
#        
#    def search_product(self,key_word):
#        # 定位输入框
#        self.key_word = key_word
#        self.browser.find_element_by_id("q").send_keys(key_word)
#        # 定义点击按钮，并点击
#        self.browser.find_element_by_class_name('btn-search').click()
#        # 最大化窗口：为了方便我们扫码
#        self.browser.maximize_window()
#        # 等待15秒，给足时间我们扫码
#        time.sleep(15)
#        page_info = self.browser.find_element_by_xpath('//div[@class="total"]').text
#        # 需要注意的是：findall()返回的是一个列表，虽然此时只有一个元素它也是一个列表。
#        page = re.findall("(\d+)",page_info)[0]
#        print(page)
##        return page
#    
#    def get_item(self):
#            # 通过页面分析发现：所有的信息都在items节点下
#        items = self.browser.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
#        for item in items:
#            # 参数信息
#            pro_desc = item.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text
#            # 价格
#            pro_price = item.find_element_by_xpath('.//strong').text
#            # 付款人数
#            buy_num = item.find_element_by_xpath('.//div[@class="deal-cnt"]').text
#            # 旗舰店
#            shop = item.find_element_by_xpath('.//div[@class="shop"]/a').text
#            # 发货地
#            address = item.find_element_by_xpath('.//div[@class="location"]').text
#            
#            with open('{}.csv'.format(self.key_word), mode='a', newline='', encoding='utf-8-sig') as f:
#                csv_writer = csv.writer(f, delimiter=',')
#                csv_writer.writerow([pro_desc, pro_price, buy_num, shop, address])
#        
#    def main(self):
#        keyword = input("请输入你要搜索的商品：")
#        page = self.search_product(keyword)
#        self.get_item()
#
def get_next_page(browser):
    try:
        browser.find_element_by_xpath('//li[@class="item next"]').click()
        time.sleep(10)
        return True
    except Exception as e:
        print(e)
        return False

#if __name__ == "__main__":
#    tb = taobao()
#    tb.main()

options = Options()
url = 'https://www.taobao.com/'
options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome('./chromedriver.exe',options=options)
browser.get(url)
items = browser.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')



key_word = input("请输入你要搜索的商品：")

browser.find_element_by_id("q").send_keys(key_word)
browser.find_element_by_class_name('btn-search').click()
browser.maximize_window()

time.sleep(15)
page_info = browser.find_element_by_xpath('//div[@class="total"]').text
page = re.findall("(\d+)",page_info)[0]
numOfItem = 0


while get_next_page(browser):
    items = browser.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    current_page = browser.find_element_by_xpath('//li[@class="item active"]/span').text
    print('page:',current_page)
    for item in items:

        pro_desc = item.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text
        item_url = item.find_element_by_xpath('.//div[@class="row row-2 title"]/a').get_attribute('href')
        pro_price = item.find_element_by_xpath('.//strong').text
        buy_num = item.find_element_by_xpath('.//div[@class="deal-cnt"]').text
        shop_url = item.find_element_by_xpath('.//div[@class="shop"]/a').get_attribute('href')
        shop = item.find_element_by_xpath('.//div[@class="shop"]/a').text
        address = item.find_element_by_xpath('.//div[@class="location"]').text
        
        with open('{}.csv'.format(key_word), mode='a', newline='', encoding='utf-8-sig') as f:
            csv_writer = csv.writer(f, delimiter=',')
            csv_writer.writerow([pro_desc,item_url,pro_price, buy_num, shop,shop_url, address])
            numOfItem += 1
    print('已经抓取了%s条数据'%(numOfItem))