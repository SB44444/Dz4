from django.core.management.base import BaseCommand, CommandParser
from ... models import User


class Command(BaseCommand):
    help = "Delete the user."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('user_id', type=int, help='user id')

    def handle(self, *args, **kwargs):
        user_pk = kwargs['user_id']
        user = User.objects.filter(u_pk=user_pk).first()
        user.delete()
        self.stdout.write(f'Клиент {self.style.ERROR(user.pk)}: {user} удалён')

        # self.stdout.write(self.style.ERROR(f'{user} deleted'))
