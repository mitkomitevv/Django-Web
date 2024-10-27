from django.urls import path
from tasty_recipes.common.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home')
]