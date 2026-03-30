from django.urls import path
from .views import todos_views

urlpatterns = [
    path('todos/', todos_views, name='todos'),
]
