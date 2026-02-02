from django.urls import path
from news.views import homepage, articoloDetailView, index, listaArticoli, queryBase, giornalistaDetailView

app_name = "news"

urlpatterns = [
    path('', index, name='index'),
    path('homepage', homepage, name="homepage"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    #int è il numero che metto e rappresenta pk che è la primary key del database
    path("lista_articoli/<int:pk>", listaArticoli, name="lista_articoli_giornalista"),
    path("lista_articoli", listaArticoli, name="lista_articoli"),
    path("query_base", queryBase, name="query_base"),
    path("giornalista_detail/<int:pk>", giornalistaDetailView, name="giornalista_detail")
]