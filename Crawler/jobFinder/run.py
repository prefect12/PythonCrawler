# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:52:44 2020

@author: Administrator
"""

from sxc import SXCCrawer
from job51 import multiTread
from processor import SXSAnalyser

sxc = SXCCrawer()

#调用参数助手
sxc.HELP()

#设置参数，开始爬取
sxc.setParams(keyword='爬虫' ,city = ['北京','上海','广州','深圳'])
sxc.run()

#获取路径
ana = SXSAnalyser(path ='./算法intern全国45.csv')

ana.draw2D()