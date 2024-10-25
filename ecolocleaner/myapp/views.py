from django.shortcuts import render,redirect
from .models import Service, Realisation
from .forms import ContactForm, DevisForm
from django.contrib import messages  

def index(request):
    services = Service.objects.all()
    realizations = Realisation.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistrer les données dans la base de données
            messages.success(request, 'Votre message a été envoyé avec succès !')
            return redirect('index')  # Rediriger pour éviter la double soumission
    else:
        form = ContactForm()

    return render(request, 'index.html', {
        'services': services,
        'realizations': realizations,
        'form': form
    })

def demande_devis(request):
    if request.method == 'POST':
        form = DevisForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre demande de devis a été enregistrée avec succès.')
            return redirect('index')  # Ensure this name matches the one in urls.py
    else:
        form = DevisForm()
    
    return render(request, 'devis.html', {'form': form})

def apropos(request):
    return render(request, 'apropos.html')
