from django.db import models
from AppAdmin.models import Compte_Utilisateur


class Medecin(models.Model):
    SEXE = (
        ('M', 'M'),
        ('F', 'F')
    )
    matricule = models.CharField(max_length=254, unique=True, null=True, blank=True)
    nom = models.CharField(max_length=254)
    prenom = models.CharField(max_length=254)
    postnom = models.CharField(max_length=254)
    email = models.CharField(max_length=100, unique=True, null=True, blank=True)
    telephone = models.CharField(max_length=100, null=True, blank=True)
    adresse = models.CharField(max_length=254)
    sexe = models.CharField(max_length=1, choices=SEXE)
    specialite = models.CharField(max_length=254)
    photo = models.ImageField(upload_to='profil', null=True, blank=True)
    auteur = models.ForeignKey(Compte_Utilisateur, on_delete=models.PROTECT)
    date_naissance = models.DateField()


    def __str__(self) -> str:
        return f'{self.nom} {self.postnom} {self.prenom}'
    
    def get_nom(self):
        return f"Medecin : {self.nom} {self.postnom} {self.prenom}"
    

class ZoneSante(models.Model):
    designation = models.CharField(max_length=254, unique=True)
    medecin = models.ManyToManyField(Medecin, through='Affectation')
    date_creation = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.designation

    @property
    def nombre_affectation_homme(self):
        list_affectation = self.affectation_set.all()
        total = len([i.medecin.sexe for i in list_affectation if i.medecin.sexe == "M"])
        return total
    

    @property
    def nombre_affectation_femme(self):
        list_affectation = self.affectation_set.all()
        total = len([i.medecin.sexe for i in list_affectation if i.medecin.sexe == "F"])
        return total

    @property
    def nombre_affectation(self):
        list_affectation = self.affectation_set.all()
        total = len([i for i in list_affectation])
        return total
    

class Affectation(models.Model):
    zone_sante = models.ForeignKey(ZoneSante, on_delete=models.PROTECT)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    lieu = models.CharField(max_length=254)
    service = models.CharField(max_length=254)
    fonction = models.CharField(max_length=254)
    date_debut = models.DateField()


    def __str__(self) -> str:
        return self.medecin.get_nom()
    

class Mouvement(models.Model):
    lieu = models.CharField(max_length=254)
    service = models.CharField(max_length=254)
    fonction = models.CharField(max_length=254)
    zone_sante = models.ForeignKey(ZoneSante, on_delete=models.PROTECT)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    date_debut = models.DateField()

    def __str__(self) -> str:
        return self.medecin.nom
    
