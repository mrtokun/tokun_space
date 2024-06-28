from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default=("ESTRELA", "Estrela"))
    publicada = models.BooleanField(default=False)
    descricao = models.TextField(null=False, blank=False)
    # foto = models.CharField(max_length=100, null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="usuario",
    )


    def __str__(self):
        # Um exemplo de utilizacao disso é no manage.py shell 
        # from galeria.models import Fotografia
        # Fotografia.objects.all() que se utilizará do método __str__
        # return f"Fotografia {self.nome}]"
        return self.nome
    