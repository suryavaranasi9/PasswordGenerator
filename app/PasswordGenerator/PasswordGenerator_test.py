#!/usr/bin/env Python3
"""
Tests the generate_password() function within password generator
"""
from app.PasswordGenerator.pwdg2 import PasswordGenerator
import unittest


class TestPasswordGenerator(unittest.TestCase):  # inherits from unittest.TestCase

    def test_symbols(self):
        """Tests the use of symbols within the password generation"""

        symbols = ['!', '@', '#', '$', '%', '&', '?']

        pwd1 = PasswordGenerator().generate_password(10, False, True, True,5)  # to test without symbols
        pwd2 = PasswordGenerator().generate_password(32, True, True, True,3)  # to test with symbols

        # Check if lengths were computed properly
        test_case1 = len(pwd1) == 10  # check to see if the length is 10
        test_case2 = len(pwd2) == 32  # check to see if the length is 10

        for symbol in symbols:
            if symbol in pwd1:  # check to see if the password contains symbols
                test_case1 = False
                break

        for symbol in symbols:
            if symbol in pwd2:  # check to see if the password contains symbols
                test_case2 = True
                break

        self.assertEqual(test_case1 is True, test_case2 is True)  # evaluate if both tests are true

    def test_numbers(self):
        """Tests the use of numbers within the password generation"""

        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        pwd1 = PasswordGenerator().generate_password(46, True, False, True,3)  # to test without numbers
        pwd2 = PasswordGenerator().generate_password(15, True, True, True,6)  # to test with  numbers

        # Check if lengths were computed properly
        test_case1 = len(pwd1) == 46  # check to see if the length is 10
        test_case2 = len(pwd2) == 15  # check to see if the length is 10

        for number in numbers:
            if number in pwd1:  # check to see if the password contains numbers
                test_case1 = False  # password should not contain numbers
                break

        for number in numbers:
            if number in pwd2:  # check to see if the password contains numbers
                test_case2 = True  # password should contain numbers
                break

        self.assertEqual(test_case1 is True, test_case2 is True)  # evaluate if both tests are true

    def test_letters(self):
        """Tests the use of letters within the password generation"""

        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                   'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u', 'v', 'w', 'x', 'y', 'z']

        pwd1 = PasswordGenerator().generate_password(32, True, True, False,8)  # to test without letters
        pwd2 = PasswordGenerator().generate_password(21, True, True, True,2)  # to test with letters

        # Check if lengths were computed properly
        test_case1 = len(pwd1) == 32
        test_case2 = len(pwd2) == 21

        for letter in letters:
            if letter in pwd1:  # check to see if the password contains letters
                test_case1 = False  # password should not contain letters
                break

        for letter in letters:
            if letter in pwd2:  # check to see if the password contains letters
                test_case2 = True  # password should contain letters
                break

        self.assertEqual(test_case1 is True, test_case2 is True)  # evaluate if both tests are true

    def test_none(self):
        """Tests the case of providing none of the options """

        pwd1 = PasswordGenerator().generate_password(10, False, False, False,5)  # to test without any options

        self.assertTrue(pwd1 == 'Cannot Generate password')  # evaluate if both tests are true
    
    def test_num_of_passwords(self):
        """Tests the case of providing Zero number of passwords for output"""
        
        pwd1 = PasswordGenerator().generate_password(20, False, True, False,0) # to test zero pass outputs
        
        self.assertTrue(pwd1 == 'Empty Password Strings') # evaluate if both tests are true
    
    def test_length_exceed(self):
        """Tests the case where password limit is NOT less than or equal to 200"""
        message = "First value and second value are not equal !"
        pwd1 = PasswordGenerator().generate_password(201, True, False, True,3) #to test without numbers
        firstValue = pwd1 
        secondValue = "Password generated"
        print(pwd1)
        
        self.assertEqual(firstValue, secondValue, message)
   
    def test_length_numPass(self):
        """Negative Test Case where length > 200 and Numof pass <0"""
        pwd1 = PasswordGenerator().generate_password(201, False, True, False,-1)
        
        self.assertTrue(pwd1 == 'Empty Password Strings')
    
    def test_negative_value_length(self):
        """"Test case for Negative value of length of password"""
        message = "First value and second value are not equal !"
        pwd1 = PasswordGenerator().generate_password(-1, False, True, False,3)
        
        self.assertEqual(pwd1,'Cannot Generate password',message)


if __name__ == '__main__':
    unittest.main()
