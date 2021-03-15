from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def homepage(request):
    return render(request, 'myapp/index.html') 

def accountInfoPage(request):
    return render(request, 'profile/accountinfo.html')

def registerPage(request):
    return render(request, 'account/registered.html')


def storeFinderPage(request):
    return render(request, 'map/storelocator.html')


def simple_function(request):
    print("\nthis is a simple function\n")
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")


def add_account_submission(request):
    print("form is submitted")
    userEmail = request.POST["userEmail"]
    return render(request, 'registered.html')
