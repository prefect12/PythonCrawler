# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 14:09:38 2020

@author: Administrator
"""


from parsel import Selector


html = '''
<em class="rel">
    <b style="width:48px;left:-48px">
        <i style="width: 16px;">4</i>
        <i style="width: 16px;">0</i>
        <i style="width: 16px;">5</i>
    </b>
    <b style="width: 16px;left:-16px">8</b>
</em>
<em class="rel">
    <b style="width:48px;left:-48px">
        <i style="width: 16px;">0</i>
        <i style="width: 16px;">7</i>
        <i style="width: 16px;">3</i>
    </b>
    <b style="width: 16px;left:-32px">3</b>
    <b style="width: 16px;left:-48px">6</b>
    <b style="width: 16px;left:-16px">0</b>
</em>
'''

content = Selector(html)
def get_price(content):
    for price in content.xpath('//em[@class="rel"]'):
        backNums = []
        frontDict = {}
        #获取底层
        back = price.xpath('.//b[1]/i')
        
        #获取上层
        front = price.xpath('.//b')[1:]
        
        #获取底层数字，放入list
        for iTag in back:
            backNums.append(iTag.xpath('./text()').extract_first())
            
        #get left offset and number put in dict
        for bTag in front:
            left = int(bTag.xpath('./@style').extract_first().split(';')[1][5:-2])
            num = bTag.xpath('./text()').extract_first()
            frontDict[int(left/16)] = num
        
        #restore the real price
        for index,val in frontDict.items():
            backNums[index] = val
        print(''.join(backNums))

