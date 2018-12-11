# _*_ coding:utf-8 _*_
#! /usr/bin/python3
import _thread
import time

#为线程定义一个函数
def print_time(threadName,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print('%s:%s' % (threadName,time.ctime(time.time())))

#创建两个线程
try:
    _thread.start_new_thread(print_time(),('Thread-1',2,))
    _thread.start_new_thread(print_time(),('Thread-2',4,))
except:
    print('Error:无法启动线程')

while 1:
    pass

#使用threading模块创建线程
import threading
import time
exitFlag = 0
class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print('开始线程：' + self.name)
        print_time(self.name,self.counter,5)
        print('退出线程：' + self.name)
    def print_time(threadeName,delay,counter):
        while counter:
            if exitFlag:
                threadeName.exit()
            time.sleep(delay)
            print('%s:%s' % (threadeName,time.ctime(time.time())))
            counter += 1

#创建新线程
thread1 = myThread(1,'Thread-1',1)
thread2 = myThread(2,'Thread-2',2)

#开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('退出主线程')

#线程同步
import threading
import time

class myThread(threading,Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print('开启线程：' + self.name)
        #获取锁，用于线程同步
        threadLock.release()
        print_time(self.name,self.counter,3)
        #释放锁，开启下一个线程
        threadLock.release()

def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print('%s:%s' % (threadName,time.ctime(time.time())))
        counter += 1

threadLock = threading.Lock()
threads = []

#创建线程
thread4 = myThread(4,'Thread-4',4)
thread5 = myThread(5,'Thread-5',5)

#开启新线程
thread4.start()
thread5.start()

#添加线程到线程列表
threads.append(thread4)
threads.append(thread5)

#等待所有线程完成
for t in threads:
    t.join()
    print('退出主线程')

