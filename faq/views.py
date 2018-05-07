from django.shortcuts import render
from .models import Glossar
from framework import views


def list_view(request, tag=None):
    faq = list(Glossar.objects.all().order_by('slug'))
    for begriff in faq:
        begriff.beschreibung = views.addLinks(begriff.beschreibung)
    if tag:
        print("ID = " + str(tag))

    return render(request, 'faq/list-view.html', {'faq': faq})
