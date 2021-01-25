import unittest
import json
from app.test.base import BaseTestCase
from app.main.service.payment_helper import CreditCardValidation



class TestCreditCardValidation(BaseTestCase):

    def test_card_number_validation(self):
        """ Test for true card number input"""
        self.assertTrue(CreditCardValidation().card_number('5893804115457289'))

    def test_card_number_validation2(self):
        """ Test for wrong card number input"""
        self.assertFalse(CreditCardValidation().card_number('5893804115457288'))

    def test_expiration_date(self):
        """ Test for true expiration date input"""
        self.assertTrue(CreditCardValidation().expiration_date('2021-10-01'))

    def test_expiration_date2(self):
        """ Test for wrong expiration input"""
        self.assertFalse(CreditCardValidation().expiration_date('2021-01-01'))

    def test_amount(self):
        """ Test for true amount input"""
        self.assertTrue(CreditCardValidation().amount(55))

    def test_amount2(self):
        """ Test for wrong amount input"""
        self.assertFalse(CreditCardValidation().expiration_date(-10))



if __name__ == '__main__':
    unittest.main()