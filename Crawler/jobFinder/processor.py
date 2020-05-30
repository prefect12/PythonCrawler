# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:11:02 2020

@author: Administrator
"""
#encoding=utf-8

import pandas as pd
import numpy as np
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import os
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans,MeanShift
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from numpy import linspace
import random


plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False


class SXSAnalyser:
    
    def __init__(self,path,userDict='./stopwords/dict.txt',stopWords='./stopwords/sum.txt'):
        if not os.path.exists('./image'):
                os.makedirs('./image')
        
        self.__path = path
        self._df = pd.read_csv(filepath_or_buffer=path,engine='python')
        self.FiltereDf = self._df
        jieba.load_userdict(userDict)
        stopWords = np.array(pd.read_csv(filepath_or_buffer=stopWords,header=None)).T.tolist()[0]
        
        
        self.__DeRedundancy()
        self.__RemoveStopWords(stopWords)
        self.__getWordFrequency()
        self.prapaerData()
        
    def __saveImag(self,plt,name):
        path = './image/' + self.__path[2:-4] + name + '.jpg'
        print(path)
        if name != '3D':
            plt.savefig(path,bbox_inches='tight')
        else:
            pass
        
    
    def prapaerData(self,select = 100,minCount = 10):
        self.__showWords = self.__wordsSelector(select,minCount)
        self.__wordVector = self.__getwordVec(self.__showWords)
    
    
    #数据去重
    def __DeRedundancy(self):
        self._df.dropna(subset=['jobUrl'],inplace=True)
        self._df.fillna(value='',inplace=True)
        self._df.drop_duplicates(['title','companyName','jobDescrib'],inplace = True)
        self._df.index = range(len(self._df))


    #预处理，删除 stop words
    def __RemoveStopWords(self,stopWord):
        self._df['jobDescrib'] = self._df['jobDescrib'].apply(lambda x:re.sub('�0|�1|�6|�2|[【】◆]','',x.lower()))
        self._df['title'] = self._df['title'].apply(lambda x:re.sub('�0|�1|�6|�2|[【】◆]','',x.lower()))
        self._df['titleWord'] = self._df['title'].apply(lambda x:[i for i in jieba.lcut(x) if len(i)>=2 ])
        self._df['jobDesWord'] = self._df['jobDescrib'].apply(lambda x:[i for i in jieba.lcut(x) if len(i)>=2 and i not in stopWord])


    # 计算词频
    def __getWordFrequency(self):
        wordDf = pd.DataFrame({'Word':np.concatenate(self._df.jobDesWord)})
        wordStat = wordDf.groupby(by=['Word'])["Word"].agg({'number':np.size})
        self._wordStat = wordStat.reset_index().sort_values(by='number',ascending=False)


    def __wordsSelector(self,select,minCount):
        #根据数字选择
        wordStat2 = self._wordStat.loc[self._wordStat['number'] >= minCount]
        if select < 1:
            num = int(len(wordStat2)*select)
        else:
            num = select
        wordStat3 = wordStat2.head(num)
        showWord = np.array(wordStat3['Word']).tolist()
        return showWord

    
    def __getwordVec(self,showWord):
        SentenceList = np.array(self._df.jobDesWord).T.tolist()
        self._model = Word2Vec(SentenceList,min_count=10)
        wordVec = self._model.wv[showWord]
        return wordVec
    
    
    def draw2D(self):
        model = TSNE(n_components=2)
        result = model.fit_transform(self.__wordVector)

        model = KMeans(5)
        lable = model.fit_predict(result)
        cm_subsection = linspace(0,1,5)
        colors = [cm.rainbow(x) for x in cm_subsection]
        random.shuffle(colors)


        fig = plt.figure(figsize=(20,12))
        for i,word in enumerate(self.__showWords):
                plt.scatter(result[i,0],result[i,1],color = colors[lable[i]])
                plt.annotate(word,xy=(result[i,0],result[i,1]))
        fig.show()

        
        self.__saveImag(plt,'2D')
        
    def draw3D(self):
        model = PCA(n_components=3)
        result = model.fit_transform(self.__wordVector)
        
        ax = plt.axes(projection='3d')
        fig = plt.figure()
        ax = Axes3D(fig)

        for i,word in enumerate(self.__showWords):
                ax.scatter3D(result[i,0],result[i,1],result[i,2])
                ax.text(result[i,0],result[i,1],result[i,2],word)
        self.__saveImag(ax,'3D')
    
    def drawCloud(self):
        wordList= ''

        word = np.array(self._wordStat['Word']).tolist()
        nums = np.array(self._wordStat['number']).tolist()
        fig = plt.figure(figsize=(20,12))
        
        for i in range(len(nums)):
            wordList += (word[i] + ' ')*nums[i]
    
        wordcloud = WordCloud(collocations=False,scale=8,font_path='simhei.ttf',background_color='white').generate(wordList)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        fig.show()
        self.__saveImag(plt,'wordCloud')
        
    
    def drawBar(self,nums=35):
        pltData = self._wordStat.head(nums)
        fig = plt.figure(figsize=(20,12))

        plt.xlabel('关键字')
        plt.ylabel('出现次数')
        plt.title('招聘关键字分析')
        plt.xticks(rotation = 45)
        plt.bar(pltData['Word'],pltData['number'])
        fig.show()
        self.__saveImag(plt,'BarChart')
    
    def strongFilter(self,keywords=[''],save=False):
        if not keywords:
            print('Input KeyWords')
        Filter = '|'.join(keywords)
        newDF = self._df.loc[self._df['title'].str.contains(Filter)]
        if save:
            newDF.to_csv('./'+Filter+'.csv',encoding='GBK',index=False)
        
    
if __name__ == "__main__":
    ana = SXSAnalyser(path="./算法intern全国45.csv")
    