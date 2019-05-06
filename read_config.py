#!/user/bin/python3
#_*_coding:utf-8 _*_

import configparser
import os
os.system('config.py')

config = configparser.ConfigParser()
config.read('config.ini')

print(config.sections())
print(config.defaults())
print(config['bitbucket.org'])
print(config['bitbucket.org']['User'])