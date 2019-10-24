# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 邮件信息配置
sender = '1455448378@qq.com'
receiver = '1785545205@qq.com'
subject = 'python email test'
smtpserver = 'smtp.qq.com'
username = '1455448378@qq.com'
password = 'wocujwtrjyprfjib'

# 以HTML形式文件内容
msg = MIMEText('<html><h1>测试HTML邮件</h1></html>','html')
msg['Subject'] = subject

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
