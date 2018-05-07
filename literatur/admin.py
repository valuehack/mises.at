from django.contrib import admin
from .models import Artikel, Buecher, Dokumente


@admin.register(Artikel, Buecher, Dokumente)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('id', 'titel', 'slug', 'autor', 'jahr')
