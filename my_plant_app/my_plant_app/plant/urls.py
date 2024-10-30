from django.urls import path
from my_plant_app.plant.views import IndexView, CatalogueView, PlantCreateView, PlantDetailsView, PlantEditView, \
    PlantDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),
    path('create/', PlantCreateView.as_view(), name='create_plant'),
    path('details/<int:id>/', PlantDetailsView.as_view(), name='details_plant'),
    path('edit/<int:id>/', PlantEditView.as_view(), name='edit_plant'),
    path('delete/<int:id>/', PlantDeleteView.as_view(), name='delete_plant'),
]