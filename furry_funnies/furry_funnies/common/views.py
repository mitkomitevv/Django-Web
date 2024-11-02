from django.views.generic import TemplateView, ListView
from furry_funnies.post.models import Post


class IndexView(TemplateView):
    template_name = 'common/index.html'


class DashboardView(ListView):
    model = Post
    template_name = 'common/dashboard.html'
    context_object_name = 'posts'
