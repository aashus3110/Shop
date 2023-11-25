from django.contrib import admin
from app.models import Product,Category,Sub_Category,Orders,OrderUpdate

# Register your models here.

admin.site.register(Product),
admin.site.register(Category),
admin.site.register(Sub_Category),
admin.site.register(Orders),
admin.site.register(OrderUpdate),


