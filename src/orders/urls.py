from django.urls import path
from . import views
from django.contrib import admin
app_name = 'orders'
urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('payments/', views.payments, name='payments'),
    path('order_complete/', views.order_complete, name='order_complete'),

]
admin.site.site_title = "Your App Title"
admin.site.site_header = "creativehands"