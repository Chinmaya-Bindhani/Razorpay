from django.contrib import admin
from .models import Product,Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','stock']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','amount','razorpay_order_id','razorpay_payment_id','razorpay_signature','is_paid','created_at']
    list_filter = ['is_paid','created_at']