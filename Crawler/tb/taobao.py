from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import re
import csv

#
def get_next_page(browser):
    try:
        browser.find_element_by_xpath('//li[@class="item next"]').click()
        time.sleep(60)
        return True
    except Exception as e:
        print(e)
        return False


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


while True:
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
    
    if not get_next_page(browser):
        break