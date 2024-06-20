from django.shortcuts import render


def index(request):

    dados = {
        1: {"nome": "Nebulosa de Carina",
            "legenda": "webbtelescope.org / NASA / James Webb"},
        2: {"nome": "Galaxia NGC 1079",
            "legenda": "nasa.org / NASA / Hubble"}
    }

    # return HttpResponse('<h1>Tokun Space </h1><p>Bem-vindo ao espaço do tokun</p>')
    return render(request, 'galeria/index.html', {"cards2": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')