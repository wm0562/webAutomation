# coding:utf-8
from selenium import webdriver
import time

option=webdriver.ChromeOptions()
option.add_argument("disable-infobars")

# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')

# 关键词搜索
# driver = webdriver.Chrome(chrome_options=option)
# driver.get("https://www.baidu.com/")
# driver.maximize_window()
# driver.find_element_by_id('kw').click()
# driver.find_element_by_id('kw').clear()
# driver.find_element_by_id("kw").send_keys("selenium + python + pychame")
# driver.find_element_by_id("su").click()
# driver.close()

# 调节浏览器宽高
# driver = webdriver.Chrome(chrome_options=option)
# driver.get("https://www.baidu.com/")
# driver.set_window_size(400, 300)

# 控制浏览器前进和后退
driver = webdriver.Chrome(chrome_options=option)
# 访问百度首页
first_url = 'http://www.baidu.com'
print  "now access %s" %(first_url)
driver.get(first_url)
# 访问新闻页面
second_url = 'http://news.baidu.com'
print  "now access %s" %(second_url)
driver.get(second_url)
# 返回（后退）到百度首页
print "back to %s"%(first_url)
driver.back()
# 前进到新闻业页
print "forward to %s"%(second_url)
driver.forward()

