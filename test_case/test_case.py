# coding:utf-8
import os
#列出某个文件夹下的所有case,这里用的是python
#所在py文件运行一次后会生成一个pyc的副本
caselist = os.listdir('E:\\20190611\\python\\Python27\\Lib\\unittest\\untitled\\test_case')
print caselist
for a in caselist:
    s = a.split('.')[1]  # 选取后缀名为py的文件
    print a
    print s
    if s == 'py':
    # 此处执行dos命令并将结果保存到log.txt
     os.system('E:\\20190611\\python\\Python27\\Lib\\unittest\\untitled\\test_case\\%s 1>>log.txt 2>&1' %a)