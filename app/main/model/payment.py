from .. import db, flask_bcrypt

import datetime
import jwt
from ..config import key



### i did not use this model for this code excercise
class Payment(db.Model):
    """ Payment Model for storing payment related details """
    __tablename__ = "payment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CreditCardNumber = db.Column(db.String(255), nullable=False)
    ExpirationDate = db.Column(db.DateTime, nullable=False)
    CardHolder = db.Column(db.String(300), nullable=False, default=False)
    SecurityCode = db.Column(db.String(100), nullable=True)
    Amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return "<credit card '{}'>".format(self.CreditCardNumber)



    