from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView
from musicApp.album.models import Album
from musicApp.profile_user.forms import ProfileCreateForm
from musicApp.utils import get_profile


class IndexView(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('index')

    def get_template_names(self):
        profile = get_profile()

        if profile:
            return ['common/home-with-profile.html']
        return ['common/home-no-profile.html']


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context
