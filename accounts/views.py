from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from playground.settings import CONSTANCE_CONFIG, get_constance


class ChartView(LoginRequiredMixin, TemplateView):

    template_name = "dashboard.html"
    login_url = "/accounts/login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = [
            [1, 2, 4, 5],
            [2, 4, 5, 7],
            [8, 6, 4, 2]
        ]
        context["labels"] = ["0", "1", "2", "3"]

        return context


class CustomLoginView(LoginView):

    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        timeout = get_constance("SESSION_TIMEOUT_SECONDS")
        request.session.set_expiry(timeout)
        return super().post(request, *args, **kwargs)