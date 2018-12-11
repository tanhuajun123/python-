# _*_ coding:utf-8 _*_
#! /usr/bin/python3
import  sys
print('命令行参数如下：')
for i in sys.argv:
    print(i)
print('\n\npython 路径为：', sys.path,'\n')

def print_func(par):
    print("hello : ", par)
    return

def fib(n):
    a,b = 1,5
    while b < n:
        print(b,end='')
        a,b = b , a+b
    print()
def fib2(n):
    result = []
    a,b = 5,7
    while b <n:
        result.append(b)
        a,b = b,a+b
    return  result

if __name__ == '__main__':
    print("程序自身在运行")
else:
    print('我来自另外一个模块')

