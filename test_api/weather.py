#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2021/3/2 9:23
# author:qiu

import requests
import json

url = "http://apis.juhe.cn/simpleWeather/query"

par = {"city":"南京",
       "key":"74c06bcc2929616745713c446449474b"
}

r = requests.post(url,params=par) #采用params格式的写法
print(r.text)

print(r.headers["Content-Type"]) #取返回值中的某个key的值

print(r.headers["Set-Cookie"])

# print(json.dumps(r.json(),indent=4)) #将返回结果转为json格式的，以四个空格隔开

