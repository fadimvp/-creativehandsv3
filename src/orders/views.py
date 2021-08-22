from django.contrib import messages
from django.http import HttpResponse
import urllib.request
import json
from django.shortcuts import render, redirect
from cart.models import CartItems
from .forms import OrderForm
import geoip2.database
# Create your views here.
from .models import Order
import datetime


def place_order(request, total=0, quantity=0):
    current_user = request.user
    # if cart count is less than or equal to 0 ,then redirect back to shop
    cart_items = CartItems.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('/')
    tax = 0
    total_tex = 0
    for cart_item in cart_items:
        total += (cart_item.product.PRDPrice * cart_item.quantity)
        quantity += cart_item.quantity
    total_tex = (total + tax)
    print(cart_item, "=====================form1=============")
    data = Order()

    if data.i_agree != True:
        messages.success(request, 'thank you for order  ')

        if request.method == 'POST':
            form = OrderForm(request.POST)

            if form.is_valid() and data.i_agree != True:

                data = Order()

                data.user = current_user
                data.first_name = form.cleaned_data['first_name']
                data.last_name = form.cleaned_data['last_name']
                data.phone = form.cleaned_data['phone']
                data.email = form.cleaned_data['email']
                data.address_1 = form.cleaned_data['address_1']
                data.address_2 = form.cleaned_data['address_2']
                data.country = form.cleaned_data['country']
                data.state = form.cleaned_data['state']
                data.city = form.cleaned_data['city']
                data.order_note = form.cleaned_data['order_note']
                data.total = total_tex
                data.tax = tax
                src = urllib.request.urlopen("https://api.ipify.org/?format=json")
                getsrc = src.read()
                print(getsrc, "=====================")
                d = json.loads(getsrc)
                json.dumps(d)
                data.ip = d
                print(d)

                if data.i_agree != True:
                    data.i_agree = form.cleaned_data['i_agree']
                    data.i_agree == True
                    print('=======================i_agree=======', data.i_agree)
                    data.save()

                else:
                    print('=======================else =======', data.i_agree)

                    data.save()

                data.save()

                # Generate odder number

                yr = int(datetime.date.today().strftime('%Y'))
                mt = int(datetime.date.today().strftime('%m'))
                dt = int(datetime.date.today().strftime('%d'))
                d = datetime.date(yr, mt, dt)
                current_date = d.strftime('%Y%m%d')
                order_number = current_date + str(data.id)
                data.order_number = order_number
                data.save()
                order = Order.objects.get(user=current_user, is_order=False, order_number=order_number)
                context = {
                    'order': order,
                    'cart_items': cart_items,
                    'tax': tax,
                    'total': total,
                    'total_tex': total_tex,
                }
                return redirect('cart:checkout')
            return redirect('cart:checkout')
        else:
            return redirect('cart:checkout')


def payments(request):
    pass
