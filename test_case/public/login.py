# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest

def login(self):
    driver = self.driver
    # 定位登录
    lg = driver.find_element_by_css_selector("#btnlogin")
    ActionChains(driver).move_to_element(lg).perform()
    time.sleep(2)
    # 点击个人登录
    driver.find_element_by_css_selector("#btn > ul > li:nth-child(1)").click()
    time.sleep(3)
    # 输入用户名 密码
    driver.find_element_by_css_selector("#loginname").send_keys("17774008145")
    driver.find_element_by_css_selector("#loginpwd").send_keys("wm250562")
    driver.find_element_by_css_selector("#submit").click()
    time.sleep(1)
