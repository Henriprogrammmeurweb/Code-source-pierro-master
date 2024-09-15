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


@login_required
def liste_utilisateur(request):
    users_site = Compte_Utilisateur.objects.all()
    context = {
        "users_site":users_site
    }
    return render(request, "user/afficher/liste_utilisateur.html", context)


@login_required
def inserer_utilisateur(request):
    form = forms.FormAddUtilisateur()
    if request.method == "POST":
        form = forms.FormAddUtilisateur(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data["username"]
            postnom = form.cleaned_data["postnom"]
            prenom = form.cleaned_data["prenom"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            is_superuser = form.cleaned_data["is_superuser"]
            
            if len(password) < 6 :
                messages.error(request, "Le mot de passe doit être supérieur ou égal à 6 caractères !")
            elif password.isdigit():
                messages.error(request, "Le mot de passe ne doit pas être entièrement numérique !")
            elif not password.isdigit() and len(password) >= 6 :
                nouveau_utilisateur = Compte_Utilisateur.objects.create_user(username=username, postnom=postnom, prenom=prenom, email=email, password=password, is_superuser=is_superuser)
                nouveau_utilisateur.save()
                messages.success(request, "Compte utilisateur crée avec succès !")
                form = forms.FormAddUtilisateur()
            else:
                messages.error(request, "Impossible de créer le compte de cet utilisateur !")
        else:
            messages.error(request, "Le formulaire est valide !")

    return render(request, "user/register/register.html", {"form":form})


@login_required
def modif_utilisateur(request, id: int):
    id_utilisateur = Compte_Utilisateur.objects.get(id=id)
    form = forms.FormModifUtilisateur(instance=id_utilisateur)
    if request.method == "POST":
        form = forms.FormModifUtilisateur(request.POST, instance=id_utilisateur)
        if form.is_valid():
            form.save()
            messages.success(request, "Information mise à jour !")
            return redirect('liste-utilisateur')
        else:
            messages.error(request, "Impossible de mettre à jour ces informations")
    return render(request, "user/update/update_user.html", {"form":form})




@login_required
def PasswordChange(request):
    form=forms.UserPasswordChange(request.user)
    if request.method == "POST":
        form=forms.UserPasswordChange(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Vous êtes maintenant deconnecté, votre mot de passe a été changé, connectez-vous à nouveau !")
            return redirect('login')
        else:
            messages.error(request, "Impossible !")
    else:
        form=forms.UserPasswordChange(request.user)
    return render(request, "user/change/passwordChange.html",{"form":form})



