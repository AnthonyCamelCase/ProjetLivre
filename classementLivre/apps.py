from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class ClassementLivreConfig(AppConfig):
    name = 'classementLivre'


class MyAdminConfig(AdminConfig):
    default_site = 'myproject.admin.MyAdminSite'
