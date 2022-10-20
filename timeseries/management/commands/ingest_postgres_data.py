from django.core.management.base import BaseCommand, CommandError
import csv
from ...models import Metric
import datetime
# from django.contrib.gis.geos import Point

class Command(BaseCommand):
    help = 'Imports data for Postgres'

    def add_arguments(self, parser):
        parser.add_argument('-d', '--data_file', type=str, help='Data file to input')

    def handle(self, *args, **options):
        csv_file = open(options['data_file'], 'r')
        csv_obj = csv.DictReader(csv_file)

        for row in csv_obj:
            # create a new metric for each row
            # point_obj = Point(
            #     float(row['longitude']),
            #     float(row['latitude'])
            # )
            Metric.objects.create(
                time=datetime.datetime.strptime(row['timestamp']+'+0000', '%Y-%m-%d %H:%M:%S.%f%z'),
                latitude=row['latitude'],
                longitude=row['longitude']
            )