from django.views.generic import TemplateView, ListView
from fruitpedia.fruit.models import Fruit
from utils import get_profile


class IndexView(TemplateView):
    template_name = 'common/index.html'


class DashboardView(ListView):
    model = Fruit
    template_name = 'common/dashboard.html'
    context_object_name = 'fruits'
