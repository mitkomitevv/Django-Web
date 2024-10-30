from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from my_plant_app.plant.forms import PlantCreateForm, PlantEditForm, PlantDeleteForm
from my_plant_app.plant.models import Plant


class IndexView(TemplateView):
    template_name = 'common/home-page.html'


class CatalogueView(ListView):
    model = Plant
    template_name = 'common/catalogue.html'
    context_object_name = 'plants'


class PlantCreateView(CreateView):
    model = Plant
    form_class = PlantCreateForm
    template_name = 'plant/create-plant.html'
    success_url = reverse_lazy('catalogue')


class PlantDetailsView(DetailView):
    model = Plant
    template_name = 'plant/plant-details.html'
    pk_url_kwarg = 'id'


class PlantEditView(UpdateView):
    model = Plant
    form_class = PlantEditForm
    pk_url_kwarg = 'id'
    template_name = 'plant/edit-plant.html'
    success_url = reverse_lazy('catalogue')


class PlantDeleteView(DeleteView):
    model = Plant
    form_class = PlantDeleteForm
    template_name = 'plant/delete-plant.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('catalogue')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
