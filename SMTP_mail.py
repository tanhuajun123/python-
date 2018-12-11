# _*_ coding:utf-8 _*_
#! /usr/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.header import Header

seder = 'from@runoob.com'
receivers = ['1017144496@qq.com']  #接收邮箱
#三个参数：第一个为文本内容，第二个plain设置文本格式，第三个设置utf编码
message = MIMEText('python邮件发送测试。。。','planin','utf-8')
message['From'] = Header('菜鸟教程','utf-8')   #发送者
message['To'] = Header('测试','utf-8')     #接收者

subject = 'python SMTP 邮件测试'
message ['subject'] = Header(subject,'utf-8')
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(seder,receivers,message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('error:无法发送邮件')


#建立第三方 SMTP 服务器
mail_host = 'smtp.xxx.com' #设置服务器
mail_user = 'xxxx'   #用户名
mail_pass = 'xxxxxxxxx' #口令