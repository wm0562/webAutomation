# coding:utf-8
from selenium import webdriver

# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')

driver = webdriver.Chrome(chrome_options=option)
driver.get("https://www.baidu.com/")
# driver.maximize_window()
driver.find_element_by_id('kw').click()
driver.find_element_by_id('kw').clear()
driver.find_element_by_id("kw").send_keys(u"百度云")
# driver.find_element_by_id("kw").send_keys("selenium + python + pychame")
driver.find_element_by_id("su").click()
# driver.close()
