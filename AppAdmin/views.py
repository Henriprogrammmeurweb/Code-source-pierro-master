from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .import forms
from AppAdmin.models import Compte_Utilisateur
from AppMedecin.models import Medecin, Affectation, ZoneSante, Mouvement


def login_user(request):
    if request.user.is_authenticated :
        return redirect('dashboard')
    form=forms.FormLoginUser()
    if request.method == "POST":
        form=forms.FormLoginUser(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(email=email, password=password)
            if not "@" in email:
                messages.warning(request, "Adresse Email incorrect")
            elif user:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Authentification échouée Merci de ressayer !")
        else:
            messages.error(request, "Oups ! Formulaire invalide")
    else:
        form=forms.FormLoginUser()
    return render(request, "user/login/login.html",{"form":form})

@login_required
def deconnexion(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    nombre_medecin = Medecin.objects.count()
    nombre_affectation = Affectation.objects.count()
    nombre_zone_sante = ZoneSante.objects.count()
    nombre_mouvement = Mouvement.objects.all().count()
    affectation = Affectation.objects.all()[:10]
    context = {
        "nombre_medecin":nombre_medecin,
        "nombre_affectation":nombre_affectation,
        "nombre_zone_sante":nombre_zone_sante,
        "nombre_mouvement":nombre_mouvement,
        "affectation":affectation
    }
    return render(request, 'accueil/dashboard.html', context)


