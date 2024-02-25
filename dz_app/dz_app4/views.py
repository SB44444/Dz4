from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . models import User, Product, Order, Gallery, CartItem
from . forms import ImageForm, ProductForm, UserForm
import logging

logger = logging.getLogger(__name__)


def product_list(request):
    products = Product.objects.all()
    return render(request, 'dz_app4/index.html', {'products': products})


def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'dz_app4/cart.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')


def home(request):
    return HttpResponse('Hello, World!')


def index1(request):
    # return HttpResponse("Hello, world!")
    # logger.info('main get request')
    context = {'index1': ['Старт проекта интернет-мазина 4']}
    return render(request, 'dz_app4/index1.html', context=context)  # Главная


def about(request):
    # logger.info('main get request')
    context = {'about': ['Страница о сайте 4']}
    return render(request, 'dz_app4/about.html', context=context)  # О магаине


def get_product(request, pk):
    logger.info('Get product info')
    product = Product.objects.filter(pk=int(pk)).first()  # Добавить перенаправление при отсутствии ID
    return render(request, template_name='dz_app4/get_product.html', context={'product': product})  # Продукт по ID


def get_products(request):
    products = Product.objects.all()
    context = {'<br>'.join([str(products) for products in products])}  # Все продукты
    return render(request, template_name='dz_app4/get_products.html', context={'context': context})


def get_users(request):
    users = User.objects.all()
    context = {'<br>'.join([str(users) for users in users])}  # Все клиенты
    return render(request, template_name='dz_app4/get_products.html', context={'context': context})


def get_order(request, pk):
    logger.info('Page about selected order accessed')
    order = Order.objects.filter(pk=int(pk)).first()
    products = order.products.get()
    html = f"""
    <body>        
        { order } { products }
    </body>
    """
    return HttpResponse(html)


def get_customer_orders(request, pk):
    customer = User.objects.filter(pk=int(pk)).first()
    orders = Order.objects.filter(customer=customer).all()

    logger.info("Page about client's orders accessed")
    return render(request, template_name='dz_app4/order.html', context={'orders': orders, 'customer': customer, })


def get_user_order(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(client=user)
    return render(request, 'dz_app4/all_user_order.html', {'user': user, 'order': orders})


def all_user_products(request, pk):
    order = Order.objects.filter(pk=int(pk)).first()
    products = order.products.all()
    logger.info("Page about products in the order accessed")
    return render(request, template_name='dz_app4/products.html', context={'order': order, 'products': products, })


def week_4order(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(client=user)
    return render(request, 'dz_app4/week_user_orders.html', {'order': orders})


def month_4order(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(client=user)
    return render(request, 'dz_app4/month_user_orders.html', {'order': orders})


def year_4order(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(client=user)
    return render(request, 'dz_app4/year_user_orders.html', {'order': orders})


def user_4order_in_year(request):
    users = User.objects.all()
    out_str = '<br>'.join([str(users) for users in users])
    return HttpResponse(out_str)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        message = 'Повторите ввод данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            date_receipt = form.cleaned_data['date_receipt']
            store = form.cleaned_data['store']
            product = Product(name=name, price=price, description=description, date_receipt=date_receipt, store=store)
            product.save()
            message = 'Данные успешно сохранены'
            logger.info(f"Обновлен подукт: {name}, цена:{price}, дата поступления:{date_receipt}, количество:{store}")
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'dz_app4/update_product.html', {'form': form, 'message': message})


def update_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        message = 'Повторите ввод данных'
        if form.is_valid():
            product = form.cleaned_data['name']
            product_name = product.name
            updated_product = Product.objects.filter(name=product_name).first()

            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            date_receipt = form.cleaned_data['date_receipt']
            store = form.cleaned_data['store']

            updated_product.name = name
            updated_product.price = price
            updated_product.description = description
            updated_product.date_receipt = date_receipt
            updated_product.store = store
            updated_product.save()
            message = 'Данные успешно сохранены'
            logger.info(f"Обновлен подукт: {name}, цена:{price}, дата поступления:{date_receipt}, количество:{store}")
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'dz_app4/update_product.html', {'form': form, 'message': message})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Повторите ввод данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            adress = form.cleaned_data['adress']
            tel = form.cleaned_data['tel']
            date_visit = form.cleaned_data['date_visit']
            about_ = form.cleaned_data['about']

            client = User(name=name, email=email, adress=adress, tel=tel, date_visit=date_visit, about=about_)
            client.save()
            message = 'Данные успешно сохранены'
            logger.info(
                f"Добавлен пользователь: {name}, {email}, телефон:{tel}, {adress}, {date_visit}, комментарии:{about_}")
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'dz_app4/update_client.html', {'form': form, 'message': message})


def update_client(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Повторите ввод данных'
        if form.is_valid():
            client = form.cleaned_data['name']
            # client = form.cleaned_data['product']
            client_name = client.name
            updated_client = User.objects.filter(name=client_name).first()

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            adress = form.cleaned_data['adress']
            tel = form.cleaned_data['tel']
            date_visit = form.cleaned_data['date_visit']
            about_ = form.cleaned_data['about']

            updated_client.name = name
            updated_client.email = email
            updated_client.adress = adress
            updated_client.tel = tel
            updated_client.date_visit = date_visit
            updated_client.about_ = about_
            updated_client.save()
            message = 'Данные успешно сохранены'
            logger.info(f"Измение данных:: {name}, телефон:{tel}, комментарии:{about_}")
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'dz_app4/update_client.html', {'form': form, 'message': message})


def upload_image(request, product_id):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product.objects.filter(pk=product_id).first()
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            product.image_field = fs.save(image.name, image)
            product.save()
            logger.info("Изображение успешно сохранено")
    else:
        form = ImageForm()
    return render(request, 'dz_app4/upload_image.html', {'form': form})


def get_media(request):
    media = Gallery.objects.all()
    return render(request, 'dz_app4/get_media.html', {'media': media})
