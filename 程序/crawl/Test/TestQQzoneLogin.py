from selenium import webdriver
import time
#实例化出一个Firefox浏览器
driver = webdriver.Chrome()

#设置浏览器窗口的位置和大小
driver.set_window_position(20, 40)
driver.set_window_size(1100,700)

#打开一个页面（QQ空间登录页）
driver.get('https://user.qzone.qq.com/2779890646/311')
#登录表单在页面的框架中，所以要切换到该框架
driver.switch_to_frame('login_frame')
#通过使用选择器选择到表单元素进行模拟输入和点击按钮提交
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').clear()
driver.find_element_by_id('u').send_keys('2844577946')
driver.find_element_by_id('p').clear()
time.sleep(5)
driver.find_element_by_id('p').send_keys('yzx19941112')
time.sleep(5)
driver.find_element_by_id('login_button').click()

#do something….
#退出窗口
# driver.quit()
