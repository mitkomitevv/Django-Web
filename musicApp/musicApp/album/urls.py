from django.urls import path, include

from musicApp.album.views import AlbumCreateView, AlbumDetailsView, AlbumUpdateView, AlbumDeleteView

urlpatterns = [
    path('add/', AlbumCreateView.as_view(), name='album-add'),
    path('<int:pk>/', include([
        path('details/', AlbumDetailsView.as_view(), name='album-details'),
        path('edit/', AlbumUpdateView.as_view(), name='album-edit'),
        path('delete/', AlbumDeleteView.as_view(), name='album-delete')
    ]))
]