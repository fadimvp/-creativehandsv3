from django.urls import path

from . import views
app_name ='product'
urlpatterns = [
    path('', views.Product_list, name='pro_list'),                           # to home page or display all products
    path('product', views.All_products, name='all_pro'),                     # all products
    path('<slug:slug>', views.Product_detail, name='pro_detail'),            # display detail and view slug name products
    path('tt/<slug:slug>', views.tt, name='tt'),            # display detail and view slug name products
    path('store/<slug:category_slug>', views.store, name='category_slug'),   # view category with name category in slug this good in seo with google
    path('store/', views.store, name='store'),                               # view all categories

    path('search/', views.search, name='search'),
]
