from django.core.management.base import BaseCommand, CommandParser
from ... models import Order, User, Product
# from datetime import datetime


class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('user_id', type=int, help='User id to order')
        parser.add_argument('product_id', type=int, help='Pruduct id in order')

    def handle(self, *args, **kwargs):
        user_pk = kwargs['user_id']
        product_pk = kwargs['product_id']

        customer = User.objects.filter(id=user_pk).first()
        product = Product.objects.filter(id=product_pk).first()

        order = Order(customer=customer, products=product, total_price=product.price * product.store)

        order.save()
        self.stdout.write(f'Заказ клиента {user_pk}:  {order}')
