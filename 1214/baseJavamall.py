#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-14 16:00
#@Author  : hcj

from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

brower=webdriver.Chrome()
url="http://10.160.250.208:8080/javamall/admin/backendUi!main.do"
brower.get(url)
sleep(1)
#先删除cookie
brower.delete_all_cookies()
#添加cookie
cookie={'name':'JSESSIONID','value':"C3186DD58F5932EA5339E8F485620351"}
brower.add_cookie(cookie)
sleep(1)
#从新获取url
brower.get(url)
sleep(3)

#登陆状态进行操作，真正开始测试
#设置=》管理员管理
setting = brower.find_element_by_xpath('//*[@id="parent43"]/a/div[4]')
ActionChains(brower).move_to_element(setting).perform()
sleep(2)
#点击管理员管理
brower.find_element_by_xpath('//*[@id="43"]/div/ul/li[4]/ul/li[1]/a').click()
sleep(2)
#切换进管理员管理frame
iframe = brower.find_element_by_xpath('//*[@id="58"]/iframe')
brower.switch_to.frame(iframe)
#点击添加 frame 切换 页面加载的时候休眠一两秒
sleep(2)
brower.find_element_by_xpath("/html/body/div[3]/div[2]/a").click()
sleep(2)
brower.find_element()
brower.find_element_by_id()
brower.quit()


