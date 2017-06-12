from django.shortcuts import render, get_object_or_404
from .models import Projekte, Stufen
from framework import views
from .utils import getPercent


def list_view(request):
    projekte = list(Projekte.objects.all().order_by('-id'))
    for p in projekte:
        p.beschreibung = views.addLinks(p.beschreibung)
        p = getPercent(p)
        # p.link = "<a class='link' href='" + reverse('denker:detail', kwargs={'denker_slug': p.auhtor.slug}) + "'><h6>" + aut.name + "</h6></a>"

    return render(request, 'projekte/list-view.html', {'projekte': projekte})


def detail_view(request, projekt_slug):
    projekt = get_object_or_404(Projekte, slug=projekt_slug)
    stufen = list(Stufen.objects.filter(projekt=projekt))
    projekt.beschreibung = views.addLinks(projekt.beschreibung)
    projekt = getPercent(projekt)
    if not stufen:
        fields = 100
    else:
        fields = 66

    context = {
        "stufen": stufen,
        "projekt": projekt,
        "fields": fields
    }
    return render(request, 'projekte/detail-view.html', context)
