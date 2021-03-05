#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2020/12/30 9:04
# author:qiu
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
class LogInOA():
    def __init__(self,driver):
        self.driver = driver

    def login(self,username,passwd):
        time.sleep(1)
        name_text = "//*[@id='userName']"
        psw_text = "//*[@id='password']"
        login_but = "//*[@id='but_login']"
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,name_text)))
        self.driver.find_element_by_xpath(name_text).send_keys(username)
        self.driver.find_element_by_xpath(psw_text).send_keys(passwd)
        self.driver.find_element_by_xpath(login_but).click()


#
#     def is_login_sucess(self):
#         try:
#             time.sleep(2)
#             t = self.driver.find_element_by_xpath("//*[@class='roll-nav roll-right J_tabExit']").text
#             print(t)
#             return t
#         except:
#             return "登录失败"
#
#
#
# if __name__ == "__main__":
#
#         from selenium import webdriver
#         driver = webdriver.Chrome()
#         sqoa = LogInOA(driver)
#         sqoa.login()







