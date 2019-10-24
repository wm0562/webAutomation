# coding:utf-8
from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
# 打开上传文件页面
# 文件保存于该程序所在文件中
file_path = 'file:///' + os.path.abspath('upload_file.html')
driver.get(file_path)
time.sleep(2)
# files = "‪C:\\Users\chengpiao\\Desktop\\sele.txt"
# print files
# 定位上传按钮，添加本地文件
driver.find_element_by_xpath("/html/body/div/div/input").send_keys("‪C:\\Users\chengpiao\\Desktop\\sele.txt")
time.sleep(2)
print "上传按钮点击成功"
print "浏览文件"
time.sleep(2)
driver.quit()