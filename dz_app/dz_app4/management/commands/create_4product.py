from django.core.management.base import BaseCommand
from ... models import Product


class Command(BaseCommand):
    help = "Create Product."

    def handle(self, *args, **kwargs):
        # product = Product(name='Pizza_Cheese', price=499, description='description', store=5)
        # product = Product(name='Pizza_Pepperoni', price=599, description='good pizza', store=3)
        product = Product(name='Pizza_Becon', price=549, description='good pizza', store=4)
        product.save()
        self.stdout.write(f'{product}')

