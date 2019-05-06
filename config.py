#!/user/bin/python3
#_*_coding:utf-8 _*_

import configparser
#生成一个处理对象
config = configparser.ConfigParser()
#默认配置
config["DEFAULT"] = {'SeverAliveInterval': "45",
                     'Compression' : 'yes',
                     'CompressionLevel' : '9'}

#生成其他的配置组
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host port'] = '50022'
topsecret['Forwardx11'] ='no'
config['DEFAULT']['Forwardx11'] = 'yes'
with open('config.ini','w') as configfile:
    config.write(configfile)
