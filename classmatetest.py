#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-08 16:46
#@Author  : hcj
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver import ActionChains
brower = webdriver.Chrome()
brower.get("https://www.baidu.com/")
input = brower.find_element_by_id("kw")
input.send_keys("中国建设")
sleep(1)
input.send_keys(Keys.DOWN)
sleep(2)
input.send_keys(Keys.ENTER)
sleep(2)
# button = brower.find_element_by_id("su")
# # ActionChains(brower).move_to_element(button).perform()
# # print(button.is_enabled())
# button.click()
guanwang = brower.find_element_by_link_text("中国建设银行")
guanwang.click()
sleep(3)
# brower.switch_to.frame(1)
# sleep(1)
handles = brower.window_handles
for handle in handles:
    sleep(3)
    brower.switch_to.window(handle)
    if brower.title == "欢迎访问中国建设银行网站":
       break
sleep(2)
brower.find_element_by_class_name("Quick_Link_top_button").click()

# login = brower.find_element_by_link_text("登陆")
# login.click()
sleep(3)