import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import  By


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.current_window_handle)

driver.find_element(By.XPATH,"//div[@id='Tabbed']/a/button").click()
print(driver.current_window_handle)

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    print(driver.current_window_handle)

    if(driver.title=="Frames & windows"):
        driver.close()

driver.quit()
