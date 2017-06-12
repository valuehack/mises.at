from django.shortcuts import render
from .models import Verlagsprogramm
from framework.views import addLinks
from django.urls import reverse


def list_view(request):
    werke = list(Verlagsprogramm.objects.all().order_by('-id'))
    for werk in werke:
        werk.desc = addLinks(werk.desc)
        for denker in werk.denker.all():
            if werk.author is not "":
                werk.author += ", "
            werk.author += "<a href='" + reverse('denker:detail', kwargs={'denker_slug': denker.slug}) + "'>" + denker.name + "</a>"

    return render(request, 'verlag/list-view.html', {'werke': werke})
