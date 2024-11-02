from django.urls import path, include
from furry_funnies.post.views import PostCreateView, PostDetailsView, PostEditView, PostDeleteView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create_post'),
    path('<int:id>/', include([
        path('details/', PostDetailsView.as_view(), name='post_details'),
        path('edit/', PostEditView.as_view(), name='edit_post'),
        path('delete/', PostDeleteView.as_view(), name='delete_post'),
    ]))
]