#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-08 16:25
#@Author  : hcj
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#从百度搜索页面进入建设银行
Chromdriver=webdriver.Chrome()
print(Chromdriver)
Chromdriver.get("http://baidu.com")
kw=Chromdriver.find_element_by_id("kw")
kw.send_keys("中国建设银行")
sleep(1)
kw.send_keys(Keys.DOWN)
sleep(1)
kw.send_keys(Keys.DOWN)
kw.send_keys(Keys.ENTER)
sleep(1)
Chromdriver.find_element_by_link_text("中国建设银行").click()
sleep(4)
windowhandles=Chromdriver.window_handles
for windowhandle  in windowhandles:
     sleep(3)
     Chromdriver.switch_to.window(windowhandle)
     if "欢迎访问中国建设银行" in Chromdriver.title:
         break;
     sleep(2)
sleep(5)
Chromdriver.find_element_by_class_name("Quick_Link_top_button").click()
sleep(2)
handles=Chromdriver.window_handles
for handle in handles:
     sleep(3)
     Chromdriver.switch_to.window(handle)
     if "个人客户" in Chromdriver.title:
         break;
     sleep(2)
Chromdriver.switch_to.frame(0)
sleep(2)
Chromdriver.find_element_by_id("USERID").send_keys("abcd")
sleep(1)
Chromdriver.find_element_by_id("LOGPASS").send_keys("bbb")
sleep(1)
Chromdriver.switch_to.parent_frame()
sleep(1)
# text=Chromdriver.find_element_by_xpath("//*[@id='portfolio']/div[1]/div/div[1]/div/div[1]/ul/li[1]/a").text
text=Chromdriver.find_element_by_css_selector("#portfolio > div.w > div > div.header_top > div > div.header_info_left > ul > li:nth-child(1) > a").text
assert text=="个人客户"
print(text)
Chromdriver.quit()


