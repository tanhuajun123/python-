# _*_ coding:utf-8 _*_
#! /usr/bin/python3
import time; #引入time模块
ticks = time.time()
print('当前时间擢为：',ticks)


#获取当前时间
import time
localtime = time.localtime(time.time())
print('本地时间为：',localtime)

#获取格式化时间
import time
localtime = time.asctime(time.localtime(time.time()))
print("本地时间为：",localtime)

#格式化日期
import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
print(time.strftime('%a %b %d %H:%M:%S %Y',time.localtime()))
#格式化字符串转换为时间擢
a = 'Sat Mar 28 22:24:24 2016'
print(time.mktime(time.strptime(a,'%a %b %d %H:%M:%S %Y')))

#获取某年月日历
import calendar
cal = calendar.month(2018,10)
print('以下输入2018年10月份的日历：')
print(cal)
