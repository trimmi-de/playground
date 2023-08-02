from django.urls import path
from django.views.generic import TemplateView

from payment.views.paypal import PaymentView, CreatePaypalOrderView, CaptureFundView, PaymentWebhookView

urlpatterns = [
    path("", PaymentView.as_view()),
    path("create-paypal-order", CreatePaypalOrderView.as_view()),
    path("capture-paypal-order", CaptureFundView.as_view()),
    path("payment-succeeded", TemplateView.as_view(template_name="payment-succeeded.html")),
    path("payment-cancelled", TemplateView.as_view(template_name="payment-cancelled.html")),
    path('webhook/', PaymentWebhookView.as_view(), name='webhook'),
]