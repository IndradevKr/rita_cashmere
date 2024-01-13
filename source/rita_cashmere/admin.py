from django.contrib import admin

from django.contrib import admin
from .models import Product, Contact, SEO_META, About, Blog, CompanyInfo, Order, CarouselImage , ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    search_fields = ['category_name']
    list_display= ['category_name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_id', 'product_code', 'product_category','product_fabric', 'product_weight', 'product_price_dollar')
    search_fields = ['product_id', 'product_code', 'product_name', 'product_category' ]
    
admin.site.register(Product, ProductAdmin)

admin.site.register(SEO_META)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_uploaded_date')  
    search_fields= ['blog_title']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')  
    search_fields= ['name', 'email', 'phone']

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('company_phone', 'company_email', 'company_address')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'name', 'amount', 'email',  'address', 'phone')
    search_fields = ['order_id', 'name', 'name', 'email', 'phone']

admin.site.register(About)
admin.site.register(CarouselImage)