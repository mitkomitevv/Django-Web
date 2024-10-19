from django.urls import path, include
from musicApp.profile_user.views import ProfileDetailsView, ProfileDeleteView

urlpatterns = [
    path('details/', ProfileDetailsView.as_view(), name='profile-details'),
    path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
]