import csv
import json
from copy import copy
from datetime import datetime

from django.core.management import BaseCommand

from scrapers.manolo_scraper.pipelines import process_item, save_item
from scrapers.manolo_scraper.utils import get_dni, make_hash
from visitors.models import Visitor


class Command(BaseCommand):
    help = "Save items from PCM downloaded as CSV. Update them if the are missing DNI"

    def add_arguments(self, parser):
        parser.add_argument('-i', '--input', action='store')

    def handle(self, *args, **options):
        input_file = options['input']
        save_items(input_file)


def save_items(input_file):
    print(f"processing {input_file}")

    with open(input_file) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            fecha = row['Fecha']
            fecha = datetime.strptime(fecha, '%d/%m/%Y')
            id_document, id_number = get_dni(row['Documento'])

            print(row['Funcionario Visitado'])
            triad = [
                i.strip() for i in row['Funcionario Visitado'].split('-')
            ]
            host_name = triad[0]
            office = " - ".join(triad[1:-1])
            host_title = triad[-1]

            lugar = row['Lugar']

            item = {
                'institution': 'pcm',
                'date': fecha,
                'full_name': row['Visitante'],
                'entity': row['Institucion del Visitante'],
                'reason': row['Motivo'],
                'host_name': host_name,
                "time_start": row['Hora Ingreso'],
                "time_end": row['Hora Salida'],
                "id_number": id_number,
                "id_document": id_document,
                "office": office,
                "host_title": host_title,
                "meeting_place": lugar,
            }
            item = make_hash(item)

            # get a dummy object to make hash and find in database
            dummy_item_for_hash = copy(item)
            dummy_item_for_hash['date'] = fecha.strftime('%d/%m/%Y')
            del dummy_item_for_hash['id_number']
            del dummy_item_for_hash['id_document']
            dummy_item_for_hash = make_hash(dummy_item_for_hash)
            dummy_hash = dummy_item_for_hash['sha1']

            try:
                incomplete_item = Visitor.objects.get(sha1=dummy_hash)
                incomplete_item.delete()
            except Visitor.DoesNotExist:
                pass

            save_item(item)
