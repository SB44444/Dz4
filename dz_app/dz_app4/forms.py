from django import forms
from . models import Product, User


class UserForm(forms.Form):  # Товар
    client = forms.ModelChoiceField(queryset=User.objects.all())
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите имя пользователя'}))
    adress = forms.CharField(max_length=100,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите свой адрес'}))
    tel = forms.CharField(max_length=20,
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    date_visit = forms.DateTimeField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    about = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Комментарии"}))


class ProductForm(forms.Form):  # Товар
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите название продукта'}))
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    description_product = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Описание товара"}))
    store = forms.IntegerField(min_value=0)
    date_receipt = forms.DateTimeField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"placeholder": "Картинка товара"}))


class ImageForm(forms.Form):  # foto Товара
    image = forms.ImageField()


class ChoiceProductById(forms.Form):  # id Товара
    id_product = forms.IntegerField()


class ChoiceProductByClientBydays(forms.Form):  # User
    id_client = forms.IntegerField()
    days = forms.IntegerField()

# class OrderForm(forms.Form):  # Заказ
#     customer = forms.ModelChoiceField(queryset=User.objects.all())
#     products = forms.ModelChoiceField(queryset=Product.objects.all())
#     date_ordered = forms.DateTimeField(auto_now_add=True)
#     total_price = forms.DecimalField(max_digits=8, decimal_places=2)
