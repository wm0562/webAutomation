# coding:utf-8
import csv
import sys
print sys.getdefaultencoding()
# 导入 csv 包
# 读取本地 CSV 文件
my_file = 'E:\\20190611\\python\\pychame\\data\\test.csv'
data = csv.reader(file(my_file, 'rb'))
# 循环输出每一行信息
for user in data:
 print user[0]
 print user[1]
 print user[2].decode('gbk').encode('utf-8')
 print user[3]