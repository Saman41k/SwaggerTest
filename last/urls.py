from django.urls import path
from .views import CarApi

urlpatterns = [
    path('api/', CarApi.as_view()),
]