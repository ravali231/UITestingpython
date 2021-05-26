import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import  By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
"""
#dropdown
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element(By.ID,"RESULT_RadioButton-9")
driver.execute_script("arguments[0].scrollIntoView();", element)

drpdown = Select(element)
#drpdown.select_by_visible_text("Morning")#by visible text

#drpdown.select_by_index(2)#by visible text
drpdown.select_by_value("Radio-2")#by visible text

#capture all options and print them as output
print(len(drpdown.options))
all_options = drpdown.options

for option in all_options:
    print(option.text)

#upload a file
driver.get("https://testautomationpractice.blogspot.com/")
driver.switch_to_frame(0)
element = driver.find_element(By.XPATH,"//input[@id='RESULT_FileUpload-10']")
driver.execute_script("arguments[0].scrollIntoView();",element)
element.send_keys("/home/ravali/Pictures/testpic.png")
"""
#download a file
driver.get("http://demo.automationtesting.in/FileDownload.html")
#driver.switch_to_frame(0)
element = driver.find_element(By.XPATH,"//textarea[@id='textbox']")
driver.execute_script("arguments[0].scrollIntoView();",element)
element.send_keys("testing text file")
driver.find_element(By.ID,"createTxt").click()
driver.find_element(By.ID,"link-to-download").click()
time.sleep(5)
element = driver.find_element(By.XPATH,"//textarea[@id='pdfbox']")
driver.execute_script("arguments[0].scrollIntoView();",element)
element.send_keys("testing pdf file")
driver.find_element(By.ID,"createPdf").click()
driver.find_element(By.ID,"pdf-link-to-download").click()

time.sleep(5)
driver.quit()