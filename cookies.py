import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import  By


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://www.amazon.in")
#capture all cookies created by browser
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
#Adding new cookie to browser
cookie = {'name':'mycookie','value':'123456'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
#deleting cookie
driver.delete_cookie('mycookie')
print(len(cookies))
driver.delete_all_cookies()#delete all cookies
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)


#start from 5:47:05
driver.quit()