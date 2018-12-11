# _*_ coding:utf-8 _*_
#! /usr/bin/python3
#服务器
#文件名：server.py
#导入 socket / sys 模块
import socket
import sys

#创建socket对象
seversocket = socket.socket(
    socket.AF_INET,socket.SOCK_STREAM)

#获取本地主机名
host= socket.gethostname()

port = 9999

#绑定端口号
serversocket.bind((host,port))

#设置最大的连接数，超过后排队
serversocket.listen(5)

while True:
    #建立客户连接
    clientsocket,addr = seversocket.accept()
    print('连接地址：%s' % str(addr))
    msg='欢迎访问菜鸟教程' + '\r\n'
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()

#客户端
#文件名：client.py
#导入socket/sys模块
#import socket
import  sys
#创建socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取本地主机名
host = socket.gethostname()

#设置端口号
port = 9999

#连接服务，指定主机和端口
s.connect((host,port))

#接收小于1024字节的数据
msg = s.recv(1024)
s.close()
print(msg.decode('utf-8'))

