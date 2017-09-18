'''
Created on 2017年4月16日

@author: mywow
'''

#coding:utf-8

import unittest
import time
from selenium import webdriver
from bs4 import BeautifulSoup


class seleniumTest(unittest.TestCase):
    user = '2844577946'  # 你的QQ号
    pw = 'yzx19941112'  # 你的QQ密码

    def setUp(self):
        # 调试的时候用firefox比较直观
#         self.driver = webdriver.PhantomJS()
        self.driver = webdriver.Chrome()

    def testEle(self):
        driver = self.driver
        # 浏览器窗口最大化
        driver.maximize_window()
        # 浏览器地址定向为qq登陆页面
        driver.get("https://user.qzone.qq.com/2779890646/311")
        # 很多时候网页由多个<frame>或<iframe>组成，webdriver默认定位的是最外层的frame，
        # 所以这里需要选中一下frame，否则找不到下面需要的网页元素
        driver.switch_to_frame('login_frame')
        #通过使用选择器选择到表单元素进行模拟输入和点击按钮提交
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys('2844577946')
        driver.find_element_by_id('p').clear()
        
        driver.find_element_by_id('p').send_keys('yzx19941112')
        
        driver.find_element_by_id('login_button').click()
        time.sleep(3)
#     driver.implicitly_wait(3)

        # 如果登录比较频繁或者服务器繁忙的时候，一次模拟点击可能失败，所以想到可以尝试多次，
        # 但是像QQ空间这种比较知名的社区在多次登录后都会出现验证码，验证码自动处理又是一个
        # 大问题，本例不赘述。本例采用手动确认的方式。即如果观察到自动登陆失败，手动登录后
        # 再执行下列操作。
        
        # 让webdriver操纵当前页
        driver.switch_to.default_content()
        # 跳到说说的url
        driver.get("https://user.qzone.qq.com/773885456/311")
        # 访问全部说说需要访问所有分页，需要获取本页数据后点击“下一页”按钮，经分析，“下一页”
        # 按钮的id会随着点击的次数发生变化，规律就是每点一下加一，所以需要在程序中动态的构造
        # 它的id。（或者不用id改用xpath）
        next_num = 0  # 初始“下一页”的id
        fout =open('shuoshuo.html','w',encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table border=1>")
        fout.write("<tr>")
        fout.write("<td>说说的发表时间</td>")
        fout.write("<td>内容</td>")
        fout.write("</tr>")
        while True:
            # 下拉滚动条，使浏览器加载出动态加载的内容，可能像这样要拉很多次，中间要适当的延时（跟网速也有关系）。
            # 如果说说内容都很长，就增大下拉的长度。
            driver.execute_script("window.scrollBy(0,10000)")
            time.sleep(3)
            driver.execute_script("window.scrollBy(0,20000)")
            time.sleep(3)
            driver.execute_script("window.scrollBy(0,30000)")
            time.sleep(3)
            driver.execute_script("window.scrollBy(0,40000)")
            time.sleep(5)
            # 很多时候网页由多个<frame>或<iframe>组成，webdriver默认定位的是最外层的frame，
            # 所以这里需要选中一下说说所在的frame，否则找不到下面需要的网页元素
            driver.switch_to.frame("app_canvas_frame")
            soup = BeautifulSoup(driver.page_source, 'xml')
            contents = soup.find_all('pre', {'class': 'content'})  # 内容
            times = soup.find_all('a', {'class': 'c_tx c_tx3 goDetail'})  # 发表时间
            
            
            for content, _time in zip(contents, times):  # 这里_time的下划线是为了与time模块区分开
#                 print(content.get_text())
#                 print(_time.get_text())
#                 print (content.get_text(), _time.get_text())
                fout.write("<tr>")
                fout.write("<td>%s</td>" % _time)
                fout.write("<td>%s</td>" % content)
                fout.write("</tr>")
            # 当已经到了尾页，“下一页”这个按钮就没有id了，可以结束了
            if driver.page_source.find('pager_next_' + str(next_num)) == -1:
                break
            # 找到“下一页”的按钮
            elem = driver.find_element_by_id('pager_next_' + str(next_num))
            # 点击“下一页”
            elem.click()
            # 下一次的“下一页”的id
            next_num += 1
            # 因为在下一个循环里首先还要把页面下拉，所以要跳到外层的frame上
            driver.switch_to.parent_frame()
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>") 
        fout.close()
    def tearDown(self):
        print ('down')

if __name__ == "__main__":
    unittest.main()
