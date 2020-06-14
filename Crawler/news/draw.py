# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 01:00:01 2020

@author: Administrator
"""

import pandas as pd
import numpy as np
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from collections import Counter

plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False

#数据预处理
def preprocessor(df):
    #去除ana行
    df.dropna(inplace=True)
    #去除重复行
    df.drop_duplicates(inplace = True)
    
    #转换为numpy
    k = np.array(df[:][:])
    
    #转化为字符串
    s = ' '.join([str(i) for i in k])
    
    #去除符号
    s = re.sub('\n|。|[|？| |*-|\r|\|\'|-|“|"|-|【|】|]|！|!','',s)
    
    #读取停止词
    stopWords = np.array(pd.read_csv(filepath_or_buffer='./sum.txt',header=None)).T.tolist()[0]
    
    #分词
    words = [i for i in jieba.lcut(s) if i not in stopWords]
    
    return words

#画云图
def drawCloud(words,title):

    #拼接成字符串
    words = ' '.join(words)
    
    #设置画布大小
    fig = plt.figure(figsize=(20,12))
    
    #设置云图属性
    wordcloud = WordCloud(collocations=False,scale=8,font_path='simhei.ttf',background_color='white').generate(words)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title('{}'.format(title))
    
    #显示图片
    fig.show()


#画柱状图
def drawBar(words,title,nums=20):
    
    #统计词频
    wordDic = Counter(words)
    
    #打包成字典
    dicList = [[i,j] for i,j in wordDic.items() if len(i) >= 2]
    
    #排序
    dicList.sort(key=lambda x: x[1],reverse=True)
    
    #选取前n个元素
    wordList = [dicList[i][0] for i in range(nums)]
    countList = [dicList[i][1] for i in range(nums)]
    
    #设置画布大小
    fig = plt.figure(figsize=(20,12))

    #画图
    plt.xlabel('关键字')
    plt.ylabel('出现次数')
    plt.title('{}出现次数最多的{}个词'.format(title,nums))
    plt.xticks(rotation = 45)
    plt.bar(wordList,countList)
    fig.show()
 
        
#读取csv
dfTianya = pd.read_csv('tianya.csv')
dfXinlang = pd.read_csv('xinlang.csv')

#预处理，返回字符串
tianyaWords = preprocessor(dfTianya)
xinlangWords = preprocessor(dfXinlang)

#画图
drawCloud(tianyaWords,'天涯论坛')
drawCloud(xinlangWords,'中国新闻网')
drawBar(tianyaWords,'天涯论坛')
drawBar(xinlangWords,'中国新闻网')