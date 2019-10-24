# coding:utf-8
import HTMLTestRunner
import unittest
import os
import time

listaa = 'E:\\20190611\\python\\Python27\\Lib\\unittest\\untitled\\test_case'
def creatsuite1():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(listaa, pattern='start_*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
        print testunit
    return testunit

alltestnames = creatsuite1()

now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
filename = 'E:\\20190611\\python\\Python27\\report\\'+now+'result.html'
fp = file(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'百度搜索测试用例',
    description=u'用例执行情况： '
)

##########控制什么时间执行脚本#####
k = 1
while k < 2:
    timing = time.strftime('%H_%M', time.localtime(time.time()))
    if timing == '10_21':
        print u'开始运行脚本： '
        runner.run(alltestnames)
        print u'运行完成退出'
        break
    else:
        time.sleep(10)
        print timing

