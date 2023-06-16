# 20200920 PYTHON
#通識講座自動零時差報名

from selenium.webdriver.common.keys import Keys


import time
from selenium import webdriver  

opt =  webdriver.ChromeOptions()      
opt.add_experimental_option('prefs',  {'profile.default_content_setting_values': {'notifications' : 2}})

browser = webdriver.Chrome(options = opt)    



browser.get('https://aps.ncue.edu.tw/sign_up/login.php')

browser.find_element_by_xpath("//input[@type='radio'][@name='auth_type'][@value='1']").click()
browser.find_element_by_name('p_usr').send_keys('S0761030') #}輸入自己的帳號
browser.find_element_by_name('p_pwd').send_keys('000000000') #}輸入自己的密碼
browser.find_element_by_name('log').click()       
time.sleep(3)
browser.get('https://aps.ncue.edu.tw/sign_up/sign_app.php?crs_seq=41913&object=1')
time.sleep(3)
browser.find_element_by_name("Value").send_keys(Keys.ENTER)
