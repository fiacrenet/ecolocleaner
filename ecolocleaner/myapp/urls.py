from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('devis/', views.demande_devis, name='devis'),  # Ensure 'devis' is the correct name
    path('apropos/', views.apropos, name='apropos'),
    ]
