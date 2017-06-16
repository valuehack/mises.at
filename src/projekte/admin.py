from django.contrib import admin
from .models import Projekte, Stufen, Spenden


@admin.register(Projekte, Stufen, Spenden)
class AuthorAdmin(admin.ModelAdmin):
    pass
