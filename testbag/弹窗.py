# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
time.sleep(2)
#点击打开搜索设置
setting = driver.find_element_by_css_selector("#u1 > a.pf")
ActionChains(driver).move_to_element(setting).perform()
# driver.find_element_by_css_selector("#u1 > a.pf").find_element_by_css_selector("#wrapper > div.bdpfmenu > a.setpref").click()
time.sleep(2)
driver.find_element_by_css_selector("#wrapper > div.bdpfmenu > a.setpref").click()
time.sleep(2)
#点击保存设置
driver.find_element_by_css_selector("#gxszButton > a.prefpanelgo").click()
time.sleep(2)
#获取网页上的警告信息
alert = driver.switch_to_alert()
#接收警告信息
alert.accept()
print alert
driver.quit()