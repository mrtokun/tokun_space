from django.contrib import admin
from apps.galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada", "categoria")
    list_editable= ("publicada", "categoria")
    list_display_links = ("nome","id")
    search_fields = ("nome","id")
    list_filter = ("categoria","usuario")
    list_per_page = 2

admin.site.register(Fotografia, ListandoFotografias)
