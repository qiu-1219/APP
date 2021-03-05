#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2020/12/29 14:47
# author:qiu
# import redis
# r=redis.Redis(host='host',port='port',password='password',decode_responses=True)
# print(r.get('验证码存储路径:手机号'))


result = 0

i = 0

while i <=100:

    result+=i

    i+=1

print(result)



count=0
sum=0
while count<101:
    sum += count
    count +=1
print(sum)



num = 1
# 当 num 小于100时，会一直执行循环体
while num < 100 :
    print("num=", num)
    # 迭代语句
    num += 1
print("循环结束!")


# 使用类名调用实例方法
class CLanguage:
    #类构造方法，也属于实例方法
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    # 下面定义了一个say实例方法,直接使用实例调用方法
    def say(self):
        print("正在调用 say() 实例方法")

clang = CLanguage()
clang.say()

class CLanguage:
    #类构造方法，也属于实例方法
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    #下面定义了一个类方法
    @classmethod
    def info(cls):
        print("正在调用类方法",cls)
# 直接使用类名调用类方法
CLanguage.info()
# 使用类对象调用类方法
clang2 = CLanguage()
clang2.info()




