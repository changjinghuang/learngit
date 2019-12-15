#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-09 13:55
#@Author  : hcj
from time import sleep
from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import win32api
import win32con
driver = webdriver.Chrome()
driver.maximize_window()
#循环打开百度新闻等链接
# newtext=driver.find_element_by_link_text("新闻")
#点击百度新闻打开新的tab方法一通过添加js属性target实现:
# # ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_down(Keys.CONTROL).perform()
# js = "var el = document.getElementsByName('tj_trnews')[0];" \
#      "el.setAttribute('target','_blank');"
# driver.execute_script(js)
# newtext.click()
#点击百度新闻打开新的tab方法二通过鼠标右键点击t实现:
VK_CODE ={'enter':0x0D, 'down_arrow':0x28}
#键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)
#键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)
def baiduUrlTest(a):
    driver.get("http://baidu.com")
    sleep(2)
    #鼠标移动到新闻上，右键点击
    newtext=driver.find_element_by_link_text(a)
    sleep(1)
    action=ActionChains(driver).move_to_element(newtext)
    sleep(1)
    action.context_click(newtext).perform()
    sleep(1)
    #按下T
    win32api.keybd_event(0x0d, 0, 0, 0)
    win32api.keybd_event(0x0d, 0, win32con.KEYEVENTF_KEYUP, 0)
    sleep(1)
    #按enter
    keyDown("enter")
    keyUp("enter")
    sleep(2)

#keys方法不能对浏览器的弹窗做操作。
# # actionOpenLinkInNewTab.keyDown(Keys.CONTROL).sendKeys("t").keyUp(Keys.CONTROL).perform();
# # ActionChains(driver).move_to_element_with_offset(newtext,10,10)
# # ActionChains(driver).key_down(Keys.).key_up(Keys.CONTROL).perform()
# # ActionChains(driver).key_down(Keys.ENTER).perform()
# # newtext.send_keys(Keys.)
# sleep(3)
#校验是否进入新闻页面
# newtext=driver.find_element_by_link_text("国内").text
# assert newtext=="国内"
# print("newtext")
# sleep(4)
#依次打开百度标签
baiduUrlTest("新闻")
baiduUrlTest("hao123")
baiduUrlTest("地图")
baiduUrlTest("视频")
baiduUrlTest("贴吧")
baiduUrlTest("学术")
windowhandles=driver.window_handles
for windowhandle in windowhandles:
    driver.switch_to.window(windowhandle)
    if "百度新闻" in driver.title:
        newtext=driver.find_element_by_partial_link_text("娱乐").text
        assert "百度新闻" in driver.title
        assert "娱乐"==newtext
        print(driver.title)
        print(newtext)
    elif "hao123" in driver.title:
        haotext=driver.find_element_by_partial_link_text("国际在线").text
        assert "hao123"in driver.title
        assert "国际在线"==haotext
        print(driver.title)
        print(haotext)
    elif "百度地图" in driver.title:
        assert "百度地图"in driver.title
        print(driver.title)
    elif "百度视频" in driver.title:
        videotext=driver.find_element_by_partial_link_text("搞笑").text
        assert "搞笑" ==videotext
        assert "百度视频" in driver.title
        print(driver.title)
        print(videotext)
    elif "百度贴吧" in driver.title:
        tietext=driver.find_element_by_partial_link_text("高级搜索").text
        assert "高级搜索" ==tietext
        assert "百度贴吧" in driver.title
        print(driver.title)
    elif "百度学术" in driver.title:
        # studytext=driver.find_element_by_class_name("s_btn").text
        # assert "百度以下"
        assert "保持学习的态度" in driver.title
        print(driver.title)
        # print(studytext)
    else:
        print("没有此页面")
driver.quit()