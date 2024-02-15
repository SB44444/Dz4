
from django.core.management.base import BaseCommand, CommandParser
from ... models import User


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')
