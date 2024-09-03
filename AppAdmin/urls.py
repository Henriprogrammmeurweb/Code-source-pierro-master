from .import views
from django.urls import path


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login', views.login_user, name='login'),
    path('deconnexion', views.deconnexion, name='deconnexion')
]