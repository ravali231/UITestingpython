import unittest

class loginTest(unittest.TestCase):
    def test_loginbyEmail(self):
        print("This is login by email test")
        self.assertTrue(True)

    def test_loginbyFacebook(self):
        print("This is login by fb test")
        self.assertTrue(True)

    def test_loginbyTwitter(self):
        print("This is login by Twitter test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()


