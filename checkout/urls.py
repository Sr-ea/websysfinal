from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('confirm/', views.checkout_confirm, name='checkout_confirm'),
    path('success/<int:order_id>/', views.checkout_success, name='checkout_success'),
]
