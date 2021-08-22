from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from django.urls import reverse
from product.models import Product, Variation, Alternative
from .models import Cart, CartItems
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def v(request):
    vv = Variation.objects.all()
    context = {
        'vv': vv
    }
    return render(request, 'cart.html', context)


def _cart_id(request):  # creat session id to cart
    cart = request.session.session_key
    if not cart:
        request.session.create()  # create new session
    return cart


def add_cart(request, product_id):  # get product.id to  url
    current_user = request.user
    product = Product.objects.get(id=product_id)
    # if the user is authenticated
    if current_user.is_authenticated:
        print("فى حاله عدم تغير ")

        product = Product.objects.get(id=product_id)
        product.stock -= 1                           # if you auth decrement one from stock
        if product.stock == -1:
            return redirect('cart:cart_item')
        product.save()

        product_variation = []
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]
                try:
                    variation = Variation.objects.get(product=product, variation_category__exact=key,
                                                      variation_vale__exact=value)
                    product_variation.append(variation)
                except:
                    pass

        is_cart_item_exists = CartItems.objects.filter(product=product, user=current_user).exists()
        if is_cart_item_exists:
            cart_item = CartItems.objects.filter(product=product, user=current_user)
            ex_var_list = []
            id = []
            for item in cart_item:
                exists_variation = item.variations.all()
                ex_var_list.append(list(exists_variation))
                id.append(item.id)
            print(exists_variation)
            if product_variation in ex_var_list:
                index = ex_var_list.index(product_variation)
                item_id = id[index]
                item = CartItems.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()
            else:
                item = CartItems.objects.create(product=product, quantity=1, user=current_user)
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)

                item.save()


        else:  # get all data from models and save all  class CartItems

            cart_item = CartItems.objects.create(
                product=product,
                quantity=1,
                user=current_user,
            )
            if len(product_variation) > 0:
                cart_item.variations.clear()

                cart_item.variations.add(*product_variation)

            cart_item.save()

        return redirect('cart:cart_item')

    else:
        product_variation = []
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]
                try:
                    variation = Variation.objects.get(product=product, variation_category__exact=key,
                                                      variation_vale__exact=value)
                    product_variation.append(variation)
                except:
                    pass

        try:
            cart = Cart.objects.get(
                cart_id=_cart_id(request))  # get the  cart using the cart_id present  in the session
            product = Product.objects.get(id=product_id)
            product.stock -= 1
            if product.stock == -1:
                return redirect('cart:cart_item')
            product.save()

            cart.save()
        except Cart.DoesNotExist:

            cart = Cart.objects.create(cart_id=_cart_id(request))
            # create cart same id session
        cart.save()  # save objects to database
        is_cart_item_exists = CartItems.objects.filter(product=product, cart=cart).exists()
        if is_cart_item_exists:

            product = Product.objects.get(id=product_id)
            cart_item = CartItems.objects.filter(product=product, cart=cart)
            ex_var_list = []
            id = []
            for item in cart_item:
                exists_variation = item.variations.all()
                ex_var_list.append(list(exists_variation))
                id.append(item.id)
            if product_variation in ex_var_list:
                index = ex_var_list.index(product_variation)
                item_id = id[index]
                item = CartItems.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()
            else:
                item = CartItems.objects.create(product=product, quantity=1, cart=cart)
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)

                item.save()


        else:  # get all data from models and save all  class CartItems

            cart_item = CartItems.objects.create(
                product=product,
                quantity=1,
                cart=cart,
            )
            if len(product_variation) > 0:
                cart_item.variations.clear()

                cart_item.variations.add(*product_variation)

            cart_item.save()

        return redirect('cart:cart_item')


# remove one item inside cart
def CartView(request, total=0, quantity=0, tax=0, cart_items=None):
    try:
        tax = 0
        if request.user.is_authenticated:

            cart_items = CartItems.objects.filter(user=request.user)
            for cart_item in cart_items:
                tax = 0
                total += (cart_item.product.PRDPrice * cart_item.quantity)
                quantity += cart_item.quantity
                tax += (total) * (cart_item.product.tax)

                print(total, "dklslfkds")
            total_tex = (total + tax)

        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))

            cart_items = CartItems.objects.filter(cart=cart)
            for cart_item in cart_items:
                total += (cart_item.product.PRDPrice * cart_item.quantity)
                quantity += cart_item.quantity
                tax += (total) * (cart_item.product.tax)
                print(total,"dklslfkds")
            total_tex = (total + tax)



    except ObjectDoesNotExist:
        total_tex = (total + tax)

    context = {
        'cart_items': cart_items,
        'quantity': quantity,
        'total': total,
        'tax': tax,
        'total_tex': total_tex,

    }
    return render(request, 'cart.html', context)


def remove_cart(request, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        if request.user.is_authenticated:
            cart_item = CartItems.objects.get(product=product, user=request.user, id=cart_item_id)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))

            cart_item = CartItems.objects.get(product=product, cart=cart, id=cart_item_id)
        cart_item.quantity -= 1

        print('bef', cart_item.quantity)
        print('befee', cart_item.quantity)
        product = Product.objects.get(id=product_id)
        product.stock += 1
        cart_item.save()
        print('aft stock', cart_item.quantity)

        product.save()
        if cart_item.quantity < 1:
            cart_item.delete()
    except:
        pass
    return redirect('cart:cart_item')


def remove_cart_item(request, product_id, cart_item_id):  # remove all items in related one product
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:
        cart_item = CartItems.objects.get(product=product, user=request.user, id=cart_item_id)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItems.objects.get(product=product, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect('cart:cart_item')

@login_required(login_url='account:login')
def checkout(request, total=0, quantity=0, tax=0, cart_items=None):
    try:
        total = 0
        quantity = 0
        tax = 0
        if request.user.is_authenticated:

            cart_items = CartItems.objects.filter(user=request.user)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))

            cart_items = CartItems.objects.filter(cart=cart)
        for cart_item in cart_items:
            total += (cart_item.product.PRDPrice * cart_item.quantity)
            quantity += cart_item.quantity
            tax += (total) * (cart_item.product.tax)
        total_tex = (total + tax)

    except ObjectDoesNotExist:
        total_tex = (total + tax)
    context = {
        'cart_items': cart_items,
        'quantity': quantity,
        'total': total,
        'tax': tax,
        'total_tex': total_tex,

    }
    return render(request, 'checkout.html', context)
