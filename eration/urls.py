from django.http import request
from django.urls import path
from eration import views

urlpatterns = [
    path('',views.index),
    path('index/',views.index),
    path('login/',views.loginuser),
    path('home/',views.homeuser),
    path('about/',views.aboutpage),
    path('products/',views.productpage),
    path('services/',views.servicespage),
    path('mail/',views.mailpage),
    path('household/',views.householdpage),
    path('vegetables/',views.vegetablespage),
    path('kitchen/',views.kitchenpage),
    path('subscribe/',views.subscribe),
    path('single/',views.singleproduct),
    path('productlist/',views.productlist),
    path('addproduct/',views.addproduct),
    ]