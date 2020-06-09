
# 知乎倒立文字英文验证码突破
### 项目介绍：

####  使用selenium和验证码识别库完成知乎的登陆。  
#### 因为知乎必须登陆才能爬取，有个登陆脚本就可以获取cookies并构建cookies池用作进一步的爬取。


**** 
### 项目逻辑
![css](./imgs/流程图.png)  



**** 
### 分析

知乎验证码有两种，英文数字验证码和倒立文字验证码。两种随机出现。其中倒立文字验证码可以使用zheye库识别坐标，并使用selenium控制鼠标



**** 

#### 技术栈
`selenium`,`zheye`,`超级鹰`


##### 代码
使用browser执行js脚本，修改元素的style
```python
browser.execute_script('document.querySelectorAll("canvas")[3].style=""')
```
**** 

调用zheye，返回倒立文字位置
```python
    def zheye(self,path):
        z = zheye()
        position = z.Recognize(path)
        return position
```
**** 

调用超级鹰api，返回验证码字符串。
```python
    def charNum(self,path):
        chaojiying = Chaojiying_Client('username', 'password', '1902')  # 用户中心>>软件ID 生成一个替换 96001
        im = open(path, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        mystr = chaojiying.PostPic(im, 1902)['pic_str']
        return mystr

```
****
通过 selenium 点击倒立文字
```python
    #点击文字
    def clickWords(self,clickLocation):
        ele = self.img_ele
        for word in clickLocation:
            x = word[1]//2
            y = word[0]//2
            ActionChains(self.browser).move_to_element_with_offset(ele,xoffset=x,yoffset=y).click().perform()
            time.sleep(0.5)
```
****
在浏览器内输入字符串验证码
```python
   def inputChar(self,char):
        input_box = self.browser.find_element_by_xpath('//input[@name="captcha"]')
        input_box.send_keys(char)

```
****
## 注意：

需要修改知乎账号密码以及超级鹰账号密码



