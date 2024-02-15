from django.core.management.base import BaseCommand
from ... models import User, Product, Order
from random import randint
import datetime
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generate fake orders"

    def add_arguments(self, parser):
        parser.add_argument('store', type=int, help='order creater')

    def handle(self, *args, **kwargs):
        store = kwargs.get('store')
        # store = 1
        customers = User.objects.all()
        products = Product.objects.all()
        products_lst = len(products)
        clients_lst = len(customers)
        products_set = set()

        for _ in range(store):
            for _ in range(randint(1, 5)):
                products_set.add(products[randint(0, products_lst-1)])
            total_price = sum([product.price for product in products_set])

            order = Order(customer=customers[randint(0, clients_lst-1)],
                          total_price=total_price, date_ordered=datetime.date.today())
            order.save()

            for product in products_set:
                order.products.add(product)

            products_set.clear()

            self.stdout.write(self.style.SUCCESS(f'Order created: {order}'))
        logger.info('Orders created')

