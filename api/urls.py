from django.urls import path
from forms_app import views
from . import views
from .views import index, todos_views 

app_name = "api"

urlpatterns = [
    path('', index, name='index'),
    path('todos/', todos_views, name='todos'),
    path('spotify-login/', views.spotify_login, name='spotify_login'),
    path('spotify-callback/', views.spotify_callback, name='spotify_callback'),
    path('spotify-success/', views.spotify_success, name='spotify_success'),
    path('test-spotify/', views.test_spotify, name='test_spotify'),
]
