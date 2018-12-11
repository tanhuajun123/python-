# _*_ coding:utf-8 _*_
#! /usr/bin/python3
class MyClass:
    '''一个简单的类实例'''
    i = 123456
    def f(self):
        return 'hello world'
#实例化类
x = MyClass()
#访问类的属性和方法
print('Myclass 类的属性 i为：', x.i)
print('Myclass 类的属性f 输出为：', x.f())

#类的初始状态,让类属性初始化的方法
def __init__(self):
    self.data = []

#参数实例化
class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0,-4.5)
print(x.r,x.i)  #结果输出

class Test:
    def per(self):
        print(self)
        print(self.__class__)
t = Test()
t.per()

#self代表的是类的实例，代表当前对象的地址，而self.class则指向类
#self不是python关键字，我们换成runoob也是可以正常执行的

class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)
t = Test()
t.prt()

#实例
class people:
    name = 'jack'
    age = 0
    __werght__ = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__werght__ = w
    def speak(self):
        print('%s 说：我 %d 岁。' % (self.name,self.age))
#实例化类
p = people('runoob',15,18)
p.speak()


#程序的调用和继承
class people:
    # name = ''
    # age = 0
    # __went__ = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.w = w
    def speak(self):
        print("%s 说：我 %d 岁。" % (self.name,self.age))
 #继承实例
class studle(people):
     grade = ''
     def __init__(self,n,a,w,g):
         super(studle,self).__init__(n,a,w)
         self.grade = g
         #复写父类的方法
     def speak(self):
        print('%s 说：我 %d 岁。我在读 %d 年级了；' % (self.name, self.age,self.grade ))
class speker():
    top = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.top = t
    def speak(self):
        print('我叫 %s，我是一个演说家，我演讲的主题是 %s ,'% (self.name,self.top))

class studie(speker,studle):
    a = ""
    def __init__(self,n,a,w,g,t):
        studle.__init__(self,n,a,w,g)
        speker.__init__(self,n,a)

test = studie('jack',15,25,4,'python')
test.speak()

class Parent:
    def myMethod(self):
        print('调用父类方法')

class Chid(Parent):
    def myMethod(self):
        print('调用子类方法')

c = Chid()
c.myMethod()  #子类调用重写
super(Chid,c).myMethod()  #用子类对象调用父类已被覆盖的方法

class JuntCounter:
    __secreCount = 0
    publicCount = 0
    def count(self):
        self.__secreCount += 1    #私有变量
        self.publicCount += 1     #公开变量
        print(self.__secreCount)

counter = JuntCounter()
counter.count()
counter.count()
print(counter.publicCount)
#print(counter.__secreCount)

class Site:
    def __init__(self,name,url):
        self.name = name
        self.__url = url

    def who(self):
        print('name:',self.name)
        print('url:',self.__url)
    def __foo(self):              #私有方法
        print('这个私有的方法')

    def foo(self):              #这个是公共的方法
        print('这个是公共方法')
        self.__foo()
x = Site('态度学科','wwww.badu.com')
x.who()
x.foo()
#x.__foo()    #调用私有方法会报错

'''类的专有方法
__init__:构造函数，在生成对象时调用
__del__:析构函数，释放对象时使用
__repr__:打印，转换
__setitem__:按照索引赋值
__getitem__:按照索引获取值
__len__:获取长度
__cmp__:比较运算
__call__:函数调用
__add__:加运算
__sub__;减运算
__mul__;成运算
__div__;除运算
__mod__;求余运算
__pow__;乘方'''

class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector(%d,%d)' % (self.a,self.b)
    def __add__(self, other):
        return Vector(self.a + other.a,self.b + other.b)

v1 = Vector(2,8)
V2 = Vector(55,48)
print(v1 +V2)
