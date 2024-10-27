from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from tasty_recipes.user_profile.forms import ProfileCreateForm, ProfileUpdateForm, ProfileDeleteForm
from tasty_recipes.user_profile.models import Profile
from tasty_recipes.utils import get_profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'user_profile/create-profile.html'
    success_url = reverse_lazy('recipe_catalogue')


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'user_profile/details-profile.html'

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sum_recipes'] = self.object.recipes.count()
        return context


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'user_profile/edit-profile.html'
    success_url = reverse_lazy('profile_details')

    def get_object(self, queryset=None):
        return get_profile()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'user_profile/delete-profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_profile()