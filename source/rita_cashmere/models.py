from email.policy import default
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class CarouselImage(models.Model):
    image_one = models.ImageField(upload_to="uploaded_carousel_image/", blank=True, null=True)
    image_one_alt = models.CharField(max_length=100, blank=True, null=True)
    image_two = models.ImageField(upload_to="uploaded_carousel_image/", blank=True, null=True)
    image_two_alt = models.CharField(max_length=100, blank=True, null=True)    
    image_three = models.ImageField(upload_to="uploaded_carousel_image/", blank=True, null=True)
    image_three_alt = models.CharField(max_length=100, blank=True, null=True)
    image_four = models.ImageField(upload_to="uploaded_carousel_image/", blank=True, null=True)
    image_four_alt = models.CharField(max_length=100, blank=True, null=True)
    

class ProductCategory(models.Model):
    slug = models.CharField(max_length=150)
    category_name = models.CharField(max_length=100, default='')
    image= models.ImageField(upload_to="uploaded_category_image/")
    meta_title= models.CharField(max_length=150, blank=True, null=True)
    meta_keywords= models.CharField(max_length=150, blank=True, null=True)
    meta_descriptions= models.CharField(max_length=150, blank=True, null=True)
    
    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural= "Product Categories"

    def __str__(self):
        return self.category_name 
    
class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    slug = models.CharField(max_length=150)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_image_front= models.ImageField(upload_to='uploaded_product_images/')
    product_image_back=models.ImageField(upload_to='uploaded_product_images/', blank=True, null=True)
    product_image_left=models.ImageField(upload_to='uploaded_product_images/', blank=True, null=True)
    product_image_right=models.ImageField(upload_to='uploaded_product_images/', blank=True, null=True)
    product_name = models.CharField(max_length=200)
    product_category = models.CharField(max_length=100, default='')
    product_price_dollar = models.DecimalField(max_digits=10, decimal_places=2)
    product_price_eur = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_fabric= models.CharField(max_length=200)
    product_code= models.CharField(max_length=100)
    product_weight = models.CharField(max_length=50)
    product_color = models.CharField(max_length=100, blank=True, null=True)
    product_description = models.TextField()
    product_available_sizes = models.CharField(max_length=200, null=True, blank=True)
    product_blog_url = models.CharField(max_length=500, null=True, blank=True)
    product_yarn_count = models.CharField(max_length=50, blank=True, null=True)
    product_yarn_ply = models.CharField(max_length=50, blank=True, null=True)
    product_style = models.CharField(max_length=50, blank=True, null= True)
    product_origin = models.CharField(max_length=50, blank=True, null=True)
    product_knit_guage = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.product_name 

class SEO_META(models.Model):
    meta_keywords = models.TextField(null=True, blank=True)
    meta_descriptions = models.TextField(null=True, blank=True)

    class Meta:
         verbose_name = "SEO META"
         verbose_name_plural= "SEO METAS"

class Blog(models.Model):
    blog_id= models.BigAutoField(primary_key=True)
    slug = models.CharField(max_length=150)
    blog_title= models.CharField(max_length=500)
    blog_image = models.ImageField(upload_to='uploaded_blog_images/', blank=True, null=True)
    blog_image_alt=models.CharField(max_length=150, default="rita cashmere industries best known for knitted products")
    blog_content = RichTextUploadingField()
    blog_author= models.CharField(max_length=100, blank=True, null=True)
    blog_uploaded_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title

class CompanyInfo(models.Model):
    company_phone = models.CharField(max_length=50)
    company_optional_phone = models.CharField(max_length=50, blank=True, null=True)
    company_email = models.EmailField(default="")
    company_address = models.CharField(max_length=200)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email= models.EmailField()
    message= models.TextField()
    phone=models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id= models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    amount=models.IntegerField()
    name=models.CharField(max_length=200)
    email=models.EmailField()
    address=models.CharField(max_length=255)
    state=models.CharField(max_length=200)
    zip_code=models.CharField(max_length=100)
    phone=models.CharField(max_length=16, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name

class About(models.Model):
    about_image_one = models.ImageField(upload_to='uploaded_about_image/')
    about_image_one_alt= models.CharField(max_length=100, default="rita-cashmere")
    about_text_one = RichTextUploadingField()
    about_image_two = models.ImageField(upload_to='uploaded_about_image/', blank=True, null=True)
    about_image_two_alt= models.CharField(max_length=100, blank=True, null=True, default="")
    about_text_two = RichTextUploadingField(blank=True, null=True)
    about_image_three = models.ImageField(upload_to='uploaded_about_image/', blank=True, null=True)
    about_image_three_alt= models.CharField(max_length=100, default="", blank=True, null=True)
    about_text_three = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.about_text_one
