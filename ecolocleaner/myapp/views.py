from django.shortcuts import render
from .models import Service, Realisation
from .forms import ContactForm  
from django.contrib import messages  

def index(request):
    services = Service.objects.all()
    realizations = Realisation.objects.all()

    # Gestion du formulaire de contact
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistrer les données dans la base de données
            messages.success(request, 'Votre message a été envoyé avec succès !')
            form = ContactForm()  # Réinitialiser le formulaire après la soumission
    else:
        form = ContactForm()

    return render(request, 'index.html', {
        'services': services,
        'realizations': realizations,
        'form': form  # Inclure le formulaire dans le contexte
    })
