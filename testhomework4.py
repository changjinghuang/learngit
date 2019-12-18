#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-16 14:35
#@Author  : hcj
import random
from time import sleep
from selenium import  webdriver
from selenium.webdriver import ActionChains

driver =webdriver.Chrome()
url="http://121.40.156.59:8080/javamall/admin/backendUi!main.do"
driver.get(url)
sleep(3)
driver.delete_all_cookies()
cookie={"name":"JSESSIONID","value":"0520797051414D26935E41DFC6869E92"}
# cookie = {'name':'JSESSIONID','value':'1CA5804C38D14E200AB1DAF14178BAFF'}
driver.add_cookie(cookie)
sleep(1)
driver.get(url)
#点击设置管理
driver.find_element_by_xpath("//*[@id='parent43']/a/div[4]").click()
sleep(2)
#点击管理员管理
driver.find_element_by_xpath("//*[@id='43']/div/ul/li[4]/ul/li[1]/a").click()
sleep(2)
#点击管理员添加按钮
driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='58']/iframe"))
sleep(2)
driver.find_element_by_link_text("添加").click()
sleep(1)
#输入用户名
driver.find_element_by_xpath("//*[@id='addAdminForm']/table/tbody/tr[1]/td/input").send_keys(random.choice(["haha","null","空"]))
password=random.sample("12345678902#%^&@#qwertyuiop",8)
print(password)
#输入密码
driver.find_element_by_id("pwd").send_keys(password)
#输入确认密码
driver.find_element_by_id("repwd").send_keys(password)
#随机选择类型
list=["notSuperChk"]
i=random.choice(list)
print(i)
driver.find_element_by_id(i).click()
#随机选择角色
sleep(1)
if "not" in i:
     num=[1,2,3,4,5]
     choicenum=random.choice(num)
     print(choicenum)
     resultnum=random.sample(num, choicenum)
     print(resultnum)
     # // *[ @ id = "rolesbox"] / li[1] / input
     for kt in range(1,len(resultnum)+1):
        xpathnum="// *[ @ id = 'rolesbox'] / li["+str(kt)+"]/ input"
        print(xpathnum)
        sleep(1)
        driver.find_element_by_xpath(xpathnum).click()
        sleep(1)
#随机获取状态
button=[1,2]
sleep(1)
lastresult=random.choice(button)
xpath="//*[@id='addAdminForm']/table/tbody/tr[6]/td/input["+str(lastresult)+"]"
driver.find_element_by_xpath(xpath).click()
#输入姓名
sleep(1)
driver.find_element_by_name("adminUser.realname").send_keys(random.choice(["小王","小石","小花"]))
#输入编号
sleep(1)
driver.find_element_by_xpath("//*[@id='addAdminForm']/table/tbody/tr[8]/td/input").send_keys(random.sample("1234567890",5))
sleep(2)
#输入部门
driver.find_element_by_name("adminUser.userdept").send_keys(random.choice(["测试部门","销售部","业务部"]))
sleep(1)
#输入备注
driver.find_element_by_name("adminUser.remark").send_keys("adfasfsafsaf")
sleep(1)
#点击确定
driver.find_element_by_xpath("//*[@id='useradmininfo']/div[2]/a[1]/span/span").click()
sleep(2)
#切换frame
driver.switch_to.default_content()
driver.find_element_by_xpath("//*[@id='parent43']/a/div[4]").click()
sleep(2)
#点击发货信息管理
driver.find_element_by_xpath("//*[@id='43']/div/ul/li[3]/ul/li[2]/a").click()
sleep(2)
anthorframe=driver.find_element_by_xpath("//*[@id='56']/iframe")
#driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='58']/iframe"))
driver.switch_to.frame(anthorframe)
#点击添加
sleep(2)
driver.find_element_by_xpath("//*[@id='tb']/a[1]").click()
sleep(2)
#发货地址
driver.find_element_by_name("dlyCenter.name").send_keys("aaaa")
sleep(1)
#发货人
driver.find_element_by_id("url").send_keys("cccd")
#性别
driver.find_element_by_xpath("//*[@id='sex']").click()
#地区
sleep(2)
#邮编
driver.find_element_by_xpath("//*[@id='dlyCenterForm']/table/tbody/tr[3]/td[2]/input").send_keys("4012222")
sleep(1)
#手机号码
driver.find_element_by_xpath("//*[@id='dlyCenterForm']/table/tbody/tr[4]/td[1]/input").send_keys("13817141700")
sleep(1)
#电话
driver.find_element_by_name("dlyCenter.phone").send_keys("021-68091145")
sleep(1)
#地址
driver.find_element_by_name("dlyCenter.address").send_keys("浦东新区")
#保存
driver.find_element_by_xpath("//*[@id='divdia']/div[2]/a/span/span").click()
sleep(2)
#默认地址
#driver.find_element_by_name("is_default").click()
# //*[@id="is_default_dc"]
# # driver.find_element_by_xpath("//*[@id='is_default_dc']").is_selected()
# defaultaddress=driver.find_element_by_xpath("//*[@id='is_default_dc']")
# ActionChains(driver).move_to_element(defaultaddress).perform()
print(driver.find_element_by_xpath("//*[@id='is_default_dc']").is_displayed())
js = "document.getElementsByName('dlyCenter.choose').setAttribute('type','text')"
driver.execute_script(js)
driver.find_element_by_xpath("//*[@id='is_default_dc']").click()
sleep(3)
#备注
driver.find_element_by_name("dlyCenter.memo").send_keys("adafdasfadsfasdfadfafasffdfasf")
sleep(2)
driver.quit()
