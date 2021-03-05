#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2020/12/29 11:43
# author
import ddt
import unittest
# 测试数据
testdata =[{"user":"zhangsan","psw":"123"},
           {"user":"wangwu","psw":"456"}]

@ddt.ddt()

class Test(unittest.TestCase):
    def setUp(self):

        print("start")

    def tearDown(self):
        print("end")

    @ddt.data(*testdata)

    def test_ddt(self,data):

        print(data)
    if __name__ == "__main__":
        unittest.main()

