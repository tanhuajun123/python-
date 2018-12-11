# _*_ coding:utf-8 _*_
#! /usr/bin/python3
var = 100
if var:
    print ("1 - 条件语句的表达式 True")
    print(var)
var1 = 5
if var1 :
    print("2 - 条件语句的表达式 True")
    print(var1)
print("Good bye")

age = int(input("请输入你的年龄："  ))
print("")
if age > 40:
    print("应该叫你大婶还是大妈？")
elif age == 18:
    print("美女加个微信呗！")
elif age < 18:
    print("小孩子一个，赶紧回家找你妈。")

print("不好玩了，吃饭了！")
input("你可以点击enter退出了。")

'''继续我们的猜数字游戏'''
number = 7
guess = 5
print("数字猜谜游戏！")
while guess != number:
    guess = int(input("请输入你的数字：") )

    if  guess == number:
        print("你是看到了底迷了吗？")
        print("游戏结束，你可以去另奖品了")
    if  guess < number:
        print("你猜的太大了！")
    if guess > number :
        print("你猜的太小了！")
print("继续继续")

'''整除数字的游戏'''
num = int(input("输入一个数字："))
if num%2 ==0:
    if num%3==0:
        print("你输入的值可以整除2和3")
    else:
        print("你输入的值可以整除2，但是不能整除3")
else:
    if num%3==0:
        print("你输入的值可以整除3，但是不能整除2")
    else:
        print("你输入的值不可以整除2和3！")

'''随机数字'''
import random
x = random.choice(range(100))
y = random.choice(range(200))

if x > y :
    print('x:',x)
elif x == y :
    print("'x+y:",x+y )
else:
    print('y:', y)

'''加入判断'''
print("优化版的年龄比对")
conner = "n"
while conner =="n":
    try:
        age = int(input("请输入你的年龄："))
        #print("")
        age = float(age)
        if age < 0:
            print("你断奶了吗？")
        elif age == 1:
            print("终于长大了一岁了！")
            break
        elif age == 2:
            print("又长大了一岁！")
            break
        else:
            huana = 18 + (age - 2 )*5
            print("相当于狗的年龄：",huana)
           break
    except ValueError:
        print("输入不合法，请输入有效年龄！")
    print("")
    conter = input("退出(Y/N）？")
    print("")
    input("")

print("欢迎使用BIM计算程序")
name = input("请输入你的名字：")
height = eval(input("请输入你的身高："))
weight = eval(input("请输入你的体重："))
gende = input("请输入你的性别(f/m)：")
BIM = float(float(weight))/(float(height)**2)
#公式
if BIM <= 18.4:
    print('姓名：',name,'身体状态偏瘦')
elif BIM <= 23.9:
    print("姓名：",name,'身体状态正常')
elif BIM <= 27.9:
    print("姓名：",name,'身体状态超重')
elif BIM <= 28:
    print("姓名：",name,'身体状态肥胖')
import  time
nowtime = (time.asctime(time.localtime(time.time())))
if gende == "f":
    print("感谢",name,'先生',nowtime,'使用本程序，祝你身体健康！')
if gende == "m":
    print("感谢",name,'女士',nowtime,"使用本程序，祝你身体健康！")