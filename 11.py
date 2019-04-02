#!/user/bin/python3
#_*_coding:utf-8 _*_


import random
from random import choice

h = set()
while (len(h)<5):
    h.add(random.randint(1,11))
print(h)


hao = eval(input('请输入需要几组数据：'))

def zhongdajiang():


    a = range(1,12)
    b = random.sample1(a,5)
    print('中奖号码为：',b)
    print('')
n=1
while True:
    zhongdajiang()
    n += 1
    if n > hao:
        break























'''list_red = [x for x in range(1,34)]
res = random.sample(list_red,6)
res.sort()
res.append(random.randint(1,16))
print(res)'''




'''zhongjiang = eval(input("请输入需要几组号码："))
print("")


def shenxianhao():
    a = range(1,35)
    b = random.sample(a,6)
    c = range(1,7)
    d = random.sample(c,1)
    print("红球：",b,"蓝球：",d)
    print("")

n=1
while True:
    shenxianhao()
    n += 1
    if n > zhongjiang:
        break'''

