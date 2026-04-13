from django.shortcuts import render
import requests

# Create your views here.

def todos_views(request):
    #Effettua la richiesta http
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/todos/')
        if response.status_code == 200:
            lista_todos = response.json()
            messaggio_errore = None
        else:
            lista_todos = []
            messaggio_errore = "Errore nel recupero dei dati. Codice di stato: " + str(response.status_code)
    except Exception as e:
        lista_todos = []
        messaggio_errore = "Errore nella connessione all'API: " + str(e)
    
    #passa i dati al template
    return render(request, 'todos.html', {
        'todos' : lista_todos,
        'errore' : messaggio_errore
    })

def index(request):
    return render(request, 'api/index.html')