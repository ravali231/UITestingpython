import unittest

#skiptests
#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

"""
class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("This is search test")

    @unittest.skip("I am skipping this test because it is not yet ready")
    def test_advancedsearch(self):
        print("This is advanced search test")

    @unittest.skipIf(1==1,"One is equal to one")
    def test_prepaidRecharge(self):
        print("This is prepaid recharge")

    def test_postpaidRecharge(self):
        print("This is postpaid recharge")

    def test_loginbygmail(self):
        print("This is login by gmail")

    def test_logoutbygmail(self):
        print("This is logout by gmail")

if __name__ == "__main__":
    unittest.main()
"""

class Test(unittest.TestCase):
    def testName(self):
        #relational operator
        self.assertGreater(100,10)
        self.assertGreaterEqual(100, 100)

        self.assertLess(10,100)
        self.assertLessEqual(100,100)


        '''
        list = {"python","selenium", "java"}
        #self.assertIn("python",list)#passed
        #self.assertIn("ruby", list)#failed

        self.assertNotIn("ruby",list) #passed
        self.assertNotIn("python", list)#failed
        '''



       # self.driver= None
        #self.driver = webdriver.Chrome(ChromeDriverManager().install())
        '''
        self.driver.maximize_window()
        self.driver.get("https://www.google.com")
        webpagetitle = self.driver.title
        '''
        #assertEqual
        #self.assertEqual("Google123",webpagetitle,"Webpage title doesn't matches")
        #self.assertNotEqual("Google123",webpagetitle)
        #self.assertTrue( webpagetitle == "Google123") #True
        #self.assertFalse(webpagetitle == "Google") #False

       # self.assertIsNone(self.driver) #driver is none true
        #self.assertIsNotNone(self.driver)





    if __name__ == "__main__":
        unittest.main()