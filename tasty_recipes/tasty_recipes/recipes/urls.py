from django.urls import path, include
from tasty_recipes.recipes.views import RecipeCreateView, RecipeCatalogueView, RecipeDetailsView, RecipeUpdateView, \
    RecipeDeleteView

urlpatterns = [
    path('create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('catalogue/', RecipeCatalogueView.as_view(), name='recipe_catalogue'),
    path('<int:id>/', include([
        path('details/', RecipeDetailsView.as_view(), name='recipe_details'),
        path('edit/', RecipeUpdateView.as_view(), name='recipe_update'),
        path('delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
    ]))
]