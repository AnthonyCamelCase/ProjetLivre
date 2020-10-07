from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('profile', views.profile, name="profile"),
    path('livre/<str:titre_livre>/', views.livre, name="livre")
]
