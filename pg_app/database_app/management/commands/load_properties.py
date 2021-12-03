from django.core.management import BaseCommand
from database_app.models import Property
import csv

class Command(BaseCommand):
    help = 'Load properties csv into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            data = list(csv.reader(f))
            for row in data[1:]:
                Property.objects.create(
                    # steet_address = row[0],
                    owner_name = row[1],
                    owner_mailing_address = row[2],
                    city_state_zip = row[3],
                    property_full_address = row[4],
                    owner_full_mailing_address = row[5],
                    units_at_property = row[6],
                    g_code = row[7],
                    latitude = row[8],
                    longitude = row[9],
                    number_associated_properties = row[10],
                    list_associated_properties = row[11]
                )

