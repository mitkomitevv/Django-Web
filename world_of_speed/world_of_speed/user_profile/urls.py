from django.urls import path
from world_of_speed.user_profile.views import ProfileCreateView, ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create_profile'),
    path('details/', ProfileDetailsView.as_view(), name='profile_details'),
    path('edit/', ProfileEditView.as_view(), name='edit_profile'),
    path('delete/', ProfileDeleteView.as_view(), name='delete_profile')
]