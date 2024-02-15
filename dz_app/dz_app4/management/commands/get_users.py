from django.core.management.base import BaseCommand
from ... models import User


class Command(BaseCommand):
    help = "Get all users."

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        self.stdout.write(f'{users}')

        for user in users:
            self.stdout.write(f'{self.style.ERROR(user.pk)}: {user}')
