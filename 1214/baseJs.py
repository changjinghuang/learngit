#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-14 14:59
#@Author  : hcj
from time import sleep

from selenium import  webdriver
webchrome=webdriver.Chrome()
webchrome.get("https://www.zuche.com/")
# js="document.getElementById('fromDate').setAttribute('value','2019-12-16')"
js="document.getElementById('fromDate').setAttribute('value','2019-12-19')"
sleep(1)
webchrome.execute_script(js)
js2="document.getElementById('toDate').setAttribute('value','2019-12-19')"
webchrome.execute_script(js2)
