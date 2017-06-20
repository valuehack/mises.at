from django.shortcuts import render, get_object_or_404
from .models import Projekte, Stufen
from framework import views
from .utils import getPercent
from .forms import SpendenModelForm  #, StufenForm


def list_view(request):
    projekte = list(Projekte.objects.all().order_by('-id'))
    for p in projekte:
        p.beschreibung = views.addLinks(p.beschreibung)
        p = getPercent(p)
        # p.link = "<a class='link' href='" + reverse('denker:detail', kwargs={'denker_slug': p.auhtor.slug}) + "'><h6>" + aut.name + "</h6></a>"

    return render(request, 'projekte/list-view.html', {'projekte': projekte})


def detail_view(request, projekt_slug):
    projekt = get_object_or_404(Projekte, slug=projekt_slug)
    stufen = Stufen.objects.filter(projekt=projekt)
    stufenList = list(stufen)
    projekt.beschreibung = views.addLinks(projekt.beschreibung)
    projekt = getPercent(projekt)
    if not stufenList:
        fields = 100
    else:
        fields = 66

    if request.method == 'POST':
        spendenForm = SpendenModelForm(get_object_or_404(Projekte, slug=projekt_slug), request.POST)
        if spendenForm.is_valid():
            spendenForm.save()
            print("SAVING")
        else:
            print('NOT SAVING')
            print(spendenForm.is_valid())
            print(spendenForm.errors)

        if spendenForm.has_error:
                print(spendenForm.errors.as_text())
    else:
        spendenForm = SpendenModelForm(get_object_or_404(Projekte, slug=projekt_slug), None)


    # for stufe in stufenList

    # stufenForm = StufenForm(request.POST, projekt)  # instance=stufen)

    context = {
        "stufen": stufenList,
        "projekt": projekt,
        "fields": fields,
        "spendenform": spendenForm,
        # "stufenform": stufenForm
    }
    return render(request, 'projekte/detail-view.html', context)
