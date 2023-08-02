import logging

from payment.api import create_order, get_token, capture_fund_for_order


logger = logging.getLogger()


def create_order_with_fresh_token():
    token = get_token()
    order = create_order(token)
    return order


def capture_fund(order_id):
    token = get_token()
    order = capture_fund_for_order(token, order_id)
    return order


def handle_payment_confirmed_event(resource: dict):

    """
    Handle Payment Confirmed event.
    """

    try:
        payment = Payment.objects.get(external_id=resource['id'], amount=2)
        payment.status = PaymentStatus.PAID
        payment.save()
        logger.error('Payment status updated to PAID for:%s', resource['id'])
    except Payment.DoesNotExist:
        logger.error('Payment Not Found for external_id=%s', resource['id'])


