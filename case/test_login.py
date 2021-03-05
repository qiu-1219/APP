#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2020/12/23 17:49
# author:qiu
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from case.loginfuc import LogInOA
from case.Index_page import IndexPage
class LoginTest(unittest.TestCase):

    def setUp(self):

        self.driver.maximize_window()
        self.driver.get('http://120.55.190.222:9090/loginController.do?login2')
        self.lg = LogInOA(self.driver)
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  #浏览器只打开一次


    def test01(self):
        """登录成功案例"""
        self.lg.login('SQOA006','sqtest')
        time.sleep(2)
        self.assertTrue(IndexPage(self.driver).loginsucess())

    def test02(self):
        """用户名正确，密码错误"""
        self.lg.login('SQOA006','1232131')
        time.sleep(2)
        self.assertTrue(IndexPage(self.driver).loginsucess())
    def test03(self):
        """用户名正确，密码为空"""
        self.lg.login('SQOA003','')
        time.sleep(1)
        self.assertTrue(IndexPage(self.driver).loginsucess())
    def test04(self):
        """用户名正确，密码为大写"""
        self.lg.login('SAOA001','SQOA001')
        time.sleep(1)
        self.assertTrue(IndexPage(self.driver).loginsucess())

    def tearDown(self):
        time.sleep(2)
        self.driver.delete_all_cookies()
        # 清空cookies，即退出登录



    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()  #编辑器的问题,所有用例执行完之后关闭浏览器

    if __name__ == "__main__":
        unittest.main()

