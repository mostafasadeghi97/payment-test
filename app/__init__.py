# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.payment_controller import api as payment_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='payment service',
          version='1.0',
          description='payment service with different methods'
          )

api.add_namespace(payment_ns, path='/payment')
