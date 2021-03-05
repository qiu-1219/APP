#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2020/12/23 17:51
# author:qiu




# 方法一：

import unittest
import HTMLTestRunner_cn
casePath = 'D:\project\APP\\case'
rule = "test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)

reportpath = "D:\\project\APP\\case\\report\\result.html"
fp = open('test_app/result.html', 'wb')
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title="测试报告的名字",
                                          description='这是我的测试报告')

runner.run(discover)











# #方法二
# loader = unittest.TestLoader()
# # from python_study.youyou.case import test_case
#
# suite.addTest(loader.loadTestsFromModule(test_case)) #从testcase中去寻找用例
#
#
# fp = open('result.html','wb')
#
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
#                                     title="报告的title",
#                                     description="测试报告")
# runner.run(suite)
# fp.close()