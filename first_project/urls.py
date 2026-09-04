

from django.contrib import admin
from django.urls import path
from zepto import views
from django.shortcuts import render
from zepto import views as appview
from myapp import views as myview


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.homepage),
    path('', views.defaultpage),
    path('login/', views.login),
    path('service/', views.service),
    path('index/', views.index_page),
    path('zepto/', views.zepto),
    path('zepto/',appview.zeptopage),
    path('myapp/',myview.mypage),
    path('recipes/',views.getrecipes),
]