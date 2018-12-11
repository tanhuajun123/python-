# _*_ coding:utf-8 _*_
#! /usr/bin/python3
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',              #数据库主机地址
    user = 'yourusername',
    passwd = 'yourpassword',
    database = 'runoob_db'
)
print(mydb)

#创建数据库，使用CREATE DATABASE 语句
import mysql.connector
mydb = mysql.connector.connect(
   host= 'localhost',
   user= 'root',
   passwd = '123456',
   database = 'runoob_db'
)
mycursor = mydb.cursor()
mycursor.execute('Create Database runoob_db')

#创建数据库前，可以使用‘SHOW DATABASE 语句来查看数据库是否存在
mycursor = mydb.cursor()
mycursor.execute('SHOW DATABASE')

for x in mycursor:
    print(x)

#创建数据表使用 CREATE TABLE 语句，创建数据表前，需要确保数据库已存在
mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE sites (name VARCHAR(255),url VARCHAR(255)) ')

#创建表的时候我们一般会设置一个主键，我们可以使用'INT AUTO_INCREMENT PRIMARY KEY 语句来创建一个主键，主键起始值为1，逐步递增
mycursor = mydb.cursor()
mycursor.execute('ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENTMARY KEY')

#插入数据使用INSERT INTO 语句
mycursor = mydb.cursor()
sql = 'INSERT INTO sites (name , url) VALUES （%s,%s)'
val = ('RUNOOB','http://www.baidu.com')
mycursor.execute(sql,val)

mydb.commit() #数据表内有更新，必须使用到语句
print(mycursor.rowcount,'记录插入成功')

#批量插入使用 executemany()方法，该方法的第二个参数是一个元组列表，包含了我们要插入的数据
mycursor = mydb.cursor()
sql = 'INSERT INTO sites(name,url) VALUES (%s,%s)'
val = [('Baidu,','http://www.baidu,com',
        'Google','http://www.Google.com',
        'Taobao','http://www.taobao.com')
]
mycursor.executemany(sql,val)
mydb.commit()  #数据表内容有更新，必须使用到该语句
print(mycursor.rowcount,'记录插入成功')
print("1条记录已插入，ID:",mycursor.lastrowid)

#查询数据使用 SELECT 语句
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM sites')
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

mycursor = mydb.cursor()
mycursor.execute('SELECT name,url FROM sites')
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#如果只想读取一条数据，可以使用fetchone()方法：
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM sites')
myresult = mycursor.fetchone()
print(myresult)

#where 条件语句，读取指定条件的数据，可以使用 where 语句
mycursor = mydb.cursor()
sql = "SELECT * FEOM sites WHERE name = 'RUNOOB'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

mycursor = mydb.cursor()
sql = "SELECT * FROM sites WHERE url LIKE '%OO%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#为了防止数据库查询发生SQL注入的攻击，我们可以使用%s站位符来转义查询的条件
mycursor = mydb.cursor()
sql = 'SELECT *FROM sites WHERE name = %s'
na = ('RUNOOB',)
mycursor.execute(sql,na)
myresult = mycursor.fetchall()
for x in myresult:
     print(x)

#查询结果排序可以使用ORDER BY语句，默认的排序方式为升序，关键字为ASC，如果要设制降序排序，可以设置关键字DESC
mycursor = mydb.cursor()
sql = 'SELECT *FROM sites ORDER BY name'
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#降序
mycursor = mydb.cursor()
sql = 'SELECT *FROM sites ORDER BY name DESC'
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#设置查询数据量，可以通过 LIMIT 语句来指定
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM sites LIMIT 3')
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#指定起始位置，使用关键字是OFF SET
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM sites LEMIT 3 OFFSET 1  ')   # 0 为第一条，1为第二条，以此类推
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#删除记录使用 DELETE FROM 语句
mycursor = mydb.cursor()
sql = 'DELETE FROM sites WHERE name = "stackoverflow"'
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, '条记录删除')

#更新表数据，数据表使用 UPDATE 语句
mycursor = mydb.cursor()
sql = 'UPDATE sites SET name = "ZH" WHERE name = "Zhihu"'
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,'条记录被修改')

