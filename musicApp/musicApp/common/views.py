from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from musicApp.album.models import Album
from musicApp.profile_user.forms import ProfileCreateForm
from musicApp.profile_user.models import Profile
from musicApp.utils import get_profile


class IndexView(TemplateView, FormView):
    form_class = ProfileCreateForm
    model = Profile
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
        context['albums'] = Album.objects.all()
        return context
