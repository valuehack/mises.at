from django.shortcuts import render, get_object_or_404
from .models import Orte
from framework.views import addLinks


def map_view(request):
    orte = Orte.objects.all()
    for ort in orte:
        ort.text = addLinks(ort.text, ort.slug)
    context = {
        "orte": orte,
    }
    return render(request, 'orte/map-view.html', context)
    

def detail_view(request, ort_slug):
    ort = get_object_or_404(Orte, slug=ort_slug)
    ort.text = addLinks(ort.text, ort.slug)
    return render(request, 'orte/detail-view.html', {'ort': ort})
