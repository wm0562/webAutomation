# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True
# 私有云登录用例
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        # + "/login/?referrer=http%3A%2F%2Fwebcloud.kuaibo.com%2F")
        # driver.maximize_window()
# 登陆
        # css定位
        driver.find_element_by_css_selector("#u1 > a.lb").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
        driver.find_element_by_css_selector("#TANGRAM__PSP_10__userName").send_keys("17774008145")
        driver.find_element_by_css_selector("#TANGRAM__PSP_10__password").send_keys("wm961125")
        driver.find_element_by_css_selector("#TANGRAM__PSP_10__memberPass").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#TANGRAM__PSP_10__submit").click()
        time.sleep(3)

        # driver.find_element_by_css_selector("#TANGRAM__39__header_a").click()
# # 新功能引导
#         driver.find_element_by_class_name("guide-ok-btn").click()
#         time.sleep(3)
# 退出
        exit = driver.find_element_by_css_selector("#s_username_top > span")
        ActionChains(driver).move_to_element(exit).perform()
        time.sleep(3)
        driver.find_element_by_css_selector("#s_user_name_menu > div > a.quit").click()
        # time.sleep(2)
        # driver.find_element_by_link_text("退出").click()
        time.sleep(2)
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        if __name__ == "__main__":
         unittest.main()

