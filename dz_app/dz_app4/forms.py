from django import forms
from .models import Product, User


class LoginForm(forms.Form):
    name = forms.CharField(label='Имя пользователя', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, min_length=6)


class RegistrationForm(forms.Form):
    name = forms.CharField(label='Имя пользователя', max_length=100)
    email = forms.EmailField(label='Электронная почта')
    password = forms.CharField(widget=forms.PasswordInput, min_length=3)
    tel = forms.CharField(label='Телефон', max_length=20)
    adress = forms.CharField(label='Адрес доставки', max_length=150)


class UserForm(forms.Form):  # Товар
    # client = forms.ModelChoiceField(queryset=User.objects.all())
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
    # product = forms.ModelChoiceField(queryset=Product.objects.all())
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
