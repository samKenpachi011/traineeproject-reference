from tabnanny import verbose
from django.apps import AppConfig as DjangoAppConfig

class AppConfig(DjangoAppConfig):
    name = "traineeproject_reference"
    verbose_name = "Traineeproject Reference"