import unittest

#Sample test
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

"""
class Test(unittest.TestCase):
    def test_FirstTest(self):
        print("This is my first unit testcase")

if __name__== "__main__":
    unittest.main()
"""
class SearchEngineTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.driver.maximize_window()
        self.driver.get("https://www.google.com")
        print(self.driver.title)

    def test_Bing(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.driver.maximize_window()
        self.driver.get("https://www.bing.com")
        print(self.driver.title)

if __name__ == "__main__":
    unittest.main()

