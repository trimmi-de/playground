import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, FormView
from django_filters.views import FilterView

from laptops.filters import LaptopFilter
from laptops.forms import CallMatchForm
from laptops.models import Laptop


class ChannelDemoView(TemplateView):
    template_name = 'channels_demo.html'


class CallMatchView(FormView):
    template_name = 'call_match.html'
    form_class = CallMatchForm
    success_url = reverse_lazy('call_match')

    def form_valid(self, form):
        text_input = form.cleaned_data['text_input']
        match = {
            'match_name': 'Test Match',
            'match_id': 2,
            'home_team': 'Zenker/Trimborn',
            'guest_team': 'Hallodri/Hanswurst',
            'court': text_input,
        }
        self.match_called_message(match)
        return super().form_valid(form)

    def match_called_message(self, match):
        channel_layer = get_channel_layer()
        user_id = self.request.user.id
        async_to_sync(channel_layer.group_send)(
            f"user_{user_id}",
            {
                'type': 'match_called',  # This must match consumer method name
                'data': {
                    'match_name': match['match_name'],
                    'match_id': match['match_id'],
                    'home_team': match['home_team'],
                    'guest_team': match['guest_team'],
                    'court': match['court'],
                }
            }
        )


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
