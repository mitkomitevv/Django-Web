from django.urls import path, include
from fruitpedia.fruit.views import FruitCreateView, FruitDetailsView, FruitDeleteView, FruitEditView

urlpatterns = [
    path('create/', FruitCreateView.as_view(), name='create_fruit'),
    path('<int:pk>/', include([
        path('details/', FruitDetailsView.as_view(), name='details_fruit'),
        path('edit/', FruitEditView.as_view(), name='edit_fruit'),
        path('delete/', FruitDeleteView.as_view(), name='delete_fruit'),
    ]))
]