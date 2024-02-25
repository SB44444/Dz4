from django.db import models
from django.conf import settings


class User(models.Model):  # Клиент
    name = models.CharField(max_length=100)
    email = models.EmailField()
    adress = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    date_visit = models.DateTimeField(auto_now_add=True)
    about = models.TextField(null=True, default=None, max_length=200)

    def __str__(self):
        return (f'Клиент: {self.name}, почта: {self.email}, адрес: {self.adress}, телефон: {self.tel},/'
                f'дата_визита: {self.date_visit}, коментарии: {self.about}')


class Product(models.Model):  # Товар
    name = models.CharField(max_length=100)  # Название
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Цена
    description = models.TextField()  # Описание
    date_receipt = models.DateTimeField(auto_now_add=True)  # Дата получения
    store = models.IntegerField(default=0)  # Количество
    image_field = models.ImageField(null=True, blank=True, default=None, upload_to='media/')  # Фото

    def __str__(self):
        return (f'товар: {self.name}, цена: {self.price}, описание: {self.description},/'
                f'дата_прихода: {self.date_receipt}, количество: {self.store}')


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    status_cart = models.CharField(max_length=20, default='формируется')
    # cart_item_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    # @property
    # def item_price(self, product):
    #     cart_item_price = product.price * self.quantity
    #     return cart_item_price

    def __str__(self):
        return f'CartItem: {self.product.name}, quantity: {self.quantity}'
        # return f'CartItem: {self.product}, quantity: {self.quantity}, cart_item_price: {self.cart_item_price}'


class Order(models.Model):  # Заказ
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Клиент
    products = models.ManyToManyField(Product)  # продукт в заказе
    date_ordered = models.DateTimeField(auto_now_add=True)  # Дата заказа
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)  # Сумма заказа
    status_order = models.CharField(max_length=20, default='формируется')

    def get_total_price(self):
        return sum([products.cart_item_price for products in self.products.all()])

    def __str__(self):
        return (f'Клиент: {self.customer}, '
                f'\nТовар: {self.products}, '
                f'\nДата_заказа: {self.date_ordered}, '                
                f'\nСумма: {self.total_price}')


# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(CartItem)
#     cart_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
#     status_cart = models.CharField(max_length=20, default='формируется')
#
#     def add_item(self, product, quantity):
#         cart_price = product.price * quantity
#         if not self.products.filter(product=product).exists():
#             cart_item = CartItem.objects.create(
#                 cart=self, product=product, quantity=quantity, cart_price=cart_price)
#             self.products.add(cart_item)
#         else:
#             existing_item = self.products.get(product=product)
#             existing_item.quantity += quantity
#             existing_item.cart_price += existing_item.price * quantity
#             existing_item.save()
#
#     def remove_item(self, product):
#         if self.products.filter(product=product).exists():
#             self.products.get(product=product).delete()
#
#     @property
#     def clear(self):
#         self.products.all().delete()
#
#     # def get_total_quantity(self):
#     #     return sum([product.quantity for product in self.products.all()])
#
#     def get_total_price(self):
#         return sum([product.cart_item_price for product in self.products.all()])
#
#     def __str__(self):
#         return f'Cart: {self.user}, products: {self.products}'


class Gallery(models.Model):
    name = models.CharField(max_length=400, db_index=True)
    image = models.ImageField(upload_to='media/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.image.url