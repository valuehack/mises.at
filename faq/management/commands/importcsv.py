from django.core.management.base import BaseCommand, CommandError
from faq.models import Glossar
import csv
import codecs

# Reset Counter of primary key:
# delete from faq_glossar;
# delete from sqlite_sequence where name='faq_glossar';


class Command(BaseCommand):
    help = "Imports the Glossar CSV"

    def glossar(self):
        f = codecs.open("/Users/merlin/mises.at/Glossar_mises_at.csv", "r", encoding='utf-8', errors='replace')

        reader = csv.reader(f)
        for row in reader:
            if len(row) == 0:
                continue
            elif len(row) < 2:
                _, created = Glossar.objects.get_or_create(begriff=row[0], beschreibung="TODO")
                print("done.")
            else:
                _, created = Glossar.objects.get_or_create(begriff=row[0], beschreibung=row[1],)
                print("done.")

    def handle(self, *args, **options):
        self.glossar()
