from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from my_plant_app.plant.models import Plant
from my_plant_app.user_profile.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from my_plant_app.user_profile.models import Profile
from my_plant_app.utils import get_profile


class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('catalogue')


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profile/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plants_count = Plant.objects.count()
        context['stars_count'] = range(min(plants_count, 3))
        return context


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile/edit-profile.html'
    success_url = reverse_lazy('details_profile')

    def get_object(self, queryset=None):
        return get_profile()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profile/delete-profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()

    def form_valid(self, form):
        Plant.objects.all().delete()
        return super().form_valid(form)
