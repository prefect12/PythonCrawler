
# 项目名

##### 项目介绍：
爬取妹子图网站所有图片，第一次整站抓取并保存状态。之后进行增量抓取
使用scrapy异步框架，极大地增加了下载速度。  
直接把图片集当成文件夹名，把图片下载到当前目录下的imgs内

**** 
### 项目逻辑
项目逻辑和淘宝类似。


**** 
### 项目技术栈
`Scrapy`

#### 技术
##### 反爬
该网站反爬有2点
1. 下载延迟最低一秒，否则会被识别为爬虫
2. 发起http请求的时候必须携带当前网页的referer字段，否则会被识别为盗链，无法下载图片。
```python
注意携带 headers={'referer': response.url}
yield Request(url=nextPage, callback=self.parse_detail,priority=20, headers={'referer': response.url})
```

##### 代码
使用以下代码运行爬虫，启停状态会被保存在 job_info/001的文件夹内，关闭爬虫时不要强制退出，使用Ctrl + C停止并等待状态保存完毕。   
使用同样代码启动
```python
scrapy crawl mzt -s JOBDIR=job_info/001
```
**** 



