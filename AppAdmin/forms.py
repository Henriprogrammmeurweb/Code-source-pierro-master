from django import forms



class  FormLoginUser(forms.Form):
    """Formulaire de connexion du personnel"""
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":'form-control', 'placeholder':'Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control','placeholder':'Password'}))
    se_souvenir_de_moi=forms.BooleanField(required=False)