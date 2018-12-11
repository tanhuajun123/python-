#conding=utf-8
#filename:redball.py
import random
import math
#这是一个彩票生成程序，可以随机生成双色球和大乐透

class newBall:
    _redQuantity = 0
    _blueQuantity = 0
    _redMax = 0
    _blueMax = 0
    _oneRecord = ()

    #类的初始化
    def __init__(self, redMax, redQuantity, blueMax, blueQuantity):
        self._redMax = redMax
        self._redQuantity = redQuantity
        self._blueQuantity = blueQuantity
        self._blueMax = blueMax
    #生成一个新的数据
    def produce_new(self):
        #从一个队列里面随机选取self._redQuantity数目的数字
        redBallList = range(1, self._rabMax + 1)
        redNewList = random.sample(redBallList, self._redQuantity)
        redBallList = sorted(redNewList)
        #随机生成蓝球
        blueBallList = range(1, self._blueMax + 1)
        blueNewList = random.sample(blueBallList, self._blueQuantity)
        self._oneRecord = redNewList + blueNewList

        #在console里面显示结果
    def showResult(self):
        print self._oneRecord
#双色球规则：33个球中抽取6个，16个蓝球中抽取1个
redball = newBall(33, 6, 16, 1)
redball.produce_new()
redball.showResult()
#大乐透规则：35个球中抽去5个，12个蓝球中抽取2个
sevenBall = newBall(35, 5, 12, 2)
sevenBall.produce_new()
sevenBall.showResult()



