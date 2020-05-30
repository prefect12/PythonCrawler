# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import urllib
from scrapy import Request
import os,sys
from urllib.request import urlopen,urlretrieve

class MeizituPipeline(object):


    def process_item(self, item, spider):
        header = [
            ('Accept','ttext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'),
            ('Accept-Language','zh-CN,zh;q=0.9,en-AU;q=0.8,en;q=0.7'),
        ('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'),
        ('accept-encoding','gzip, deflate, br'),
        ('cookie','Hm_lvt_cb7f29be3c304cd3bb0c65a4faa96c30=1588322017,1590136600; Hm_lpvt_cb7f29be3c304cd3bb0c65a4faa96c30=1590143315'),
        ('sec-fetch-dest','document'),
        ('sec-fetch-mode','navigate'),
        ('upgrade-insecure-requests','1')
        ]

        url = item['url']
        header.append(('referer',item['refeUrl']))

        opener = urllib.request.build_opener()
        opener.addheaders = header
        data = opener.open(url, timeout=5000)

        project_dir = os.path.dirname(os.path.abspath(__file__))
        path = project_dir + "\\img\\%s"%(item['name'])
        if not os.path.exists(path):
                os.makedirs(path)
        path += '\\' + item['md5'] + '.jpg'

        f = open(path, "wb+")
        f.write(data.read())
        print(url)
        f.close()


# class ArticleImagePipeline(ImagesPipeline):
#     def item_completed(self, results, item, info):
#         if 'front_image_url' in item:
#             image_file_path = ""
#             for ok,value in results:
#                 image_file_path = value["path"]
#             item["front_image_path"] = image_file_path
#         return item