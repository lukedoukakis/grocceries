from django.shortcuts import render

from django.http import HttpResponse
from myapp import models

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def simple_function(request):
    print("\nthis is a simple function\n")
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

# adds an item to the database - for now, hardcoded as a banana
def add_item(request):
    models.add_item('1234', 'banana', 1.5)
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")