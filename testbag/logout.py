# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

def logout(self):
    driver = self.driver
    exit = driver.find_element_by_css_selector("#s_username_top > span")
    ActionChains(driver).move_to_element(exit).perform()
    time.sleep(3)
    driver.find_element_by_css_selector("#s_user_name_menu > div > a.quit").click()
    time.sleep(2)
    driver.find_element_by_css_selector("#tip_con_wrap > div.button-wrap > a.s-btn.btn-ok").click()
    time.sleep(2)