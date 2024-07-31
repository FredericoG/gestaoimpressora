from django.shortcuts import render, redirect
from .forms import EquipamentoForm, ItemForm, TrocaForm, ContadorForm

def cadastrar_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success', page='cadastrar_equipamento')
    else:
        form = EquipamentoForm()
    return render(request, 'cadastrar_equipamento.html', {'form': form})

def cadastrar_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success', page='cadastrar_item')
    else:
        form = ItemForm()
    return render(request, 'cadastrar_item.html', {'form': form})

def cadastrar_troca(request):
    if request.method == 'POST':
        form = TrocaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success', page='cadastrar_troca')
    else:
        form = TrocaForm()
    return render(request, 'cadastrar_troca.html', {'form': form})

def cadastrar_contador(request):
    if request.method == 'POST':
        form = ContadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success', page='cadastrar_contador')
    else:
        form = ContadorForm()
    return render(request, 'cadastrar_contador.html', {'form': form})

def success_view(request, page):
    return render(request, 'success.html', {'page': page})
