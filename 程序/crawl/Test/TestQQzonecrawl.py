'''
Created on 2017年4月16日

@author: mywow
'''
from bs4 import BeautifulSoup
from selenium import webdriver
import time

#使用selenium
driver = webdriver.Chrome()

#登录QQ空间
def get_shuoshuo(qq):
    driver.get('https://user.qzone.qq.com/2779890646/311')
#     time.sleep(5)
    try:
        driver.find_element_by_id('login_div')
        a = True
    except:
        a = False
    if a == True:
        driver.switch_to_frame('login_frame')
        #通过使用选择器选择到表单元素进行模拟输入和点击按钮提交
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys('2844577946')
        driver.find_element_by_id('p').clear()
        
        driver.find_element_by_id('p').send_keys('yzx19941112')
        
        driver.find_element_by_id('login_button').click()
        time.sleep(3)
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
        b = True
    except:
        b = False
    if b == True:
        driver.switch_to.frame('app_canvas_frame')
        content = driver.find_elements_by_css_selector('.content')
#         print(content)
        stime = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
#         print(stime)
        
        
        for con,sti in zip(content,stime):
            data = {
                'time':sti.text,
                'shuos':con.text
            }
#             print(data)
        pages = driver.page_source
        soup = BeautifulSoup(pages,'lxml')
#         print(soup)
#         fout =open('output.html','w',encoding='utf-8')
#         for strs in soup.get('rt_createTime2'):
#             fout.write(strs)
#         
#         fout.close()


#     cookie = driver.get_cookies()
#     cookie_dict = []
#     for c in cookie:
#         ck = "{0}={1};".format(c['name'],c['value'])
#         cookie_dict.append(ck)
#     i = ''
#     for c in cookie_dict:
#         i += c
#     print('Cookies:',i)
#     print("==========完成================")

    driver.close()
    driver.quit()

if __name__ == '__main__':
    get_shuoshuo('2779890646')