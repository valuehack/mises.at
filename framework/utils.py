from denker.models import Denker
from orte.models import Orte
from faq.models import Glossar
import re
from django.urls import reverse
import datetime


def addLinks(text, current=""):
    orte = Orte.objects.all()
    denker = Denker.objects.all()
    glossar = Glossar.objects.all()
    # werke = chain(Buecher.objects.all(), Artikel.objects.all())
    
    # Führt zu Problemen, da manche Werke zu unspezifische Namen haben.
    # for werk in werke:
    #     if werk.slug == current or werk.quelle:
    #         continue
    #     text = re.sub(r'(?P<name>' + werk.name + r's?)\b', '<a href="' + reverse('literatur:detail', kwargs={'ort_slug': ort.slug}) + '">' + r'\g<name>' + '</a>', text)
    
    for ort in orte:
        if ort.slug == current:
            continue
        text = re.sub(r'(?P<name>' + ort.name + r's?)\b', '<a href="' + reverse('orte:detail', kwargs={'ort_slug': ort.slug}) + '">' + r'\g<name>' + '</a>', text)
        
    for term in glossar:
        if term.beschreibung:
            text = re.sub(r'(?P<name>' + term.begriff + r')\b', '<a href="' + reverse('faq:list') + '#' + term.slug + '" onclick="tagLink()">' + r'\g<name>' + '</a>', text)

    for denk in denker:
        if denk.slug == current:
            continue
        name = denk.name.rsplit(None, 1)
        text = re.sub(r'(?P<name>(' + name[0] + r'\s)?' + name[-1] + r's?)\b', '<a href="' + reverse('denker:detail', kwargs={'denker_slug': denk.slug}) + '">' + r'\g<name>' + '</a>', text)

    return text


def getDays():
    denker = Denker.objects.all()
    result = [[],[]]
    now = datetime.datetime.now() # date.today()
    # now = datetime.date(2017, 1, 1)
    for denk in denker:
        if str(denk.geburt)[5:] == now.isoformat()[5:10]:
            result[0].append({
                        'denker': denk,
                        'years': now.year-denk.geburt.year,
                        })
            continue;
        if str(denk.tod)[5:] == now.isoformat()[5:10]:
            result[1].append({
                        'denker': denk,
                        'years': now.year-denk.tod.year,
                        })
    return result
