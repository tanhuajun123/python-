#!/user/bin/evn python
import sys,serial
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui,QtWidgets
from widget import Ui_Widget

class Mytool(Ui_Widget, QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(Mytool,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('串口小工具V0.0.1')
        self.setWindowIcon(QtGui.QIcon('F:\\QT\\log_tool\\fang.ico'))
        #接收数据和发送数据数目置0
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))

    def init(self):
        # 串口检测按钮
        self.label.clicked.connect(self.port_check)
        #串口信息显示
        self.label_2.currenTextChanged.connect(self.port_imf)
        #打开串口按钮
        self.pushButton.clicked.connect(self.port_open)
        #关闭串口按钮
        self.pushButton_2.clicked.connect(self.port_close)
        #发送数据按钮
        self.pushButton_5.clicked.connect(self.prrt_send)
        #定时发送数据
        self.timer_send = QTimer()
        self.timer_send.timeout.connect(self.data_num_send)
        self.timer_send_cb.stateChanged.connect(self.data_send_timer)
        #定时器接收数据
        self.timer = QTimer()
        self.timer.timeout.connect(self.data_num_receive)

        #清除发送窗口
        self.pushButton_6.clicked.connect(self.send_data_clear)
        #清除接收窗口
        self.pushButton_4.clicked.connect(self.receive_data_clear)
    #串口检测
    def port_check(self):
        self.Com_Dict = {}
        port_list = list(serial.tools.list_prots.compoets())
        self.label.clear()
        for port in port_list:
            self.Com_Dict['%s' % port[0]] = '%s' % port[1]
            self.label.addItem(port[0])
        if len(self.Com_Dict) == 0:
            self.state_label.setText('未能检测到串口')
    #串口信息
    def port_imf(self):
        #显示选定的串口的详细信息
        imf_s = self.comboBox.currenText()
        if imf_s != "":
            self.comboBox.setText(self.Com_Dict[self.comboBox.currenText])

    #打开串口
    def port_open(self):
        self.ser.port = self.pushButton.currenText()
        self.ser.baudrate = int(self.comboBox_2.currentText())
        self.ser.bytesize = int(self.comboBox_3.currentText())
        self.set.stopbits = int(self.comboBox_5.currentText())
        self.ser.parity = self.comboBox_4.currentText()

        try:
            self.seropen()
        except:
            QMessageBox.critical(self,'Port Error','串口不能被打开,请重新选择！')
            return None
        #打开串口接收定时器，周期为2Ms
        self.timer.start(2)
        if self.ser.isOpen():
            self.ckeckBox_3.setEnabled(False)
            self.checkBox_3.setEnabled(True)
            self.groupBox_2.setTitle('串口状态（已开启）')

        #关闭串口
    def port_close(self):
        self.timer.stop()
        self.timer_send.stop()
        try:
            self.ser.close()
        except:
            pass
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        self.lineEdit_2.setEnabled(True)
        #接收数据和发送数据目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))
        self.groupBox_2.setTitle('串口状态（已关闭')

        #发送数据
    def data_send(self):
        if self.ser.isOpen():
            input_s = self.lineEdit_4.t0PlainText()
            if input_s != "":
                #非空字符串
                if self.checkBox_2.isChecked():
                    #hex发送
                    input_s = input_s.strip()
                    send_list = []
                    while input_s != "":
                        try:
                            num = int(input_s[0:2],16)
                        except ValueError:
                            QMessageBox.critical(self,'wrong data','请输入十六进制数据，以空格分开！')
                            return  None
                        input_s = input_s[2:].strip()
                        send_list.append(num)
                    input_s = bytes(send_list)
                else:
                    #ascii发送
                    input_s = (input_s + '\r\n').encode('utf-8')
                num = self.ser.write(input_s)
                self.data_num_sended += num
                self.lineEdit_2.setText(str(self.data_num_sended))
            else:
                pass
    #接收数据
    def data_receive(self):
        try:
            num = self.ser.inWaiting()
        except:
            self.port_close()
            return None
        if num > 0:
            data = self.ser.read(num)
            num = len(data)
            #hex显示
            if  self.checkBox.checkState():
                out_s = ''
                for i in range(0,len(data)):
                    out_s = out_s + '{:02X}'.format(data[i]) + ''
                self.lineEdit_3.insertPlaninText(out_s)
            else:
                #串口接收到的字符串为B'123',要转化成Unicode字符串才能输入到窗口中去
                self.lineEdit_3.insertPlaninText(data.decode('iso-8859-1'))

            #统计接收字符的数量
            self.data_num_received += num
            self.lineEdit.setText(str(self.data_num_received))

            #获取到text光标
            textCursor = self.lineEdit_3.textCursor()
            #滚动到底部
            textCursor.movePosition(textCursor.End)
            #设置光标到text中去
            self.lineEdit_3.setTextCursor(textCursor)
        else:
            pass
    #定时发送数据
    def data_send_timer(self):
        if self.timer_send_cb.isChecked():
            self.timer_send.start(int(self.lineEdit_5.text()))
            self.lineEdit_5.setEnabled(False)
        else:
            self.timer_send.stop()
            self.lineEdit_5.setEnabled(True)
    #清除显示
    def send_data_clear(self):
        self.lineEdit_4.setText('')
    def receive_data_clear(self):
        self.lineEdit_3.setText()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    My =  Mytool()
    My.show()
    sys.exit(app.exec())

