# _*_ coding:utf-8 _*_
#! /usr/bin/python3
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1到%d: %d"% (n,sum))    #%d转换格式,转换为指定格式，%d转换为设定的是循环次数

var = 1
while var == 1:
    num = int(input("请输入你认为正确的数字："))
    print("你输入的数字是：", num)
    if num == var:
        print("你输入正确。")
    break
print("Good bye")

con = 0
while con < 5:
    print(con, "小于 5 ")
    con += 1
else:
    print(con, "大于或等于5")

flash = 0
while (flash): print ("欢迎使用python!")
print("welcome")

i = ['1','2','3','4']
for x in i :
    print(x)

site = ['baidu', 'google','tianmao']
for siet in site:
    if siet == 'google':
        print("这么快答对了！")
        break
    print("继续循环" + siet)
else:
    print("没有找到你想要的！")
print('完成循环！')

for i in range(10,15):
    print(i)

for i in 'english':
    if i == 'l':
        break       #执行到此条件终止语句
    print('当前字母：', i)

for lj in 'english':
    if lj ==  's':
        continue    #跳过条件，运行下一语句
    print('当前数字为：', lj)

for lh in 'china':
    if lh == 'n':
        pass
        print('执行pass块')
    print('当前字母为：',lh)
print('退出')

i = 1
while i <= 9:
    j = 1
    while j <= 1:
        m = j*i
        print('%d*%d = %d'%(j,i,m),end = "")
        j+=1
    print("")
    i+=1

for i in range(9,0,-1):
 for j in range(1,i):
        print("\t",end="")
 for k in range(i,10):
     print('%d*%d=%d'%(i,k,k*i),end="\t")
     print()
