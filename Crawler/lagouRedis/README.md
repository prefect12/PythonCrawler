# 拉勾网职位/公司抓取

##### 项目介绍：
通过Scrapy抓取拉勾网的职位和公司，Scrapy是一个基于协程的异步框架，所以效率非常的高。同时必须要限速，否则IP极易被封。
同时把scrapy框架的schedule核心改为为scrapy-redis，scrapy就会从redis中获取requests，返回item或者response重新进入redis。当多个爬虫共享一个redis数据库并往里面存取的时候就实现了分布式爬虫。

**** 
### 项目逻辑
![淘宝抓取逻辑](./imgs/流程图.png)
(点击查看大图)

注意：
1. 函数中所有的函数调用都是使用回调函数的方式，并且使用yield关键词返回item，防止线程阻塞
2. 实际上所有的item和requests都会被保存在Redis中由Schedule负责调用，并不会像普通的scrapy一样直接返回到下一个函数中

**** 
### 项目技术栈
`Scrapy-Reids`,`Redis`,`Requests`



#### 使用 setting内参数进行反爬

`AUTOTHROTTLE_ENABLED` ：一个根据算法自动限速的框架，对网页更加友好，防止在短时间内发起大量http请求导致服务器压力增大或者ip地址被封。  
来源：https://docs.scrapy.org/en/0.24/topics/autothrottle.html
  
`COOKIES_ENABLED`：是否携带 setting内的的cookies，如果打开每次就会带上相同的cookies，因为拉勾网不需要登陆所以每次请求应该携带上次response的cookies。每次携带相同的cookies极易被识别为爬虫，选择False。  
来源：https://docs.scrapy.org/en/0.24/topics/downloader-middleware.html?highlight=cookies_enable#std:setting-COOKIES_ENABLED

`DOWNLOAD_DELAY`:下载延迟，不设置IP极易被封  
  
`RANDOMIZE_DOWNLOAD_DELAY`:  随机延迟，设定后延迟会取 0.5*DOWNLOAD_DELAY 到 1.5*DOWNLOAD_DELAY中的一个随机值，防止网站通过请求特征反爬（例：恰好每30秒访问一次极易被识别为爬虫特征）

##### 代码
```python
 custom_settings = {
        "COOKIES_ENABLED": False,
        "AUTOTHROTTLE_ENABLED": True,
        "DOWNLOAD_DELAY": 15,
        "RANDOMIZE_DOWNLOAD_DELAY":True,
        }
```
**** 
#### 定制化ItemLoader
通过ItemLoad实现获取数据和预处理数据代码分离，提高代码分离度，更容易维护和更新。
同时可以继承Scrapy自带的ItemLoader并改写其中的方法，使得ItemLoader更易于使用。

##### 代码
```python
#导入所需要的类
from scrapy.loader.processors import MapCompose,TakeFirst,Identity,Join
from scrapy.loader import ItemLoader

#创建预处理类
class getString(object):
    def __call__(self, values):
        temp = ''
        for value in values:
            if value is not None and value != '':
                value = re.sub('| |\n|//|\\xa0|','',value)
                temp += value
        return temp


#通过继承并修改函数实现定制化 ItemLoader，避免item各个字段重复调用函数
class JobLagouItemLoader(ItemLoader):
    default_input_processor = getString()
    default_output_processor = TakeFirst()
    
```

****  
### 抓取内容
#### 职位
|字段|
|---|
|网页URL|
|岗位名|
|薪资|
|工作地址|
|需要经验|
|学历要求|
|岗位类型|
|岗位详细信息|
|公司名|

#### 公司
|字段|
|---|
|公司URL|
|公司名(显示)|
|公司名(实际)|
|简历回复率|
|简历回复平均时间|
|面试评价个数|
|最后的登录时间|
|公司规模|
|公司地址|
|公司简介|

****  
### 运行截图
#### 当redis内没有任何URL时必须使用下面命令添加 start_urls
```
lpush lagou:start_urls https://www.lagou.com/
```
![运行截图](./imgs/等待中.png)

#### 运行截图
#### scrapy会把获取的数据用log的形式打印出来
![运行截图](./imgs/抓取界面.png)

#### 抓取结果（csv文件会保存在当前文件夹下）
![运行截图](./imgs/抓取结果.png)


