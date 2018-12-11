# _*_ coding:utf-8 _*_
#! /usr/bin/python3
#list.append(x) #把一个元素添加到列表的结尾，
#list.extend(l)#通过添加指定列表的所有元素来扩充列表
#list.insert(i,x)#在指定位置插入一个元素，第一个参数是准备插入到其前面的那个元素的索引
#list.remove(x)#删除列表中值为x的第一个元素，如果没有这样的元素，就会返回一个错误
#list.pop([1])#从列表的指定位置移除元素，并将其返回，如果么有指定索引，a.pop()返回最后一个元素
#list.clear()#移除列表中的所有项，等于dela:{
#list.index()#返回列表中第一个值为X的元素的索引，如果没有匹配的元素就会返回一个错误
#list.count(x)#返回x在列表中出现的次数
#list.sort()#对列表中的元素进行排序
#list.remove()#倒排列表中的元素
#list.copy()#返回列表的浅复制，等于a[;]



a = [66.25, 333, 333, 1, 1234.5]
print(a.count(66.25))
a.insert(1,3)
a.append(536.36)
a.sort()
a.pop(333)
a.remove(1)
a.copy()

