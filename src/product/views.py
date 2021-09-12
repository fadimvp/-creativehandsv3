from django.contrib import messages
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Product, Category, Variation, ReviewRating, Products_Language, Languagee, llist
from django.core.paginator import Paginator
from .models import Category
from .forms import SearchForm
from cart.models import CartItems
from cart.views import _cart_id
from .filters import Product_list_filter
from django.utils.translation import gettext as aa
from .forms import ReviewForm,MyForm
from django.db.models import Q


# Display  all products  and counts on Home page and category all
def Product_list(request):
    form1 = MyForm()
    language = Products_Language.objects.all()
    product_list = Product.objects.filter(approved=True).order_by(
        'id')  # Display  all products if you check in approved

    product_featured = Product.objects.filter(
        Q(featured=True) & Q(approved=True))  # Display  all products if you check in product_featured
    limited_products = Product.objects.filter(limited_products=True)
    limited_products = Product.objects.filter(limited_products=True)
    list = Languagee.objects.filter(status=True)
    list1 = []
    # for rs in llist:
    #     list1.append((rs.code, rs.name))
    # langlist = (list1)
    # if langlist.index['en','en']:
    #     print(langlist)
    # list2 = Product.objects.filter(lang=list1)
    # print(list2)

    # print(langlist, '############2')
    langar = Product.objects.filter(lang=Product.lang == 1)
    product_count = product_list.count()  # count all products
    d = Category.objects.all()  # display all category on home page
    # paginator
    paginator = Paginator(product_list, 6)  # product_list == how many products  display on one page
    page_number = request.GET.get('page')  # get number data
    product_list = paginator.get_page(page_number)

    context = {
        'product_list': product_list,
        'product_count': product_count,
        'product_featured': product_featured,
        'limited_products': limited_products,
        'Produts_language': language,
        'langar': langar,

        'd': d,
    }
    return render(request, 'product/product_list.html', context)


# if you selected show more display all products on home page
def All_products(request):
    product_list = Product.objects.all().order_by('id')
    product_count = product_list.count()
    d = Category.objects.all()
    paginator = Paginator(product_list, 1)  # product_list == how many products  display on one page
    page_number = request.GET.get('page')  # get number data
    product_list = paginator.get_page(page_number)

    context = {
        'product_list': product_list,
        'd': d,
        'product_count': product_count,
    }
    return render(request, 'product/all_products.html', context)


''' display all category and through date to url.py must send tow arg used data with models  def category 
get_url  '''


def category(request, category_slug):
    d = get_object_or_404(Category, slug=category_slug)

    context = {
        'd': d
    }

    return render(request, 'product/product_list.html', context)


def Product_detail(request, slug):
    # pro_detail = Product.objects.get(slug=slug)
    pro_detail = get_object_or_404(Product, PRDSlug=slug)
    d = Category.objects.all()
    in_cart = CartItems.objects.filter(cart__cart_id=_cart_id(request), product=pro_detail).exists()

    context = {
        'pro_detail': pro_detail,
        'd': d,
        'in_cart': in_cart,

    }
    return render(request, 'product/singlpage.html', context)


def tt(request, slug):
    pro_detail = get_object_or_404(Product, PRDSlug=slug)
    d = Category.objects.all()
    in_cart = CartItems.objects.filter(cart__cart_id=_cart_id(request), product=pro_detail).exists()

    context = {
        'pro_detail': pro_detail,
        'd': d,
        'in_cart': in_cart,

    }
    return render(request, 'product/tt.html', context)


# store :  any  products under category  and  slug
def store(request, category_slug=None):
    categories = None
    product_list = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        product_list = Product.objects.filter(PRDCategory=categories, approved=True)
        product_count = product_list.count()
        d = Category.objects.all()
        paginator = Paginator(product_list, 1)  # product_list == how many products  display on one page
        page_number = request.GET.get('page')  # get number data
        product_list = paginator.get_page(page_number)

    else:
        product_list = Product.objects.all().filter(approved=True).order_by('id')
        product_count = product_list.count()
        d = Category.objects.all()

        paginator = Paginator(product_list, 1)  # product_list == how many products  display on one page
        page_number = request.GET.get('page')  # get number data
        product_list = paginator.get_page(page_number)

    context = {
        'product_list': product_list,
        'product_count': product_count,
        'd': d,

    }
    return render(request, 'product/store.html', context)


# search  method  if you want search  about products inside one category
def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']  # get  data from input query name from  base.html
            catid = form.cleaned_data['catid']  # get  data from input select element   base.html
            if catid == 0:  # condition  if catid value = "0"  display  all products
                product_list = Product.objects.filter(PRDName__icontains=query, approved=True)
            else:
                product_list = Product.objects.filter(PRDName__icontains=query, PRDCategory_id=catid, approved=True)
            d = Category.objects.all()
            context = {
                'product_list': product_list,
                'd': d,
            }

            return render(request, 'product/product_list.html', context)
    return HttpResponseRedirect(
        '/')  # if you do search  other page same page details or anther page back to display all products in home page


def submit_review(request, product_id):
    print("any=======================")
    url = request.META.get('HTTP_REFERER')
    print(url)
    if request.method == 'POST':

        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, ' dsdsdsdsd')
            return redirect(url)

        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.review = form.cleaned_data['review']
                data.r = form.cleaned_data['rating']
                data.user_id = request.user.id
                data.product_id = product_id
                data.ip = request.META.get('REMOTE_ADDR')
                data.save()
                messages.success(request, 'SUECCESS')
                return redirect(url)

