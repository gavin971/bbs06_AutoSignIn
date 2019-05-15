# =============================================================================
# Author: Gavin | Affiliation: NJU
# Email : Zhpfu.atm@gmail.com
# Last modified: 2019-05-15 18:31
# Filename: discuz_click.py
# Description: 1.气象家园自动签到脚本（签到+访问别人空间）
#              2.非静默方式,比较初级的版本
#              3.需要借助Chrome驱动模块
# =============================================================================
#-*- coding:utf-8 -*-
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


option = Options()
# option.add_argument('--headless')
# option.add_argument('--disable-gpu')

username=r"风往北吹"    #需要自己用户名修改
passwd="12345678"       #需要自己的密码修改
browser = webdriver.Chrome( chrome_options=option)
browser.get('http://bbs.06climate.com/forum.php')
print(browser.title)
browser.maximize_window()

elem=browser.find_element_by_id("ls_username").send_keys(username)
elem=browser.find_element_by_id("ls_password").send_keys(passwd)
elem=browser.find_element_by_id("ls_cookietime").click()
browser.find_element_by_xpath('/html/body/div[5]/div/div[1]/form/div/div[1]/table/tbody/tr[2]/td[3]/button/em').click()
time.sleep(1)


browser.find_element_by_xpath('/html/body/div[5]/div/div[1]/div/div/a/img').click()
time.sleep(1)


browser.find_element_by_xpath('/html/body/div[6]/div/div/div[3]/div[1]/div[2]/ul/li[1]/a/img').click()

browser.find_element_by_xpath('/html/body/div[6]/div/div/div[3]/div[1]/div[2]/ul/li[2]/a/img').click()

browser.find_element_by_xpath('/html/body/div[6]/div/div/div[3]/div[1]/div[2]/ul/li[3]/a/img').click()

browser.find_element_by_xpath('/html/body/div[6]/div/div/div[3]/div[1]/div[2]/ul/li[4]/a/img').click()
time.sleep(5)

# print(browser.window_handles)
browser.quit()

i = datetime.datetime.now()
print ("完成时间 %s" % i)
