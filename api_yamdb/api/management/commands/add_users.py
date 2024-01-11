import csv

from django.core.management.base import BaseCommand, CommandError
from api.models import User


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('input_file', type=str, nargs='?', default='static/data/users.csv')

    def handle(self, *args, **options):
        file_path = options['input_file']
        try:
            with open(file_path, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                titles = next(spamreader)
                for row in spamreader:
                    kwargs = dict(zip(titles, row))
                    User.objects.get_or_create(**kwargs)
            print("Succesfulyy added users")
        except Exception as exc_str:
            raise CommandError(f'Cannot add users: {exc_str}')
