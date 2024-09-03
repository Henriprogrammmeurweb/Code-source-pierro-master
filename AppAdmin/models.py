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
        return f"{self.username} {self.postnom} {self.prenom}"
    

    @property
    def get_admin(self):
        return "Oui" if self.is_superuser and self.is_staff else "Non"
    
    


