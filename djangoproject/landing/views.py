from django.shortcuts import render, redirect
from .forms import InscricaoForm
from .models import Depoimento


def home(request):
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InscricaoForm()
    depoimentos = Depoimento.objects.all()
    return render(request, 'home.html', {'form': form, 'depoimentos': depoimentos})
