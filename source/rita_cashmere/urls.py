from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.index, name="index"),
    path("collections/", views.collections, name="collections"),
    path("collections/<str:slug>/", views.collectionsView, name="collectionsView"),
    path('order/<int:product_id>/', views.place_order, name="order"),
    path('contact/', views.contact, name='contact'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<slug:slug>', views.blog_details, name='blog_details'),
    path("about/", views.about, name="about")
]
