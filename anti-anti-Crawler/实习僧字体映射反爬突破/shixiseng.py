import requests
from lxml import etree
from items import wordDict


url = 'https://www.shixiseng.com/interns?keyword=%E7%88%AC%E8%99%AB&page=1&city=%E5%85%A8%E5%9B%BD'
response = requests.get(url)
content = etree.HTML(response.text)

salary = content.xpath('//span[@class="day font"]/text()')
for job in salary:
    for key,val in wordDict.items():
        job = job.replace(key,val)
    print(job)
    
    
