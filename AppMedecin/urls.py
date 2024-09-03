from django.urls import path
from .import views



urlpatterns = [
    path('liste-medecin', views.liste_medecin, name='liste-medecin'),
    path('ajout-medecin', views.ajout_medecin, name='ajout-medecin'),
    path('modif-medecin=<int:id>', views.modif_medecin, name='modif-medecin'),
    path('supp-medecin=<int:id>', views.supprimer_medecin, name='supp-medecin'),
    path('liste-zone-sante', views.liste_zone_sante, name="liste-zone-sante"),
    path('ajout-zonse-sante', views.ajout_zonse_sante, name="ajout-zonse-sante"),
    path('modif-zone-sante=<int:id>', views.modif_zone_sante, name="modif-zone-sante"),
    path('supp-zone-sante=<int:id>', views.supp_zone_sante, name="supp-zone-sante"),
    path('liste-affectation', views.liste_affectation, name='liste-affectation'),
    path('ajout-affectation', views.ajout_affectation, name="ajout-affectation"),
    path('modif-affectation=<int:id>', views.modif_affectation, name="modif-affectation"),
    path('supprimer-affectation=<int:id>',views.supprimer_affectation, name="supprimer-affectation"),
    path('liste-mouvement', views.liste_mouvement, name="liste-mouvement"),
    path('ajout-mouvement', views.ajout_mouvement, name="ajout-mouvement"),
    path('modif-mouvement=<int:id>', views.modif_mouvement, name="modif-mouvement"),
    path('supprimer-mouvement=<int:id>', views.supprimer_mouvement, name="supprimer-mouvement")
]