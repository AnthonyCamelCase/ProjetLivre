import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.


class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)
    slug = models.SlugField()
    prenom = models.CharField(max_length=50)
    date_inscription = models.DateTimeField("date d'inscription ")
    auteur_favori = models.ForeignKey(
        "auteur", on_delete=models.DO_NOTHING)
    livre_favori = models.ForeignKey(
        "livre", on_delete=models.DO_NOTHING)
    liste_de_lecture = models.ForeignKey(
        "listeDeLecture", on_delete=models.DO_NOTHING)
    # nb_de_livre = models.IntegerField(default=0) une fonctio peut être. ???

    def __str__(self):
        return self.nom


# table détaillant les livres lus par l'utilisateur
class ListeDeLecture(models.Model):
    livre = models.ForeignKey(
        "livre", on_delete=models.DO_NOTHING)
    date_creation = models.DateTimeField(" date de création ")


# table des livres contenant le nom et le nombre de mots liés aux tables d'auteurs et de sagas
class Livre(models.Model):
    titre = models.CharField(max_length=200)
    prepopulated_fields = {"slug": ("titre",)}
    saga = models.ForeignKey(
        "saga", on_delete=models.DO_NOTHING, default="livre unique")
    auteur = models.ForeignKey(
        "auteur", on_delete=models.DO_NOTHING)
    nb_de_mots = models.IntegerField(default=0)
    avis = models.ForeignKey("avis", on_delete=models.CASCADE)

    def __str__(self):
        return self.titre


class Avis(models.Model):
    titre_avis = models.CharField(max_length=200)
    titre = models.CharField(max_length=200)
    commentaire = models.TextField()
    date_avis = models.DateTimeField(auto_now_add=True)
    # utilisateur auteur de l'avis

    def __str__(self):
        return self.titre_avis


# table présentant les auteurs, prénom, nom et age, voire lien biblio??
class Auteur(models.Model):
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.nom


# table présentant les noms des sagas et le nombre de tome les composant
class Saga(models.Model):
    nom_saga = models.CharField(max_length=200)
    nb_de_tome = models.IntegerField(default=0)

    def __str__(self):
        return self.nom_saga
