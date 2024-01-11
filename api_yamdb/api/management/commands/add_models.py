from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            call_command('add_users')
            call_command('add_titles', '--model', 'category', '--input_file', 'static/data/category.csv')
            call_command('add_titles', '--model', 'genre', '--input_file', 'static/data/genre.csv')
            call_command('add_titles', '--model', 'title', '--input_file', 'static/data/titles.csv')
            call_command('add_titles', '--model', 'genre_title', '--input_file', 'static/data/genre_title.csv')
            call_command('add_reviews', '--model', 'review', '--input_file', 'static/data/review.csv')
            call_command('add_reviews', '--model', 'comment', '--input_file', 'static/data/comments.csv')
        except Exception as exc_str:
            raise CommandError(f'Cannot execute: {exc_str}')
