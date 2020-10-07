from django.contrib import admin
from .models import Utilisateur, ListeDeLecture, Livre, Auteur, Saga, Avis
# Register your models here.

admin.site.register(Utilisateur)
admin.site.register(ListeDeLecture)
admin.site.register(Livre)
admin.site.register(Auteur)
admin.site.register(Saga)
admin.site.register(Avis)
