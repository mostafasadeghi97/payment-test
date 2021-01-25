
import uuid
import datetime

from app.main import db
from app.main.service.payment_helper import CreditCardValidation, Payment

def apply_payment(data):

    try:
        validator = CreditCardValidation()
        if check_validation(validator, data):
            return process_payment_rules(data)
        else:
            return {'message': 'Bad Request'}, 400
    except:
        return {'message': 'payment gateway error'}, 500
        

def check_validation(validator, data):
    try:
        number_validation = validator.card_number(data['CreditCardNumber'])
        expiration_date_validation = validator.expiration_date(data['ExpirationDate'])
        amount_validation = validator.amount(data['Amount'])
        if number_validation and expiration_date_validation and amount_validation:
            return True
        else:
            return False
    except:
        return False


def process_payment_rules(data):

    try:
        payment = Payment()
        if data['Amount'] < 20:
            
            if payment.cheap_payment_gateway():
                return {'message': 'payment successfull ( cheap gateway) '}, 200
            else:
                return {'message': 'payment gateway error'}, 500
        elif 20 <= data['Amount'] <= 500:

            if payment.expensive_payment_gateway():
                return {'message': 'payment successfull ( expensive gateway) '}, 200
            else:
                if payment.cheap_payment_gateway():
                    return {'message': 'payment successfull ( cheap gateway) '}, 200
                else:
                    return {'message': 'payment gateway error'}, 500
        
        elif data['Amount'] > 500:
            i = 1
            while i <= 3:
                if payment.premium_payment_gateway():
                    return {'message': 'payment successfull ( premium gateway) '}, 200
                    break
                else:
                    i+=1

            return {'message': 'payment gateway error'}, 500
    except:
        return {'message': 'payment gateway error'}, 500
     
