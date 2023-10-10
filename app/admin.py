from django.contrib import admin
from .models import (
    Customer,Product,Cart,Orderplaced
)
# Register your models here.
@admin.register(Customer)
class Customermodeladmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']

@admin.register(Product)
class Productmodeladmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','description','brand','category','product_image']
    

@admin.register(Cart)
class Cartmodeladmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']


@admin.register(Orderplaced)
class Orderplacedmodeladmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','ordered_date','status']