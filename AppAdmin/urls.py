from .import views
from django.urls import path


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login', views.login_user, name='login'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
    path('liste-utilisateur', views.liste_utilisateur, name='liste-utilisateur'),
    path('inserer-utilisateur', views.inserer_utilisateur, name="inserer-utilisateur"),
    path('modif-utilisateur=<int:id>', views.modif_utilisateur, name="modif-utilisateur"),
    path('password-change', views.PasswordChange, name="password-change")
]