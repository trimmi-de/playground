import json

import requests

from playground import settings


def create_order(token):
    headers = {
        'Content-Type': 'application/json',
        'PayPal-Request-Id': '7b92603e-77ed-4896-8e78-5dea2050476a',
        'Authorization': f'Bearer {token}',
    }

    data = json.dumps({
        "intent": "CAPTURE",
        "purchase_units": [
            {
                "reference_id": "a9f80740-38f0-11e8-b467-0ed5f89f718s",
                "amount": {
                    "currency_code": "USD",
                    "value": "110.00"
                },
                "payment_source": {
                    "paypal": {
                        "experience_context": {
                            "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED",
                            "payment_method_selected": "PAYPAL", "brand_name": "EXAMPLE INC",
                            "locale": "en-US", "landing_page": "LOGIN",
                            "shipping_preference": "SET_PROVIDED_ADDRESS", "user_action": "PAY_NOW",
                            "return_url": "http://localhost:8000/pay/payment-succeeded",
                            "cancel_url": "http://localhost:8000/pay/payment-cancelled"
                        }
                    }
                }
            }
        ]
    })

    response = requests.post(
        "https://api-m.sandbox.paypal.com/v2/checkout/orders",
        headers=headers, data=data
    )

    return response


def get_token():
    headers = {
        "Accept-Language": "en_US",
        "Content-Type": "application/json"
    }
    response = requests.post(
        "https://api-m.sandbox.paypal.com/v1/oauth2/token",
        headers=headers,
        auth=(settings.CLIENT_ID, settings.APP_SECRET),
        data={'grant_type': 'client_credentials'}
    )
    return response.json()["access_token"]


def capture_fund_for_order(token, order_id):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }

    data = json.dumps({
        "amount": {
            "currency_code": "USD",
            "value": "110.00"
        },
        "description": "Boomsserang"
    })

    print(data)
    response = requests.post(
        f"https://api-m.sandbox.paypal.com/v2/checkout/orders/{order_id}/capture",
        headers=headers,
        data=data
    )
    print(response.__dict__)
    return response.json()
