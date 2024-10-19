from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView
from musicApp.profile_user.models import Profile
from musicApp.utils import get_profile


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profile/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()


class ProfileDeleteView(DeleteView):
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()
