from django.urls import path
from forms_app.views import contatti, listaContatti, index

app_name = "forms_app"

urlpatterns = [
    path('index/', index, name='index'),
    path('contattaci/', contatti, name='contatti'),
    path('lista_contatti/', listaContatti, name='lista_contatti'),
]