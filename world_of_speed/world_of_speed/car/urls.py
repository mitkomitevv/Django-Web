from django.urls import path, include
from world_of_speed.car.views import CatalogueView, CarCreateView, CarDetailsView, CarEditView, CarDeleteView

urlpatterns = [
    path('create/', CarCreateView.as_view(), name='create_car'),
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),
    path('<int:id>/', include([
        path('details/', CarDetailsView.as_view(), name='car_details'),
        path('edit/', CarEditView.as_view(), name='edit_car'),
        path('delete/', CarDeleteView.as_view(), name='delete_car'),
    ]))
]