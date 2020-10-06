from django.shortcuts import render
from django.http import HttpResponse

from .models import Utilisateur, Auteur, Livre, Saga

# Create your views here.

app_name = "classementLivre"


def accueil(request):
    return render(request, "classementLivre/accueil.html")
    # return HttpResponse("Bienvenue sur le site du lecteur du dimanche.")


def profile(request):
    livres = Livre.objects.all()
    return render(request, "classementLivre/profile.html", {"livres": livres})
