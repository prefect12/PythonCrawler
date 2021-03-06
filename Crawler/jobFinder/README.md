# 数据爬取/岗位分析
* 根据关键字抓取对应岗位信息  
* 根据岗位描述找到某岗位所需的条件  
* 进行数据清洗，过滤，降维，可视化  
* 分析技术栈之间的关联  
**** 
## 内容分为3个部分

* [实习僧网站爬虫](#实习僧网站)
* [前程无忧网站爬虫](#前程无忧网站)
* [数据可视化](#数据分析)
****  
## 实习僧网站
实习僧网站限制了访问速度，如果速度过快IP会被封禁，必须使用sleep函数限速。访问必须携带user-agent，否则会被识别为爬虫

#### 技术栈
所用到的库
`requests`,`bs4`,`pandas`,`urllib3`

****  
#### 使用方法
```python
from sxc import SXCCrawer  

sxc = SXCCrawer()
```

#### 调用参数助手
```python
sxc.HELP()
keyword:职位关键字
例子:算法工程师/Python


city:工作城市
例子:["武汉","北京"]


area:城市区域
例子:朝阳区


city:职位发布时间
day:今天发布
wek:这周发布
mon:三十天内发布


mon:实习时间
1:一个月
2:两个月
3:三个月
4:三个月以上


day:一周工作天数
1:1天
2:2天
3:3天
4:4天
5:5天
6:6天以上


degree:学历要求
大专:大专
本科:本科
硕士:硕士
博士:博士


salary:日薪
-0:不限
0-100:0-100
100-150:100-150
150-200:150-200
200-300:200-300
300-:300以上

```
#### 设置参数
```python
#设置城市和关键字参数
设置参数函数
setParams(self,keyword='',area='',months='',days='',degree='',official='',salary='-0',publishTime='',city='')

city = ['武汉','北京']
cra.setParams(keyword='算法',city=city)
```
#### 开始下载,csv文件会保存在当前目录
```python
 cra.run()
```

****  
## 前程无忧网站
因为前程无忧几乎没有做任何反爬，所以使用了多线程加速爬取过程，同时爬取多个城市的职位信息，并且把多线程封装到了函数内方便日后修改。

#### 技术栈
所用到的库
`requests`,`lxml.etree`,`pandas`,`urllib3`,`threading`

#### 使用方法
调用 multiTrhead函数后直接开始下载，csv文件会保存在当前目录
```
from job51 import multiTread

#设置关键字
city = ['深圳','杭州','北京','上海','武汉']
keyword = 'Python'
multiTrehad(cityList=city,keyword=keyword)

```

****  
## 数据分析
1. 使用pandas基础数据清洗，包括去除带有缺失字段的数据，去除重复数据
2. 使用jieba分词,并进一步处理，去除stop words
3. 进行词频统计
4. 使用gensim中的Word2Vec计算词向量
5. 使用sklarn中的PCA降维到2或3维并使用KMeans方法类聚
6. 使用matplot绘2d或3d图  

#### 技术栈
所用到的库
`sklearn`,`pandas`,`numpy`,`jieba`,`wordCould`,`sklearn`,`matplotlib`,`gensim`

#### 使用方法
```
ana = SXSAnalyser(path ='./算法intern全国45.csv')

#minCount，词频阈值，低于数字的就不会被统计，默认10
#select, 绘图词数值，默认100

ana.prapaerData(select=,minCount=)

#图片会自动保存在目录的./image/

#绘制词云图
ana.drawCloud()

#绘制2D类聚词向量图
#ana.draw2D()

#绘制3D类聚词向量图
ana.draw3D()


#绘制柱状图
ana.drawBar()
```

## 可视化展示

#### 词云图
![image](https://github.com/prefect12/jobFinder/blob/master/image/%E7%AE%97%E6%B3%95intern%E5%85%A8%E5%9B%BD45wordCloud.jpg)
（点击图片查看大图）<br>
<br>
<br>


#### 排名靠前的关键字
![image](https://github.com/prefect12/jobFinder/blob/master/image/%E7%AE%97%E6%B3%95intern%E5%85%A8%E5%9B%BD45BarChart.jpg)
（点击图片查看大图）<br>
<br>
<br>


#### 降至2维可视化
![image](https://github.com/prefect12/jobFinder/blob/master/image/%E7%AE%97%E6%B3%95intern%E5%85%A8%E5%9B%BD452D.jpg)
（点击图片查看大图）
<br>
<br>


#### 降至3维可视化
![image](https://github.com/prefect12/jobFinder/blob/master/image/%E7%AE%97%E6%B3%95intern%E5%85%A8%E5%9B%BD453D.png)
（点击图片查看大图）
