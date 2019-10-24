# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')

# 打开chrome浏览器
driver = webdriver.Chrome(chrome_options=option)
driver.get("https://www.baidu.com")

# css定位
driver.find_element_by_css_selector("#u1 > a.lb").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
driver.find_element_by_css_selector("#TANGRAM__PSP_10__userName").send_keys("17774008145")
driver.find_element_by_css_selector("#TANGRAM__PSP_10__password").send_keys("mima")
driver.find_element_by_css_selector("#TANGRAM__PSP_10__memberPass").click()
time.sleep(2)
driver.find_element_by_css_selector("#TANGRAM__PSP_10__submit").click()
# xpath定位
# driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
print(driver.title)
print driver.quit()

