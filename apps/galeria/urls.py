from django.urls import path
from apps.galeria.views import buscar, index, imagem, buscar3, inserir_imagem, editar_imagem, remover_imagem

urlpatterns = [
    path('', index, name='index2'),
    path('imagem/<int:foto_id>', imagem, name='imagem2'),
    path('buscar', buscar, name='buscar'),
    path('buscar3/<str:key>', buscar3, name='buscar3'),    
    path('inserir-imagem', inserir_imagem, name='inserir_imagem'),    
    path('editar-imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),    
    path('remover-imagem/<int:foto_id>', remover_imagem, name='remover_imagem'),            
]