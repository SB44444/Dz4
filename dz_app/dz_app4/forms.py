from django import forms
from .models import User


class LoginForm(forms.Form):
    name = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'tel', 'adress']


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
