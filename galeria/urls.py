from django.urls import path
from galeria.views import buscar, index, imagem, buscar3

urlpatterns = [
    path('', index, name='index2'),
    path('imagem/<int:foto_id>', imagem, name='imagem2'),
    path('buscar', buscar, name='buscar'),
    path('buscar3/<str:key>', buscar3, name='buscar3'),    
]