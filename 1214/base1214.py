#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-14 9:51
#@Author  : hcj
from time import sleep

from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("file:///C:/Users/changjing/Desktop/pop.html")
# # driver.find_element_by_id("goo1").click()
# # sleep(2)
# # driver.find_element_by_id("goo2").click()
# # sleep(2)
# # driver.find_element_by_id("goo3").click()
# # sleep(2)
# # driver.find_element_by_id("goo4").click()
#
# for i in range(1,5):
#     driver.find_element_by_id("goo"+str(i)).click()
#     sleep(1)
# handles=driver.window_handles
# for handele in handles:
#     driver.switch_to.window(handele)
#     print(driver.title)
#
# links=driver.find_elements_by_tag_name("a")
# for link in links:
#     print(link.text)

webchrome=webdriver.Chrome()
url="http://www.baidu.com"
webchrome.get(url)
links=webchrome.find_elements_by_tag_name("a")
flag=0
for link in links:
     if "About" in link.text:
         link.click()
         flag=1
         break

if flag==0:
   print("no such element")
# print(printa)


