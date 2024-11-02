from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from furry_funnies.post.forms import PostCreateForm, PostEditForm, PostDeleteForm
from furry_funnies.post.models import Post
from furry_funnies.utils import get_author


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post/create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = get_author()

        return super().form_valid(form)


class PostDetailsView(DetailView):
    model = Post
    template_name = 'post/details-post.html'
    pk_url_kwarg = 'id'


class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'post/edit-post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('dashboard')


class PostDeleteView(DeleteView):
    model = Post
    form_class = PostDeleteForm
    template_name = 'post/delete-post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
