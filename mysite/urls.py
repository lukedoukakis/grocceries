"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from . import views
from core import views as views_core

urlpatterns = [
    re_path(r'^$', views.homepage, name='home'),
    re_path(r'^register/$', views.registerPage, name='register'),
    re_path(r'^add_account_submission/$', views.add_account_submission, name='add_account_submission'),
    re_path(r'^storeLocator/$', views.storeFinderPage, name='storeFinder'),
    re_path(r'^account/$', views.accountInfoPage, name='account'),
    path('admin/', admin.site.urls), 
    path("simple_function", views.simple_function),
    path("get_vendors", views_core.get_vendors),
    path("get_items", views_core.get_items),
    path("get_items_global", views_core.get_items_global)

]
