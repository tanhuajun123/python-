# _*_ coding:utf-8 _*_
#! /usr/bin/python3
'''
import  os
os.access(path=,mode=)  检验权限模式
os.chdir(path=) 改变当前工作目录
os.chflags(path=,flags=) 设置路径的标记为数字标记
os.chmod(path=,mode=) 更改权限
os.chown(path=,uid=,gid=) 更改文件所有者
os.chroot(path=) 改变当前进程的根目录
os.close(fd=) 关闭文件描述符FD
os.closerange(fd_low,fd_high) 关闭所以文件描述符,从fd_Low（包含）到fd_high(不包含),错误会忽略
os.dup(fd=) 复制文件描述符fd
os.dup2(fd2=,fd2=)  将一个文件描述符fd复制到另一个fd2
os.fchdir(fd=) 通过文件描述符改变当前工作目录
os.fchmod(fd=,mode=) 改变一个文件的访问的权限,该文件有参数fd 指定,参数mode是unix下的文件访问权限
os.fchown(fd=,uid=,gid=) 修改一个文件的所有权,这个函数修改一个文件的用户ID和用户组ID,该文件由文件描述符fd指定
os.fdatasync(fd=) 强制将文件写入磁盘,该文件由文件描述符fd指定，但是不强制更新文件的状态信息
os.fdopen(fd=[,mode[,bufsize]]) 通过文件描述符fd创建一个文件对象，并返回这个文件对象
os.fpathconf(fd=,name=) 返回一个打开的文件系统配置信息，name为检索的系统配置的值，它也许是一个定义系统值的字符串
os.fstat(fd=) 返回文件描述符fd的状态，像stat（）
os.fstatvfs(fd=) 返回包含文件描述符fd的文件的文件系统的信息
os.fsync(fd=) 强制将文件描述符为fd的文件写入硬盘
os.ftruncate(fd=,length=) 裁剪文件描述符fd对应的文件,所以它最大不能超过文件大小
os.getcwd() 返回当前工作目录
os.getcwdu() 返回一个当前工作目录的Unicode对象
os.isatty(fd=) 如果文件描述符fd是打开的,同时与tty（-like）设备相连,则返回True或False
os.lchflags(path=,flags=)  设置路径的标记委书记标记，类似chflage（）,但是没有软链接
os.lchmod(path=,mode=) 修改连接文件权限
os.lchown() 更改文件的所有者，类似chown,但是不追踪链接
os.link(src,dst) 创建硬链接，名为参数dst，指向参数src
os.listdir(path=) 返回path指定的文件夹的文件或文件夹的名字的列表
os.lseek(fd=,pos=,how=) 设置文件描述符fd当前位置pass,how方式修改：seek_set或者设置从文件开始的计算的pos;
os.lstat(path=)  像stat（）但是没有软链接
os.major(device=) 从原始的设备号中提取设备major号码
os.makedev(major=,minor=) 以major和minor设备号组成一个原始设备号
os.makedirs(path=[,mode])  递归文件夹创建函数，像mkdir()但是创建的所以intermediate-level文件夹需要包含子文件夹
os.minor(device=) 从原始的设备号中提取设备minor号码
os.mkdir(path=[,mode]) 以数字mode 的mode创建一个名为path的文件夹，默认的mode是0777八进制
os.mknod(filename=[,mode=0600,device])  创建一个名为filename文件系统节点
os.open(file=,flags=,[mede]) 打开一个文件，并且设置需要的打开选项，mode参数是可选的
os.openpty() 打开一个新的伪终端对，返回pty和tty文件描述符
os.pathconf(path=,name=) 返回相关文件的系统配置信息
os.pipe() 创建一个管道，返回一对文件描述符(f，w)分别为读和写
os.popen(command=,[mode],[bufsize])   从一个command 打开一个管道
os.read(fd=,n) 从文件描述符fd中读取最多n个字节，返回包含读取字节的字符串，文件描述符fd对应文件已经到结尾，返回一个空字符串
os.readlink(path=)  返回软链接所指向的文件
os.remove(path=) 删除路径为path的文件，如果path是一个文件夹，将抛出OSError查看下面的rmdir()删除一个directory
os.removedirs(path=) 递归删除目录
os.rename(src=,dst=) 重命题文件或目录，从src到dst
os.rename(old,new) 递归地目录进行更名，也可以对文件进行更名
os.stat(path=) 获取path指定的路径的信息，功能等同于C API中的stat（）系统调用
os.stat_float_times([newvalue]) 决定stat_result是否以float对象显示时间擢
os.statvfs(path=) 获取指定路径的文件系统统计信息
os.symlink(src,dst) 创建一个软链接
os.tcgetpgrp(fd=) 返回与终端fd关联的进程组
os.tcsetpgrp(fd=,pg=) 设置与终端fd关联的进程组为pg
os.tempnam([dir,[prefix]])  返回唯一的路径名用于创建临时文件
os.tmpfile() 返回一个打开的模式为（w+b）的文件对象，这文件对象没有文件入口，没有文件描述符，将会自动删除
os.tmpnam() 为创建一个临时文件返回一个唯一的路径
os.ttyname(fd=) 返回一个字符串，它表示与文件描述符fd关联的终端设备，如果fd 没有和终端设备关联，则引发一个异常
os.unlink(path=) 删除文件路径
os.utime(path=,times=) 返回指定的path文件的访问和修改的时间
os.walk(top=,[topdown=True,[onerror=None,[followlinks=False]]])  输出在文件夹的文件名通过在树中游走，向上或者向下
os.write(fd=,str) 写入字符串到文件描述符fd中，返回实际写入的字符串长度
'''

import  os
def search_file(start_dir,target):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            vedio_list.append(os.getcwd()+ os.sep + each_file + os.linesep)
            if os.path.isdir(each_file):
                search_file(each_file, target)   #递归调用
                os.chdir(os.pardir)        #递归调用后切记返回上一层目录

start_dir = input('请输入待查看的初始目录：')
program_dir = os.getcwd()

targert = ['.mp4','.avi','.rmvb']
vedio_list = []

search_file(start_dir,targert)
f = open(program_dir + os.sep + 'vedioList.txt','w')
f.writelines(vedio_list)
f.close()
