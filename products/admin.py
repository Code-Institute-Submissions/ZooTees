from django.contrib import admin

# Register your models here.
from .models import Product, Category, Collection


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "price",
        "image",
    )

    ordering = ("sku",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Collection)
