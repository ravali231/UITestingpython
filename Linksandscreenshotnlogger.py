import time
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import  By

"""
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()

#links
driver.get("http://demo.guru99.com/test/newtours/")
#get all links in page
links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))
#iterate all links to get text of all links
for link in links:
    print(link.text)

# link text
#driver.find_element(By.LINK_TEXT,"REGISTER").click()
#partial link text
driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()

#screenshot
driver.get("http://demo.guru99.com/test/newtours/")
#save screenshot
#driver.save_screenshot("/home/ravali/Autotesting/screenshots/homePage.png")
#get screenshot

driver.get_screenshot_as_file("/home/ravali/Autotesting/screenshots/homePage2.png")
"""

logging.basicConfig(filename="/home/ravali/Autotesting/seleniumlogs/test.log",format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S:%P')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")

#time.sleep(3)
#driver.quit()
