from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='services/images/')

    def __str__(self):
        return self.title

class Realisation(models.Model):
    avant = models.ImageField(upload_to='images/avant/')
    apres = models.ImageField(upload_to='images/apres/', default='images/default.jpg')  # Valeur par défaut

    def __str__(self):
        return f'Realisation {self.id}'

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Devis(models.Model):
    TYPE_CLIENT_CHOICES = [
        ('societe', 'Société'),
        ('particulier', 'Particulier'),
    ]
    
    type_client = models.CharField(max_length=20, choices=TYPE_CLIENT_CHOICES, default='societe')
    raison_sociale = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    service = models.CharField(max_length=255, default='Nettoyage Ecologique & Sans Eau des Véhicules')
    observation = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email