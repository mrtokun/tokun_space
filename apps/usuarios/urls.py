from django.urls import path
from apps.usuarios.views import logon, cadastrar, logoff

urlpatterns = [
    path('logon', logon, name='logon'),
    path('cadastrar', cadastrar, name='cadastrar'),
    path('logoff', logoff, name='logoff'),
]