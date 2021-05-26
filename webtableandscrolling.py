import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
"""
driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
rows = len(driver.find_elements_by_xpath("//table[@id='task-table']/tbody/tr"))
columns = len(driver.find_elements_by_xpath("//table[@id='task-table']/tbody/tr[1]/td"))

print("#"+"        "+"Task"+"      "+"Assignee"+"       "+"Status")

for r in range(1,rows+1):
    for c in range(1,columns+1):
        value = driver.find_element(By.XPATH,"//table[@id='task-table']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end='       ')
    print()

"""
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
#driver.execute_script("window.scrollBy(0,1000)","") #scroll down by pixel.

flag = driver.find_element_by_xpath("//td[contains(text(),'India')]")
#driver.execute_script("arguments[0].scrollIntoView();",flag) #Scroll with element.

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")#scroll down till page end


time.sleep(2)

driver.quit()