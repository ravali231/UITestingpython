from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import XLUtils
from selenium.webdriver.common.by import  By

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("http://demo.guru99.com/test/newtours/")

path = "/home/ravali/Downloads/badge_44_accounts.csv"
rows = XLUtils.getRowCount(path,'Sheet1')
for r in range(2,rows+1):
    username = XLUtils.readData(path,'Sheet1',r,1)
    password = XLUtils.readData(path, 'Sheet1', r, 2)

    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_name("login").click()

    if driver.title=="Find a Flight: Mercury Tours:":
        print("Test is passed")
        XLUtils.writeData(path,"Sheet1",r,3,"test passed")
    else:
        print("Test is Failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test failed")

    driver.find_element_by_link_text("Home").click()