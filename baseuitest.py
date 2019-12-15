#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-07 9:45
#@Author  : hcj
from selenium import webdriver
from time import sleep
#启动浏览器
brower=webdriver.Chrome()
#启动不同的浏览器
brower=webdriver.Firefox()
brower=webdriver.Ie()
brower=webdriver.Edge()
brower.set_window_size(480,800)

#打开url
brower.get("https://baidu.com/")
sleep(1)
brower.minimize_window()
brower.get("https://cn.bing.com/")

#浏览器导航
brower.back()
brower.forward()
#获取页面title,url源码
print(brower.title)
print(brower.current_url)
brower.refresh()
sleep(1)
print(brower.page_source)
#关闭当前页面
brower.close()
#退出所有页面
brower.quit()

