import unittest
from Package1.TC_LoginTest import loginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturnsTest import PaymentReturnsTest

#Get all Testcases from Package1,Package2
tc1= unittest.TestLoader().loadTestsFromTestCase(loginTest)
tc2= unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3= unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4= unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

#creating Test suites
sanityTestSuite = unittest.TestSuite([tc1,tc2])
functionalTestSuite = unittest.TestSuite([tc3,tc4])
masterTestSuite = unittest.TestSuite([tc1,tc2,tc3,tc4])


unittest.TextTestRunner(verbosity=2).run(masterTestSuite)
#unittest.TextTestRunner().run(functionalTestSuite)
#unittest.TextTestRunner().run(sanityTestSuite)
#pytest -v -s {testfilename) toget detailed output
#@pytest.yield_fixture()--Before and after(setupandteardown methods)





