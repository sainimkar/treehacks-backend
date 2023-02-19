from django.urls import re_path
from django.urls import path, include
from .views import (
    TreehacksApiView,
)

urlpatterns = [
    re_path('api', TreehacksApiView.as_view()),
]