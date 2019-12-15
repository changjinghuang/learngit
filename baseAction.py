#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-07 13:50
#@Author  : hcj
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

brwoer=webdriver.Chrome()
brwoer.get("http://baidu.com/")
# setting=brwoer.find_element_by_name("tj_settingicon")
setting=brwoer.find_element_by_name("tj_briicon")
# print(setting.get_attribute())
ActionChains(brwoer).move_to_element(setting).perform()
brwoer.find_element_by_name("tj_img").click()

sleep(4)
brwoer.quit()

#
#
# from selenium import webdriver
# from time import sleep
#
# browser = webdriver.Chrome()
#
# browser.get("https://www.baidu.com/")
# sleep(2)
# news = browser.find_element_by_link_text("新闻")
# news.click()
# sleep(2)
# browser.back()
# sleep(1)
# map = browser.find_element_by_partial_link_text("地")
# map.click()
# sleep(2)
#
# browser.quit()


# from selenium import webdriver
# from time import sleep
#
# from selenium.webdriver import ActionChains
#
# browser = webdriver.Chrome()
# browser.get("https://www.baidu.com/")
#
# more = browser.find_element_by_name("tj_briicon")
#
# #鼠标移动到更多产品上
# ActionChains(browser).move_to_element(more).perform()
# sleep(3)
# browser.find_element_by_name("tj_img").click()
# sleep(2)
# browser.quit()