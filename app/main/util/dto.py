from flask_restplus import Namespace, fields



class PaymentDto:
    api = Namespace('payment', description='payment related operations')
    payment = api.model('payment_details', {
        'CreditCardNumber': fields.String(required=True),
        'CardHolder': fields.String(required=True),
        'ExpirationDate': fields.Date(required=True),
        'SecurityCode': fields.String(),
        'Amount': fields.Float(required=True)
    })