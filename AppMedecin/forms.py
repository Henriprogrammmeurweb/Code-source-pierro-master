from .import models
from django import forms
from django.forms import ModelForm


class FormAjoutMedecin(ModelForm):
    class Meta:
        model = models.Medecin

        fields = [
                    'matricule','nom', 'postnom', 'prenom', 'sexe', 
                    'email', 'telephone','specialite', 'adresse', 
                    'date_naissance', 'photo'
                ]

        widgets = {
            "matricule":forms.TextInput(attrs={"class":'form-control', 'placeholder':'matricule'}),
            "nom":forms.TextInput(attrs={"class":'form-control', 'placeholder':'nom'}),
            "postnom":forms.TextInput(attrs={"class":'form-control', 'placeholder':'postnom'}),
            "prenom":forms.TextInput(attrs={"class":'form-control', 'placeholder':'prenom'}),
            "sexe":forms.Select(attrs={"class":'form-control', 'placeholder':'sexe'}),
            "email":forms.EmailInput(attrs={"class":'form-control', 'placeholder':'email'}),
            "telephone":forms.TextInput(attrs={"class":'form-control', 'placeholder':'telephone'}),
            "specialite":forms.TextInput(attrs={"class":'form-control', 'placeholder':'specialite'}),
            "adresse":forms.TextInput(attrs={"class":'form-control', 'placeholder':'adresse'}),
            "date_naissance":forms.DateInput(attrs={"class":'form-control', 'placeholder':'date_naissance', 'type':'date'}),
            "photo":forms.FileInput(attrs={"class":'form-control', 'placeholder':'photo'}),
        }


class FormAjoutZoneSante(ModelForm):
    class Meta:
        model = models.ZoneSante

        fields = ['designation']

        widgets = {
            "designation":forms.TextInput(attrs={"class":'form-control', 'placeholder':'designation'}),
        }


class FormAjoutAffectation(ModelForm):
    class Meta:
        model = models.Affectation

        fields = ['medecin', 'zone_sante',  'lieu', 'service', 'fonction', 'date_debut']

        widgets = {
            "medecin":forms.Select(attrs={"class":"form-control"}),
            "zone_sante":forms.Select(attrs={"class":"form-control"}),
            "lieu":forms.TextInput(attrs={"class":"form-control"}),
            "service":forms.TextInput(attrs={"class":"form-control"}),
            "fonction":forms.TextInput(attrs={"class":"form-control"}),
            "date_debut":forms.TextInput(attrs={"class":"form-control", 'type':'date'}),
        }


class FormAjoutMouvement(ModelForm):
    class Meta:
        model = models.Mouvement

        fields = ['medecin', 'zone_sante',  'lieu', 'service', 'fonction', 'date_debut']

        widgets = {
            "medecin":forms.Select(attrs={"class":"form-control"}),
            "zone_sante":forms.Select(attrs={"class":"form-control"}),
            "lieu":forms.TextInput(attrs={"class":"form-control"}),
            "service":forms.TextInput(attrs={"class":"form-control"}),
            "fonction":forms.TextInput(attrs={"class":"form-control"}),
            "date_debut":forms.TextInput(attrs={"class":"form-control", 'type':'date'}),
        }
