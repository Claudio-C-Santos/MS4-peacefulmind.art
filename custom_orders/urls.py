from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.custom_orders, name='custom_orders'),
    path('pending_orders/', views.pending_orders, name='pending_orders'),
    path('custom_order_details/<int:custom_order_id>/', views.custom_order_details, name='custom_order_details'),
    path('custom_order_completed/<int:custom_order_id>/', views.custom_order_completed, name='custom_order_completed'),
]