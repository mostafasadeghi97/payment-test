import unittest
import datetime

from app.main import db
from app.main.model.payment import Payment
from app.test.base import BaseTestCase


class TestpaymentModel(BaseTestCase):

    def test_encode_auth_token(self):
        payment = Payment(
            CreditCardNumber='test@test.com',
            CardHolder='test',
            ExpirationDate=datetime.datetime.utcnow(),
            SecurityCode='54545',
            Amount=45.6
        )
        db.session.add(payment)
        db.session.commit()
        payment2 = Payment.query.filter_by(SecurityCode='54545').first()
        self.assertEqual(payment, payment2)

if __name__ == '__main__':
    unittest.main()