from django.core.management import BaseCommand
from pg_app.models import Property
import csv

class Command(BaseCommand):
    help = 'Load properties csv into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f)
            for row in reader:
                Property.objects.create(
                    steet_address = row[0],
                    owner_name = row[1],
                    owner_mailing_address = row[2],
                    city_state_zip = row[3],
                    property_full_ownership = row[4],
                    number_properties_owned = row[5],
                    units = row[6],
                    g_code = row[7],
                    latitude = row[8],
                    longitude = row[9],
                    list_properties_owned = row[10]
                )

