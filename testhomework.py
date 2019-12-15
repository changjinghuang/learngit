#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-07 18:29
#@Author  : hcj
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import random
driver=webdriver.Chrome()
#打开百度页面
driver.get("http://baidu.com/")
#获取设置元素位置
setting=driver.find_element_by_link_text("设置")
#鼠标移动到设置上
ActionChains(driver).move_to_element(setting).perform()
#获取高级搜索元素并且进行点击操作
highsearch=driver.find_element_by_link_text("高级搜索").click()
# driver.switch_to.frame()
sleep(1)
#循环获取和输入搜索结果需要包含的关键字
for i in range(1,5):
    if(i<=3):
        adv_keyword=driver.find_element_by_name("q"+str(i))
        adv_keyword.send_keys("selenium")
        sleep(1)
    else:
         adv_keyword2=driver.find_element_by_name("q"+str(i))
         adv_keyword2.send_keys("广告")
         sleep(1)

sleep(1)
#获取时间下拉列表里的值
select=driver.find_element_by_name("gpc")
result=Select(select)
opt=[]
options=result.options
for option in options:
    optiona=option.text
    opt.append(optiona)
Select(select).select_by_visible_text(random.choice(opt))

#获取文档下拉列表里的值
select2=driver.find_element_by_name("ft")
listSelect=Select(select2).options
listsel=[]
for L in listSelect:
    atext=L.text
    listsel.append(atext)
Select(select2).select_by_visible_text(random.choice(listsel))
#随机点击关键字
list = []
for i in range(0,3):
   list.append("q5_"+str(i))
result=random.choice(list)
driver.find_element_by_id(result).click()
sleep(1)
#站内搜索元素的获取和输入操作
input=driver.find_element_by_name("q6")
input.send_keys("baidu.com")
#点击高级搜索按钮
driver.find_element_by_class_name("advanced-search-btn").click()
sleep(2)
driver.quit()






