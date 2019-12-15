#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-10 0:21
#@Author  : hcj
from selenium import  webdriver
import unittest
from time import sleep
import os
from selenium.webdriver import ActionChains
#百度登陆页面
driver=webdriver.Chrome()
driver.get("http://baidu.com")
driver.fullscreen_window()
driver.maximize_window()
# driver.find_element_by_css_selector()
print(driver.title)
print(driver.current_url)
driver.refresh()
sleep(3)
# driver.find_element_by_link_text("登陆").click()
driver.find_element_by_link_text("登录").click()
sleep(2)
driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
sleep(1)
driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("13817141700")
sleep(1)
driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("hcj03250861")
sleep(1)
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
vcode=driver.find_element_by_xpath("//*[@id='vcode-spin-button798']")
ActionChains(driver).click_and_hold(vcode).perform()