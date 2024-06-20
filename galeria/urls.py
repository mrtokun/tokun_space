from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name='index2'),
    path('imagem/', imagem, name='imagem2')
]