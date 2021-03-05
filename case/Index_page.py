#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2020/12/30 9:48
# author:qiu
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class IndexPage:

    def __init__(self,driver):
        self.driver = driver
        sleep(1)


    def loginsucess(self):
        # 如果存在就返回True,不存在就返回False
        # 确定元素的定位表达式ele_locator = "TANGRAM__PSP_10__footerULoginBtn"  # 通过id,确定‘用户名登录’元素
        #
        # EC.方法名(定位方式,定位表达式)
        # EC.visibility_of_element_located(By.ID,ele_locator)#元素可见
        # 调用WebDriverWait类设置等待总时长、轮询周期
        # WebDriverWait(driver, 超时时长, 调用频率（默认0.5s）).until(可执行方法, 超时时返回的信息)
        # 等待15秒钟，每隔1秒去查看对应的元素是否可见；如果可见，继续下一步操作；如果不可见，则继续等待，直到15s结束，如果元素还是不可见，则抛出超时异常
        # WebDriverWait(driver,10,1).until(EC.visibility_of_element_located((By.ID, ele_locator)))

        local = (By.XPATH,"//*[@class='right-sidebar-toggle']")

        try:
            WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(local))
            return True
        except:
            print("登录失败")
            return False
