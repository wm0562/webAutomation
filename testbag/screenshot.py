# coding:utf-8
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("disable-infobars")

browser = webdriver.Chrome(chrome_options=option)
browser.get("http://www.baidu.com")
# 捕捉百度异常
try:
    browser.find_element_by_id("kwsss").send_keys("selenium")
    browser.find_element_by_id("su").click()
except:
    browser.get_screenshot_as_file("E:/20190611/python/pychame/data/test.png")

    browser.quit()