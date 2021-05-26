import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
time.sleep(5)
driver.get("http://pavantestingtools.blogspot.in/")
print(driver.title)
time.sleep(5)
driver.back()
print(driver.title)
time.sleep(5)
driver.forward()
print(driver.title)

driver.close()