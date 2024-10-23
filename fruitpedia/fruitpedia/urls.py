from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fruitpedia.common.urls')),
    path('profile/', include('fruitpedia.user_profile.urls')),
    path('fruit/', include('fruitpedia.fruit.urls'))
]
