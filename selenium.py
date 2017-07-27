#!/usr/bin/env python
# -*- coding:utf-8 -*-


import selenium
from selenium.webdriver.common.keys import Keys

driver=ellenium.webdriver.PhantomJS()

#获取网址
driver.get("https://www.douban.com/accounts/login")
driver.save_screenshot("D:/douban.png")

#输入账号密码
driver.find_element_by_name("form_email").send_keys("123456")
driver.find_element_by_name("form_password").send_keys("666666")

#模拟登陆
driver.find_element_by_name("login").click()

driver.save_screenshot("D:/login.png")

