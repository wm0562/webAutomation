# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱
sender = '1455448378@qq.com'
# 接收邮箱
receiver = '1785545205@qq.com'
# 发送邮件主题
subject = 'python email test'
# 发送邮箱服务器
smtpserver = 'smtp.qq.com'
# 发送邮箱用户/密码
username = '1455448378@qq.com'
password = 'wocujwtrjyprfjib'

# 中文需参数‘utf-8’，单字节字符不需要
msg = MIMEText('这是发用的邮件内容')  #'text', 'utf-8'
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
