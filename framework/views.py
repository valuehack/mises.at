from django.shortcuts import render
from django.urls import reverse
from itertools import chain
import datetime
import locale

from denker.models import Denker
from verlag.models import Verlagsprogramm
from projekte.models import Projekte
from literatur.models import Buecher, Artikel
from .models import StatischeInhalte

from denker.utils import getImage
from projekte.utils import getPercent
from literatur.utils import createLink
from .utils import addLinks, getDays


def home_view(request):
    infotext = StatischeInhalte.objects.get(id="startseite")
    denker = Denker.objects.order_by("-id")[:4]
    verlag = Verlagsprogramm.objects.order_by("-id")[:2]
    projekt = Projekte.objects.order_by("-id")[0]
    literatur = chain(Buecher.objects.order_by("-id")[:2], Artikel.objects.order_by("-id")[:2])

    for denk in denker:
        denk = getImage(denk)

    for werk in verlag:
        werk.desc = addLinks(werk.desc)
        for aut in werk.denker.all():
            if werk.author is not "":
                werk.author += ", "
            werk.author += "<a class='link' href='" + reverse('denker:detail', kwargs={'denker_slug': aut.slug}) + "'><h6 lass='h-left' style='text-align: left;'>" + aut.name + "</h6></a>"

    projekt.beschreibung = addLinks(projekt.beschreibung)
    projekt = getPercent(projekt)

    literatur = createLink(literatur)

    tagesbezogenes = getDays()
    heute = ""
    if tagesbezogenes[0] or tagesbezogenes[1]:
        locale.setlocale(locale.LC_TIME, "de_DE.UTF-8")
        heute = datetime.datetime.strftime(datetime.date.today(), "%A, der %d. %B")
        daymatch = True
    else:
        daymatch = False

    context = {
        'infotext': infotext,
        'denker': denker,
        'verlag': verlag,
        'projekt': projekt,
        'literatur': literatur,
        'daymatch': daymatch,
        'geboren': tagesbezogenes[0],
        'gestorben': tagesbezogenes[1],
        'heute': heute,
    }

    return render(request, 'framework/home-view.html', context)
