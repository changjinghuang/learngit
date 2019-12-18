#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-16 14:34
#@Author  : hcj
from time import sleep

from selenium import  webdriver
class test_ui():
    #构建函数
    def __init__(self,brower,tbody):
        self.brower=brower
        self.tbody=tbody
    #获取文本信息
    def get_call_text(self,column):
        result=[]
        for i in range(2,5):
             #// *[ @ id = "table"] / tbody / tr[2] / td[2]
             xpath=self.tbody+'/tr['+str(i)+']/td['+str(column)+']'
             text=self.brower.find_element_by_xpath(xpath).text
             result.append(text)
        return result
    #统计总数
    def sum_total_price(self,result):
        i=0
        for j in range(len(result)):
            i+=int(result[j])
        return i
    #获取文案总数
   # // *[ @ id = "table"] / tbody / tr[5] / th[2]
    #// *[ @ id = "table"] / tbody / tr[5] / th[3]
    def total_price(self,i):
          xpath=self.tbody+'/tr[5]/th['+str(i)+']'
          # xpath = self.tbody + '/tr[' + str(i) + ']/td[' + str(column) + ']'
          return self.brower.find_element_by_xpath(xpath).text
    def assertresult(self,realresult,actualresult):
        if int(realresult)==int(actualresult):
            print("一月输出正确")
        else:
            print("二月计算错误")
            print("计算为%s"%realresult)
            print("展示为%s"%actualresult)
            print("误差为%s"%(int(actualresult)-int(realresult)))

driver=webdriver.Chrome()
url="file:///C:/Users/changjing/Desktop/testtable.html"
driver.get(url)
tbody="//*[@id='table']/tbody"
table=test_ui(driver,tbody)
i=2
while i<4:
    result=table.get_call_text(i)
    realtotalnum=table.sum_total_price(result)
    acualtotalnum=table.total_price(i)
    table.assertresult(realtotalnum,acualtotalnum)
    i+=1
sleep(2)
driver.quit()