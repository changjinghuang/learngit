#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-07 15:28
#@Author  : hcj
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get("file:///C:/Users/changjing/Desktop/testprompt2.html")
button=driver.find_element_by_name("button1")
# button.click()
# sleep(1)
# alert.send_keys("admin")
# sleep(1)
# alert.accept()

button.click()
alert1=driver.switch_to.alert
sleep(1)
alert1.send_keys("selenium")
print(alert1.text)
sleep(1)
alert1.dismiss()

# driver=webdriver.Chrome()
# driver.get("file:///C:/Users/changjing/Desktop/frame.html")
# input=driver.find_element_by_id("input1")
# input.send_keys("adaf")
# driver.quit()
#元素获取不到的时候通过查看源码
# driver=webdriver.Chrome()
# driver.get("file:///C:/Users/changjing/Desktop/main.html")
# driver.switch_to.frame(0)
# input=driver.find_element_by_id("input1")
# input.send_keys("adaf")
# # driver.switch_to.default_content()
# print(driver.page_source)
# driver.switch_to.parent_frame()
# driver.quit()
#
# driver=webdriver.Chrome()
# driver.get("https://ibsbjstar.ccb.com.cn/CCBIS/V6/common/login.jsp?UDC_CUSTOMER_ID=&UDC_CUSTOMER_NAME=&UDC_COOKIE=a49202bfd5735801XRc00CDPuTYrcZxrLiCi1553322967612lMYrh7tf1UzPX6LLSUy6d69135281ff8dd9f88c844a89a8fcdd6&UDC_SESSION_ID=DUKLKE6b2bfSF3l40e825581a4a-20191207161243")
# driver.switch_to.frame(0)
# userid=driver.find_element_by_id("USERID")
# userid.send_keys("adfasf")
# logpass=driver.find_element_by_id("LOGPASS")
# logpass.send_keys("adaf")
# driver.quit()

# driver1=webdriver.Chrome()
# driver1.get("file:///C:/Users/changjing/Desktop/testpop.html")
# driver1.find_element_by_link_text("百度搜索").click()
# handles=driver1.window_handles
# for handle in handles:
#     driver1.switch_to.window(handle)
#     print(driver1.title)
#     if driver1.title=="百度一下，你就知道":
#         break
# kw=driver1.find_element_by_id("kw")
# kw.send_keys("selen")
# sleep(1)
# driver1.quit()



