
#Importing the libraries required for performing the unit-testing
import unittest
import Test_Func

"""
Defining the 3-Test Cases for the Address Book application
"""
class TestStringMethod(unittest.TestCase):

    """
    Will check for the user name and will the return the alert message therein if the test fails in any way.

    """
    def test_name(self):
        name,_,_ = Test_Func.testing_fun('Manish', 'Subhash Road' , 9822097072)
        self.assertEqual(name, 'Manish', msg="Please enter the string properly")

    """
    Will check for the user address and will the return the alert message therein if the test fails in any way.
    It will give the proper details 

    """

    def test_address(self):
        _, address, _ = Test_Func.testing_fun('Manish', 'Subhash Road', 9822097072)
        self.assertEqual(address, 'Subhash Road',msg='Enter the correct address')

    """
    Will check for the user contact details and will the return the alert message therein if the test fails in any way.

    """
    def test_phone(self):
        _,_, phone = Test_Func.testing_fun('Manish', 'Subhash Road', 8605325747)
        self.assertGreaterEqual(len(str(phone)), 10, 'Please enter the contact number carefully')

if __name__ == '__main__':
    unittest.main()