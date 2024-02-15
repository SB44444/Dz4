import logging

from django.core.management.base import BaseCommand
from ... models import User

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create user."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Имя заказчика")
        parser.add_argument('email', type=str, help="email заказчика")
        parser.add_argument('adress', type=str, help="Адрес заказчика")
        parser.add_argument('tel', type=str, help="Телефон заказчика")
        parser.add_argument('adress', type=str, help="Дата первого визита заказчика")
        parser.add_argument('birthday', type=str, help="Комментарии")

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        tel = kwargs.get('tel')
        adress = kwargs.get('adress')
        date_visit = kwargs.get('date_visit')
        about = 'about'

        user = User(name=name, email=email, adress=adress, tel=tel, date_visit=date_visit, about=about)

        user.save()
        self.stdout.write(f'Создан закзчик:{user}')
        logger.info('User created')

    # def handle(self, *args, **kwargs):
    #     # user = User(name='Ivan', email='ivan@big.com', adress='Street 1', tel='+7(900)521-65-44', about='Хороший клиент')
    #     user = User(name='Igor', email='igor@big.com', adress='Street 3', tel='+7(900)521-11-33', about='Хороший клиент')
    #     # user = User(name='Oleg', email='oleg@big.com', adress='Street 2', tel='+7(900)521-00-22', about='Хороший клиент')
    #     user.save()
    #     self.stdout.write(f'{user}')
