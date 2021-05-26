import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
"""
#mousehover actions
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@id='txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()
time.sleep(2)
admin = driver.find_element(By.XPATH,"//a[@id='menu_admin_viewAdminModule']")
usermanagement = driver.find_element(By.XPATH,"//a[@id='menu_admin_UserManagement']")
users = driver.find_element(By.XPATH,"//a[@id='menu_admin_viewSystemUsers']")

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(usermanagement).move_to_element(users).click().perform()

# double click
driver.get("https://testautomationpractice.blogspot.com/")
actions = ActionChains(driver)
element = driver.find_element(By.XPATH,"//button[@ondblclick='myFunction1()']")
actions.double_click(element).perform()

# right click
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
actions = ActionChains(driver)
element = driver.find_element(By.XPATH,"//span[contains(text(),'right click me')]")
actions.context_click(element).perform()
"""
# drag and drop
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

source_element = driver.find_element(By.XPATH,"//div[@id='box6']")
target_element = driver.find_element(By.XPATH,"//div[@id='box106']")

actions = ActionChains(driver)
actions.drag_and_drop(source_element,target_element).perform()

time.sleep(2)
driver.quit()