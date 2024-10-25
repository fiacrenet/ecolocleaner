from django.contrib import admin
from .models import Service,Realisation,Devis,ContactMessage

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', 'description')

@admin.register(Realisation)
class RealisationAdmin(admin.ModelAdmin):
    list_display = ['id', 'avant', 'apres']  

@admin.register(Devis)
class DevisAdmin(admin.ModelAdmin):
    list_display = ('type_client', 'raison_sociale', 'email', 'adresse', 'telephone', 'service', 'observation')
    list_filter = ('type_client', 'service')
    search_fields = ('raison_sociale', 'email', 'adresse', 'telephone')
    # Trier les objets par ID décroissant
    ordering = ('-id',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phone', 'subject', 'message', 'created_at')  # Affichez les champs souhaités
    search_fields = ('fullname', 'email', 'subject')  # Champs de recherche
    list_filter = ('created_at',)  # Filtre par date de création si applicable
    ordering = ('-created_at',)  # Trie par date de création décroissante