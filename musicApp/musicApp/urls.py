from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('musicApp.common.urls')),
    path('album/', include('musicApp.album.urls')),
    path('profile/', include('musicApp.profile_user.urls'))
]
