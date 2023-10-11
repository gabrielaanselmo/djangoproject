from django.shortcuts import render, redirect
from .forms import InscricaoForm, DepoimentoForm
from .models import Depoimento


def home(request):
    if request.method == 'POST':
        form_inscricao = InscricaoForm(request.POST or None, prefix='form_inscricao')
        form_depoimento = DepoimentoForm(request.POST or None, prefix='form_depoimento')

        if 'form_inscricao-submit' in request.POST and form_inscricao.is_valid():
            form_inscricao.save()
            return redirect('home')
        elif 'form_depoimento-submit' in request.POST and form_depoimento.is_valid():
            form_depoimento.save()
            return redirect('home')
    else:
        form_inscricao = InscricaoForm(prefix='form_inscricao')
        form_depoimento = DepoimentoForm(prefix='form_depoimento')

    depoimentos = Depoimento.objects.all()
    return render(request, 'home.html',
                  {'form_inscricao': form_inscricao, 'form_depoimento': form_depoimento, 'depoimentos': depoimentos})
