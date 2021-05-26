import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import  By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

inputboxes = driver.find_elements(By.CLASS_NAME,"text_field")
print(len(inputboxes))

driver.find_element(By.ID,"RESULT_TextField-1").send_keys("Ravali")
driver.find_element(By.ID,"RESULT_TextField-2").send_keys("Reddy")
driver.find_element(By.ID,"RESULT_TextField-3").send_keys("93493094")

status = driver.find_element(By.ID,"RESULT_TextField-1").is_displayed()
print("Is displayed ",status)

status1 = driver.find_element(By.ID,"RESULT_TextField-1").is_enabled()
print("Is Enabled ",status1)

driver.quit()