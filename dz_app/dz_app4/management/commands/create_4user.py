from django.core.management.base import BaseCommand
from ... models import User
# from dz_app4.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        # user1 = User(name='Ivan', email='ivan@big.com', adress='Street 1', tel='+7(900)521-65-44', about='Хороший клиент')
        # user2 = User(name='Igor', email='igor@big.com', adress='Street 3', tel='+7(900)521-11-33', about='Хороший клиент')
        user3 = User(name='Oleg', email='oleg@big.com', adress='Street 2', tel='+7(900)521-00-22', about='Хороший клиент')
        user3.save()
        self.stdout.write(f'Create user: {user3}')
        # users = [user1, user2, user3] # objects.bulk_create(users)
        # for user in users:
        #     # assert isinstance(user, object)
        #     user.save()
        #     self.stdout.write(f'{user}')

        # name = models.CharField(max_length=100)
        # email = models.EmailField()
        # adress = models.CharField(max_length=100)
        # tel = models.CharField(max_length=20)
        # date_visit = models.DateTimeField(auto_now_add=True)
        # about = models.TextField()
