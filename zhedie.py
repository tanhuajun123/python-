#!_*_ coding:utf-8 _*_
#!/usr/bin/evn py
import os
import time
def nsfile(s):
    #判断文件夹是否存在，如果不存在则创建；
    b = os.path.exists("E:\\testfile\\")
    if b:
        print("flie exist")
    else:
        os.mkdir("E;\\testfile")
        #生成文件夹
        for i in range(1, s+1):
            localsTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
            filename = "E:\\testFile\\"+localsTime+".txt"
            f = open(filename, 'ab')
            testnote = '测试文件'
            f.write(testnote)
            f.close()
            #输入第几个文件名和对应的文件名称
            print("file"+" "+str(i)+":"+str(localsTime)+".txt")
            time.sleep(1)
            print"ALL Down"
            time.sleep(1)

            if __name__ == '__main__':
                s = input("请输入文件夹的数量：")
                nsfile(s)
