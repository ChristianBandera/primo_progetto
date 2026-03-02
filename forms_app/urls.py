from django.urls import path
from forms_app.views import contatti, listaContatti, index, modifica_contatto, elimina_contatto

app_name = "forms_app"

urlpatterns = [
    path('index/', index, name='index'),
    path('contattaci/', contatti, name='contatti'),
    path('lista_contatti/', listaContatti, name='lista_contatti'),
    path('elimina-contatto/<int:pk>', elimina_contatto, name='elimina-contatto'),
    path('modifica-contatto/<int:pk>', modifica_contatto, name='modifica-contatto'),
]