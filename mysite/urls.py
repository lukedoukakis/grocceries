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
from django.urls import path, re_path, include
from register import views as vr
from . import views
from store import views as viewstore
from core import views as views_core
from storelocator import views as views_storelocator

urlpatterns = [
    re_path(r'^$', views.homepage, name='home'),
    re_path(r'^register/$', vr.register, name='register'),
    re_path(r'^storeLocator/$', views_storelocator.storeLocatorPage, name='storeLocator'),
    re_path(r'^account/$', views.accountInfoPage, name='account'),
    re_path(r'^logout/$', views.logout, name='logout'),
    # [a-zA-Z0-9~@#$^*()_+=[\]{}|\\,.?: -]
    re_path(r'^storepage/(?P<storeIdentifier>[\w\-]+)/(?P<searchTerm>.+)/$', viewstore.storePage, name='storepage'),
    re_path(r'^itempage/(?P<itemIdentifier>[\w\-]+)/$', views.itemPage, name='itempage'),
    re_path(r'^cardpayment/$', views.paymentPage, name='cardpayment'),
    
    path('add-to-cart/', viewstore.add_to_cart),
    path('admin/', admin.site.urls),
    path("simple_function", views.simple_function),
    path("get_vendors", views_core.get_vendors),
    path("get_items", views_core.get_items),
    path("get_items_global", views_core.get_items_global),

    path('', include("django.contrib.auth.urls")),

]
