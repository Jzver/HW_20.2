from django.contrib import admin

from catalog.models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'cost_product', 'category', 'imagery')
    list_filter = ('category',)
    search_fields = ('product_name', 'product_description',)
    list_editable = ('cost_product',)
    list_per_page = 50
    ordering = ('-id',)
