import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("http://demo.guru99.com/test/newtours/")
user_ele = driver.find_element_by_name("userName")

print(user_ele.is_enabled())
print(user_ele.is_displayed())

user_pass = driver.find_element_by_name("password")

print(user_pass.is_enabled())
print(user_pass.is_displayed())

user_ele.send_keys("mercury")
user_pass.send_keys("mercury")

driver.find_element_by_name("submit").click()
time.sleep(5)
roundtrip_radio = driver.find_element_by_xpath("//input[@value='roundtrip']")
print("round trip",roundtrip_radio.is_selected())
oneway_radio = driver.find_element_by_xpath("//input[@value='oneway']")
print("one way",oneway_radio.is_selected())


driver.close()

driver.quit()


