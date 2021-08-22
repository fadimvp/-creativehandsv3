# _*_ coding: utf-8 _*_
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image

# Create your models here.

User = settings.AUTH_USER_MODEL


#
# class ProductQuerySet(models.query.QuerySet):
#     def PRDName(self):
#         return self.filter(PRDName=False)
# class ProductManger (models.Manager):
#     def get_queryset(self):
#         return ProductQuerySet(self.model,using=self._db)
#     def all (self,*args,**kwargs):
#         return self.get_queryset().PRDName()
class Product(models.Model):
    # objects =ProductManger()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    PRDName = models.CharField(max_length=75)
    PRDVandor_Name = models.CharField(max_length=75)
    PRDCategory = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    PRDIMG = models.ImageField(upload_to='', blank=True, null=True)
    PRDDec = models.TextField(max_length=500)
    PRDBrand = models.ForeignKey('settings.Brand', on_delete=models.CASCADE, blank=True, null=True)
    PRDPrice = models.DecimalField(max_digits=5, decimal_places=2)
    PRDCost = models.DecimalField(max_digits=5, decimal_places=2)
    PRDDisc = models.DecimalField(max_digits=5, decimal_places=2)
    PRDSlug = models.SlugField(blank=True, null=True, allow_unicode=True)
    PRDCreated = models.DateTimeField()
    PRDISNew = models.BooleanField(default=False)
    PRDISbest = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    tax = models.DecimalField(max_digits=3, decimal_places=2, default=0.15)

    # Additional data
    on_sale = models.BooleanField(default=False)
    sale_date = models.BooleanField(default=True)
    on_sale_start = models.DateField(null=True, blank=True)
    on_sale_ends = models.DateField(null=True, blank=True)

    # admin data
    approved = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    limited_products = models.BooleanField(default=False)

    added_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, null=True)

    # Needs to Add Rating

    # Proprites
    weight = models.IntegerField(default=0, null=True)
    length = models.DecimalField(decimal_places=2, default=0, max_digits=100)
    height = models.DecimalField(decimal_places=2, default=0, max_digits=100)
    width = models.DecimalField(decimal_places=2, default=0, max_digits=100)

    def __str__(self):
        return str(self.PRDName)

    def save(self, *args, **kwargs):
        def save(self, *args, **kwargs):

            if not self.PRDSlug:
                self.PRDSlug = slugify(self.PRDVandor_Name)

                if not self.PRDSlug:
                    self.PRDSlug = self.arabic_slugify(self.PRDVandor_Name)

            super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return self.PRDName

    def save(self, *args, **kwargs):

        if not self.PRDSlug:
            self.PRDSlug = slugify(self.PRDVandor_Name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:pro_detail', kwargs={"slug": self.PRDSlug})


var_category_choice = (
    ("color", "color"),
    ("size","size"),

)

class VarationManger(models.Manager):
    def colors(self):
        return super(VarationManger,self).filter(variation_category='color',is_active=True)
    def sizes (self):
        return super(VarationManger,self).filter(variation_category='size',is_active=True)

class Variation(models.Model):
    product = models.ForeignKey(Product,blank=True,on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=var_category_choice)
    variation_vale = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now=True)
    objects = VarationManger()
    def __str__(self):
        return str(self.variation_vale)



    def get_absolute_url(self):
        return self.product.get_absolute_url()


def image_upoad_to(instance, filename):
    title = instance.PRDIProduct
    slug = slugify(title)
    file_extansion = filename.split(".")
    new_filename = "%s.%s"

    return "prod/%s/%s" % (slug, filename)


# def image_upoad_to(instance, filename):
#     imgname , extension =filename.split('.')
#     return "varimg/%s/%s"%(instance.id, extension)


class Product_Img(models.Model):
    PRDIProduct = models.ForeignKey(Product, on_delete=models.CASCADE)

    PRDImg = models.ImageField(upload_to=image_upoad_to)

    def __str__(self):
        return str(self.PRDIProduct)


class Category(models.Model):

    CATName = models.CharField(max_length=255)
    CATParent = models.ForeignKey('self', limit_choices_to={'CATParent__isnull': True}, on_delete=models.CASCADE,
                                  blank=True, null=True)
    CATDesc = models.TextField()
    slug = models.SlugField()
    CATImg = models.ImageField(upload_to='Category/')
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.CATImg.path)
        if img.width > 200 or img.height > 200:
            output_size =(200,200)
            img.thumbnail(output_size)
            img.save(self.CATImg.path)
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categoryios'

    def get_url(self):
        return reverse('products:category_slug', args={self.slug})


    def __str__(self):
        return self.CATName



class Alternative(models.Model):
    PALNProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='main_product')
    PLNAlternative = models.ManyToManyField(Product, related_name='alternative_products')

    def __str__(self):
        return self.PLNAlternative


class Product_Accessories(models.Model):
    PACCProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="PACCProduct")
    PACAlternative = models.ManyToManyField(Product, related_name="PACAlternative")

    def __str__(self):
        return str(self.PACCProduct)
