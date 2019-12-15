#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-07 14:26
#@Author  : hcj
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get("http://baidu.com")
setting=driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(setting).perform()
driver.find_element_by_link_text("高级搜索").click()
sleep(3)
driver.quit()
