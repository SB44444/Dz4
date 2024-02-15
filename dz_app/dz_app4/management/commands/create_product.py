import logging
from decimal import Decimal
from django.core.management.base import BaseCommand
from ...models import Product

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create Product."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Название продукта")
        parser.add_argument('price', type=Decimal, help="Цена продукта")
        parser.add_argument('description', type=str, help="Описание продукта")
        parser.add_argument('date_receipt', type=str, help="Дата поступления продукта")
        parser.add_argument('store', type=int, help="Количество продукта")
        parser.add_argument('image_field', type=str, help="Фото продукта")

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        price = kwargs.get('price')
        description = kwargs.get('description')
        date_receipt = kwargs.get('date_receipt')
        store = kwargs.get('store')
        image_field = kwargs.get('image_field')

        product = Product(name=name, price=price, description=description,
                          date_receipt=date_receipt, store=store, image_field=image_field)

        product.save()
        self.stdout.write(f'Создан продукт: {product}')
        logger.info('Product created')

    # def handle(self, *args, **kwargs):
    #     # product = Product(name='Pizza_Cheese', price=499, description='description', store=5)
    #     # product = Product(name='Pizza_Pepperoni', price=599, description='good pizza', store=3)
    #     product = Product(name='Pizza_Becon', price=549, description='good pizza', store=4)
    #     product.save()
    #     self.stdout.write(f'{product}')
