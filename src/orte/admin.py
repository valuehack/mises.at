from django.contrib import admin
from .models import Orte


@admin.register(Orte)
class AuthorAdmin(admin.ModelAdmin):
    pass
