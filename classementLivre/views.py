from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

app_name = "classementLivre"


def accueil(request):
    return render(request, "classementLivre/accueil.html")
    # return HttpResponse("Bienvenue sur le site du lecteur du dimanche.")
