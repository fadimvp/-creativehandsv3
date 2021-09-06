from django.contrib import messages
from django.http import HttpResponse, JsonResponse
import urllib.request
import json
from django.shortcuts import render, redirect
from cart.models import CartItems
from .forms import OrderForm
import geoip2.database
# Create your views here.
from .models import Order, Payment, OrderProduct
import datetime
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from product.models import Product


def place_order(request, total=0, quantity=0):
    current_user = request.user
    # if cart count is less than or equal to 0 ,then redirect back to shop
    cart_items = CartItems.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('/')
    tax = 0
    tax1 = 0
    total_tex = 0
    total1=0
    for cart_item in cart_items:
        tax=0
        quantity=0
        total += (cart_item.product.PRDPrice * cart_item.quantity)
        # total1 += (cart_item.product.PRDPrice * cart_item.quantity)
        quantity += cart_item.quantity
        tax1+= ( total) * (cart_item.product.tax)

        tax += ( total) * (cart_item.product.tax)
        print(tax,"test atx")
        print(tax1,"test atx")
        print(quantity,"test quantity")
        print(total,"test total")
        total_tex = (total + tax)
    print(cart_item, "=====================form1=============")
    data = Order()

    if data.i_agree != True:
        messages.success(request, 'thank you for order  ')

        if request.method == 'POST':
            form = OrderForm(request.POST or None)
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
                print(order.order_number)
                # reduce the quantity  of   the  sold   products
                cart_items = CartItems.objects.filter(user=request.user)
                for item in cart_items:
                    product = Product.objects.get(id=item.product_id)
                    product.stock -= item.quantity

                    product.save()
                    print(product,"test  product =======================")
                context = {
                    'data': data,
                    'order': order,
                    'cart_items': cart_items,
                    'tax': tax,
                    'total': total,
                    'total_tex': total_tex,
                }

            return render(request, 'payments.html', context)

        else:
            return redirect('cart:checkout')


def payments(request):
    # get data from js paypal API Response data
    body = json.loads(request.body or None)
    order = Order.objects.get(user=request.user, is_order=False, order_number=body['order_number'])
    print(body)
    payment = Payment(
        user=request.user,
        payment_id=body['transID'],
        payment_method=body['payment_method'],
        status=body['statUs'],
        order_number=body['order_number'],
        amount_paid=order.total,

    )
    payment.save()
    order.payment = payment
    order.is_order = True
    order.save()
    # move the cart items   to  order
    cart_items = CartItems.objects.filter(user=request.user)
    for item in cart_items:
        orderproduct = OrderProduct()
        orderproduct.order_id = order.id
        orderproduct.payment = payment
        orderproduct.user_id = request.user.id
        orderproduct.user = item.user

        orderproduct.quantity = item.quantity
        orderproduct.product_price = item.product.PRDPrice
        orderproduct.product_id = item.product_id
        orderproduct.ordered = True
        orderproduct.save()

        # save variations with  order product

        cart_item = CartItems.objects.get(id=item.id)
        product_variation = cart_item.variations.all()
        orderproduct = OrderProduct.objects.get(id=orderproduct.id)
        orderproduct.variations.set(product_variation)
        orderproduct.save()
        print(orderproduct)
        # reduce the quantity  of   the  sold   products
        # product = Product.objects.get(id=item.product_id)
        # product.stock -= item.quantity
        # product.save()

    # clear cart
    CartItems.objects.filter(user=request.user).delete()

    # send order received email to customer
    mail_subject = "please  activate your mail "
    message = render_to_string('order_recived_email.html', {
        'user': request.user,
        'order': order,

    })
    to_email = request.user.email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.send()
    # send order number  and   transaction id back to json response  api
    data = {
        'order_number': order.order_number,
        'transID': payment.payment_id

    }

    # return render(request, 'payments.html', context)
    return JsonResponse(data)


def order_complete(request):
    order_number = request.GET.get('order_number')

    print(order_number, "++++++++++++++++++++fffffffff")
    transID = request.GET.get('payment_id')
    payment = Payment.objects.get(payment_id=transID)
    print(transID)

    try:
        order = Order.objects.get(order_number=order_number, is_order=True)
        ordered_products = OrderProduct.objects.filter(order_id=order.id)

        tax = 0

        subtotal = 0
        for i in ordered_products:
            subtotal += i.product_price * i.quantity

            grandtotal =(subtotal)+(tax)
            print(tax, "++++++++++++++++++++fffffffff")

        context = {
            'order': order,
            'ordered_products': ordered_products,
            'order_number': order.order_number,
            'transID': payment.payment_id,
            'subtotal':subtotal,

            'grandtotal':grandtotal,

        }
        return render(request, 'order_complete.html', context)
    except (Payment.DoesNotExist, Order.DoesNotExist):
        return redirect('products:pro_list')
