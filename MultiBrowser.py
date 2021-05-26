from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#driver=None
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Firefox(GeckoDriverManager().install())
#driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://newtours.demoaut.com/")
print(driver.title)
print(driver.current_url)
driver.close()