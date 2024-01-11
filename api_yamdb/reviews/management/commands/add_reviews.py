import csv

from django.core.management.base import BaseCommand, CommandError
from reviews.models import Review, Comment
from titles.models import Title
from api.models import User


def mean(array: list):
    _sum = sum(array)
    _len = len(array)
    return _sum // _len


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--input_file', type=str)
        parser.add_argument('--model', type=str)

    def handle(self, *args, **options):
        try:
            file_path = options['input_file']
            model_name = options['model']
            if model_name == 'review':
                self.add_review(file_path)
            elif model_name == 'comment':
                self.add_comment(file_path)
        except Exception as exc_str:
            raise CommandError(f'Cannot add elements: {exc_str}')

    @staticmethod
    def add_review(file_path):
        with open(file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            titles = next(spamreader)
            for row in spamreader:
                kwargs = dict(zip(titles, row))
                title = Title.objects.get(id=kwargs['title_id'])
                kwargs['title'] = title
                kwargs.pop('title_id')
                kwargs['author'] = User.objects.get(id=kwargs['author'])
                Review.objects.get_or_create(**kwargs)
                title.rating = mean(Review.objects.filter(title=title).values_list('score', flat=True))
                title.save()
        print("Succesfulyy added reviews")

    @staticmethod
    def add_comment(file_path):
        with open(file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            titles = next(spamreader)
            for row in spamreader:
                kwargs = dict(zip(titles, row))
                review = Review.objects.get(id=kwargs['review_id'])
                kwargs['review'] = review
                kwargs.pop('review_id')
                kwargs['author'] = User.objects.get(id=kwargs['author'])
                Comment.objects.get_or_create(**kwargs)
        print("Succesfulyy added comments")
