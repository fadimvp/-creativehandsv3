from django import template
from product.models import Product

register = template.Library()
@register.inclusion_tag('product/tt.html')
def tt():
    context = {
      'dd': Product.objects.all()

          }
    return context