#!/user/bin/python3
#_*_coding:utf-8 _*_
from config import *
from aip import AipSpeech
from playsound import playsound
import time
APP_ID = '15124327'
API_KEY = 'tIjgKXnnSM7m0o6LQQHnoffw'
SECRET_KEY = 'n9u76a12YF4IBA9Qy2Rfw8zBbfG25e1w'
client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)
with open(r'audio.txt', 'r') as f:
    content_s = f.read()
result = client.synthesis(content_s, 'zh', 1, {
    'vol': 9,
    'spd': 2,
    'pit': 5,
    'per': 0,
})
time.sleep(2)
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)
playsound("auido.mp3")