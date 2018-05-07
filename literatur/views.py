from django.shortcuts import render
from .models import Buecher, Artikel
from denker.models import Denker
from itertools import chain
from .utils import createLink, gen_werke, splitlist


def list_view(request):
    author_list = list(Denker.objects.all())
    qs_literatur = list(chain(Buecher.objects.all(), Artikel.objects.all()))
    qs_sorted = sorted(qs_literatur, key=lambda x: x.jahr, reverse=True)
    qs = createLink(qs_sorted)
    
    author_split = splitlist(author_list)
    
    context = {
        "author_list": author_split,
        "lit_list": qs,
    }
    return render(request, 'literatur/list-view.html', context)
    
    
def denker_view(request, denker_slug):
    denker = Denker.objects.get(slug=denker_slug)
    author_list = list(set(Denker.objects.all()))
    
    werke = gen_werke(denker)
    author_split = splitlist(author_list)
    
    context = {
        "author_list": author_split,
        "author": denker,
        "lit_list": werke,
    }
    
    return render(request, 'literatur/list-view.html', context)
