from django.urls import path
from usuarios.views import logon, cadastrar, logoff

urlpatterns = [
    path('logon', logon, name='logon'),
    path('cadastrar', cadastrar, name='cadastrar'),
    path('logoff', logoff, name='logoff'),
]