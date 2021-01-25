from app.main.model.payment import Payment

import time
import datetime


class CreditCardValidation:


    @staticmethod
    def card_number(credit_card_number):
        try:
            card_number = list(credit_card_number.strip())

            # Remove the last digit from the card number
            check_digit = card_number.pop()

            # Reverse the order of the remaining numbers
            card_number.reverse()

            processed_digits = []

            for index, digit in enumerate(card_number):
                if index % 2 == 0:
                    doubled_digit = int(digit) * 2

                    # Subtract 9 from any results that are greater than 9		
                    if doubled_digit > 9:
                        doubled_digit = doubled_digit - 9

                    processed_digits.append(doubled_digit)
                else:
                    processed_digits.append(int(digit))

            total = int(check_digit) + sum(processed_digits)

            # Verify that the sum of the digits is divisible by 10
            if total % 10 == 0:
                return True
            else:
                return False
        except:
            return False


    @staticmethod
    def expiration_date(expiration_date):
        
        try:
            card_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date()
            today = datetime.datetime.now().date()
            if card_date >= today:
                return True
            else:
                return False

        except:
            return False

    @staticmethod
    def amount(amount):
        
        try:
            if float(amount) > 0:
                return True
            else:
                return False
        except:
            return False

    


class Payment:

    def premium_payment_gateway(data):

        try:
            #  call payment with required parameters

            
            pay_flag = True

            #### pay  : in case of failure pay_flag = False
            if pay_flag == False:
                raise Exception("there is a problem in payment process")

            return pay_flag
        
        except:
            return False


    def expensive_payment_gateway(data):

        try:
            #  call payment with required parameters

            
            pay_flag = True

            #### pay  : in case of failure pay_flag = False
            if pay_flag == False:
                raise Exception("there is a problem in payment process")

            return pay_flag
        
        except:
            return False


    def cheap_payment_gateway(data):

        try:
            #  call payment with required parameters

            pay_flag = True

            #### pay  : in case of failure pay_flag = False
            if pay_flag == False:
                raise Exception("there is a problem in payment process")

            return pay_flag
        
        except:
            return False


    