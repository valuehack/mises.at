from django.contrib import admin
from .models import Denker


@admin.register(Denker)
class AuthorAdmin(admin.ModelAdmin):
    pass
