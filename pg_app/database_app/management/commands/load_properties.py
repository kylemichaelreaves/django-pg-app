from django.core.management import BaseCommand
from database_app.models import Property
import csv
import pdb

class Command(BaseCommand):
    help = 'Load properties csv into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'r') as f:
            data = list(csv.reader(f))
            for row in data[1:]:
                Property.objects.create(
                    property_id = row[0],
                    street_address = row[1],
                    owner_name = row[2],
                    owner_mailing_address = row[3],
                    city_state_zip = row[4],
                    property_full_address = row[5],
                    owner_full_mailing_address = row[6],
                    units_at_property = row[7],
                    g_code = row[8],
                    latitude = row[9],
                    longitude = row[10],
                    number_associated_properties = row[11],
                    #list_associated_properties = row[12]
                    )

