import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
import os
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib import messages
from .models import Medecin, ZoneSante, Mouvement, Affectation
from .import forms


@login_required
def liste_medecin(request):
    tout_medecin = Medecin.objects.all().order_by('nom')
    context = {
        'tout_medecin':tout_medecin
    }
    return render(request, 'admin/crud/medecin/liste_medecin.html', context)


@login_required
def detail_medecin(request, id: int):
    id_medecin = Medecin.objects.get(id=id)
    affectation = Affectation.objects.filter(medecin=id_medecin)
    mouvement = Mouvement.objects.filter(medecin=id_medecin)
    context = {
        'id_medecin':id_medecin,
        'affectation':affectation,
        'mouvement':mouvement
    }
    return render(request, "admin/detail/medecin/detail_medecin.html", context)


@login_required
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


@login_required
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


@login_required
def supprimer_medecin(request, id:int):
    id_medecin = Medecin.objects.get(id=id)
    if request.method == 'POST':
        id_medecin.delete()
        messages.success(request, f'{id_medecin.nom} {id_medecin.postnom} {id_medecin.prenom} supprimer avec succès !')
        return redirect('liste-medecin')
    return render(request, 'admin/crud/medecin/supp_medecin.html', {"id_medecin":id_medecin})


@login_required
def liste_zone_sante(request):
    zone_sante = ZoneSante.objects.all().order_by('designation')
    context = {
        "zone_sante":zone_sante
    }
    return render(request, 'admin/crud/zone/liste_zone_sante.html', context)


@login_required
def detail_zone_sante(request, id :int):
    id_zone = ZoneSante.objects.get(id=id)
    affectation = Affectation.objects.filter(zone_sante=id_zone)
    mouvement = Mouvement.objects.filter(zone_sante=id_zone)
    context = {
        "id_zone":id_zone,
        "affectation":affectation,
        "mouvement":mouvement
    }
    return render(request, "admin/detail/zone/detail_zone_sante.html", context)


@login_required
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


@login_required
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


@login_required
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


@login_required
def liste_affectation(request):
    affectation = Affectation.objects.all()
    context = {
        "affectation":affectation
    }
    return render(request, 'admin/crud/affectation/liste_affectation.html', context)


@login_required
def ajout_affectation(request):
    form = forms.FormAjoutAffectation()
    if request.method == "POST":
        form = forms.FormAjoutAffectation(request.POST)
        if form.is_valid():
            medecin = form.cleaned_data['medecin']
            affectation = Affectation.objects.filter(medecin=medecin).exists()
            if affectation:
                messages.error(request, "Ce médecin est déjà affecté, il peut déjà faire des mouvements")
            else:
                form.save()
                messages.success(request, "Affectation enregistré avec succès !")
                form=forms.FormAjoutAffectation()
        else:
            messages.error(request, "Impossible d'enregistrer cette affectation !")
    return render(request, 'admin/crud/affectation/ajout_affectation.html', {"form":form})


@login_required
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


@login_required
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


@login_required
def liste_mouvement(request):
    mouvement = Mouvement.objects.all()
    context = {
        "mouvement":mouvement
    }
    return render(request, 'admin/crud/mouvement/liste_mouvement.html', context)


@login_required
def ajout_mouvement(request):
    form = forms.FormAjoutMouvement()
    if request.method == "POST":
        form = forms.FormAjoutMouvement(request.POST)
        if form.is_valid():
            medecin = form.cleaned_data['medecin']
            affectation = Affectation.objects.filter(medecin=medecin).exists()
            if affectation:
                form.save()
                messages.success(request, "Mouvement enregistré avec succès !")
                form=forms.FormAjoutMouvement()
            else:
                messages.error(request, "Ce médecin n'a jamais été affecté, il ne peut jamais faire de mouvement !")
        else:
            messages.error(request, "Impossible d'enregistrer ce mouvement !")
    return render(request, 'admin/crud/mouvement/ajout_mouvement.html', {"form":form})


@login_required
def modif_mouvement(request, id: int):
    id_mouvement = Mouvement.objects.get(id=id)
    form = forms.FormAjoutMouvement(instance=id_mouvement)
    if request.method == "POST":
        form = forms.FormAjoutMouvement(request.POST, instance=id_mouvement)
        if form.is_valid():
            medecin = form.cleaned_data['medecin']
            affectation = Affectation.objects.filter(medecin=medecin).exists()
            if affectation:
                form.save()
                messages.success(request, "Mouvement modifié avec succès !")
                return redirect('liste-mouvement')
            else:
                messages.error(request, "Ce médecin n'a jamais été affecté, il ne peut jamais faire de mouvement !")
        else:
            messages.error(request, "Impossible de modifiée ce mmouvement !")
    return render(request, 'admin/crud/mouvement/modif_mouvement.html', {"form":form})


@login_required
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


@login_required
def pdf_affectation(request, id: int):
    affectation_id = Affectation.objects.get(id=id)
    dateToday = datetime.date.today()
    context = {
        "affectation_id":affectation_id,
        'dateToday':dateToday,
    }
    template_path = 'admin/crud/affectation/pdf_affectation.html'
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="pdf_affectation.pdf"'
    template = get_template(template_path)
    html = template.render(context)
        # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('Impossible de générer ce pdf')
    return response


@login_required
def pdf_mouvement(request, id: int):
    mouvement_id = Mouvement.objects.get(id=id)
    dateToday = datetime.date.today()
    context = {
        "mouvement_id":mouvement_id,
        'dateToday':dateToday,
    }
    template_path = 'admin/crud/mouvement/pdf_mouvement.html'
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="pdf_affectation.pdf"'
    template = get_template(template_path)
    html = template.render(context)
        # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('Impossible de générer ce pdf')
    return response



