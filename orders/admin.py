from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ['product_name', 'price', 'quantity']
    can_delete = False

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'full_name', 'total', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['full_name', 'user__username']
    inlines = [OrderItemInline]
    readonly_fields = ['user', 'full_name', 'email', 'address', 'city', 'postal_code', 'country', 'total']
