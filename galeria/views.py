from django.shortcuts import render

def index(request):
    # return HttpResponse('<h1>Tokun Space </h1><p>Bem-vindo ao espaço do tokun</p>')
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')