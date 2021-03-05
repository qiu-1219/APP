#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2021/3/3 13:27
# author:qiu


import requests
import json
#登录用户，获取token
url = "http://120.55.190.222:9090/rest/toController"

# header = {"Content-Type":"application/json"}

payload = {"userName":"SQOA006",
           "password":"sqtest"}



data_json = json.dumps(payload)

response = requests.post(url,json=data_json)

print(response.text)

