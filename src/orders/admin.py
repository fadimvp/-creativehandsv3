from django.contrib import admin
from .models import Payment,Order,OrderProduct
# Register your models here.
class OrderInline(admin.TabularInline):
    model = OrderProduct
    extra = 0
class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','payment_id','payment_method','amount_paid','status','created_at','order_number']
    list_filter = ['payment_method']
    search_fields = ['user','order']
    list_per_page = 15


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','payment','order_number','first_name','last_name','email','is_order']
    list_filter = ['status','payment',]
    search_fields = ['order_number','email','phone']
    list_per_page = 20
    inlines = [OrderInline]

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user','payment','order','quantity','product_price','ordered','created_at','updated_at']
    list_filter = ['ordered','user']
    search_fields = ['product_price','payment']
    list_per_page = 15

admin.site.register(Payment,PaymentAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)