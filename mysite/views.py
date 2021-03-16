from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def homepage(request):
    return render(request, 'login.html')


def accountInfoPage(request):
    return render(request, 'accountinfo.html')

<<<<<<< Updated upstream
# def registerPage(request):
#     return render(request, 'registered.html')
=======

def registerPage(request):
    return render(request, 'registered.html')
>>>>>>> Stashed changes


def storeFinderPage(request):
    return render(request, 'storelocator.html')


def simple_function(request):
    print("\nthis is a simple function\n")
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
