#!/user/bin/python3
#_*_coding:utf-8 _*_
import os
import time
class APP():
    def __init__(self,count):
        self.count = count

        #开启wifi的方法
        def openwifi(self):
            cmd = "adb shell svc wifi enable"
            os.popen(cmd)
            time.sleep(60)

        #关闭wifi的方法
        def closewifi(self):
            cmd = "adb shell svc wifi disable"
            time.sleep(5)
        #控制wifi循环的方法
        def controlwifi(self):
            i = 1
            while (self,count > 0 ):
                print("第 %d 次执行开关WiFi 操作" % i)
                self.closewifi()
                self.closewifi()
                i = i + 1
                slef.count = self.count - 1

if __name__ == "__main__":
    #控制开关次数
    app = APP()
    app.controlwifi()
