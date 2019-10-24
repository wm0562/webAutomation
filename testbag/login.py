# coding:utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time
#登陆模块（函数）
def login(self):
 driver = self.driver
 # driver.maximize_window()
 # css定位
 driver.find_element_by_css_selector("#u1 > a.lb").click()
 time.sleep(3)
 driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
 driver.find_element_by_css_selector("#TANGRAM__PSP_10__userName").send_keys("17774008145")
 driver.find_element_by_css_selector("#TANGRAM__PSP_10__password").send_keys("wm961125")
 # 下次登录勾选去掉
 driver.find_element_by_css_selector("#TANGRAM__PSP_10__memberPass").click()
 time.sleep(2)
 # 点击登录
 driver.find_element_by_css_selector("#TANGRAM__PSP_10__submit").click()
 time.sleep(2)
 # 点击发送验证码
 driver.find_element_by_css_selector("#TANGRAM__39__button_send_mobile").click()
 time.sleep(25)
# 点击确定
 driver.find_element_by_css_selector("#TANGRAM__39__button_submit").click()
 time.sleep(3)