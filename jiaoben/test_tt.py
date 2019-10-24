# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import unittest
import re
import time

class TestTt(unittest.TestCase):
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.url = "http://www.baidu.com/"
    self.driver.implicitly_wait(30)
    self.vars = {}
  
  def test_tt(self):
    driver = self.driver
    driver.get(self.url)
    # driver.set_window_size(782, 692)
    driver.find_element_by_link_text("登录").click()
    time.sleep(2)
    driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
    driver.find_element_by_id("TANGRAM__PSP_10__userName").click()
    driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("17774008145")
    driver.find_element_by_id("TANGRAM__PSP_10__password").click()
    self.driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("wm961125")
    self.driver.find_element_by_id("TANGRAM__PSP_10__memberPass").click()
    time.sleep(2)
    self.driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
    element = self.driver.find_element_by_id("vcode-spin-bottom370")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)
    self.driver.find_element_by_link_text("退出").click()
    time.sleep(2)
    self.driver.find_element_by_link_text("确定").click()
    time.sleep(3)
    self.driver.close()
  
  def teardown_method(self, method):
    self.driver.quit()