from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from world_of_speed.car.forms import CarCreateForm, CarUpdateForm, CarDeleteForm
from world_of_speed.car.models import Car
from world_of_speed.utils import get_profile


class CarCreateView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'car/car-create.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.owner = get_profile()

        return super().form_valid(form)


class CatalogueView(ListView):
    model = Car
    template_name = 'car/catalogue.html'
    context_object_name = 'cars'


class CarDetailsView(DetailView):
    model = Car
    template_name = 'car/car-details.html'
    pk_url_kwarg = 'id'


class CarEditView(UpdateView):
    model = Car
    form_class = CarUpdateForm
    template_name = 'car/car-edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('catalogue')


class CarDeleteView(DeleteView):
    model = Car
    form_class = CarDeleteForm
    template_name = 'car/car-delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('catalogue')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields['type'].widget.attrs['disabled'] = True
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True

        return form
