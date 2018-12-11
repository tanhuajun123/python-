# _*_ coding:utf-8 _*_
#! /usr/bin/python3
#创建一个数据库
import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb= myclient['runnoobdb']

#判断数据库是否存在
myclient = pymongo.MongoClient('mongodb:/localhost:27017/')
dblist = myclient.list_database_names()
if 'runoobdb' in dblist:
    print('数据库已存在')

#创建一个集合
myclient = pymongo.MongoClient('mongodb:/localhost:/271017/')
mydb = myclient['runoodb']
mycol = mydb['sites']

myclient = pymongo.MongoClient('mongodb://localhost:271017/')
mydb = myclient['runoodb']
collist = mydb.list_collection_names()
if 'sites' in collist:
    print('数据库已存在')

