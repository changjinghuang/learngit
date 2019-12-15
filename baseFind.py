#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-07 10:27
#@Author  : hcj
import select

from selenium import  webdriver
from time import sleep
# browser=webdriver.Chrome()
# browser.get("http://baidu.com")
# element=browser.find_element_by_id("kw")
# element=browser.find_element_by_class_name("s_ipt")
# element2=browser.find_element_by_class_name("s_btn")
# element.send_keys("selenium")

# element2.click()
#
# sleep(1)


# driver=webdriver.Chrome()
# driver.get("https://cn.bing.com/")
# # driver.minimize_window()
# id=driver.find_element_by_id("sb_form_q")
# sleep(2)
# id.send_keys("selenium")
# id2=driver.find_element_by_id("sb_form_go")
# sleep(2)
# id2.click()

# brower = webdriver.Chrome()
# brower.get("https://cn.bing.com/")
# element = brower.find_element_by_id("sb_form_q")
# element.send_keys("selenium")
# sleep(2)
# element2 = brower.find_element_by_id("sb_form_go")
# element2.click()
# sleep(3)
# brower.quit()
from selenium.webdriver.support.select import Select
#
brwoer=webdriver.Chrome()
brwoer.get("file:///C:/Users/changjing/Desktop/autotest.html")
accountID=brwoer.find_element_by_id("accountID")
accountID.clear()
passwordID=brwoer.find_element_by_id("passwordID")
passwordID.clear()
accountID.send_keys("hcj")
passwordID.send_keys("pingan123")
#(alt+enter)
print(accountID.get_attribute("value"))

# select=brwoer.find_element_by_id("areaID")
# sleep(1)
# Select(select).select_by_visible_text("北京市")
# # Select(select).select_by_index(3)
# sexID2=brwoer.find_element_by_id('sexID2')
# sexID2.click()
# print(sexID2.is_enabled())
# for i in range(1,5):
#     u4=brwoer.find_element_by_id("u"+str(i))
#     u4.click()
# file=brwoer.find_element_by_name("file")
# file.send_keys("C:/Users/changjing/Desktop/autotest.html")
# sleep(3)
# buttonID=brwoer.find_element_by_id("buttonID")
# buttonID.click()
# sleep(3)
# alert=brwoer.switch_to.alert
# alert.dismiss()
# sleep(3)
# brwoer.quit()

#模态窗口
# driverChrome=webdriver.Chrome()
# driverChrome.get("file:///C:/Users/changjing/Desktop/dialogs.html")
# alert1=driverChrome.find_element_by_id("alert").click()
# alert2=driverChrome.switch_to.alert
# alert2.accept()
# sleep(2)
# driverChrome.find_element_by_id("confirm").click()
# sleep(2)
# alert4=driverChrome.switch_to.alert
# alert4.dismiss()
#
# sleep(2)
# driverChrome.quit()
#

