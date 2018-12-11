# _*_ coding:utf-8 _*_
#! /usr/bin/python3
import json
#pythoN字典类型转换为JSON对象
data = {
    'no':1,
    'name':'Runoob',
    'url':'http://www.runoob.com'
}

json_str = json.dumps(data)
print('python 原始数据：',repr(data))
print('JOSN对象：',json_str)

#python 字典类型转换为json对象
data1={
    'no':1,
    'name': 'runoob',
    'url':'http://www.baidu.com'
}

json_str = json.dumps(data1)
print('pyrhon 原始数据：',repr(data1))
print('JSON 对象：',json_str)

#将JSON对象转换为python
data2 = json.loads(json_str)
print("data2['name']:",data2['name'])
print("data2['url']:",data2['url'])


#写入JSON数据
with open('data.json','w') as f:
    json.dump(data,f)

#读取数据
with open('data.json','r') as f:
    data = json.load(f)