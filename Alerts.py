import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import  By


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()

time.sleep(3)
#alert accept
#driver.switch_to_alert().accept()
#alert dismiss
driver.switch_to_alert().dismiss()
time.sleep(3)
driver.quit()