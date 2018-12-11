# _*_ coding:utf-8 _*_
#! /usr/bin/python3
def hello():
    print("hello world")

def area(width,height):
    return  width * height
def print_welcome(name):
    print("welcome",name)
print_welcome("Runoob")
w = 4
h = 5
print('width=', w , 'height = ',h, "area = ",area(w,h))

def printme(str):
    print(str)
    return

printme("我要调用用户自定义函数！")
printme("再次调用同一函数")

def changint(a):
    a= 10
b= 5
changint(b)
print(b)

#可写函数说明；
def changeme(mylist):
    mylist.append([1,2,3,4,5])
    print('函数内取值：',mylist)
    return
#调用函数
mylist = [10,20,30]
changeme(mylist)
print('函数外取值：',mylist)

def printinfo (name,age):
    print('年龄：',age)
    print('名字：',name)
    return
printinfo(age=50,name='jack')

def printinfo (arg1, *vartuple):
    print('输出：')
    print(arg1)
    print(vartuple)

printinfo(70,60,50)

def printinfo(arg2,*vartuple):
    print('输出：')
    print(arg2)
    for var in vartuple:
        print(var)
        return

#调用printinfo函数
printinfo(10)
printinfo(70,60,50)

def pringtinfo(arg3,**vardict):
    print('输出')
    print(arg3)
    print(vardict)

printinfo(1, 'a = 2, b =3')

sum = lambda  arg1,arg2:arg1 + arg2

print('相加后的值为：',sum(10,20))
print('相加后的值为：',sum(20,220))

def sum(arg1,arg2):
    total = arg1 + arg2
    print('函数内：', total)
    return  total
total = sum(10,200)
print('函数外：',total)

# L 局部作用域
# E 闭包函数外的函数中
# G 全局作用域
# B 内建作用域

x = int(2.9)    #内建作用域
g_count = 0 #全局作用域
def outer():
    o_count = 1 #闭包函数外的函数中
def inner():
    i_count = 2 #局部作用域

total = 0
def suma(arg1,arg2):
    total = arg1 + arg2
    print('函数内是局部变量：',total)
    return total

sum(10,30)
print('函数外是局部变量：',total)


#内部作用域改成外部作用域
num = 1
def fun1():
    global num
    print(num)
    num = 36
    print(num)
fun1()
print(num)

#修改成嵌套作用域
def outer():
    num = 10
    def inner():
        nonlocal  num
        num = 123
        print(num)
    inner()
    print(num)
outer()

a = 10
def test(a):
    a = a+1
    print(a)
test(a)