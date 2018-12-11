# _*_ coding:utf-8 _*_
#! /usr/bin/python3

import  re
print(re.match('www','www.runoob.com').span())  #在起始位置匹配
print(re.match('com','www.runoob.com'))    #不在起始位置匹配

line = 'cat are smarter than dogs'
matchobj = re.match(r'(.*)are(.*?).*',line,re.M|re.I)

if matchobj:
    print('matchobj.group():',matchobj.group())
    print('matchobj.group(1):',matchobj.group(1))
    print('matchobj.group(2):',matchobj.group(2))
else:
    print('no math!!!')

print(re.search('www','www.runoob.com').span())
print(re.search('com','www.runoob.com').span())

phone = '123456-235-395'  #电话号码
num = re.sub(r'#.*$','',phone)
print('电话号码：',num)

num = re.sub(r'\D','',phone)
print('电话号码：',num)

def double (mathed):
    value = int(mathed.group('value'))
    return str(value *2)
s = 'A23G4HFD567'
print(re.sub("(?P<value>\d+)",double,s))

pattern = re.compile(r'\d+')           #用于匹配至少一个数字
m = pattern.match('one12twothree34four')
print(m)

patter = re.compile(r'([a-z])+([a-z]+)',re.I)     #re.I表示忽悠大小写
m = patter.match('HELLO WORD WIDE WEB')
print(m)
m.group(1)

patten = re.compile(r'\d+')
res1 = patten.findall('runksnddds2251122 32321dsfsdf 2133dfds 2s12f1dsf2s1f2ds')
res2 = patten.findall('gs323sdf3sd3f2s2f32sf3s1gffghvxcv133dfs3',0,10)
print(res1)
print(res2)


it = re.finditer(r'\d+','sa21f1f31fsdf3sdfsdf31sd')
for match in it :
    print(match.group())

re.split('\W+','hfjshjfhsjhfafs,fh,shfj,k,sfj')
