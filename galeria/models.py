from django.db import models

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        # Um exemplo de utilizacao disso é no manage.py shell 
        # from galeria.models import Fotografia
        # Fotografia.objects.all() que se utilizará do método __str__
        return f"Fotografia [nome={self.nome}]"
