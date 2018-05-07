from django.shortcuts import render, get_object_or_404
from .models import Denker
from literatur.views import gen_werke
from framework.views import addLinks
from .utils import getImage


def list_view(request):
    qs = list(Denker.objects.order_by('slug'))
    gen = ["menger", "bawerk", "mises", "rothbard"]
    letters = []
    letter_last = ""
    
    for denker in qs:
        firstletter = denker.slug[:1]
        
        if firstletter != letter_last:
            letters.append(firstletter.upper())
            letter_last = firstletter
            
        denker.firstletter = firstletter.upper()
        denker = getImage(denker)
    
    context = {
        "gen": gen,
        "denker_list": qs,
        "denker_bybirth": sorted(qs, key=lambda x: x.geburt), 
        "letters": letters,
    }
    return render(request, 'denker/list-view.html', context)


def detail_view(request, denker_slug):
    denker = getImage(get_object_or_404(Denker, slug=denker_slug))
    werke = gen_werke(denker)
    denker.bio = addLinks(denker.bio, denker.slug)
    
    context = {
        'denker': denker,
        'werke': werke[:10]
    }
    
    return render(request, 'denker/detail-view.html', context)
