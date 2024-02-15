from django.contrib import admin
from .models import User, Product, Order  # Category


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'tel', 'date_visit', 'adress']  # Отображаемые поля
    ordering = ['name', 'date_visit', 'adress']  # Сортировка по строкам
    list_filter = ['name', 'email', 'tel', 'date_visit', 'adress']  # Список отбора по строкам
    search_fields = ['name', 'email', 'tel', 'date_visit', 'adress']  # Список строк для поиска
    search_help_text = "Поиск возможен по: 'name', 'email', 'tel', 'date_visit', 'adress'"  # Текст справки
    # readonly_fields = ['id']  # Поле только для чтения

    """Отдельный клиент"""
    # fields = ['name', 'email', 'tel', 'date_visit', 'adress']
    readonly_fields = ['date_visit']  # Поле только для чтения

    fieldsets = [
        (
            'User',
            {
                'classes': ['wide'],
                'fields': ['name', 'email'],
            },
        ),
        (
            'Контакты',
            {
                'classes': ['collapse'],
                'description': 'Contact information',
                'fields': ['tel', 'address'],
            },
        ),
        (
            'Other info',
            {
                'description': 'Описание',
                'fields': ['about'],
            }
        ),
    ]


@admin.action(description='Сбросить или задать количество')
def reset_store(modeladmin, request, queryset):
    queryset.update_or_create(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'store', 'date_receipt']  # Отображаемые поля
    ordering = ['name', 'price', 'date_receipt', 'store']  # Сортировка по строкам
    list_filter = ['name', 'price', 'store', 'date_receipt']  # Список отбора по строкам
    search_fields = ['name', 'price', 'date_receipt']  # Список строк для поиска
    search_help_text = "Поиск возможен по: 'name', 'price', 'date_receipt'"  # Текст справки
    readonly_fields = ['image_field']  # Поле только для чтения # (добавить 'id')

    actions = [reset_store]  # Ф-ция массового сброса/установки количества товара, по умолчанию 0

    fieldsets = [
        (
            'Продукт',
            {
                'classes': ['wide'],
                'fields': ['name', 'price', 'store'],
            },
        ),
        (
            'Подробнее',
            {
                'classes': ['collapse'],
                'description': 'Contact information',
                'fields': ['date_receipt'],
            },
        ),
        (
            'Дополнительно',
            {
                'classes': ['collapse'],
                'description': 'Дополнительная информация',
                'fields': ['description', 'image_field'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'date_ordered']  # Отображаемые поля
    ordering = ['customer', 'total_price', '-date_ordered']  # Сортировка по строкам
    list_filter = ['customer', 'total_price', 'date_ordered']  # Список отбора по строкам
    search_fields = ['customer', 'total_price', 'date_ordered']  # Список строк для поиска
    search_help_text = "Поиск возможен по: 'customer', 'total_price', 'date_ordered'"  # Текст справки
    # readonly_fields = ['id']  # Поле только для чтения

    fieldsets = [
        (
            'Заказ',
            {
                'classes': ['wide'],
                'fields': ['customer', 'total_price', 'date_ordered'],
            },
        ),
        (
            'Дополнительно',
            {
                'classes': ['collapse'],
                'description': 'Список продуктов в заказе',
                'fields': ['products'],
            }
        ),
    ]


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
