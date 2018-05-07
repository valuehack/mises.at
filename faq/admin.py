from django.contrib import admin
from .models import Glossar


@admin.register(Glossar)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('begriff', 'id')
