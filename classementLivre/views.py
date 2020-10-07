from django.shortcuts import render
from django.http import HttpResponse

from .models import Utilisateur, Auteur, Livre, Saga, Avis

# Create your views here.

app_name = "classementLivre"


def accueil(request):
    return render(request, "classementLivre/accueil.html")
    # return HttpResponse("Bienvenue sur le site du lecteur du dimanche.")


def profile(request):
    livres = Livre.objects.all()
    return render(request, "classementLivre/profile.html", {"livres": livres})


def livre(request, titre_livre):
    livre = Livre.objects.all().filter(titre=titre_livre)[0]
    return render(request, "classementLivre/livre.html", {"livre": livre})
