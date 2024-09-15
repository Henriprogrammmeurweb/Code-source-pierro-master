from django import forms
from AppAdmin.models import Compte_Utilisateur
from django.contrib.auth.forms import PasswordChangeForm


class  FormLoginUser(forms.Form):
    """Formulaire de connexion du personnel"""
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":'form-control', 'placeholder':'Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control','placeholder':'Password'}))
    se_souvenir_de_moi=forms.BooleanField(required=False)


class FormAddUtilisateur(forms.ModelForm):
    """Formulaire de création des utilisateurs du site"""
    class Meta:
        model = Compte_Utilisateur

        fields = ['username','postnom', 'prenom', 'email', 'password', 'is_superuser']

        widgets ={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "postnom":forms.TextInput(attrs={"class":"form-control"}),
            "prenom":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
        }


class FormModifUtilisateur(forms.ModelForm):
    """Formulaire de modification des utilisateurs du site"""
    class Meta:
        model = Compte_Utilisateur

        fields = ['username','postnom', 'prenom', 'email', 'is_superuser', 'user_permissions']

        widgets ={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "postnom":forms.TextInput(attrs={"class":"form-control"}),
            "prenom":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
            "user_permissions":forms.SelectMultiple(attrs={"class":"form-control"}),
        }


class UserPasswordChange(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control'}))
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control'}))
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control'}))
