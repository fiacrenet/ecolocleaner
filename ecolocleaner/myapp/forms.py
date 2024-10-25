from django import forms
from .models import ContactMessage, Devis

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['fullname', 'email', 'phone', 'subject', 'message']


class DevisForm(forms.ModelForm):
    class Meta:
        model = Devis
        fields = ['type_client', 'raison_sociale', 'email', 'adresse', 'telephone', 'service', 'observation']
