#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-14 13:39
#@Author  : hcj
from time import sleep
from selenium import  webdriver
webchrome=webdriver.Chrome()
webchrome.get("file:///C:/Users/changjing/Desktop/css.html")
print(webchrome.find_elements_by_css_selector("#recordlist>li+li+li"))
print(webchrome.find_elements_by_css_selector("#recordlist >p:nth-child(1)"))

webchrome.find_element_by_css_selector("recordlist")
#