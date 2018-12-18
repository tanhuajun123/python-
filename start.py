#!/user/bin/python
# -*- coding: utf-8-*-
import sys
from dialog import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import num2

class Heng(QtWidgets.QMainWindow,Ui_Dialog):
    def __init__(self,parent=None):
        super(Heng,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('短信轰炸器')
        self.setWindowIcon(QtGui.QIcon(''))
        self.lineEdit.setText('')
        self.pushButton_3.clicked.connect(self.button3)
        self.pushButton_2.clicked.connect(self.button2)
        self.pushButton.clicked.connect(self.button)
        self.textEdit.setText('')
        self.lineEdit_2.setText('1')
        self.SMSsend_one_Thread = QtCore.QThread()


    def linEdit(self):
        print('OK')
    def linEdit2(self):
        print('OK')
    def text(self):
        print('ok')
    def button(self):
        self.SMSsend_one_Thread = num2.SMSsend_one(self.lineEdit.text(),self.lineEdit_2.text())
        self.SMSsend_two_Thread = num2.SMSsend_one(self.lineEdit.text(), self.lineEdit_2.text())
        self.SMSsend_three_Thread = num2.SMSsend_one(self.lineEdit.text(), self.lineEdit_2.text())
        self.SMSsend_four_Thread = num2.SMSsend_one(self.lineEdit.text(), self.lineEdit_2.text())
        self.SMSsend_fine_Thread = num2.SMSsend_one(self.lineEdit.text(), self.lineEdit_2.text())
        self.SMSsend_six_Thread = num2.SMSsend_one(self.lineEdit.text(), self.lineEdit_2.text())
        self.SMSsend_seven_Thread = num2.SMSsend_one(self.lineEdit.text(), self.lineEdit_2.text())
        self.SMSsend_eigth_Thread = num2.SMSsend_one(self.lineEdit.text(), self.lineEdit_2.text())
        self.SMSsend_one_Thread.log_output_sigl.connect(self.log_output)
        self.SMSsend_two_Thread.log_output_sigl2.connect(self.log_output)
        self.SMSsend_three_Thread.log_output_sigl3.connect(self.log_output)
        self.SMSsend_four_Thread.log_output_sigl4.connect(self.log_output)
        self.SMSsend_fine_Thread.log_output_sigl5.connect(self.log_output)
        self.SMSsend_six_Thread.log_output_sigl6.connect(self.log_output)
        self.SMSsend_seven_Thread.log_output_sigl7.connect(self.log_output)
        self.SMSsend_eigth_Thread.log_output_sigl8.connect(self.log_output)

    def button2(self):
        self.SMSsend_one_Thread.isRunning()
        self.SMSsend_one_Thread.terminate()
        self.SMSsend_two_Thread.isRunning()
        self.SMSsend_two_Thread.terminate()
        self.SMSsend_three_Thread.isRunning()
        self.SMSsend_three_Thread.terminate()
        self.SMSsend_four_Thread.isRunning()
        self.SMSsend_four_Thread.terminate()
        self.SMSsend_fine_Thread.isRunning()
        self.SMSsend_fine_Thread.terminate()
        self.SMSsend_six_Thread.isRunning()
        self.SMSsend_six_Thread.terminate()
        self.SMSsend_seven_Thread.isRunning()
        self.SMSsend_seven_Thread.terminate()
        self.SMSsend_eigth_Thread.isRunning()
        self.SMSsend_eigth_Thread.terminate()
        self.textEdit.append('已关闭')


    def button3(self):
        print('ok')


    def log_output(self,argv):
        self.textEdit.append(argv)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Heng()
    window.show()
    sys.exit(app.exec_())
