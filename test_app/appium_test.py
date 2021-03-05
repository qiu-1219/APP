#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2020/12/24 9:40
# author:qiu
from appium import webdriver
import time

desired_caps = {
                'platformName':'Android',
                'deviceName':'949c3e52',
                'platformVersion':'10.0.3',
                'appPackage':'com.tencent.news',
                'appActivity':'com.tencent.news.activity.SplashActivity',
                'unicodeKeyboard ':True,  #使用 unicode 编码方式发送字符串
                'resetKeyboard':True   #是将键盘隐藏起来
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
time.sleep(5)
driver.implicitly_wait(20)
driver.find_element_by_id('com.tencent.news:id/pd').click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element_by_id('com.tencent.news:id/cp4').click()
time.sleep(5)
contexts = driver.contexts
print(contexts)#切换到新闻主页获取所有的环境
time.sleep(3)

print('over')









# driver.find_element_by_id('com.tencent.news:id/c8l').send_keys(u'英国')

# # driver.switch_to.alert.accept()
# time.sleep(3)
# driver.find_element_by_xpath('').click()
# time.sleep(2)
# driver.find_element_by_class_name('android.widget.LinearLayout').click()
# time.sleep(3)
# driver.find_element_by_class_name('android.widget.ImageViewo').click()