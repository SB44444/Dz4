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
        # order = Order(customer=customer, products=product, total_price=Product.self.price * Product.self.store)

        order.save()
        self.stdout.write(f'Заказ клиента {Product.self.id}:  {order}')

        # customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Клиент
        # products = models.ManyToManyField(Product)  # продукт этого заказа
        # date_ordered = models.DateTimeField(auto_now_add=True)  # Дата заказа
        # total_price = models.DecimalField(max_digits=8, decimal_places=2)  # Сумма заказа
