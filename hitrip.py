#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2020/12/25 17:27
# author:qiu
from appium import webdriver
import time

desired_caps = {
                'platformName':'Android',
                'deviceName':'949c3e52',
                'platformVersion':'10.0.3',
                'appPackage':'cn.hitrip',
                'appActivity':'cn.hitrip.MainActivity',
                'unicodeKeyboard ':True,  #使用 unicode 编码方式发送字符串
                'resetKeyboard':True   #是将键盘隐藏起来
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
time.sleep(5)
driver.implicitly_wait(10)
driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element_by_class_name('android.widget.Button').click()
time.sleep(1)
driver.find_element_by_class_name("android.widget.EditText").send_keys('18375836065')
# driver.find_element_by_class_name('android.widget.TextView').click()
time.sleep(1)
driver.find_element_by_class_name('android.widget.Button').click()#点击登录
time.sleep(2)
driver.find_element_by_class_name('android.view.View').click()#点击完成
time.sleep(2)

driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="嗨游服务区"]').click()


# element = driver.find_element_by_class_name('android.view.ViewGroup')
# elements = element.find_elements_by_class_name('android.view.ViewGroup')
# elements[2].click();

# print(driver.get_window_size())
# x = driver.get_window_size()['width']
# # 获取屏幕宽
# y = driver.get_window_size()['height']
#
# driver.swipe(6/7*x, 1/2*y, 1/7*x, 1/2*y, 200)
# time.sleep(1)
# driver.swipe(6/7*x, 1/2*y, 1/7*x, 1/2*y, 200)
# time.sleep(1)
# driver.swipe(6/7*x, 1/2*y, 1/7*x, 1/2*y, 200)

