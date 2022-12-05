from django.contrib import admin
from . models import Product, Variation

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ['product_name', 'slug', 'price', 'stock','created_date', 'is_available']
    list_display_links = ['product_name', 'slug']

class VariationAdmin(admin.ModelAdmin):
    list_display = ['product', 'variation_category', 'variation_value', 'is_active']
    list_display_links = ['product', 'variation_category']
    list_editable = ['is_active']

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)