# coding:utf-8
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("diable-infobars")

driver = webdriver.Chrome(chrome_options=option)
driver.get("http://passport.kuaibo.com/login/?referrer=http%3A%2F%2Fwebclou d.kuaibo.com%2F")
driver.find_element_by_id("user_name").clear()
driver.find_element_by_id("user_name").send_keys("username")
driver.find_element_by_id("user_pwd").clear()
driver.find_element_by_id("user_pwd").send_keys("password")
driver.find_element_by_id("dl_an_submit").click()
#通过submit()来提交操作
#driver.find_element_by_id("dl_an_submit").submit()

# driver.quit()

