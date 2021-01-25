import unittest
import json
from app.test.base import BaseTestCase


def cheap_gateway_payment(self):
    return self.client.post(
        '/payment/',
        data=json.dumps({
                        "CreditCardNumber": "5893804115457289",
                        "CardHolder": "Mostafa",
                        "ExpirationDate": "2021-10-01",
                        "SecurityCode": "4585454",
                        "Amount": 2
                            }),
        content_type='application/json'
    )


def expensive_gateway_payment(self):
    return self.client.post(
        '/payment/',
        data=json.dumps({
                        "CreditCardNumber": "5893804115457289",
                        "CardHolder": "Mostafa",
                        "ExpirationDate": "2021-10-01",
                        "SecurityCode": "4585454",
                        "Amount": 22
                            }),
        content_type='application/json'
    )



def premium_gateway_payment(self):
    return self.client.post(
        '/payment/',
        data=json.dumps({
                        "CreditCardNumber": "5893804115457289",
                        "CardHolder": "Mostafa",
                        "ExpirationDate": "2021-10-01",
                        "SecurityCode": "4585454",
                        "Amount": 2222
                            }),
        content_type='application/json'
    )



def wrong_expire_date(self):
    return self.client.post(
        '/payment/',
        data=json.dumps({
                        "CreditCardNumber": "5893804115457289",
                        "CardHolder": "Mostafa",
                        "ExpirationDate": "2021-01-01",
                        "SecurityCode": "4585454",
                        "Amount": 2222
                            }),
        content_type='application/json'
    )


def wrong_credit_card_number(self):
    return self.client.post(
        '/payment/',
        data=json.dumps({
                        "CreditCardNumber": "5893804115457288",
                        "CardHolder": "Mostafa",
                        "ExpirationDate": "2021-01-01",
                        "SecurityCode": "4585454",
                        "Amount": 2222
                            }),
        content_type='application/json'
    )


def wrong_amount(self):
    return self.client.post(
        '/payment/',
        data=json.dumps({
                        "CreditCardNumber": "5893804115457288",
                        "CardHolder": "Mostafa",
                        "ExpirationDate": "2021-01-01",
                        "SecurityCode": "4585454",
                        "Amount": -100
                            }),
        content_type='application/json'
    )


class TestPaymentProcess(BaseTestCase):

    def test_cheap_gateway(self):
            """ Test for cheap gateway"""
            with self.client:
                # user registration
                payment_response = cheap_gateway_payment(self)
                response_data = json.loads(payment_response.data.decode())
                # self.assertTrue(response_data['Authorization'])
                self.assertEqual(payment_response.status_code, 200)
                self.assertEqual(response_data['message'], 'payment successfull ( cheap gateway) ')

    def test_expensive_gateway(self):
            """ Test for expensive gateway """
            with self.client:
                # user registration
                payment_response = expensive_gateway_payment(self)
                response_data = json.loads(payment_response.data.decode())
                # self.assertTrue(response_data['Authorization'])
                self.assertEqual(payment_response.status_code, 200)
                self.assertEqual(response_data['message'] ,'payment successfull ( expensive gateway) ')


    def test_premium_gateway(self):
            """ Test for premium gateway"""
            with self.client:
                # user registration
                payment_response = premium_gateway_payment(self)
                response_data = json.loads(payment_response.data.decode())
                # self.assertTrue(response_data['Authorization'])
                self.assertEqual(payment_response.status_code, 200)
                self.assertEqual(response_data['message'] ,'payment successfull ( premium gateway) ')

    def test_wrong_expire_date(self):
            """ Test for premium gateway"""
            with self.client:
                # user registration
                payment_response = wrong_expire_date(self)
                response_data = json.loads(payment_response.data.decode())
                # self.assertTrue(response_data['Authorization'])
                self.assertEqual(payment_response.status_code, 400)
                self.assertEqual(response_data['message'] ,'Bad Request')

    
    def test_wrong_credit_card_number(self):
            """ Test for premium gateway"""
            with self.client:
                # user registration
                payment_response = wrong_credit_card_number(self)
                response_data = json.loads(payment_response.data.decode())
                # self.assertTrue(response_data['Authorization'])
                self.assertEqual(payment_response.status_code, 400)
                self.assertEqual(response_data['message'] ,'Bad Request')


    def test_wrong_amount(self):
            """ Test for premium gateway"""
            with self.client:
                # user registration
                payment_response = wrong_amount(self)
                response_data = json.loads(payment_response.data.decode())
                # self.assertTrue(response_data['Authorization'])
                self.assertEqual(payment_response.status_code, 400)
                self.assertEqual(response_data['message'] ,'Bad Request')



if __name__ == '__main__':
    unittest.main()