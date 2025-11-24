import random
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "prova_pratica_1/index.html")

def view_x(request):
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    differenza = num1-num2
    context = {
        "num1":num1,
        "num2": num2,
        "differenza" : differenza
    }
    return render(request, "diff.html", context)

def view_y(request):
    lista=[]
    nPari=0
    nDisp=0

    for i in range(15):
        numero=(random.randint(1, 20))
        lista.append(numero)
        if(numero %2==0):
            nPari+=1
        else:
            nDisp+=1

    context = {
        "listaNumeri" : lista,
        "numeriPari" : nPari,
        "numeriDispari" : nDisp
    }
    return render(request, "pari.html", context)