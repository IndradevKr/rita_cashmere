from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
from .forms import OrderForm, ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from captcha.fields import ReCaptchaField
from django.db.models import Q


def index(request):
    template = loader.get_template("rita_cashmere/index.html")
    carousel_images = CarouselImage.objects.all()[0]
    category_items = ProductCategory.objects.all()[:12]
    latest_products = Product.objects.all()[:12]
    context = {
        "carousel_images": carousel_images,
        "category_items": category_items,
        "latest_products": latest_products,
    }
    return HttpResponse(template.render(context, request))


def collections(request):
    template = loader.get_template("rita_cashmere/collections.html")
    search_query = request.GET.get('q')
    categories_list = ProductCategory.objects.all().order_by('category_name')
    
    if search_query:
        categories_list = categories_list.filter(Q(category_name__icontains=search_query)| Q(category_name__icontains=search_query.split())).order_by('category_name')

    paginator = Paginator(categories_list, 12)
    page = request.GET.get('page')
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    context = {"categories": categories}
    if not categories:
        return render(request, "rita_cashmere/not-found.html")

    return HttpResponse(template.render(context, request))


def collectionsView(request, slug):
    template = loader.get_template("rita_cashmere/products.html")
    if ProductCategory.objects.filter(slug=slug):
        products_list = Product.objects.filter(category__slug=slug)
        category_name = ProductCategory.objects.filter(slug=slug).first()

        paginator = Paginator(products_list, 12)
        page = request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
       
        context = {
            "products": products,
            "category_name": category_name,
            }
        return render(request, "rita_cashmere/products.html", context)
    else:
        return render(request, "rita_cashmere/not-found.html")


def contact(request):
    company = CompanyInfo.objects.all()[0]
    try:
        if request.method =="POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.save()
                return render(request, "rita_cashmere/contact_success.html")
        else:
            form=ContactForm()
    except Exception as e:
        print(e)
    return render(request, "rita_cashmere/contact.html", {"form": form, "company": company})

def blogs(request):
    latest_blog = Blog.objects.latest('blog_uploaded_date')
    blogs = Blog.objects.exclude(pk=latest_blog.pk)
    context = {
        "latest_blog":latest_blog,
        "blogs": blogs,
    }
    return render(request, "rita_cashmere/blogs.html", context)

def blog_details(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
        context = {
            "blog": blog,
        }
        return render(request, "rita_cashmere/blog_details.html", context)
    
    except Exception as e:
        print(e)

def about(request):
    about_details = About.objects.all()[0]
    context = {"about": about_details}
    return render(request, "rita_cashmere/about.html", context)


def place_order(request, product_id):
    try:
        product = Product.objects.get(product_id=product_id)
        if request.method == "POST":
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.product = product
                order.save()
                # redirect to a success page
                return render(request, "rita_cashmere/contact_success.html")
        else:
            form = OrderForm()
    except Exception as e:
        print(e)

    return render(
        request, "rita_cashmere/order.html", {"form": form, "product": product}
    )
