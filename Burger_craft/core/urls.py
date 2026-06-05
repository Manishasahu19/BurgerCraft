from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('burger/<int:pk>/', views.product_detail, name='detail'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/update/<int:pk>/<str:action>/', views.update_cart_qty, name='update_cart_qty'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('about/', views.about, name='about'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment-success/', views.payment_success, name='payment_success'),
]
