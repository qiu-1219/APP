#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2021/2/23 13:28
# author:qiu


# 发送post请求获取token

import requests
import json
url = "http://120.55.190.222:9090/rest/toController"

header = {"Content-Typ":"application/json"}

payload = {'userName':'SQOA006',
           'password':'sqtest'}

# data = json.dumps(payload)

r = requests.post(url,headers=header,data=json.dumps(payload))
print(r.text)