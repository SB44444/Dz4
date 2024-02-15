from django.core.management.base import BaseCommand
from ... models import Order


class Command(BaseCommand):
    help = "Get all products."

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        self.stdout.write(f'{orders}')

        for order in orders:
            self.stdout.write(f'{self.style.ERROR(order.pk)}: {order}')
