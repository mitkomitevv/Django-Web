from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, TemplateView
from fruitpedia.user_profile.forms import ProfileCreateForm
from fruitpedia.user_profile.models import Profile
from utils import get_profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('dashboard')


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profile/details-profile.html'

    def get_object(self, queryset=None):
        return get_profile()


class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'profile/edit-profile.html'
    form_class = modelform_factory(Profile, fields=['first_name', 'last_name', 'image_url', 'age'])
    success_url = reverse_lazy('details_profile')

    def get_object(self, queryset=None):
        return get_profile()

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields['image_url'].label = 'Image URL'

        return form


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profile/delete-profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()
