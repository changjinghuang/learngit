#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-07 20:38
#@Author  : hcj
import random
from time import sleep

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.ccb.com/cn/home/indexv3.html")
driver.find_element_by_class_name("Quick_Link_top_button").click()
handles=driver.window_handles
sleep(2)
for handle in handles:
    driver.switch_to.window(handle)
    sleep(2)
    if  "个人客户网上银行" in driver.title:
        break

driver.switch_to.frame(0)
driver.find_element_by_id("USERID").send_keys("aaa")
sleep(2)
# logPass=driver.find_element_by_id("LOGPASS").send_keys("bbb")
driver.find_element_by_id("keyboardBtn").click()
keybordkeyboardBtn=driver.find_element_by_id("keybordkeyboardBtn")
# print(keybordkeyboardBtn)
table=keybordkeyboardBtn.find_element_by_tag_name("table")
trlist=table.find_elements_by_tag_name("tr")
# print(list)
valuelist=[]
#循环行
for i in range(len(trlist)):
    tdlist=trlist[i].find_elements_by_tag_name("td")
#循环列
    for j in range(len(tdlist)):
#获取每一列的值放入list中
      value=trlist[i].find_elements_by_tag_name("td")[j]
      valuelist.append(value)
print(valuelist)
#随机获取10位密码
for j in range(len(valuelist)):
       # if valuelist[j].text!="确定":
       #       valuelist[j].click()
       # else:
       #     pass
       if (j <= 9):
               finalresult = random.choice(valuelist)
               if finalresult.text!="确定":
                  finalresult.click()
                  sleep(1)
               else:
                   pass
#点击确定
driver.find_element_by_xpath("//*[@id='keybordkeyboardBtn']/table/tbody/tr[4]/td[14]/span").click()
sleep(2)
#切换frame输出个人客户
driver.switch_to.parent_frame()
text=driver.find_element_by_css_selector("#portfolio > div.w > div > div.header_top > div > div.header_info_left > ul > li:nth-child(1) > a").text
sleep(1)
assert text=="个人客户"
print(text)
driver.switch_to.frame(0)
#点击登陆
driver.find_element_by_id("loginButton").click()
sleep(2)
driver.quit()