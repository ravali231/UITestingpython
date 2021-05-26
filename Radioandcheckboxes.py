import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import  By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

status = driver.find_element(By.ID,"RESULT_RadioButton-7_0").is_selected()
print(status)

element = driver.find_element(By.XPATH,"//input[@id='RESULT_RadioButton-7_0']")
"""
actions = ActionChains(driver)
actions.move_to_element(element).perform()"""

driver.execute_script("arguments[0].scrollIntoView();", element)
driver.execute_script("arguments[0].click();", element)

#element.click()

status = driver.find_element(By.ID,"RESULT_RadioButton-7_0").is_selected()
print(status)
sunday = driver.find_element(By.XPATH,"//input[@id='RESULT_CheckBox-8_0']")
driver.execute_script("arguments[0].click();", sunday)
saturday = driver.find_element(By.XPATH,"//input[@id='RESULT_CheckBox-8_6']")
driver.execute_script("arguments[0].click();", saturday)
time.sleep(5)

driver.quit()