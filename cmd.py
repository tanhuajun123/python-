import os
mystr=os.popen("tasklist")  #popen与system可以执行指令,popen可以接受返回对象
mystr=mystr.read() #读取输出
print("hello",mystr)
if mystr.find("QQ.exe") !=1:
    print("发现QQ")
else:
    print("QQ已死有事请烧纸")

mystr = os.popen('ipconfig').read()
print(mystr)

mystr = os.popen('ping 192.168.10.1 ')
mystr = mystr.read()
print(mystr)


