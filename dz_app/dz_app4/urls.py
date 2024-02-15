from django.urls import path
from . import views
from . views import update_product, update_client, upload_image


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('user/add/', update_client, name='update_client'),
    path('product/add/', update_product, name='update_product'),
    # path('update_product/', views.update_product, name='update_product'),
    path('get_product/<int:pk>', views.get_product, name='get_product'),
    path('get_products/', views.get_products, name='products'),
    path('get_users/', views.get_users, name='users'),
    path('user_products/<int:client_id>/<int:days_num>', views.all_user_products, name='all_user_products'),
    path('get_customer_orders/<int:pk>', views.get_customer_orders, name='get_customer_orders'),
    path('get_user_order/<int:product_id>', views.get_user_order, name='get_user_order'),
    path('get_order/<int:pk>', views.get_order, name='get_order'),
    path('upload_image/<int:product_id>', upload_image, name='upload_image')
    ]
