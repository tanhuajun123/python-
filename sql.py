#!/usr/bin/python
# _*_ coding:utf-8 _*_
import os
class Employes:
    '所以员工的基类'
    empCont = 0
    def __int__(self, name, salary):
        self.name = name
        self.salary = salary
        Employes.empCont += 1

    def displayCont(self):
        print"Total Enployes %d" % Employes.empCont
    def displayCont(self):
        print"name:", self.name, "salary:", self.salary

"创建 Employee 类的第一个对象"
#emp1 = Employes("Zara", 2000)
"创建 Employee 类的第二个对象"
#emp2 = Employes("Manni", 5000)
#emp1.displayEmployee()
#emp2.displayEmployee()
#print "Total Employee %d" % Employes.empCount

class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()

import  datetime
i = datetime.datetime.now()
print("当前的日期和时间: %s" % i)