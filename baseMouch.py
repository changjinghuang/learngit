#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-07 15:00
#@Author  : hcj
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get("file:///C:/Users/changjing/Desktop/Clicks.html")
doubleclick=driver.find_element_by_id("button1")
ActionChains(driver).double_click(doubleclick).perform()
sleep(3)
contextClick=driver.find_element_by_id("button3")
ActionChains(driver).context_click(contextClick).perform()
sleep(1)
quit()


