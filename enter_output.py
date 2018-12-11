# _*_ coding:utf-8 _*_
#! /usr/bin/python3
for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end="")
    print(repr(x*x*x).rjust(4))

for x in range(1,11):
    print('{0:2d}{1:3d}{2:4d}'.format(x,x*x,x*x*x))

print('{}网址：''{}!'.format('百度',''))
print('{0}和{1}'.format("Google",'baidu'))

import math
print('常量PI的直近似为：{}。'.format(math.pi))
print('常量PI的值近似为：{0:2f}'.format(math.pi))
print('常量PI的值近似为：%5.3f.'%math.pi)

#键盘输入
str = input('请输入：')
print('你输入的内容：',str)

#读写文件
f = open('D://aws//test.txt','w')
f.write('python是一个非常好用的语言。\n是的,的确非常好！！！\n')

c = open('D://aws//test.txt','r')
ter = c.read()
print(ter)
c.close()

c = open('D://aws//test.txt','r')
ter = c.readline()      #单独的一行
print(ter)
c.close()

c = open('D://aws//test.txt','r')
ter = c.readlines()    #最后一行
print(ter)
c.close()

c = open('D://aws//test.txt','r')
for iu in c:
    print(iu,end="")
c.close()

c = open('D://aws//test.txt','w')
num = c.write("穷在闹市无人问，富在深山有远亲")
print(num)
c.close()

#c.tell()   返回文件对象当前所处的位置，文件开头算起的字节数

#e = open('D://aws//te.txt','rb+')
#f.write(b'da255f45s4s4f6fs4')
#f.seek(5)

import pprint,pickle
pkl_file = open('D://aws//test.txt','rb')
data1 = pickle.load((test.txt))
pprint.pprint(data1)
data2 = pickle.load(test.txt)
pprint.pprint(data2)
pkl_file.close()

#语法说明
'''整数的输出
print('%o'% 20) #八进制24
print('%d'% 20) #十进制20
print('%x'% 24) #十六进制18
'''

'''浮点数输出
print('%f'% 1.11) #默认保留6位小数
print('%.1f'% 1.11) #默认保留1位小数
print('%e'% 1.11) #默认保留6位小数
print('%.3e' % 1.11) #默认保留3位小数
print('%g' % 11111.1121) #默认6个有效数字
print('%.7g' % 1.11112212) #默认7位有效数字
'''

'''字符串输出'''
print('%s' % 'hello world') #字符串输出hell world
print('%20s' % 'asdsaddasdasdsadsadsadasdada' ) #右对齐，取20位，不够则补位
print('%-20s' % 'sdjsjdjdjsjdjkdkkskdskksdsd')  #左对齐，取20位，不够则补位
print('%.2s' % 'hello')   #取2位he
print('%10.2s' % 'hello world') #右对齐，10位取2位he
print('%-10.2s' % 'hello world') #左对齐，10位取2为he
