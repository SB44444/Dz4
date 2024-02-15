
from django.core.management.base import BaseCommand, CommandParser
from ... models import User


class Command(BaseCommand):
    help = "Update user name by id."

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('adress', type=str, help='User adress')
        parser.add_argument('tel', type=str, help='User tel')
        parser.add_argument('about', type=str, help='User about')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        adress, tel, about = kwargs.get('adress'), kwargs.get('tel'), kwargs.get('about')
        user = User.objects.filter(pk=pk).first()
        user.name = name
        user.adress, user.tel, user.about = adress, tel, about
        user.save()
        self.stdout.write(f'{user}')

        # email = models.EmailField()
