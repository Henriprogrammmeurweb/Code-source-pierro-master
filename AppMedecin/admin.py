from django.contrib import admin
from .import models


admin.site.register(models.Medecin)
admin.site.register(models.Affectation)
admin.site.register(models.ZoneSante)
admin.site.register(models.Mouvement)

