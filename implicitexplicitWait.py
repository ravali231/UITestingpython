import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import  By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
#implicit wait
"""
driver.get("http://demo.guru99.com/test/newtours/")

driver.implicitly_wait(10)

assert "Welcome: Mercury Tours" in driver.title

user_ele = driver.find_element_by_name("userName")

user_pass = driver.find_element_by_name("password")


user_ele.send_keys("mercury")
user_pass.send_keys("mercury")

driver.find_element_by_name("submit").click()
"""
#Explicit wait

driver.get("https://www.expedia.com/")

driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.XPATH,"(//a[@role='tab'])[2]").click()

driver.find_element(By.XPATH,"//button[@aria-label='Leaving from']").send_keys("SFO")
time.sleep(5)
driver.find_element(By.XPATH,"(//ul[@data-stid='location-field-leg1-origin-results']/li/button)[1]").click()

driver.find_element(By.XPATH,"//button[@aria-label='Going to']").send_keys("NYC")
time.sleep(5)

driver.find_element(By.XPATH,"(//ul[@data-stid='location-field-leg1-destination-results']/li/button)[1]").click()

#driver.find_element(By.XPATH,"//button[@id='d1-btn']").clear()
time.sleep(5)
driver.find_element(By.XPATH,"//button[@id='d1-btn']").send_keys("05/27/2021")
#driver.find_element(By.XPATH,"//button[@id='d1-btn']").clear()
time.sleep(5)

driver.find_element(By.XPATH,"//button[@id='d2-btn']").send_keys("05/28/2021")

driver.find_element(By.XPATH,"//button[@type='submit']").click()

#Explicit wait
wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,"(//span[@class='uitk-switch-control'])[4]")))
driver.execute_script("arguments[0].click();", element)

#element.click()
time.sleep(3)

driver.close()

driver.quit()


