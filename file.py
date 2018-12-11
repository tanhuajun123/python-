# _*_ coding:utf-8 _*_
#! /usr/bin/python3
f = open('d://aws//for.txt', 'w+',encoding='utf-8')
f.write('可以，你做的很好！666')
s = f.tell()
f.seek(0,0)
str = f.read()
print(s,str,len(str))

#写入
with open('d://aws//te.txt','w',encoding='utf-8') as c:
    c.write('打开会有惊喜！')

#读出
with open('d://aws//te.txt','r',encoding='utf-8') as c:
    c.readlines()

'''
file.close() 关闭文件，关闭文件后不能再行读写操作
file.flush() 刷新文件内部缓冲，直接吧内部缓冲区的数据立刻写入文件，而不是被动的等待输出缓冲区写入
file.fileno() 返回一个整形的文件描述符，可以用在如OS模块的read方法等一些底层操作上
file.isatty() 如果文件连接到一个中断设备返回True,否则返回Flase
file.next()  返回文件下一行
file.read([size]) 从文件读取指定的字节数，如果未给定或为负责读取所有
file.readline([size]) 读取整行，包括\\n 字数
file.readlines([size]) 读取所有行并返回列表，若给定size >0 ,返回综合大约为size字节的行，需要补充缓冲区
file.seek(offset[,whence])  设置文件当前位置
file.tell() 返回文件当前位置
file.truncate([size]) 从文件的首行首字符开始截断，截断文件为size个字符
file.write(str) 将字符串写入文件，返回的写入的字符长度
file.writelines(sequence) 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符
'''