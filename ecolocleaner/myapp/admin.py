from django.contrib import admin
from .models import Service,Realisation,ContactMessage

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