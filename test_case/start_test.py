# coding:utf-8
from selenium import webdriver
import unittest, time
# from test_case.public import login, logout
import sys
sys.path.append("E:\\20190611\\python\\Python27\\Lib\\unittest\\untitled\\test_case\\public")
from public import login
from public import logout

class Login(unittest.TestCase):
    """登录退出"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(70)
        self.base_url = "http://hzxh.zjzwfw.gov.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True

# 浙江政务网登录用例
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url+'/')
# 调用登录模块
        login.login(self)
# 获取用户名
        user = driver.find_element_by_css_selector("#infor > div.head-portrait > a > div").text
# 用户名是否正确，不正确抛出异常
        if user == u'敏':
            print '登录成功'
        else:
            raise NameError('user name error!')
        time.sleep(3)
# 退出用例
        logout.logout(self)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
   unittest.main()
