from django.urls import path
from voti.views import index, view_a, view_b, view_c, view_d

app_name = "voti"

urlpatterns = [
    path('', index, name='index'),
    path('materie', view_a, name="materie"),
    path('votiS', view_b, name="votiS"),
    path('media', view_c, name="media"),
    path('max_min', view_d, name="max_min"),
]