from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasty_recipes.common.urls')),
    path('profile/', include('tasty_recipes.user_profile.urls')),
    path('recipe/', include('tasty_recipes.recipes.urls')),
]
