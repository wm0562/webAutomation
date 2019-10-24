# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

def logout(self):
    driver = self.driver
    lu = driver.find_element_by_css_selector("#user > a")
    ActionChains(driver).move_to_element(lu).perform()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='out1']/a[3]/span").click()
    time.sleep(2)