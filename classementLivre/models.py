import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.


class Utilisateur(models.Model):

    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_inscription = models.DateTimeField("date d'inscription ")
    auteur_favori = models.ForeignKey(
        "auteur", on_delete=models.DO_NOTHING)
    livre_favori = models.ForeignKey(
        "livre", on_delete=models.DO_NOTHING)
    liste_de_lecture = models.ForeignKey(
        "listeDeLecture", on_delete=models.DO_NOTHING)
    # nb_de_livre = models.IntegerField(default=0) une fonctio peut être. ???


class ListeDeLecture(models.Model):

    livre = models.ForeignKey(
        "livre", on_delete=models.DO_NOTHING)
    date_creation = models.DateTimeField(" date de création ")


class Livre(models.Model):
    titre = models.CharField(max_length=200)
    saga = models.ForeignKey(
        "saga", on_delete=models.DO_NOTHING)
    auteur = models.ForeignKey(
        "auteur", on_delete=models.DO_NOTHING)
    nb_de_mots = models.IntegerField(default=0)


class Auteur(models.Model):
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    age = models.IntegerField(default=0)


class Saga(models.Model):
    nom_saga = models.CharField(max_length=200)
    nb_de_tome = models.IntegerField(default=0)
