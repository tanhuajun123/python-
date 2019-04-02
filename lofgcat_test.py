#!/user/bin/python3
#_*_coding:utf-8 _*_
import os, sys
import constant
import re
import subprocess
import time

def pull_file(file_name):
    """Push a file to device.
    Args:
        file_name: the name of the file pull.
        下载log 到脚本所在目录下
        下载完log立即删除log
    """
    cur_dir = os.getcwd()
    command_pull = 'adb pull /oem/duer/' + file_name + ' {0}'.format(cur_dir)
    print
    command_pull
    os.system(command_pull)
    time.sleep(3)


def del_file(file_name):
    command_rm = 'adb shell rm -rf /oem/duer/' + file_name
    print
    command_rm
    time.sleep(2)
    os.system(command_rm)


def get_filename():
    """
    adb shell ls /oem/duer/
    查看/oem/duer/目录下是否有需要导出的log
    :return:
    """
    cur_dir = os.getcwd()  # 获取脚本所在目录
    com_ls = 'adb shell ls /oem/duer/ > {0}/filename.txt'.format(cur_dir)
    os.system(com_ls)
    with open('filename.txt', 'rw') as fr:
        filename = fr.read().strip().split()
        return filename


def main():
    duer_link = 'duer_link.log'
    dcssdk = 'dcssdk.log'
    linklog_bak = 'duer_link.log-bak.log'
    dcssdklog_bak = 'dcssdk.log-bak.log'
    filename = get_filename()
    print
    filename
    if 'dcssdk.log' in filename:
        pull_file(dcssdk)
        del_file(dcssdk)
    else:
        print
        'no dcssdk.log '

    if 'dcssdk.log-bak.log' in filename:
        pull_file(dcssdklog_bak)
        del_file(dcssdklog_bak)
    else:
        print
        'no dcssdk.log-bak.log'

    if 'duer_link.log' in filename:
        pull_file(duer_link)
        del_file(duer_link)
    else:
        print
        'no duer_link.log'

    if 'duer_link.log-bak.log' in filename:
        pull_file(linklog_bak)
        del_file(linklog_bak)
    else:
        print
        'no duer_link.log-bak.log'

    cur_dir = os.getcwd()
    time.sleep(2)
    os.remove(cur_dir + os.sep + 'filename.txt')


def findDevice():
    '''
    检查设备
    :return:
    '''
    deviceRegex = re.compile(r'\w*1234\w*')
    try:
        out = subprocess.check_output("adb devices", shell=True)
        #print(type(out))
        if deviceRegex.search("out") == None:
            print("设备 adb 连接失败 T.T ..请检查设备连接")
            return False
    except subprocess.CalledProcessError as e:
        if e.returncode == 127:
            print("adb 命令获取失败， 请检查adb是否安装成功")
            return False
    return True

if __name__ == '__main__':
        if findDevice():
            main()
        else:
            print("Please check the device connection  ")
