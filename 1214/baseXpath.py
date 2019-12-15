#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-14 11:03
#@Author  : hcj
from time import sleep
from selenium import  webdriver
webchrome=webdriver.Chrome()
# webchrome.get("http://www.ccb.com/cn/home/indexv3.html")
# # webchrome.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[1]/a")
# # webchrome.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[4]/a")
# #绝对路径
# user = webchrome.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/ul/li[4]/a')
# #相对路径
# # user = webchrome.find_element_by_xpath('//*[@id="portfolio"]/div[1]/div/div[1]/div/div[1]/ul/li[4]/a')
webchrome.get("file:///C:/Users/changjing/Desktop/css.html")
# webchrome.find_element_by_xpath("//*[@value='SYS123456']").send_keys("adb")
# print(webchrome.find_element_by_xpath("//*[text()='Cat']").text)
# print(webchrome.find_element_by_xpath("//*[text()='Cat']").text)
# for i in range(1,5):
# print(webchrome.find_element_by_xpath("//ul[@id='recordlist']/li["+str(i)+"]").text)
# sleep(1)
# print(webchrome.find_element_by_xpath("//input[@*='password']").send_keys("test"))
animials=webchrome.find_elements_by_xpath("//ul[@id='recordlist']/li")
for animial in animials:
    print(animial.text)
sleep(2)
webchrome.quit()

webchrome.find_elements_by_xpath()