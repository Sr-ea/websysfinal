from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('products/', views.dashboard_products, name='dashboard_products'),
    path('products/add/', views.dashboard_product_add, name='dashboard_product_add'),
    path('products/<int:product_id>/edit/', views.dashboard_product_edit, name='dashboard_product_edit'),
    path('products/<int:product_id>/delete/', views.dashboard_product_delete, name='dashboard_product_delete'),
    path('orders/', views.dashboard_orders, name='dashboard_orders'),
    path('orders/<int:order_id>/status/', views.dashboard_order_status, name='dashboard_order_status'),
    path('categories/', views.dashboard_categories, name='dashboard_categories'),
    path('categories/add/', views.dashboard_category_add, name='dashboard_category_add'),
    path('categories/<int:category_id>/edit/', views.dashboard_category_edit, name='dashboard_category_edit'),
    path('categories/<int:category_id>/delete/', views.dashboard_category_delete, name='dashboard_category_delete'),
]
