from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_dipslay = ['__str__', 'slug']
    class Meta:
        model = Product
        
admin.site.register(Product, ProductAdmin)