from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from furry_funnies.author_profile.forms import AuthorCreateForm, AuthorEditForm
from furry_funnies.author_profile.models import Author
from furry_funnies.post.models import Post
from furry_funnies.utils import get_author


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'author/create-author.html'
    success_url = reverse_lazy('dashboard')


class AuthorDetailsView(DetailView):
    model = Author
    template_name = 'author/details-author.html'

    def get_object(self, queryset=None):
        return get_author()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['latest_post'] = Post.objects.order_by('-updated_at').first()
        return context

class AuthorEditView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'author/edit-author.html'
    success_url = reverse_lazy('details_author')

    def get_object(self, queryset=None):
        return get_author()

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_author()
