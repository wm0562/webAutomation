# coding:utf-8
from selenium import webdriver
import time, os

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('js.html')
driver.get(file_path)
time.sleep(3)
#######通过 JS 隐藏选中的元素##########第一种方法：
#隐藏文字信息
# driver.execute_script('$("#tooltip").fadeOut();')
# # driver.execute_script('document.getElementByTd("tooltip")')
# # driver.execute_script('$("#tooltip").fadeOut();')
# time.sleep(5)

print "隐藏文字成功"
time.sleep(5)
#隐藏按钮：
bu = 'document.querySelector("body > div > div > a.btn")'
bt = bu.fadeOut()
# button = driver.find_element_by_class_name('btn')
driver.execute_script(bt, bu)
# driver.execute_script('$(arguments[0]).fadeOut()', button)
time.sleep(5)
driver.quit()
