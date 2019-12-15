import time
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.implicitly_wait(6)
#
# driver.get("http://www.baidu.com/")
# time.sleep(1)
# # driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
# driver.find_element_by_css_selector("#u1 > a.lb").click()
# time.sleep(1)
#
# driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_8__submit']").click()
# # # 断言方法一
# # try:
# #     error_message = driver.find_element_by_xpath(
# #         "//*[@id='TANGRAM__PSP_8__error' and text()='请您填写手机/邮箱/用户名']").is_displayed()
# #     print("Test pass. the error message is display.")
# # except Exception as e:
# #     print("Test fail.", format(e))
#
# # 断言方法二，本文重点介绍方法
# error_mes = driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_8__error']").text
#
# assert error_mes == u'请您填写手机/邮箱/用户名'
# print('Test pass.')

# from selenium import webdriver
#
# driver = webdriver.Firefox()
#
# driver.get("http://www.baidu.com")
#
# js = 'document.getElementById("setf").target="";'
#
# driver.execute_script(js)
#
# driver.find_element_by_id("setf").click()
#
# driver.find_element_by_link_text("百度首页").click()



from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
time.sleep(2)

# 定位 新闻
element = driver.find_element_by_name('tj_trnews')

# js 语句， 定义一个变量el，并且给其赋值 新闻 元素
# 对 el 进行 target='_blank' 属性设置
js = "var el = document.getElementsByName('tj_trnews')[0];" \
     "el.setAttribute('target','_blank');"

# 移除属性 target，使访问的页面在当前页面打开
# el.removeAttribute("target");

# driver 执行 js 语句
driver.execute_script(js)

element.click()

# driver.quit()