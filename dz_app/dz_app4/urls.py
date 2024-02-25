from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
from .views import upload_image, add_user, add_product, product_list, view_cart, add_to_cart, remove_from_cart, home
app_name = 'cart'

urlpatterns = [
    path('', views.product_list, name="index"),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('/home', views.home, name='home'),
    # path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('user/add/', add_user, name='add_user'),
    path('admin/dz_app4/user/add/', add_user, name='add_user'),
    path('product/add/', add_product, name='add_product'),
    path('admin/dz_app4/product/add/', add_product, name='add_product'),
    path('update_product/', views.update_product, name='update_product'),
    path('update_client/', views.update_client, name='update_client'),
    path('add/1/', views.update_client, name='update_client'),
    path('get_product/<int:pk>', views.get_product, name='get_product'),
    path('get_products/', views.get_products, name='get_products'),
    path('get_users/', views.get_users, name='users'),
    path('user_products/<int:client_id>/<int:days_num>', views.all_user_products, name='all_user_products'),
    path('get_customer_orders/<int:pk>', views.get_customer_orders, name='get_customer_orders'),
    path('get_user_order/<int:product_id>', views.get_user_order, name='get_user_order'),
    path('get_order/<int:pk>', views.get_order, name='get_order'),
    path('get_media/', views.get_media, name='get_media'),
    path('upload_image/<int:product_id>', upload_image, name='upload_image')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
