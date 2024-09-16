from django.db import models
from django.contrib.auth.models import AbstractUser


class Compte_Utilisateur(AbstractUser):
    username = models.CharField(max_length=254)
    prenom = models.CharField(max_length=254)
    postnom = models.CharField(max_length=254)
    email = models.CharField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'prenom', 'postnom']

    def __str__(self) -> str:
        return self.username

    @property
    def get_nom(self):
        return f"{self.prenom.capitalize()} {self.username.capitalize()}"
    

    @property
    def get_admin(self):
        return "Oui" if self.is_superuser and self.is_staff else "Non"
    
    @property
    def get_nombre_medecin_cree(self):
        medecin = self.medecin_set.all()
        total = len([i.auteur for i in medecin])
        return total
    
    


