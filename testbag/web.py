# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time
import login  # 导入登录文件
import logout # 导入退出文件

class Login(unittest.TestCase):
 def setUp(self):
  self.driver = webdriver.Chrome()
  self.driver.implicitly_wait(30)
  self.base_url = "http://www.baidu.com"
  self.verificationErrors = []
  self.accept_next_alert = True
# 百度登录用例
 def test_login(self):
  driver = self.driver
  driver.get(self.base_url)
# 调用登录模块
  login.login(self)
# 获取用户名
  user=driver.find_element_by_css_selector("#s_username_top > span").text
# 用户名是否正确，不正确抛出异常
  if user==u'默默ppt是我':
   print '登录成功'
  else:
   raise NameError('user name error!')
time.sleep(3)
# 退出用例
def test_logout(self):
 driver=self.driver
 logout.logout(self)

def tearDown(self):
  self.driver.quit()
  self.assertEqual([], self.verificationErrors)
  if __name__ == "__main__":
   unittest.main()
