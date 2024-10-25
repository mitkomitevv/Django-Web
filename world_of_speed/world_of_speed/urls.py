from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('world_of_speed.common.urls')),
    path('profile/', include('world_of_speed.user_profile.urls')),
    path('car/', include('world_of_speed.car.urls'))
]
