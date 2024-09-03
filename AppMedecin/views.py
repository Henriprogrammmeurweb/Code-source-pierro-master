from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Medecin, ZoneSante, Mouvement, Affectation
from .import forms


def liste_medecin(request):
    tout_medecin = Medecin.objects.all().order_by('nom')
    context = {
        'tout_medecin':tout_medecin
    }
    return render(request, 'admin/crud/medecin/liste_medecin.html', context)


def ajout_medecin(request):
    form=forms.FormAjoutMedecin()
    if request.method == 'POST':
        form = forms.FormAjoutMedecin(request.POST, request.FILES)
        if form.is_valid():
            nouveau_medecin = form.save(commit=False)
            nouveau_medecin.auteur = request.user
            nouveau_medecin.save()
            messages.success(request, 'Medecin inseré avec succès !')
            form=forms.FormAjoutMedecin()
        else:
            messages.error(request, "Impossible d'enregistrer ce medecin !")
    return render(request, 'admin/crud/medecin/ajout_medecin.html', {"form":form})


def modif_medecin(request, id:int):
    id_medecin = Medecin.objects.get(id=id)
    form=forms.FormAjoutMedecin(instance=id_medecin)
    if request.method == 'POST':
        form = forms.FormAjoutMedecin(request.POST, request.FILES, instance=id_medecin)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medecin modifié avec succès !')
            return redirect('liste-medecin')
        else:
            messages.error(request, "Impossible de modifier ce medecin !")
    return render(request, 'admin/crud/medecin/modif_medecin.html', {"form":form})


def supprimer_medecin(request, id:int):
    id_medecin = Medecin.objects.get(id=id)
    if request.method == 'POST':
        id_medecin.delete()
        messages.success(request, f'{id_medecin.nom} {id_medecin.postnom} {id_medecin.prenom} supprimer avec succès !')
        return redirect('liste-medecin')
    return render(request, 'admin/crud/medecin/supp_medecin.html', {"id_medecin":id_medecin})


def liste_zone_sante(request):
    zone_sante = ZoneSante.objects.all().order_by('designation')
    context = {
        "zone_sante":zone_sante
    }
    return render(request, 'admin/crud/zone/liste_zone_sante.html', context)


def ajout_zonse_sante(request):
    form=forms.FormAjoutZoneSante()
    if request.method == "POST":
        form = forms.FormAjoutZoneSante(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Zone de santé enregsitrée avec succès !")
            form = forms.FormAjoutZoneSante()
        else:
            messages.error(request, "Impossible d'ajouter cette zone de santé !")
    return render(request, 'admin/crud/zone/ajout_zone_sante.html', {"form":form})


def modif_zone_sante(request, id: int):
    id_zone = ZoneSante.objects.get(id=id)
    form=forms.FormAjoutZoneSante(instance=id_zone)
    if request.method == "POST":
        form = forms.FormAjoutZoneSante(request.POST, instance=id_zone)
        if form.is_valid():
            form.save()
            messages.success(request, "Zone de santé modifiée avec succès !")
            return redirect('liste-zone-sante')
        else:
            messages.error(request, "Impossible de modifié cette zone de santé !")
    return render(request, 'admin/crud/zone/modif_zone_sante.html', {"form":form})


def supp_zone_sante(request, id: int):
    id_zone = ZoneSante.objects.get(id=id)
    try:
        if request.method == "POST":
            id_zone.delete()
            messages.success(request, f"Zone de santé {id_zone.designation} supprimée avec succès !")
            return redirect('liste-zone-sante')
    except:
        messages.error(request, 'Impossible de supprimer cette zone de santé !')
    return render(request, 'admin/crud/zone/supp_zone_sante.html', {"id_zone":id_zone})


def liste_affectation(request):
    affectation = Affectation.objects.all()
    context = {
        "affectation":affectation
    }
    return render(request, 'admin/crud/affectation/liste_affectation.html', context)


def ajout_affectation(request):
    form = forms.FormAjoutAffectation()
    if request.method == "POST":
        form = forms.FormAjoutAffectation(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Affectation enregistré avec succès !")
            form=forms.FormAjoutAffectation()
        else:
            messages.error(request, "Impossible d'enregistrer cette affectation !")
    return render(request, 'admin/crud/affectation/ajout_affectation.html', {"form":form})


def modif_affectation(request, id: int):
    id_affectation = Affectation.objects.get(id=id)
    form = forms.FormAjoutAffectation(instance=id_affectation)
    if request.method == "POST":
        form = forms.FormAjoutAffectation(request.POST, instance=id_affectation)
        if form.is_valid():
            form.save()
            messages.success(request, "Affectation modifée avec succès !")
            return redirect('liste-affectation')
        else:
            messages.error(request, "Impossible de modifiée cette affectation !")
    return render(request, 'admin/crud/affectation/modif_affectation.html', {"form":form})


def supprimer_affectation(request, id: int):
    id_affectation = Affectation.objects.get(id=id)
    try:
        if request.method == "POST":
            id_affectation.delete()
            messages.success(request, "Affectation supprimée avec succès !")
            return redirect('liste-affectation')
    except:
        messages.error(request, "Impossible de supprimer cette affectation")
    return render(request, 'admin/crud/affectation/supp_affectation.html',{"id_affectation":id_affectation})



def liste_mouvement(request):
    mouvement = Mouvement.objects.all()
    context = {
        "mouvement":mouvement
    }
    return render(request, 'admin/crud/mouvement/liste_mouvement.html', context)


def ajout_mouvement(request):
    form = forms.FormAjoutMouvement()
    if request.method == "POST":
        form = forms.FormAjoutMouvement(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mouvement enregistré avec succès !")
            form=forms.FormAjoutMouvement()
        else:
            messages.error(request, "Impossible d'enregistrer ce mouvement !")
    return render(request, 'admin/crud/mouvement/ajout_mouvement.html', {"form":form})


def modif_mouvement(request, id: int):
    id_mouvement = Mouvement.objects.get(id=id)
    form = forms.FormAjoutMouvement(instance=id_mouvement)
    if request.method == "POST":
        form = forms.FormAjoutMouvement(request.POST, instance=id_mouvement)
        if form.is_valid():
            form.save()
            messages.success(request, "Mouvement modifié avec succès !")
            return redirect('liste-mouvement')
        else:
            messages.error(request, "Impossible de modifiée ce mmouvement !")
    return render(request, 'admin/crud/mouvement/modif_mouvement.html', {"form":form})



def supprimer_mouvement(request, id: int):
    id_mouvement = Mouvement.objects.get(id=id)
    try:
        if request.method == "POST":
            id_mouvement.delete()
            messages.success(request, "Mouvement supprimé avec succès !")
            return redirect('liste-mouvement')
    except:
        messages.error(request, "Impossible de supprimer ce mouvement !")
    return render(request, 'admin/crud/mouvement/supp_mouvement.html', {"id_mouvement":id_mouvement})


