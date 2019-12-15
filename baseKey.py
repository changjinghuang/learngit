#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-07 14:47
#@Author  : hcj
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

brower=webdriver.Chrome()
brower.get("http://baidu.com/")
input=brower.find_element_by_id("kw")
input.send_keys("sel")
sleep(1)
input.send_keys(Keys.DOWN)
sleep(1)
input.send_keys(Keys.DOWN)
sleep(1)
input.send_keys(Keys.UP)
sleep(1)
brower.quit()
