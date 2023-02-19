
from django.contrib import admin
from django.urls import path, include
from treehacks_backend_api import urls as treehacks_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('photo/', include(treehacks_urls)),
]