#为了防止数据库查询发生SQL注入的攻击，我们使用%s占位符来转义更新语句的条件
mycursor = mydb.cursor()
sql = 'UPDATE sites SET name = %s WHERE name = %s'
val = ('Zhihu','ZH')
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,'条记录被修改')

#删除表使用的 DROP TABLE 语句，IF EXISTS 关键字是用于判断表是否存在，只有在存在的情况才删除
mycursor = mydb.cursor()
sql = 'DROP TABLE IF EXISTS sites'  #删除数据表sites
mycursor.execute(sql)


#实例
import pymysql
#打开数据库连接
db = pymysql.connect('localhost','tetstuer','test123','TESTDB')
#使用cursor()方法创建一个游标对象
mycursor = db.cursor()
#使用execute()方法执行SQL查询
mycursor.execute('SELECT VERSION()')
#使用fetchone()方法获取单条数据
data = mycursor.fetchone()
print('Database version : %s' % data)
#关闭数据库连接
db.close()

#创建数据库表
import pymysql
#打开数据库
db = pymysql.connect('localhost','testuer','test123','TESTDB')
#使用cursor()方法创建一个游标对象 Cursor
mycursor = db.cursor()
#使用execute()方法执行sql,如果表存在则删除
mycursor.execute('DROP TABLE IF EXISTS EMPLOYEE')
#使用预处理语句创建表
sql = '''CREATE TABLE EMPLOYEE (
         FIRST_NAME CHAR(20) NOT NULL.
         LAST_NAME CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT)'''
mycursor.execute(sql)
#关闭数据库连接
db.close()

#数据库插入操作
import pymysql
#打开数据连接
db = pymysql.connect('localhost','testuser','test123','TESTDB')
#使用cursor（）方法获取操作游标
mycursor = db.cursor()
#sql插入语句
sql = '''INSERT INTO EMPLOYEE (FIRST_NAME,
         LAST_NAME,AGE,SEX,INCOME)
         VALUES('Mac','Mohan',20,'M',2000)'''
try:
    #执行sql语句
    mycursor.execute(sql)
    #提交到数据库执行
    db.commit()
except:
    #如果发生错误则回滚
    db.rollback()
#关闭数据库
db.close()

#数据库查询操作
import pymysql
#打开数据库
db = pymysql.connect('localhost','testuser','test123','TESTDB')
#获取操作游标
mycursor = db.cursor()
#sql查询语句
sql = 'SELLECT * FROM EMPLOYEEE \
       WHERE INCOME > "%d"' % (1000)
try:
    #执行sql语句
    mycursor.execute(sql)
    #获取所有记录列表
    myresult = mycursor.fetchall()
    for row in myresult:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        #打印结果
        print('fname=%s,lname=%s,age=%d,sex=%s,income=%d'% \
              (fname,lname,age,sex,income))
except:
    print('ERROR:unable to fetch data')
#关闭数据库连接
db.close()

#数据库更新操作
import pymysql
#打开数据库连接
db = pymysql.connect('localhost','testuser','test123','TESTDB')
#获取操作游标
mycursor = db.cursor()
#sql更新语句
sql = 'UPDATE EMPLOYEE SER AGE = AGE + 1 WHERE SEX = "%c"' %  ('M')
try:
    #执行sql语句
    mycursor.execute(sql)
    #提交到数据执行
    db.commit()
except:
    #发生错误时回滚
    db.rollback()
#关闭数据库连接
db.close()

#删除操作
import pymysql
#打开你的数据库连接
db = pymysql.connect('localhost','testuser','test123','TESTDB')
#获取操作游标
mycursor = db.cursor()
#删除sql 语句
sql = 'DELETE FROM EMPLOYEE WHRER AGE > "%d"'% (20)
try:
    #执行sql语句
    mycursor.execute(sql)
    #提交到数据
    db.commit()
except:
    #发生错误时处理
    db.rollback()
#关闭连接
db .close()

#sql删除记录语句
sql = 'DELETE FROM EMPLOYEE WHERE AGE > "%d"' % (20)
try:
    #执行sql语句
    mycursor.execute(sql)
    #提交数据库
    db.commit()
except:
    #发生错误时回滚
    db.rollback()

