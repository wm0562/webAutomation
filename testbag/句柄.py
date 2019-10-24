# coding:utf-8
from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_argument("diable-infobars")

driver = webdriver.Chrome(chrome_options=option)
driver.get("http://www.baidu.com/")
#获得当前窗口
nowhandle = driver.current_window_handle
driver.find_element_by_css_selector("#u1 > a.lb").click()
time.sleep(3)
#打开注册新窗口
driver.find_element_by_xpath("//*[@id='passport-login-pop-dialog']/div/div/div/div[4]/a").click()
#获得所有窗口
allhandles = driver.window_handles
#循环判断窗口是否为当前窗口
for handle in allhandles:
 if handle != nowhandle:
  driver.switch_to_window(handle)
print 'now register window!'
#切换到登录标签
driver.find_element_by_css_selector("#login_btn").click()
time.sleep(3)
driver.close()
#回到原先的窗口
driver.switch_to_window(nowhandle)
driver.find_element_by_id("kw").send_keys(u"注册成功！")
time.sleep(3)
driver.quit()