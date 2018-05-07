from django.shortcuts import render, get_object_or_404
from .models import Projekte, Stufen
from framework import views
from .utils import getPercent
from .forms import SpendenModelForm
from django.http import HttpResponse
import pprint


def list_view(request):
    projekte = list(Projekte.objects.all().order_by('-id'))
    for p in projekte:
        p.beschreibung = views.addLinks(p.beschreibung)
        p = getPercent(p)
        
    return render(request, 'projekte/list-view.html', {'projekte': projekte})


def detail_view(request, projekt_slug):
    projekt = get_object_or_404(Projekte, slug=projekt_slug)
    stufen = Stufen.objects.filter(projekt=projekt)
    stufenList = list(stufen)
    projekt.beschreibung = views.addLinks(projekt.beschreibung)
    projekt = getPercent(projekt)

    fields = 100
    if stufenList:
        fields = fields/len(stufenList)

    spendenForm = SpendenModelForm(get_object_or_404(Projekte, slug=projekt_slug), request.POST or None)
    
    if spendenForm.is_valid():
        spendenForm.save()
        print("SAVING")
        return payment_view(request)
    else:
        print('NOT SAVING')
        print(spendenForm.errors)
    
    context = {
        "stufen": stufenList,
        "fields": fields,
        "projekt": projekt,
        "spendenform": spendenForm,
    }
    return render(request, 'projekte/detail-view.html', context)
    

def payment_view(request):
    pprint.pprint(request.POST['Stufe'])
    context = {
        "stufe": Stufen.objects.get(pk = int(request.POST['Stufe'])),
    }
    return render(request, 'projekte/payment-view.html', context)
    # return HttpResponse(request.POST['projekt'])
