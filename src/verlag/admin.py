from django.contrib import admin
from .models import Verlagsprogramm


@admin.register(Verlagsprogramm)
class AuthorAdmin(admin.ModelAdmin):
    pass
