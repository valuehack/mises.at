from django.contrib import admin
from .models import Projekte, Stufen


@admin.register(Projekte, Stufen)
class AuthorAdmin(admin.ModelAdmin):
    pass
