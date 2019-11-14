# coding:utf-8
import os
import pickle
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

brower = webdriver.Chrome()
wait = WebDriverWait(brower, 10)

def getTaobaoCookies():
    # get login taobao cookies
    url = "http://test360admin.weilianupup.com/index.html"
    brower.get("http://test360admin.weilianupup.com/xqf-login.html")
    while True:
        print("Please login in test360")
        time.sleep(3)
        # if login in successfully, url  jump to www.taobao.com
        while brower.current_url == url:
            tbCookies = brower.get_cookies()
            brower.quit()
            cookies = {}
            for item in tbCookies:
                cookies[item['name']] = item['value']
            outputPath = open('test360.pickle','wb')
            pickle.dump(cookies,outputPath)
            outputPath.close()
            return cookies

def readTaobaoCookies():
    # if hava cookies file ,use it
    # if not , getTaobaoCookies()
    if os.path.exists('test360.pickle'):
        readPath = open('test360.pickle','rb')
        tbCookies = pickle.load(readPath)
    else:
        tbCookies = getTaobaoCookies()
    return tbCookies

tbCookies = readTaobaoCookies()

brower.get("http://test360admin.weilianupup.com/index.html")
for cookie in tbCookies:
    brower.add_cookie({
        "domain":".taobao.com",
        "name":cookie,
        "value":tbCookies[cookie],
        "path":'/',
        "expires":None
    })
brower.get("http://test360admin.weilianupup.com/")



