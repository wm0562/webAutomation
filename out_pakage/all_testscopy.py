# coding:utf-8
import unittest
# 把test_case目录添加到path下，这里用的相对路径
import sys
sys.path.append("E:\\20190611\\python\\Python27\\Lib\\unittest\\untitled\\test_case")

# from test_case import youdao
# from test_case import baidu
# from test_case import test

import HTMLTestRunner
import time
import allcase_list

#获取数组方法
alltestnames = allcase_list.caselist()

# alltestnames = [
#     baidu.Baidu,
#     youdao.Youdao,
#     test.Login
# ]

testunit = unittest.TestSuite()

# 将测试用例加入到测试容器中--不同路径下
# testunit.addTest(unittest.makeSuite(baidu.Baidu))
# testunit.addTest(unittest.makeSuite(youdao.Youdao))
# ---另写一个用例数组
for tests in alltestnames:
    testunit.addTest(unittest.makeSuite(tests))

#取当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

#定义个报告存放路径，支持相对路径
filename = "E:\\20190611\\python\\Python27\\report\\"+now+'result.html'
fp = file(filename, 'wb')

# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'百度搜索测试报告',
    description=u'用例执行情况： '
)

#运行测试用例
runner.run(testunit)

# # 执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(testunit)