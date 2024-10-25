from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from world_of_speed.user_profile.forms import ProfileCreateForm, ProfileUpdateForm
from world_of_speed.user_profile.models import Profile
from world_of_speed.utils import get_profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/profile-create.html'
    success_url = reverse_lazy('catalogue')


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profile/profile-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_price = Profile.objects.aggregate(total_price=Sum('cars__price'))['total_price']
        context['total_price'] = total_price
        return context

    def get_object(self, queryset=None):
        return get_profile()


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile/profile-edit.html'
    success_url = reverse_lazy('profile_details')

    def get_object(self, queryset=None):
        return get_profile()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()
