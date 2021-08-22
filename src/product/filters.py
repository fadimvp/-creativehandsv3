import django_filters

from .models import *


class Product_list_filter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields =  '__all__'
        exclude = ['CATImg']
