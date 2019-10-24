# coding:utf-8
# 把test_case目录添加到path下
import sys
sys.path.append("E:\\20190611\\python\\Python27\\Lib\\unittest\\untitled\\test_case")

from test_case import start_baidu
from test_case import start_youdao
from test_case import start_test

#用例文件列表
def caselist():
    alltestnames = [
        start_baidu.Baidu,
        start_youdao.Youdao,
        start_test.Login
    ]
    print "success read case list!!"

    return alltestnames