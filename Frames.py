import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import  By


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?deprecated-list.html")
driver.switch_to.frame("packageListFrame")#switching to first frame
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
time.sleep(2)
driver.switch_to.default_content()##switching to main frame
driver.switch_to.frame("packageFrame")#switching to second frame
driver.find_element(By.LINK_TEXT,"WebDriver").click()
time.sleep(2)
driver.switch_to.default_content()##switching to main frame
driver.switch_to.frame("classFrame")#switching to second frame
driver.find_element(By.XPATH,"(//a[contains(text(),'Deprecated')])[1]").click()
time.sleep(2)
driver.switch_to.default_content()##switching to main frame
time.sleep(2)#python wait
#start work from 2:36:06 windowhandles.

driver.quit()
