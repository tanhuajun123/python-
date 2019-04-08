#!/user/bin/python3
#_*_coding:utf-8 _*_
import os
import time

import os
import time

class App():

    def __init__(self,count):
        self.count = count
    def device(self):
        device = "adb devices "
        src_outer = os.popen(device).read().strip()
        if not src_outer:
            print('cmd没有提示消息 ' + device)
            sys.exit(0)
        touch_info = 'List of devices attached'
        lists = src_outer[src_outer.index(touch_info) + len(touch_info):]

        if not lists:
            print("没有设备连接电脑，请检查连接 ! ")
            sys.exit(0)

    # 开启wifi的方法
    def openWifi(self):
        cmd = 'adb shell svc wifi enable'
        os.popen(cmd)
        time.sleep(10)

    def scan(self):
        cmd = "adb shell ping 127.0.0.1"
        os.popen(cmd)
        time.sleep(1)


    # 关闭wifi的方法
    def closeWifi(self):
        cmd = 'adb shell svc wifi disable'
        time.sleep(10)

    #控制wifi循环的方法
    def controlWifi(self):
        i = 1
        while (self.count >0):
            print("第 %d 次执行开关Wi-Fi操作" % i)
            self.device()
            self.closeWifi()
            self.scan()
            self.openWifi()
            i = i +1
            self.count = self.count - 1


if __name__ == '__main__':
    #控制Wi-Fi开关执行100次
    app = App(10)
    app.controlWifi()
