from django.contrib import admin
from .models import ProductTable,Size,Colour,BrandName,User, cart
# Register your models here.
admin.site.register(ProductTable)
admin.site.register(Size)
admin.site.register(Colour)
admin.site.register(BrandName)
admin.site.register(User)
admin.site.register(cart)