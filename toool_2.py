#!/user/bin/env python
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
from widget import Ui_Widget
#from datetime import datetime
import serial
import serial.tools.list_ports
import sys
from _pyio import *
import tkinter
from PIL import ImageTk,Image


class Main(Ui_Widget,QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('F:\\QT\\tool-2\\fang.png'))
        self.setWindowTitle('第二版串口小工具V0.0.1')
        #串口无效
        self.ser = 0
        self.send_num = 0
        self.lineEdit.setText(str(self.send_num))
        self.receive_num = 0
        self.textEdit.setText(str(self.receive_num))
        # 显示发送与接收的字符数量
        dis = '发送：' + '{:d}'.format(self.send_num) + '  接收:' + '{:d}'.format(self.receive_num)
        self.statusBar().showMessage(dis)
    def init(self):
        self.refresh()
        # 波特率控件
        self.comboBox_2.addItem('115200')
        self.comboBox_2.addItem('57600')
        self.comboBox_2.addItem('56000')
        self.comboBox_2.addItem('38400')
        self.comboBox_2.addItem('19200')
        self.comboBox_2.addItem('14400')
        self.comboBox_2.addItem('9600')
        self.comboBox_2.addItem('4800')
        self.comboBox_2.addItem('2400')
        self.comboBox_2.addItem('1200')
         # 数据位控件
        self.comboBox_3.addItem('8')
        self.comboBox_3.addItem('7')
        self.comboBox_3.addItem('6')
        self.comboBox_3.addItem('5')
         # 停止位控件
        self.comboBox_4.addItem('1')
        self.comboBox_4.addItem('1.5')
        self.comboBox_4.addItem('2')
         # 校验位控件
        self.comboBox_5.addItem('NONE')
        self.comboBox_5.addItem('ODD')
        self.comboBox_5.addItem('EVEN')
        #对testEdit进行事件过滤
        self.textEdit.installEventFilter(self)
        #实例化一个定时器
        self.timer = QTimer(self)
        self.timer_send = QTimer(self)
        #定时发送
        self.timer_send.timeout().connect(self.send)
        #定时器调用读取串口接收数
        self.timer.timeout().connect(self.recv)
        #发送数据按钮
        self.pushButton.clicked.connect(self.send)
        #打开关闭串口按钮
        self.pushButton_2.clicked.connect(self.open_close)
        #刷新串口外设按钮
        self.pushButton_4.clicked.connect(self.refresh)
        #清除窗口
        self.pushButton_3.clicked.connect(self.clear)
        #定时发送
        self.checkBox_4.clicked.connect(self.send_timer_box)

        #刷新一下串口
    def refresh(self):
        #查询可用的串口
        plist = list(serial.tools.list_ports.comports())
        if len(plist) <= 0:
            print("没有扫描到客户端口连接")
        else:
            plist_0 = list(plist[0])
            serialName = plist_0[0]
            serialFd = serial.Serial(serialName,115200,timeout=0.5)
            print('可用端口名称》》'),serialFd.name

    def eventFilter(self, Obj,event):
        if  event.type() == event.KeyPress:
            if self.ser != None:
                char = event.text()
                num = self.ser.write(char.encode('utf-8'))
                self.send_num = self.send_num +num
                dis = '发送：' + '{:d}'.format(self.send_num) + '接收：' + '{:d}'.format(self.receive_num)
                self.statusBar().showMessage(dis)
            else:
                pass
            return True
        else:
             return  False

    def closeEvent(self, e):
        self.timer_send.stop()
        self.timer.stop()

        if self.ser != None:
           self.ser.close()
           self.ser  = None
    def send_timer_box(self):
        if self.checkBox_4.checkState():
            time = self.lineEdit_2.text()

            try:
                time_val = int(time,10)
            except ValueError:
                QMessageBox.critical(self,'pycom','请输入有效的定时时间！')
                return  None
            if time_val == 0 :
                QMessageBox.critical(self,'pycom','定时时间必须大于零！')
                return None
            self.timer_send.start(time_val)

        else:
            self.timer_send.stop()

    def clear(self):
        self.textEdit.clear()
        self.send_num = 0
        self.receive_num = 0
        dis = '发送：' + '{:d}'.format(self.send_num) + '接收：' + '{:d}'.format(self.receive_num)
        self.statusBar().showMessage(dis)

     #串口接收数据处理
    def recv(self):
        try:
            num = self.ser.inWaiting()
        except:
            self.timer_send.stop()
            self.timer.stop()

            self.ser.close()
            self.ser = None


            self.pushButton_2.setChecked(False)
            self.pushButton_2.setText('打开串口')
            print('Serial ERROR')
            return None
        if num > 0:
            data = self.ser.reade(num)
            #打印输出数据
            print(data)
            num = len(data)
            #十六进制显示
            if self.checkBox_3.checkState():
                out_s = ""
                for i in range(0,len(data)):
                    out_s = out_s + '{:02X}'.format(data[i]) + ''
                self.textEdit.initPainter(out_s)

            else:
                self.textEdit.initPainter(data.decode('iso-8859-1'))

            self.receive_num = self.receive_num + num
            dis = '发送：' + '{:d}'.format(self.send_num) + '接收：' + '{:d}'.format(self.receive_num)
            self.statusBar().showMessage(dis)

            #获得光标
            textCursor = self.textEdit.textCursor()
            textCursor.movePosition(textCursor.End)
            #设置光标到text中去
            self.textEdit.setTextCursor(textCursor)
        else:
            pass


        #串口发送数据
    def send(self):
        if self.ser != None:
            input_s = self.lineEdit.text()
            if input_s != '':

                 #发送字符
                 if (self.checkBox.checkState() == False):
                     if self.checkBox_2.checkState():
                         #发送新行
                         input_s = input_s + '\r\n'
                         input_s = input_s.encode('utf-8')
                 else:
                     input_s = input_s.strip()  #删除前后的空格
                     send_list = []
                     while input_s  != '':
                        try:
                            num = int(input_s[0:2],16)

                        except ValueError:
                            print('提示HEX数据错误')
                            QMessageBox.critical(self,'pycom','请输入十六进制数据，以空格分开！')
                            return  None
                        input_s = input_s[2:]
                        input_s = input_s.strip()
                        #添加到发送列表中
                        self.send_list.append(num)
                        input_s = bytes(self.send_list)
                     print(input_s)
                     #发送数据
                     try:
                         num = self.lineEdit.ser.write(input_s)
                     except:
                         self.timer_send.stop()
                         self.timer.stop()
                    #串口拔出错误，关闭定时器
                         self.ser.close()
                         self.ser = None


                    #设置为打开状态
                         self.pushButton_2.setChecked(False)
                         self.pushButton_2.setText('打开串口')
                         print('串口输入数据错误')
                         return  None
                     self.send_num = self.send_num + num
                     dis = '发送：' + '{:d}'.format(self.send_num) + '接收：'  + '{:d}'.format(self.receive_num)
                     self.statusBar().showMessage(dis)
                     print('输入数据完成')
            else:
                print('没有数据输入')
        else:
            self.timer_send.stop()
            QMessageBox.critical(self,'pycom','请打开串口')
    def open_close(self,btn_sta):
        if btn_sta == True:
            try:
                input('输入参数 COM 115200')
                print(int(self.comboBox_2.currentText()))
                self.ser = serial.Serial(self.comboBox.currentText(),int(self.comboBox_2.currentText()),timeout = 0.1)
            except:
                QMessageBox.Critical(self,'pycom','没有可用的串口或者当前的串口被占用')
                return  None
            #字符间隔超时设置
            self.ser.interCharTimeout =0.001

            #1ms的测试周期
            self.timer.start(2)
            self.pushButton_2.setText('关闭串口')
            print('打开！')
        else:
            self.timer_send.stop()
            self.timer.stop()
            try:
                #关闭串口
                self.ser.close()
            except:
                QMessageBox.critical(self,'pycom','关闭串口失败')
                return None
            self.ser = None
            self.pushButton_2.setText('打开串口')
            print('关闭')

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  mainWindow = Main()
  mainWindow.show()
  sys.exit(app.exec_())

