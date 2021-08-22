from django.urls import path
from . import views
app_name ='cart'
urlpatterns = [
    path('', views.CartView, name='cart_item'),                           # to home page or display all products
    path('v/', views.v, name='v'),                           # to home page or display all products
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),  # to home page or display all products
    path('remove_cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name='remove_cart'),  # to remove product item from cart
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),  # to remove item from cart
    path('checkout/', views.checkout, name='checkout'),  # checkout

]
