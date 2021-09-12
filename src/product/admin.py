from django.contrib import admin
from .models import Product, Product_Img, Category,Variation, Alternative, Product_Accessories,ReviewRating, Products_Language,Setting,Settinglang,Languagee




# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('CATName',)}
    list_display = ('CATName', 'slug')
class  langAdmin(admin.ModelAdmin):
    list_display = ['name','code','status']
    list_filter = ['status']



class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", 'user', "PRDName", "PRDPrice", "PRDDisc", "PRDCost", "stock", "PRDCreated", "PRDIMG")
    list_display_links = ("id", 'user', "PRDName", "PRDPrice", "PRDDisc",)
    search_fields = ("PRDName", "user")
    list_editable = ('stock',)


class VariationAdmin(admin.ModelAdmin):
    list_display = ['product','variation_category','variation_vale','is_active']
    list_editable = ('is_active',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation,VariationAdmin)
admin.site.register(Product_Img)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Alternative)
admin.site.register(ReviewRating)
admin.site.register(Products_Language)

admin.site.register(Setting)
admin.site.register(Languagee,langAdmin)
admin.site.register(Settinglang)
# admin.site.register(Product_Accessories)
