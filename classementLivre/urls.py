from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.accueil, name='accueil'),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^livre/<str:titre_livre>/$', views.livre, name="livre")
]
