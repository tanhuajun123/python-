#!_*_ coding:utf-8 _*_
#!/usr/bin/python
import time
file = open('D:\\aws\\SN.txt', 'w+')
file.write("www.baidu.com！\n666666666\n")
file.close()
file = open("D:\\aws\\SN.txt", "r+")
str = file.read(5)
print"数字：", str


fo = open("foo.txt", "w")
fo.write("www.runoob.com!\nVery good site!\n")
# 关闭打开的文件
fo.close()
fo = open("foo.txt", "r+")
str = fo.read(10)
print "读取的字符串是 : ", str
# 关闭打开的文件
fo.close()


root = open("D:\\aws\\123.txt", "w+")
for i in range(1, 5):
   print(i)

localt = time.asctime()
print "本地时间为 :", localt
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())