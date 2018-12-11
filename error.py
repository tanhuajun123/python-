# _*_ coding:utf-8 _*_
#! /usr/bin/python3
while True:
    try:
        x = int(input('请输入你认为正确的数值：'))
        break
    except ValueError:
        print('请再次确认你想输入的数值！')
import  sys
try:
    f = open('D://aws//tst.txt')
    s = f.readlines()
    i = int(s.steip())
except OSError as err:
    print('OS 错误：{0}'.format(err))
except ValueError:
    print('重新开始，继续不用停')
except:
    print('系统错误：',sys.exc_info()[0])
    raise

for arg  in  sys.argv[1:]:
    try:
        f = open(arg,'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has',len(f.readlines()),'liens')
        f.close()

#先设置一个异常条件
def this_fails():
    x = 1/0

    try:
        this_fails()
    except ZeroDivisionError as err:
        print('handling run-time error:',err)

'''handling run - time error: int division or modulo by zero'''


'''try:
   raise NameError('hi there')
except NameError:
   print('an exception flew by!')
   raise '''

'''class MyError(Exception):
    def __init__(self,value):
        self.value = value
        def __str__(self):
            return  repr(self.value)

        try:
            raise  MyError(2*2)
        except MyError as e :
            print('My exception occurred , value:' , e.value)
'''
'''try:
    raise  KeyboardInterrupt
finally:
    print('Gooogle bye!')
    '''

'''def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero!')
    else:
        print('result is ', result)
    finally:
        print('executing finally clause')'''

#预先定义清理行为
'''for line in open('D://aws//tx.txt'):
    print(line,end='')

with open('myflie.txt') as f :
    print(line1, end='')
'''
#参数的异常处理
def temp_convert(var):
    try:
        return int(var)
    except (ValueError) as Argument:
        print('参数没有包含数字\n',Argument)

temp_convert('xyz')


