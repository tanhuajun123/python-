# _*_ coding:utf-8 _*_
#! /usr/bin/python3
import os
os.getcwd()     #返回当前的工作目录
os.chdir('d://aws')    #修改当前的工作目录
os.system('mkdir today')  #执行系统命令 mkdir

#文件高级操作
# import  shutil
# shutil.copyfile('data.ab','archive.ab')
# shutil.move('d:/aws','installdir')

#文件通配符
import  glob
glob.glob('*.py')

#错误输入重定向和程序终止
import  sys
sys.stderr.write('属性错误，请重新定向。\n')

#字符串正则匹配
import re
re.findall(r'\bf[a-z]*','which foot or hand fell fastest')
re.sub(r'(\b[a-z]+)\1',r'\1','cat in the the hat')

#数学
import  math
math.cos(math.pi / 4)
math.log(1024,2)

#生成随机数工具
import random
random.choice(['apple','pear','banna'])    #字符串随机
random.sample(range(100),10)        #随机列表
random.random()    #随机浮点数
random.randrange(6) #随机整数

#访问互联网
'''from urllib.request import urlopen
for line in urlopen("https://translate.google.cn/#en/zh-CN/request"):
   line = line.decde('utf-8')
   if 'EST' in line or 'EDT' in line:
    print(line)

import smtplib
server = smtplib.SMTP('locatlhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',)
server.quit()

from datetime import date
now = date.today()
now.strftime('%m-%d-%y.%d %b %Y is a %A on the %d day of %B')

birthday = date(1964,7,31)
age = now - birthday
'''
#数据压缩
import zlib
s = b'witch which has which witches wrist watc'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)
zlib.crc32(s)

#性能度量
'''from timeie import Timer
Timer('t=a;a=b;b=t','a=1;b=2').timeit()
Timer('a,b = b,a','a=1;b=2')
'''

def average(values):
    '''强化模块内嵌入测试'''
    return sum(values) / len(values)
import  doctest
doctest.testmod()   #自动验证嵌入测试

import unittest
class TestStatisticalFunctions(unittest.TestCase):
    def test_acerage(self):
        self.assertEqual(average([20,30,70]),40.0)
        self.assertEqual(round(average([1,5,7]),1),4.3)
        self.assertRaises(ZeroDivisionError,average,[])
        self.assertRaises(TypeError,average,20,30,70)
unittest.main()

import  urllib
from urllib.request import urlopen
from urllib.parse import urlencode
