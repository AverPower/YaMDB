import csv

from django.core.management.base import BaseCommand, CommandError
from titles.models import Title, Category, Genre


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--input_file', type=str)
        parser.add_argument('--model', type=str)

    def handle(self, *args, **options):
        try:
            file_path = options['input_file']
            model_name = options['model']
            if model_name == 'category':
                self.add_category(file_path)
            elif model_name == 'title':
                self.add_title(file_path)
            elif model_name == 'genre':
                self.add_genre(file_path)
            elif model_name == 'genre_title':
                self.add_genre_title(file_path)
        except Exception as exc_str:
            raise CommandError(f'Cannot add elements: {exc_str}')

    @staticmethod
    def add_category(file_path):
        with open(file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            titles = next(spamreader)
            for row in spamreader:
                kwargs = dict(zip(titles, row))
                Category.objects.get_or_create(**kwargs)
        print("Succesfulyy added categories")

    @staticmethod
    def add_genre(file_path):
        with open(file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            titles = next(spamreader)
            for row in spamreader:
                kwargs = dict(zip(titles, row))
                Genre.objects.get_or_create(**kwargs)
        print("Succesfulyy added genres")

    @staticmethod
    def add_title(file_path):
        with open(file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            titles = next(spamreader)
            for row in spamreader:
                kwargs = dict(zip(titles, row))
                kwargs['category'] = Category.objects.get(id=kwargs['category'])
                Title.objects.get_or_create(**kwargs)
        print("Succesfulyy added titles")

    @staticmethod
    def add_genre_title(file_path):
        with open(file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            titles = next(spamreader)
            for row in spamreader:
                kwargs = dict(zip(titles, row))
                title_id = kwargs['title_id']
                title = Title.objects.get(id=title_id)
                genre_id = kwargs['genre_id']
                genre = Genre.objects.get(id=genre_id)
                title.genres.add(genre)
                title.save()
        print("Succesfulyy added genre titles")
