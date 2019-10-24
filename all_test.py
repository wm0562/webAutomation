# coding:utf-8
import unittest
# 把test_case目录添加到path下，这里用的相对路径
import os
# sys.path.append("E:\\20190611\\python\\Python27\\Lib\\unittest\\untitled\\test_case")
import HTMLTestRunner
import time
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# 定义发送邮件
def sentmail(file_new):  #发送邮箱
    mail_from = '1455448378@qq.com'
    # 收信邮箱
    mail_to = '1785545205@qq.com'
    # 定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    # 定义标题
    msg['Subject'] = u'百度测试报告'
    # 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP()
    # 连接SMTP服务器
    smtp.connect('smtp.qq.com')
    # 用户密码
    smtp.login('1455448378@qq.com', 'wocujwtrjyprfjib')
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print 'email has send out !'

# 查找测试报告，调用邮件功能
def sendreport():
    result_dir = 'E:\\20190611\\python\\Python27\\report'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn)
    if not os.path.isdir(result_dir+"\\"+fn) else 0)
    print (u'最新测试生产的报告： '+lists[-1])
    # 找到最新生成的文件
    file_new = os.path.join(result_dir, lists[-1])
    print file_new
    # 调用发邮件
    sentmail(file_new)

listaa = "E:\\20190611\\python\\Python27\\Lib\\unittest\\untitled\\test_case"

def creatsuitel():
    testunit = unittest.TestSuite()

    #discover方法定义
    discover = unittest.defaultTestLoader.discover(listaa,
                                                   pattern='start_*.py',
                                                   top_level_dir=None)
    #discovver 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
            print testunit
    return testunit

alltestnames = creatsuitel()
# now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
# 将测试用例加入到测试容器中
# testunit.addTest(unittest.makeSuite(baidu.Baidu))
# testunit.addTest(unittest.makeSuite(youdao.Youdao))
# for tests in alltestnames:
#     testunit.addTest(unittest.makeSuite(tests))

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

# 运行测试用例
runner.run(alltestnames)
# 执行发邮件
sendreport()

# # 执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(testunit)