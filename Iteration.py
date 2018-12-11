# _*_ coding:utf-8 _*_
#! /usr/bin/python3
import  sys
list = [1,2,3,4,]
it = iter(list)  #创建迭代对象
for x in it :
    print(x, end="")

lis = [1,2,3,4,5]
iv = iter(lis)
while True:
    try:
        print(next(iv))
    except StopIteration:
        sys.exit()
import sys
def filbonacci(n):      #生成器函数
    a,b,counter = 0,1,0
    while True:
        if (counter > n):
            return
        yield a
        a,b = b , a + b
        counter += 1
f = filbonacci(10)
while True:
    try:
        print(next(f), end="")
    except StopIteration:
        sys.exit()