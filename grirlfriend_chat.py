#!/user/bin/python3
#_*_coding:utf-8 _*_


from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import random

bot = Bot()


# linux执行登陆请调用下面的这句
# bot = Bot(console_qr=2,cache_path="botoo.pkl")
def get_news():
    """获取金山词霸每日一句，英文和翻译"""
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note


def send_news():
    try:
        contents = get_news()
        # 你朋友的微信名称，不是备注，也不是微信帐号。
        #my_friend = bot.friends().search('夏天')[0]
        # 输入群名称【】和你的群聊对象""
        my_friend = bot.groups().search("阿文"),[兔路小分队]
        my_friend.send(contents[0])
        my_friend.send(contents[1])
        my_friend.send(u"当你还能付出时千万不要放弃，任何事都不会真正结束，直到你停止努力，放弃的那一刻！")
        # 每86400秒（1天），发送1次
        t = Timer(86400, send_news)
        # 为了防止时间太固定，于是决定对其加上随机数
        ran_int = random.randint(0, 100)
        t = Timer(86400 + ran_int, send_news)

        t.start()
    except:

        # 你的微信名称，不是微信帐号。
        my_friend = bot.friends().search('须归')[0]
        my_friend.send(u"今天消息发送失败了")


if __name__ == "__main__":
    send_news()
