from django.contrib import admin
from .models import StatischeInhalte


@admin.register(StatischeInhalte)
class AuthorAdmin(admin.ModelAdmin):
    pass
