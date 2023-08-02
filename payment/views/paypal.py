import json
import logging

from django.http import JsonResponse
from django.utils.decorators import method_decorator

from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from payment.utils import create_order_with_fresh_token, capture_fund, handle_payment_confirmed_event


logger = logging.getLogger("django")


class PaymentView(TemplateView):

    template_name = "pay.html"


@method_decorator(csrf_exempt, name='dispatch')
class CreatePaypalOrderView(View):

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        order = create_order_with_fresh_token()
        print("Order created:")
        return JsonResponse(order.json())


@method_decorator(csrf_exempt, name='dispatch')
class CaptureFundView(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        print(data)
        order = capture_fund(data["orderID"])
        print("Order captured:")
        print(order)
        return JsonResponse(order)


@method_decorator(csrf_exempt, name='dispatch')
class PaymentWebhookView(View):

    def post(self, request, *args, **kwargs):
        """
        Webhook handler
        """
        request_data = request.data
        logger.info(request_data)

        if request_data['event_type'] == "PAYMENT.CAPTURE.COMPLETED":
            payment = request_data['resource']
            handle_payment_confirmed_event(payment)

        return JsonResponse({})
