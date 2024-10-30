from django.urls import path
from my_plant_app.user_profile.views import CreateProfileView, ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('create/', CreateProfileView.as_view(), name='create_profile'),
    path('details/', ProfileDetailsView.as_view(), name='details_profile'),
    path('edit/', ProfileEditView.as_view(), name='edit_profile'),
    path('delete/', ProfileDeleteView.as_view(), name='delete_profile'),
]