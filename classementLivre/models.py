import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_inscription = models.DateTimeField("date d'inscription ")
    auteur_favori = models.CharField(max_length=200)
    livre_favori = models.CharField(max_length=200)
    liste_de_lecture = models.ForeignKey(
        "listeDeLecture", on_delete=models.DO_NOTHING)


class ListeDeLecture(models.Model):
    nb_de_livre = models.IntegerField(default=0)
    livre = models.ForeignKey(
        "livre", on_delete=models.DO_NOTHING)
    date_creation = models.DateTimeField(" date de création ")


class Livre(models.Model):
    titre = models.CharField(max_length=200)
    saga = models.ForeignKey(
        "saga", on_delete=models.DO_NOTHING)
    nb_de_mots = models.IntegerField(default=0)
    auteur = models.ForeignKey(
        "auteur", on_delete=models.DO_NOTHING)


class Auteur(models.Model):
    liste_livre = models.CharField(max_length=200)
    liste_saga = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    age = models.IntegerField(default=0)


class Saga(models.Model):
    nom_saga = models.CharField(max_length=200)
    nb_de_tome = models.IntegerField(default=0)
