from itertools import chain
import os.path
from django.conf import settings


def createLink(qs):
    qs = list(qs)
    for i in qs:
        if i.quelle == "PDF":
            i.link = os.path.join(settings.STATIC_ROOT, 'literatur/' + i.typ + '/', i.slug) + ".pdf"
    return qs


def gen_werke(denker, rev=True):
    qs_literatur = chain(denker.buecher_set.all(), denker.artikel_set.all())
    qs_sorted = sorted(qs_literatur, key=lambda x: x.jahr, reverse=rev)
    return createLink(qs_sorted)


def splitlist(author_list):
    return [author_list[0:int(len(author_list) / 4)],
            author_list[int(len(author_list) / 4):int(len(author_list) / 2)],
            author_list[int(len(author_list) / 2):int(3 * len(author_list) / 4)],
            author_list[int(3 * len(author_list) / 4):len(author_list)]]
