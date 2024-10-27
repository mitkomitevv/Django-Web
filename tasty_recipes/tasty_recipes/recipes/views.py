from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from tasty_recipes.recipes.models import Recipe
from tasty_recipes.recipes.forms import RecipeCreateForm, RecipeUpdateForm, RecipeDeleteForm
from tasty_recipes.utils import get_profile


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipes/create-recipe.html'
    success_url = reverse_lazy('recipe_catalogue')

    def form_valid(self, form):
        form.instance.author = get_profile()

        return super().form_valid(form)


class RecipeCatalogueView(ListView):
    model = Recipe
    template_name = 'recipes/catalogue.html'
    context_object_name = 'recipes'


class RecipeDetailsView(DetailView):
    model = Recipe
    template_name = 'recipes/details-recipe.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        context['ingredients'] = recipe.ingredients.split(', ')
        return context


class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeUpdateForm
    pk_url_kwarg = 'id'
    template_name = 'recipes/edit-recipe.html'
    success_url = reverse_lazy('recipe_catalogue')


class RecipeDeleteView(DeleteView):
    model = Recipe
    form_class = RecipeDeleteForm
    pk_url_kwarg = 'id'
    template_name = 'recipes/delete-recipe.html'
    success_url = reverse_lazy('recipe_catalogue')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
