#!/user/bin/python3
#_*_coding:utf-8 _*_

import json
data = {
    'nanbei':'hah',
    'a':[1,2,3,4],
    'b':(1,2,3)
}

with open("json_test.txt",'w') as f :
    print(json.dump(data,f))

with open("json_test.txt",'r+') as f :
    print(json.load(f))