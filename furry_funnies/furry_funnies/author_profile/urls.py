from django.urls import path

from furry_funnies.author_profile.views import AuthorCreateView, AuthorDetailsView, AuthorEditView, AuthorDeleteView

urlpatterns = [
    path('create/', AuthorCreateView.as_view(), name='create_author'),
    path('details/', AuthorDetailsView.as_view(), name='details_author'),
    path('edit/', AuthorEditView.as_view(), name='edit_author'),
    path('delete/', AuthorDeleteView.as_view(), name='delete_author'),

]