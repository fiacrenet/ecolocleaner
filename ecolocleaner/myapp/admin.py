from django.contrib import admin
from .models import Service,Realisation,ContactMessage,Devis

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', 'description')

@admin.register(Realisation)
class RealisationAdmin(admin.ModelAdmin):
    list_display = ['id', 'avant', 'apres']  

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)

@admin.register(Devis)
class DevisAdmin(admin.ModelAdmin):
    list_display = ('type_client', 'raison_sociale', 'email', 'adresse', 'telephone', 'service', 'observation')
    list_filter = ('type_client', 'service')
    search_fields = ('raison_sociale', 'email', 'adresse', 'telephone')
    # Trier les objets par ID décroissant
    ordering = ('-id',)