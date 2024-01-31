import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import BaseDetailView
from django_filters.views import FilterView

from laptops.filters import LaptopFilter
from laptops.models import Laptop


class LaptopListView(FilterView):

    template_name = "laptops.html"
    model = Laptop
    filterset_class = LaptopFilter

    class Meta:
        model = Laptop


class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """

    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context


class TestAjaxView(TemplateView):

    template_name = "ajax_test.html"


@csrf_exempt
def increaseCounterView(request):

    json_dict = json.loads(request.body)
    counter = int(json_dict["counter"])
    counter += 1

    return JsonResponse({"counter": counter})
