#!/user/bin/python3
#_*_coding:utf-8 _*_
#author: THJ

import time
import os, re, subprocess, sys
import threading

"""
重启后检测到设备可以自动抓取log,生成log.txt
"""
type = sys.getfilesystemencoding()


def getLog():
    # os.popen("start /b adb logcat -v time >"+fileNameTime+".txt")
    os.popen("start /b adb logcat -v time >""log.txt")


def closeADB():
    os.system('adb kill-server')


def GetSNnumber():
    device_cmd = 'adb devices'
    out = os.popen(device_cmd)
    info = out.readlines()
    if len(info) == 2:
        print("没有检测到设备".encode(type))
        # print "没有检测到设备"
        time.sleep(10)
        GetSNnumber()
    else:
        getLog()


if __name__ == '__main__':

    while True:
        GetSNnumber()
        try:
            t = threading.Thread(target=GetSNnumber())
            t.start()
            t.join()
        # time.sleep(10)
        except KeyboardInterrupt as e:
            i = False
            sys.exit()
