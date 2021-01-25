from flask import request
from flask_restplus import Resource

from ..util.dto import PaymentDto
from ..service.payment_service import  apply_payment

api = PaymentDto.api
_payment = PaymentDto.payment


@api.route('/')
class ProcessPayment(Resource):
    
    @api.response(200, 'Ok')
    @api.response(400, 'Bad Request')
    @api.response(500, 'Internal Server Error')
    @api.doc('process payments')
    @api.expect(_payment, validate=True)
    def post(self):
        """process payments"""
        data = request.json
        return apply_payment(data=data)



