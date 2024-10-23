from django.urls import path
from fruitpedia.common.views import DashboardView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]