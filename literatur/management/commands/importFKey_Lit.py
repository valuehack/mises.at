from django.core.management.base import BaseCommand, CommandError
from denker.models import Denker
from literatur.models import Artikel, Buecher

buecher = Buecher.objects.all()
artikel = Artikel.objects.all()

denker = Denker.objects.all()


class Command(BaseCommand):
    help = 'Imports Denker to Buecher and Artikel Models'

    def importKeys(self, Schrift):
        n = 0
        found = False
        failed = []
        authors = []
        for buch in Schrift:
            for denk in denker:
                if denk.name == buch.autor or denk.name == (buch.autor + " "):
                    buch.author = denk
                    buch.save()
                    print("Changed: " + str(buch.id) + " | " + buch.author.name + ": " + buch.titel)
                    found = True
                elif buch.author == denk:
                    print(str(buch.id) + " | " + buch.author.name + ": " + buch.titel)
                    found = True
                # elif buch.autor == "Joerg Guido Huelsmann" and denk.slug == "hulsmann":
                #     buch.author = denk
                #     buch.save()
                #     print("Changed: " + str(buch.id) + " | " + buch.author.name + ": " + buch.titel)
                #     found = True
                
                    
            if not found:
                print("FAILED: " + str(buch.id) + " | " + buch.autor + ": " + buch.titel)
                failed.append(buch)
                authors.append(buch.autor)
                n = n + 1
            else:
                found = False
        
        print(str(n) + " Authors missing:")
        print(list(set(authors)))
        
        print("FAILED IDs: ")
        for i in failed:
            print(str(i.id) + ", ", end="")
        print()

    def handle(self, *args, **options):
        self.importKeys(buecher)
        self.importKeys(artikel)
