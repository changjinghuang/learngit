#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-09 19:47
#@Author  : hcj

from selenium import  webdriver
from time import sleep
import os
driver=webdriver.Chrome()
driver.get("http://baidu.com")
# img=os.path.abspath("file:///C:/Users/changjing/Desktop/main.html")
driver.find_element_by_xpath("//*[@id='form']/span[1]/span").click()
sleep(3)
##driver.find_element_by_class_name("upload-pic").send_keys('C:/Users/changjing/Desktop/autotest.html')
driver.find_element_by_class_name("upload-pic").send_keys('C:/Users/changjing/Desktop/luhan.jpg')
# driver.find_element_by_class_name("upload-pic").send_keys(img)
sleep(3)
# photoico.send_keys("‪C:\Users\changjing\Desktop\luhan.jpg")
sleep(1)
driver.quit()