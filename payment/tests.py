from django.test import TestCase

from payment.api import get_token, create_order


# Create your tests here.
class TokenTests(TestCase):

    def test_can_get_paypal_token(self):
        token = get_token()
        print(token)
        assert token is not None

    def test_create_order(self):
        token = "A21AAIUmLPGq-KoxGXdqHP2wd5ULkNJc-oG4PFGSiqLv1orJ-oepX7ZWbJnSWuFN8VcwpTBz6IapBUnD6sQJ4kpxAAF-IzDCQ"
        order = create_order(token)
        print(order.json())
