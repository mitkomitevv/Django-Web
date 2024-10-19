from django.urls import path
from musicApp.common.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

]