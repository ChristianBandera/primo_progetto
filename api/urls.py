from django.urls import path
from .views import todos_views, index

app_name = "api"

urlpatterns = [
    path('', index, name='index'),
    path('todos/', todos_views, name='todos'),
]
