from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from fruitpedia.fruit.forms import FruitCreateForm
from fruitpedia.fruit.models import Fruit
from utils import get_profile


class FruitCreateView(CreateView):
    model = Fruit
    form_class = FruitCreateForm
    template_name = 'fruit/create-fruit.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner_id = get_profile().pk
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['profile'] = get_profile()
    #     return context


class FruitDetailsView(DetailView):
    model = Fruit
    template_name = 'fruit/details-fruit.html'


class FruitEditView(UpdateView):
    model = Fruit
    template_name = 'fruit/edit-fruit.html'
    form_class = FruitCreateForm
    success_url = reverse_lazy('dashboard')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields['name'].label = 'Name'
        form.fields['image_url'].label = 'Image URL'
        form.fields['description'].label = 'Description'
        form.fields['nutrition'].label = 'Nutrition'

        return form


class FruitDeleteView(DeleteView):
    model = Fruit
    form_class = FruitCreateForm
    template_name = 'fruit/delete-fruit.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields['name'].label = 'Name'
        form.fields['image_url'].label = 'Image URL'
        form.fields['description'].label = 'Description'
        form.fields['nutrition'].label = 'Nutrition'

        for field in form.fields.values():
            field.widget.attrs['readonly'] = True

        return form