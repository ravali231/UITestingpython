import unittest

def setUpModule():#will be executed before executing any class or method present in the test class
    print("setup Module")

def tearDownModule():#will be executed after completing everything in the python module
    print("teardown Module")


class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self) -> None: #executes before all test methods
        print("This is login Test")

    @classmethod
    def tearDown(self) -> None: #executes after all test methods
        print("This is logout Test")

    @classmethod
    def setUpClass(cls) -> None:#execute once when the class started
        print("open Application")

    @classmethod
    def tearDownClass(cls) -> None:#execute once after the class completed
        print("Close Application")

    def test_search(self):
        print("This is search test")

    def test_advancedsearch(self):
        print("This is advanced search test")

    def test_prepaidRecharge(self):
        print("This is prepaid recharge")

    def test_postpaidRecharge(self):
        print("This is postpaid recharge")

if __name__ == "__main__":
    unittest.main()