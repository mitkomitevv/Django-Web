from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from musicApp.album.mixins import AlbumFormMixin
from musicApp.album.models import Album
from musicApp.utils import get_profile


class AlbumCreateView(AlbumFormMixin, CreateView):
    model = Album
    fields = ['name', 'artist_name', 'genre', 'description', 'image_url', 'price']
    template_name = 'album/album-add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.owner = get_profile()

        return super().form_valid(form)


class AlbumDetailsView(DetailView):
    model = Album
    template_name = 'album/album-details.html'


class AlbumUpdateView(AlbumFormMixin, UpdateView):
    model = Album
    fields = ['name', 'artist_name', 'genre', 'description', 'image_url', 'price']
    template_name = 'album/album-edit.html'
    success_url = reverse_lazy('index')


class AlbumDeleteView(DeleteView):
    model = Album
    form_class = modelform_factory(Album, fields=['name', 'artist_name', 'genre', 'description', 'image_url', 'price'])
    template_name = 'album/album-delete.html'
    success_url = reverse_lazy('index')

    # def get_initial(self):
    #     return self.object.__dict__
    #                                                     If ModelForm
    # def form_invalid(self, form):
    #     return self.form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        for field in form.fields.values():
            field.widget.attrs['readonly'] = True

        return form
