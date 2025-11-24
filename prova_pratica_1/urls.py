from django.urls import path
from prova_pratica_1.views import view_x, view_y, index

app_name="prova_pratica_1"
urlpatterns=[
    path('index', index, name='index'),
    path('view_x/differenza', view_x, name='differenza'),
    path('view_y/pari_dispari', view_y, name='pari_dispari'),
]