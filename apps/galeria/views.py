from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")
        return redirect('logon')
    # dados = {
    #     1: {"nome": "Nebulosa de Carina",
    #         "legenda": "webbtelescope.org / NASA / James Webb"},
    #     2: {"nome": "Galaxia NGC 1079",
    #         "legenda": "nasa.org / NASA / Hubble"}
    # }

    # colocar um - na frente de data_fotografia faz com que seja ordenado de forma crescente, se não tiver o - o padrão é decrescente
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    # é possível incluir mais filtros, .filter(publicada=True).filter(categoria=Nebulosa)
    # print(f'{fotografias}')

    # return HttpResponse('<h1>Tokun Space </h1><p>Bem-vindo ao espaço do tokun</p>')
    return render(request, 'galeria/index.html', {"cards2": fotografias})

def imagem(request, foto_id):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")        
        return redirect('logon')
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):    
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")        
        return redirect('logon')

    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True, categoria=request.GET['buscar2'])
    # fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    # if "buscar2" in request.GET:
    #     palavra_chave = request.GET['buscar2']
    #     if palavra_chave:
    #         fotografias = fotografias.filter(nome__icontains=palavra_chave)

    return render(request, 'galeria/index.html', {"cards2": fotografias})

def buscar3(request, key):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")        
        return redirect('logon')
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True, categoria=key)
    # fotografias = fotografias.filter(nome__icontains=key)

    return render(request, 'galeria/index.html', {"cards2": fotografias})

def inserir_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")
        return redirect('logon')
    
    form = FotografiaForms()

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada!')
            return redirect('index2')
        
    return render(request, 'galeria/inserir_imagem.html', {'form': form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index2')
    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

def remover_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Fotografia removida com sucesso!!!')
    return redirect('index2')
